# Example INPUT — Abandoned Mansion Restoration

> Paste the entire `META-PROMPT.md` into Claude / GPT-5 / Gemini, then append this INPUT block at the bottom and submit. The model will return a complete master prompt for the abandoned-mansion-restoration niche.

---

## INPUT block

```
NICHE: abandoned mansion restoration with cinematic transformation arc — debris removal → deep cleaning → structural rebuild → epoxy floor reveal → luxury furnishing → final glow

YOUTUBE_URL: https://www.youtube.com/watch?v=XXXXXXXXXXX
(replace with the reference channel video you want reverse-engineered — e.g., a popular AI mansion-restoration video)

TARGET_TOOL: VEO3

DURATION: longform (8–15 minutes)

LANGUAGE: English

EXTRA_NOTES:
- ASMR-tier sleep-listen register
- Heavy emphasis on satisfying transformation moments
- Epoxy floor must be the visual signature reveal (stage 6 only, indoor only)
- Lock teal-shadow / warm-highlight grade from section 1
- 24mm lens, eye-level fixed framing inside each section
- No workers' faces — keep camera at chest height when humans are in frame
- Each room section: 8–12 stages from filthy to luxurious
```

---

## What the master prompt this generates will let you do

Once you have the master prompt, every new mansion topic just needs:

```
TITLE: Abandoned Tuscan Villa, 1850s Stone Construction
REFERENCE IMAGE: <optional — drop a still>
```

…and it produces:
1. Section-by-section image prompts (one per stage)
2. Scene JSONs for VEO3 (start/end image + camera + audio fields)
3. Transition images and JSONs between sections
4. Audio cues per stage (debris sounds, scrubbing, hammering, epoxy pour, fire ambience)

You stop writing prompts. The master prompt does it.

---

## Variations you can request after generation

- `variant` — re-roll the variation engine (different epoxy types, ceiling styles, lighting setups)
- `tighten` — drop examples, keep rules (more compact)
- `loosen` — expand examples and edge cases
- `show phase 2` — see the underlying video analysis the master prompt was built on
