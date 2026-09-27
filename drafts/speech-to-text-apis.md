# Speech to text API comparison

**Goal:** gain relevant followers — share something useful, no pitch
**From:** raw-material (log it: testing transcription APIs for captions)
**Hook family:** first person
**Humanizer:** LinkedIn mode, 9/10
**Status:** Drafted — one claim to confirm

---

## The post

I tested 5 speech to text APIs for captions.

The fastest one is also the cheapest, which is not how this usually goes.

Here are the numbers.

All of these are for one 1 minute video.

• Groq Whisper Turbo, ~1 sec, ₹0.06, 8 hours free every day
• Deepgram Nova-3, ~2 sec, ₹0.37, $200 free credit
• ElevenLabs Scribe, ~3 to 5 sec, ₹0.31, 30 min free a month
• Gladia, ~10 sec, ₹0.86, 10 hours free a month
• Speechmatics, ~20 to 40 sec, ₹0.57, $100 free credit

Groq is up to 40 times faster than the slowest, and 14 times cheaper than the
most expensive. 8 free hours a day is more than I will get through.

One catch. Groq is the weakest of the five on Hindi. ElevenLabs Scribe was the
best I found for it, at 5 times the price.

So I am starting with Groq.

Numbers are approximate and from this week. Check them before you build on
them.

---

## Fill in before posting

- [ ] **"I am starting with Groq" is a plan, not a result.** True to your own
      note, which said "Now: Groq". If you have already wired it in, say
      "I went with Groq" instead, which is stronger.
- [ ] Optional: whether you are keeping Scribe as the Hindi fallback. That is a
      real decision and worth one line, but only you know it. I left it out
      rather than guess.
- [ ] Optional: what you are building this for. Naming Vireeli turns a useful
      post into a useful post people can follow. Leave it out if you would
      rather not plug.

## Alternate openings

**A — bare number**
> 1 second to transcribe a minute of video.
> ₹0.06 to do it.

*Sharpest open. Two numbers, no setup. Use if you want the figures to be the
hook rather than the test.*

**B — corrective**
> Fast, cheap, accurate. You usually get two.
> On transcription right now you can have all three.

*Widest reach and the most argument in the comments. Least about you.*

**C — this X / your X**
> If you are adding captions to anything, check the per minute price before
> you pick the model.
> Most of the difference is not accuracy.

*Most useful to a builder, most likely to be saved. Narrower, since it assumes
the reader is already shipping something with audio.*

## The call

Run the main one. "The fastest one is also the cheapest, which is not how this
usually goes" is the line doing the work: it states a real result and makes the
reader want the table. The five rows then pay it off, and the Hindi caveat is
what stops it reading like an ad for Groq.

## Voice notes

Applied from the profile:
- Opens on the work, no run-up
- Options listed, not described
- "One catch." on its own line, flat, no cushion
- No em dashes, no exclamation points, no hashtags, no "journey"
- Ends on the practical note, not a lesson

Two things kept in on purpose:
- **The Hindi weakness of the tool being recommended.** A comparison that hides
  the downside of its own pick reads like a sponsorship. Naming it is what
  makes the other four rows believable.
- **The caveat line.** The source table says "approximate", so the post says it
  too. The README rule is never to publish a number you can't defend.

Bullets are literal `•` characters, not markdown. LinkedIn strips markdown, so
`- item` pastes as a hyphen.

## Check before it ships

- [x] Every number came from the source table
- [x] Ratios checked: ₹0.86 ÷ ₹0.06 = 14x, ₹0.31 ÷ ₹0.06 = 5x, 40 sec ÷ 1 sec = 40x
- [x] Opening doesn't give away the ending — line 2 states the surprise,
      never names the winner
- [x] No "It's not X, it's Y"
- [x] No two consecutive lines on the same skeleton
- [x] Sentence lengths vary
- [x] Ending doesn't restate the opening
- [x] No hashtags, no emoji, no em dashes
- [ ] "starting with Groq" confirmed as plan or done
- [ ] Read out loud once
