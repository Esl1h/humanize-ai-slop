---
name: humanize-ai-slop
description: |
  Rewrite AI-sounding text so it reads like a person wrote it, without changing
  what it says, or flag every sign of AI writing without rewriting anything.
  Use when editing or reviewing prose for inflated claims, sales language,
  vague sources, repetitive structure, stock AI words, passive voice, filler,
  fake depth, or chatbot artifacts. Merges the patterns of Wikipedia's
  "Signs of AI writing" with the editing principles and rhetorical patterns
  of the No AI Slop project.
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

Do not rewrite, score the draft, or guess whether AI wrote it. AI detectors guess. Named patterns are evidence the user can check with their own eyes. When the draft is in a file and the bundled scanner is available, run `python3 scripts/slop_scan.py <path>` first: it lists the mechanical findings (banned words, dashes, decorated headings, mixed quotes, bold-label lists, stacked hyphen pairs) with pattern numbers, so you add only the rhetorical patterns. If the scanner is not installed, apply those checks by hand. Offer to edit the draft after.

## What to do

When given text to humanize:

1. **Find AI patterns.** Check the text against the patterns below.
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

The catalog in one glance, grouped by category. Use it to find a pattern by number when checking a draft instead of rereading the whole catalog.

**Content:** 1 inflated importance, 2 name-dropping, 3 shallow -ing analysis, 4 sales language, 5 vague sources, 6 vague association, 7 formulaic challenges
**Language and grammar:** 8 overused AI words, 9 avoiding is/are/has, 10 binary contrasts, 11 forced triads, 12 synonym cycling, 13 false ranges, 14 passive voice
**Style and formatting:** 15 dashes, 16 bold overload, 17 bold-label lists, 18 title case headings, 19 emoji decoration, 20 quote consistency
**Chatbot:** 21 chatbot leftovers, 22 knowledge-limit guesses, 23 agreeable tone, 24 re-explaining shared context
**Filler and endings:** 25 filler phrases, 26 qualifier stacks, 27 generic endings and recaps
**Hyphenation:** 28 hyphenated pairs
**Fake depth and rhetoric:** 29 fake deeper truth, 30 announcing the point, 31 heading restated, 32 writing about the document, 33 forced punchlines, 34 formulaic sayings, 35 fake-candid openers, 36 unanswered objections, 37 fake alternatives, 38 colon reveals, 39 interpretive metadiscourse, 40 formatting slop, 41 faux-insight setups

## AI writing patterns

### Content patterns

#### 1. Inflated claims about importance and legacy

**Words to watch:** stands/serves as, is a testament/reminder, a vital/significant/crucial/pivotal/key role/moment, underscores/highlights its importance/significance, reflects broader, symbolizing its ongoing/enduring/lasting, contributing to the, setting the stage for, marking/shaping the, represents/marks a shift, key turning point, evolving landscape, focal point, indelible mark, deeply rooted, solidifies its position

**Problem:** AI writing often claims that ordinary details mark a major change, prove a legacy, or reflect a broad trend. State the fact and let the reader judge whether it matters.

**Before:**
> The Statistical Institute of Catalonia was officially established in 1989, marking a pivotal moment in the evolution of regional statistics in Spain. This initiative was part of a broader movement across Spain to decentralize administrative functions and enhance regional governance.

**After:**
> The Statistical Institute of Catalonia was established in 1989, part of a wider decentralization of administrative functions in Spain.

**Before (product launch):**
> The launch marks a pivotal moment for the company.

**After:**
> The launch is the company's first paid product.

#### 2. Name-dropping to prove importance

**Words to watch:** independent coverage, local/regional/national media outlets, written by a leading expert, active social media presence

**Problem:** AI writing often lists well-known publications or follower counts to prove that a person matters. The list usually gives no useful context.

**Before:**
> Her views have been cited in The New York Times, BBC, Financial Times, and The Hindu. She maintains an active social media presence with over 500,000 followers.

**After:**
> Her views have been cited in The New York Times and the BBC.

If the source explains what the person said and where, keep that useful citation. Do not invent context for a shorter version.

#### 3. Shallow analysis with -ing phrases

