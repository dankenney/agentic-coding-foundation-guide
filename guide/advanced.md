# Reuse workflows and add automation

Repeated work or a specific bottleneck gives you a reason to add a script, skill, tool, or automation. Start with the simplest option that addresses it.

## Choose what to add

| Repeated problem | Smallest useful response | Evidence before expanding |
| --- | --- | --- |
| A deterministic transformation is repeated | Script with explicit input/output and failure handling | Known fixtures, useful errors, reproducible outputs |
| Agents miss a repository convention | Concise project instruction plus a canonical example | A fresh session follows it on the relevant task |
| A multi-step judgment workflow repeats | Focused skill or saved procedure | Realistic cases, clear trigger, inspected final artifacts |
| Relevant facts live in another system | Scoped connector/tool access | Correct source, least needed access, known side effects |
| Independent work can proceed together | Parallel agents with distinct ownership | Integration cost is lower than the time saved |
| A stable task should recur | Scheduled run with an owner and review path | Fresh inputs, successful runs, failure reporting, retirement rule |

## Try the workflow before making it reusable

Work through a representative task with an agent first. Identify what you provide, which decisions you make, how you check the output, and how to handle failure. Save the steps you'll repeat, using scripts for deterministic logic and short procedures for judgment.

A skill needs to say when to use it, what it produces, and what supporting material to read along the way. Check how your platform discovers and runs skills; a portable Markdown file may run differently between platforms. OpenAI's [skills guidance](https://developers.openai.com/plugins/concepts/skills) distinguishes tools, which provide live capabilities, from skills, which organize work around them.

Try the procedure on a normal case, an edge case, and a case where it should decline or ask for missing information. Read the output and inspect its actions; successful invocation alone tells you little. A single preference usually needs a sentence in your instructions rather than its own skill.

For a worked example, see the [UX lens skill](../examples/skills/ux-lens/SKILL.md). It reviews business-app screens and flows in three modes (brief, review and walk). It says what it won't review (code and back ends), and it adds a section for apps whose figures get audited. It was tried on a normal screen review, a single read-only screenshot with missing states, and a request to review a function's performance. The second case added its "not seen" verdict, and the third added its scope section.

## Connect a service for a specific task

Before connecting a service, describe the work it will handle and the data and actions it needs. Read access may be enough to test the idea. Inspect tool definitions, dependencies, and supporting scripts before enabling a new package. Give credentials only the permissions required, and keep them out of tracked examples.

Record the connected account, effective permissions, owner, and how to revoke access, including signed-in browser sessions. Before allowing unattended writes, test stopping the job and revoking its write access with a disposable connection. You'll still need to address any changes it made before you stopped it.

Decide what the agent can read, change, execute, send, spend, or deploy, and enforce the important limits through environment and account controls. Retrieved documents, logs, and ordinary source content may contain misleading instructions; treat them as evidence to assess. Recognized project instructions still apply under the user's and platform's governing rules. Anthropic's [tool design guidance](https://www.anthropic.com/engineering/writing-tools-for-agents) recommends distinct capabilities, relevant outputs, and realistic evaluations. Assess each connector yourself; the article doesn't establish whether a particular connector is safe or reliable.

## Split work that can proceed independently

Parallel agents can help with researching separate systems, reviewing a fixed diff, or implementing separate modules against an agreed interface. Give each agent a specific output, files it owns, assumptions to check, and a stopping condition. Assign someone to integrate and verify the result.

Separate branches or worktrees can keep independent edits apart. A worktree is a separate working checkout that shares Git history; credentials, databases, and external services need their own isolation. Coordinate agents that change the same files or fixture data. Consider whether the time saved is worth the extra review, integration, cost, and ways the work can fail.

## Choose a model for the task

Use an approved model that's capable of your usual work. Consider more reasoning or another model for a difficult diagnosis, unresolved design tradeoffs, or repeated failures after checking context and environment. Compare a few representative tasks using the same inputs, tools, and acceptance checks. Include cost, elapsed time, review effort, and failed attempts.

Treat small leaderboard differences cautiously. Anthropic's [infrastructure-noise study](https://www.anthropic.com/engineering/infrastructure-noise) shows that evaluation resource settings can change coding scores in particular benchmark setups. It can't forecast performance on your team's work. The practical recommendation is to compare the complete setup, including tools and environment.

## Maintain what you automate

Write down when the automation runs, its inputs and freshness requirements, allowed actions, output location, owner, and when to stop or retire it. Decide how failures will reach the owner. Set limits on time, usage or spend, and retries; enforce them where supported, stop when reached, and report why. Give temporary increases an expiry. Check that each run produces current, useful output. Starting on schedule doesn't mean it finished its work.

Start with a trial that proposes actions without external writes. Review the proposals and test an input failure and recovery. Enable writes once you have evidence that it handles the expected work and failures. A run that checks everything and finds no change can be successful. Missing required coverage needs attention.

For external writes, use a stable operation identifier and duplicate prevention enforced by the destination, where supported. Otherwise, avoid concurrent writers and check whether an earlier attempt took effect before retrying. If a ticket-creation request times out, the ticket may already exist. Adding a label won't prevent a duplicate. When you can't establish the outcome, stop and alert the owner. Test this lost-confirmation case before allowing unattended writes.

When collecting lessons for a guide or team, let automation propose changes for a person to accept. A script doing stable, deterministic work may need less supervision. Review the workflow when its model, tools, permissions, dependencies, or expected inputs change. If a recurring digest stops helping anyone make a decision, narrow it or retire it.

Check whether the addition removed the bottleneck you started with. You should be able to inspect its results and recover when it fails. If maintaining it takes more effort than the work it saves, simplify it.
