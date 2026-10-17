#!/usr/bin/env python3
"""Check the guide's links, portable content and source registry using Python only."""

from __future__ import annotations

import argparse
import datetime as dt
from html import unescape
import ipaddress
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit


SKIP_DIRECTORIES = {".git", ".venv", "__pycache__", "node_modules", "work", "outputs"}
REGISTRY_PATH = Path("maintenance/source-watch.json")
HTML_TAG_PATTERN = r"<[a-z](?:[^>\"']|\"[^\"]*\"|'[^']*')*>"


def markdown_unescape(value: str) -> str:
    """Decode the escapes Markdown permits in labels and destinations."""
    return unescape(re.sub(r"\\([!-/:-@\[-`{-~])", r"\1", value))


def private_note_url(url: str) -> bool:
    try:
        hostname = unquote(urlsplit(markdown_unescape(url).rstrip(").,;:!?]}")).hostname or "").rstrip(".").lower()
    except ValueError:
        return False
    return any(hostname == domain or hostname.endswith("." + domain) for domain in ("notion.so", "notion.site", "notion.com"))


def public_source_url_error(url: object) -> str | None:
    """Reject obvious private targets; an operator curates URLs, not a DNS sandbox."""
    if not isinstance(url, str):
        return "must be an https URL without credentials"
    if any(char.isspace() or ord(char) < 32 or ord(char) == 127 for char in url):
        return "must not contain unescaped whitespace or control characters"
    try:
        parsed = urlsplit(url)
        hostname = (parsed.hostname or "").rstrip(".").lower()
        if parsed.scheme != "https" or not hostname or parsed.username or parsed.password:
            return "must be an https URL without credentials"
        # Accessing .port also checks malformed port syntax.
        if parsed.port is not None and not 1 <= parsed.port <= 65535:
            return "must use a valid port"
        if any(hostname == domain or hostname.endswith("." + domain) for domain in ("notion.so", "notion.site", "notion.com")):
            return "private Notion URLs are not source-watch targets"
        try:
            address = ipaddress.ip_address(hostname)
        except ValueError:
            address = None
        if address is not None:
            if not address.is_global or address.is_multicast:
                return "must not target loopback, private or reserved IP addresses"
            return None
        special_hosts = ("localhost", "local", "internal", "intranet", "lan", "corp", "home", "home.arpa", "test", "invalid", "example", "onion")
        if any(hostname == suffix or hostname.endswith("." + suffix) for suffix in special_hosts):
            return "must not target local or special-use hostnames"
        ascii_host = hostname.encode("idna").decode("ascii")
        labels = ascii_host.split(".")
        if len(labels) < 2 or not re.fullmatch(r"[a-z][a-z0-9-]*", labels[-1]) or any(not re.fullmatch(r"[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?", label) for label in labels):
            return "must name a public hostname or global IP address"
    except (ValueError, UnicodeError):
        return "must be a valid https URL without credentials"
    return None


def without_code(text: str) -> str:
    """Keep line numbers stable while removing fenced code and HTML comments."""
    text = re.sub(r"<!--.*?-->", lambda m: "\n" * m.group().count("\n"), text, flags=re.S)
    lines = text.splitlines()
    fence = None
    for number, line in enumerate(lines):
        match = re.match(r"^\s{0,3}(`{3,}|~{3,})", line)
        if match:
            marker = match.group(1)
            if fence is None:
                fence = marker
            elif marker[0] == fence[0] and len(marker) >= len(fence):
                fence = None
            lines[number] = ""
        elif fence is not None:
            lines[number] = ""
    return "\n".join(lines)


def heading_anchors(text: str) -> set[str]:
    """Use GitHub's common heading slug rules, including duplicate headings."""
    text = without_code(text)
    anchors = set()
    for tag in re.finditer(HTML_TAG_PATTERN, without_inline_code(text), re.I):
        for match in re.finditer(r"\b(?:id|name)\s*=\s*(?:\"([^\"]*)\"|'([^']*)'|([^\s`=<>\"']+))", tag.group(), re.I):
            anchors.add(unescape(next(value for value in match.groups() if value is not None)))
    counts: dict[str, int] = {}
    headings = []
    lines = text.splitlines()
    for number, line in enumerate(lines):
        match = re.match(r"^\s{0,3}#{1,6}\s+(.+?)\s*#*\s*$", line)
        if match:
            headings.append(match.group(1))
        elif number and re.match(r"^\s{0,3}(?:=+|-+)\s*$", line) and lines[number - 1].strip():
            headings.append(lines[number - 1].strip())
    for heading in headings:
        heading = re.sub(r"<[^>]*>", "", heading)
        heading = re.sub(r"!?\[([^\]]*)\]\([^)]*\)", r"\1", heading)
        heading = unescape(heading).lower()
        slug = "".join(char for char in heading if char.isalnum() or char in " _-")
        slug = slug.replace(" ", "-")
        count = counts.get(slug, 0)
        counts[slug] = count + 1
        candidate = f"{slug}-{count}" if count else slug
        # A literal heading may collide with the suffix of an earlier heading.
        while candidate in anchors:
            count += 1
            counts[slug] = count + 1
            candidate = f"{slug}-{count}"
        anchors.add(candidate)
    return anchors


