# Working as a team

When someone else will use or maintain the result, they need to know who owns it, what was checked, and how to continue the work. Agree on those expectations before the handoff.

## Agree how the team will work

Agree where to track the task, which repository instructions everyone follows, how to review changes, and who owns the result. Be explicit about approved data and services, who may change production, and who handles recovery. Your workplace's tool and data policies still apply.

Keep the shared instructions in one concise, canonical file. Where a tool needs its own entry file, point it to that source and verify that the agent reads it. Maintaining a separate manual for every tool creates work and invites conflicting instructions. Review instruction changes as carefully as code changes: they affect what agents do on later tasks.

## Assign responsibilities

| Role | Responsibility | Evidence it should produce |
| --- | --- | --- |
| Task owner | Choose the problem and acceptance criteria | A clear outcome and release decision |
| Builder | Implement within the brief | Diff, runnable artifact, checks and gaps |
| Reviewer/verifier | Challenge the result against the criteria | Specific findings and independently observed behavior |
| Integrator | Resolve interfaces and verify the combined change | A working combined revision |

People and agents can share these roles, and one person may hold several on a small task. The task owner still needs to judge the evidence, even when a reviewer has already looked at it.

Before splitting work, agree who owns each file or module and how the parts will fit together. Integrate a small change early so you can catch conflicting assumptions. Then check the combined revision and keep a way to recover it; passing tests on separate branches won't tell you whether the pieces work together.

## Review what people will actually receive

Compare what was requested with the changed implementation and the result you can observe. Give the reviewer the artifact or revision, instructions to run it, checks performed, known limits, and any decision you need from them. If something remains uncertain, say what would resolve it.

For UI work, show the changed flow and the relevant error or empty state. Open exported files and reports in the form you'll deliver them. For permissions or migrations, involve someone who can assess what's changing and whether the recovery plan covers it. Use test data in screenshots and fixtures.

## Release and follow through

Before a shared release, confirm who will use it, where it will run, how it was checked, who owns it, and how to recover. Verify the intended deployed version with safe test data, and keep development configuration separate from production. After release, watch for the errors, failed jobs, broken flows, or user feedback relevant to the change. If people will depend on a prototype, assign someone to maintain it.

Leave a [handoff](../templates/handoff.md) when someone else needs to pick up the work. They should be able to find their next action without reading the chat. Record a lasting design choice when its rationale will help them; skip the session log if it adds nothing useful.

## Check whether the workflow helps

Choose a few comparable tasks and record how long it takes to reach an accepted result, the effort spent on review and rework, failures found after release, and whether the output solved the intended problem. Include human and agent costs, and note any change in scope. Generated lines, commit counts, and guessed hours saved won't tell you whether the work improved.

Published research can help you decide what to measure, but it can't forecast the benefit for your team. The [DORA 2025 report abstract](https://research.google/pubs/dora-2025-state-of-ai-assisted-software-development-report/) describes organizational strengths and weaknesses being amplified; it doesn't establish a causal effect for your team. METR's [February 2026 experiment update](https://metr.org/blog/2026-02-24-uplift-update/) explains problems with selection and time measurement. Its [May 2026 survey](https://metr.org/blog/2026-05-11-ai-usage-survey/) distinguishes perceived speed from value and warns about self-report bias. Measure your own workflow before promising an improvement.

In a short weekly conversation, choose one improvement to try. It might be a clearer brief, a check that catches a missed failure, an instruction you can remove, or a workflow worth repeating. Keep the lessons that help, along with their evidence and limits, using the [maintenance process](../maintenance/README.md).
