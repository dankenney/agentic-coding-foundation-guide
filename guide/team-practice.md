# Working as a team

**Use when:** an agent-assisted result will be used or maintained by someone else. Shared work needs clear ownership, inspectable evidence, and a project another person can continue.

## Agree a small working contract

Decide where the current task lives, which repository instructions are canonical, how changes are reviewed, what may touch production, and who owns the result. Make important boundaries concrete: approved data, permitted services, deployment authority, and recovery responsibility. Follow your workplace's tool and data policies.

Do not make one person maintain duplicate instruction manuals for every tool. Keep a concise canonical contract; use small platform entry files where needed and verify that the agent reads the intended source. Review changes to those files as carefully as changes to code, because they alter future behavior.

## Give each role a useful job

| Role | Responsibility | Evidence it should produce |
| --- | --- | --- |
| Task owner | Choose the problem and acceptance criteria | A clear outcome and release decision |
| Builder | Implement within the brief | Diff, runnable artifact, checks and gaps |
| Reviewer/verifier | Challenge the result against the criteria | Specific findings and independently observed behavior |
| Integrator | Resolve interfaces and verify the combined change | A working combined revision |

People and agents can share these roles. One person may hold several on a small task. Assigning a reviewer does not remove the task owner's responsibility to judge the evidence.

For parallel work, define file or module ownership and shared contracts first. Integrate a small change early to expose mismatched assumptions. Tests that pass in separate branches do not prove the combined result. Keep the combined revision recoverable and check it again.

## Review the result people will receive

A good review connects three things: the requested behavior, the changed implementation, and the observed result. Include the artifact/revision, how to run it, checks performed, known limits, and the decision needed. Make uncertainty visible enough that a reviewer can act on it.

For UI work, include a clear view of the changed flow and the relevant error or empty state. For exported files or reports, open the actual delivered file. For permissions or migrations, involve someone who can assess the affected contract and recovery plan. Keep real user data out of screenshots and fixtures.

## Ship the smallest useful slice

Before a shared release, identify its audience, environment, validation, owner, and recovery path. Verify the intended deployed version with safe test data. Keep development configuration separate from production. After release, watch the signals relevant to the change: errors, failed jobs, broken flows, or user feedback. A prototype becomes a maintained tool when someone owns its ongoing operation.

At a meaningful pause, leave a [handoff](../templates/handoff.md). It should answer “what can I do next?” without replaying a chat. Record a lasting design choice only when its rationale helps future work; do not generate logs for their own sake.

## Measure what improves work

Choose a few comparable tasks and record time to an accepted result, review/rework effort, escaped failures, and whether the output solved the intended problem. Include human and agent costs. Compare like tasks and note changed scope. Do not use generated lines, commits, or guessed hours saved as a productivity score.

Research is a reason to measure locally, not to promise a multiplier. The [DORA 2025 report abstract](https://research.google/pubs/dora-2025-state-of-ai-assisted-software-development-report/) describes organizational strengths and weaknesses being amplified; it does not establish a causal effect for your team. METR's [February 2026 experiment update](https://metr.org/blog/2026-02-24-uplift-update/) explains selection and time-measurement problems. Its [May 2026 survey](https://metr.org/blog/2026-05-11-ai-usage-survey/) distinguishes perceived speed from value and warns about self-report bias. None supplies a dependable forecast for a particular workflow.

Use a short weekly conversation to select one improvement: a clearer brief, a failing check, an unnecessary instruction to remove, or a workflow worth repeating. Capture the best lesson with evidence and limits. The [maintenance process](../maintenance/README.md) keeps that learning selective.
