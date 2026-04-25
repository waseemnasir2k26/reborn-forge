# Agent 4 — Prompt Architect

> Designs the master prompt as a pipeline-style system. The compiled output lives in `prompts/MASTER-PROMPT-REBORN-ENGLISH.md`. This document is the **architecture spec** — the reasoning behind every section of the master prompt.

**INPUT:**
- NICHE PROFILE: `01-niche-intelligence.md`
- PATTERN: `03-pattern-engine.md`
- VIDEO ANALYSIS: `02-video-analysis.md`

---

## [SYSTEM ROLE]

> "You are an AI system specialized in generating cinematic English long-form AI-historical-reconstruction YouTube videos in the style of Tim - Reborn History. Output pipeline: SCRIPT → IMAGE PROMPTS → SCENE JSONs."

**Why a system role and not an instruction set:** the model needs to anchor itself to a *persistent identity* across 3 phases. An instruction set drifts after Phase 1. A system role survives multi-turn continuation commands (`phase 2`, `phase 3`, `rebuild scene N`).

## [PRIMARY OBJECTIVE]

Six priorities, **strict order, never overridden**:

1. Historical accuracy
2. Atmospheric dread
3. Narrator cadence
4. Continuity
5. Cinematic restraint
6. Retention

**Why this order:** retention is last because in this niche, retention is *produced* by the first five. If you optimize for retention directly, you get fast cuts and shock hooks — which fails the genre. If you optimize for accuracy + dread + cadence + continuity + restraint, retention emerges as a side effect.

## [INPUT SYSTEM]

Six fields. Two required (TOPIC, DURATION). Four optional with sensible defaults (ERA inferred, GEOGRAPHY inferred, NARRATOR defaulted, KEY FIGURES inferred).

**Why minimal inputs:** the master prompt does the research itself via internal HISTORY CARD construction. Forcing the user to supply 12 fields increases drop-off; forcing 2 fields with optional 4 produces 90% of the quality at 30% of the friction.

## [FIXED STRUCTURE]

The 6-stage arc is **mandatory and invariant**. The prompt cannot be reconfigured to use 4 stages or 8 stages — those break the genre.

The 4-axis variant engine (era × geography × POV × visual motif) is **flexible** — 1,050 combinations within the fixed structure.

This is the right rigidity/flexibility split: fix what defines the genre, vary everything else.

## [FIRST FRAME RULE]

> "Single grim image + one-line stake. No music. Whisper VO. SFX: distant single church bell toll at 0:03, wind bed."

**Why exactly this:** the first 1.5 seconds of the video must produce three signals simultaneously:

1. **Cinema signal** — 80% shadow + halation + grain → "this is not a slideshow channel"
2. **Genre signal** — desaturated cool LUT → "this is grimdark history, not pop history"
3. **ASMR signal** — silence + whisper → "this is sleep-listen tier, settle in"

If any of the three is missing, the wrong audience clicks through and bounces. The first-frame rule is **load-bearing**.

## [PROGRESSION RULE]

> "Scene N+1 = Scene N + ONE change (position OR action OR weather — not all)."

**Why one-axis evolution:** AI image+video models cannot maintain continuity across multi-axis changes. Single-axis change keeps the viewer's perceptual model intact. Multi-axis change reads as "different scene entirely" and breaks the trance.

Plus: the audio bed is built on continuity. A music drone that's been holding D minor for 90 seconds is broken by a sudden visual jump-cut. Single-axis change preserves the audio illusion.

## [CONSTRAINT SYSTEM]

### Pacing constraints
- Longform shot duration: 4–6 sec average; 12–25s on hero stills.
- Shorts shot duration: 1.5–2.5 sec.
- VO pace: 125–140 wpm English; 130–145 Hindi.
- Music entry: never before 8 sec.
- Music level: −20 LUFS minimum under VO.

### Visual constraints
- Color: crushed black + cool blue-grey + desaturated mid-greens + 55% saturation + heavy 16mm grain + soft halation.
- Composition: low-angle + over-shoulder + dirty foreground.
- Camera moves: slow Ken Burns push-in / pull-out / left-right parallax / static / orbital 10° (rare).
- Forbidden: drone, whip pans, rack focus, shaky cam, fast cuts, saturated colors.

### Narrative constraints
- Past-tense, third-person, mournful.
- Sentence length 15–25 words avg.
- No second-person address.
- No moral lectures.
- No questions to viewer.
- Date + place anchors at scene openers.

### Consistency constraints
- 50-word character description reused VERBATIM across scenes.
- Geography lock: named landmarks appear same shape, weather, decay-level.
- Era lock: technology cap enforced (no anachronistic objects).
- Linguistic register lock (per locale).

