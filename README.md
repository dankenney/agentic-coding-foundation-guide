# Agentic Coding Foundation

**Build something useful. Know why it works. Leave it easier to continue.**

A field guide for people who use coding agents at work: engineers, analysts, operators, designers, and the teammates building alongside them. Start with a small, useful change. Grow into systems you can inspect, trust, and maintain.

An agent can read a project, propose an approach, change files, and run tools. Your contribution is to make the work worth doing: choose the outcome, supply the context that matters, exercise judgment, and decide what evidence is enough.

## Start where you are

| What you need today | Start here | What you will leave with |
| --- | --- | --- |
| Your first useful result | [First task](guide/first-task.md) | A small change you have checked yourself |
| A better way to delegate work | [The working loop](guide/workflow.md) | A clear brief and a reviewable result |
| An agent that understands the project | [Context that earns its place](guide/context.md) | Small, useful project instructions |
| Confidence that the result works | [Verification](guide/verification.md) | Evidence from actual behavior |
| A session that has gone off track | [Recovery](guide/recovery.md) | A known state and a next diagnostic step |
| Consistent team practice | [Working as a team](guide/team-practice.md) | Shared boundaries and a useful handoff |
| Repeated or larger work | [Advanced practice](guide/advanced.md) | A reasoned choice about tools and automation |
| Tool-specific differences | [Platform notes](guide/platforms.md) | The details to verify in your own environment |

Read [one worked task](examples/worked-task.md) to see the brief, review, failure, and lesson fit together. Use the [templates](templates/README.md) when an empty page is slowing you down.

No project yet? Try the [self-contained practice task](examples/practice-task.md): supplied report files, a tiny converter, and independent expected outputs. It needs no accounts or network access.

## Bring your agent

Give an agent this repository link and this request:

```text
Read guide/agent-entry.md in this repository. Help me complete one useful
task with the guide. Adapt to my experience and tools. Start by finding
out what I want to accomplish; teach through the work and show evidence
before calling it done.
```

The [agent entry](guide/agent-entry.md) is a short route through the guide, with readiness checks and stopping points. It works by reading ordinary Markdown; no special integration is required. [llms.txt](llms.txt) is a navigation index, not a promise that every agent discovers it automatically.

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

Editorial baseline: **2026-10-17**. A source's verification date records when it was read; it does not guarantee that a product is unchanged today.
