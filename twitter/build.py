"""Turn the raw X export into readable Markdown.

    python twitter/build.py            # uses twitter/data/adityaships-export.csv

Writes:
    twitter/top-posts.md        best 100 posts, ranked by likes
    twitter/archive/YYYY-MM.md  every original post, month by month
    twitter/replies.md          his short replies (how he talks in the comments)
    twitter/data/posts.json     clean data for scripts

A new export? Drop it over data/adityaships-export.csv and re-run.
"""
import csv, json, re, statistics, sys
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).parent
SRC = HERE / "data" / "adityaships-export.csv"
HANDLE = "@AdityaShips"
ISO = re.compile(r"^\d{4}-\d{2}-\d{2}T")
MONTHS = "January February March April May June July August September October November December".split()


def num(x):
    x = (x or "").strip().replace(",", "")
    if not x:
        return 0
    if x[-1] in "Kk":
        return int(float(x[:-1]) * 1000)
    if x[-1] in "Mm":
        return int(float(x[:-1]) * 1_000_000)
    return int(float(x))


def rows(path):
    """The export's quoting breaks on some quote-tweets: one post gets split
    across several CSV rows, or an unquoted comma shifts the columns. Repair both."""
    with open(path, encoding="utf-8-sig", newline="") as f:
        raw = list(csv.reader(f))[1:]
    posts = []
    for r in raw:
        if r and ISO.match(r[0]):
            if len(r) > 8:
                r = r[:2] + [",".join(r[2:-5])] + r[-5:]
            posts.append(r + [""] * (8 - len(r)))
            continue
        prev = posts[-1]
        if len(r) >= 6 and (r[-5].startswith("blob:") or r[-4].startswith("http") or r[-3].strip().isdigit()):
            prev[2] += "\n" + ",".join(r[:-5]).rstrip('"')
            prev[3:8] = r[-5:]
        else:
            prev[2] += "\n" + ",".join(r).rstrip('"')
    return posts


# In a quote tweet the export glues his words straight onto the quoted text:
# "damn, this is seriously terrifyingFinally launching Mascot Design".
JOIN = re.compile(r"(?<=[a-z?!.:;)’”\U0001F300-\U0001FAFF☀-➿️])(?=[A-Z“])")
OWN_QUOTE = re.compile(r"\s*x\.com/adityaships/st\S*\s*$", re.I)


def split_quote(text):
    own = bool(OWN_QUOTE.search(text))
    text = OWN_QUOTE.sub("", text)
    for m in JOIN.finditer(text):
        before = text[:m.start()]
        word = re.split(r"\s", before)[-1]
        letters = re.sub(r"[^A-Za-z]", "", word)
        # skip CamelCase names: NotchOwl, SaaS, iPhone, TikTok, ChatGPT...
        if letters and (not letters.islower() or len(letters) < 2) and word[-1:].isalpha():
            continue
        if len(before.strip()) < 2:
            continue
        return before.strip(), text[m.start():].strip(), own
    return text.strip(), "", own


def load(path=SRC):
    out = []
    for d, typ, content, vt, img, like, rt, rep in rows(path):
        text = content.rstrip('"').strip()
        own_text, quoted, own = split_quote(text)
        out.append({
            "date": d[:10],
            "time_utc": d[11:16],
            "type": typ.strip() or "text",
            "text": own_text,
            "quoted": quoted,
            "quotes_own_post": own,
            "media": [u for u in (vt + "," + img).split(",") if u.startswith("http")],
            "likes": num(like), "retweets": num(rt), "replies": num(rep),
        })
    return out


def is_original(p):
    """The export doesn't say which rows are replies. Short text-only rows with
    few likes are almost always replies under other people's posts."""
    return p["type"] != "text" or p["likes"] >= 15 or len(p["text"]) >= 100 or bool(p["quoted"])


def ist(p):
    h, m = map(int, p["time_utc"].split(":"))
    t = (h * 60 + m + 330) % 1440
    return f"{t // 60:02d}:{t % 60:02d} IST"


