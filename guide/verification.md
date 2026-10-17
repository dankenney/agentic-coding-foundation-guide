# Verify the delivered thing

**Use when:** deciding whether a change works, reviewing another agent's output, or preparing to share a result. Completion needs evidence matched to the actual job.

## Start with a claim and an observation

“Tests pass” and “a user can submit a request” are different claims. The first may support the second, but you still need to observe the flow that matters.

| Claim | Useful observation | What it does not establish |
| --- | --- | --- |
| The project builds | Required build/check exits successfully | Correct interaction or production configuration |
| A filter works | Choose an owner; visible rows and count change correctly | Persistence unless separately checked |
| A request saves | Submit; see confirmation; reload and find the record | Correct authorization for another role |
| An export is correct | Open output; compare rows, types, totals, and escaping to a known fixture | Correctness for every possible input |
| A report is supported | Compare each material number/claim with its cited source | That the source itself is correct |
| A release works | Exercise the intended deployed version and environment | Future reliability without monitoring |

Anthropic's [evaluation guidance](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents) distinguishes the final environment state from what an agent says happened. It also separates regression checks from experiments that measure new capability. Apply that discipline proportionately: beginners need a few meaningful checks, not an evaluation platform.

## Before an interaction check

Confirm the running revision, effective backend/data environment, starting browser session, and what the action can change. A localhost or preview URL can still write to production or send real notifications. Use disposable fixtures and a test account in an isolated session where needed. Identify cleanup and disable or sandbox downstream sends, payments, and jobs before exercising them.

If the only available environment has unknown effects or no authorized test account, inspect code, existing tests, and logs first; prepare the reproduction for an authorized operator. Record the interaction as **not run**. Do not create live records, restore data, or deploy merely to satisfy this guide's verification requirement.

## For a non-trivial application change

1. Run the project's lint, type checks/build, and relevant tests. Investigate failures; record existing failures separately with evidence.
2. Exercise the primary user action in a real running app. Assert the visible result, not just the response code.
3. Check a meaningful alternate state: empty results, invalid input, error recovery, or the relevant permission boundary.
4. Check login and logout when authentication applies, including what protected UI does after logout. Name the starting session state.
5. Repeat the relevant flow on an existing live/UAT URL before sign-off, within authorized access and with safe test data. Verify the deployed revision. If unavailable or outside scope, report the gap and withhold live-readiness claims.

Use browser automation such as Playwright or the platform's browser tools. Store a reusable `scripts/runtime_behavior_check.*` check when fixing a reported interaction regression. Make the setup, test data, assertions, and cleanup understandable enough that another session can rerun it. Fix a failing runtime check before continuing feature work.

Derive expected results from the requirements and controlled inputs. A test that repeats the implementation's assumptions can pass with the same bug. When an agent changes an existing test or fixture, check that the new expectation reflects the intended contract; do not accept rewritten assertions merely to make the suite green. For a documentation-only change, check the content and affected reader route instead of exercising unrelated app flows.

A screenshot establishes appearance at one moment. A recording helps explain sequence. Assertions establish the specific conditions you wrote. Use the combination that answers the acceptance criteria. Check keyboard interaction and the relevant narrow-screen layout when the change affects them; do not mistake a desktop screenshot for complete UI coverage.

## For files, data, and generated artifacts

Open the final artifact from its delivered path. Confirm it exists, is the expected version, and contains the requested content. For a CSV, check row counts, column names, representative values, encoding, missing values, and totals against a controlled input. For a document or slide deck, render and inspect it as a reader will see it. Recalculate deterministic numbers and verify citations against the exact source.

Keep evidence tied to an artifact or commit. Reviewing an earlier file while delivering a later file breaks that connection. If a reviewer reports a defect, rerun the affected check on the corrected artifact.

## Make a useful evidence record

```text
Artifact/revision:
Environment and URL/path:
Starting state and test data:
Acceptance criterion -> action/check -> observed result:
Checks run (exact commands):
Failed, skipped, or unavailable checks:
Evidence location:
Remaining release decision and owner:
```

Use real results. Do not fill the record with expected outcomes and label them passed. A test plan and an executed test are separate artifacts.

## Review independently where it matters

A reviewer should inspect the final diff and exercise the critical behavior without relying on the builder's summary as proof. Give the reviewer acceptance criteria and a reproducible environment. A second model can catch a different class of mistakes, but the value comes from independent observation and useful checks, not the number of approvals.

When evidence conflicts, follow the failing behavior. A green test suite with a stale UI is a reason to improve the checks. Continue with [recovery](recovery.md) and preserve the reproduction.
