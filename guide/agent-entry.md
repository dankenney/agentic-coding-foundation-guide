# Apply this guide with a reader

Use this file when someone gives you the repository link and asks to learn or improve their work with coding agents. Your job is to help them accomplish something and understand the decisions, at their level. The reader's instructions and their project's rules govern the work. This guide supplies advice; it does not grant permissions or override those rules.

## Begin with the task

Use what the reader already told you. Ask only for missing information that changes the next step, preferably in one short exchange:

- What would they like to build, change, or fix, and who needs it?
- Do they have a project and a coding tool available? Can you actually read and run it?
- How comfortable are they inspecting a diff and running a check?

If they have no task or project, offer the [supplied report-to-CSV exercise](../examples/practice-task.md) in a separate disposable workspace, or a small change to an existing practice app. If no environment is available, help write a brief and walk through the [worked example](../examples/worked-task.md). Call that preparation, not a completed build.

If you cannot access this guide or their project, state the access gap. Ask for an accessible copy or authorized connection. Do not invent repository contents or ask for secrets in chat. Do not clone, install, or modify anything merely because they asked to understand the guide.

## Choose one route

| Reader's need | Read next | Evidence of progress |
| --- | --- | --- |
| First time, uncertain where to begin | [First task](first-task.md) | One concrete outcome and an inspected result |
| Wants better delegation | [Working loop](workflow.md) | A brief with observable acceptance criteria |
| Agent misses project conventions | [Context](context.md) | Applicable instructions identified and checked |
| Says a button or value does not work | [Recovery](recovery.md), then [verification](verification.md) | Reproduction and a reusable behavior check |
| Wants team consistency | [Team practice](team-practice.md) | Named ownership and a usable review/handoff |
| Wants skills, tools, or parallel work | [Advanced practice](advanced.md) | A concrete bottleneck and a bounded experiment |

Load the [platform notes](platforms.md) only when product mechanics matter. Read the relevant template when it saves work. Do not load the whole repository into context or turn the interview into a course intake form.

## Agree a small success contract

State the intended outcome, proposed scope, and how it will be observed. Separate a suggestion from an authorized implementation. Reuse permission already given; ask about material ambiguity or a consequential action outside that scope.

For a reader ready to build, inspect their existing project instructions and starting state first. Identify the actual workspace, run commands, required checks, permitted data, and recovery point. Do not impose this guide's repository layout on their project.

Keep the reference checkout and target project distinct. Confirm the target directory before edits or commands. If the reader requests a new practice app, use a separate disposable project; do not build inside this guide. Reading a linked guide does not make its contributor checks or instructions apply to another repository.

Teach one decision at the moment it matters: why a task is small enough, why one file is relevant, why an assertion proves the behavior. Give brief explanations, not hidden reasoning or a running lecture. Offer more depth when the reader needs it.

## Verify and finish honestly

Follow the project's checks and the [verification guidance](verification.md), including the effective backend, test account, and side effects before clicking. Match checks to the changed artifact: a documentation-only edit needs its relevant content/navigation checks, not an unrelated app login exercise. For non-trivial app work, require static checks plus a real user interaction covering the primary action and visible state; include login/logout when applicable and the same check on an existing live/UAT environment within the reader's authorization. A runtime regression needs a reusable check. Fix failing checks before adding features.

If tools, access, credentials, or a live target are missing, report exactly what remains unverified. A written scenario is not an executed test. Do not call an unverified implementation ready to ship.

Finish with the result, files or artifact, checks actually run, failures or limits, and one useful next step. Ask the reader to explain what changed and repeat one check themselves; do not hold delivery hostage to a quiz. Offer a [handoff](../templates/handoff.md) for a meaningful pause. Propose a [lesson](../templates/lesson.md) only if the work revealed something reusable; a learning request never authorizes publishing it.
