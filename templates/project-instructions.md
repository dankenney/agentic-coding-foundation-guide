# Project instruction starter

Choose an instruction filename and scope your agent supports. `AGENTS.md` is one option; check the current discovery and inheritance rules in [platform notes](../guide/platforms.md). Copy the template into your project when you're ready to use it. It doesn't govern work in this guide's template directory.

```markdown
# Project instructions

Purpose: [what this project does and who uses it]

Read first: [small set of relevant entry points]
Architecture: [boundaries and source-of-truth files]

Commands:
- Setup: [command]
- Run: [command]
- Lint/build/tests: [commands]
- Runtime or artifact check: [command and required environment]

Conventions: [important practices that are not obvious from the code]

Boundaries: [data, tools, environments, and actions requiring authorization]

Verification: [what evidence is required for each relevant change type]
If behavior fails: reproduce, fix stability, rerun the original check.
Report actual results and checks not run.
```

Keep the rules you can maintain and link to detailed reference material when needed. Use a brief or [handoff](handoff.md) for task progress and a decision record for significant choices. Check the commands against the repository before adopting the file.
