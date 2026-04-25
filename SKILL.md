---
name: reborn-history
description: Generate Tim-Reborn-style grimdark AI history videos in English. Three-phase pipeline (Script → Image Prompts → Scene JSONs) producing cinematic 8–18 min YouTube longforms or 60s Shorts. Engineered for ASMR-tier sleep-listen retention, citation-grade historical accuracy, and Midjourney v7 + Kling 2.5 + ElevenLabs v3 + VEO 3.1 production stack. Optional locales include Hindi (Urdu-leaning Hindustani). Trigger when user says "reborn history", "AI history video", "grimdark history", "history reconstruction", "plague video", "fallen empire video", or invokes /reborn-history.
license: MIT
---

# Reborn History — Claude Code Skill

Cinematic AI-history video generation system. Reverse-engineered from Tim - Reborn History (`@Tim_Reborn_History`), reference video *The Bubonic Plague in the 1300s* (`X-UgHOce2kk`).

**Default language:** English (general). **Optional locales:** Hindi (Urdu-leaning Hindustani).

## When to use

- User asks for an AI-history YouTube video
- Topic is dark/grimdark: plague, war, atrocity, fall-of-empire, lost civilization, disaster
- Format is faceless, narrated, cinematic, 8–18 min longform OR 60s Short
- Target stack: Midjourney v7 / Flux 1.1 Pro + Kling 2.5 / Runway Gen-4 / VEO 3.1 + ElevenLabs v3 + CapCut/Premiere

## Pipeline

Three phases. One input.

| Phase | Output | Tool consumes |
|-------|--------|---------------|
| 1 | Script (markdown, scene-by-scene VO + SFX + visual seed) | ElevenLabs (VO), `tools/_build.py` (PDF) |
| 2 | Image prompts (one per scene, era-locked, anti-anachronism) | Midjourney v7 / Flux 1.1 Pro / Nano Banana |
| 3 | Scene JSONs (camera + motion + audio + continuity locks) | Kling 2.5 Master / Runway Gen-4 / VEO 3.1 |

## How to invoke

1. Pick prompt by language + format:
   - **English grimdark longform (DEFAULT)** → [`prompts/MASTER-PROMPT-REBORN-ENGLISH.md`](./prompts/MASTER-PROMPT-REBORN-ENGLISH.md)
   - English/Hindi grimdark Short (9:16, 60s) → [`prompts/MASTER-PROMPT-SHORT-HINDI.md`](./prompts/MASTER-PROMPT-SHORT-HINDI.md)
   - Hindi grimdark longform (Urdu-leaning) → [`prompts/MASTER-PROMPT-REBORN-HINDI.md`](./prompts/MASTER-PROMPT-REBORN-HINDI.md)
   - Hindi golden-hour longform → [`prompts/MASTER-PROMPT-LONG-HINDI.md`](./prompts/MASTER-PROMPT-LONG-HINDI.md)
2. Copy the fenced master-prompt block, paste into Claude/GPT/Gemini.
3. Fill INPUT (TOPIC, ERA, GEOGRAPHY, DURATION, NARRATOR, KEY FIGURES).
4. Receive Phase 1 (Script). Then `phase 2` (Image prompts), then `phase 3` (Scene JSONs).

## Inputs

```
TOPIC: <event/era>          — e.g. "Bubonic Plague 1347 Europe"
ERA: <verified dates>       — e.g. "1347–1351 CE"
GEOGRAPHY: <route>          — e.g. "Messina → Genoa → Marseille → Paris"
DURATION: 8 | 12 | 18 min   — longform; 45 | 60 sec for Short
NARRATOR: <ElevenLabs voice>— e.g. "Adam (British-RP somber)" / "Daniel" / "Brian"
KEY FIGURES: <optional>     — verified historical individuals
```

## Constraints (anti-fail)

- **Anachronism kill list**: plague-doctor beak mask pre-1619, eyeglasses pre-1286, printed books pre-1440, gunpowder cannon pre-1340, Yersinia pestis as period name (named 1894).
- **Pacing lock**: 4–6 sec/shot longform, 1.5–2.5 sec Shorts. Hold 12–25s on hero stills.
- **Audio lock**: VO 125–140 wpm; music −20 LUFS under VO; first 8 sec silent.
- **Color lock**: crushed black + cool blue-grey + desaturated mid-greens + 55% saturation + heavy 16mm grain + FilmConvert Nostalgic LUT.
- **Composition signature (Tim Reborn)**: low-angle + over-shoulder POV + dirty foreground (hood, hand, banner edge).
- **Continuity lock**: 50-word character description reused VERBATIM across scenes.

## Output deliverables

- `SCRIPT-<topic>-REBORN.md`
- `IMAGE-PROMPTS-<topic>-REBORN.md`
- `SCENES-<topic>-REBORN.json`
- PDF via `python tools/_build.py`

## Skill files

- [`prompts/`](./prompts/) — four master prompts (English-Reborn DEFAULT, Hindi-Reborn, Hindi-Long, Hindi-Short)
- [`reference/`](./reference/) — 5-agent pipeline outputs: niche intelligence, video analysis, pattern engine, prompt architect, output compiler, Tim Reborn deep research
- [`examples/`](./examples/) — sample INPUT blocks
- [`tools/_build.py`](./tools/_build.py) — markdown → PDF builder

## Cost + time per video

| Tier | Tooling | Cost | Time |
|------|---------|------|------|
| Low | Midjourney Basic + Kling 2.5 std + ElevenLabs Creator | $35–48 | 6 hrs |
| Mid | Midjourney Std + Kling 2.5 Master + Runway Gen-4 hero + ElevenLabs Pro | $70–110 | 8 hrs |
| Premium | Midjourney Pro + Kling 2.5 Master + VEO 3.1 + ElevenLabs voice clone | $130–190 | 10 hrs |

## Continuation commands

`phase 2` · `phase 3` · `rebuild scene N` · `variant` (4-axis reroll) · `next episode` · `convert to short` · `extend to 18 min`

## License

MIT. Free for commercial use. Attribution appreciated.
