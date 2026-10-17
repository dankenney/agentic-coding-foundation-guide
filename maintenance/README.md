# Keep a selective, living guide

**Goal:** improve the guidance when evidence or practice changes. A small, current guide is more useful than an expanding feed.

## Capture privately, publish selectively

Use the [lesson template](../templates/lesson.md) for discoveries from work, a new primary source, or a failed workflow. Keep private sources and identifiable examples in an approved private intake system, such as Notion. Capture the exact source, date, practical decision, candidate wording, evidence, and uncertainty.

Translate a private observation into a general hypothesis. Test it on safe examples and seek public support where appropriate. A private note can motivate a recommendation; it cannot establish a public product fact. Do not synchronize an entire notebook into the guide or preserve private links in the public review packet.

## Prepare a weekly review

1. Inspect the guide's current revision, open review branches, recent accepted changes, and unresolved candidates. Avoid duplicate proposals or overwriting concurrent work.
2. Review due or changed sources from [the registry](source-watch.json), then inspect relevant official release notes and publications for corrections or useful new practices. Also inspect selected new private intake with available authorized access. State gaps; never imply a complete scan of every source or notebook.
3. Read source pages and their exceptions. A changed hash or new release is a lead, not proof that the guide needs editing.
4. Select **zero to three** useful proposals. Give each a specific page, proposed diff, affected reader/platform, source, practical example, evidence, and limitation. Include obsolete guidance to remove. Use the [weekly review packet](../templates/weekly-review.md).
5. Discuss adopt / trial / watch / reject with the maintainer. An incomplete source scan remains incomplete. No substantive change is a valid outcome.
6. After acceptance, apply the agreed edits on a review branch, run checks and the affected learner route, update source dates for claims actually reviewed, and record the decision. Do not merge or publish automatically.

Keep rejected or deferred candidates in private intake with a short reason and reconsideration trigger. Keep the public changelog about adopted guidance. Avoid creating a permanent weekly file when there is no useful durable record.

## What should become guidance?

| Decision | Use when | Follow-through |
| --- | --- | --- |
| Adopt | A supported correction or useful practice with adequate evidence | Reviewable edit and appropriate validation |
| Trial | Promising, but local usefulness is uncertain | Small safe experiment with success/stop conditions |
| Watch | Relevant but premature or inaccessible | Named question and revisit trigger |
| Reject | Weak, redundant, irrelevant, or costly | Brief reason; no guide expansion |
| Retire | Existing guidance no longer earns its place | Remove or replace it; fix incoming links |

Treat current official docs as the primary source for product mechanics, and primary research as evidence with its own methods and limits. Check conflicts explicitly. A newer timestamp alone does not supersede a more specific statement.

## Source evidence tools

The registry maps sources to the pages they support. `last_verified` is a human research date; `review_after_days` sets an editorial review interval. Fast-changing platform mechanics use shorter intervals than stable concepts. Neither is a product freshness guarantee.

```sh
python scripts/check_guide.py
python -m unittest discover -s tests -v
python scripts/source_watch.py --output work/source-review-2026-10-17.json
```

For a later run, choose a new output filename and optionally compare with the earlier report:

```sh
python scripts/source_watch.py --baseline work/source-review-2026-10-17.json --output work/source-review-next.json
```

Use `--only SOURCE_ID` to inspect one source, and `--timeout 10` to set the per-request socket timeout. A failed fetch exits nonzero and records missing coverage. A successful fetch records response and redirect metadata plus a digest of the complete response. A byte change can be page navigation or dynamic content; unchanged bytes do not establish that every claim is still correct. The watcher never updates guidance or verification dates.

The public-source registry is operator curated. URL checks reject obvious private note hosts, local hostnames, and literal private IPs, including redirect targets; they do not provide DNS-level network isolation. Run it with the same network controls appropriate to any other documentation fetcher. Reports stay in ignored `work/` or `reports/` paths, or an explicitly chosen external JSON file; use new filenames to preserve evidence.

## Automation and ownership

The [source-watch workflow](../.github/workflows/source-watch.yml) fetches public sources Fridays at 11:17 UTC and on manual dispatch, with read-only repository permissions. It stores a short-lived evidence artifact, including failed fetches, rather than opening or merging changes. Scheduled workflows start only after the file reaches the repository's default branch. Download a previous artifact if you want a local baseline comparison; scheduled runs do not automatically compare prior artifacts.

A separate, maintainer-owned weekly research session can combine that evidence with private intake and bring a review packet to the discussion. It needs authorized source access, a working checkout, and a reliable notification path. The automation configured in a maintainer's app is separate from this repository: cloning the guide does not install or schedule anything.

If access fails, sources become stale, or the process keeps producing unused digests, surface the missing coverage and repair, narrow, pause, or retire it with the owner. Do not silently recycle old recommendations or equate a scheduler invocation with a completed review.
