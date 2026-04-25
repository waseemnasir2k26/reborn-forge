# Agent 5 — Output Compiler

> Cleans + finalizes the master prompt for direct paste-and-use. The compiled artifact lives in [`prompts/MASTER-PROMPT-REBORN-ENGLISH.md`](../prompts/MASTER-PROMPT-REBORN-ENGLISH.md).

This document records the **compiler decisions** — what was removed, what was tightened, what was kept verbatim, and why.

---

## Compiler decisions

### Removed
- Internal architecture commentary (lives in `04-prompt-architect.md` instead)
- "Why we chose X" rationale (compiler keeps only what model needs at runtime)
- Examples of what NOT to write (model treats negative examples as suggestions; better to use a Negative Prompt block in Phase 2/3)
- Author preamble / "this prompt was designed by" header
- Repeated reminders ("remember to…") — replaced with single failsafe block

### Tightened
- Stage names: long descriptive ("the COLD-DREAD opening shot of the film") → single token (`COLD_DREAD`)
- Pacing rules: paragraph form → table form
- Continuity rules: prose → enumerated single-axis-change rule
- Music rules: 6 paragraphs → mix-level table

### Kept verbatim
- 6-stage arc names (load-bearing for downstream commands like `rebuild scene 4` to know what stage scene 4 is in)
- Anachronism kill list (precision matters — "plague-doctor beak mask pre-1619" must be exact, not paraphrased)
- LUT references (`FilmConvert FJ Nostalgic`, `ARRI K1S1 desaturated`) — these are concrete tooling references the editor uses
- Mortality stats with sources (citation-grade requirement)
- Continuation command syntax (`phase 2`, `phase 3`, `rebuild scene N`, `variant`) — the user types these, so they must match exactly

---

## Compiled output

The final master prompt is at:

**[`../prompts/MASTER-PROMPT-REBORN-ENGLISH.md`](../prompts/MASTER-PROMPT-REBORN-ENGLISH.md)** (DEFAULT, English, general use)

Three additional locale/format compilations:

- [`../prompts/MASTER-PROMPT-REBORN-HINDI.md`](../prompts/MASTER-PROMPT-REBORN-HINDI.md) — Hindi grimdark longform (Urdu-leaning)
- [`../prompts/MASTER-PROMPT-LONG-HINDI.md`](../prompts/MASTER-PROMPT-LONG-HINDI.md) — Hindi golden-hour longform
- [`../prompts/MASTER-PROMPT-SHORT-HINDI.md`](../prompts/MASTER-PROMPT-SHORT-HINDI.md) — Hindi/English Short (9:16, 60s)

---

## Validation checklist (run before publishing a new compilation)

When you fork this skill and produce a new master prompt (e.g. for a new locale or format), validate against:

- [ ] Single fenced ```` ```` ```` block contains the full prompt — user can copy-paste in one selection
- [ ] System role is the first non-blank line inside the fenced block
- [ ] PRIMARY OBJECTIVE table appears in priority order (1 → 6)
- [ ] INPUT SYSTEM lists every required + optional field
- [ ] HISTORICAL ACCURACY LOCK includes era-specific anachronism kill list
- [ ] 6-stage arc table appears with % runtime targets
- [ ] 4-axis variant engine spec appears
- [ ] CAMERA SYSTEM has lens / movement / aperture / hold-time
- [ ] COLOR GRADING LOCK has shadows / midtones / highlights / saturation / haze / grain / vignette / LUT
- [ ] AUDIO SYSTEM has VO + music + SFX-per-stage + mix-level table
- [ ] PHASE 1 OUTPUT spec produces a single markdown block (script)
- [ ] PHASE 2 OUTPUT spec is one-prompt-per-scene with negative-prompt and aspect flags
- [ ] PHASE 3 OUTPUT spec is one-JSON-per-scene with all required fields
- [ ] CONTINUITY RULES include character + geography + weather progression rules
- [ ] FAILSAFE block lists at least 8 regenerate triggers
- [ ] CONTINUATION COMMANDS list `phase 2`, `phase 3`, `rebuild scene N`, `variant` minimum
- [ ] MODEL NOTES suggest model routing per phase
- [ ] BEGIN trigger at end so the model knows to start

---

## Failure modes the compiler prevents

1. **Multi-block prompts** — user copies first block, misses the rest. Fix: single fenced block.
2. **Drift across continuation turns** — model loses pacing rules by Phase 3. Fix: rules embedded in system role, not in instruction body.
3. **Anachronism creep** — model proposes "smart" period names. Fix: explicit kill list with year-locked replacements.
4. **JSON schema breakage in Phase 3** — model omits fields like `continuity_locks`. Fix: full schema in master prompt; prompt instructs "complete JSON, every field, no nulls."
5. **Locale register drift** — Hindi master prompt drifts into Sanskritized academic register. Fix: explicit USE / AVOID vocabulary table embedded in master prompt.
6. **Cost-tier confusion** — user asks "which engine should I use?" mid-conversation. Fix: model routing table embedded in master prompt.

---

## When to recompile

Recompile when:

- New image / video engine emerges with materially different syntax (e.g. Sora 2 release, Wan 2.5)
- Anachronism gap discovered (one era's tech-cap was wrong) → update kill list + recompile
- Locale gap discovered (a vocabulary item drifts in the model) → update register table + recompile
- Pricing tier shifts > 50% (e.g. Kling 2.5 → Kling 3.0 changes mid-tier cost)
- Phase 3 JSON schema needed extension (new field — e.g. `lip_sync_target` for VEO 3.1)

Don't recompile for:

- Cosmetic improvements ("this could be worded better")
- Adding more examples (examples bloat the prompt; keep them in `examples/` instead)
- Reorganizing for readability (the model reads the prompt the same regardless of human readability)
