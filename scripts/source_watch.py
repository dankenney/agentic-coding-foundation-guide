#!/usr/bin/env python3
"""Fetch public source evidence for human review; never rewrite guide content."""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
from http.client import HTTPException
import json
from pathlib import Path
import sys
from urllib.error import HTTPError, URLError
from urllib.request import HTTPRedirectHandler, Request, build_opener

from check_guide import REGISTRY_PATH, public_source_url_error, registry_errors


MAX_BYTES = 4 * 1024 * 1024


def permitted_url(url: str) -> bool:
    return public_source_url_error(url) is None


class PublicHTTPSRedirects(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        if not permitted_url(newurl):
            raise URLError("redirect blocked: " + public_source_url_error(newurl))
        return super().redirect_request(req, fp, code, msg, headers, newurl)


def fetch_evidence(source: dict, timeout: float, opener=None) -> dict:
    """Return network facts. A content digest is emitted only after a complete read."""
    result = {"id": source["id"], "url": source["url"], "fetch_ok": False}
    if not permitted_url(source["url"]):
        result["error"] = "source URL " + public_source_url_error(source["url"])
        return result
    opener = opener or build_opener(PublicHTTPSRedirects())
    try:
        request = Request(source["url"], headers={"User-Agent": "AgenticCodingFoundation-SourceWatch/1.0", "Accept": "text/html,text/plain,application/json;q=0.9,*/*;q=0.5"}, method="GET")
        with opener.open(request, timeout=timeout) as response:
            result.update({"status": response.status, "final_url": response.geturl(), "content_type": response.headers.get("Content-Type"), "etag": response.headers.get("ETag"), "last_modified": response.headers.get("Last-Modified")})
            if not permitted_url(response.geturl()):
                result["error"] = "final URL is not an allowed public source"
                return result
            body = response.read(MAX_BYTES + 1)
            result["bytes_read"] = len(body)
            if len(body) > MAX_BYTES:
                result["error"] = f"response exceeds {MAX_BYTES} byte limit; digest omitted"
                return result
            # HTTPResponse.read(amt) can return an early EOF without raising
            # IncompleteRead. Do not hash a declared body that arrived partly.
            declared_length = response.headers.get("Content-Length")
            chunked = "chunked" in response.headers.get("Transfer-Encoding", "").lower()
            if declared_length is not None and not chunked:
                try:
                    expected = int(declared_length)
                except ValueError:
                    expected = -1
                if expected < 0 or len(body) != expected:
                    result["error"] = f"incomplete or invalid response length: received {len(body)} bytes, declared {declared_length}; digest omitted"
                    return result
            result["sha256"] = hashlib.sha256(body).hexdigest()
            result["fetch_ok"] = 200 <= response.status < 300
            if not result["fetch_ok"]:
                result["error"] = f"unexpected HTTP status {response.status}"
    except HTTPError as exc:
        result.update({"status": exc.code, "final_url": exc.geturl(), "error": f"HTTP {exc.code}: {exc.reason}"})
    except (URLError, TimeoutError, OSError, HTTPException, UnicodeError, ValueError) as exc:
        result["error"] = str(exc)
    return result


def review_evidence(source: dict, fetch: dict, previous: dict | None, today: dt.date) -> dict:
    """Separate freshness of a human review from availability or byte changes."""
    verified = dt.date.fromisoformat(source["last_verified"])
    due = verified + dt.timedelta(days=source["review_after_days"])
    result = {**fetch, "last_verified": source["last_verified"], "review_due_on": due.isoformat(), "review_due": today >= due, "used_in": source["used_in"]}
    if not fetch.get("fetch_ok"):
        result["comparison"] = "fetch_failed"
    elif not previous or previous.get("url") != source["url"] or not previous.get("sha256"):
        result["comparison"] = "no_baseline"
    elif previous["sha256"] != fetch.get("sha256"):
        result["comparison"] = "content_bytes_changed"
    elif previous.get("final_url") != fetch.get("final_url"):
        result["comparison"] = "redirect_changed"
    else:
        result["comparison"] = "same_content_bytes"
    result["redirect_changed"] = bool(previous and previous.get("final_url") and previous["final_url"] != fetch.get("final_url"))
    return result


def load_baseline(path: Path | None) -> dict[str, dict]:
    if path is None:
        return {}
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict) or not isinstance(data.get("sources"), list):
        raise ValueError("baseline must be a source-watch JSON report with a sources list")
    result = {}
    for source in data["sources"]:
        if not isinstance(source, dict) or not isinstance(source.get("id"), str):
            raise ValueError("baseline source entries must have string ids")
        if source["id"] in result:
            raise ValueError("baseline contains duplicate source ids")
        result[source["id"]] = source
    return result


