---
name: pattern-audit
description: Groups LinkedIn posts by opening pattern, shows which patterns produced strong results, and names one to use more. Use after scoreboard or when reviewing why posts stopped working.
---

# Pattern audit

Most people improve their content by adding: more posts, new formats, another hour of writing. This skill improves it by subtracting, which is faster and costs nothing. Your post history already contains the answer to "what should I write more of?" You have been running experiments for months without reading the results. This audit reads them, names the opening patterns that are quietly wasting your weeks, and hands you the one pattern that actually produces your winners.

**When to use:** right after scoreboard, before drafting a new batch, or the moment you notice your posts stopped working and you cannot say why.
**Time it takes:** about 5 minutes if you have your scoreboard output, 15 if you start from raw posts.
**What you end with:** a ranked table of your opening patterns, a short retire list with your own posts as the evidence, and the single pattern to use more.

## What to give it

**1. Best: your scoreboard output.** The tiers and your median are the fuel. Paste the whole thing. Good input looks like this:

> Run pattern-audit on my scoreboard below.
> Median: 12 comments across 24 posts.
> HIT: "I moved all 34 clients off hourly billing in January." 74 comments
> DEAD: "The E-commerce Sales Tax Checklist is here." 4 comments
> [the rest of the tiered list]

**2. No scoreboard? Paste your posts with numbers instead.** The first line of each post plus its comment count is the minimum. This skill will compute the median and tiers itself before auditing, using the same rules scoreboard uses: median never mean, a Hit is 5x your median or better.

Either way, make sure the first line of every post is included word for word. The audit sorts on first lines, and a paraphrased first line gets sorted into the wrong group.

## The method

### Step 1. Establish the tiers

If tiers came in from scoreboard, use them. If raw posts came in, compute the median (median, never mean; one viral post wrecks a mean) and tier every post: Hit is 5x the median or better, Solid at or above, Flat between a quarter and the median, Dead under a quarter.

### Step 2. Sort every post by hook family

Read only the first line of each post and sort into these families:

| Family | Test |
|---|---|
| First person | Opens with a thing the author did. "I built", "I spent", "I stopped", "We fired" |
| Bare product title | Names the thing they made, no verb about them. "The 2026 pricing guide is here" |
| Bare number first | Opens on a number with no verb. "34 clients." |
| This X / Your X | Speaks straight at something the reader owns. "Your books are lying to you" |
| Corrective | Opens by contradicting a common belief |
| Tool as subject | The tool does the acting. "Claude can now..." |
| Unfinished story | Opens inside a moment with the ending withheld. "The email came in at 11pm." |
| Other | Anything else |

### Step 3. Sort by format

Same posts, second lens: lead post (offers something in exchange for a comment), how-to, contrarian take, story, list, opinion, other.

### Step 4. Rank on hit rate, not median

This is the part everyone gets wrong.

For each family and each format, report: count, median comments, best single result, and **hit rate**, meaning the share of that group's posts that became big winners, the ones that cleared your Hit tier.

Then rank on hit rate.

Here is why. Medians across hook families usually sit within a few percent of each other, which makes it look like the pattern does not matter. It does. You are not trying to land on your median; you are trying to clear it by 5x. A family can have an ordinary median and still be twice as likely to produce a Hit, and that family is the one to bet on.

### Step 5. Name the retirements

For each family or format being retired, give three things:

1. The name of the pattern
2. The count and the number that justifies the call
3. One verbatim example from the user's own posts, quoted exactly, so they recognize their own writing on the list

A group with fewer than 4 posts is not evidence. Say so and leave it unranked rather than retiring it on a hunch.

### Step 6. Run the weak-topic trap check

A family can look dead because it was only ever used on weak topics, or only during one bad stretch. Before retiring any pattern, check whether its posts share a topic or a time period. If every post in a family went out in one bad fortnight, the fortnight is the problem, not the family. Put it on probation, one more attempt on a strong topic, instead of the retire list.

### Step 7. End on the one to use more

Finish with the single family that has the best hit rate on a real sample, and why. One recommendation, not a ranked list of seven. An audit that ends with seven suggestions gets ignored; an audit that ends with one gets used this week.

## Output

1. Hook family table: family, count, median, best, hit rate with its sample size, sorted by hit rate.
2. Format table, same columns.
3. The retire list: each pattern named, the number behind the call, and one verbatim example.
4. Any pattern on probation from the trap check, with what would settle it.
5. One closing line: the family to use more, and why.
6. Any group too thin to judge, listed rather than ranked.

## What good looks like

Read the retire list out loud. If you catch yourself defending one of the patterns on it, "but that one is my style", good: the audit just found the pattern you were protecting by feel instead of by results. If the retire list came back empty and everything looks fine, the sample was probably too thin to judge, and the output should have said exactly that.

## Guardrails

- Never retire a pattern on fewer than 4 posts.
- Never present a hit rate without its sample size right next to it. "50% hit rate" on 2 posts is a coin flip, not a finding.
- Quote the user's example posts exactly. A paraphrased example breaks the recognition that makes the retire list land.
- If the whole library is one family, say that instead of ranking it, and name the two families to test next so future audits have something to compare.
- Never judge a post's body or topic quality here. This audit reads first lines and formats only; the writing itself is another skill's job.

## Works even better with

- **scoreboard** produces the tiers this audit runs on, and keeps the median honest month over month.
- **hook-writer** writes 10 new openings in your winning family the moment this audit names it.
- **post-brief** locks that winning family into the plan before you draft.
