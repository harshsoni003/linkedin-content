---
name: scoreboard
description: Calculates a user's median LinkedIn result and groups posts above or below it from pasted results or screenshots. Use when reviewing what worked before planning the next month.
---

# Scoreboard

Most people judge their posts against an industry benchmark or their single best post. Neither tells them what is normal for their own audience. Their median is a more useful personal baseline. This skill computes it from whatever results they actually have and compares every post against it, worst first.

**When to use:** the start of every content month, before drafting a new batch, or whenever you catch yourself guessing what works.
**Time it takes:** about 15 minutes once your results are ready. Gathering them can take longer.
**What you end with:** your own median, every post tiered against it, and the failures listed first so you finally look at them.

## What to give it

**1. Best: a pasted list of your recent posts with whatever numbers you have.** Aim for 20 or more posts. For each one: the first line of the post, plus any of comments, reactions, impressions, and the date. Whatever you have is enough; missing columns are fine. Good input looks like this:

> Use scoreboard. Here are my last 24 posts.
> Aug 12 | "I moved all 34 clients off hourly billing in January." | 74 comments, 312 reactions, 41,000 impressions
> Aug 9 | "The E-commerce Sales Tax Checklist is here." | 4 comments, 38 reactions, 2,100 impressions
> Aug 6 | "Your Shopify payout report is hiding four numbers." | 11 comments, 89 reactions, 6,400 impressions
> [21 more rows like this]

**2. Or: screenshots of your LinkedIn analytics.** Claude reads images. Capture any LinkedIn view that shows each post's first line and result numbers in the same image. For posts that matter most, also capture the post's "View analytics" screen when it is available. Make sure every number is readable.

**3. If you happen to have an export or spreadsheet, paste it in.** Accepted gladly, never required. Nothing in this skill needs anything beyond what is on your screen right now.

Dates are optional but valuable. One warning if you use screenshots: LinkedIn labels older posts "2w" or "1mo", and those labels are too coarse to place a post on a real day. Real dates support the rhythm analysis in Step 4; "2w" does not.

## The method

### Step 1. Build the post table

Turn whatever came in, pasted rows or screenshots, into one table: first line, comments, reactions, impressions, date. Read the count back to the user: "I can see 24 posts, 22 with comment counts, 19 with impressions." If a screenshot is unreadable, ask for a re-shot of that screen instead of guessing at the numbers.

### Step 2. Pick the ranking metric

Rank on comments wherever comment counts exist, because this collection focuses on conversation and comment-based lead posts. Report impressions alongside them. If the input has no comment counts, rank on impressions and say so plainly at the top of the output.

### Step 3. Compute the median

The median, never the mean. One viral post drags a mean so far up that half the library looks like failure against it; the median is the honest middle of what this audience actually gives this author. If fewer than 20 posts came in, compute it anyway and label it provisional: "This median rests on 14 posts. Treat it as a sketch until you have 20."

### Step 4. Tier every post against that median

| Tier | Rule |
|---|---|
| Hit | 5x the median or better |
| Solid | at or above the median |
| Flat | between a quarter of the median and the median |
| Dead | under a quarter of the median |

The bar for a Hit is deliberately high. You are not trying to land on your median; you are trying to clear it by 5x. Everything else in this pack is aimed at making Hits more frequent, and that starts with knowing exactly how rare they currently are.

### Step 5. Read the posting rhythm, only if real dates exist

With real dates, look at the pattern: posts per week, bursts, silences. Most accounts post in bursts and then go dark, and seeing the burst next to the numbers is usually the moment that habit dies. Do not rank days of the week unless a day has 5 or more posts behind it; small samples produce confident nonsense, and a wrong posting-day recommendation is expensive. If all you have is "2w"-style labels, skip this step entirely and say why, rather than building analysis on mush.

### Step 6. Lead with the failures

List every post worst first. People already know their best post; they have reread it a dozen times. The value is at the bottom of the table, in the posts they have quietly stopped thinking about.

## Output

1. The headline: your own median, with the metric named. "Your median is 12 comments per post, across 24 posts."
2. Tier counts, plus one line in this exact shape: "7 of 24 posts sat under a quarter of your own median."
3. Every post listed worst first: first line, its numbers, its tier.
4. Posting rhythm notes, if real dates allowed them.
5. Every caveat that applies, stated plainly: provisional median, missing metrics, thin days.

## What good looks like

Before reading the tiers, guess from memory which of your posts were Hits. Then compare. Wherever your guess and the table disagree, that gap is the whole point: memory tracks the posts you enjoyed writing, the table tracks the ones your audience actually moved for. A good scoreboard stings a little and names specific posts. If it reads like a compliment, something went wrong.

## Guardrails

- Never invent a number. If it was not in the input, it does not exist.
- Never compare the user to another account, a creator they admire, or an industry average. The median is theirs alone.
- Never rank any group of fewer than 5 posts without flagging it as thin.
- Fewer than 20 posts total: compute everything, label the median provisional, and say what it would take to firm it up.
- If screenshots and pasted numbers disagree for the same post, ask which is current instead of averaging them.

## Works even better with

- **pattern-audit** takes these tiers and finds which opening patterns produce your Hits and which to retire.
- **calendar** uses the rhythm findings when dating your next batch.
- **tracker** collects next month's results in a format this skill can read without rebuilding the post list.
