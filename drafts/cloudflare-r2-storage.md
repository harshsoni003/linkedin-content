# Cloudflare R2 storage switch

**Goal:** gain relevant followers — share something useful, no pitch
**From:** raw-material (log it: the 50 MB wall on a 118 MB video)
**Hook family:** first person
**Humanizer:** LinkedIn mode, 8/10 -> 9/10, 4 fixes applied
**Voice:** Harsh Soni profile applied
**Status:** Drafted — one claim to confirm

---

## The post

I compared every free storage tier I could find.

Oracle gives the most free space. I didn't pick Oracle.

Here's what actually decided it.

I needed somewhere to put 118 MB videos. Supabase caps a single file at 50 MB,
so that was out on day one.

What the free tiers give you:

Cloudflare R2, 10 GB, 5 GB per file, downloads free, card needed
Backblaze B2, 10 GB, 5 GB per file, free downloads to 30 GB a month, no card
Oracle Cloud, 20 GB, harder setup, card needed
Google Cloud, 5 GB, US regions only
AWS S3 and Azure, 5 GB, free trial only, not free forever
Cloudinary, about 25 GB, but a 100 MB file cap my videos fail

I went with R2, and the storage size had nothing to do with it.

Storage is the cheap part. Egress is what turns a free tier into a bill, and R2
charges nothing to serve files out. B2 is the close second and
doesn't even ask for a card, but its free egress stops at 30 GB a month.

If you are building anything that serves files to users, that one line is the
whole decision.

Numbers are from their free tiers this week. Check the pricing page before you
commit, these move.

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

## Humanizer pass

LinkedIn mode, voice-profile.md + reference/ai-tells.md. Score 8/10 -> 9/10.

Four fixes:

| Was | Tell | Now |
|---|---|---|
| "I compared 7 storage providers" | invented count. The source table has 7 rows, but one row is "AWS S3 / Azure", which is two services. The number is not defensible in the comments. | "every free storage tier I could find" |
| "what actually decided it" + "what the free tiers actually give you" | #7, "actually" is AI vocabulary and it appeared twice in a short post | second one cut |
| "Cloudinary, 25 GB" | #38 in reverse. The source says "about 25 GB", so dropping the hedge overstated it | "about 25 GB" restored |
| "charges nothing to serve files out, at any volume" | claim not in the source table, which only says "Free downloads" | "at any volume" cut |

Checked and clean: no em dashes, no hashtags, no emoji, no exclamation points, no
"It's not X, it's Y", no forced triads, no lesson ending, no parallel repetition.
The provider list is a stack list, which the tells reference explicitly does not
flag as a rule of three.

## Check before it ships

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