def report_output_path(root: Path, requested: Path) -> Path:
    """Reports are new files in scratch/report folders or explicit external paths."""
    path = (requested if requested.is_absolute() else root / requested).resolve()
    if path.suffix.lower() != ".json":
        raise ValueError("--output must name a new .json evidence report")
    try:
        relative = path.relative_to(root.resolve())
    except ValueError:
        if not requested.is_absolute():
            raise ValueError("relative --output must stay inside repository work/ or reports/")
    else:
        if not relative.parts or relative.parts[0] not in {"work", "reports"}:
            raise ValueError("--output inside the repository must be in work/ or reports/")
    if path.exists() or path.is_symlink():
        raise ValueError("--output must be a new file; existing files and baselines are never overwritten")
    return path


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--baseline", type=Path, help="previous JSON report for byte and redirect comparison")
    parser.add_argument("--output", type=Path, help="create a new JSON report in work/ or reports/, or at an absolute external path; never overwrite")
    parser.add_argument("--timeout", type=float, default=12, help="per-request socket timeout in seconds, 1 to 30 (default: 12)")
    parser.add_argument("--only", action="append", default=[], metavar="SOURCE_ID", help="fetch only this registry id; repeat for multiple ids")
    args = parser.parse_args(argv)
    if not 1 <= args.timeout <= 30:
        parser.error("--timeout must be between 1 and 30 seconds")
    try:
        output_path = report_output_path(args.root, args.output) if args.output else None
    except ValueError as exc:
        parser.error(str(exc))
    errors = registry_errors(args.root)
    if errors:
        print("Source registry is invalid:\n  " + "\n  ".join(errors), file=sys.stderr)
        return 2
    registry = json.loads((args.root / REGISTRY_PATH).read_text(encoding="utf-8"))
    try:
        baseline = load_baseline(args.baseline)
    except (OSError, UnicodeError, ValueError, json.JSONDecodeError) as exc:
        print(f"Cannot read baseline: {exc}", file=sys.stderr)
        return 2
    known = {source["id"] for source in registry["sources"]}
    unknown = set(args.only) - known
    if unknown:
        parser.error("unknown source ids: " + ", ".join(sorted(unknown)))
    now = dt.datetime.now(dt.timezone.utc)
    report = {"checked_at": now.isoformat(timespec="seconds"), "registry_checked_on": registry["checked_on"], "meaning": "Fetches and byte changes are review evidence only. They do not establish that guidance changed, remains correct, or should be adopted. last_verified changes only after human review.", "network_scope": "An operator curates the registry. URL checks reject obvious private hosts and literal IPs; they do not resolve DNS or provide SSRF isolation.", "sources": []}
    for source in registry["sources"]:
        if args.only and source["id"] not in args.only:
            continue
        evidence = review_evidence(source, fetch_evidence(source, args.timeout), baseline.get(source["id"]), now.date())
        report["sources"].append(evidence)
        freshness = "review due" if evidence["review_due"] else f"review due {evidence['review_due_on']}"
        print(f"{source['id']}: {evidence['comparison']}; {freshness}; HTTP {evidence.get('status', 'unavailable')}", flush=True)
        if evidence.get("error"):
            print(f"  {evidence['error']}", flush=True)
    if output_path:
        try:
            output_path.parent.mkdir(parents=True, exist_ok=True)
            with output_path.open("x", encoding="utf-8") as output_file:
                output_file.write(json.dumps(report, indent=2, ensure_ascii=False) + "\n")
        except OSError as exc:
            print(f"Cannot create evidence report: {exc}", file=sys.stderr)
            return 2
        print(f"Evidence written to {output_path}")
    print("Human review is required; this command changes no guide content, review dates or remote state.")
    return 1 if any(not source["fetch_ok"] for source in report["sources"]) else 0


if __name__ == "__main__":
    raise SystemExit(main())
