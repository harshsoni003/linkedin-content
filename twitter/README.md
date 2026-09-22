# Twitter / X

My X writing workspace. The reference account is **[@AdityaShips](https://x.com/AdityaShips)**: short, casual build-in-public posts about real money and real moments.

## What's here

```
style-guide.md        START HERE: how he writes, the 9 post types that work, what flops
top-posts.md          his 100 best posts, ranked by likes, full text
archive/              every post he made, one file per month
replies.md            his short replies (how he talks in the comments)

drafts/               my X posts being written
published/            my X posts that went out, with results

data/                 raw CSV export + clean posts.json
build.py              rebuilds top-posts, archive, replies from the CSV
```

## Writing a post

Ask Claude: **"write a Twitter post about [what happened]"**. It reads `style-guide.md` and `top-posts.md` first, picks the post type that fits, and writes it in that style using my facts.

Or by hand:

1. Pick the post type in [style-guide.md](style-guide.md) that matches what happened
2. Look at 2–3 of his real examples of that type in [top-posts.md](top-posts.md)
3. Draft in `drafts/` using [drafts/_template.md](drafts/_template.md)
4. Run `/humanizer` on it, then the checklist at the bottom of the style guide
5. Post, then move it to `published/` with the numbers after 48 hours

## Rules

- His style, **my facts**. Never borrow his numbers or his story
- Missing numbers stay `[NUMBER: what goes here]` until I fill them
- Under 280 characters unless it's a launch or an income report
- No hashtags

## New export

Save the new CSV over `data/adityaships-export.csv`, then:

```
python twitter/build.py
```
