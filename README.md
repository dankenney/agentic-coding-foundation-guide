# Agentic Coding Foundation

If you use coding agents at work, this guide will help you choose a useful task, give the agent what it needs, and check the result. It's written for engineers, analysts, operators, designers, and anyone building alongside them.

An agent can read a project, suggest an approach, change files, and run the tools it has access to. You decide what should happen, which constraints matter, and whether the result is ready for someone else to use.

## If you don't have a project

If you don't have a project yet, try the [supplied practice task](examples/practice-task.md). It has made-up reports and expected answers, and you won't need to connect any accounts. If your tool can't create files and run commands, use the [short CSV walkthrough](examples/worked-task.md#document-to-csv-verify-each-extracted-value) in chat.

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

The [agent entry](guide/agent-entry.md) helps the agent choose a chapter, check what it can access, and recognize when it needs to stop. It reads ordinary Markdown, so there's nothing to install. [llms.txt](llms.txt) lists the pages for agents that use it; other agents may need you to point them there.

## Choose a chapter

- [First task](guide/first-task.md): complete one small change and check it yourself.
- [The working loop](guide/workflow.md): give a clear brief and review the result.
- [Project context](guide/context.md): help the agent follow the project with small, useful instructions.
- [Verification](guide/verification.md): check actual behavior.
- [Recovery](guide/recovery.md): get a stalled session to a known state and choose the next diagnostic step.
- [Working as a team](guide/team-practice.md): agree boundaries and leave a useful handoff.
- [Advanced practice](guide/advanced.md): choose tools and automation for repeated or larger work.
- [Platform notes](guide/platforms.md): verify details in your environment.

The [worked examples](examples/worked-task.md) show how to brief a task, check the result, and investigate a failure. Use whichever parts of the [templates](templates/README.md) save you work.

## The habits this guide teaches

1. Describe what a person should be able to do when the task works.
2. Give the agent the context that affects its decisions, with links to the detail it can read when needed.
3. Know what a checkpoint or backup restores before changing files or data.
4. Try the result. Check that the button, export, or saved record behaves as intended.
5. Save a lesson as a short rule, check, or procedure when you've verified that it's worth reusing.

These are our working recommendations. Adapt them to the task. The dated [platform notes](guide/platforms.md) cover product behavior, and [sources](maintenance/sources.md) explain the supporting evidence and its limits.

## Keep it useful

If you find advice worth adding, use the [lesson template](templates/lesson.md) to record when it helps, what to do, and how you checked it. Each week, review a few proposed additions, corrections, and deletions. Some weeks there won't be anything worth adding.

The [maintenance process](maintenance/README.md) explains how to check sources and prepare changes for review. Automation can collect evidence and draft changes; a maintainer decides what goes into the guide.

## Contribute

Corrections, worked examples, and clearer explanations are welcome. Before adding a link, explain what a reader should do with it. See [CONTRIBUTING.md](CONTRIBUTING.md) and the contributor instructions in [AGENTS.md](AGENTS.md).

Local checks require Python 3.11 or later and no third-party packages:

```sh
python scripts/check_guide.py
python -m unittest discover -s tests -v
```

The guide and scripts are available under the [MIT License](LICENSE).

Editorial baseline: **2026-10-17**. Source verification dates record when a page was read. Check current documentation before relying on a product setting.
