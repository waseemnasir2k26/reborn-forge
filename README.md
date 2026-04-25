# Reborn History — Cinematic AI History Video Skill

> **A Claude Code skill that generates Tim-Reborn-style grimdark AI history videos.** Three-phase pipeline — Script → Image Prompts → Scene JSONs — engineered for ASMR-tier sleep-listen retention, citation-grade historical accuracy, and the Midjourney + Kling + ElevenLabs + VEO production stack.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)
[![Skill format: SKILL.md](https://img.shields.io/badge/format-SKILL.md-blue)](./SKILL.md)
[![Default language: English](https://img.shields.io/badge/language-English%20%2B%20Hindi-green)](#languages)
[![Reference: Tim Reborn History](https://img.shields.io/badge/reference-Tim%20Reborn%20History-black)](https://www.youtube.com/@Tim_Reborn_History)

---

## What this is

A **reusable, public, MIT-licensed prompt system** that turns any historical event (plague, war, fall of empire, disaster, lost civilization) into a complete production package for a cinematic faceless YouTube video — the same visual + narrative formula used by the *Tim - Reborn History* channel and its imitators.

You give it a topic. It gives you back:

1. A **scene-by-scene script** (8–18 min longform or 60s Short), with VO copy, SFX cues, music timing, on-screen text, and citation-grade history-card.
2. An **image prompt** for every scene (Midjourney v7 / Flux 1.1 Pro / Nano Banana), era-locked with anachronism guards.
3. A **motion JSON** for every scene (Kling 2.5 Master / Runway Gen-4 / VEO 3.1) with camera moves, lighting, audio fields, and continuity locks.

You assemble in CapCut / Premiere. Ship.

**Reference video reverse-engineered:** [*The Bubonic Plague in the 1300s* — Tim Reborn History](https://www.youtube.com/watch?v=X-UgHOce2kk).

---

## Quick start

### 1. Pick a master prompt

| File | Use when |
|------|----------|
| [`prompts/MASTER-PROMPT-REBORN-ENGLISH.md`](./prompts/MASTER-PROMPT-REBORN-ENGLISH.md) | **DEFAULT.** English longform 8–18 min, grimdark, ASMR sleep-listen tier. |
| [`prompts/MASTER-PROMPT-REBORN-HINDI.md`](./prompts/MASTER-PROMPT-REBORN-HINDI.md) | Hindi longform, Urdu-leaning Hindustani register (taareekh / qayamat / fanaa). |
| [`prompts/MASTER-PROMPT-LONG-HINDI.md`](./prompts/MASTER-PROMPT-LONG-HINDI.md) | Hindi longform, golden-hour register (less grim, more "wonder"). |
| [`prompts/MASTER-PROMPT-SHORT-HINDI.md`](./prompts/MASTER-PROMPT-SHORT-HINDI.md) | 9:16 Short / Reel / TikTok, 45–60 sec, fast pacing. |

### 2. Paste it into Claude, GPT, or Gemini

Copy the fenced master-prompt block. Paste into your model of choice. Fill the INPUT block:

```
TOPIC: Bubonic Plague 1347 Europe
ERA: 1347–1351 CE
GEOGRAPHY: Messina → Genoa → Marseille → Avignon → Paris → London
DURATION: 12 minutes
NARRATOR: ElevenLabs "Adam" — British-RP somber
KEY NAMED FIGURES: Pope Clement VI, Boccaccio, Gabriele de' Mussi, Edward III
```

### 3. Receive Phase 1 → 2 → 3

The model returns Phase 1 (script). Type `phase 2` for image prompts. Type `phase 3` for scene JSONs.

### 4. Build

- Generate stills in Midjourney v7 (`--ar 16:9 --style raw --v 7`).
- Animate with Kling 2.5 Master (5–10s clips, start + end image, JSON).
- Voice with ElevenLabs (Adam / Brian / Daniel for English; Anjali / Niraj for Hindi).
- Assemble in CapCut or Premiere. Add 16mm grain overlay. FilmConvert Nostalgic LUT. Master to −14 LUFS.

### 5. Build PDF (optional)

```bash
python tools/_build.py
```

Generates printable PDFs of every script + prompt file in the repo into `PDF/`.

---

## Why this skill works

It's the result of a **5-agent reverse-engineering pipeline** applied to a viral channel. Each agent's output lives in [`reference/`](./reference/):

| Agent | Output | File |
|-------|--------|------|
| 1 — Niche Intelligence | Defines how the AI-history niche behaves (content type, hook, pacing, retention drivers, failure conditions) | [`reference/01-niche-intelligence.md`](./reference/01-niche-intelligence.md) |
| 2 — Video Analyzer | Breaks reference video into observable structure (first frame, scroll-stop trigger, contradiction, section flow, pacing, transformation, loop logic) | [`reference/02-video-analysis.md`](./reference/02-video-analysis.md) |
| 3 — Pattern Engine | Converts video into reusable system (core pattern, structure model, retention mechanism, progression logic, repeatable template) | [`reference/03-pattern-engine.md`](./reference/03-pattern-engine.md) |
| 4 — Prompt Architect | Designs the master prompt (system role, primary objective, fixed structure, first-frame rule, progression rule, constraints, output format, anti-fail) | [`reference/04-prompt-architect.md`](./reference/04-prompt-architect.md) |
| 5 — Output Compiler | Cleans + finalizes for direct paste-and-use | [`reference/05-output-compiler.md`](./reference/05-output-compiler.md) |

Plus deep research on the reference channel: [`reference/tim-reborn-research.md`](./reference/tim-reborn-research.md).

---

## The formula in one paragraph

**Cold-Open Atrocity → Context Drop → Human Vignette → Escalation → Death Toll → Quiet Coda.** Open mid-horror (a body, a scream, a burning village). Pull back to "It was the year 1347…". Drill into one named or archetypal person. Escalate the body count with map/numbers overlay. Land on a slow, almost mournful epilogue ("…and so the world was changed forever"). No moral lecture — the imagery carries the meaning. Visual signature: **desaturated sepia-to-cool-grey LUT, chiaroscuro low-key lighting (80% shadow), slow Ken Burns + 2.5D parallax on Midjourney stills, heavy 16mm grain + halation, low-angle + over-shoulder POV with dirty foreground.** Audio signature: **125–140 wpm somber British-RP narration, dark-ambient drone at 60–75 BPM in D minor / A minor, music sits −20 LUFS under VO, first 8 sec silent, single church bell as pattern interrupt.**

---

## Repository layout

```
AI-HISTORY-VIDEO-SYSTEM/
├── README.md                                  ← you are here
├── SKILL.md                                   ← Claude Code skill manifest
├── LICENSE                                    ← MIT
├── CHANGELOG.md
├── CONTRIBUTING.md
├── .gitignore
├── prompts/                                   ← 4 master prompts
│   ├── MASTER-PROMPT-REBORN-ENGLISH.md        ← DEFAULT
│   ├── MASTER-PROMPT-REBORN-HINDI.md
│   ├── MASTER-PROMPT-LONG-HINDI.md
│   └── MASTER-PROMPT-SHORT-HINDI.md
├── reference/                                 ← 5-agent pipeline outputs
│   ├── 01-niche-intelligence.md
│   ├── 02-video-analysis.md
│   ├── 03-pattern-engine.md
│   ├── 04-prompt-architect.md
│   ├── 05-output-compiler.md
│   ├── tim-reborn-research.md
│   └── style-guide.md
├── examples/                                  ← sample inputs
│   ├── input-bubonic-plague.md
│   ├── input-fall-of-baghdad.md
│   ├── input-pompeii.md
│   └── input-great-fire-london.md
├── tools/
│   └── _build.py                              ← markdown → PDF builder
├── PDF/                                       ← build outputs (gitignored)
└── .github/
    ├── ISSUE_TEMPLATE/
    └── workflows/
```

---

## Languages

**Default: English (general).** The skill is English-first. Hindi (Urdu-leaning Hindustani) is included as an optional locale because the original use-case targeted both an English Reborn channel and a Hindi cluster (`@HistoryVision2`-style). If you want to add a locale (Spanish, Arabic, Mandarin, Portuguese), fork the English master and apply a register lock similar to the Hindi file's vocabulary table.

---

## Stack

| Layer | Tool | Why |
|-------|------|-----|
| Stills | **Midjourney v7** (preferred) / Flux 1.1 Pro / Nano Banana | Strongest grimdark engraving-revival look at 16:9 |
| Motion | **Kling 2.5 Master** (preferred) / Runway Gen-4 / VEO 3.1 | Cheapest path to cinematic 4K parallax animation |
| Voice | **ElevenLabs Multilingual v3** | Universal in this niche; British-RP voices nail the register |
| Music | **Suno v4** / Epidemic Sound / Artlist | Dark-ambient drone, beatless, D minor / A minor |
| Edit | **CapCut Pro** / Premiere / DaVinci Resolve | Final grain, LUT, master mix |
| Upscale | **Topaz Video AI** | 4K final pass |

Total cost per video: **$35–$190** depending on tier.

---

## Anti-fail checklist (built into the prompt)

- ❌ Plague-doctor beak mask in pre-1619 scenes (mask is 1619 Lorme design — easy AI tell)
- ❌ Eyeglasses pre-1286, printed books pre-1440, gunpowder cannon pre-1340 in Europe
- ❌ Yersinia pestis as period name (named 1894)
- ❌ Modern uniform cobblestone (medieval streets were rough mud + stone mix)
- ❌ Saturated colors (genre = grimdark; kill anything cheerful)
- ❌ Cuts faster than 4 sec in longform (breaks ASMR trance, exposes AI artifacts)
- ❌ Music in first 8 sec (HOOK must be silent)
- ❌ Narrator pace > 145 wpm (fails sleep-listen register)
- ❌ Direct address to viewer ("guys", "doston") — kills ASMR spell
- ❌ Tonal break: joke, modern reference, cheerful music

If a scene fails any rule, regenerate before render.

---

## Production SOP

1. Pick master prompt → fill INPUT → receive Phase 1.
2. Save `SCRIPT-<topic>-REBORN.md`. Build PDF via `python tools/_build.py`.
3. Type `phase 2` → save `IMAGE-PROMPTS-<topic>-REBORN.md`.
4. Generate Midjourney stills, 2–3 variations per scene. Save best as `scenes/S01-start.png`, `S01-end.png`.
5. Type `phase 3` → save `SCENES-<topic>-REBORN.json`.
6. Render 5–10s motion clips in Kling 2.5 Master. Use start+end image + JSON.
7. ElevenLabs VO export. Pace 125–140 wpm. Light reverb (0.4s).
8. CapCut/Premiere assembly. 16mm grain overlay. Vignette. FilmConvert Nostalgic LUT. Music bed −20 LUFS under VO.
9. Run anti-fail checklist. Regenerate any flagged scenes.
10. Master to **−14 LUFS / −1 dBTP**. Upload YouTube. Title + tags from script header.

---

## 1,050 unique formats — 4-axis variant engine

The skill has a baked-in variant generator: **6 ERAs × 7 GEOGRAPHIES × 5 POVs × 5 VISUAL MOTIFs = 1,050 format combinations**. Type `variant` after Phase 1 to reroll. Track combos across your channel history to avoid self-cannibalization.

---

## Examples

See [`examples/`](./examples/) for ready-to-paste INPUT blocks:

- [Bubonic Plague 1347](./examples/input-bubonic-plague.md) — canonical reference
- [Fall of Baghdad 1258](./examples/input-fall-of-baghdad.md) — Mongol siege, alternate geography
- [Pompeii 79 CE](./examples/input-pompeii.md) — antiquity disaster
- [Great Fire of London 1666](./examples/input-great-fire-london.md) — early modern disaster

---

## Contributing

PRs welcome — especially:

- New locales (translate Hindi register-lock template to Spanish, Arabic, Portuguese, Mandarin)
- New variant axes (e.g. SCALE: city / region / continent / global)
- New image-engine sub-prompts (Sora 2, Wan 2.5, Hailuo)
- More example INPUT blocks (one per major historical era)
- Bug reports for anachronisms the prompt fails to catch

See [CONTRIBUTING.md](./CONTRIBUTING.md).

---

## Credits

- **Reference channel:** [Tim - Reborn History](https://www.youtube.com/@Tim_Reborn_History) — the formula this skill reverse-engineers.
- **Architecture parent:** Skyline Reborn (Abandoned-Jet-Prompt-System).
- **Built by:** [Waseem Nasir](https://www.waseemnasir.com) / [SkynetLabs](https://www.skynetjoe.com).

---

## License

MIT — see [LICENSE](./LICENSE). Free for commercial use. Attribution appreciated, not required.

If you ship something good with this skill, [tag me](https://www.linkedin.com/in/waseem-nasir-skynet/) — I want to watch it.
