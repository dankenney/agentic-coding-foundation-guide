# A first task with everything supplied

**Use when:** you have a coding agent but no project yet. Build a small report-to-CSV converter in a separate disposable workspace. The inputs are made up, no accounts or network access are needed, and the result has a precise check.

You need a tool that can read files and run a small program, or a teammate who can run it with you. Reading the exercise and drafting code without running it is preparation; report that limit.

## The job

A two-page report lists request counts by region. Turn it into a CSV that another person can use without guessing where the numbers came from.

- [Original report](fixtures/report.txt) → [expected CSV](fixtures/report-expected.csv)
- [Revised report](fixtures/report-revised.txt) → [expected revised CSV](fixtures/report-revised-expected.csv)
- [Ambiguous report](fixtures/report-ambiguous.txt) → fail clearly; do not create an output

The contract is deliberately small: columns `region,request_count,source_page`, one row per region, in report order. `source_page` is the printed page marker in the input, not a line number. Counts are integers; `not reported` becomes an empty field. A repeated region is ambiguous and must produce an error. Never invent a count or reuse a previous result.

## Give the agent this task

```text
Use examples/practice-task.md in this guide. In a separate disposable
workspace, build a small command-line converter with an input path and
output path. Use an available language/runtime and its standard library.
Keep the guide and fixtures unchanged; do not install packages or connect
services. Read any instructions that apply to the target workspace.

Follow the contract and use the supplied reports as inputs. Refuse an
existing output path so a rerun cannot silently replace earlier work.
For invalid input, exit unsuccessfully with a useful error and leave no
output. Run the original, revised, ambiguous, and existing-output cases.
Compare the actual CSV values against the independent expected files.
Show exact commands, actual results, and any checks you could not run.
```

If no runtime is available, choose an approved environment before treating the task as executable. Do not let the agent turn a setup gap into a package installation or a subscription decision without explaining what is needed.

## Inspect the result yourself

1. Open the original output: exactly two rows, North 12 on page 1 and South 8 on page 2, with the agreed header.
2. Open the revised output: North changes to 14 and East appears on page 3 with a blank count. This catches a converter that hard-codes the first example or carries stale data forward.
3. Run the ambiguous input to a new output path: a nonzero exit and a clear duplicate-region error; no output file exists.
4. Rerun against an existing output: a nonzero exit and the previous file is unchanged.

Compare parsed CSV fields and row order, allowing normal platform differences in line endings. Ask the agent which code preserves page provenance and rejects ambiguity. Change one valid count in a **copy** of the source, predict the output, and check it again. Expected files are independent checks; changing them to match incorrect output does not fix the converter.

**Done means:** a real program ran, the delivered files match both valid cases, invalid/rerun behavior is demonstrated, and you can repeat one check. Save the run command and any limits in a short [handoff](../templates/handoff.md). Continue with [the working loop](../guide/workflow.md) when you have a task from your own work.
