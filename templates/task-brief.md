# Task brief

**Outcome:** What should a user be able to do, or what artifact should exist?

**Starting point:** Repository, current behavior, relevant files, known constraints.

**Scope:** The smallest complete change. Explicit exclusions that matter.

**Acceptance:** Observable actions and expected results. Include empty/error states, persistence, and existing access behavior when relevant.

**Evidence:** Relevant static checks; runtime interactions or artifact comparisons; existing live/UAT check; where to save results. For interactions, name the effective backend, disposable data/account, downstream effects, and cleanup. Report unrun checks as unrun.

**Authority:** Continue within this request's authorization and repository rules. State permitted reads, edits, commands, and environments where useful. Identify actions needing separate authorization, such as deployment or external messages. Ask only when a missing decision or boundary blocks the next action.

**Budget, when needed:** Time, usage/spend, and retry limits; what stops at the limit; expiry of any temporary increase.

**Recovery:** How to undo or contain a failed change.

**Completion:** Reviewable diff or artifact, actual verification results, remaining limits, and next step.

Delete fields that add no value. For an example, see [worked tasks](../examples/worked-task.md).
