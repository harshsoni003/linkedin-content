#!/usr/bin/env bash
# Package x-writer as a standalone skill you can upload to the Claude app
# (+ menu -> Skills -> Manage skills -> upload).
#
# The skill is useless without its data, so this bundles the style guide, the
# top posts, the replies, the voice profile and the full export into
# reference/, and rewrites the file paths so the skill finds them with no repo
# around it. Inside this repo the same files live in twitter/ and the skill
# reads them from there.
#
# Re-run this after `python twitter/build.py`, or the uploaded copy keeps
# serving the old numbers.
#
#   bash .claude/skills/x-writer/pack.sh
#   -> dist/x-writer.zip

set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../.." && pwd)"
BUILD="$(mktemp -d)"
trap 'rm -rf "$BUILD"' EXIT

mkdir -p "$BUILD/x-writer/reference"
cp "$ROOT/.claude/skills/x-writer/SKILL.md" "$BUILD/x-writer/SKILL.md"
cp "$ROOT/twitter/style-guide.md" \
   "$ROOT/twitter/top-posts.md" \
   "$ROOT/twitter/replies.md" \
   "$ROOT/voice-profile.md" \
   "$ROOT/twitter/data/posts.json" \
   "$BUILD/x-writer/reference/"

python3 -I - "$BUILD/x-writer/SKILL.md" <<'PY'
import io, sys
p = sys.argv[1]
t = io.open(p, encoding='utf-8').read()
t = t.replace(
    "| File | When | Why |",
    "Inside the `linkedin-content` repo these live in `twitter/`. Uploaded as a\n"
    "standalone skill they live in `reference/` next to this file. Check both.\n\n"
    "| File | When | Why |",
    1)
for old, new in (
    ("`twitter/style-guide.md`", "`style-guide.md`"),
    ("`twitter/top-posts.md`", "`top-posts.md`"),
    ("`twitter/data/posts.json`", "`posts.json`"),
    ("`twitter/replies.md`", "`replies.md`"),
    ("`twitter/archive/`", "`twitter/archive/` (repo only)"),
    ("cd twitter && python3", "python3"),
    ("io.open('data/posts.json'", "io.open('reference/posts.json'"),
):
    t = t.replace(old, new)
io.open(p, "w", encoding="utf-8").write(t)
PY

mkdir -p "$ROOT/dist"
rm -f "$ROOT/dist/x-writer.zip"
( cd "$BUILD" && zip -qr "$ROOT/dist/x-writer.zip" x-writer )

echo "dist/x-writer.zip  ($(du -h "$ROOT/dist/x-writer.zip" | cut -f1))"
unzip -l "$ROOT/dist/x-writer.zip" | tail -n +4 | head -n -2
