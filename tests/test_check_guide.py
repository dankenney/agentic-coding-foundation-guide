"""Regression checks for the quality gate, using disposable tiny guide repositories."""

import copy
import datetime as dt
from http.client import HTTPResponse
import io
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch
from urllib.error import HTTPError, URLError
from urllib.response import addinfourl

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import check_guide
import source_watch


class GuideChecks(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.write("README.md", "# Guide\n\n[Start](guide/start.md#make-a-change)\n")
        self.write("guide/start.md", "# Start\n\n## Make a change\n\n[Home](../README.md#guide)\n")
        self.write("llms.txt", "# Agent index\n\n[Start](guide/start.md)\n")
        self.registry = {"checked_on": "2026-10-17", "sources": [{"id": "official-docs", "title": "Official documentation", "url": "https://example.com/docs", "kind": "documentation", "review_after_days": 30, "last_verified": "2026-10-17", "used_in": ["guide/start.md"]}]}
        self.save_registry()

    def write(self, name, content):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")

    def save_registry(self):
        self.write("maintenance/source-watch.json", json.dumps(self.registry))

    def errors(self):
        return check_guide.check(self.root)[0]

    def assert_error(self, phrase):
        errors = self.errors()
        self.assertTrue(any(phrase in error for error in errors), errors)

    def test_valid_repo(self):
        self.assertEqual([], self.errors())

    def test_missing_relative_file(self):
        self.write("README.md", "[Missing](guide/missing.md)\n")
        self.assert_error("missing local target")

    def test_missing_anchor(self):
        self.write("README.md", "[Missing](guide/start.md#removed-heading)\n")
        self.assert_error("missing anchor #removed-heading")

    def test_current_page_anchor(self):
        self.write("README.md", "# Guide\n[Jump](#missing)\n")
        self.assert_error("missing anchor #missing")

    def test_duplicate_unicode_and_explicit_anchors(self):
        self.write("guide/start.md", '# Start\n## Make a change\n## Make a change\n## Résumé: `API` & tests!\n<a id="custom"></a>\n')
        self.write("README.md", "# Guide\n[Second](guide/start.md#make-a-change-1)\n[Unicode](guide/start.md#r%C3%A9sum%C3%A9-api--tests)\n[Explicit](guide/start.md#custom)\n")
        self.assertEqual([], self.errors())

    def test_reference_and_html_links(self):
        self.write("README.md", '# Guide\n[Start][entry]\n[entry]: guide/start.md#make-a-change\n<a href="guide/gone.md">Gone</a>\n')
        self.assert_error("missing local target 'guide/gone.md'")

    def test_undefined_reference(self):
        self.write("README.md", "# Guide\n[Start][unknown]\n")
        self.assert_error("undefined Markdown reference")

    def test_image_and_balanced_parentheses_destination(self):
        self.write("guide/image (one).svg", "<svg/>")
        self.write("README.md", '# Guide\n![Image](<guide/image (one).svg>)\n[Other](guide/start.md "title")\n[Doc](guide/a(b).md)\n')
        self.write("guide/a(b).md", "# Other\n")
        self.assertEqual([], self.errors())

    def test_fenced_samples_are_not_links(self):
        self.write("README.md", "# Guide\n```markdown\n[Example](placeholder.md)\n# Invisible\n```\n~~~md\n[Example](other.md)\n~~~\n[Start](guide/start.md)\n")
        self.assertEqual([], self.errors())
        self.assertNotIn("invisible", check_guide.heading_anchors((self.root / "README.md").read_text()))

    def test_inline_code_and_escaped_labels_are_not_links(self):
        self.write("README.md", "# Guide\nUse `[Example](placeholder.md)` or `` `[Example](other.md)` ``.\n\\[Literal](absent.md)\n")
        self.assertEqual([], self.errors())
        # Two backslashes leave an ordinary link after an escaped backslash.
        self.write("README.md", r"\\[Actual](missing.md)" + "\n")
        self.assert_error("missing local target 'missing.md'")

    def test_nested_labels_and_multiline_destinations_are_checked(self):
        for text in ("[Docs [v2]](missing.md)\n", "[Docs](\nmissing.md\n)\n", "[Docs [v2]](\nguide/start.md#missing\n)\n"):
            with self.subTest(text=text):
                self.write("README.md", "# Guide\n" + text)
                self.assert_error("missing anchor" if "#missing" in text else "missing local target 'missing.md'")
        self.write("README.md", '# Guide\n[Docs [v2]](\nguide/start.md#make-a-change\n"A title"\n)\n')
        self.assertEqual([], self.errors())

    def test_html_attributes_allow_spacing_lines_and_unquoted_paths(self):
        for text in ('<a href = "missing.md">Docs</a>\n', "<img\n src = missing.svg>\n"):
            with self.subTest(text=text):
                self.write("README.md", "# Guide\n" + text)
                self.assert_error("missing local target")
        self.write("README.md", '# Guide\n<a\n href = "guide/start.md#make-a-change">Docs</a>\n')
        self.assertEqual([], self.errors())

    def test_explicit_anchors_must_be_html_outside_inline_code(self):
        self.write("README.md", "[Jump](guide/start.md#sample)\n")
        self.write("guide/start.md", '# Start\nUse `<a id="sample"></a>` as the syntax.\n')
        self.assert_error("missing anchor #sample")
        self.write("guide/start.md", '# Start\n<a id = sample></a>\n')
        self.assertEqual([], self.errors())

    def test_traversal_is_rejected(self):
        self.write("README.md", "[Escape](../outside.md)\n")
        self.assert_error("link escapes repository")

    def test_missing_llms_and_broken_llms_path(self):
        (self.root / "llms.txt").unlink()
        self.assert_error("missing agent index")
        self.write("llms.txt", "[Missing](guide/missing.md)\n")
        self.assert_error("llms.txt:1: missing local target")

    def test_private_notes_and_client_paths_rejected_in_examples(self):
        self.write("README.md", "# Guide\nhttps://www.notion.so/private-id\n```text\nC:\\Users\\example\\secret.txt\n```\n")
        self.assert_error("private Notion reference")
        self.assert_error("local/client artifact")

    def test_private_note_destinations_are_normalized_in_all_examples(self):
        for text in (
            "[Notes](//team.notion.site/private)",
            "[Notes](https://team&#46;notion&#46;site/private)",
            "[Notes](https://notion.so)",
            '<a href = "//app.notion.com/private">Notes</a>',
            "[Notes](https://reader@notion.so/private)",
            "`//team.notion.site/private`",
            r"[Notes](https:\/\/team\.notion\.site/private)",
            "[Notes](https://notion%2Eso/private)",
        ):
            with self.subTest(text=text):
                self.write("README.md", "# Guide\n" + text + "\n")
                self.assert_error("private Notion reference")
        self.write("README.md", "# Guide\n[Public](https://notion.so.example.com/)\n[Public](https://example.com/notion.so)\n")
        self.assertEqual([], self.errors())

    def test_fixture_text_and_csv_are_content_checked_without_markdown_parsing(self):
        for name in ("examples/fixtures/sample.txt", "examples/fixtures/sample.csv"):
            with self.subTest(name=name):
                self.write(name, "Literal [example](missing.md)\n")
                self.assertEqual([], self.errors())
                self.write(name, "Source: //team.notion.site/private\n")
                self.assert_error(f"{name}:1: private Notion reference")
                self.write(name, "Safe made-up sample\n")
        _, documents, fixtures = check_guide.check(self.root)
        self.assertEqual(3, documents)
        self.assertEqual(2, fixtures)

    def test_registry_content_fields_cannot_hide_private_provenance(self):
        for field, value in (("supports", "See //team.notion.site/private"), ("limits", r"Derived from C:\Users\example\notes.txt"), ("intake", {"links": ["https://team&#46;notion&#46;site/private"]})):
            with self.subTest(field=field):
                source = self.registry["sources"][0]
                source[field] = value
                self.save_registry()
                errors = check_guide.registry_errors(self.root)
                self.assertTrue(any(f"registry.sources[0].{field}" in error for error in errors), errors)
                del source[field]

    def test_non_utf8_anchor_target_is_reported_without_crashing(self):
        self.write("README.md", "# Guide\n[Jump](guide/start.md#sample)\n")
        (self.root / "guide/start.md").write_bytes(b"\xff")
        self.assert_error("cannot read UTF-8")

    def test_retired_tool_and_legacy_filename(self):
        self.write("docs/claude-setup.md", "# Old\n")
        self.write("README.md", "# Guide\nClaude Code setup\n")
        self.assert_error("legacy tool reference")
        self.assert_error("legacy tool filename")

    def test_source_schema_rejects_missing_and_invalid_fields(self):
        source = self.registry["sources"][0]
        del source["title"]
        source.update(url="http://example.com", last_verified="2026-02-30", review_after_days=True)
        self.save_registry()
        for phrase in ("missing title", "url must be an https", "last_verified must be a real", "review_after_days must be a positive integer"):
            self.assert_error(phrase)

    def test_source_duplicate_ids_and_paths(self):
        self.registry["sources"].append(copy.deepcopy(self.registry["sources"][0]))
        self.registry["sources"][0]["used_in"] = ["guide/missing.md", "../outside.md", "https://example.com/guide.md", "guide/start.md#start"]
        self.save_registry()
        self.assert_error("duplicate id")
        self.assert_error("used_in path does not name an existing")

    def test_source_registry_private_url_and_future_review(self):
        self.registry["sources"][0].update(url="https://team.notion.site/private", last_verified="2026-10-18")
        self.save_registry()
        self.assert_error("private Notion URLs")
        self.assert_error("last_verified is after checked_on")

    def test_registry_rejects_review_date_overflow(self):
        for verified, interval in (("2026-10-17", 10**20), ("9999-12-31", 1)):
            with self.subTest(verified=verified, interval=interval):
                self.registry["checked_on"] = verified
                self.registry["sources"][0].update(last_verified=verified, review_after_days=interval)
                self.save_registry()
                self.assert_error("review interval exceeds the supported calendar range")

    def test_registry_rejects_url_whitespace_and_controls(self):
        for url in ("https://example.com/a b", "https://example.com/\n", "https://example.com/\x00"):
            with self.subTest(url=url):
                self.registry["sources"][0]["url"] = url
                self.save_registry()
                self.assert_error("unescaped whitespace or control characters")

    def test_registry_rejects_note_hosts_and_nonpublic_targets(self):
        for url in ("https://notion.com/private", "https://app.notion.com/private", "https://127.0.0.1/docs", "https://10.0.0.2/docs", "https://[::1]/docs", "https://localhost/docs", "https://docs.local/docs", "https://server/docs"):
            with self.subTest(url=url):
                self.registry["sources"][0]["url"] = url
                self.save_registry()
                self.assertTrue(check_guide.registry_errors(self.root))

    def test_invalid_json(self):
        self.write("maintenance/source-watch.json", "{")
        self.assert_error("invalid JSON")

    def test_check_cli_exit_status_and_output(self):
        with patch("sys.stdout", new_callable=io.StringIO) as output:
            self.assertEqual(0, check_guide.main(["--root", str(self.root)]))
            self.assertIn("Guide checks passed", output.getvalue())
        self.write("README.md", "[Broken](missing.md)\n")
        with patch("sys.stderr", new_callable=io.StringIO) as output:
            self.assertEqual(1, check_guide.main(["--root", str(self.root)]))
            self.assertIn("missing local target", output.getvalue())

    def test_watch_cli_saves_evidence_without_changing_registry(self):
        path = self.root / "work" / "evidence.json"
        before = (self.root / check_guide.REGISTRY_PATH).read_bytes()
        fetched = {"id": "official-docs", "url": "https://example.com/docs", "final_url": "https://example.com/docs", "fetch_ok": True, "sha256": "abc", "status": 200}
        with patch("source_watch.fetch_evidence", return_value=fetched), patch("sys.stdout", new_callable=io.StringIO):
            self.assertEqual(0, source_watch.main(["--root", str(self.root), "--output", str(path)]))
            first = json.loads(path.read_text())
            self.assertEqual("no_baseline", first["sources"][0]["comparison"])
            second_path = self.root / "work" / "second.json"
            self.assertEqual(0, source_watch.main(["--root", str(self.root), "--baseline", str(path), "--output", str(second_path)]))
            second = json.loads(second_path.read_text())
            self.assertEqual("same_content_bytes", second["sources"][0]["comparison"])
        self.assertEqual(before, (self.root / check_guide.REGISTRY_PATH).read_bytes())

    def test_watch_cli_rejects_registry_as_output(self):
        with patch("sys.stderr", new_callable=io.StringIO):
            with self.assertRaises(SystemExit) as raised:
                source_watch.main(["--root", str(self.root), "--output", str(self.root / check_guide.REGISTRY_PATH)])
        self.assertEqual(2, raised.exception.code)

    def test_watch_cli_failed_fetch_still_writes_report(self):
        path = self.root / "work" / "failed.json"
        fetched = {"id": "official-docs", "url": "https://example.com/docs", "fetch_ok": False, "error": "timeout"}
        with patch("source_watch.fetch_evidence", return_value=fetched), patch("sys.stdout", new_callable=io.StringIO):
            self.assertEqual(1, source_watch.main(["--root", str(self.root), "--output", str(path)]))
        self.assertEqual("fetch_failed", json.loads(path.read_text())["sources"][0]["comparison"])

    def test_report_output_boundary_and_no_overwrite(self):
        for name in ("other.json", "maintenance/other.json", "guide/sources.json", "README.md", "work/report.txt", "../escape.json"):
            with self.subTest(name=name), self.assertRaises(ValueError):
                source_watch.report_output_path(self.root, Path(name))
        self.assertEqual(self.root / "work" / "fresh.json", source_watch.report_output_path(self.root, Path("work/fresh.json")))
        self.assertEqual(self.root / "reports" / "fresh.json", source_watch.report_output_path(self.root, Path("reports/fresh.json")))
        self.write("work/baseline.json", '{"sources": []}')
        with self.assertRaisesRegex(ValueError, "never overwritten"):
            source_watch.report_output_path(self.root, self.root / "work" / "baseline.json")
        with tempfile.TemporaryDirectory() as directory:
            external = Path(directory) / "fresh.json"
            self.assertEqual(external, source_watch.report_output_path(self.root, external))

    def test_watch_cli_rejects_existing_report_before_fetch(self):
        self.write("work/baseline.json", '{"sources": []}')
        with patch("source_watch.fetch_evidence") as fetch, patch("sys.stderr", new_callable=io.StringIO):
            with self.assertRaises(SystemExit):
                source_watch.main(["--root", str(self.root), "--baseline", str(self.root / "work" / "baseline.json"), "--output", "work/baseline.json"])
        fetch.assert_not_called()

    def test_watch_cli_rejects_review_overflow_before_fetch(self):
        self.registry["sources"][0]["review_after_days"] = 10**20
        self.save_registry()
        with patch("source_watch.fetch_evidence") as fetch, patch("sys.stderr", new_callable=io.StringIO) as output:
            self.assertEqual(2, source_watch.main(["--root", str(self.root)]))
        self.assertIn("review interval exceeds", output.getvalue())
        fetch.assert_not_called()


class FakeResponse:
    status = 200
    headers = {"Content-Type": "text/html", "ETag": '"v1"'}

    def __init__(self, body=b"current source", url="https://example.com/docs"):
        self.body = body
        self.url = url

    def __enter__(self):
        return self

    def __exit__(self, *args):
        return None

    def geturl(self):
        return self.url

    def read(self, limit):
        return self.body[:limit]


class FakeOpener:
    def __init__(self, response=None, error=None):
        self.response = response or FakeResponse()
        self.error = error
        self.calls = []

    def open(self, request, timeout):
        self.calls.append((request, timeout))
        if self.error:
            raise self.error
        return self.response


class SourceWatcher(unittest.TestCase):
    def setUp(self):
        self.source = {"id": "docs", "url": "https://example.com/docs", "last_verified": "2026-10-01", "review_after_days": 7, "used_in": ["guide/start.md"]}

    def test_get_hash_and_metadata(self):
        opener = FakeOpener()
        fetched = source_watch.fetch_evidence(self.source, 3, opener)
        self.assertTrue(fetched["fetch_ok"])
        self.assertEqual(64, len(fetched["sha256"]))
        self.assertEqual("GET", opener.calls[0][0].method)
        self.assertEqual(3, opener.calls[0][1])
        self.assertEqual('"v1"', fetched["etag"])

    def test_staleness_and_changes_are_distinct(self):
        fetched = source_watch.fetch_evidence(self.source, 3, FakeOpener())
        result = source_watch.review_evidence(self.source, fetched, {**fetched, "sha256": "old"}, dt.date(2026, 10, 17))
        self.assertEqual("content_bytes_changed", result["comparison"])
        self.assertTrue(result["review_due"])
        result = source_watch.review_evidence(self.source, fetched, fetched, dt.date(2026, 10, 7))
        self.assertEqual("same_content_bytes", result["comparison"])
        self.assertFalse(result["review_due"])
        self.assertEqual("2026-10-08", result["review_due_on"])
        self.assertEqual("2026-10-01", result["last_verified"])

    def test_new_url_requires_new_baseline(self):
        fetched = source_watch.fetch_evidence(self.source, 3, FakeOpener())
        previous = {**fetched, "url": "https://example.com/other"}
        result = source_watch.review_evidence(self.source, fetched, previous, dt.date(2026, 10, 17))
        self.assertEqual("no_baseline", result["comparison"])

    def test_private_and_non_https_sources_never_fetch(self):
        for url in ("https://www.notion.so/private", "https://team.notion.site/private", "https://notion.com/private", "https://app.notion.com/private", "http://example.com", "https://localhost/docs", "https://127.0.0.1/docs", "https://10.1.2.3/docs", "https://[::1]/docs", "https://docs.internal/docs"):
            opener = FakeOpener()
            fetched = source_watch.fetch_evidence({**self.source, "url": url}, 3, opener)
            self.assertFalse(fetched["fetch_ok"])
            self.assertEqual([], opener.calls)

    def test_private_or_downgrade_redirect_is_blocked(self):
        handler = source_watch.PublicHTTPSRedirects()
        for target in ("https://team.notion.site/private", "https://app.notion.com/private", "http://example.com/docs", "https://127.0.0.1/docs", "https://[::1]/docs", "https://docs.local/docs", "https://localhost/docs"):
            with self.assertRaises(URLError):
                handler.redirect_request(None, None, 302, "Found", {}, target)

    def test_public_urls_and_special_host_rejection(self):
        for url in ("https://openai.com/docs", "https://docs.replit.com/docs", "https://example.com/docs", "https://8.8.8.8/docs", "https://[2606:4700:4700::1111]/docs"):
            with self.subTest(url=url):
                self.assertTrue(source_watch.permitted_url(url))
        for url in ("https://127.1/docs", "https://2130706433/docs", "https://0x7f000001/docs", "https://224.0.0.1/docs", "https://169.254.169.254/", "https://docs.test/", "https://notion.com./private", "https://user:pass@example.com/", "https://example.com:99999/"):
            with self.subTest(url=url):
                self.assertFalse(source_watch.permitted_url(url))

    def test_failed_get_and_size_limit_have_no_digest(self):
        for opener in (FakeOpener(error=URLError("timeout")), FakeOpener(FakeResponse(b"a" * (source_watch.MAX_BYTES + 1)))):
            fetched = source_watch.fetch_evidence(self.source, 3, opener)
            self.assertFalse(fetched["fetch_ok"])
            self.assertNotIn("sha256", fetched)
            result = source_watch.review_evidence(self.source, fetched, None, dt.date(2026, 10, 17))
            self.assertEqual("fetch_failed", result["comparison"])

    def test_early_eof_with_content_length_has_no_digest(self):
        class TruncatedSocket:
            def makefile(self, *args):
                return io.BytesIO(b"HTTP/1.1 200 OK\r\nContent-Length: 100\r\n\r\nshort")
        response = HTTPResponse(TruncatedSocket())
        response.begin()
        wrapped = addinfourl(response, response.headers, self.source["url"], response.status)
        fetched = source_watch.fetch_evidence(self.source, 3, FakeOpener(wrapped))
        self.assertFalse(fetched["fetch_ok"])
        self.assertNotIn("sha256", fetched)
        self.assertEqual(5, fetched["bytes_read"])
        self.assertIn("declared 100", fetched["error"])

    def test_invalid_declared_length_and_read_errors_are_failed_evidence(self):
        for length in ("-1", "invalid", "100"):
            with self.subTest(length=length):
                response = FakeResponse()
                response.headers = {"Content-Length": length}
                fetched = source_watch.fetch_evidence(self.source, 3, FakeOpener(response))
                self.assertFalse(fetched["fetch_ok"])
                self.assertNotIn("sha256", fetched)
        class FailedBody(FakeResponse):
            def read(self, limit):
                raise TimeoutError("body timed out")
        fetched = source_watch.fetch_evidence(self.source, 3, FakeOpener(FailedBody()))
        self.assertFalse(fetched["fetch_ok"])
        self.assertNotIn("sha256", fetched)
        self.assertIn("body timed out", fetched["error"])

    def test_chunked_framing_takes_precedence_over_content_length(self):
        response = FakeResponse()
        response.headers = {"Content-Length": "100", "Transfer-Encoding": "chunked"}
        self.assertTrue(source_watch.fetch_evidence(self.source, 3, FakeOpener(response))["fetch_ok"])

    def test_request_encoding_failure_becomes_failed_evidence(self):
        opener = FakeOpener(error=UnicodeEncodeError("ascii", "\u00e9", 0, 1, "non-ASCII URL"))
        fetched = source_watch.fetch_evidence(self.source, 3, opener)
        self.assertFalse(fetched["fetch_ok"])
        self.assertNotIn("sha256", fetched)
        self.assertIn("non-ASCII URL", fetched["error"])

    def test_http_failure_is_evidence(self):
        opener = FakeOpener(error=HTTPError(self.source["url"], 404, "Not Found", {}, None))
        fetched = source_watch.fetch_evidence(self.source, 3, opener)
        self.assertEqual(404, fetched["status"])
        self.assertFalse(fetched["fetch_ok"])

    def test_baseline_schema(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "baseline.json"
            path.write_text('{"sources": [{"id": "docs", "sha256": "abc"}]}')
            self.assertEqual("abc", source_watch.load_baseline(path)["docs"]["sha256"])
            path.write_text('{"sources": [{"id": "docs"}, {"id": "docs"}]}')
            with self.assertRaisesRegex(ValueError, "duplicate"):
                source_watch.load_baseline(path)


if __name__ == "__main__":
    unittest.main()
