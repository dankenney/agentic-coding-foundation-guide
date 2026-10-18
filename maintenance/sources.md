# Sources and limits

We read these primary sources for the guide's 2026-10-17 editorial baseline. Each supports a decision in the guide; this isn't a comprehensive reading list. In the [registry](source-watch.json), a verification date records when someone assessed the relevant claim, which may differ from the source's publication date. The registry also links claims to guide pages and sets review intervals.

The workflows and templates combine our recommendations with what these sources support. We attribute product mechanics to official docs and keep research findings within their stated scope. Examples use invented cases; they don't show that we executed a test. Private research stays outside the repository, and readers don't need it to follow the guide.

| Source | Used for | Important limit |
| --- | --- | --- |
| [Best practices](https://learn.chatgpt.com/guides/best-practices) | Goal, context, constraints, and completion conditions. | Product guidance; no comparative proof of productivity. |
| [Custom instructions with AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md) | Codex instruction discovery, overrides, scope, and limits. | Discovery depends on working directory and configuration. |
| [Agent approvals and security](https://learn.chatgpt.com/docs/agent-approvals-security) | Sandbox restrictions and approvals are separate controls. | Actual platform, network, and managed policy matter. |
| [Rethinking skills and prompts for GPT-6 Astra](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra) | Reducing unnecessary required reading and clarifying when a skill applies. | Observations about this model don't establish how every model behaves. |
| [Skills: plugin concepts](https://developers.openai.com/plugins/concepts/skills) | Organizing repeatable workflows around tools. | Platforms can differ in how they discover and execute skills. |
| [Cursor Rules](https://cursor.com/docs/rules) | Root/nested instructions, native rule formats, and referenced files. | Precedence and activation can change; check team settings. |
| [Cursor Run Modes](https://cursor.com/docs/agent/security/run-modes) | Local execution modes, separate approval and sandbox controls, and cloud differences. | We used this specific current page where older adjacent pages used different approval terminology. |
| [Cursor Agent security](https://cursor.com/docs/agent/security) | Immediate file writes and auto-reload execution risk. | Guardrails are not complete containment; defaults may differ. |
| [Cursor Browser](https://cursor.com/docs/agent/tools/browser) | Browser interactions and persistent cookies/storage. | Used for capabilities and state; the Run Modes page supplies current execution policy. |
| [Cursor checkpoints](https://cursor.com/docs/agent/overview#checkpoints) | File-only restore, retained chat, local state separate from Git. | No evidence of external-system or database rollback. |
| [Replit project instructions](https://docs.replit.com/features/project-setup/replit-dot-md) | Root replit.md discovery, agent updates, and size limits. | Doesn't establish equivalent behavior in other tools or nested instruction discovery. |
| [Replit App Testing](https://docs.replit.com/features/agent/app-testing) | Selective test execution, supported apps, modes, and login obstacles. | Enabling the feature doesn't establish that tests ran or covered the relevant behavior. |
| [Replit checkpoints and rollbacks](https://docs.replit.com/features/version-control/checkpoints-and-rollbacks) | Checkpoint scope and database restoration exceptions. | Development and production data have distinct recovery paths. |
| [Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) | Selective retrieval and durable state across longer work. | Engineering guidance; no universal optimal context size. |
| [Demystifying evals for AI agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents) | Checking final outcomes against claims and distinguishing regression from capability evaluations. | Users of coding agents should adapt the approach to the size and risk of their task. |
| [Writing effective tools for agents — with agents](https://www.anthropic.com/engineering/writing-tools-for-agents) | Distinct tool contracts, relevant outputs, realistic evaluations. | Not evidence that a particular connector is safe. |
| [Quantifying infrastructure noise in agentic coding evals](https://www.anthropic.com/engineering/infrastructure-noise) | Resource settings can change benchmark outcomes. | Specific experimental setups; not a general workplace productivity estimate. |
| [DORA 2025 State of AI-assisted Software Development Report: abstract](https://research.google/pubs/dora-2025-state-of-ai-assisted-software-development-report/) | The role of organizational context in AI-assisted work. | Only the abstract was used here. Its observational framing doesn't predict a causal effect for a particular team. |
| [METR productivity experiment design update](https://metr.org/blog/2026-02-24-uplift-update/) | How selection effects and time measurement limit productivity estimates. | Explains uncertainty; doesn't establish a current speedup for everyone. |
| [METR self-reported productivity survey](https://metr.org/blog/2026-05-11-ai-usage-survey/) | Distinguish perceived speed and value; self-report and sampling limits. | Convenience sample and reported perceptions are not causal effects. |
| [DeepLearning.AI AI Engineering Skills Map](https://www.linkedin.com/pulse/ai-engineering-skills-map-andrew-ng-m479c/) | Choosing a next practice task. | The author published it as an educational framework. We adapted it for optional exercises, rather than a required curriculum or proficiency assessment. |
| [Skills map: Software engineering fundamentals](https://www.linkedin.com/pulse/ai-engineering-skills-map-software-fundamentals-andrew-ng-7lnac/) | Understand data flow and architectural tradeoffs to steer an agent. | Educational guidance; no comparative productivity claim. |
| [Skills map: Shaping the build](https://www.linkedin.com/pulse/ai-engineering-skills-map-shaping-build-andrew-ng-td7uc/) | Testing the user need and using feedback to change what gets built. | The guide's discovery step stays within the task's scope. It doesn't authorize external contact or release. |
| [AGENTS.md](https://agents.md/) | Comparison: instruction format as a documentation scope. | Not a guarantee every product discovers the file. |
| [AI Agents for Beginners](https://github.com/microsoft/ai-agents-for-beginners) | Comparing scope with a course on building agent systems through lessons and code. | A selected comparison of scope, with no claim to rank every competing guide. |

## How to read this evidence

Vendor docs describe intended product behavior. They can lag an installed version or contain inconsistent older sections. For a specific operating claim, use the current page that addresses it directly and report any conflict you can't resolve. This literature review didn't exercise the Cursor, Replit, or Codex product runtimes.

An engineering article can suggest a practice worth trying without proving it works best everywhere. Research abstracts, experiments, and surveys answer different questions, so keep their limits attached to the claims you use. None of the sources here justifies a promised productivity multiplier, a fixed model ranking, or one autonomy policy for every task.

Read the relevant primary page before relying on a product detail that may have changed. Fetch results, hash comparisons, and link checks help locate changes and broken references; someone still needs to assess the claim. Use the [maintenance process](README.md) to propose a correction, trial, or removal.
