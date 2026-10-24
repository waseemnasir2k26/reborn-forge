# reborn-forge

Every AI video niche needs its own master prompt, and writing one by hand takes days. Reborn Forge builds it for you: give it a niche and a reference YouTube video, and it returns a reusable master prompt for that niche, which you then feed one title at a time.

## What it does

- Takes `NICHE` and `YOUTUBE_URL` (plus target tool, duration, language, and whether you want a script).
- Runs a five-step reverse-engineering pass: niche intelligence, video analysis, pattern engine, prompt architect, output compiler (`agents/01` to `agents/05`).
- Returns one niche-locked master prompt with 33 sections: priority order, variation engine, stage progression, audio and lighting systems, scene JSON schema, anti-fail rules, style lock.
- Lets you reuse that master prompt for every topic in the niche. New video means a new TITLE, not a new prompt.
- Includes examples (mansion restoration, luxury watch restoration, Pompeii, Great Fire of London and others in `examples/`) and previously generated prompts in `outputs/generated/`.

## Quickstart

1. Open `META-PROMPT.md` and copy the whole file.
2. Paste it into Claude, GPT or Gemini.
3. Fill the INPUT block at the bottom:

```
NICHE: luxury watch restoration
YOUTUBE_URL: https://youtube.com/watch?v=xxxxx
TARGET_TOOL: VEO3
DURATION: longform
LANGUAGE: English
INCLUDE_SCRIPT: no
EXTRA_NOTES: ASMR-tier, no narration first 8s
```

`INCLUDE_SCRIPT` is required: `yes` for niches that need narration (history, lore, explainers), `no` for purely visual ones (restoration, craft, ASMR).

4. Send it. You get the master prompt back.
5. Save it. For each new video, paste the master prompt plus a TITLE (and an optional reference image).

You can also install it as a Claude Code skill; see `INSTALL.md` and `SKILL.md`. Other docs: `USAGE-GUIDE.md`, `FAQ.md`, `TROUBLESHOOTING.md`, `BATCH-VIDEOS.md`, `ARCHITECTURE.md`.

## For you if

You make faceless AI video in a repeatable niche and are tired of rebuilding the prompt scaffolding for each video.

## Status and limits

- Version 2.3.0. It generates prompts only. It does not render video or call any video model.
- The quality of the result depends on the model you paste the meta-prompt into and on how well it can read the reference video. A transcript or description of the reference helps when the model cannot watch video.
- Scene-count maths in the generated prompts assumes 8-second scenes; change it if your tool differs.
- Successor to the history-only `reborn-history` prompts, which are kept under `prompts/legacy/`. See `MIGRATION-GUIDE.md`.
- Not affiliated with the reference channel credited in `reference/tim-reborn-research.md`.

## Credits

Architecture parent: `reborn-history`. Built by SkynetLabs.

## License

MIT, see [LICENSE](LICENSE).

---

Built by SkynetLabs. Contact: info@skynetjoe.com

Need this wired into your business? SkynetLabs builds voice agents, n8n back offices and sites that convert → https://skynetjoe.com
