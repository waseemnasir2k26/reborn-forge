# INSTALL — Quick Update Guide

> Apne existing `reborn-history` repo ko v2.1.0 mein upgrade karne ka simplest path.

---

## TL;DR — 3 commands

```bash
# 1. Clone your existing repo (or cd into it)
cd reborn-history

# 2. Tag v1 as backup, create v2 branch
git tag v1.0.0-final && git push origin v1.0.0-final
git checkout -b v2.1.0-generalized

# 3. Copy all files from this package into the repo root
#    (overwrites README, SKILL, CHANGELOG; adds new files)
cp -r path/to/reborn-master-prompt-generator/* .

# 4. Move v1 master prompts to legacy folder
mkdir -p prompts/legacy
git mv prompts/MASTER-PROMPT-*.md prompts/legacy/ 2>/dev/null
git mv MASTER-PROMPT-*.md prompts/legacy/ 2>/dev/null

# 5. Commit and push
git add .
git commit -m "feat(v2.1.0): niche-agnostic master prompt generator with SCRIPT WRITING SYSTEM"
git tag v2.1.0
git push origin v2.1.0-generalized --tags

# 6. Open PR or merge to main
git checkout main
git merge v2.1.0-generalized
git push origin main
```

---

## What this does

- Backs up v1 as `v1.0.0-final` tag (anyone can `git checkout v1.0.0-final` to restore)
- Adds v2.1.0 files: `META-PROMPT.md`, `agents/`, `templates/`, new examples
- Moves the 4 original master prompts into `prompts/legacy/` as documented examples
- Tags the new release as `v2.1.0`
- Pushes everything to GitHub

---

## File-level changes

| Action | File | Notes |
| --- | --- | --- |
| ADD | `META-PROMPT.md` | The generator (paste-and-use). New top-level entry point. |
| ADD | `MIGRATION-GUIDE.md` | Detailed v1→v2 migration reasoning |
| ADD | `INSTALL.md` | This file |
| ADD | `agents/01-niche-intelligence.md` | Niche profiling agent |
| ADD | `agents/02-video-analyzer.md` | Video forensic analyzer |
| ADD | `agents/03-pattern-engine.md` | Formula extractor |
| ADD | `agents/04-prompt-architect.md` | 9-decision architect (includes Script System) |
| ADD | `agents/05-output-compiler.md` | Final assembler + quality gates |
| ADD | `templates/MASTER-PROMPT-TEMPLATE.md` | Canonical 34-section skeleton |
| ADD | `examples/input-mansion-restoration.md` | Non-history example INPUT |
| ADD | `examples/input-luxury-watch-restoration.md` | Non-history example INPUT |
| ADD | `examples/sample-output-grimdark-history.md` | Real generator output (3,480 words) |
| OVERWRITE | `README.md` | Rewritten for niche-agnostic workflow |
| OVERWRITE | `SKILL.md` | Bumped to v2.1.0, 34-section structure |
| OVERWRITE | `CHANGELOG.md` | v2.0.0 + v2.1.0 entries added |
| MOVE | `prompts/MASTER-PROMPT-*.md` → `prompts/legacy/` | Preserved as examples |
| KEEP | `LICENSE` | MIT, unchanged |
| KEEP | `CONTRIBUTING.md` | Unchanged (still accurate) |
| KEEP | `tools/_build.py` | Markdown→PDF builder still works |
| KEEP | `reference/*` | Original Tim Reborn agent outputs preserved as worked example |
| KEEP | `examples/input-*.md` (history ones) | Bubonic Plague, Pompeii, Baghdad, Great Fire — keep |

---

## After migration

Update GitHub repo metadata:

- **Description:** `Niche-agnostic master-prompt generator for AI video. Paste a NICHE and a YOUTUBE_URL, get back a complete master prompt for that niche. 5-agent pipeline + 34-section structure with built-in SCRIPT WRITING SYSTEM. English / Hindi / any locale.`

- **Topics to add:** `meta-prompt`, `prompt-generator`, `master-prompt`, `ai-video-generator`, `script-writing`

- **Repo rename (optional):** `reborn-history` → `reborn-master-prompt-generator` or `reborn-prompt-architect`. If you keep the original name, just update the README headline.

---

## Test before you ship

After merging, sanity-check:

1. Open `META-PROMPT.md` — copy entire file
2. Paste into Claude / GPT-5 / Gemini
3. Append at the bottom:
   ```
   NICHE: ancient ruins exploration with cinematic reconstruction overlays
   YOUTUBE_URL: <pick any reference video>
   TARGET_TOOL: VEO3
   DURATION: longform
   LANGUAGE: English
   ```
4. Submit
5. Verify the output is a complete master prompt with all 34 sections including SCRIPT WRITING SYSTEM

If the output is missing the script section or any other gate fails, file an issue — the meta-prompt design needs a tweak.

---

## Rollback

If anything breaks:

```bash
git checkout v1.0.0-final
```

You're back to v1. The v2 branch and tag remain available; you can fix and re-merge later.