def escaped_at(text: str, position: int) -> bool:
    count = 0
    while position > 0 and text[position - 1] == "\\":
        count += 1
        position -= 1
    return count % 2 == 1


def without_inline_code(text: str) -> str:
    """Mask matched backtick runs while retaining offsets and line numbers."""
    runs = list(re.finditer(r"`+", text))
    characters = list(text)
    index = 0
    while index < len(runs):
        opening = runs[index]
        if escaped_at(text, opening.start()):
            index += 1
            continue
        closing = next((other for other in range(index + 1, len(runs)) if len(runs[other].group()) == len(opening.group())), None)
        if closing is None:
            index += 1
            continue
        for position in range(opening.start(), runs[closing].end()):
            if characters[position] != "\n":
                characters[position] = " "
        index = closing + 1
    return "".join(characters)


def closing_bracket(text: str, opening: int) -> int | None:
    depth = 1
    for position in range(opening + 1, len(text)):
        if escaped_at(text, position):
            continue
        if text[position] == "[":
            depth += 1
        elif text[position] == "]":
            depth -= 1
            if not depth:
                return position
    return None


def inline_destination(text: str, opening: int) -> tuple[str, int] | None:
    """Read a balanced destination and optional title, including line breaks."""
    position = opening + 1
    while position < len(text) and text[position].isspace():
        position += 1
    start = position
    if position < len(text) and text[position] == "<":
        position += 1
        start = position
        while position < len(text) and (text[position] != ">" or escaped_at(text, position)):
            if text[position] in "\r\n":
                return None
            position += 1
        if position == len(text):
            return None
        destination = text[start:position]
        position += 1
    else:
        depth = 0
        while position < len(text):
            char = text[position]
            if not escaped_at(text, position):
                if char == "(":
                    depth += 1
                elif char == ")":
                    if not depth:
                        return markdown_unescape(text[start:position]), position + 1
                    depth -= 1
                elif char.isspace() and not depth:
                    break
            position += 1
        destination = text[start:position]
    before_space = position
    while position < len(text) and text[position].isspace():
        position += 1
    if position < len(text) and text[position] == ")":
        return markdown_unescape(destination), position + 1
    if position == before_space or position == len(text) or text[position] not in "\"'(":
        return None
    ending = ")" if text[position] == "(" else text[position]
    position += 1
    while position < len(text) and (text[position] != ending or escaped_at(text, position)):
        position += 1
    position += 1
    while position < len(text) and text[position].isspace():
        position += 1
    if position < len(text) and text[position] == ")":
        return markdown_unescape(destination), position + 1
    return None


def markdown_links(text: str) -> list[tuple[int, str]]:
    """Extract common inline, reference and HTML links outside code samples."""
    text = without_inline_code(without_code(text))
    definitions: dict[str, str] = {}
    links: list[tuple[int, str]] = []
    lines = text.splitlines(keepends=True)
    offset = 0
    characters = list(text)
    def reference_key(value: str) -> str:
        return re.sub(r"\s+", " ", markdown_unescape(value).strip()).casefold()
    for number, line in enumerate(lines, 1):
        match = re.match(r"^\s{0,3}\[([^\]]+)\]:\s*(<[^>]+>|\S+)", line)
        if match:
            key = reference_key(match.group(1))
            destination = markdown_unescape(match.group(2).strip("<>"))
            # CommonMark uses the first definition of a reference label.
            definitions.setdefault(key, destination)
            links.append((number, destination))
            for position in range(offset, offset + len(line)):
                if characters[position] != "\n":
                    characters[position] = " "
        offset += len(line)
    text = "".join(characters)
    position = 0
    while position < len(text):
        if text[position] != "[" or escaped_at(text, position):
            position += 1
            continue
        closing = closing_bracket(text, position)
        if closing is None:
            position += 1
            continue
        number = text.count("\n", 0, position) + 1
        label = text[position + 1:closing]
        after = closing + 1
        if after < len(text) and text[after] == "(":
            destination = inline_destination(text, after)
            if destination is not None:
                links.append((number, destination[0]))
                position = destination[1]
                continue
        if after < len(text) and text[after] == "[":
            reference_end = closing_bracket(text, after)
            if reference_end is None:
                position = closing + 1
                continue
            key = reference_key(text[after + 1:reference_end] or label)
            if key in definitions:
                links.append((number, definitions[key]))
            else:
                links.append((number, f"missing-reference:{key}"))
            position = reference_end + 1
        else:
            key = reference_key(label)
            if key in definitions:
                links.append((number, definitions[key]))
            position = closing + 1
    for tag in re.finditer(HTML_TAG_PATTERN, text, re.I):
        for attribute in re.finditer(r"\b(?:href|src)\s*=\s*(?:\"([^\"]*)\"|'([^']*)'|([^\s`=<>\"']+))", tag.group(), re.I):
            number = text.count("\n", 0, tag.start() + attribute.start()) + 1
            links.append((number, next(value for value in attribute.groups() if value is not None)))
    return links


