---
name: ux-lens
description: An eight-item UX lens for business apps, built from the classic UX laws (Doherty, Hick, Von Restorff, Peak-End, Miller, Tesler, Jakob, Fitts, Postel, error prevention). It has an extra section for audit-grade apps where figures must be exact and records can't be undone. Use it whenever someone writes a spec, brief or acceptance criteria for a screen or flow; reviews or critiques a screen, mockup, prototype or screenshot; plans a walkthrough or usability session; or asks how to make a business app feel faster, clearer or better than the tools users already know. That holds even if they never say "UX laws". It also covers dashboards, review queues, sign-off flows, data tables and reporting tools.
---

# UX lens

Eight checks that turn the common UX laws into decisions for business apps. Use them in three ways:

- **Brief:** a spec, a brief or acceptance criteria for a screen.
- **Review:** a screen, a mockup or screenshots.
- **Walk:** a hands-on walkthrough with a real user or the product owner.

The laws are well known, and competitors follow them too. A product wins by applying them to the moments that matter for its users: the click that waits on a slow back end, the end of a sign-off, the long table nobody can scan. Each item below says what to check and why it matters, so you can judge the cases it doesn't spell out.

## The eight items

1. **Instant acknowledgment** (Doherty threshold). Within 400 ms of any click, the screen shows a visible pending state: a busy or disabled control plus a status in words that assistive tech can read. The final result then replaces that state in place. Back ends are often slow, and a frozen button makes people click again or doubt the result. The user should always know their click registered.
2. **One designed moment, one primary action** (Von Restorff, Hick, the peak in Peak-End). Each screen has one thing a first-time reader should remember and one primary action. Everything else is visibly quieter. Users never face more than a handful of equal-weight choices at once. If you can't name the designed moment, the screen doesn't have one yet.
3. **A deliberate ending** (the end in Peak-End, Zeigarnik). People judge a flow by its peak and its end. Every flow ends on a clear done state that says what happened, what was recorded or sent, and what comes next. Unfinished work shows where it stands and what is left, so people come back to it.
4. **Chunk long lists** (Miller, Serial Position). Group rows by the unit users reason in, such as category, owner, period or requirement, not by database order. Put the group that matters most for the decision first.
5. **Absorb complexity** (Tesler, sensible defaults, Occam's razor). Complexity can be moved but not removed, so the product carries it, not the user. Pick the right period, basis and filter by default, and say which one was picked. Don't ask users to choose between options they shouldn't need to understand. Alternate views stay one labelled step away. Remove anything that doesn't help the decision.
6. **Familiar behaviour, actions next to their content** (Jakob, Fitts, target distance). Business users live in spreadsheets and the tools they already know:
   - Tables sort, filter and copy exact values the way a spreadsheet does.
   - Links look like links.
   - A shared URL opens in the same state.
   - The control that acts on a row or figure sits on that row or figure.
   - Targets meet [WCAG 2.2 criterion 2.5.8](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html): at least 24 by 24 CSS px, or enough spacing.
7. **Forgiving inputs, clear outputs** (Postel). Search and filters accept loose input: case, spacing, common date and period formats, extra whitespace. Output is consistent and explicit. When input really is invalid, the refusal says why and how to fix it.
8. **Prevent, then explain** (error prevention and recovery). Constraints and confirmations stop costly mistakes before they happen, and the confirmation names exactly what will happen. Where undo is possible, offer it. Every failure says in place what went wrong and what to do next. "Something went wrong" is not enough.

Proximity, similarity, connectedness and Prägnanz belong to the design system: spacing, tokens and shared components. Check them there, not screen by screen.

## Audit-grade apps

Apply A1–A5 when the app holds figures that will be signed, filed or audited, or keeps an append-only record such as a ledger, an approval log or a disclosure history. If the user hasn't said, and the screen suggests it (sign-offs, ledger numbers, disclosure references), apply them and say you inferred it. If you can't tell, ask. These adjustments override the generic items:

- **A1. Exact figures** (adjusts item 5). The interface never rounds, sums or converts a figure to "make it simpler". Showing a total that the system of record served is fine. Computing one in the interface is not. Show each value with its unit and basis, and let every figure trace to its source or calculation in one step.
- **A2. Forgiving inputs only** (adjusts item 7). Be forgiving with search and filter input, never with figures. Don't coerce, round or guess a value. Refusing bad data, in plain words, is the feature.
- **A3. No undo** (adjusts item 8). A signed or recorded decision can't be undone. Prevention carries more weight: the confirmation names exactly what will be recorded and by whom. A mistake is corrected by a visible reversal or correction entry, never a silent undo.
- **A4. Honest unknowns.** When evidence is missing, contradictory or unreadable, the answer is "not known" with the reason, never a confident yes. Fail closed. Every status, such as "not blocking" or "changed", says why or what changed.
- **A5. Agents and people.** If software agents propose or act, show who or what acted and why. People must be able to tell a person, a rules engine and an agent apart without relying on colour, and a person approves the costly step. Role names stay consistent across the screen.

## How to use it

### Brief mode

Add a "UX lens" section to the brief, with one line per item: how this screen or flow meets the item, or why the item doesn't apply. Make each line testable where possible. For example: "Approve shows a pending state within 400 ms; e2e test holds the response for 3 s and asserts `aria-busy` within 400 ms." Note the audit-grade overrides if they apply.

### Review mode

Look at the rendered screen, not a description of it. Ask for every state you can get: loading, empty, error, success and long content. First list the states you actually saw, and any masked or cropped areas. Judge only those. Mark anything else "not seen" rather than guessing.

Then report one row per item, plus rows A1–A5 for an audit-grade app:

| # | Item | Verdict | Severity | Evidence (screen, element, what you saw) | Fix (exact change; text, style or structural) |

- **Verdict:** meets, partial, gap, not seen, or n/a.
- **Severity** (gaps and partials only):
  - **Blocker:** stops or misleads someone on the main task.
  - **Major:** slows or confuses people often.
  - **Minor:** polish.

Rank the gaps by severity, then by how many people they hurt. Some items need a running product. For example, item 1 can't be judged from a screenshot: mark it "not seen" and ask for a timed run or a recording.

Two items need judgement on some screens:
- **Item 2 on a read-only screen.** The primary action is the one that serves the screen's job. That may be the obvious next step, such as a link to the queue that clears the problem, or a secondary tool like re-run or export. If there is truly nothing to do, the designed moment carries the screen alone.
- **Item 3 on a screen that isn't a flow.** The "ending" is the answer the screen gives. Check that the answer is stated plainly and says what to do next.

### Walk mode

Give the walker these questions, one per item, to answer during or right after the walk:

1. Did any click leave you unsure whether it registered?
2. On each screen, what did you notice first? Was it the right thing?
3. At the end of the flow, did you know you were done and what had happened?
4. Did any list make you hunt for the row that mattered?
5. Did a screen ask you to choose something you didn't care about?
6. Did sorting, filtering, copying or a shared link behave differently from what you expected?
7. Did any input refuse something reasonable, or did any output surprise you?
8. Before anything costly or permanent, did you know exactly what would happen? After a failure, did you know what to do next?

Record the answers as observations: what the walker saw and did. Turn each "no" or hesitation into a ranked fix.

## Things this lens is not

- **Not for code, back ends or algorithms.** The lens judges screens and flows that people use. If someone asks it to review a function's performance or a data pipeline, say the lens doesn't apply and review the code directly. The Doherty item is about how fast the screen acknowledges a person, not how fast code runs.
- **Not a substitute for watching a real user.** The walk mode is there for that reason.
- **Not a score.** Don't average the items. One serious gap on the main flow outweighs several passes.
- **Not a style guide.** Visual polish, brand and point of view need their own review. This lens checks whether the experience works and feels fast and trustworthy.
