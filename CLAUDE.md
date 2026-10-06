# Content workspace

Two channels live here: LinkedIn (repo root) and Twitter / X (`twitter/`).

## Twitter / X posts

When asked for a Twitter, X, or tweet post, **read the whole `twitter/`
folder every single time**. Not from memory, not from earlier in the
conversation. Open the files. This applies to one-line posts, replies and
bio edits as much as to full posts.

1. **Every time, before writing anything:**
   - `twitter/style-guide.md` in full
   - `twitter/top-posts.md` for 2–3 real examples of the post type that fits
   - `twitter/data/posts.json` queried for the actual topic at hand, so the
     recommendation rests on his real numbers rather than remembered ones
   - `twitter/replies.md` when the task is a reply or a comment
   - `twitter/archive/` when the post is seasonal, a festival, a national day,
     or anything where it matters whether he posts that kind of thing at all

   If the data has no example of the kind of post being asked for, **say so**
   rather than guessing. A finding like "330 posts, zero gym posts" is more
   useful than a confident post with nothing behind it.
2. Write in @AdityaShips' style: short (under 280 characters unless it's a launch or income report), casual, one idea, exact numbers, blank line between beats, 0–2 emoji, no hashtags.
3. Use only the user's own facts. Never reuse Aditya's numbers, products, or life details. Missing facts go in as `[NUMBER: what goes here]`.
4. Give the post, 3 alternate first lines, and name which of the 9 post types it is.
5. Save drafts to `twitter/drafts/` only when asked.
6. When the user asks to humanize or clean up a post, use the `humanizer` skill (in this repo at `.claude/skills/humanizer/SKILL.md`). It picks X or LinkedIn mode and loads the voice files here on its own.

## LinkedIn posts

Use `voice-profile.md`, `reference/`, and the skills described in `skills/README.md`. Don't apply the Twitter style guide to LinkedIn.
