# Changelog

All notable changes to this skill will be documented here. Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [1.0.0] — 2026-04-25

### Added
- **English Reborn master prompt** — DEFAULT. Tim-Reborn-style grimdark, 8–18 min longform, ASMR sleep-listen tier. (`prompts/MASTER-PROMPT-REBORN-ENGLISH.md`)
- **Hindi Reborn master prompt** — Urdu-leaning Hindustani register (taareekh / qayamat / fanaa vocabulary lock). (`prompts/MASTER-PROMPT-REBORN-HINDI.md`)
- **Hindi golden-hour longform** master prompt. (`prompts/MASTER-PROMPT-LONG-HINDI.md`)
- **Hindi/English Short master prompt** — 9:16, 45–60 sec. (`prompts/MASTER-PROMPT-SHORT-HINDI.md`)
- **5-agent reverse-engineering reference set:**
  - Niche Intelligence
  - Video Analyzer (Tim Reborn `X-UgHOce2kk`)
  - Pattern Engine
  - Prompt Architect
  - Output Compiler
- **Tim Reborn deep research** — channel-cluster analysis, visual signature breakdown, tooling-stack fingerprint, hook template, retention drivers. (`reference/tim-reborn-research.md`)
- **Style guide** — color/composition/audio/anti-anachronism rules. (`reference/style-guide.md`)
- **Example INPUT blocks** — Bubonic Plague 1347, Fall of Baghdad 1258, Pompeii 79 CE, Great Fire of London 1666.
- **`tools/_build.py`** — markdown → PDF builder (auto-discovers all `.md` files).
- **GitHub repo scaffolding** — `SKILL.md`, `LICENSE` (MIT), `CHANGELOG.md`, `CONTRIBUTING.md`, `.gitignore`, issue templates, FUNDING.

### Architecture
- 3-phase pipeline: Script → Image Prompts → Scene JSONs.
- 6-stage narrative arc: Cold Dread → Origin → Spread → Collapse → Aftermath → Echo.
- 4-axis variant engine: 6 eras × 7 geographies × 5 POVs × 5 visual motifs = 1,050 unique formats.
- Anachronism kill list: plague-doctor beak mask pre-1619, eyeglasses pre-1286, printed books pre-1440, gunpowder cannon pre-1340.
- Continuity lock: 50-word character description reused verbatim across scenes.

### Inherited from Skyline Reborn
- Markdown → PDF pipeline.
- Phase-gated continuation (`phase 2`, `phase 3`, `rebuild scene N`, `variant`).
- Citation-grade source lock (Britannica, history.com, Science Museum, JSTOR).
