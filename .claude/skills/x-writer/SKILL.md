---
name: x-writer
version: 1.0.0
description: |
  Writes X / Twitter posts and replies in Harsh's voice, using the @AdityaShips
  style data in twitter/. Use for any tweet, X post, thread, reply, comment,
  quote tweet or bio edit, including one-liners. Picks the post type from the 9
  that work, checks the request against 721 real posts before writing, and
  reports honestly when the data has no example of what is being asked for.
  Never invents a number. Runs the humanizer before delivering.
license: MIT
compatibility: any-agent
allowed-tools:
  - Read
  - Write
  - Edit
  - Grep
  - Glob
  - Bash
  - Skill
---

# X writer

Every X post in this workspace is written from evidence, not from memory. The
`twitter/` folder holds a real export of 721 posts and replies with their like
counts. That data answers most questions about what to write before a single
line is drafted: which opening pulls, which ask flops, whether he has ever
posted this kind of thing at all.

The failure mode this skill exists to prevent: writing from what you remember
about his voice instead of opening the files. It reads the same, it is wrong in
small ways, and the small ways are the ones that cost likes.

**Use for:** posts, replies, quote tweets, bio edits, one-liners, grammar fixes
on a draft he wrote himself.
**What you end with:** the post, alternate first lines, which of the 9 types it
is, the character count, and the real numbers behind the recommendation.

---

## Step 0: read the folder. Every time.

Not from memory. Not from earlier in the conversation. Open the files.

| File | When | Why |
|---|---|---|
| `twitter/style-guide.md` | **Always, in full** | The 9 types, the flop table, voice rules, posting times |
| `twitter/top-posts.md` | **Always** | 2–3 real examples of the type that fits |
| `twitter/data/posts.json` | **Always, queried for the actual topic** | Whether he has ever posted this, and how it did |
| `twitter/replies.md` | Replies and comments | His short-reply register |
| `twitter/archive/` | Seasonal, festival, national day posts | What he did last time |
| `voice-profile.md` | Always | Harsh's own voice, which outranks the style guide |

**If the data has no example of what is being asked for, say so.** Do not guess
and do not pad. "Zero posts about X in 721 records" is a finding, and it is more
useful than a confident post built on nothing. Then build from the nearest real
neighbour and name which one you used.

### Querying the data

```bash
cd twitter && python3 -I - <<'PY'
import json, io, re, statistics as st
d = json.load(io.open('data/posts.json', encoding='utf-8'))
# The export does not mark replies. This is build.py's own heuristic:
def is_original(p):
    return p["type"]!="text" or p["likes"]>=15 or len(p["text"])>=100 or bool(p["quoted"])
orig=[r for r in d if is_original(r)]        # 330 posts, median 64
for r in sorted(orig, key=lambda r:-(r.get('likes') or 0)):
    t=(r.get('text') or '')
    if re.search(r'YOUR_TOPIC_REGEX', t, re.I):
        print('❤️',r['likes'],'💬',r['replies'],'|',t.strip()[:160].replace('\n',' / '))
PY
```

Fields: `date, time_utc, type, text, quoted, quotes_own_post, media, likes, retweets, replies`.
`type` is `text` / `image` / `video`, never `reply` — use the heuristic above or
the counts will be wrong (all 721 records median 4, which is replies dragging it
down).

---

## Writing a post

1. **Find the moment, not the topic.** A topic invites invention. If what you
   have is a topic, ask for the moment or the number.
2. **Pick the type** from the 9 in the style guide. Name it in the output.
3. **Pull 2–3 real examples** of that type from `top-posts.md`. Match the shape,
   not the words.
4. **Query `posts.json` for the actual subject.** Launches, prices, gym, SEO,
   Product Hunt, feedback asks, a named person — check before writing, report
   what you found.
5. **Draft.** One idea. Blank line between beats. Under 280 unless it is a
   launch or an income report.