def local_destination(root: Path, source: Path, destination: str) -> tuple[Path | None, str, str | None]:
    if destination.startswith("missing-reference:"):
        return None, "", f"undefined Markdown reference {destination.split(':', 1)[1]!r}"
    try:
        parsed = urlsplit(unescape(destination))
    except ValueError:
        return None, "", f"invalid link {destination!r}"
    if parsed.scheme or parsed.netloc:
        return None, "", None
    decoded = unquote(parsed.path).replace("\\", "/")
    target = (root / decoded.lstrip("/")) if decoded.startswith("/") else (source.parent / decoded)
    target = target.resolve() if decoded else source.resolve()
    try:
        target.relative_to(root.resolve())
    except ValueError:
        return None, "", f"link escapes repository: {destination!r}"
    if target.is_dir():
        target = target / "README.md"
    return target, unquote(parsed.fragment), None


def content_errors(relative: Path, text: str) -> list[str]:
    errors = []
    # Scan prose and examples, because portable examples must also be safe to copy.
    forbidden = [
        (r"\bclaude[\s_-]*code\b|\bclaude\.md\b|\bcc-foundation\b|\bcc-specific\b|\bcc\b", "legacy tool reference"),
        (r"(?:[A-Za-z]:[\\/]Users[\\/]|/Users/[^/\s]+/|/home/[^/\s]+/|(?:library|project)-file:|plugin://|codex://)", "local/client artifact"),
    ]
    for pattern, description in forbidden:
        for match in re.finditer(pattern, text, re.I):
            line = text.count("\n", 0, match.start()) + 1
            errors.append(f"{relative.as_posix()}:{line}: {description}")
    # Scan examples as well as prose, decoding Markdown/HTML URL spelling.
    for number, line in enumerate(text.splitlines(), 1):
        decoded = markdown_unescape(line)
        for match in re.finditer(r"(?:https?:)?//[^\s<>\"']+", decoded, re.I):
            if private_note_url(match.group()):
                errors.append(f"{relative.as_posix()}:{number}: private Notion reference")
    if re.search(r"(?:claude|cc-foundation)", relative.as_posix(), re.I):
        errors.append(f"{relative.as_posix()}: legacy tool filename")
    return errors