**Words to watch:** highlighting/underscoring/emphasizing..., ensuring..., reflecting/symbolizing..., contributing to..., cultivating/fostering..., encompassing..., showcasing...

**Problem:** AI writing often adds a trailing -ing phrase to make a simple fact sound deeper than it is, or to pretend to explain what the fact means.

**Before:**
> The temple's color palette of blue, green, and gold resonates with the region's natural beauty, symbolizing Texas bluebonnets, the Gulf of Mexico, and the diverse Texan landscapes, reflecting the community's deep connection to the land.

**After:**
> The temple is painted blue, green, and gold, colors meant to evoke Texas bluebonnets and the Gulf of Mexico.

**Before (product copy):**
> The launch adds file search, highlighting the team's commitment to better workflows.

**After:**
> The launch adds file search, so users can find old drafts without leaving the editor.

Replace the -ing phrase with a real consequence only when the source supports it. Otherwise cut it.

#### 4. Sales language

**Words to watch:** boasts a, vibrant, rich (figurative), profound, enhancing its, showcasing, exemplifies, commitment to, natural beauty, nestled, in the heart of, groundbreaking (figurative), renowned, breathtaking, must-visit, stunning, unwavering

**Problem:** AI writing often sounds like an advertisement, especially when it describes places, culture, products, or organizations.

**Before:**
> Nestled within the breathtaking region of Gonder in Ethiopia, Alamata Raya Kobo stands as a vibrant town with a rich cultural heritage and stunning natural beauty.

**After:**
> Alamata Raya Kobo is a town in the Gonder region of Ethiopia.

#### 5. Vague sources and weasel attribution

**Words to watch:** experts believe/agree/argue, industry reports suggest, observers have cited, some critics argue, many argue, widely regarded as, studies show, several sources/publications (when few are cited)

**Problem:** AI writing often assigns a claim to unnamed experts, critics, reports, or observers.

**Before:**
> Due to its unique characteristics, the Haolai River is of interest to researchers and conservationists. Experts believe it plays a crucial role in the regional ecosystem.

**After:**
> Researchers and conservationists study the Haolai River for its unusual characteristics.

Name a real source when the source text provides one. Otherwise, remove the unsupported claim. If the user has no source, ask instead of inventing one.

#### 6. Vague connection or association

**Words to watch:** associated with, in association with, connected to, in connection with, linked to, tied to

**Problem:** AI writing often says two things are connected without saying how. "He was associated with the orchestra" hides whether he founded it, conducted it, or only reviewed it. Name the relationship the source gives. If the source does not say how, keep the vague wording rather than inventing a role.

**Before:**
> He is associated with the Rajhans Orchestra, which he founded and conducts. The concerts were organised in connection with the celebrations of Pakistan's 50th anniversary.

**After:**
> He founded and conducts the Rajhans Orchestra. The concerts were part of the celebrations of Pakistan's 50th anniversary.

#### 7. Formulaic challenges and outlook sections

**Words to watch:** Despite its... faces several challenges..., Despite these challenges, Challenges and Legacy, Future Outlook, continues to thrive

**Problem:** AI articles often add a stock section about challenges, future prospects, or continued growth. These sections usually repeat vague claims instead of adding facts.

**Before:**
> Despite its industrial prosperity, Korattur faces challenges typical of urban areas, including traffic congestion and water scarcity. Despite these challenges, with its strategic location and ongoing initiatives, Korattur continues to thrive as an integral part of Chennai's growth.

**After:**
> Korattur has recurring traffic congestion and water shortages.

Add details such as dates or public actions only when they come from the source or the user.

### Language and grammar patterns

#### 8. Overused AI words

**High-frequency AI words:** actually, additionally, align with, bolstered, crucial, deep dive, delve, emphasizing, enduring, enhance, fostering, garner, gate/gated/gating (figurative; keep established technical usage), highlight (verb), interplay, intricate/intricacies, journey (figurative), key (adjective), landscape (abstract noun), leverage, pivotal, quietly, robust, seamless, showcase, tapestry (abstract noun), testament, underscore (verb), valuable, vibrant

**Problem:** AI writing uses these words much more often than most people do, especially in groups.

