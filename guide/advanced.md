# Add capability when the work earns it

**Use when:** a working process has a concrete bottleneck. Start with the simplest approach that solves it, and remove what stops helping.

## Choose the mechanism for the problem

| Repeated problem | Smallest useful response | Evidence before expanding |
| --- | --- | --- |
| A deterministic transformation is repeated | Script with explicit input/output and failure handling | Known fixtures, useful errors, reproducible outputs |
| Agents miss a repository convention | Concise project instruction plus a canonical example | A fresh session follows it on the relevant task |
| A multi-step judgment workflow repeats | Focused skill or saved procedure | Realistic cases, clear trigger, inspected final artifacts |
| Relevant facts live in another system | Scoped connector/tool access | Correct source, least needed access, known side effects |
| Independent work can proceed together | Parallel agents with distinct ownership | Integration cost is lower than the time saved |
| A stable task should recur | Scheduled run with an owner and review path | Fresh inputs, successful runs, failure reporting, retirement rule |

## Build a workflow before packaging it

Complete a representative task manually with an agent. Identify the inputs, decisions, outputs, checks, failure behavior, and boundaries. Then package only what repeats. Put deterministic logic in scripts and nuanced decisions in a concise procedure.

Skills should have a distinct trigger, a clear output, and supporting detail loaded when needed. Check how the target platform discovers and runs them; portability of a Markdown format does not guarantee identical execution. OpenAI's [skills guidance](https://developers.openai.com/plugins/concepts/skills) distinguishes tools that provide live capabilities from skills that organize a workflow around them.

Test a reusable procedure on a normal case, an edge case, and a case where it should decline or ask for missing information. Inspect the output and actions, not just whether the skill was invoked. Do not package a single preference as an elaborate skill.

## Add tools with a job and a boundary

Before connecting a service, name the manual loop it will remove and which data/actions it needs. Start with read access if that proves the workflow. Inspect tool definitions, dependencies, and supporting scripts before enabling a new package. Keep credentials scoped and outside tracked examples.

Record the connected account, effective permissions, owner, and revocation route, including signed-in browser sessions. Before unattended writes, test how to stop the job and revoke its write access with a disposable connection. Neither step undoes earlier effects.

Decide what can be read, changed, executed, sent, spent, or deployed. Enforce important limits through environment and account controls. Treat retrieved documents, logs, and ordinary source content as untrusted evidence. Recognized project instructions still apply under the user's and platform's governing rules. Anthropic's [tool design guidance](https://www.anthropic.com/engineering/writing-tools-for-agents) recommends distinct capabilities, relevant outputs, and realistic evaluations; this does not establish that any particular connector is safe or reliable.

## Parallelize independent uncertainty

Good candidates include researching separate systems, reviewing a fixed diff, or implementing separate modules against an agreed interface. Give each worker a bounded output, file ownership, assumptions to check, and a stopping condition. An integrator owns the combined result.

Use isolated branches or worktrees for independent edits when appropriate. A **worktree** is a separate working checkout sharing Git history; it does not isolate credentials, databases, or external services. Avoid multiple agents changing the same files or fixture data without coordination. More agents also add review, merging, cost, and failure paths.

## Choose a model by the work

Use an approved, capable default. Increase reasoning or try another model when the evidence shows a bottleneck: difficult diagnosis, unresolved design tradeoffs, or repeated failures after context and environment are checked. Compare on a few representative tasks with the same inputs, tools, and acceptance checks. Keep cost, elapsed time, review effort, and failed attempts in view.

Small leaderboard differences should not drive the process. Anthropic's [infrastructure-noise study](https://www.anthropic.com/engineering/infrastructure-noise) shows that evaluation resource settings can change coding scores. It studies particular benchmark setups, not every workplace task; the practical inference is to compare the complete working setup rather than a model name alone.

## Operate an automation as a maintained system

Specify trigger, inputs, freshness requirements, allowed actions, output location, failure signal, owner, and stop/retire condition. Set a time, usage/spend, and retry budget; enforce limits where supported, stop when reached, and report why. Temporary increases need an expiry. A scheduled invocation is not evidence that the intended work finished. Verify that outputs are current and used.

Start with a trial that proposes actions without external writes. Inspect the proposals and test an input failure and recovery before enabling writes. Graduate on demonstrated behavior, not elapsed days. A verified no-change result is valid; missing coverage is not.

For external writes, use a stable operation identifier and destination-enforced duplicate prevention where supported. Otherwise avoid concurrent writers and reconcile any existing effect before retrying. A timeout after creating a ticket may mean the ticket exists. A label alone does not prevent duplicates. If the outcome remains unknown, stop and alert the owner. Test a lost confirmation before enabling unattended writes.

For learning capture, let automation collect and propose while a person adopts changes. For stable deterministic work, a script may need less supervision. Review after changes to a model, tool, permission, dependency, or input contract. If a digest repeatedly produces no useful decision, narrow it or retire it.

**Check your result:** the added capability removes a measured obstacle, produces inspectable evidence, and remains recoverable. If the process becomes harder to explain than the work it performs, simplify it.
