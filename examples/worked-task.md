# Worked examples

These are made-up scenarios for working through a task and checking the result. They describe what should happen; no tests were run for this page. The request tracker illustrates an app change. The separate [practice task](practice-task.md) has input files and independent expected outputs you can use yourself.

## Request tracker: filter open requests by owner

### Before

A team has a request tracker with an Open tab that lists the requests the signed-in viewer may access. To find one owner's work, they have to scan the table. The app already has authentication and server-side access controls.

Before adding test data, confirm that the preview uses an isolated backend and disposable viewer accounts. Disable notifications and any other external effects for the exercise. Use the made-up records below. Their IDs stay fixed; owner names are display labels.

| Request ID | Owner / owner ID | Status | Viewers with access |
| --- | --- | --- | --- |
| a-1 | Owner A / owner-a | Open | Viewer 1, Viewer 2 |
| a-2 | Owner A / owner-a | Open | Viewer 1 |
| a-3 | Owner A / owner-a | Closed | Viewer 1 |
| b-1 | Owner B / owner-b | Open | Viewer 1 |
| c-1 | Owner C / owner-c | Closed | Viewer 1 |
| d-1 | Owner D / owner-d | Open | Neither viewer |

Viewer 1 can select Owners A, B, and C from the existing owner directory, including Owner C, who has no open requests. Start checks as Viewer 1 unless a step says otherwise. The unfiltered Open tab should contain exactly a-1, a-2, and b-1.

### Brief

> Add an owner filter to the Open tab. Default to all owners. Selecting an owner should show only that owner's open requests that the viewer may access. Preserve the filter in the URL so reload and shared links reproduce the view for each viewer's own permissions. Reuse existing UI and query conventions. Keep existing authentication and authorization. Make the smallest complete change, run the relevant checks, and show evidence for the visible behavior.

Follow the request and repository rules. Adding this filter doesn't authorize a new identity system, a different permission model, deployment, or external communication.

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

The agent should find the table, existing filter patterns, query/cache code, and access tests first. It can then explain which files it expects to change and how it will check the result. If it needs broader authority or an incompatible API change, it should explain that dependency before proceeding.

### The API is correct, but the table is stale

Suppose the API request includes `owner_id=owner-a` and returns the right rows, but the table still shows every owner. The API test passes. The person trying to use the filter still has the original problem.

Select Owner A in the browser and watch the table to reproduce the failure. Follow the state from the control through the URL, request parameters, cache key, response, and rendered rows. The cache key might include the Open tab but omit the owner. If the code and runtime trace confirm that cause, include the owner in the query identity and use the project's existing mechanism for avoiding stale responses. Then repeat the original interaction. Check the cause before using this fix on another stale table.

### Verification record to complete during real work

Record what happened against the commit and environment you tested. Mark a check **not run** if you couldn't execute it.

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

Keep the runtime script as a required check for future filter regressions. Use assertions and a trace to check the interaction; a screenshot alone only shows one moment. Fix failed checks before expanding the feature.

### Rollout and reusable lesson

Review the diff and check results through the project's existing release and approval process. Before sign-off, repeat the runtime checks against an existing live/UAT environment. If rollout fails, use the project's recovery process to revert the change and keep the reproduction so someone can investigate it.

After a real reproduction and verified fix, this could become useful guidance: when a filter request is correct but rows stay stale, check query identity alongside rendered state. Other failures can come from server filtering, access rules, or race handling, so keep that limit with the advice.

## Document to CSV: verify each extracted value

Suppose a synthetic two-page operations report contains `North: 12` on printed page 1 and `South: 8` on printed page 2. The task is to extract region, request count, and printed source page into CSV. The expected rows are `North,12,1` and `South,8,2`.

With a chat-only tool, write the brief and compare the rows by hand. Leave the file and execution checks below for an approved environment that can run them.

Before extracting anything, agree on the schema, units, page-number convention, and missing-value rule. Keep the original source and record its file hash with the output so someone can identify the version you used. Don't infer missing counts.

Open the delivered CSV and check that it parses, has the agreed header and exactly two data rows, includes each expected region once, and uses integer counts. Check quoting and encoding as well. Reject missing or duplicate rows. Compare every count, region label, and page number with the actual source page. A total of 20 could still hide swapped regions. If you need the total, calculate it deterministically from the verified rows.

Save the source version, script/command, row-level comparisons, actual results, and any unresolved ambiguity. This example hasn't been executed. In a real task, those records should let someone check each value, its unit and label, and where it came from.

Continue with [verification](../guide/verification.md) or use the [task brief](../templates/task-brief.md).
