# Platform notes

**Documentation verified: 2026-10-17.** These notes describe public documentation we read, not product behavior we tested ourselves. Check your installed version, plan, workspace, and team policy before relying on a setting. A verification date is a research timestamp, not a compatibility guarantee.

Start with the [working loop](workflow.md). Use these notes when a platform difference changes your next action. Our recommended practices are labeled separately from documented behavior.

| Decision | Codex | Cursor | Replit |
| --- | --- | --- | --- |
| Where do project instructions live? | Layered global/project `AGENTS.md`, with override and discovery limits. [Instructions](https://learn.chatgpt.com/docs/agent-configuration/agents-md) | Root or nested `AGENTS.md`; native scoped rules use `.cursor/rules/*.mdc`. [Rules](https://cursor.com/docs/rules) | Root `replit.md`; subdirectory copies are not automatically discovered. [Project instructions](https://docs.replit.com/features/project-setup/replit-dot-md) |
| How can I inspect user behavior? | Confirm the actual environment has browser/runtime tools; request a concrete flow and evidence. | Browser tools can interact with the app and inspect screenshots, console, and network activity. [Browser](https://cursor.com/docs/agent/tools/browser) | App Testing can exercise supported web apps in a browser and provide a replay. [App Testing](https://docs.replit.com/features/agent/app-testing) |
| What does a checkpoint restore? | Use the project's known Git state for file recovery; verify additional environment recovery separately. | Files; conversation messages remain. Checkpoints are local and separate from Git. [Checkpoints](https://cursor.com/docs/agent/overview#checkpoints) | Project state and conversation context; database restoration has separate options and limits. [Rollback](https://docs.replit.com/features/version-control/checkpoints-and-rollbacks) |

## Codex

**Documented behavior.** Codex builds an instruction chain from global guidance and project directories down to its current working directory. It uses at most one instruction file per directory, preferring `AGENTS.override.md` before `AGENTS.md`, with configured fallbacks and a combined size limit. Deeper guidance can override earlier guidance. [Project instructions](https://learn.chatgpt.com/docs/agent-configuration/agents-md)

Sandbox restrictions and approval policy are separate controls; network and managed policy also affect what can run. A setting that suppresses prompts does not by itself establish containment. [Agent approvals and security](https://learn.chatgpt.com/docs/agent-approvals-security)

**Our practice.** Confirm the working directory, loaded instructions, active controls, and available runtime tools before relying on them. Give a task concrete completion evidence and permission to finish authorized local verification. Keep durable milestones in the project's Git history and verify recovery for data and external effects separately. A desktop, CLI, IDE, or cloud session may expose different tools and environments; do not infer capability from the model name.

## Cursor

**Documented behavior.** A file referenced from a rule is a pointer the agent can read; its contents are not automatically included. Rules can apply always, by file scope, by relevance, or manually. Nested `AGENTS.md` instructions combine with parent instructions, with more specific instructions taking precedence. Team rules can impose additional requirements. [Rules](https://cursor.com/docs/rules)

Local execution modes distinguish approvals from sandbox restrictions. Auto-review can combine allowlisting, sandboxed commands, and a fallible classifier. An allowlisted call may run outside the sandbox. Team controls can override local configuration. Cloud agents use dedicated machines and do not use local Run Modes. [Run Modes](https://cursor.com/docs/agent/security/run-modes)

Workspace edits save immediately, and auto-reload may execute changed code before you inspect it. [Agent security](https://cursor.com/docs/agent/security) Browser cookies and storage persist between sessions within a workspace. [Browser](https://cursor.com/docs/agent/tools/browser)

**Our practice.** Start with concise project instructions and link to canonical examples. Confirm the agent reads referenced material before relying on it. Use isolation appropriate to the repository and credentials. State whether a browser check starts signed in, signed out, or with fresh data. Preserve durable milestones in Git; a checkpoint does not establish recovery for database or external effects. See [context](context.md), [verification](verification.md), and [recovery](recovery.md).

## Replit

**Documented behavior.** Agent reads the root `replit.md` and may update it as the project changes. The file does not automatically instruct other AI tools, and very large files may not be fully processed. [Project instructions](https://docs.replit.com/features/project-setup/replit-dot-md)

App Testing runs when Agent decides enough has changed, not after every message. Current documentation limits support to full-stack JavaScript and Streamlit Python web apps, with App Testing available in Power/Max modes and off in Free Mode. Login obstacles may require human takeover; skipping can end the test. [App Testing](https://docs.replit.com/features/agent/app-testing)

Checkpoints capture files, configuration, conversation context, and database state. **Rollback does not restore the database by default.** Development database restoration is optional; production database restoration requires a separate point-in-time restore. [Checkpoints and rollbacks](https://docs.replit.com/features/version-control/checkpoints-and-rollbacks)

**Our practice.** Review changes to `replit.md` alongside code changes. Keep shared guidance in a canonical file and explicitly direct Agent to read it. Ask for critical user flows and inspect what actually ran; an enabled testing toggle is insufficient evidence. Before changing data, name the development and production recovery paths separately. See [verification](verification.md) and [recovery](recovery.md).

## Portable concepts from research

Anthropic's engineering articles inform the guide's context and evaluation practices without adding another operating workflow. Their useful distinctions include retrieving relevant context on demand and evaluating actual environment outcomes separately from an agent's claims. We adapt these as recommendations proportionate to the task. They do not establish equivalent features across products. [Context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents), [agent evaluations](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)

## Prove your setup

Before a consequential task, ask the agent to establish these facts using available evidence:

1. Identify the actual workspace, repository, branch, and working changes.
2. Locate the instruction files that apply and read required references. Name anything unavailable.
3. Identify active authority controls: file access, execution, network, credentials, and external actions requiring review.
4. Demonstrate the runtime capability needed for the task with a harmless interaction. Name unavailable tools or skipped checks.
5. Identify a known working state and what recovery covers: files, conversation, development data, production data, deployments, and external effects.

Keep the result brief. Resolve a material gap before depending on it, then continue through [your first task](first-task.md) or the [working loop](workflow.md).
