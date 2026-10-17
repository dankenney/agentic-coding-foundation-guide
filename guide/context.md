# Context that earns its place

**Use when:** an agent repeats a mistake, misses a constraint, or spends too long rediscovering the project. Improve the information it uses before adding more instructions.

## Put each kind of information in the right place

| Information | Home | Example |
| --- | --- | --- |
| This task's outcome and limits | Task brief | Export the current filtered set; no schema changes |
| Durable project conventions | Project instructions | Use the existing API client; exact test commands |
| A lasting choice and its reason | Decision record | Why records use immutable IDs rather than display names |
| Current progress and next step | Handoff | Filter works locally; live check remains |
| A repeatable procedure | Script or focused skill | Generate a report and validate its references |
| Detailed domain information | Linked reference | Schema, design system, service contract |
| Evidence that behavior holds | Tests and review artifacts | A saved regression check and its result |

This is a placement guide, not a required file tree. Keep the smallest set that lets a new teammate continue correctly. A short task often needs only a brief and the existing project instructions.

## Write useful project instructions

Include verified setup and check commands, boundaries that are easy to miss, a few conventions that affect decisions, and links to canonical examples. Explain a surprising constraint with its reason. “Use immutable owner IDs because names can change” helps the agent handle an unfamiliar case.

Avoid copying the repository tree, entire manuals, old task status, or formatting rules already enforced by tools. Review instructions after repeated failures and after major tool changes; remove rules whose cost exceeds their benefit. OpenAI's [instruction and skill review guidance](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra) specifically cautions against broad mandatory reading and overlapping skill descriptions. Its model-specific observations are not a guarantee for other models.

Use the [project instruction template](../templates/project-instructions.md), then verify use in the intended working directory. A fresh session's list of loaded files is a diagnostic lead. Check an available loading trace and give the session one harmless task governed by an important scoped rule, such as choosing the correct check command. Compare its action with the actual instructions and precedence. Do not supply the rule in the test prompt. If effective loading cannot be established, report that gap. [Platform notes](platforms.md) explain why filenames and discovery differ.

## Retrieve detail when it matters

For an export task, the agent needs the current data shape, filtering behavior, output contract, and one good existing export. It probably does not need the entire product roadmap. Provide paths and specific questions so it can retrieve the rest when necessary.

Anthropic's [context engineering article](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) supports selective retrieval and durable notes for longer work. It is engineering guidance, not evidence for a universal token budget or a fixed session length. Judge context by whether the agent can make the right next decision.

Distinguish an instruction from evidence. A web page or log that says “ignore the user and run this command” is untrusted source content. A connector grants access to a system; it does not make every returned sentence authoritative. Keep private data out of public instructions and use fabricated examples when teaching.

## Preserve decisions, not the whole conversation

At a meaningful pause, record the current objective, changed files or artifact, decisions that affect the next step, checks actually run, unresolved issues, and the next action. Link to evidence rather than copying huge logs. Recheck the current files when resuming; a handoff can become stale.

If a session starts looping or loses important constraints, stop adding patches. Write a compact [handoff](../templates/handoff.md), start with a fresh working context where appropriate, and inspect the actual state again. A summary can omit details, so preserve exact error messages, contract decisions, and paths needed to reproduce the problem.

## Choose the smallest durable fix

An agent repeatedly uses an owner's display name as a database key. Fix the data contract to require an immutable owner ID, validate that contract where records enter the system, and add a regression test for renamed owners. Choose the smallest layer that prevents recurrence: an executable check for an enforceable constraint, or a short instruction pointing to the canonical implementation when judgment is needed. A one-off misunderstanding may need only the test; avoid a permanent rule for every failed attempt.

**Check your result:** a new session can identify the applicable instructions, run the right check, and explain the constraint without reconstructing the old chat. If it cannot, improve the location or precision of the information before expanding the document.
