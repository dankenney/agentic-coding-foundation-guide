# Check the result

Before you accept or share an agent's work, check the result against what you asked it to do. Choose checks that can show whether the change works for the person who'll use it.

## Start with a claim and an observation

A passing test suite gives you evidence about the conditions it covers. To establish that a user can submit a request, you also need to try that flow and observe what happens.

| Claim | Useful observation | What it does not establish |
| --- | --- | --- |
| The project builds | Required build/check exits successfully | Correct interaction or production configuration |
| A filter works | Choose an owner; visible rows and count change correctly | Persistence unless separately checked |
| A request saves | Submit; see confirmation; reload and find the record | Correct authorization for another role |
| An export is correct | Open output; compare rows, types, totals, and escaping to a known fixture | Correctness for every possible input |
| A report is supported | Compare each material number/claim with its cited source | That the source itself is correct |
| A release works | Exercise the intended deployed version and environment | Future reliability without monitoring |

Anthropic's [evaluation guidance](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents) distinguishes the final state of the environment from the agent's account of what happened. It also separates regression checks from experiments that measure new capability. You can apply this to a first task with a few meaningful checks; there's no need to build an evaluation platform.

## Before an interaction check

First confirm which revision is running, which backend and data it uses, the browser's starting session, and what the action can change. A localhost or preview URL can still write to production or send real notifications. Use disposable fixtures and a test account in an isolated session where needed. Plan the cleanup, and disable or sandbox downstream sends, payments, and jobs before trying them.

If you don't know what the available environment will affect, or you don't have an authorized test account, start by inspecting the code, existing tests, and logs. Prepare the reproduction for someone authorized to run it and record the interaction as not run. This guide's checks don't authorize you to create live records, restore data, or deploy.

## For a non-trivial application change

1. Run the project's lint, type checks/build, and relevant tests. Investigate failures; record existing failures separately with evidence.
2. Exercise the primary user action in a real running app. Assert the visible result, not just the response code.
3. Check a meaningful alternate state: empty results, invalid input, error recovery, or the relevant permission boundary.
4. Check login and logout when authentication applies, including what protected UI does after logout. Name the starting session state.
5. Repeat the relevant flow on an existing live/UAT URL before sign-off, within authorized access and with safe test data. Verify the deployed revision. If unavailable or outside scope, report the gap and withhold live-readiness claims.

Use browser automation such as Playwright or the platform's browser tools. When fixing a reported interaction regression, save a reusable `scripts/runtime_behavior_check.*` check. Include enough detail about the setup, test data, assertions, and cleanup for another session to rerun it. If the runtime check fails, fix that before continuing feature work.

Work out the expected results from the requirements and controlled inputs. If the test repeats the implementation's assumptions, it can share the same bug. Review any changes the agent makes to existing tests or fixtures against the intended contract. A failing assertion needs a reason to change beyond getting the suite to pass. For a documentation-only change, check the content and affected reader route; unrelated app flows won't help verify the edit.

Choose evidence to answer the acceptance criteria. A screenshot shows appearance at one moment, a recording helps explain a sequence, and assertions check the specific conditions you wrote. Include keyboard interaction and the relevant narrow-screen layout when the change affects them. A desktop screenshot leaves those questions open.

Once the correctness checks pass, try the result as its intended user. Check whether they can find the next action, understand the result, and recover without your explanation. If something gets in the way, fix the most consequential issue within scope and try the flow again.

## For files, data, and generated artifacts

Open the artifact from the path you're delivering. Confirm it's the expected version and contains the requested content. For a CSV, compare row counts, column names, representative values, encoding, missing values, and totals with a controlled input. Render documents and slide decks so you can inspect what the reader will see. Recalculate deterministic numbers and check citations against the exact source.

Record which artifact or commit you checked. If you change it after review, the earlier evidence may no longer apply. When a reviewer reports a defect, rerun the affected check on the corrected artifact.

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

Fill this in with observed results. Keep expected outcomes in the test plan until you've run the checks; only then can you report whether they passed.

## Review independently where it matters

Give a reviewer the acceptance criteria and an environment where they can reproduce the checks. They should inspect the final diff and try the critical behavior themselves. A second model may catch mistakes the first missed, provided it checks the work rather than accepting the builder's summary.

If the tests pass but the UI is stale, investigate the behavior and improve the checks that missed it. Keep the reproduction and continue with [recovery](recovery.md).
