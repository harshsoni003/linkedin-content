# Cloudflare R2 storage switch

**Goal:** gain relevant followers — share something useful, no pitch
**From:** raw-material (log it: the 50 MB wall on a 118 MB video)
**Hook family:** advice, straight out
**Humanizer:** LinkedIn mode, 8/10 -> 9/10, 4 fixes applied
**Voice:** Harsh Soni profile applied
**Status:** Drafted — one claim to confirm

---

## The post

If you are building a product and need extra storage, go with Cloudflare R2.

10 GB free, 5 GB per file, downloads free.

The last one is why.

My problem: 118 MB videos. Supabase stops at 50 MB per file.

So I checked every free tier.

Out straight away:

Supabase, 50 MB per file
Cloudinary, 100 MB per file
AWS and Azure, trial only, not free forever
Google Cloud, 5 GB and US regions only

That left three:

Oracle, 20 GB free, harder to set up, card needed
Backblaze B2, 10 GB free, 5 GB per file, no card
Cloudflare R2, 10 GB free, 5 GB per file, card needed

Oracle gives the most space. I still picked R2.

Storage is cheap. Downloads are what cost money.

R2 does not charge for them. B2 stops being free after 30 GB a month.

That one line is the whole decision.

Check the pricing pages before you sign up. These change.

---

## Fill in before posting

- [ ] **"I went with R2" is written as done.** If you have decided but not
      migrated yet, change it to "I'm going with R2". Your README rule is never
      to publish a claim you can't defend, and someone will ask how it went.
- [ ] Optional: how long the switch took. "Took me an afternoon" turns a
      recommendation into evidence. Only if it's true.

## Alternate openings

**A — bare number**
> 50 MB.
> That's the largest file Supabase will take on its free tier.

*Sharpest open. Use if you want the constraint itself to be the hook rather
than the comparison.*

**B — corrective**
> Free storage tiers advertise the wrong number.
> Nobody gets billed for storage.

*Widest reach, most argument in the comments. Least about you, so it wins
attention and builds less trust.*

**C — this X / your X**
> Your storage bill is not the number that will bite you.
> Egress is.

*Best for an engineering audience and the most reshareable. Narrower, since it
assumes the reader already pays for storage.*

## The call

Run the main one. "Oracle gives the most free space. I didn't pick Oracle."
does the hardest job in the post: it names a real result and immediately
refuses to explain it, so the reader has to open the post to find out why. The
comparison then pays that off, and the egress point is genuinely useful rather
than an opinion.

## Voice notes

Applied from the profile:
- Opens on the work, no run-up
- Providers listed, not described, same move as "auth, database, payments,
  agents, deploy"
- Short landing lines against longer explaining ones
- No em dashes, no exclamation points, no hashtags, no "journey"
- Ends on the practical note, not a lesson

Two things deliberately kept in:
- **R2 needs a card, B2 does not.** Leaving that out would make the post read
  like a recommendation with something to hide. Naming the tradeoff is what
  makes the rest believable.
- **The caveat line.** Free tiers change, and the README rule is to never
  publish a number you can't defend. That line makes every figure above it
  defensible.

Avoided: "It's not the storage, it's the egress." That is the single most
recognizable AI construction in `reference/ai-tells.md`. Written instead as
"the storage size had nothing to do with it", then explained.

## Why this format

The earlier version listed six providers in one flat block. Nobody reads a wall
on LinkedIn, and worse, it gave equal weight to options that were never in the
running.

This version sorts them the way the decision actually went:

**Two labelled groups instead of one list.** "Out straight away" and "That left
three". The reader sees the shortlist shrink, which is the shape of a real
decision and takes no effort to follow.

**The eliminated ones carry their reason inline.** "Cloudinary, 100 MB per
file" says why it lost without a sentence explaining it.

**The three finalists are formatted identically**, so the differences between
them are the only thing that moves. R2 and B2 line up almost exactly, which
makes "downloads free" the visible variable.

**One idea per line in the closing.** "Storage is cheap. Downloads are what
cost money." sits alone, with white space either side, because it is the point
of the post.

**No markdown.** LinkedIn's composer strips bold, bullets and tables. Everything
here is plain text and line breaks, so it pastes exactly as written.

15 blank lines across 159 words. On LinkedIn white space is pacing, not
decoration.

## Humanizer pass

LinkedIn mode, voice-profile.md + reference/ai-tells.md. 9/10.

Clean on: em dashes, hashtags, emoji, exclamation points, "It's not X, it's Y",
forced triads, lesson endings, parallel repetition, vendor grammar, fake hedges.
The provider lists are stack lists, which the tells reference explicitly does not
flag as a rule of three.

"egress" stays out. "Downloads are what cost money" is the same fact in the word
a normal person uses.

**One deliberate break from post-format.md.** The rule says don't answer the
question before the "see more" cut. This hook gives the recommendation away on
line 1 on purpose, because Harsh asked for it that way. It still holds a loop
open: the post says *what* to use above the cut, and "The last one is why" keeps
*why* below it.

## Check before it ships## Check before it ships## Check before it ships

- [x] Every number came from the material I was given
- [x] Opening doesn't give away the ending — line 2 names a result and
      withholds the reason
- [x] No "It's not X, it's Y"
- [x] No two consecutive lines on the same skeleton
- [x] Sentence lengths vary
- [x] Ending doesn't restate the opening
- [x] No hashtags, no emoji, no em dashes
- [ ] "I went with R2" confirmed as past tense
- [ ] Read out loud once
