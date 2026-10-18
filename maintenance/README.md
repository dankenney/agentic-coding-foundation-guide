# Maintain the guide

Keep the recommended workflows current, and add guidance when a correction or tested practice would help someone use a coding agent. Review new releases for useful changes without trying to cover them all.

## Review lessons from private work

Use the [lesson template](../templates/lesson.md) when a task, a failed workflow, or a new primary source suggests something worth adding. Record the source and date, the decision it could change, a proposed edit, and the evidence and uncertainty. Keep private sources and identifiable examples in an approved private system, such as Notion.

If the lesson comes from private work, ask what someone else could use, then test that guidance on examples that are safe to share. Find public support where the claim needs it. A private note can suggest a recommendation, but a product claim still needs public evidence. Review individual candidates rather than syncing a notebook into the guide, and leave private links out of the public review packet.

## Prepare a weekly review

1. Check the current guide revision, open review branches, recently accepted changes, and unresolved candidates so you don't duplicate a proposal or overwrite someone else's work.
2. Review due or changed sources in [the registry](source-watch.json). Look for relevant corrections and useful practices in official release notes and publications. Review selected new private notes where you have authorized access, and say which sources you couldn't check.
3. Read the source pages, including their exceptions. A changed hash or a new release gives you something to investigate; it doesn't tell you whether the guidance needs to change.
4. Prepare zero to three changes using the [weekly review packet](../templates/weekly-review.md). For each, name the page, proposed diff, affected reader or platform, supporting source, practical example, evidence, and limitation. Include guidance that should be removed. Complete the [editing passes](#edit-every-proposal-before-review) before presenting an edit as ready for review.
5. Discuss whether to adopt, trial, watch, or reject each proposal with the maintainer. Be clear about missing source coverage. If nothing warrants a change, say so.
6. After acceptance, apply the agreed edits on a review branch. Run the checks and affected learner route, update verification dates only for claims you reviewed, and record the decision. Merge and publication still require authorization.

Keep rejected or deferred candidates in the private system with a short reason and a trigger for revisiting them. Record adopted changes in the public changelog. Save a weekly record only when there's a decision or evidence worth keeping.

## Edit every proposal before review

For every proposed edit, read the affected pages in full and review all changed wording, including headings, prompts, templates, and replacement text. Check removals in context too. Apply the [natural writing editor](../skills/natural-writing-editor/SKILL.md) first, then the maintainer's privately configured voice skill. Run both passes again if the wording changes during review.

After the voice pass, compare the result with the intended change and its sources. Preserve technical meaning, commands, examples, citations, qualifications, and permission boundaries. Editing for voice must not add an unsupported claim or weaken an instruction.

Record completion of both passes and that final comparison in the review packet. If either skill is unavailable or a pass is unfinished, keep the candidate pending and report what's missing. Research can continue, but the edit isn't ready for review. Keep the voice skill, its private configuration, and its source material outside shared packets, public files, and workflow artifacts. Configure access privately; don't upload the skill to run maintenance.

## What should become guidance?

| Decision | Use when | Follow-through |
| --- | --- | --- |
| Adopt | A correction or useful practice has enough support | Prepare the edit and validate it |
| Trial | The idea looks useful, but we need to test it | Run a small, safe experiment with success and stop conditions |
| Watch | The idea is relevant, but it's too early or we lack access | Record the open question and when to revisit it |
| Reject | The proposal is weak, redundant, irrelevant, or too costly | Record the reason and leave it out |
| Retire | Existing guidance is obsolete or no longer useful | Remove or replace it and fix incoming links |

Use current official docs to check product mechanics. Read primary research with its methods and limits in view. If sources conflict, explain the conflict; a newer date doesn't automatically outweigh a more specific statement.

## Source evidence tools

The registry maps sources to the pages they support. `last_verified` records when someone assessed the relevant claim, and `review_after_days` sets the interval for reviewing it again. Platform mechanics change more often than stable concepts, so they have shorter intervals. These dates help schedule review; they don't guarantee that a product claim is still current.

```sh
python scripts/check_guide.py
python -m unittest discover -s tests -v
python scripts/source_watch.py --output work/source-review-2026-10-17.json
```

For a later run, choose a new output filename and optionally compare with the earlier report:

```sh
python scripts/source_watch.py --baseline work/source-review-2026-10-17.json --output work/source-review-next.json
```

Use `--only SOURCE_ID` to inspect one source and `--timeout 10` to set the per-request socket timeout. A failed fetch exits nonzero and records the missing coverage. A successful fetch saves response and redirect metadata plus a digest of the complete response. Inspect changes before drawing conclusions: navigation or dynamic content can change the bytes, and an unchanged page can still contain an outdated claim. The watcher doesn't update guidance or verification dates.

Maintainers choose the public sources in the registry. URL checks reject obvious private note hosts, local hostnames, and literal private IPs, including redirect targets. They don't provide DNS-level network isolation, so use the network controls you'd apply to another documentation fetcher. Save reports in ignored `work/` or `reports/` paths, or an explicitly chosen external JSON file. Use new filenames to preserve earlier evidence.

## Automation and ownership

The [source-watch workflow](../.github/workflows/source-watch.yml) fetches public sources on Fridays at 11:17 UTC and on manual dispatch. It has read-only repository permissions and saves a short-lived artifact containing the fetch results, including failures. It can't open or merge changes. Scheduled workflows start after the file reaches the repository's default branch. To compare a run with an earlier one, download the earlier artifact and use it as a local baseline; scheduled runs don't compare prior artifacts automatically.

A maintainer can use a separate weekly research session to review those results alongside private notes and prepare a review packet. That session needs authorized source access, a working checkout, and a reliable way to notify the maintainer. App automations are configured separately; cloning this guide doesn't install or schedule them.

If access fails, sources become stale, or nobody uses the reports, tell the owner what's missing. Agree whether to repair, narrow, pause, or stop the process. Don't present old recommendations as newly reviewed or report a completed review just because a scheduled run started.
