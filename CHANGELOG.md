# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [2.1.0] — 2026-04-25

### Added
- `SCRIPT WRITING SYSTEM` section to the canonical master-prompt structure (now 34 sections, was 33)
- Section is **always present** with explicit `MODE`: `full-narration` / `minimal-narration` / `text-only` / `silent`
- Register lock: tone, wpm, sentence length, vocabulary, direct-address rules, person, reading level
- Hook formula: second-by-second breakdown of first 8 seconds + open-loop planting
- Section-level script structure: word count + duration + tone + mandatory content per section
- Retention mechanics: open loop, mini-payoff cadence, named-subject introduction, pattern interrupts, curiosity gaps
- On-screen text rules: char limits, hold times, fonts, positioning, use cases, forbidden patterns
- Cue notation reference: `[SFX: ...]`, `[MUSIC IN/OUT/SWELL/DUCK]`, `[PAUSE: Ns]`, `[BEAT]`, `[SOURCE: ...]`, `[ON-SCREEN: ...]`
- Closing-line formula with forbidden CTAs
- Script anti-fail list (6+ niche-specific failures per niche)
- Script output format example (worked 2-section + closing example)
- New post-generation commands: `script only`, `flip mode to {full|minimal|text-only|silent}`

### Changed
- `META-PROMPT.md` — PHASE 4 now has 9 architectural decisions (was 8); added DECISION 9 — Script System
- `agents/04-prompt-architect.md` — added DECISION 9 (subsections 9a–9j) covering the full script architecture
- `agents/05-output-compiler.md` — assembly order now 34 items (script slots between AUDIO and LIGHTING); quality gates updated
- `templates/MASTER-PROMPT-TEMPLATE.md` — added SCRIPT WRITING SYSTEM skeleton and updated Structural Contract to require it
- `SKILL.md` — section list bumped to 34, quality gates expanded, new commands documented
- Minimum master-prompt length raised from 1500 to 1800 words to account for new section

### Rationale
Some niches (history, lore, mystery, educational) require scripts to maximize clarity, engagement, and retention. Other niches (ASMR-craft, aesthetic loops) need minimal or zero narration. The previous version of the META-PROMPT had no script architecture at all, leaving downstream models to invent their own VO style. The new MODE-based system makes the niche's voice/text policy explicit and enforceable, while keeping the section flexible enough to span every niche from grimdark history (full-narration) to aesthetic mansion-restoration loops (silent).

---

## [2.0.0] — 2026-04-25

Major release. The repo evolves from a single-niche skill (cinematic AI history) into a niche-agnostic master-prompt generator.

### Added
- `META-PROMPT.md` — paste-and-use generator that takes `NICHE` + `YOUTUBE_URL` and produces a complete master prompt
- `agents/01-niche-intelligence.md` — niche profiling agent
- `agents/02-video-analyzer.md` — reference-video forensic analyzer
- `agents/03-pattern-engine.md` — formula extractor and structure model builder
- `agents/04-prompt-architect.md` — 8-decision architectural designer
- `agents/05-output-compiler.md` — final assembly + quality gates
- `templates/MASTER-PROMPT-TEMPLATE.md` — canonical 33-section output skeleton
- `examples/input-mansion-restoration.md` — non-history example
- `examples/input-luxury-watch-restoration.md` — non-history example
- `MIGRATION-GUIDE.md` — v1 → v2 upgrade path

### Changed
- `README.md` — rewritten for niche-agnostic workflow
- `SKILL.md` — `name` updated to `reborn-master-prompt-generator`, `version` bumped to 2.0.0
- Repo positioning shifted from "history video skill" to "master prompt generator"

### Moved
- `prompts/MASTER-PROMPT-REBORN-ENGLISH.md` → `prompts/legacy/`
- `prompts/MASTER-PROMPT-REBORN-HINDI.md` → `prompts/legacy/`
- `prompts/MASTER-PROMPT-LONG-HINDI.md` → `prompts/legacy/`
- `prompts/MASTER-PROMPT-SHORT-HINDI.md` → `prompts/legacy/`
- These are now examples of what the v2 generator produces, not the primary deliverable

### Preserved
- All 4 v1 master prompts continue to work standalone (zero breaking changes for v1 users)
- `reference/` Tim Reborn agent outputs preserved as a worked example
- MIT license, author credits, `tools/_build.py`

### Backward compatibility
Anyone using the v1 master prompts directly: nothing breaks. Tag `v1.0.0-final` is available for `git checkout` if needed.

---

## [1.0.0] — Initial Release

- 4 hardcoded master prompts for grimdark cinematic AI history (English default + 3 Hindi variants)
- 5-agent reverse-engineering pipeline outputs (one-time, hardcoded to Tim Reborn channel)
- 4 example INPUT blocks (Bubonic Plague, Fall of Baghdad, Pompeii, Great Fire of London)
- `_build.py` markdown → PDF tool
- MIT license
