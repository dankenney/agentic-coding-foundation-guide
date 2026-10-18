# Platform notes

Documentation verified: 2026-10-17. These notes are based on public documentation. We haven't tested the product behavior described here. Check your installed version, plan, workspace, and team policy before relying on a setting; the date tells you when we read the documentation, not whether your setup matches it.

Use the [working loop](workflow.md) for the general approach and this page when a platform difference affects what you need to do. Each platform section separates documented behavior from our recommendations.

| Decision | Codex | Cursor | Replit |
| --- | --- | --- | --- |
| Where do project instructions live? | Layered global/project `AGENTS.md`, with override and discovery limits. [Instructions](https://learn.chatgpt.com/docs/agent-configuration/agents-md) | Root or nested `AGENTS.md`; native scoped rules use `.cursor/rules/*.mdc`. [Rules](https://cursor.com/docs/rules) | Root `replit.md`; subdirectory copies are not automatically discovered. [Project instructions](https://docs.replit.com/features/project-setup/replit-dot-md) |
| How can I inspect user behavior? | Confirm the actual environment has browser/runtime tools; request a concrete flow and evidence. | Browser tools can interact with the app and inspect screenshots, console, and network activity. [Browser](https://cursor.com/docs/agent/tools/browser) | App Testing can exercise supported web apps in a browser and provide a replay. [App Testing](https://docs.replit.com/features/agent/app-testing) |
| What does a checkpoint restore? | Use the project's known Git state for file recovery; verify additional environment recovery separately. | Files; conversation messages remain. Checkpoints are local and separate from Git. [Checkpoints](https://cursor.com/docs/agent/overview#checkpoints) | Project state and conversation context; database restoration has separate options and limits. [Rollback](https://docs.replit.com/features/version-control/checkpoints-and-rollbacks) |

## Codex

Documented behavior. Codex builds an instruction chain from global guidance and project directories down to its current working directory. It uses at most one instruction file per directory, preferring `AGENTS.override.md` before `AGENTS.md`, with configured fallbacks and a combined size limit. Deeper guidance can override earlier guidance. [Project instructions](https://learn.chatgpt.com/docs/agent-configuration/agents-md)

Sandbox restrictions and approval policy are separate controls. Network and managed policy also affect what can run. Suppressing approval prompts doesn't, by itself, restrict what the agent can access or execute. [Agent approvals and security](https://learn.chatgpt.com/docs/agent-approvals-security)

Our recommendation. Confirm the working directory, loaded instructions, active controls, and available runtime tools before relying on them. Tell the agent what evidence you need and which local checks it may run. Save milestones in the project's Git history, and check separately how you'll recover data and external changes. Desktop, CLI, IDE, and cloud sessions may have different tools and environments, even when they use the same model.

## Cursor

Documented behavior. A file referenced from a rule is available for the agent to read, but its contents are not automatically included. Rules can apply always, by file scope, by relevance, or manually. Nested `AGENTS.md` instructions combine with parent instructions, with more specific instructions taking precedence. Team rules can impose additional requirements. [Rules](https://cursor.com/docs/rules)

Local execution modes distinguish approvals from sandbox restrictions. Auto-review can combine allowlisting, sandboxed commands, and a classifier that can make mistakes. An allowlisted call may run outside the sandbox. Team controls can override local configuration. Cloud agents use dedicated machines and do not use local Run Modes. [Run Modes](https://cursor.com/docs/agent/security/run-modes)

Workspace edits save immediately, and auto-reload may execute changed code before you inspect it. [Agent security](https://cursor.com/docs/agent/security) Browser cookies and storage persist between sessions within a workspace. [Browser](https://cursor.com/docs/agent/tools/browser)

Our recommendation. Keep project instructions concise and link to canonical examples. Confirm the agent reads those references before relying on them. Choose isolation that accounts for the repository and credentials it can access. Specify whether a browser check should start signed in, signed out, or with fresh data. Save milestones in Git, and check how you'll recover database and external changes separately from a checkpoint. See [context](context.md), [verification](verification.md), and [recovery](recovery.md).

## Replit

Documented behavior. Agent reads the root `replit.md` and may update it as the project changes. The file does not automatically instruct other AI tools, and very large files may not be fully processed. [Project instructions](https://docs.replit.com/features/project-setup/replit-dot-md)

App Testing runs when Agent decides enough has changed, not after every message. Current documentation limits support to full-stack JavaScript and Streamlit Python web apps, with App Testing available in Power/Max modes and off in Free Mode. Login obstacles may require human takeover; skipping can end the test. [App Testing](https://docs.replit.com/features/agent/app-testing)

Checkpoints capture files, configuration, conversation context, and database state. Rollback does not restore the database by default. Development database restoration is optional; production database restoration requires a separate point-in-time restore. [Checkpoints and rollbacks](https://docs.replit.com/features/version-control/checkpoints-and-rollbacks)

Our recommendation. Review changes to `replit.md` alongside code changes. Keep shared guidance in a canonical file and explicitly direct Agent to read it. Request tests of the critical user flows, then inspect which tests actually ran. An enabled testing toggle doesn't tell you whether a flow was checked. Before changing data, establish how you'll recover development and production data separately. See [verification](verification.md) and [recovery](recovery.md).

## Portable concepts from research

The guide draws on Anthropic's engineering articles for context and evaluation advice. In particular, retrieve relevant context when you need it, and check what actually happened in the environment separately from what an agent says happened. Apply that advice in proportion to the task. These articles don't establish equivalent features across products or add another platform workflow to this guide. [Context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents), [agent evaluations](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)

## Check your setup before relying on it

Before a task where an error would be costly, ask the agent to check the following using the evidence available:

1. Which workspace, repository, and branch is it using, and what changes are already there?
2. Which instruction files apply? Have it read the required references and name anything it can't access.
3. What controls apply to file access, execution, network access, credentials, and external actions requiring review?
4. Can it perform the runtime interaction the task needs? Ask for a harmless demonstration and a clear account of unavailable tools or skipped checks.
5. What known working state can you return to? Check what recovery covers for files, conversation, development data, production data, deployments, and external effects.

Keep the response brief. Resolve any gap that would affect the task before proceeding, then continue with [your first task](first-task.md) or the [working loop](workflow.md).
