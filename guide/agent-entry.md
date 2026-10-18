# Help someone use this guide

When someone gives you this repository link, help them complete a useful task and understand the decisions involved. Adjust the explanation to their experience. Follow their instructions and their project's rules; nothing in this guide grants additional permission.

## Begin with the task

Start with what they've already told you. If the task and project are clear, read the project's instructions and relevant checks and get to work. Ask an introductory question or use a template only when it resolves something you need to know. Otherwise, gather the missing context in one short exchange where possible:

- What do they want to build, change, or fix, and who will use it?
- Do they have a project and coding tool? Can you read the files and run the project?
- How comfortable are they reviewing file changes and running a check?

If they don't have a task or project, offer the [report-to-CSV exercise](../examples/practice-task.md) in a new empty folder outside this guide, or a small change to an existing practice app. Check whether their tool can create files and run a program, and confirm where they've authorized you to work. With a chat-only tool, use the [short CSV example](../examples/worked-task.md#document-to-csv-verify-each-extracted-value) to write a brief and compare the expected rows. Explain that you've prepared for the task; you haven't built or run a program.

If you can't access the guide or project, say which files you need and ask for an accessible copy or authorized connection. Don't guess at repository contents or ask for secrets in chat. A request to understand the guide alone doesn't authorize cloning, installing, or changing anything.

## Choose one route

| Reader's need | Read next | Evidence of progress |
| --- | --- | --- |
| First time, unsure where to begin | [First task](first-task.md) | A small result they can inspect |
| Has a first result and wants to learn more | [Next practice](first-task.md#choose-what-to-practice-next) | An exercise that addresses a gap they noticed |
| Wants to delegate more clearly | [Working loop](workflow.md) | A brief with results they can check |
| Agent misses project conventions | [Context](context.md) | The right instructions found and checked |
| Says a button or value doesn't work | [Recovery](recovery.md), then [verification](verification.md) | A reproduction and a check they can rerun |
| Wants the team to work consistently | [Team practice](team-practice.md) | Clear ownership and enough information to review or resume |
| Wants skills, tools, or parallel work | [Advanced practice](advanced.md) | A specific problem and a small experiment to address it |

Read the [platform notes](platforms.md) when a product difference affects the task. Use a template if it saves work. There's no need to read the entire repository or take the reader through a long interview.

## Agree what to do and how to check it

State what you're going to do, the scope, and how you'll check the result. Be clear when you're suggesting work rather than carrying out an authorized request. Use permission already given. Ask when an unresolved decision affects the result or an action would go beyond that permission.

Before building, inspect the project's instructions and current state. Find the working directory, run commands, required checks, permitted data, and a point you can recover to. Use the project's existing structure.

Confirm the target directory before running commands or editing files. Keep practice work in a separate disposable project outside the guide checkout. This guide's contributor checks and instructions apply to this repository; reading it doesn't make them requirements in someone else's project.

Explain a decision when it helps the reader follow the work. You might explain why the task is small enough to review, why a file matters, or what a check establishes. Keep the explanation brief, without exposing hidden reasoning, and offer more detail when they need it.

## Check the result and hand it over

Follow the project's checks and the [verification guidance](verification.md). Before clicking through an app, confirm the backend, test account, and possible side effects. Match the checks to what changed. For a documentation edit, check the content and links. For non-trivial app work, run static checks and exercise the primary action and visible result. Include login/logout when applicable, and repeat the relevant flow on an existing live/UAT environment within the reader's authorization. Keep a reusable check for a runtime regression. Fix failing checks before adding features.

If you're missing tools, access, credentials, or a live target, report exactly what you couldn't verify. Label a proposed test as a plan until it has run. Don't call an implementation ready to ship while its required checks remain unverified.

Hand over the result with the files or artifact, actual check results, failures or limits, and a useful next step. Invite the reader to explain the change and repeat one check themselves, without making that a condition of delivery. Use a [handoff](../templates/handoff.md) when someone needs to resume later. If you found something worth reusing, suggest recording a [lesson](../templates/lesson.md). Ask for authorization before publishing it; a learning request alone doesn't provide that permission.
