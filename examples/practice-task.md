# Practice task: convert a report to CSV

If you have a coding agent but no project yet, try this small report-to-CSV converter. Work in a new empty folder outside the guide. The reports are made up, and the expected CSV files give you a way to check the result. Fetch the linked exercise files first; after that, the program and checks run offline without connected accounts.

You'll need a tool that can create files and run a program, or a teammate who can run it with you. Ask the agent which language is already available before choosing one. With a chat-only tool, use the [short CSV walkthrough](worked-task.md#document-to-csv-verify-each-extracted-value) to prepare the brief and compare rows. You won't have built or run a converter yet.

## The job

A two-page report lists request counts by region. Convert it to CSV and keep each count's printed page number so someone can check it against the source.

- [Original report](fixtures/report.txt) → [expected CSV](fixtures/report-expected.csv)
- [Revised report](fixtures/report-revised.txt) → [expected revised CSV](fixtures/report-revised-expected.csv)
- [Ambiguous report](fixtures/report-ambiguous.txt) → fail clearly; do not create an output

Use the columns `region,request_count,source_page`, with one row per region in report order. `source_page` is the printed page marker in the input, not a line number. Counts are integers; use an empty field for `not reported`. If a region appears twice, the input is ambiguous and the program must return an error. Don't invent a count or reuse a previous result.

## Give the agent this task

```text
Use examples/practice-task.md in this guide. Work in this new empty
folder outside the guide: [folder I authorize you to use]. Build a small
command-line converter with an input path and output path. Use an already
available language and its standard library. Fetch the linked exercise
files before starting, then run offline. Keep the guide and fixtures
unchanged; do not install packages or connect services. Read any
instructions that apply to the target folder.

Follow the contract and use the supplied reports as inputs. Refuse an
existing output path so a rerun cannot silently replace earlier work.
For invalid input, exit unsuccessfully with a useful error and leave no
output. Run the original, revised, ambiguous, and existing-output cases.
Compare the actual CSV values against the independent expected files.
Show exact commands, actual results, and any checks you could not run.
```

Replace the folder placeholder before sending the request. You don't need to set up Git for this exercise. Keep the inputs unchanged and use a new output name for each run. If no language can run in the folder, use the walkthrough or choose an approved environment first. Ask the agent to explain the setup gap before proposing installations or a subscription.

## Inspect the result yourself

1. Open the original output: exactly two rows, North 12 on page 1 and South 8 on page 2, with the agreed header.
2. Open the revised output: North changes to 14 and East appears on page 3 with a blank count. This catches a converter that hard-codes the first example or carries stale data forward.
3. Run the ambiguous input to a new output path: a nonzero exit and a clear duplicate-region error; no output file exists.
4. Rerun against an existing output: a nonzero exit and the previous file is unchanged.

Compare parsed CSV fields and row order, allowing for normal differences in line endings across platforms. Ask the agent to show you the code that preserves printed page numbers and rejects duplicate regions. Then change one valid count in a **copy** of the source, predict the output, and run it again. Keep the expected files unchanged so they can check the converter independently.

You've finished when the program has run, both valid outputs match, you've checked invalid input and rerun behavior, and you can repeat a check yourself. Save the run command and any limits in a short [handoff](../templates/handoff.md). When you're ready to try a task from your own work, use [the working loop](../guide/workflow.md).
