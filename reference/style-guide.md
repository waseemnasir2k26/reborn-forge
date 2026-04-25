# Style Guide — Reborn History Skill

> Single source of truth for color, composition, audio, narration, and anachronism rules. Every master prompt in `prompts/` enforces this guide. Edit this file when the genre's standards shift; recompile prompts.

---

## Color grade

| Channel | Target |
|---------|--------|
| Shadows | Crushed deep black; lifted blacks rolled toward cool blue-grey |
| Midtones | Muted grey-green, desaturated; skin pushed yellow-green for plague pallor |
| Highlights | Cool overcast white; occasional warm earth-tone (rust, ochre, burnt umber) |
| Saturation | **50–60%** (Echo stage may creep to 65%) |
| Haze / mist | 20–30% mid-ground volumetric |
| Halation | Soft, around bright sources (candle, torch, window shaft) |
| Grain | Heavy 16mm |
| Vignette | Subtle dark-corner falloff |
| LUT | `FilmConvert FJ Nostalgic` OR `ARRI K1S1 desaturated` |

**Reject:** saturated reds (except blood/fire), golden-hour light, daylight Midjourney defaults, Bollywood-style key lighting.

---

## Composition

| Element | Target |
|---------|--------|
| Lens | 35–85mm |
| Aperture feel | f/2.8–f/4 (shallow, claustrophobic) |
| Eye height | 1.50–1.65m |
| Camera angle | **Low-angle + over-shoulder POV preferred** |
| Foreground | **Dirty foreground element** (hood, hand, banner edge, gloved sleeve) |
| Frame in shadow | **80%** |
| Hard key | Single source (candle, torch, window shaft, off-frame west sun) |
| Volumetric | God-rays through dust/smoke at 30% opacity (signature recurring beat) |

**Reject:** drone shots, whip pans, rack focus, shaky cam, perfectly clean foregrounds.

---

## Camera movement

One movement per scene. Pick from:

- Slow Ken Burns push-in (0.2× speed) — most common
- Slow pull-out
- Left-to-right parallax (2.5D)
- Static locked-off (allowed for hero stills, 5–8s)
- Orbital 10° (rare, hero only)

**Reject:** any movement that doesn't fit ASMR pacing.

---

## Audio

### Voice over

| Property | Target |
|----------|--------|
| Engine | ElevenLabs Multilingual v3 |
| Voice (English) | "Adam" / "Brian" / "Daniel" — British-RP somber preferred |
| Voice (Hindi) | "Anjali" / "Niraj" — somber baritone, or custom-cloned Urdu-leaning male |
| Pace (English) | **125–140 wpm** |
| Pace (Hindi) | **130–145 wpm** |
| Register | Literary-grim, past-tense, near-whisper |
| Reverb | Light tail (0.4s, low mix) |
| Compression | Gentle (3:1, slow attack) |

**Reject:** theatrical peaks, second-person address ("you", "doston", "guys"), questions to viewer, comedic interjection, modern-Hindi register.

### Music bed

| Property | Target |
|----------|--------|
| Genre | Dark ambient / medieval drone / cinematic underscore |
| Instrumentation | Low strings (cello drone) + sustained pads + distant choir + hurdy-gurdy / vielle / shawm; for Indo-Persian: santoor drone, ney flute, distant qawwali choir |
| BPM | **60–75** (often beatless) |
| Key | D minor / A minor; for Indo-Persian use Bhairavi / Asavari mode |
| Level | **−20 to −22 LUFS** under VO |
| Source | Suno v4 / Epidemic Sound / Artlist |
| Entry timing | Never before 8 sec |

**Reject:** Bollywood instrumentation on European/Middle-Eastern scenes, BPM > 90, music levels above VO.

### SFX per stage

| Stage | SFX |
|-------|-----|
| Cold Dread | Distant single church bell toll, wind, low rumble |
| Origin | Ship creak, rope groan, rats scurrying, fire crackle |
| Spread | Hoofbeats, cart wheels on cobblestone, distant tolling-bell sequence (3+ tolls) |
| Collapse | Crow caws, flies buzzing, soft cough, body thump on cart, single sob, distant maatam wail (Hindi locale) |
| Aftermath | Church bell single toll, wind through ruins, distant hammer (rebuilding) |
| Echo | Silence → single bell → fade |

### Master mix

| Element | Level |
|---------|-------|
| VO | −3 to −6 dB front, dry to lightly-reverbed |
| Music bed | −18 to −22 LUFS |
| SFX | −15 to −20 dB |
| Master integrated loudness | **−14 LUFS** (YouTube target) |
| True peak | **−1 dBTP** |

---

## Narration

### Sentence patterns

- Past-tense memoirist: *"It was the year 1347. The ship that docked at Messina — its sailors were already dead."*
- Date + place anchors at scene-openers.
- Named-individual zoom every 60–90 sec: *"A scholar named Gabriele de' Mussi recorded what happened next."*
- Mortality stats with sources: *"By 1351, between 30 and 60 percent of Europe was dead."*
- Mournful coda lines: *"…and so the streets of Avignon fell silent."*

### Avoid

- Second-person: "you", "imagine", "picture this"
- Direct address: "guys", "folks", "dear viewer"
- Modern-day metaphor: "imagine the internet went down"
- Moral: "this teaches us that…"
- Question: "what would you have done?"

---

## Anachronism kill list

If a scene includes any of these in the wrong era, **regenerate**:

| Anachronism | Earliest correct year | Common error |
|-------------|----------------------|--------------|
| Plague-doctor beak mask | 1619 (Charles de Lorme) | Used in Black Death 1347 scenes |
| Eyeglasses | 1286 (Italy) | Used in earlier-medieval scenes |
| Printed books | 1440 (Gutenberg) | Used in pre-1440 scribe scenes |
| Gunpowder cannon (Europe) | ~1340 | Used in Crusades / earlier scenes |
| "Yersinia pestis" in narrator's mouth | 1894 (named) | Anachronistic period naming — use "the Pestilence" / "taa'oon" |
| Modern uniform cobblestone | 19th C | Used in medieval scenes — medieval streets were rough mud + stone mix |
| Steel-cut full plate armor | ~1400 | Used in earlier scenes |
| Gothic pointed arch | post-1140 | Used in Romanesque scenes |
| Cotton plain-weave | post-1500 in Europe | Use linen / wool / hemp for medieval European costumes |
| Saffron-dyed bright orange (cheap dye) | post-Industrial | Period colors are muted natural dyes (madder, woad, weld) |

When adding a new historical event to your channel, **expand this list** for that event's era and add to the master prompt's HISTORICAL ACCURACY LOCK section.

---

## Linguistic register (per locale)

### English (default, general)

- Literary-grim
- British-RP or neutral-US
- Past-tense
- 15–25 word sentence avg
- No second-person, no direct address, no moral

### Hindi (Urdu-leaning Hindustani)

USE: taareekh, qayamat, fanaa, halaakat, azaab, tabaahi, barbaadi, marg, maut, saqoot, ehyaa, gumshudah, raat ki khaamoshi, veerana, maatam, janaaza, baashinde, saaye

AVOID: vinaash, vikaas, pratikriya, sthithi, modern English loans (event, society, system), devotional uplift (bhagwaan ki kripa, dharm ki vijay), direct address (doston, guys)

### Future locales

When adding (Spanish, Arabic, Portuguese, Mandarin), build a USE/AVOID vocabulary table aligned to grimdark literary register in that language. Submit as PR.
