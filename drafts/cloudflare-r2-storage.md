# Cloudflare R2 storage switch

**Goal:** gain relevant followers — share something useful, no pitch
**From:** raw-material (log it: the 50 MB wall on a 118 MB video)
**Hook family:** bare number
**Voice:** Harsh Soni profile applied
**Status:** Drafted — one claim to confirm

---

## The post

My upload failed at 50 MB.

The video was 118.

Here's where it ended up.

Supabase gives you 1 GB of storage and caps a single file at 50 MB. Fine for
images, useless for video.

So I went looking. What I found:

Cloudflare R2, 10 GB free, 5 GB per file, downloads free
Backblaze B2, 10 GB free, 5 GB per file, no card needed
Oracle Cloud, 20 GB free, harder setup
Cloudinary, caps files at 100 MB, out before I started

I moved to R2. 10 GB holds about 85 videos at my size, and downloads cost
nothing, which is the part most people miss until the bill shows up.

Numbers are from their free tiers this week. Check the pricing page before you
commit, these move.

---

## Fill in before posting

- [ ] **"I moved to R2" is written as done.** If you have only decided and not
      migrated yet, change it to "I'm moving to R2". Your own README rule is
      never to publish a claim you can't defend in the comments, and someone
      will ask how the migration went.
- [ ] Optional: how long the switch took. "Took me an afternoon" turns a
      recommendation into evidence. Only if it's true.

## Alternate openings

**A — corrective**
> Free storage tiers are not the number that matters.
> The per-file cap is.

*Widest reach, most argument in the comments. Least about you, so it wins
attention and builds less trust.*

**B — first person**
> I picked Supabase for storage without reading the per-file limit.
> That cost me an afternoon.

*Most human of the three, opens on your own mistake. Needs the afternoon claim
to be true.*

**C — this X / your X**
> Your storage bill is not the number that will bite you.
> Egress is.

*Sharpest for an engineering audience, and the one most likely to be reshared.
Narrower, since it assumes the reader already pays for storage.*

## The call

Run the main one. The two numbers in the first two lines do the whole job, and
it opens on a wall you actually hit rather than on an opinion. It also fixes the
gap your voice profile flags hardest: this is the first post of yours carrying
real figures on nearly every line.

## Voice notes

Applied from the profile:
- Opens on the build, no run-up
- Options listed, not described, same move as "auth, database, payments,
  agents, deploy"
- Short landing lines against longer explaining ones
- No em dashes, no exclamation points, no "journey", no "excited to announce"
- Ends on the practical note, not a lesson

The caveat line at the end is deliberate. Free tiers change, and your README
rule is to never publish a number you can't defend. That line makes every
figure above it defensible.

## Check before it ships

- [x] Every number came from the material I was given
- [x] Opening doesn't give away the ending — line 2 sets up the problem,
      never names the answer
- [x] No "It's not X, it's Y"
- [x] No two consecutive lines on the same skeleton
- [x] Sentence lengths vary
- [x] Ending doesn't restate the opening
- [x] No hashtags, no emoji
- [ ] "I moved to R2" confirmed as past tense
- [ ] Read out loud once