def registry_errors(root: Path, registry_path: Path = REGISTRY_PATH) -> list[str]:
    path = root / registry_path
    prefix = registry_path.as_posix()
    errors = []
    if not path.is_file():
        return [f"{prefix}: missing source registry"]
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        return [f"{prefix}: invalid JSON: {exc}"]
    if not isinstance(data, dict):
        return [f"{prefix}: registry must be an object"]

    def inspect_strings(value: object, field: str) -> None:
        if isinstance(value, str):
            errors.extend(error.replace(f"{prefix}:", f"{prefix} ({field}):", 1) for error in content_errors(registry_path, value))
        elif isinstance(value, dict):
            for key, child in value.items():
                inspect_strings(child, f"{field}.{key}")
        elif isinstance(value, list):
            for index, child in enumerate(value):
                inspect_strings(child, f"{field}[{index}]")

    inspect_strings(data, "registry")

    def valid_date(value: object) -> bool:
        if not isinstance(value, str) or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
            return False
        try:
            dt.date.fromisoformat(value)
            return True
        except ValueError:
            return False

    checked_on = data.get("checked_on")
    if not valid_date(checked_on):
        errors.append(f"{prefix}: checked_on must be a real YYYY-MM-DD date")
    sources = data.get("sources")
    if not isinstance(sources, list) or not sources:
        return errors + [f"{prefix}: sources must be a non-empty list"]
    seen = set()
    for number, source in enumerate(sources, 1):
        label = f"{prefix}: source {number}"
        if not isinstance(source, dict):
            errors.append(f"{label} must be an object")
            continue
        for key in ("id", "title", "url", "kind", "review_after_days", "last_verified", "used_in"):
            if key not in source:
                errors.append(f"{label} missing {key}")
        identifier = source.get("id")
        if not isinstance(identifier, str) or not re.fullmatch(r"[a-z0-9][a-z0-9._-]*", identifier):
            errors.append(f"{label} id must be a lowercase identifier")
        elif identifier in seen:
            errors.append(f"{label} duplicate id {identifier!r}")
        else:
            seen.add(identifier)
        for key in ("title", "kind"):
            if not isinstance(source.get(key), str) or not source[key].strip():
                errors.append(f"{label} {key} must be a non-empty string")
        url_error = public_source_url_error(source.get("url"))
        if url_error:
            errors.append(f"{label} url {url_error}")
        interval = source.get("review_after_days")
        if isinstance(interval, bool) or not isinstance(interval, int) or interval < 1:
            errors.append(f"{label} review_after_days must be a positive integer")
        verified = source.get("last_verified")
        if not valid_date(verified):
            errors.append(f"{label} last_verified must be a real YYYY-MM-DD date")
        elif valid_date(checked_on) and verified > checked_on:
            errors.append(f"{label} last_verified is after checked_on")
        if valid_date(verified) and isinstance(interval, int) and not isinstance(interval, bool) and interval > 0:
            try:
                dt.date.fromisoformat(verified) + dt.timedelta(days=interval)
            except OverflowError:
                errors.append(f"{label} review interval exceeds the supported calendar range")
        paths = source.get("used_in")
        if not isinstance(paths, list) or not paths:
            errors.append(f"{label} used_in must be a non-empty list")
            continue
        seen_paths = set()
        for used_in in paths:
            if not isinstance(used_in, str) or not used_in.strip():
                errors.append(f"{label} used_in entries must be non-empty relative Markdown paths")
                continue
            if used_in in seen_paths:
                errors.append(f"{label} duplicate used_in path {used_in!r}")
            seen_paths.add(used_in)
            target, anchor, error = local_destination(root, root / "README.md", used_in)
            if error or target is None or Path(used_in).is_absolute() or used_in.startswith("/") or "#" in used_in or "?" in used_in or target.suffix.lower() != ".md" or not target.is_file():
                errors.append(f"{label} used_in path does not name an existing relative Markdown file: {used_in!r}")
    return errors


def check(root: Path) -> tuple[list[str], int, int]:
    root = root.resolve()
    errors = []
    files = []
    fixtures = []
    for path in root.rglob("*"):
        if not path.is_file() or any(part in SKIP_DIRECTORIES for part in path.relative_to(root).parts):
            continue
        relative = path.relative_to(root)
        if path.suffix.lower() == ".md" or path.name == "llms.txt":
            files.append(path)
        elif relative.parts[:2] == ("examples", "fixtures") and path.suffix.lower() in {".txt", ".csv"}:
            fixtures.append(path)
    files.sort()
    fixtures.sort()
    texts: dict[Path, str] = {}
    for path in files + fixtures:
        relative = path.relative_to(root)
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as exc:
            errors.append(f"{relative.as_posix()}: cannot read UTF-8: {exc}")
            continue
        if path in files:
            texts[path] = text
        errors.extend(content_errors(relative, text))
    llms = root / "llms.txt"
    if not llms.is_file():
        errors.append("llms.txt: missing agent index")
    elif llms in texts and not markdown_links(texts[llms]):
        errors.append("llms.txt: must contain Markdown links to guide entry points")
    for source, source_text in texts.items():
        for line, destination in markdown_links(source_text):
            target, anchor, error = local_destination(root, source, destination)
            prefix = f"{source.relative_to(root).as_posix()}:{line}"
            if error:
                errors.append(f"{prefix}: {error}")
            elif target is not None:
                if not target.is_file():
                    errors.append(f"{prefix}: missing local target {destination!r}")
                elif anchor and target.suffix.lower() in {".md", ".txt"}:
                    target_text = texts.get(target)
                    if target_text is None:
                        try:
                            target_text = target.read_text(encoding="utf-8")
                        except (OSError, UnicodeError) as exc:
                            errors.append(f"{prefix}: cannot read anchor target as UTF-8: {exc}")
                            continue
                    if anchor not in heading_anchors(target_text):
                        errors.append(f"{prefix}: missing anchor #{anchor} in {target.relative_to(root).as_posix()}")
    errors.extend(registry_errors(root))
    return errors, len(files), len(fixtures)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1], help="repository root (defaults to this script's parent)")
    args = parser.parse_args(argv)
    errors, count, fixture_count = check(args.root)
    if errors:
        print(f"Guide checks failed ({len(errors)} issue(s), {count} Markdown documents, {fixture_count} text fixtures):", file=sys.stderr)
        for error in errors:
            print(f"  {error}", file=sys.stderr)
        return 1
    print(f"Guide checks passed: {count} Markdown documents, {fixture_count} text fixtures; local links and anchors, agent index, portable content and source registry.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