**Before:**
> Additionally, a distinctive feature of Somali cuisine is the incorporation of camel meat. An enduring testament to Italian colonial influence is the widespread adoption of pasta in the local culinary landscape, showcasing how these dishes have integrated into the traditional diet.

**After:**
> Somali cuisine also includes camel meat, which is considered a delicacy. Pasta dishes, introduced during Italian colonization, remain common, especially in the south.

#### 9. Avoiding is, are, and has

**Words to watch:** serves as/stands as/marks/represents [a], boasts/features/offers [a], acts as, functions as

**Problem:** AI writing often replaces simple verbs such as *is*, *are*, and *has* with longer phrases that sound stronger and say less.

**Before:**
> Gallery 825 serves as LAAA's exhibition space for contemporary art. The gallery features four separate spaces and boasts over 3,000 square feet.

**After:**
> Gallery 825 is LAAA's exhibition space for contemporary art. The gallery has four rooms totaling 3,000 square feet.

**Before (fake-strong verb):**
> The app serves as a centralized hub for sponsor management.

**After:**
> The app tracks sponsors, drafts, due dates, and approvals in one place.

#### 10. Not X but Y, binary contrasts, and negative listing

**Problem:** AI writing overuses forms such as "not only... but...", "it's not just X, it's Y", "the question isn't X, it's Y", inside one sentence or split across two. It also stacks negations before the point ("Not a X. Not a Y. A Z.") and adds clipped endings such as "no guessing" instead of writing a clear clause. State Y directly.

**Before:**
> It's not just about the beat riding under the vocals; it's part of the aggression and atmosphere. It's not merely a song, it's a statement.

**After:**
> The heavy beat adds to the aggressive tone.

**Before (two-sentence contrast):**
> The question isn't the model. It's the eval.

**After:**
> The eval matters more than the model.

**Before (negative listing):**
> Not a framework. Not a library. A new way to think about state.

**After:**
> It is a state management pattern, not a library.

**Before (tailing negation):**
> The options come from the selected item, no guessing.

**After:**
> The options come from the selected item without forcing the user to guess.

#### 11. Forced groups of three

**Problem:** AI writing often forces ideas into groups of three to sound complete.

**Before:**
> The event features keynote sessions, panel discussions, and networking opportunities. Attendees can expect innovation, inspiration, and industry insights.

**After:**
> The event includes talks and panels. There's also time for informal networking between sessions.

#### 12. Synonym cycling and repeated sentence openings

**Problem:** AI writing handles repetition by rule instead of by ear. It may keep renaming the same person or thing. It may also start several sentences with the same subject, often *she* or *he*.

Use one clear name for the same subject. If the clear word is right, repeat it. For repeated openings, merge sentences, change the subject when that helps, or begin with the action.

**Before (synonym cycling):**
> The agent reviews the draft. The assistant scores the piece. The tool suggests fixes.

**After:**
> The agent reviews the draft, scores it, and suggests fixes.

**Before (repeated openings):**
> She noted the door. She noted the lock on it. She filed both away.

**After:**
> She noted the door and its lock, then filed both away.

Do not ban the repeated word. Fix the repeated sentence pattern. The remaining sentence may still start with "She."

#### 13. False from X to Y ranges

**Problem:** AI writing often uses "from X to Y" when X and Y do not form a real range.

**Before:**
> Our journey through the universe has taken us from the singularity of the Big Bang to the grand cosmic web, from the birth and death of stars to the enigmatic dance of dark matter.

**After:**
> The book covers the Big Bang, star formation, and current theories about dark matter.

#### 14. Passive voice and missing subjects

**Problem:** AI writing often hides who acts or drops the subject. Use active voice when it makes the actor and action clearer. Never let inanimate things do human verbs ("the decision emerged").

**Before:**
> No configuration file needed. The results are preserved automatically.

**After:**
> You do not need a configuration file. The system preserves the results automatically.

### Style and formatting patterns

#### 15. Em and en dashes

**Rule:** The final rewrite must not use em dashes (—) or en dashes (–) as a rhythm crutch, unless the writer's sample uses them. Replace a dash with a period, comma, colon, or parentheses, or rewrite the sentence. Also check for spaced dashes ( — ) and double hyphens (--) used as dashes. In short copy, use none. In longer drafts, one or two are fine if they clearly beat commas, periods, or parentheses. Remove clusters and decorative dashes.

