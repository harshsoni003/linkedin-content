# Install

Custom skills are currently available on Claude Free, Pro, Max, Team, and Enterprise accounts when code execution and file creation are enabled. A Team or Enterprise owner may limit personal skill uploads.

Start with voice-match, post-writer, and voice-firewall. Add the other eight only when you want their planning and review jobs.

## Claude on the web or desktop

The complete download already contains ready-to-upload ZIPs. Leave them zipped.

1. Sign in to Claude.
2. Open **Settings**, then **Capabilities**.
3. Turn on **Code execution and file creation**.
4. Open **Customize**, then **Skills**.
5. Click **+**, then **Create skill**, then **Upload a skill**.
6. Upload install-first/voice-match.zip.
7. Repeat for post-writer.zip and voice-firewall.zip.
8. Open a new chat and type: Use voice-match.

If Claude asks for writing samples, the skill is working.

Each upload contains one skill in the structure Claude expects:

    voice-match.zip
    └── voice-match/
        └── SKILL.md

Custom skills you upload are private to your account unless an organization owner shares them.

## Claude Code

From the unzipped complete download, run:

    mkdir -p ~/.claude/skills
    cp -R skills/* ~/.claude/skills/
    ls ~/.claude/skills/voice-match/SKILL.md

If the last command shows the file, the skills are in Claude Code's personal skills folder. If you created the top-level skills folder while Claude Code was already open, restart Claude Code once so it can watch the new folder.

## Common questions

**Do I need paid Claude?** No. Anthropic currently lists custom skills for Free, Pro, Max, Team, and Enterprise plans. Code execution and file creation must be enabled.

**Why is the upload option missing?** Check Code execution and file creation first. On Team or Enterprise, the account owner may have disabled personal skill uploads or removed the permission from your role.

**Do I have to install all eleven?** No. Start with voice-match, post-writer, and voice-firewall.

Installed? Open START-HERE.md.
