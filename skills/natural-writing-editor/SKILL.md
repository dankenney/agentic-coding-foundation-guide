---
name: natural-writing-editor
description: Edit or audit guide prose and technical explanations for clarity, concrete guidance, and natural rhythm while preserving meaning, evidence, and working instructions. Use for editorial revisions, not product research or code changes.
---

# Natural writing editor

Help the reader understand the point and know what to do with it. Read and edit the full scope the user requested. Leave a sentence alone when it already works, and revise the passages that get in the reader's way. Follow the current request and the publication's audience before stored style preferences or samples.

## Choose the requested mode

- **Edit:** revise the text and return one best version with a short account of meaningful changes. Edit files directly when the user has authorized that.
- **Audit:** identify the problems you can observe, quote the relevant wording, and suggest a short fix. Don't rewrite the whole piece unless asked.

Describe the writing patterns you find. Don't use them to score AI authorship or guess who wrote the passage.

## Read before revising

Read each affected page in full. Identify who it's for, what they need to do, and the main point. For a request covering several pages, keep track of which ones you've reviewed. Read linked material when you need it to understand a claim or instruction. Check whether a passage is explanatory prose, a quotation, code, an example, or an operational requirement before changing it.

Keep the meaning and working details intact:

- Preserve supported facts, citations, quotations, uncertainty, and limits that affect the claim. Flag a claim that needs support rather than inventing evidence or making it sound more certain.
- Preserve commands, code, inline identifiers, schemas, expected outputs, and permission or recovery boundaries. Report a suspected technical defect separately from the prose edit.
- Keep heading anchors and link targets stable unless the requested edit requires changing them. Update incoming links and check navigation when they change.
- Keep vocabulary, humor, contractions, and variation in sentence rhythm when they fit the writer. Don't introduce errors or invent personal experience to make the writing sound natural.

## Decide what to revise

Put the main point early. Use a concrete action or consequence when the draft provides one, and give the reader enough background to follow it. Look for:

- Repetition that adds no example, qualification, or next action.
- Openings that announce an explanation, dramatic reveals, and artificial contrasts.
- Inflated claims, vague authority, and commentary that attributes broader meaning without evidence.
- Ornamental verbs, abstract nouns, and rotating synonyms for the same technical term.
- Forced symmetry, punchline fragments, decorative formatting, and endings that only restate the page.

Use judgment with these patterns. A contrast may explain a real technical difference; a repeated label may help someone find the right section. Keep those uses, along with technical terms, useful lists, and genuine uncertainty. Advice can apply across platforms and still be useful. Check what the sentence helps the reader decide before cutting it for being general.

Use the draft's specific details when they explain how something works or what follows from it. If that detail is missing, simplify the claim or flag the gap. Don't add examples, sources, commitments, or opinions just to make the prose more vivid.

## Check the final version

Read the revision for rhythm, then compare it with the source. Check the qualifications, evidence, instructions, and navigation. Undo changes that only make every passage sound alike. If the user requests a voice pass, apply it next and check fidelity again. Keep stock phrases, email conventions, and private details out of a guide.

Run the publication's relevant checks. In this repository, follow [CONTRIBUTING.md](../../CONTRIBUTING.md). Editing prose doesn't establish product behavior or count as a fresh review of a cited source. Say which checks actually ran and use the delivery format the user requested.
