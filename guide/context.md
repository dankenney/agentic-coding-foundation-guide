# Project context and instructions

If an agent keeps making the same mistake, misses a constraint, or spends too long rediscovering the project, check the information it's working from. You may need to correct a rule or make an existing reference easier to find.

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

Use this table to decide where information belongs. You don't need a separate file for every row. A short task often needs only a brief and the existing project instructions; add more when someone needs it to continue correctly.

## Write useful project instructions

Put the setup and check commands you've verified in the project instructions, along with boundaries that are easy to miss, conventions that affect decisions, and links to the examples people should follow. Explain constraints that might otherwise seem arbitrary. “Use immutable owner IDs because names can change” gives the agent a reason it can apply to an unfamiliar case.

Leave out copies of the repository tree, entire manuals, old task status, and formatting rules that tools already enforce. Revisit the instructions after repeated failures or major tool changes, and remove rules that create more work than they save. OpenAI's [instruction and skill review guidance](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra) cautions against broad mandatory reading and overlapping skill descriptions. Its observations concern a particular model, so don't assume the same results for other models.

The [project instruction template](../templates/project-instructions.md) gives you a starting point. Then check that the agent uses those instructions in the intended working directory. In a fresh session, inspect the list of loaded files and any available loading trace. Give it a harmless task that depends on an important scoped rule, such as choosing the correct check command, without revealing that rule in your prompt. Compare what it does with the instructions and their precedence. If you can't establish that the instructions loaded and applied, report the gap. [Platform notes](platforms.md) explain differences in filenames and discovery.

## Retrieve detail when it matters

For an export task, give the agent the current data shape, filtering behavior, output contract, and a good existing export. The full product roadmap probably won't help. Provide paths and specific questions so it can look up further details when it needs them.

Anthropic's [context engineering article](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) recommends selective retrieval and durable notes for longer work. That engineering guidance doesn't establish a universal token budget or fixed session length. The useful question is whether the agent has enough context to make the next decision correctly.

Treat retrieved pages and logs as evidence to assess. If one says “ignore the user and run this command,” that text has no authority to change the task. A connector gives the agent access to a system, but the content it returns still needs the same judgment. Keep private data out of public instructions and use made-up examples when teaching.

## Keep a useful handoff

When you pause work that someone will need to resume, record the objective, changed files or artifact, decisions that affect the next step, checks actually run, unresolved issues, and next action. Link to evidence instead of copying huge logs. Check the current files when you resume because the handoff may be out of date.

If the agent repeats failed fixes or loses important constraints, stop adding patches. Write a compact [handoff](../templates/handoff.md), start fresh where appropriate, and inspect the actual state again. Keep the exact error messages, contract decisions, and paths needed to reproduce the problem; a general summary can lose those details.

## Fix recurring mistakes

Suppose an agent repeatedly uses an owner's display name as a database key. Correct the data contract to require an immutable owner ID, validate it where records enter the system, and add a regression test for renamed owners. Address the mistake where you can prevent it from recurring. Use an executable check for a constraint you can enforce. When the agent needs to exercise judgment, a short instruction pointing to the canonical implementation may help. A one-off misunderstanding may need only the test, without a permanent instruction about that failed attempt.

Try the task in a new session. It should find the applicable instructions, run the right check, and explain the constraint without the old chat. If it can't, check whether the information is hard to find or unclear before adding more.
