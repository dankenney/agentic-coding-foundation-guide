# Agentic Coding Foundation

**Build something useful. Know why it works. Leave it easier to continue.**

A field guide for people who use coding agents at work: engineers, analysts, operators, designers, and the teammates building alongside them. Start with a small, useful change. Grow into systems you can inspect, trust, and maintain.

An agent can read a project, propose an approach, change files, and run tools. You choose the outcome, supply the context that matters, and judge whether the evidence is enough.

## Start where you are

For a first try without a project, use the [supplied practice task](examples/practice-task.md): made-up reports, expected answers, and no connected accounts. If your tool cannot create files and run commands, start with the [short CSV walkthrough](examples/worked-task.md#document-to-csv-verify-each-extracted-value).

## Bring your agent

Give an agent this repository link and this request:

```text
Read guide/agent-entry.md
in this repository. Help me
complete one useful task
with the guide. Adapt to my
experience and tools. Start
by finding out what I want
to accomplish; teach through
the work and show evidence
before calling it done.
```

The [agent entry](guide/agent-entry.md) is a short route through the guide, with readiness checks and stopping points. It works by reading ordinary Markdown; no special integration is required. [llms.txt](llms.txt) is a navigation index, not a promise that every agent discovers it automatically.

## Choose a chapter

- [First task](guide/first-task.md): complete one small change and check it yourself.
- [The working loop](guide/workflow.md): give a clear brief and review the result.
- [Context that earns its place](guide/context.md): help the agent follow the project with small, useful instructions.
- [Verification](guide/verification.md): check actual behavior.
- [Recovery](guide/recovery.md): get a stalled session to a known state and choose the next diagnostic step.
- [Working as a team](guide/team-practice.md): agree boundaries and leave a useful handoff.
- [Advanced practice](guide/advanced.md): choose tools and automation for repeated or larger work.
- [Platform notes](guide/platforms.md): verify details in your environment.

Read [one worked task](examples/worked-task.md) to see the brief, review, failure, and lesson fit together. Use the [templates](templates/README.md) when an empty page is slowing you down.

## The habits this guide teaches

1. **Make the outcome observable.** Describe what a person can do when the task works.
2. **Give context a job.** Include what changes a decision; link to the rest.
3. **Keep changes recoverable.** Know the starting state and the limits of undo.
4. **Inspect behavior.** A convincing explanation cannot establish that a button works.
5. **Let useful work compound.** Turn a verified lesson into a small rule, check, or reusable workflow.

These are editorial recommendations, not claims that one method wins for every task. Product behavior is separated into dated [platform notes](guide/platforms.md); primary evidence and its limits are in [sources](maintenance/sources.md).

## Keep it useful

Capture a candidate with the [lesson template](templates/lesson.md). Each week, review a small set of proposed additions, corrections, and deletions. A discovery earns a place when it changes a useful decision and has enough evidence to support it. Quiet weeks are welcome.

The [maintenance process](maintenance/README.md) includes source checking, a human review packet, and an explicit adoption gate. Automation prepares evidence; a maintainer decides what becomes guidance.

## Contribute

Improve a reader's next action. Prefer a concrete example, a corrected claim, or a clearer decision over another link. See [CONTRIBUTING.md](CONTRIBUTING.md) and the contributor instructions in [AGENTS.md](AGENTS.md).

Local checks require Python 3.11 or later and no third-party packages:

```sh
python scripts/check_guide.py
python -m unittest discover -s tests -v
```

The guide and scripts are available under the [MIT License](LICENSE).

Editorial baseline: **2026-10-17**. A source's verification date records when it was read; it does not guarantee that a product is unchanged today.
