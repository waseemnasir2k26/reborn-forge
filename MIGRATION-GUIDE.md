# MIGRATION GUIDE — reborn-history v1 → v2

> v1 was a single-niche skill (grimdark cinematic AI history). v2 is a niche-agnostic master-prompt generator. This guide shows you exactly what to add, move, and update in your existing repo.

---

## Summary of changes

| Layer | v1 (history-only) | v2 (generalized) |
| --- | --- | --- |
| Input | Topic + era + geography | NICHE + YOUTUBE_URL |
| Output | Script + image prompts + scene JSONs | Master prompt (which then produces those) |
| Master prompts | 4 hardcoded (English / Hindi long / short / grimdark) | Generated on demand for any niche |
| Agents | 5-agent pipeline ran once during repo creation | 5-agent pipeline runs every time a user generates a prompt |
| Reference | Hardcoded to Tim Reborn channel | Any user-provided YouTube URL |

The v1 master prompts are not deleted — they are preserved as **examples** of what v2 produces. Anyone can still paste them and use them directly.

---

## Step-by-step migration

### 1. Add new top-level files

```
+ META-PROMPT.md                      ← THE generator (new entrypoint)
+ MIGRATION-GUIDE.md                  ← this file
~ README.md                           ← rewrite (see below)
~ SKILL.md                            ← rewrite (see below)
~ CHANGELOG.md                        ← add v2.0.0 entry
```

### 2. Add new directories

```
+ agents/
  + 01-niche-intelligence.md
  + 02-video-analyzer.md
  + 03-pattern-engine.md
  + 04-prompt-architect.md
  + 05-output-compiler.md

+ templates/
  + MASTER-PROMPT-TEMPLATE.md
```

### 3. Reorganize existing content

```
prompts/                              ← rename internally; treat as legacy examples
  → prompts/legacy/
    MASTER-PROMPT-REBORN-ENGLISH.md   (was prompts/MASTER-PROMPT-REBORN-ENGLISH.md)
    MASTER-PROMPT-REBORN-HINDI.md
    MASTER-PROMPT-LONG-HINDI.md
    MASTER-PROMPT-SHORT-HINDI.md

reference/                            ← keep as-is (these are the agent outputs for the history niche, useful as a worked example of what the agents produce)

examples/                             ← keep, expand with new niches
  input-bubonic-plague.md             (existing)
  input-fall-of-baghdad.md            (existing)
  input-pompeii.md                    (existing)
  input-great-fire-london.md          (existing)
  + input-mansion-restoration.md      (new — non-history example)
  + input-luxury-watch-restoration.md (new — non-history example)
```

### 4. Update CHANGELOG.md

```markdown
## [2.0.0] — 2026-XX-XX

### Added
- `META-PROMPT.md` — niche-agnostic master-prompt generator (paste-and-use)
- `agents/` — 5 modular agent prompts (niche intelligence, video analyzer, pattern engine, prompt architect, output compiler)
- `templates/MASTER-PROMPT-TEMPLATE.md` — canonical 33-section output skeleton
- `MIGRATION-GUIDE.md`

### Changed
- `README.md` rewritten for niche-agnostic workflow
- `SKILL.md` updated (`name: reborn-master-prompt-generator`, `version: 2.0.0`)
- `prompts/*.md` moved to `prompts/legacy/` and reframed as examples
- Repo description updated on GitHub

### Preserved
- All v1 master prompts (history-niche) work standalone — backward compatible
- `reference/` agent outputs preserved as a worked example of the generator's internal output for the history niche

### Backward compatibility
- Anyone using v1 master prompts directly: no change required
- Anyone using the 4 reference master prompts as drop-in templates: no change required
```

### 5. Update GitHub repo metadata

- **Description:** `Niche-agnostic master-prompt generator for AI video. Paste a NICHE and a YOUTUBE_URL, get back a complete master prompt for that niche. 5-agent reverse-engineering pipeline. English / Hindi / any locale. VEO 3.1 / Kling 2.5 / Runway / Sora.`
- **Topics:** add `meta-prompt`, `prompt-generator`, `master-prompt`, `ai-video-generator`. Keep existing topics.
- **Optional rename:** consider renaming the repo from `reborn-history` to `reborn-master-prompt-generator` or `reborn-prompt-generator`. If you keep the original name, update the README headline to clarify scope.

---

## What stays the same

- License (MIT)
- Author / credits
- The 5-agent architecture (now generalized but conceptually identical)
- The original 4 history master prompts (preserved as examples)
- The reference Tim Reborn analysis (preserved as a worked example)
- `tools/_build.py` (still works for any markdown → PDF)

---

## What users gain

| Before | After |
| --- | --- |
| Could only make grimdark history videos | Can make any niche of cinematic AI video |
| Locked into Tim Reborn formula | Locked into whatever formula they pick |
| 4 master prompts, take-it-or-leave-it | Infinite master prompts, generated on demand |
| Repo was the artifact | Repo is the factory |

---

## Rollback plan

If v2 breaks anything:

1. The legacy prompts are untouched — users can still paste them directly.
2. Tag the v1 commit before merging v2: `git tag v1.0.0-final` and push.
3. Anyone wanting v1 behavior: `git checkout v1.0.0-final`.

---

## Suggested commit sequence

```bash
# 1. Tag v1
git tag v1.0.0-final
git push origin v1.0.0-final

# 2. Create v2 branch
git checkout -b v2-generalized

# 3. Add new files
git add META-PROMPT.md agents/ templates/ MIGRATION-GUIDE.md
git commit -m "feat: add META-PROMPT generator and 5-agent pipeline"

# 4. Move legacy prompts
mkdir -p prompts/legacy
git mv prompts/MASTER-PROMPT-*.md prompts/legacy/
git commit -m "refactor: move v1 master prompts to prompts/legacy/ as examples"

# 5. Rewrite README + SKILL
git add README.md SKILL.md CHANGELOG.md
git commit -m "docs: rewrite for niche-agnostic v2 workflow"

# 6. Add new examples
git add examples/input-mansion-restoration.md examples/input-luxury-watch-restoration.md
git commit -m "examples: add non-history niche samples"

# 7. Tag and merge
git tag v2.0.0
git checkout main
git merge v2-generalized
git push origin main --tags
```