## [OUTPUT FORMAT]

Three artifacts, gated by continuation commands:

### Phase 1 — Script
Markdown. PDF-ready. Contains:
- Title + metadata header (duration, era, geography, narrator)
- HISTORY CARD (sources, causal chain, mortality, named figures, anachronism warnings)
- Thumbnail + YouTube metadata block
- Scene-by-scene VO + on-screen text + music cue + SFX + visual seed

### Phase 2 — Image prompts
One per scene. Each prompt is a structured 9-line block:
1. Subject lock
2. Action verb
3. Setting (era + geography + architecture + weather)
4. Costume (era-correct fabric + color + no anachronism)
5. Lighting (key + fill + practical + volumetric)
6. Camera (lens + height + aperture + movement + composition bias)
7. Color grade (full spec)
8. Mood
9. Medium + film stock + LUT
+ Negative prompt
+ Aspect ratio + style + version flags

### Phase 3 — Scene JSONs
Strict JSON schema for Kling / Runway / VEO consumption:
- scene_id, stage, duration_seconds, aspect_ratio
- start_image, end_image references
- camera object (lens, movement, speed, height, angle, composition)
- subject_motion + environment_motion objects
- lighting object (key + fill + practical + volumetric)
- audio object (vo_english + vo_localized + music + sfx[])
- color_grade string
- continuity_locks object (character_face_ref + geography + era_cap)
- negative_prompt string
- render_target string

## [ANTI-FAIL CONDITIONS]

12 regenerate triggers, encoded into the master prompt:

1. Anachronism (per kill list)
2. Character drift across scenes
3. Saturated colors
4. Music too early (before 8 sec)
5. Music too loud (over −20 LUFS under VO)
6. AI-slop tells (extra fingers, melted face, floating objects)
7. Narrator pace > 145 wpm
8. Tonal break (joke / modern reference / cheerful music)
9. Linguistic register break (locale-dependent — e.g. Sanskritized Hindi where Urdu-leaning required)
10. Direct viewer address ("guys" / "doston")
11. Bollywood-style lighting on European/Middle-Eastern scenes (Hindi locale)
12. Devotional uplift register where atrocity demands grief (Hindi locale)

The model is instructed to **regenerate, not repair**. Repair leaves AI-slop traces; regeneration is cheap.

## [CONTINUATION COMMANDS]

Designed for multi-turn workflow. The master prompt is paste-once; user issues short commands thereafter:

| Command | Effect |
|---------|--------|
| `phase 2` | Output image prompts |
| `phase 3` | Output scene JSONs |
| `rebuild scene N` | Regenerate scene N across all 3 phases |
| `variant` | Reroll 4-axis (new era / geography / POV / motif) |
| `next episode` | Adjacent event, same era/geography family |
| `convert to short` | Compress current 12-min to 60s Short |
| `extend to 18 min` | Expand current 8-min to 18-min long |

## [MODEL NOTES]

The architecture document tags which model each phase suits:

- **Claude Opus 4.7 / Sonnet 4.6** — Phase 1 + Phase 3 (respects historical accuracy + JSON completeness).
- **GPT-5.4** — Phase 1 (literary cadence) but watch for inflated symbolism.
- **Gemini 3 Pro** — Phase 2 (Midjourney syntax strength).
- **DeepSeek V3** — bulk Phase 2 (cheap).

This is **stack-aware prompting** — the master prompt is the same across models, but routing decisions per phase optimize cost + quality.

---

## Architecture in one diagram

```
                     ┌─────────────────────────────┐
INPUT ──────────────▶│   MASTER PROMPT (system)    │
(TOPIC + ERA + ...) │  - 6-stage arc (fixed)       │
                     │  - 4-axis variant engine    │
                     │  - 12 anti-fail conditions  │
                     │  - HISTORY CARD (internal)  │
                     └──┬──────────┬──────────┬────┘
                        │          │          │
                        ▼          ▼          ▼
                   ┌─────────┐ ┌────────┐ ┌─────────┐
                   │ PHASE 1 │ │ PHASE 2│ │ PHASE 3 │
                   │ Script  │ │ Image  │ │ Scene   │
                   │  (.md)  │ │ Prompts│ │ JSONs   │
                   │         │ │ (text) │ │ (.json) │
                   └────┬────┘ └────┬───┘ └────┬────┘
                        │           │          │
                        ▼           ▼          ▼
                   ElevenLabs  Midjourney   Kling 2.5
                   + _build.py  v7 / Flux   Master /
                   PDF                       Runway /
                                             VEO 3.1
                        │           │          │
                        └───────────┼──────────┘
                                    ▼
                              CapCut / Premiere
                                    │
                                    ▼
                              YouTube upload
```