**Before:**
> The term is primarily promoted by Dutch institutions—not by the people themselves. You don't say "Netherlands, Europe" as an address—yet this mislabeling continues—even in official documents.

**After:**
> The term is primarily promoted by Dutch institutions, not by the people themselves. You don't say "Netherlands, Europe" as an address, yet this mislabeling continues in official documents.

**Before:**
> The new policy — announced without warning — affects thousands of workers. The changes -- long overdue according to critics -- will take effect immediately.

**After:**
> The new policy, announced without warning, affects thousands of workers. The changes, long overdue according to critics, will take effect immediately.

Before returning the rewrite, search for `—` and `–`. Remove each one unless the writer's sample uses that mark. In that case, match the sample's rate.

#### 16. Too much bold text

**Problem:** AI chatbots often bold words and phrases without a clear reason.

**Before:**
> It blends **OKRs (Objectives and Key Results)**, **KPIs (Key Performance Indicators)**, and visual strategy tools such as the **Business Model Canvas (BMC)** and **Balanced Scorecard (BSC)**.

**After:**
> It blends OKRs, KPIs, and visual strategy tools like the Business Model Canvas and Balanced Scorecard.

#### 17. Lists with bold mini-headings

**Problem:** AI writing often uses vertical lists in which every item starts with a bold label and a colon.

**Before:**
> - **User Experience:** The user experience has been significantly improved with a new interface.
> - **Performance:** Performance has been enhanced through optimized algorithms.
> - **Security:** Security has been strengthened with end-to-end encryption.

**After:**
> The update improves the interface, speeds up load times through optimized algorithms, and adds end-to-end encryption.

#### 18. Title case in headings

**Problem:** AI chatbots often capitalize every main word in a heading.

**Before:**
> ## Strategic Negotiations And Global Partnerships

**After:**
> ## Strategic negotiations and global partnerships

#### 19. Emojis

**Problem:** AI chatbots often add emojis to headings and list items as decoration.

**Before:**
> 🚀 **Launch Phase:** The product launches in Q3
> 💡 **Key Insight:** Users prefer simplicity
> ✅ **Next Steps:** Schedule follow-up meeting

**After:**
> The product launches in Q3. User research showed a preference for simplicity. Next step: schedule a follow-up meeting.

#### 20. Curly quotation marks and mixed quote styles

**Problem:** ChatGPT often uses curly quotes (“...”) where the writer or the target format uses straight quotes ("..."). Mixing both styles in one document is a stronger sign than either style alone. Match the quote style of the writer's sample or the target format, and keep it consistent throughout.

**Before:**
> He said “the project is on track” but others disagreed.

**After:**
> He said "the project is on track" but others disagreed.