def quote(text):
    return "\n".join("> " + line if line.strip() else ">" for line in text.splitlines())


def block(p, rank=None):
    kind = p["type"]
    if p["quoted"] or p["quotes_own_post"]:
        kind += " · quote tweet"
    head = f"### {rank}. " if rank else "### "
    head += f"❤️ {p['likes']:,} · 🔁 {p['retweets']} · 💬 {p['replies']}  —  {p['date']} {ist(p)} · {kind}"
    parts = [head, "", quote(p["text"] or "(no text)")]
    if p["quoted"]:
        parts += ["", "<details><summary>Quoted post</summary>", "", quote(p["quoted"]), "", "</details>"]
    elif p["quotes_own_post"]:
        parts += ["", "*Quoting one of his own earlier posts.*"]
    if p["media"]:
        parts += ["", "Media: " + " · ".join(f"[{i + 1}]({u})" for i, u in enumerate(p["media"]))]
    return "\n".join(parts)


def main():
    src = Path(sys.argv[1]) if len(sys.argv) > 1 else SRC
    posts = load(src)
    orig = [p for p in posts if is_original(p)]
    reps = [p for p in posts if not is_original(p)]
    first, last = posts[-1]["date"], posts[0]["date"]
    med = statistics.median([p["likes"] for p in orig])

    (HERE / "data" / "posts.json").write_text(json.dumps(posts, ensure_ascii=False, indent=1), encoding="utf-8")

    top = sorted(orig, key=lambda p: -p["likes"])[:100]
    md = [f"# {HANDLE} — top 100 posts", "",
          f"Ranked by likes. {first} → {last}. {len(orig)} original posts, median {med:.0f} likes.", "",
          "Read these before writing. What he does is in [style-guide.md](style-guide.md); this is the proof.", "",
          "Quote tweets: his words are shown first, the post he quoted is folded under *Quoted post*.", "", "---", ""]
    for i, p in enumerate(top, 1):
        md += [block(p, i), "", "---", ""]
    (HERE / "top-posts.md").write_text("\n".join(md), encoding="utf-8")

    arc = HERE / "archive"
    arc.mkdir(exist_ok=True)
    by_month = defaultdict(list)
    for p in orig:
        by_month[p["date"][:7]].append(p)
    index = []
    for ym in sorted(by_month):
        ps = sorted(by_month[ym], key=lambda p: (p["date"], p["time_utc"]))
        y, m = ym.split("-")
        name = f"{MONTHS[int(m) - 1]} {y}"
        mm = statistics.median([p["likes"] for p in ps])
        best = max(ps, key=lambda p: p["likes"])
        md = [f"# {name} — {HANDLE}", "", f"{len(ps)} posts · median {mm:.0f} likes · oldest first", "", "---", ""]
        for p in ps:
            md += [block(p), "", "---", ""]
        (arc / f"{ym}.md").write_text("\n".join(md), encoding="utf-8")
        hook = best["text"].splitlines()[0][:70].replace("|", r"\|") if best["text"] else ""
        index.append(f"| [{name}]({ym}.md) | {len(ps)} | {mm:.0f} | {best['likes']:,} — \"{hook}\" |")
    (arc / "README.md").write_text("\n".join(
        ["# Archive — every original post by month", "", "| Month | Posts | Median likes | Best post |", "|---|---|---|---|"]
        + index) + "\n", encoding="utf-8")

    md = [f"# {HANDLE} — replies", "",
          f"{len(reps)} short replies he left under other people's posts. Useful for how he talks in comments, not for post ideas.", "",
          "| Date | ❤️ | Reply |", "|---|---|---|"]
    for p in reps:
        t = p["text"].replace("\n", " / ").replace("|", r"\|")
        md.append(f"| {p['date']} | {p['likes']} | {t} |")
    (HERE / "replies.md").write_text("\n".join(md) + "\n", encoding="utf-8")

    print(f"{len(posts)} rows → {len(orig)} posts, {len(reps)} replies, {len(by_month)} months")


if __name__ == "__main__":
    main()
