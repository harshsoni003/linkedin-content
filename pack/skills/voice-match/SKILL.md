---
name: voice-match
description: Builds a reusable voice profile from writing samples or an interview. Use when someone wants AI writing to sound like them, asks for a voice profile, or pastes their own writing for analysis.
---

# Voice match

Most people ask AI to write in their voice and hand it nothing to study. So the AI guesses, and every guess lands in the same place: the polished, forgettable voice of the average LinkedIn post. Readers scroll past it because it sounds like nobody in particular. This skill fixes the input, not the output. It studies writing you have already done, pins down the specific habits a stranger could pick you out of a lineup by, and packs them into a short profile you paste into any writing conversation from now on.

**When to use:** before AI writes anything public for you, or the moment a draft comes back sounding like everyone else.
**Time it takes:** about 10 minutes.
**What you end with:** a voice profile under 25 lines. Save it once, paste it forever.

## What to give it

**Best: your name, role, audience, and 3 to 10 LinkedIn posts you wrote yourself.** Full text, not links. Choose the ones that sound most like you, not just the ones that got likes. More posts means a sharper profile. Good input looks like this:

> Use voice-match. Here are five of my posts.
> My name is Dana Reyes. I run a bookkeeping firm. I write for owner-led small businesses.
> POST 1: We stopped billing by the hour in January. Moved 34 clients to flat monthly pricing. One left. [the rest of the post]
> POST 2: Stop running your business off your bank balance. [the rest of the post]
> POST 3: [full text] ...

**No posts? Emails and notes work.** Paste anything where you wrote real sentences: client emails, a newsletter, long messages to a friend about work. Aim for at least 300 words total. Remove anything confidential before pasting.

**Nothing written at all? Say "interview me."** You answer six questions by typing the way you talk. Each answer counts as a separate writing sample:

1. What is your name, what do you do, who do you write for, and what happened in your business this week? Answer in 3 to 5 sentences like a voice note to a friend. Do not polish it.
2. What is one opinion about your industry you would defend in an argument?
3. Which words or phrases do you use constantly? Which business words make you cringe?
4. A project just went wrong. Type the message you would actually send that client.
5. When you talk about money or results, do you say "$4,310" or "about four grand"?
6. Humor and swearing in your public writing: none, a little, or half your personality?

## The method

1. **Read every sample twice.** Once for what the person says, once for how they say it. The profile is about the how.
2. **Work through eleven dimensions, one at a time:** how their first lines behave, sentence rhythm, paragraph shape, punctuation, words they reach for, words they would never touch, signature moves, how they handle numbers, humor, how their posts end, and what would instantly break the voice.
3. **Apply the evidence rule.** A habit earns a line in the profile only if it shows up in at least two samples. One appearance is an accident. If the samples are thin on a dimension, say which lines are guesses instead of filling every field with confidence.
4. **Quote, do not summarize.** Wherever possible, anchor a line with a short fragment from their actual writing, in quotes. "Dry humor" tells them little. Quoting the joke shows the exact dose.
5. **Pull the three lines that sound most like them,** verbatim, from different posts, emails, notes, or interview answers. These are the examples every future draft gets held against.
6. **Run the half-of-LinkedIn test on every line.** If a line could describe half the people on LinkedIn ("conversational but professional", "tells stories"), sharpen it with a quoted fragment or cut it.
7. **Deliver the profile in the exact format below** and tell the user to save it somewhere easy to find: a notes app, a document, or anywhere they already keep useful writing material.

## Output

The voice profile, exactly this shape, under 25 lines:

```
VOICE PROFILE: [name]
Who I am: [one line: what you do and who you write for]

Openings: [how their first lines behave, with a quoted fragment]
Rhythm: [the sentence-length pattern they actually use]
Paragraphs: [how they break up text]
Punctuation: [what the samples show, including whether the writer uses em dashes]
Words I use: [5 to 8 words or phrases pulled straight from their writing]
Words I never use: [3 to 6 words that would ring false]
Signature moves: [2 to 4 specific habits, each seen in at least two samples]
Numbers: [how they handle figures: exact, rounded, rare]
Humor: [type and dose, or "none"]
Endings: [how their posts land]
Never do: [2 or 3 things that would instantly break the voice]

Sounds exactly like me:
1. "[verbatim line from their writing]"
2. "[verbatim line]"
3. "[verbatim line]"
```

If the profile was built from the interview instead of real writing, add one final line: `Built from interview only. Rerun voice-match after your first 5 real posts.`

## What good looks like

Read the finished profile line by line and ask of each one: could this describe half of LinkedIn? A good profile fails that question on every line. If two or more lines could belong to anyone, rerun the skill and paste more posts. The mark of a great profile: a stranger holding it could pick your post out of ten unlabeled posts from your industry.

## Guardrails

- Every line in the profile must trace to something visible in the pasted material. Never invent a trait to fill a field; write "not enough evidence yet" instead.
- If the user did not supply their name, role, or audience, write "not supplied" in that field instead of guessing.
- The profile describes how you actually write, not how you wish you wrote. If you want the voice to shift ("less formal", "more direct"), edit the finished profile by hand. Your edit wins.
- If someone pastes another person's posts, the profile will describe that person. Say so plainly instead of pretending it is theirs.
- No scores, no grades, no commentary on whether the writing is good. This is a working tool, not a report card.
- Match the punctuation visible in the supplied writing. If there is no clear evidence, prefer periods and commas. Do not add em dashes merely because generated writing often uses them.

## Works even better with

**post-writer.** Paste this profile at the top of any post-writer request and every draft starts in your voice instead of drifting toward the average.
