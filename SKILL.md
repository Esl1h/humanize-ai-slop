---
name: humanize-ai-slop
description: |
  Rewrite AI-sounding English text so it reads like a person wrote it, without
  changing what it says, or flag every sign of AI writing without rewriting
  anything. Use when editing or reviewing prose for inflated claims, sales
  language, vague sources, repetitive structure, stock AI words, passive
  voice, filler, fake depth, or chatbot artifacts. Merges the patterns of
  Wikipedia's "Signs of AI writing" with the editing principles and rhetorical
  patterns of the No AI Slop project. For Brazilian Portuguese text, use
  humanize-br.
license: MIT
metadata:
  version: "1.1.0"
---

# Humanize AI Slop: remove AI writing patterns

Rewrite AI-sounding text so it reads like the writer, not a chatbot. Do not change what it says or make up details.

The patterns below merge two sources. The first is Wikipedia's ["Signs of AI writing"](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing), maintained by WikiProject AI Cleanup, as organized into numbered patterns by the [Humanizer](https://github.com/blader/humanizer) skill. The second is [No AI Slop](https://github.com/petergyang/no-ai-slop), by Peter Yang, which contributes the editing principles, the detect mode, the word lists, and the rhetorical patterns that Wikipedia's list does not cover. Later Humanizer revisions contributed patterns 6 and 24 and the widened forms of 32 and 40; this skill keeps its own thematic numbering.

## Two modes

**Edit (default).** The user shares a draft to fix. Make the minimum effective edit with the rules below and return the edited draft plus a **What changed** section.

**Detect.** The user asks whether a piece sounds like AI, or asks to audit, scan, or flag a draft without rewriting. Name each pattern from this skill that appears, quote the exact line, and give the fix in a few words, one finding per line in document order:

- **Pattern N (name):** "quoted line" → the fix in a few words

End the report with one summary line: how many findings, how many distinct patterns, and where they cluster ("9 findings, 6 patterns, mostly in the opening and the closing paragraph"). Several patterns in one passage are stronger evidence than one pattern spread thin, so the summary tells the user where to look first. Read [`references/patterns.md`](references/patterns.md) before writing the report, so each finding uses the catalog's name and scope.

Do not rewrite, score the draft, or guess whether AI wrote it. AI detectors guess. Named patterns are evidence the user can check with their own eyes. When the draft is in a file and the bundled scanner is available, run `python3 scripts/slop_scan.py <path>` first: it lists the mechanical findings (banned words, dashes, decorated headings, emoji, mixed quotes, bold-label lists, stacked hyphen pairs) as `fix`, and watched phrases (chatbot leftovers, faux-insight setups, filler, binary contrasts, horizontal rules) as `watch`, each with a pattern number. Confirm or dismiss each `watch` finding by reading the context, then add the rhetorical patterns the scanner cannot see. If the scanner is not installed, apply those checks by hand. Offer to edit the draft after.

## What to do

When given text to humanize:

1. **Find AI patterns.** Check the text against the [pattern index](#pattern-index).
2. **Keep every claim.** You may shorten dull parts, expand useful parts, and merge or split paragraphs. Keep the information even when you change the structure.
3. **Do not invent facts.** Do not add a fact, name, number, date, quote, citation, or reference unless it comes from the source or the user. If a sentence needs a missing detail, ask for it or use a simpler sentence. You may add an opinion or reaction when the writer's voice calls for one, but you may not add a factual claim. Fiction is exempt because invented details are part of the task.
4. **Match the voice.** Use the right tone for the text, such as formal, casual, or technical. Add personality only when the text and the writer call for it.

The input type controls what you return. See [How to return the result](#how-to-return-the-result). Use the same rewrite process in every mode.

## What to ask for

If the user has not provided a draft, ask them to paste it.

If the audience or format is unclear and the answer would change the edit, ask one question: who is this for and where will it be published? Otherwise, edit with the most likely reading and say which one you chose.

If a sentence needs a fact the draft does not contain, ask for it instead of inventing it.

## Match the writer's voice

If the user provides a writing sample (their own previous writing), analyze it before rewriting:

1. Read the sample first. Note its sentence length, word choice, paragraph openings, punctuation, repeated phrases, and transitions.
2. Match those habits. Do not replace casual words with formal ones or remove deliberate quirks.
3. If there is no sample, use the guidance below.

A writing sample takes priority over these style rules. If the sample uses em dashes, keep them at about the same rate. Do not apply pattern 15 as a ban.

## Add personality only when it fits

Removing AI patterns is only half the job. The result should still sound like a person.

Use personality in blog posts, essays, opinions, and personal writing when it fits the writer. Keep reference, technical, legal, and factual text neutral. Do not add opinions or first-person language where they do not belong.

When personality fits, keep the writer's opinions, uncertainty, mixed feelings, humor, asides, and uneven rhythm. Never invent facts to make the text feel personal.

## Editing principles

- **Preserve the writer's real voice.** First notice the draft's vocabulary, cadence, bluntness, humor, uncertainty, digressions, and level of polish. Keep the traits that feel personal to the writer. Do not make every paragraph equally tidy or rewrite distinctive lines merely for consistency.
- **Make the minimum effective edit.** Fix AI patterns, errors, repetition, and unclear passages. Leave strong human sentences alone. A rough draft with a real voice should still sound like the same person after editing.
- **Lead with the point when the setup adds nothing.** Cut generic throat-clearing. Keep a personal aside, story, or admission when it creates context, tension, or character.
- **Front-load only when it improves clarity.** Put conclusions early when that helps the reader. Do not force every section and paragraph into the same point-detail-background shape.
- **Keep the user's meaning.** Do not invent claims, examples, stats, or opinions. If something is unclear, ask.
- **Open it up, do not dumb it down.** Keep the substance, nuance, and precision. Strip out only what makes it hard to read: jargon, long sentences, abstract nouns, and tangled structure.
- **Use active voice.** "The team shipped it Tuesday" beats "the decision emerged." Never let inanimate things do human verbs.
- **Make every sentence earn its place.** Cut empty qualifiers and throat-clearing. Keep phrases such as "I think," "maybe," or "to be honest" when they express real uncertainty, self-awareness, or the writer's spoken rhythm.
- **Untangle sentences without flattening the cadence.** Split sentences and paragraphs when they are genuinely hard to follow. Keep longer spoken sentences, fragments, and changes in pace when they are clear and characteristic of the writer.
- **Be concrete and specific.** Abstraction is where writing goes to die. "The integration improved efficiency" becomes "The integration cut deploy time from 40 minutes to 4." Names, numbers, dates, mechanisms, and examples beat abstractions.
- **Use the portability test.** If a sentence could move unchanged to another person, company, country, or product, it is probably filler. Cut it or replace it with a fact, example, mechanism, consequence, or judgment specific to this subject.
- **Show, do not tell the reader what to think.** Make facts, actions, examples, and consequences carry the emphasis. Cut commentary that labels a point important, surprising, subtle, or obvious instead of demonstrating why. If the surrounding prose already shows the point, trust the reader and delete the commentary.
- **Protect the specific fact.** Do not smooth a useful detail into generic importance. "The tool significantly improves engineering productivity" becomes "The tool cut review time from 30 minutes to 8."
- **Make verbs do the work.** Replace weak verb phrases with direct verbs. "Made a decision" becomes "decided." "Has the ability to" becomes "can."
- **Know the job.** Before structure or word choice, know what the piece is trying to do and who it is for.
- **Preserve useful edge and character.** Keep strong opinions, blunt language, humor, profanity, self-interruptions, and honest admissions when they belong to the writer. Do not replace them with safer or more professional wording.
- **Keep structure unless it is hurting the piece.** Preserve the writer's progression and detours when they carry personality. If you reorganize, say why in the What changed section.

## Words and phrases to watch

Banned outright: delve, foster, leverage, utilize, facilitate, empower, streamline, robust, cutting-edge, paradigm shift, game changer, this is huge, this changes everything, tapestry, realm, beacon, multifaceted, meticulous, intricate, paramount, transformative, elevate, embark, supercharge, harness, ever-evolving.

Often-empty adverbs: just, literally, honestly, simply, actually, truly, fundamentally, importantly, crucially, inherently, inevitably. Cut them when they add nothing. Keep them when they carry emphasis, uncertainty, contrast, or the writer's natural spoken rhythm.

Often-empty phrases: it's worth noting, it's important to note, at the end of the day, when it comes to, at its core, in today's world, in the age of, in the world of, the reality is, the truth is, in terms of, with regard to, in order to, going forward, in this article, let's dive in. Cut them when they delay the point. Keep an occasional phrase when it is part of the writer's recognizable voice and the sentence still earns its place.

## Pattern index

Each line names a pattern and the usual fix. This is enough for most edits. Read [`references/patterns.md`](references/patterns.md) for the phrases to watch and the before and after examples: always for a detect report, and whenever a pattern's scope is unclear.

### Content

1. Inflated importance: drop "pivotal moment" and "testament to"; state the fact and let the reader judge it.
2. Name-dropping: replace a list of outlets or experts with what one named source actually said.
3. Shallow -ing analysis: cut trailing "highlighting...", "ensuring..." clauses or turn them into a sourced claim.
4. Sales language: replace "vibrant", "nestled", "breathtaking" with plain description.
5. Vague sources: name the source or flag the claim as unsupported; never invent a citation.
6. Vague association: replace "associated with" and "linked to" with the real relationship.
7. Formulaic challenges: cut "despite its challenges... continues to thrive" sections; keep only concrete problems.

### Language and grammar

8. Overused AI words: replace the banned and watched words with plain ones.
9. Avoiding is, are, and has: "serves as" and "boasts" become "is" and "has".
10. Binary contrasts: rewrite "not X, but Y" and "not A, not B, but C" as a direct claim.
11. Forced triads: keep the items the text needs, whether that is one, two, or four.
12. Synonym cycling: repeat the clearest noun instead of rotating synonyms; vary repeated sentence openings.
13. False ranges: drop "from X to Y" when X and Y are not ends of a real scale.
14. Passive voice: name who acted.

### Style and formatting

15. Dashes: replace em and en dashes with commas, colons, parentheses, or new sentences, unless the writer's sample uses them.
16. Bold overload: remove bold that marks nothing the reader must find.
17. Bold-label lists: turn "**Label:** text" bullets into prose or plain items.
18. Title case headings: use sentence case.
19. Emoji decoration: remove emoji from headings and list items.
20. Quote consistency: use one quote style per document, matched to the writer or target format.

### Chatbot

21. Chatbot leftovers: delete "I hope this helps", "Want me to...?", "Let me know".
22. Knowledge-limit guesses: delete training-cutoff disclaimers and guesses presented as facts.
23. Agreeable tone: drop "Great question!" and "You're absolutely right!".
24. Re-explaining shared context: lead with the decision or answer; do not restate what the reader wrote.

### Filler and endings

25. Filler phrases: cut "in order to", "it's worth noting", "when it comes to".
26. Qualifier stacks: keep one honest hedge at most.
27. Generic endings and recaps: end on a concrete point or next step, not "the future looks bright".

### Hyphenation

28. Hyphenated pairs: limit pairs to what grammar needs; rewrite stacked corporate jargon.

### Fake depth and rhetoric

29. Fake deeper truth: cut "the real question is" and "at its core"; state the point.
30. Announcing the point: cut "let's dive in" and self-answered questions; say the point.
31. Heading restated: do not repeat the heading in the first sentence.
32. Writing about the document: describe the subject, not the document or how it was made.
33. Forced punchlines and robotic rhythm: merge stacked dramatic fragments; vary sentence length.
34. Formulaic sayings: delete fake-profound kickers instead of rewriting them into better metaphors.
35. Fake-candid openers: cut "Let's be honest" and "Here's the thing" when used as hooks.
36. Unasked objections: cut "To be clear" and "I'm not saying" when nobody raised the point.
37. Fake alternatives: cut options the text only raises to dismiss.
38. Colon reveals: rewrite "The best part: it learns" as a plain sentence.
39. Interpretive metadiscourse: cut commentary that labels a point important, subtle, or surprising.
40. Formatting slop: remove decorative symbols, rules between every section, and headings over tiny sections.
41. Faux-insight setups: cut "here's what nobody tells you"; let the claim carry itself.

## What not to flag

### Patterns that are not proof by themselves

A person may use some of these patterns. Do not treat any item below as proof by itself:

- **Perfect grammar and consistent style.** Many writers are professionals or have been edited. Polish does not equal AI.
- **Mixed casual and formal styles.** This can reflect the writer's field, age, or personal habits.
- **"Bland" or "robotic" prose.** AI prose has *specific* tells. Generic dryness without those tells is just dry writing.
- **Formal or academic words.** Pattern 8 lists specific words that AI writing overuses. Do not simplify every formal word.
- **Letter-style opening or closing on a comment.** Salutations and sign-offs predate ChatGPT by centuries.
- **Common transition words in isolation.** *Additionally*, *moreover*, *consequently* are AI-coded only when piled up. One *however* is not a tell.
- **Curly quotes alone.** macOS, Word, Google Docs, and most CMSes auto-curl by default. Curly quotes only count when stacked with other tells.
- **Em dashes alone.** Many editors and journalists use them often. Em dashes are evidence only when paired with formulaic sales-y rhythm.
- **One short sentence for emphasis.** Flag dramatic fragments only when several appear in a row.
- **Deliberate repeated openings.** Writers may repeat an opening to build rhythm or pressure, as in "She came. She saw. She conquered." Change it only when the repetition adds nothing.
- **"Honestly" or "look" mid-sentence.** These are ordinary in casual writing. The tell is the standalone theatrical opener, not the word itself.
- **Useful limits and disclaimers.** Keep scope statements, legal and safety notices, real corrections, named objections, replies, and FAQ answers.
- **Real alternatives.** Keep options that a reader may consider in a design document, tutorial, or argument. Remove only an unlikely option that the text dismisses and never uses again.
- **A colon before a real list, label, or quote.** Pattern 38 targets staged reveals, not ordinary punctuation.
- **Unsourced claims.** Most of the web is unsourced. Lack of citations does not prove anything.
- **Correct, complex formatting.** Visual editors and templates produce clean output without any AI.
- **Secondhand text.** Do not rewrite watched phrases inside quotations, titles, proper names, or examples where the phrase is being discussed rather than used.

When unsure, look for several patterns together. One em dash proves nothing. Several stock patterns in the same passage are stronger evidence.

### Human details to keep

These details often carry the writer's voice. Keep them unless they hurt the meaning:

- **Specific, unusual details.** Keep a real address, an odd quote, or a phrase such as "the lawyer who used to work upstairs from my dentist."
- **Mixed feelings and unresolved tension.** Keep lines such as "I think this is mostly good, but it bothers me, and I can't fully explain why."
- **Dated, era-bound references.** Slang, memes, or in-jokes that map to a specific year and subculture. Models lag by a year or more.
- **Deliberate first-person choices.** Keep a cut or word choice when the writer can explain why it belongs.
- **Variety in sentence length.** Real writing alternates short and long. AI writing tends toward an even, mid-length cadence.
- **Genuine asides, parentheticals, or self-corrections.** "(I keep wanting to say 'almost' here, but it really was certain.)" Models rarely interrupt themselves like this.
- **Edits made before November 30, 2022.** ChatGPT's public launch. Anything older than that is, with very rare exceptions, not AI-written.

## How to return the result

**Pasted text (default).** Return the final rewrite followed by a short **What changed** section. Do not return intermediate drafts.

**File mode.** When the user names a file, run the full rewrite process but write only the final text to the file. Change prose only. Keep code blocks, YAML metadata, data, and link targets unchanged. Then give the user a short summary.

**Embedded mode.** When another task uses this skill for a pull request, commit message, or document, return only the final text.

**Detect mode.** One line per finding, in document order: **Pattern N (name):** "quoted line" → the fix in a few words. End with the summary line described in [Two modes](#two-modes). Do not rewrite the draft, score it, or claim whether AI wrote it.

## Rewrite process and self-check

1. Read the full draft and mark each AI pattern. Identify the core point and the voice traits to preserve: vocabulary, cadence, bluntness, humor, uncertainty, digressions. If you cannot identify the core point, ask the user.
2. For a detect request, return the findings report described in [Two modes](#two-modes) and stop.
3. Write a draft. Read it aloud. Check the rhythm, details, simple verbs such as *is* and *has*, and the right level of formality.
4. Ask two questions:
   - **"What still sounds AI-generated?"**
   - **"Did the rewrite add or remove any fact, name, number, date, quote, citation, ranking, or other claim?"**
   Treat any unsupported addition or lost claim as an error.
5. Write the final version. State each point naturally instead of patching one flagged phrase at a time. If a sentence stays awkward, rewrite the paragraph around its main point. Apply the dash rule in pattern 15.
6. Check the rewrite against the list in [`eval.md`](eval.md). If any check fails, fix the draft and run the checks again. In file mode, when the bundled scanner is available, run `python3 scripts/slop_scan.py <path>` on the rewritten file as the last check; a clean rewrite has no `fix` finding, and each `watch` finding is either fixed or fine in context.

Return the result required by [How to return the result](#how-to-return-the-result).

## Sources

This skill merges two English sources:

- [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing), maintained by WikiProject AI Cleanup, as organized into numbered patterns by earlier versions of [Humanizer](https://github.com/blader/humanizer). Its later v3 revision, reordered by strength, contributed patterns 6 and 24 and the widened forms of 32 and 40. Its patterns come from reviews of AI-generated text on Wikipedia.
- [No AI Slop](https://github.com/petergyang/no-ai-slop), by Peter Yang, which contributed the editing principles, the detect mode, the word lists, the self-check list, and the rhetorical patterns in sections 34, 35, 38, 39, 40, and 41.

The merge and the numbering follow [Humanize BR](https://github.com/Esl1h/humanize-br), which combined the same two sources for Brazilian Portuguese.

Wikipedia's main point: "LLMs use statistical algorithms to guess what should come next. The result tends toward the most statistically likely result that applies to the widest variety of cases." That statistical flattening is what this skill tries to undo.
