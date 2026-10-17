# Worked tasks: make the result observable

These synthetic scenarios explain expected behavior and failure modes; they are not execution logs. The request tracker is illustrative. For an exercise with supplied inputs and independent expected outputs, use the [practice task](practice-task.md).

## Request tracker: filter open requests by owner

### Before

A team uses an existing request tracker. Its Open tab lists requests the signed-in viewer may access. Finding one owner's work requires scanning the table. The app already has authentication and server-side access controls.

Use an isolated test environment and disposable viewer accounts; confirm the preview's backend before seeding data. Disable downstream notifications or other external effects for the exercise. Use these synthetic fixtures; IDs are stable, while owner names are display labels:

| Request ID | Owner / owner ID | Status | Viewers with access |
| --- | --- | --- | --- |
| a-1 | Owner A / owner-a | Open | Viewer 1, Viewer 2 |
| a-2 | Owner A / owner-a | Open | Viewer 1 |
| a-3 | Owner A / owner-a | Closed | Viewer 1 |
| b-1 | Owner B / owner-b | Open | Viewer 1 |
| c-1 | Owner C / owner-c | Closed | Viewer 1 |
| d-1 | Owner D / owner-d | Open | Neither viewer |

The existing owner directory makes Owners A, B, and C selectable for Viewer 1, including Owner C with no open requests. Begin checks as Viewer 1 unless stated otherwise; the unfiltered Open tab contains exactly a-1, a-2, and b-1.

### Brief

> Add an owner filter to the Open tab. Default to all owners. Selecting an owner should show only that owner's open requests that the viewer may access. Preserve the filter in the URL so reload and shared links reproduce the view for each viewer's own permissions. Reuse existing UI and query conventions. Keep existing authentication and authorization. Make the smallest complete change, run the relevant checks, and show evidence for the visible behavior.

Work within the existing request and repository rules. This task does not authorize a new identity system, permission model, deployment, or external communication.

### Acceptance

| Action | Observable result |
|---|---|
| Open the Open tab without a filter | All permitted open requests appear; closed requests do not. |
| Choose Owner A | The control shows Owner A; exactly the two permitted open fixtures appear. |
| Choose Owner C | A clear empty state appears; old rows disappear. |
| Clear the filter | All permitted open requests return. |
| Reload a filtered URL | The selection and rows agree with that URL. |
| Open Viewer 1's Owner A URL as Viewer 2, including after switching accounts in the same browser | Only a-1 appears; a-2 from the previous session does not remain visible. |
| Switch owners quickly | A slower earlier response cannot replace the latest selection's results. |
| Change the owner ID in the filtered URL to one outside the viewer's scope | No inaccessible rows or owner details are returned by the server or shown in the UI. The filter does not grant access. |
| Exercise the existing login/logout flow | Existing access behavior still works; unauthorized rows never appear. |

The agent first finds the table, filter conventions, query/cache code, and existing access tests. It states the likely files and verification approach, then implements within that scope. If the change requires broader authority or an incompatible API change, it reports the specific dependency before proceeding.

### A misleading success and the diagnostic seam

Suppose the API request includes `owner_id=owner-a` and returns the right rows, but the table still shows every owner. An API test would pass while the feature fails.

Reproduce by selecting Owner A in the browser and observing the table. Follow the state across the control, URL, request parameters, cache key, response, and rendered rows. One possible cause is that the cache key includes the Open tab but omits the owner. If confirmed in the code and runtime trace, include the owner in the query identity and use the project's existing mechanism for avoiding stale responses. Then rerun the original interaction. Do not assume this diagnosis applies to every stale table.

### Verification record to complete during real work

Record actual results against the tested commit and environment. Leave an unrun check marked **not run**.

```text
Commit / environment / fixture setup:
Lint, build, relevant tests: command → actual result
Browser: choose / clear / empty / reload / quick switch → actual result
Access: login / logout / shared URL as Viewer 2 / out-of-scope owner URL → actual result
Regression script: scripts/runtime_behavior_check.<project language>
Evidence: trace, screenshot, or assertion output locations
Live/UAT: same interaction results, or no existing URL / access unavailable
Unresolved failures or limits:
```

Keep the runtime script as a required check for future filter regressions. A screenshot can show a moment; assertions and a trace should establish the interaction that produced it. Fix failed checks before expanding the feature.

### Rollout and reusable lesson

Review the diff and evidence, then use the project's existing release and approval process. Repeat the runtime checks against an existing live/UAT environment before sign-off. If rollout fails, revert the change using the project's recovery process and retain the reproduction.

Candidate lesson: **when a filter request is correct but rows stay stale, trace query identity and rendered state together.** Adopt that lesson only after a real reproduction and verified fix. Its limit: other failures may come from server filtering, access rules, or race handling.

## Document to CSV: verify each extracted value

Suppose a synthetic two-page operations report contains `North: 12` on printed page 1 and `South: 8` on printed page 2. The task is to extract region, request count, and printed source page into CSV. The expected rows are `North,12,1` and `South,8,2`.

Specify the schema, units, page-number convention, and missing-value rule before extraction. Preserve the original source and record its file hash with the extraction output. Do not infer missing counts.

Verify that the CSV parses, has the agreed header and exactly two data rows, includes each expected region once, and uses integer counts. Reject missing or duplicate rows. Compare each value, region label, and page number with the actual source page; a matching total alone could hide swapped regions. If a total is needed, calculate 20 deterministically from verified rows. Inspect the delivered CSV itself, including quoting and encoding, rather than the agent's summary.

Record the source version, script/command, row-level comparisons, actual results, and unresolved ambiguities. This example has no execution evidence. The transferable lesson is to turn factual claims into checks at the smallest useful unit: value, unit, label, and source location.

Continue with [verification](../guide/verification.md) or use the [task brief](../templates/task-brief.md).
