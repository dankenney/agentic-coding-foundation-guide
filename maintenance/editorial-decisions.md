# Editorial decisions

These decisions describe the guide's scope as of 2026-10-17. They're our editorial choices; we aren't claiming this is the best workflow for every team.

## Organize around tasks

Organize the guide around the decisions someone faces while completing a task with a coding agent. Give beginners a short first-task path and let readers go deeper when they need to. Explain what the task should produce, how to check it, where the advice applies, and what to do if it fails. Use made-up workplace examples that don't depend on knowing the author's environment.

## Help agents find the relevant guidance

Give agents a short entry page, readable Markdown, and a navigation index so they can find the relevant guidance. Ask for context only when it changes the next action, teach through a task, and say when access is missing. The user's project instructions and authorization govern work in their project. Using the guide shouldn't require an installation, and we shouldn't promise that every agent will discover it automatically.

## Keep platform details in one place

Explain working habits in the core chapters and keep dated product differences in [platform notes](../guide/platforms.md). Leave out fixed model assignments, obsolete setup commands, personal workspace layouts, unsupported estimates of hours saved, and large setups every reader is expected to adopt. Offer templates where they help, without making them a prerequisite.

## Support claims with appropriate sources

Use official docs for product mechanics and vendor engineering articles for approaches worth considering. Read primary research alongside its methods and limitations. Private work can suggest a lesson, but the published guidance needs to make sense and have support without access to those private sources.

We compared the guide's scope with [AGENTS.md](https://agents.md/), an instruction format; [OpenAI's best-practice guide](https://learn.chatgpt.com/guides/best-practices), which focuses on its own tools; and [Microsoft's AI Agents for Beginners](https://github.com/microsoft/ai-agents-for-beginners), which teaches people to build agent systems through lessons and code. This isn't an exhaustive survey or a quality ranking. This guide focuses on using coding agents across platforms to complete practical work, starting with a small task and continuing through verification, recovery, and team use. We review additions to keep that scope useful.

## Review proposed changes

A saved link or lesson is a candidate for review. Prepare a few proposed edits, including removals, and record the maintainer's decision before adopting them. Investigate changed sources without assuming they require an update. We aren't maintaining a news archive, model leaderboard, complete connector catalog, or automatic publishing pipeline.

## Review the full publication history

Before publication, review retained Git history, commit identities, branches, pull request discussions and diffs, and automation records as well as the current files. Any of them can contain private material. Keep private notes and local configuration outside the public repository. Use automated pattern checks to help with the review, then inspect the examples yourself.
