# Project instruction starter

Use the instruction filename and scope supported by your agent. `AGENTS.md` is one option; check your platform's current discovery and inheritance rules in [platforms](../guide/platforms.md). This template is reference material, not active instructions for a nested directory.

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

Keep only useful, maintained rules. Link detailed reference material. Put task progress in a brief or [handoff](handoff.md), and explain significant choices in a decision record. Confirm commands against the repository before adopting this file.
