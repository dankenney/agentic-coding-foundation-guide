# Contributing

People use this guide to work with coding agents, from a first task through tools their team will maintain. A contribution should help them choose an approach, check a result, or recover from a problem. Agents need to be able to follow it too.

## What to include

Useful additions include a corrected product claim, a worked example, a reliable fix for a recurring failure, or a simpler explanation of a decision. Explain who the advice is for, when it applies, what to do, and how to check it. Include the limits so someone can tell when to use another approach.

Before adding a page, see whether the lesson fits an existing example or paragraph. Remove advice that's redundant, obsolete, speculative, or more work than it's worth. A release announcement or interesting bookmark is a reason to review the guidance; it still needs to meet the same standard before we add it.

## Evidence and privacy

- Link a product claim to the specific official page that supports it. Read the page and its exceptions before relying on it; a search snippet doesn't give you enough context.
- Identify documented behavior, research findings, illustrative examples, and our recommendations so readers can tell them apart. Record the scope, date, and limits that affect the claim.
- Update the affected entries in [source-watch.json](maintenance/source-watch.json) and [sources](maintenance/sources.md). Change `last_verified` only after you've read the source and assessed the relevant claim. An HTTP success isn't that review.
- Use made-up data and generic workplace examples. Keep private research, internal URLs, names, identifiers, and credentials outside the repository.
- Support claims that a method is proven, universal, faster, or safer with evidence specific to that claim. Report only tests that actually ran.

## Editorial shape

Keep it easy to find what to do next. Explain an unfamiliar term when the reader first needs it, and include a copy-ready prompt when it saves them work. Put product details that change frequently in [platform notes](guide/platforms.md), so the main guidance remains useful across tools. Skip fixed model rankings, exhaustive tool catalogs, large required setups, and permission requests for every reversible step.

For a new workflow, describe what it produces, how someone can check that it worked, and how to recover if it fails. Use templates only where they help. Someone should be able to find their way through the guide without installing a package or giving an agent write access.

The optional [natural writing editor](skills/natural-writing-editor/SKILL.md) helps maintainers revise prose without changing technical meaning. Readers can use the guide without installing it.

## Validate a contribution

```sh
python scripts/check_guide.py
python -m unittest discover -s tests -v
```

The first command checks local links and anchors, content boundaries, the agent index, and source-registry structure. The second tests those checks and the source watcher. You still need to review the claims and try the teaching with a reader or agent.

The scanner covers specific patterns. It doesn't parse every possible Markdown construct or perform a complete privacy audit. Review new fixtures and examples for confidential content even when the checks pass.

For navigation or onboarding changes, start from the README and ask an independent agent to try the relevant [learner scenarios](maintenance/learner-scenarios.md). Check which pages it reads, whether it follows the user's project rules, and how it reports missing access or checks it couldn't run. For a script change, run representative CLI success and failure cases. Include the actual results in the pull request.

This documentation repository has no app build, authentication flow, or live/UAT website. If a contribution adds an app, follow the runtime requirements in [AGENTS.md](AGENTS.md). That app will need its own behavior checks; this guide's link check won't establish that it works.

## Propose a reviewable change

Use a branch and pull request. Explain the reader's problem and how the change helps, then include sources, actual validation, limits, and any guidance you removed. Record significant changes in the [changelog](maintenance/CHANGELOG.md). Automated research can prepare a diff for review. A maintainer decides whether to adopt and merge it.
