# Example: voice-firewall

**This entire page is a worked example.** Dana, Ledgerline, the client, and every number are fictional, written to show what good input and output look like. Your own run uses your real draft.

**The founder:** Dana Reyes runs Ledgerline, a six-person bookkeeping firm serving owner-led small businesses. She has run it for eleven years. Her voice profile came from the voice-match example (see voice-match-example.md). She had an AI tool draft a post from a real story, and it came back not sounding like her.

## What Dana sent

Her tool repeated the same contrast slogan twice and used a hyphen as a dash both times.

> Run voice-firewall on this draft. My voice profile is below it.
>
> DRAFT:
> Most business owners think bookkeeping is an expense. It's not an expense - it's an investment.
>
> Last month, a client asked us to cut our fee to save money. Instead of pushing back, we dove into his books.
>
> We found roughly $11,000 in savings. Duplicate subscriptions. Missed vendor credits. Unclaimed deductions.
>
> More visibility. More savings. More peace of mind.
>
> In today's fast-paced business world, you can't afford to fly blind.
>
> Bookkeeping isn't an expense - it's an investment.
>
> VOICE PROFILE: Dana Reyes
> Who I am: owner of a 6-person bookkeeping firm; I write for owner-led small businesses
>
> Openings: a specific client moment or a blunt instruction in line one ("A restaurant client swore he made money in March.")
> Rhythm: two or three plain sentences, then one short dry landing line ("Reconcile.")
> Paragraphs: one to three lines each, white space between every thought
> Punctuation: periods and commas; the samples do not use em dashes
> Words I use: "the books", "reconcile", "payroll", "current", exact dollar figures
> Words I never use: "hustle", "leverage", "game-changer", "journey"
> Signature moves: exact unrounded numbers ($6,200, $9,800); translating accounting into consequences ("other people's money with a deadline attached"); admitting the wobble before the lesson ("I rewrote the announcement email about ten times")
> Numbers: exact, never rounded; at least one real figure in every post
> Humor: dry, one beat per post, always in the last two lines
> Endings: one plain instruction or rule, never a motivational quote
> Never do: exclamation points, emojis, "Agree?", pretending a loss didn't sting
>
> Sounds exactly like me:
> 1. "Those deposits were other people's money with a deadline attached."
> 2. "Your bank balance is one number with no memory."
> 3. "Boring, I know. So is making payroll on time."

She also told it the real figures when asked: the total was $11,400, made up of $6,900 in duplicate software subscriptions, $3,200 in unclaimed vendor credits, and $1,300 in missed deductions. The client is a plumbing company.

## What voice-firewall returned

**1. Voice score: 3/10.** A 10 would sound unmistakably like Dana. This draft reads machine-written from the first line and the reader will decide that before "see more."

**2. Flagged lines, with rewrites in Dana's voice**

> "It's not an expense - it's an investment."

Tell: the "It's not X, it's Y" construction, repeated as a slogan instead of grounded in the client story.
Rewrite: cut the abstraction and open where Dana always opens, inside the client moment: "A plumbing client asked me to cut our fee last month. Money was tight and the books looked like a place to save."

> "Instead of pushing back, we dove into his books."

Tell: filler transition energy, and it skips the human beat.
Rewrite: "I asked for one week before he decided."

> "We found roughly $11,000 in savings. Duplicate subscriptions. Missed vendor credits. Unclaimed deductions."

Tell: a manufactured hedge on a number Dana knows exactly, followed by a bare triad. Her profile says exact unrounded figures.
Rewrite: "We went through everything. Duplicate software subscriptions, $6,900. Vendor credits nobody had claimed, another $3,200. His old setup had also missed $1,300 in deductions."

> "More visibility. More savings. More peace of mind."

Tell: parallel repetition, three lines on one skeleton. Humans escalate; models echo.
Rewrite, keeping only the escalation that matters: "$11,400. More than he pays us in a year."

> "In today's fast-paced business world, you can't afford to fly blind."

Tell: stock filler phrase. Says nothing Dana's numbers have not already said.
Rewrite: cut entirely.

> "Bookkeeping isn't an expense - it's an investment."

Tell: a conclusion that restates the opening and repeats the same contrast construction. Dana ends on short dry landing lines.
Rewrite: "He kept the fee." Then the landing line: "Cheap books are the expensive kind."

**3. Lines that went abstract:** "roughly $11,000 in savings" hid three exact figures Dana had. The rewrite above restores all three plus the total. No other line needed a number forced into it.

**4. Punctuation:** the original used a hyphen as a dash twice. Dana's profile shows periods and commas, so the clean version removes both.

**5. Contradictions:** none.

**6. Verdict: FAIL.** The score is under 7, the opening is generic, and the draft used an imprecise total until Dana supplied the exact figures. The clean version below fixes every flag.

**7. The clean draft**

> A plumbing client asked me to cut our fee last month.
>
> Money was tight and the books looked like a place to save. I asked for one week before he decided.
>
> We went through everything. Duplicate software subscriptions, $6,900. Vendor credits nobody had claimed, another $3,200. His old setup had also missed $1,300 in deductions.
>
> $11,400. More than he pays us in a year.
>
> He kept the fee.
>
> Cheap books are the expensive kind.
