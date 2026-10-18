# Your first task

Start with one small change that you understand well enough to check yourself. You can learn these habits with an approved coding tool and a practice project; there's no need to assemble a new set of tools first.

## Choose an outcome you understand

Choose a project you're allowed to change. An existing, working project gives you something to compare before and after. If you don't have one, use a disposable practice folder and made-up data.

The [report-to-CSV practice task](../examples/practice-task.md) supplies the input files, expected outputs, and failure cases. It's a useful starting point if you'd rather try the process before designing an app or connecting a service.

Other good first tasks include clearer form validation, a filter on a small list, or a script that converts a sample file into a specified output. Pick something you can describe in a sentence and check in a few actions. Save production permissions, payments, and data migrations for work that someone responsible for those systems can help review.

A few terms will come up: a **repository** is the project's versioned folder, a **diff** shows file changes, and a **commit** saves a snapshot in version control. A **preview** is a running copy you can try. It may differ from the version people use.

## Orient before changing

Ask your agent:

```text
Help me understand this project for this task: [outcome]. Read the
applicable project instructions and inspect the relevant files. Tell me
how to run it, which checks apply, and what is already changed. Don't
change files yet. Explain unfamiliar terms briefly as they come up.
```

In an existing project, ask for the actual run commands and check that the app or script runs before changing it. Keep any existing work and identify a starting point you can restore through the project's version control. Find out what that restore covers. In a new practice folder, you can begin with the supplied inputs; you don't need an existing app or Git setup.

Before trying buttons or entering data, check which backend the running copy uses. A local preview can still connect to production. Use disposable data and a test account where needed. If you can't tell what an interaction might change, pause it and check the setup in the [verification guide](verification.md#before-an-interaction-check).

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

Replace the example with your own task. Say what you want, what limits apply, and how you'll check the result. Resolve any decision that could change the intended outcome before implementation. Ask for a plan if the task is large or uncertain; a clear, small change usually needs only a short explanation of the approach.

## Watch the result, then inspect the change

Try the filter yourself. Check that selecting an owner changes the list, reset restores it, and an empty result makes sense. If the selection should persist, refresh and check it. Then open the changed files or diff with the agent and ask it to connect the code to what you observed.

To understand more of the implementation, predict what a small example will do, then try a variation. Follow one value from input through any API (a service interface) and storage to the screen. For a script, follow it from source file to output. Explain where the value could become stale, who may access it, and what the design trades off in reliability or cost. This is one way to practice [software fundamentals](https://www.linkedin.com/pulse/ai-engineering-skills-map-software-fundamentals-andrew-ng-7lnac) on your own task.

Look for changes you didn't ask for, too. A new package or a changed permission file deserves an explanation. You don't need to understand every line, but you should know what changed, how it was checked, and who can review the parts you can't yet assess.

If something fails, record the steps you took and what you saw, then use the [recovery guidance](recovery.md). Give the agent that evidence before asking it to try another fix.

## Finish with something you can resume

Before you stop, ask for a short handoff with the changes, run command, actual check results, remaining limits, and next step. Use your team's normal review process before sharing or deploying the result.

You've completed the exercise when you can show the result, find the changed files or diff, and repeat a check. Use [the working loop](workflow.md) when you're ready to apply the process again. The [worked task](../examples/worked-task.md) includes a full brief and review.

## Choose what to practice next

DeepLearning.AI's [AI Engineering Skills Map](https://www.linkedin.com/pulse/ai-engineering-skills-map-andrew-ng-m479c/) can help you choose what to learn next. The exercises below are our suggestions. Pick one that addresses a gap you noticed in the task.

| Gap | Next exercise |
| --- | --- |
| Unsure whether a feature helps | [Working loop](workflow.md#define-the-outcome): name one assumption and evidence that would stop the build. |
| Cannot explain the data flow | [Recovery](recovery.md#find-where-the-behavior-breaks): trace one working value and explain what survives a refresh or rerun. |
| Cannot judge “done” | [Verification](verification.md): derive one expected output from made-up input and compare the actual result. |
