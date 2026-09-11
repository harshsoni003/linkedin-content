---
name: tracker
description: Maintains one table of drafted, reviewed, ready, and dated LinkedIn posts, with required editing and calendar checks. Use when managing a batch or closing a content month.
---

# Tracker

Content plans rarely fail at the writing. They fail between steps: posts get written and never checked, or checked and never dated, and a month later there is a folder of finished work and an empty feed. This skill keeps one plain table with four statuses, enforces two checks, and turns the month's published posts into a report for next month.

**When to use:** when a new batch starts, every time a post changes status, and at the end of the month.
**Time it takes:** about 2 minutes per update, 10 for the month-end report.
**What you end with:** one table that always shows where every post stands, and a month-end report ready to hand straight to scoreboard.

## What to give it

**1. First run: your posts in flight, with where each one honestly stands.** Good input looks like this:

> Use tracker. Set up my table.
> 1. "I moved all 34 clients off hourly billing in January." Written, not checked.
> 2. "The E-commerce Sales Tax Checklist" (gated). Passed voice-firewall yesterday.
> 3. "Your Shopify payout report is hiding four numbers." Half written.

**2. Every run after that: the current table.** Keep the whole month in one conversation and the table is already there. If you start a fresh conversation, paste the last table Claude printed; a new conversation cannot see the old one, so the table you paste is the record. Copy the table into your notes at the end of each session, or ask for it as a downloadable file.

**3. Status changes as plain sentences.** "Post 1 passed voice-firewall." "Calendar gave post 2 September 9." "Move post 3 to Ready." Claude applies the checks and reprints the table.

## The method

### Step 1. Hold exactly four statuses

| Status | Means | Entry requirement |
|---|---|---|
| Drafted | Written, not checked | Has a full body |
| In review | Being checked now | Nothing cleared yet |
| Ready | Cleared to publish | Passed voice-firewall |
| Dated | Has a publish date | Has a slot from calendar |

Four statuses, not seven. Every extra status is a place work goes to sit. If a post does not fit one, the post needs a decision.

### Step 2. Enforce the two checks, out loud

**Nothing reaches Ready without a voice-firewall pass.** Not "we will check it later." The check is the status change. If voice-firewall is not installed, a real editing pass, read in full and recorded here by name and date, counts. The requirement exists so nothing unchecked is marked Ready.

**Nothing reaches Dated without a slot from calendar.** A date somebody picked by feel is how two gated posts end up on consecutive days.

When a move skips a check, refuse it and name exactly what is missing: "Refused. Post 3 has no voice-firewall pass on record. Run the check, tell me it passed, and I will move it."

### Step 3. Reprint the table after every change

The full table, every time, in this shape:

| # | Post (first line) | Comment ask | Status | Editing check | Date |
|---|---|---|---|---|---|

Never answer only "updated as requested." The reprinted table is what the user saves, so it must always be complete and current.

### Step 4. Raise two warnings without being asked

**Everything pooling in Drafted.** The writing is happening and the checking is not, which almost always means voice-firewall is being skipped. Say so the moment the pattern shows.

**Everything in Ready, nothing Dated.** Posts are finished and not going out. Say so the moment it appears, not at month end.

### Step 5. Close the month

When the user says the month is done, produce the report:

1. Posts published against posts planned.
2. For each published post: first line, gated or not, and its numbers, asking for any that are missing.
3. Which hook families went out this month.
4. A paste-ready block of every published post with its numbers, formatted as scoreboard input.
5. One line: the thing next month should stop doing, based on what this table showed.

### Step 6. Prepare next month

The paste-ready block is the point of the whole exercise. Published posts and their numbers go into next month's scoreboard, the median moves, pattern-audit gets a bigger sample, and every skill in the pack gets sharper. A ghostwriter starts over every month. This compounds instead.

## Output

1. The current table after every change.
2. Any refused move, with the missing check named and the exact step that clears it.
3. Either warning, raised the moment it appears.
4. At month end: the report, ending in the paste-ready scoreboard block.

## What good looks like

Ask for the table cold, mid-month. If the table alone tells you what to do next, such as check post 4 or get a date for post 6, it is working. If every post has held the same status for two weeks, the table has made a stalled process visible.

## Guardrails

- Never move a post to Ready without a recorded voice-firewall pass, or a named, dated human editing pass in its place.
- Never move a post to Dated without a slot from calendar.
- Never add a fifth status, whatever it is called.
- Never close a month without producing the paste-ready scoreboard block.
- The tracker records and refuses; it never rewrites a post, invents a date, or fills in numbers the user did not give.

## Works even better with

- **voice-firewall** provides the editing check required for Ready.
- **calendar** provides the date required for Dated.
- **scoreboard** receives the month-end block and turns this month's results into next month's bar.