6. **Run the humanizer** (`.claude/skills/humanizer/SKILL.md`), X mode.
7. **Deliver** in the format below.

## Writing a reply

Replies are a different register and have their own file. Read `replies.md`.

- 2–5 words is normal. His best short replies: "Its over for Lovable" (12),
  "We are so back" (6), "Bruhhhh i needed this thanks" (7), "Finally 😭" (9)
- For someone else's win: "Congratulations bro" (used 4 times), "lfgg bhai
  congratulations", "always cooking", "W", "Damn this is crazy", "Goat"
- Warm, lowercase, `bro` / `bhai` / `buddy` / `man`, 🫶 and 😭
- **A reply gets 0–4 likes. That is normal and not a failure.** If reach is the
  goal, quote tweet instead: his #1 post ever (1,600 ❤️) was a 7-word quote
  tweet reaction.

---

## What the data already settled

Do not re-derive these. Do re-check them if the export is rebuilt.

| Thing | Finding |
|---|---|
| Overall | 330 original posts, **median 64** likes |
| Format | image **75** · text **48** · video **42** |
| Length | under 280 → **66–71** · over 280 → **38** |
| A link or domain in the body | 14 posts, median **45.5**, against **67** with none |
| Two or more links | 6 posts, median **44.5** (so the second link is nearly free) |
| An @mention in the post | 4 posts, median **62**. No boost |
| Starting a post with `@` | X shows it only to mutual followers. Never do it |
| Feedback asks | 6 posts: **0, 1, 3, 5, 5, 7**. His most reliable way to be ignored |
| Discount offers | **Zero** in 721 records. No precedent at all |
| "DM me" | 2, both replies, 1 ❤️ and 0 ❤️ |
| Product Hunt | 1 post, 70 ❤️ / 16 💬, link kept out of the body ("Link below") |
| "Introducing X 🎉" | His **weakest** launch hook: 474, against 962 / 721 / 654 for surprise-specific openers |
| Highest replies ever | **459**, on a pain question with no incentive attached |

**Topic medians:** family + money 142 · money 105 · Day N series 97 · AI tools 72
· exams 70 · launches 69 · SEO 64.

---

## What flops

From the style guide's own table, plus what the queries confirmed:

- "Btw I built this with my tool" plugs → **7**
- Asking for feedback → **5**
- Long explanations → **4**
- "Coming soon" with nothing to show → **0**
- A bare reminder to go buy ("In case you haven't upvoted yet") → **3**
- Announcing that someone copied someone → **19**

Plugs and explanations belong in a reply under a post that is already working,
never in a new post.

---

## Never

- **Never invent a number.** Not a duration, not a count, not a price, not a
  percentage. Missing ones stay `[NUMBER: what goes here]`. A blank is safe; an
  invented figure that gets challenged under his own post is not. This rule has
  been broken in practice — a "four second test" that the source never said —
  so treat every number in a draft as needing a source in the user's own words
  or a file on disk.
- Never borrow @AdityaShips' numbers, products, mom, exams or revenue. Style
  only.
- Never use hashtags.
- Never "excited to announce", "leverage", "game-changer", "thrilled".
- Never a thread with 1/ 2/ 3/.
- Never explain the screenshot or the joke.
- Never claim a feature from a spec field that is empty. Check the file.
- Never write an accusation about a named person from an inference. Read what
  they actually published first.

---

## What to deliver

```
[Which files were read, one line]

[Any honest finding first, if the data had no example or contradicts the ask]

## Option 1 — [post type]
[the post, ready to paste]
[character count]

## Option 2 — [post type]
...

**3 alternate first lines:**
- ...

[Any [NUMBER: ...] to fill, the format to attach, and one line naming the pick
and why, with the number behind it]
```

Three options is the default. One is fine for a grammar fix or a reply.

Lead with the finding when the data disagrees with the request. He would rather
know that discount posts have no precedent than get a polished discount post.
But if he reaffirms the ask after hearing it, write it properly and stop
arguing — state the concern once, then do the work.