Curly quotes by themselves are not evidence of AI. See [What not to flag](#what-not-to-flag).

### Chatbot patterns

#### 21. Chatbot text left in the answer

**Words to watch:** I hope this helps, Of course!, Certainly!, You're absolutely right!, Would you like..., Want me to...?, Want me to give examples?, Should I continue?, let me know, here is a...

**Problem:** A chatbot's greeting, offer, or closing sometimes remains in text that should stand on its own.

**Before:**
> Here is an overview of the French Revolution. I hope this helps! Let me know if you'd like me to expand on any section.

**After:**
> The French Revolution began in 1789 when financial crisis and food shortages led to widespread unrest.

#### 22. Knowledge-limit disclaimers and guesses

**Words to watch:** as of [date], up to my last training update, while specific details are limited/scarce..., based on available information, not publicly available, maintains a low profile, keeps personal details private, prefers to stay out of the spotlight, likely [grew up/studied/began], it is believed that

**Problem:** Older models may mention the date when their knowledge ends. A model may also explain that it could not find a source, then fill the gap with a plausible guess. State what the source does not show, or remove the sentence. Do not present a guess as a fact.

**Before (cutoff disclaimer):**
> While specific details about the company's founding are not extensively documented in readily available sources, it appears to have been established sometime in the 1990s.

**After:**
> The company's founding date is not documented in the available sources. (Or cut the sentence. State a date only if a source provides one.)

**Before (speculative gap-fill):**
> Information about her early life is not publicly available, suggesting she maintains a low profile and keeps personal details private. She likely grew up in a middle-class household, which shaped her later interest in education reform.

**After:**
> Her early life is not documented in the available sources. (Or omit the section.)

#### 23. Overly agreeable tone

**Problem:** AI assistants often praise the user or agree before giving the answer.

**Before:**
> Great question! You're absolutely right that this is a complex topic. That's an excellent point about the economic factors.

**After:**
> The economic factors you mentioned are relevant here.

#### 24. Re-explaining what the reader already knows

**Signs to watch:** a short reply that restates the problem, walks through the diagnosis, and lays out the evidence before it reaches the decision; a query, command, or set of numbers included to prove a plan will work; background the other person wrote or already agreed to; the answer itself sitting in the last line.

**Problem:** In a reply, the reader already has the context, so rebuilding it adds nothing and buries the point. Each sentence can read fine on its own, so this tell survives sentence-level cleanup. Lead with the decision and keep only the reasoning that would change whether the reader agrees: usually one fact they lack and any link they need to act. The diagnosis and the proof belong in the ticket or document that follows. Act on this pattern when you can see the surrounding conversation or the text plainly is a reply. If you cannot tell, ask or leave the text alone.

**Before:**
> Yeah, you're right, this works around the issue rather than fixing it. The real fix is in `MergeService`: when we move a child under a new parent, it should update `pipeline_id` along with `parent_id`. We can backfill the bad rows from the audit log. I checked QA: 123 past merges, only 6 rows wrong now, so the cleanup is small.
>
> Since `MergeService` is shared code, I'd rather open a separate ticket than widen this PR. The fallback here is fine to keep until then.

**After:**
> Agreed, this is a workaround. Fixing `MergeService` means touching shared code plus a small backfill, which would widen this PR past its scope.
>
> I'd rather open a separate ticket for the fix and keep the fallback here until then.

### Filler, hedging, and endings

#### 25. Filler phrases

**Before → After:**
- "In order to achieve this goal" → "To achieve this"
- "Due to the fact that it was raining" → "Because it was raining"
- "At this point in time" → "Now"
- "In the event that you need help" → "If you need help"
- "The system has the ability to process" → "The system can process"
- "It is important to note that the data shows" → "The data shows"
- "Made a decision to" → "Decided to"

#### 26. Too many qualifiers

**Phrases to watch:** to be fair, it's also possible, could potentially, might arguably, in some cases it may, this is an inference

**Problem:** Repeated editing can add one qualifier after another until every claim sounds uncertain. Keep a qualifier only when the source supports it and the meaning needs it. Remove caveats that only repair an earlier overstatement.

**Before:**
> It could potentially possibly be argued that the policy might have some effect on outcomes.

**After:**
> The policy may affect outcomes.

#### 27. Generic positive endings and summary recaps

**Words to watch:** the future looks bright, exciting times lie ahead, in conclusion, ultimately, overall, as we have seen, to sum up

**Problem:** AI writing often ends with vague optimism instead of the last useful fact, or with a final paragraph that restates the piece. The reader was just there. End on the last concrete point, takeaway, or next action instead. For endings that turn the point into a metaphor or mic-drop line, see pattern 34.

**Before (generic ending):**
> The future looks bright for the company. Exciting times lie ahead as they continue their journey toward excellence. This represents a major step in the right direction.

**After:**
> (Cut the paragraph. End on the last concrete fact instead of a send-off. If the source states real plans, use those.)

**Before (recap):**
> In conclusion, we have covered the main points of the migration. As we have seen, the new pipeline brought many benefits to the team.

**After:**
> (Cut the recap paragraph. End on the most recent concrete point or a next action.)

### Hyphenation

#### 28. Too many hyphenated word pairs

**Words to watch:** third-party, cross-functional, client-facing, data-driven, decision-making, well-known, high-quality, real-time, long-term, end-to-end, customer-centric, state-of-the-art

**Problem:** AI writing often hyphenates these pairs everywhere, and stacks several of them in one sentence as corporate shorthand. Keep the hyphen before a noun when grammar needs it, as in `a high-quality report`. Drop it after the noun, as in `the report is high quality`. When three or more stack up, rewrite with plain words.

**Before:**
> The cross-functional team delivered a high-quality, data-driven report. The team is cross-functional, the report is high-quality, and the methodology is data-driven.

**After:**
> The cross-functional team delivered a high-quality, data-driven report. The team is cross functional, the report is high quality, and the methodology is data driven.

**Before (stacked jargon):**
> We built a customer-centric, data-driven, state-of-the-art onboarding flow.

**After:**
> We rebuilt onboarding around what customers told us in interviews and what the usage data showed.

Keep the hyphenated term when it is the established name of a technology or concept (end-to-end encryption, real-time operating system). The target is decorative jargon, not technical vocabulary.

### Fake depth and rhetoric

#### 29. Pretending to reveal a deeper truth

**Phrases to watch:** the real question is, at its core, in reality, what really matters, fundamentally, the deeper issue, the heart of the matter

**Problem:** AI writing uses these phrases to make an ordinary point sound like a hidden truth.

**Before:**
> The real question is whether teams can adapt. At its core, what really matters is organizational readiness.

**After:**
> The question is whether teams can adapt. That mostly depends on whether the organization is ready to change its habits.

#### 30. Announcing the next point and rhetorical setups

**Phrases to watch:** let's dive in, let's explore, let's break this down, here's what you need to know, now let's look at, without further ado, heads up, quick note, before I forget, what if I told you, think about it:, plot twist:, and self-answered "Question? Answer." pairs

**Problem:** AI writing often announces the next point instead of stating it, or stages a rhetorical setup before a routine claim. A casual phrase such as "one thing that bit me" can have the same problem. Remove the announcement, not just its formal tone.

**Before:**
> Let's dive into how caching works in Next.js. Here's what you need to know.

**After:**
> Next.js caches data at multiple layers, including request memoization, the data cache, and the router cache.

**Before (casual register):**
> One thing that bit me hard, so pay attention to this part: the webpack dev server doesn't send the CORS header by default.

**After:**
> The webpack dev server doesn't send the CORS header by default.

**Before (rhetorical setup):**
> What if I told you that most of your test suite never catches a real bug? Think about it: coverage measures lines, not behavior.

**After:**
> Most of the test suite never catches a real bug, because coverage measures lines, not behavior.

#### 31. A heading repeated in the first sentence

**Signs to watch:** A heading followed by a one-line paragraph that simply restates the heading before the real content begins.

**Problem:** AI writing often follows a heading with a sentence that only repeats the heading. Remove the repeated sentence.

**Before:**
> ## Performance
>
> Speed matters.
>
> When users hit a slow page, they leave.

**After:**
> ## Performance
>
> When users hit a slow page, they leave.

#### 32. Writing about the document instead of its subject

**Words to watch:** was added to replace, generated from, compiled from, drawn from, the table below compares, this section is organized by, the sections that follow

**Problem:** The text describes itself instead of its subject. The move has three forms: what the text replaced, how it was assembled or sourced, and a legend, layout, or order the reader can already see. Mention a previous version only in change logs, release notes, migration guides, and other documents about change. Keep a source credit the reader can follow, and cut the account of how you worked. Keep a caveat that changes what the reader should do. State a convention only when the reader cannot infer it, and state it once.

**Before:**
> This function was added to replace the previous approach of iterating through all items, which caused O(n²) performance.

**After:**
> This function uses a hash map for O(1) lookups, avoiding the O(n²) cost of naive iteration.

**Before (method narration):**
> The figures below are drawn from each vendor's published pricing; anything we could not confirm is flagged rather than guessed.

**After:**
> Prices are each vendor's published rate. Two vendors publish nothing; call them.

#### 33. Forced punchlines, dramatic fragments, and robotic rhythm

**Problem:** AI writing often turns each sentence into a dramatic closing line. One short sentence can add emphasis. A row of short fragments usually feels forced ("That's it. That's the whole thing."), and so do paragraphs that repeat the same sentence shape one after another. Use complete sentences and vary the shape only when it helps the point.

**Before:**
> Then AlphaEvolve arrived. It had no preference for symmetry. No aesthetic prior. No nostalgia for human taste. The old rules were gone.

**After:**
> AlphaEvolve changed the search because it did not favor symmetry or human-looking designs. That made some of the older assumptions less useful.

#### 34. Formulaic sayings and fake-profound kickers

**Words to watch:** X is the Y of Z, X becomes a trap, X is not a tool but a mirror, the language of, the currency of, the architecture of, the future isn't coming, it's already here

**Problem:** AI writing often turns an ordinary claim into a saying that sounds deep but adds no detail. It also likes to close a piece with a "deep" line that turns the point into a cute metaphor, aphorism, or mic-drop sentence. Replace a saying in the body with the specific claim. Delete a kicker at the end instead of rewriting it into a better metaphor, then end on the clearest concrete sentence already in the draft. If the ending needs more closure, add a plain takeaway or next action.

**Before (saying):**
> Symmetry is the language of trust. Efficiency becomes a trap when teams forget the human layer.

**After:**
> Symmetric layouts often feel more predictable to users. Teams can over-optimize workflows and miss how people actually use them.

**Before (kicker):**
> We shipped the new billing flow to all customers on Monday. The future of payments isn't coming. It's already here.

**After:**
> We shipped the new billing flow to all customers on Monday.

#### 35. Fake-candid and throat-clearing openers

**Phrases to watch:** Honestly?, Look, Here's the thing, Here's what I mean, The thing is, Let me be clear, Let's be honest, I'll be honest, Real talk, The uncomfortable truth is, when used as standalone hooks or staged pauses before an ordinary point

**Problem:** AI writing often starts with a staged pause or claim of honesty before making a routine point. Cut the opener and state the point directly.

**Before:**
> Is it worth the price? Honestly? It depends on how often you'll use it.

**After:**
> Whether it's worth the price depends on how often you'll use it.

**Before:**
> Here's the thing: most onboarding flows ask for too much on the first screen.

**After:**
> Most onboarding flows ask for too much on the first screen.

#### 36. Answering objections no one raised

**Phrases to watch:** This isn't (mainly/really) about, I'm not saying/arguing/trying to, To be clear, Don't get me wrong, This is not to say, You could argue/frame this differently but, Some might say... but

**Problem:** AI writing may answer an objection that does not appear in the text. Watch for an unattributed statement about what the writer does not mean, especially when the topic appears nowhere else. A direct claim such as "the API is not thread-safe" is not this pattern.

**Before:**
> This isn't mainly about prompt length, and I'm not arguing that documentation doesn't matter. You could categorize the problem another way, but the issue is whether the agent can use the instruction when it acts.

**After:**
> The issue is whether the agent can use the instruction when it acts.

Remove only the unsupported defense. If it contains a real claim, state that claim directly. Keep an objection when the text names its source or answers it in full.

#### 37. Rejecting fake alternatives

**Phrases to watch:** A tempting option/approach would be, One might be tempted to, An obvious approach would be, You might think... but, It would be easy to just, Some would suggest

**Problem:** AI writing may introduce an option that no reader would consider, reject it in a clause, and never mention it again. This often leaves an old drafting idea in the final text. Remove the fake option and state the real constraint directly.

**Before:**
> Session tokens are rotated every 24 hours. A tempting approach would be to rotate them by restarting the auth service on a cron job, but that would drop every active session. Rotation happens in place, and clients refresh transparently.

**After:**
> Session tokens are rotated every 24 hours, in place, and clients refresh transparently.

One rejected option may be valid. Several short, unrelated rejections are a stronger sign. Ask what new information each sentence adds. If it only records an earlier edit, rewrite the paragraph around its main point.

#### 38. Colon reveals

**Problem:** AI writing likes to set up a noun phrase, a colon, then a lowercase dramatic reveal: "The detail that makes it work: a separate agent grades it." "The best part: it learns." Rewrite as a plain sentence. Use colons for lists, labels, and quotes, not fake drama. Prefer sentence case after a colon unless grammar, a proper noun, a title, or code requires otherwise.

**Before:**
> The detail that makes it work: a separate agent grades the output.

**After:**
> A separate agent grades the output, which is what makes the system work.

#### 39. Interpretive metadiscourse

**Problem:** AI writing sometimes steps outside the subject to tell the reader what to notice, how much weight to give it, or how to interpret the prose: "That last part matters more than it sounds," "The key point is," "As you can see," "This distinction matters," a sentence after an example, scene, or number that names what it showed ("This shows the importance of..."), or a redundant "In other words." If the point is clear, delete the aside. Otherwise, replace it with support or facts already in the content.

**Before:**
> That last part matters more than it sounds. As you can see, this distinction is essential. In other words, the process got faster.

**After:**
> The process got faster.

#### 40. Formatting slop

**Problem:** Several artificial formatting habits usually show up together: emoji in headings (pattern 19), bold sprinkled mid-sentence for emphasis (pattern 16), bullet lists where two sentences of prose would read better (pattern 17), and headers over two-sentence sections (pattern 31). The same family covers arrows and other symbols used as decoration, a horizontal rule between every section, a document that opens by repeating its own title, and headings written for effect instead of naming what the section holds ("The decision, on one screen" becomes "How the six options compare"). Format should follow the content, not decorate it. When reviewing, ask whether each visual element carries information or only imitates the look of an organized document.

#### 41. Faux-insight setups

**Phrases to watch:** this is the part most people skip, what most people get wrong, here's what nobody tells you, the part everyone misses, the secret is, most people don't realize

**Problem:** AI writing flatters the writer as the lone expert before a claim that can stand on its own. Cut the setup and make the claim carry itself. If the claim is genuinely contrarian, the surrounding evidence should show that, not the framing.

**Before:**
> Here's what nobody tells you about hiring: most interviews measure confidence, not skill.

**After:**
> Most interviews measure confidence, not skill.

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

**Pasted text (default).** Return the draft, a short list of remaining AI patterns, and the final rewrite with a short **What changed** section.

**File mode.** When the user names a file, run the full rewrite process but write only the final text to the file. Change prose only. Keep code blocks, YAML metadata, data, and link targets unchanged. Then give the user a short summary.

**Embedded mode.** When another task uses this skill for a pull request, commit message, or document, return only the final text.

**Detect mode.** One line per finding, in document order: **Pattern N (name):** "quoted line" → the fix in a few words. Do not rewrite the draft, score it, or claim whether AI wrote it.

## Rewrite process and self-check

1. Read the full draft and mark each AI pattern. Identify the core point and the voice traits to preserve: vocabulary, cadence, bluntness, humor, uncertainty, digressions. If you cannot identify the core point, ask the user.
2. For a detect request, return the findings report described in [Two modes](#two-modes) and stop.
3. Write a draft. Read it aloud. Check the rhythm, details, simple verbs such as *is* and *has*, and the right level of formality.
4. Ask two questions:
   - **"What still sounds AI-generated?"**
   - **"Did the rewrite add or remove any fact, name, number, date, quote, citation, ranking, or other claim?"**
   Treat any unsupported addition or lost claim as an error.
5. Write the final version. State each point naturally instead of patching one flagged phrase at a time. If a sentence stays awkward, rewrite the paragraph around its main point. Apply the dash rule in pattern 15.
6. Check the rewrite against the list in [`eval.md`](eval.md). If any check fails, fix the draft and run the checks again. In file mode, when the bundled scanner is available, run `python3 scripts/slop_scan.py <path>` on the rewritten file as the last check; a clean rewrite reports nothing.

Return the result required by [How to return the result](#how-to-return-the-result).

## Sources

This skill merges two English sources:

- [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing), maintained by WikiProject AI Cleanup, as organized into numbered patterns by earlier versions of [Humanizer](https://github.com/blader/humanizer). Its later v3 revision, reordered by strength, contributed patterns 6 and 24 and the widened forms of 32 and 40. Its patterns come from reviews of AI-generated text on Wikipedia.
- [No AI Slop](https://github.com/petergyang/no-ai-slop), by Peter Yang, which contributed the editing principles, the detect mode, the word lists, the self-check list, and the rhetorical patterns in sections 34, 35, 38, 39, 40, and 41.

The merge and the numbering follow [Humanize BR](https://github.com/Esl1h/humanize-br), which combined the same two sources for Brazilian Portuguese.

Wikipedia's main point: "LLMs use statistical algorithms to guess what should come next. The result tends toward the most statistically likely result that applies to the widest variety of cases." That statistical flattening is what this skill tries to undo.
