# Sources and limits

Primary sources read for the 2026-10-17 editorial baseline. These are selected to support decisions in the guide, not a comprehensive reading list. Publication dates and verification dates are different: the latter records when the relevant claim was assessed. The [registry](source-watch.json) maps claims to pages and review intervals.

Our workflows and templates are editorial synthesis. Product mechanics are attributed to official docs; research is used with its stated scope. Illustrative cases are invented, not execution evidence. Private research stays outside the repository and is not needed to follow the public guidance.

| Source | Used for | Important limit |
| --- | --- | --- |
| [Best practices](https://learn.chatgpt.com/guides/best-practices) | Goal, context, constraints, and completion conditions. | Product guidance; no comparative proof of productivity. |
| [Custom instructions with AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md) | Codex instruction discovery, overrides, scope, and limits. | Discovery depends on working directory and configuration. |
| [Agent approvals and security](https://learn.chatgpt.com/docs/agent-approvals-security) | Sandbox restrictions and approvals are separate controls. | Actual platform, network, and managed policy matter. |
| [Rethinking skills and prompts for GPT-6 Astra](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra) | Remove excess mandatory reading and ambiguous skill triggers. | Model-specific observations do not establish universal behavior. |
| [Skills: plugin concepts](https://developers.openai.com/plugins/concepts/skills) | Skills organize repeatable workflows around tools. | Do not infer identical discovery/execution across platforms. |
| [Cursor Rules](https://cursor.com/docs/rules) | Root/nested instructions, native rule formats, and referenced files. | Precedence and activation can change; check team settings. |
| [Cursor Run Modes](https://cursor.com/docs/agent/security/run-modes) | Local execution modes, approval/sandbox separation, cloud distinction. | Specific current page used over older adjacent approval terminology. |
| [Cursor Agent security](https://cursor.com/docs/agent/security) | Immediate file writes and auto-reload execution risk. | Guardrails are not complete containment; defaults may differ. |
| [Cursor Browser](https://cursor.com/docs/agent/tools/browser) | Browser interactions and persistent cookies/storage. | Read for capabilities/state; current execution policy comes from Run Modes. |
| [Cursor checkpoints](https://cursor.com/docs/agent/overview#checkpoints) | File-only restore, retained chat, local state separate from Git. | No evidence of external-system or database rollback. |
| [Replit project instructions](https://docs.replit.com/features/project-setup/replit-dot-md) | Root replit.md discovery, agent updates, size limits. | No automatic cross-tool equivalence or nested discovery implied. |
| [Replit App Testing](https://docs.replit.com/features/agent/app-testing) | Selective test execution, supported apps, modes, login obstacles. | Enabled does not mean executed or sufficient coverage. |
| [Replit checkpoints and rollbacks](https://docs.replit.com/features/version-control/checkpoints-and-rollbacks) | Checkpoint scope and database restoration exceptions. | Development and production data have distinct recovery paths. |
| [Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) | Selective retrieval and durable state across longer work. | Engineering guidance; no universal optimal context size. |
| [Demystifying evals for AI agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents) | Final outcomes versus claims; regression versus capability evaluations. | Adapt evaluation discipline proportionately for users of agents. |
| [Writing effective tools for agents — with agents](https://www.anthropic.com/engineering/writing-tools-for-agents) | Distinct tool contracts, relevant outputs, realistic evaluations. | Not evidence that a particular connector is safe. |
| [Quantifying infrastructure noise in agentic coding evals](https://www.anthropic.com/engineering/infrastructure-noise) | Resource settings can change benchmark outcomes. | Specific experimental setups; not a general workplace productivity estimate. |
| [DORA 2025 State of AI-assisted Software Development Report: abstract](https://research.google/pubs/dora-2025-state-of-ai-assisted-software-development-report/) | Organizational context matters for AI-assisted work. | Only abstract used here; observational framing is not a local causal forecast. |
| [METR productivity experiment design update](https://metr.org/blog/2026-02-24-uplift-update/) | Selection effects and time-measurement problems limit productivity estimates. | An update explaining uncertainty, not a current universal speedup. |
| [METR self-reported productivity survey](https://metr.org/blog/2026-05-11-ai-usage-survey/) | Distinguish perceived speed and value; self-report and sampling limits. | Convenience sample and reported perceptions are not causal effects. |
| [DeepLearning.AI AI Engineering Skills Map](https://www.linkedin.com/pulse/ai-engineering-skills-map-andrew-ng-m479c/) | Optional compass for choosing a next practice task. | Author's publication of an educational framework; our exercises are an adaptation, not a required curriculum or proficiency rubric. |
| [Skills map: Software engineering fundamentals](https://www.linkedin.com/pulse/ai-engineering-skills-map-software-fundamentals-andrew-ng-7lnac/) | Understand data flow and architectural tradeoffs to steer an agent. | Educational guidance; no comparative productivity claim. |
| [Skills map: Shaping the build](https://www.linkedin.com/pulse/ai-engineering-skills-map-shaping-build-andrew-ng-td7uc/) | Test the user need and use feedback to change what gets built. | Our bounded discovery step is applied guidance, not permission for external contact or release. |
| [AGENTS.md](https://agents.md/) | Comparison: instruction format as a documentation scope. | Not a guarantee every product discovers the file. |
| [AI Agents for Beginners](https://github.com/microsoft/ai-agents-for-beginners) | Comparison: course on building agent systems through lessons and code. | Selected scope comparison, not an exhaustive competitive ranking. |

## How to read this evidence

Vendor documentation describes intended product behavior and may lag an installed version or contain inconsistent older sections. Specific, current operational documentation takes precedence for a narrow claim; unresolved conflicts should be reported. No Cursor, Replit, or Codex product runtime was exercised as part of this literature review.

Engineering articles motivate practices; they do not prove one workflow works best everywhere. Research abstracts, experiments, and surveys answer different questions. We do not convert any of them into a promised productivity multiplier, fixed model ranking, or universal autonomy policy.

Review the relevant primary page before acting on volatile mechanics. A source fetch, hash comparison, or green link check establishes availability or structure, not truth. Follow the [maintenance process](README.md) to correct, trial, or retire guidance.
