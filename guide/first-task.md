# Your first useful task

**Goal:** complete one small change you can recognize and check. You do not need a custom agent stack, a prompt library, or a new subscription to learn the working habits.

## Choose an outcome you understand

Use an approved coding tool and a project you are allowed to change. An existing, working project is a good place to start because you can compare before and after. If you have no project, practice with a disposable example and made-up data.

For a ready-made starting point, use the [report-to-CSV practice task](../examples/practice-task.md). It supplies input files, exact expected outputs, and failure cases. You can complete it without designing an app or connecting a service.

Good first tasks include clearer validation on a form, a filter on a small list, or a script that converts a sample file into a specified output. Pick something you can describe in one sentence and verify in a few actions. Defer production permissions, payments, and data migrations until someone responsible for those systems can help review them.

A **repository** is the project's versioned folder. A **diff** shows the file changes. A **commit** is a durable snapshot in version control. A **preview** is a running copy you can try; it may differ from the deployed version people use.

## Orient before changing

Ask your agent:

```text
Help me understand this project for this task: [outcome]. Read the
applicable project instructions and inspect the relevant files. Tell me
how to run it, which checks apply, and what is already changed. Don't
change files yet. Explain unfamiliar terms briefly as they come up.
```

Have it show the actual commands from the project instead of guessing. Confirm that the app or script currently runs. Preserve existing work and identify a recoverable starting point with the project's version control. A backup or checkpoint is useful only if you know what it restores.

Before trying buttons or entering data, confirm which backend the running copy uses. A local preview can still connect to production. Use disposable data and a test account where needed; pause an interaction if its effects are unclear. The [verification guide](verification.md#before-an-interaction-check) explains the setup.

## Give it a small, complete brief

For example:

```text
Add an owner filter to the existing request list. A user should be able
to choose an owner, see only that owner's open requests, and reset to
all open requests. Show a clear empty state when none match.

Use the existing components and data. Do not add dependencies, change
permissions, or deploy. Inspect the relevant code, describe the approach
briefly, then implement. Run the project's static checks and exercise
the filter and reset through the UI. Show what you checked and any gaps.
```

Replace the example with your task. A useful brief names the result, constraints, and evidence. If a decision would change what you want, resolve it before implementation. For a larger or uncertain task, ask for a plan first. For a clear small change, a short approach is enough.

## Watch the result, then inspect the change

Try the user action yourself. Does the list change? Does reset restore the expected list? Is an empty result understandable? If persistence matters, refresh and check it. Ask the agent to open the changed files or diff and explain how the change causes the behavior you observed.

Optionally, predict what a small example will do, try it with a few variations, and explain the behavior in your own words. Build toward harder problems as your understanding grows.

You are looking for unintended changes as well as the requested result. Why did a new package appear? Why did a permission file change? You do not need to understand every line, but you should know what changed, how it was checked, and who can review what you cannot yet assess.

If the result fails, say what happened with the exact steps and visible result. Move to [recovery](recovery.md); repeated requests to “fix it” provide little new evidence.

## Finish with something you can resume

Ask for a concise handoff: what changed, how to run it, checks and actual outcomes, remaining limits, and the next step. Use the team's normal review process before sharing or deploying it.

You have completed the exercise when you can show the changed behavior, find the relevant diff, and repeat a check. Read [the working loop](workflow.md) next to make the process easier to repeat. The [worked task](../examples/worked-task.md) shows what a complete brief and review can look like.
