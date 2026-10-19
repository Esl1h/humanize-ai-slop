# Humanize AI Slop self-check

Use this after the rewrite. Answer each check with pass or fail. If any check fails, fix the draft before returning it.

For detect requests, make sure the response names each pattern found with a quoted line and a short fix, ends with one summary line, and does not rewrite the draft.

## Editing principles

1. Does the edit preserve the writer's point without adding claims, examples, stats, quotes, references, or opinions?
2. Does it preserve the writer's distinctive vocabulary, cadence, bluntness, humor, uncertainty, digressions, and level of polish?
3. Does it leave strong human sentences alone instead of rewriting them for consistency or making every paragraph equally tidy?
4. Is the amount of cutting proportional to the actual AI slop, with no aggressive compression that strips out character?
5. Does the draft lead with what the reader needs while keeping personal setup that adds context, tension, or character?
6. Are points front-loaded where that improves clarity without forcing every unit into the same structure?
7. Do sentences earn their place, with concrete facts, protected details, and direct verbs where the draft supports them?
8. Does every generic sentence pass the portability test, or was it cut or made specific to this subject?
9. Does the draft use active voice with human subjects where possible?
10. Does the edit keep useful edge and preserve structure unless the structure was hurting the piece?
11. Are genuinely tangled sentences fixed while clear spoken cadence, fragments, and changes in pace remain intact?

## Words and phrases to watch

1. Are banned words, filler phrases, often-empty adverbs, and inflated claims removed unless quoted as examples?

## The 41 patterns

1. Are binary contrasts, negative listings, rhetorical setups, announcements, and fake-candid or throat-clearing openers removed?
2. Are faux-insight setups, colon reveals, shallow -ing analysis, fake-strong verbs, synonym cycling, dramatic fragments, and robotic rhythm fixed?
3. Are inflated importance, sales language, vague sources, and vague association replaced with plain facts, named sources, and named relationships, or flagged for the writer when no source exists?
4. Is interpretive metadiscourse and writing about the document instead of its subject removed, including method narration, authorial metacommentary, reader guidance, emphasis markers, and redundant glossing?
5. Are fake-profound kicker lines deleted instead of rewritten into better metaphors?
6. Are generic positive endings and summary recaps cut so the piece ends on a concrete point, takeaway, or next action?
7. Are chatbot leftovers, knowledge-limit disclaimers, disguised guesses, and overly agreeable openers gone, and are replies that re-explain shared context trimmed to the decision?
8. Is formatting slop removed: emoji and decorative symbols in headings, decorative bold, bold mini-heading lists, title case in headings, bullets that should be prose, headers over tiny sections?
9. Are colons sentence case unless grammar, a proper noun, a title, or code requires otherwise?
10. Are em dashes used sparingly: usually none in short copy, and only one or two in longer drafts when they clearly help, unless the writer's sample uses them?
11. Are quotation marks consistent throughout the document and matched to the writer or the target format?
12. Are hyphenated word pairs limited to what grammar needs, with stacked corporate jargon rewritten in plain words?

## Final read

1. Does the draft avoid robotic symmetry, repeated sentence shapes, and stacked punchy fragments?
2. Would the writer recognize the edited draft as their own voice?
3. Would the edited draft sound natural if read aloud to a sharp colleague?
4. Does the final output include the full edited draft and a short **What changed** section?
5. For detect requests, does the response name each pattern with a quoted line and a short fix, end with a summary line of findings, patterns, and where they cluster, and avoid rewriting, scoring, or claiming AI authorship?
6. In file mode, when the bundled scanner is available, does `scripts/slop_scan.py` report no `fix` finding on the rewritten file, and was each `watch` finding either fixed or judged fine in context?
