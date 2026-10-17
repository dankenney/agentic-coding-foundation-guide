# Improve the next decision

The guide serves people using coding agents for practical work, from first tasks through maintained team workflows. Agents are readers too. A contribution should make a useful action clearer, easier to verify, or easier to recover.

## What earns a place

Prefer a corrected product claim, a worked example, a recurring failure with a reliable remedy, or a simpler explanation of an important decision. State who needs it, when it applies, what to do, how to check it, and where it stops being useful.

Before adding a page, ask whether an existing example or paragraph can carry the lesson. Prefer deletion when advice is redundant, obsolete, speculative, or too costly for its benefit. A release announcement or interesting bookmark is a candidate for review, not automatically guide content.

## Evidence and privacy

- Link current product claims to the specific official page that supports them. Read the page, including exceptions; a search snippet is insufficient.
- Separate documented behavior, research findings, illustrative examples, and our recommendations. Record scope, date, and material limits.
- Add or update affected entries in [source-watch.json](maintenance/source-watch.json) and [sources](maintenance/sources.md). Change `last_verified` after reading and assessing the relevant claim, not after an HTTP success.
- Use made-up data and generic workplace examples. Keep private research, internal URLs, names, identifiers, and credentials outside the repository.
- Do not claim a method is proven, universal, faster, or safer without evidence for that claim. Do not invent executed test results.

## Editorial shape

Keep pages short enough to find the next action. Explain unfamiliar terms where they first matter. Use copy-ready prompts selectively and give each one a purpose. Put volatile product mechanics in [platform notes](guide/platforms.md); keep the working habits portable. Avoid fixed model rankings, exhaustive tool catalogs, mandatory large scaffolds, and instructions to seek permission at every reversible step.

When adding a workflow, include an expected artifact, evidence of success, and a recovery path. Keep templates optional and proportional. Make navigation usable without installing a package or giving an agent write access.

## Validate a contribution

```sh
python scripts/check_guide.py
python -m unittest discover -s tests -v
```

The first checks local links/anchors, content boundaries, the agent index, and source-registry structure. The second exercises those checks and source-watcher behavior. Neither establishes that the prose is true or the teaching works.

The scanner is a targeted quality gate, not a complete Markdown parser or privacy audit. Review new fixtures and examples for confidential content even when automated checks pass.

For navigation or onboarding changes, follow the reader route from the README and ask an independent agent to apply it to the relevant [learner scenarios](maintenance/learner-scenarios.md). Check that it reads selectively, respects the user's project rules, and reports missing access or unexecuted checks honestly. For a script change, execute representative CLI success and failure paths. Report what actually ran in the pull request.

This is a documentation repository, so there is no app build, authentication flow, or live/UAT website to test. If a contribution adds an app, follow the runtime gate in [AGENTS.md](AGENTS.md). Do not substitute this guide's link check for an application's behavior check.

## Propose a reviewable change

Use a branch and pull request. Lead with the reader's problem and resulting improvement. Include source support, validation, limits, and any removed guidance. Significant changes belong in the [changelog](maintenance/CHANGELOG.md). Adoption and merge remain a maintainer decision; automated research should prepare concrete diffs for review.
