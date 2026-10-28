<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/banner.svg">
  <source media="(prefers-color-scheme: light)" srcset="assets/banner-light.svg">
  <img alt="awesome-ai-video-prompts by UniqAI" src="assets/banner.svg" width="1280" height="320">
</picture>

[![License: CC BY 4.0](https://img.shields.io/badge/license-CC_BY_4.0-d1fe17?style=flat-square&labelColor=0d0f12)](LICENSE)
[![Claude Code skill](https://img.shields.io/badge/Claude_Code-skill-d1fe17?style=flat-square&labelColor=0d0f12)](#install)
[![Cursor](https://img.shields.io/badge/Cursor-rules-d1fe17?style=flat-square&labelColor=0d0f12)](#install)
[![Codex](https://img.shields.io/badge/Codex-AGENTS.md-d1fe17?style=flat-square&labelColor=0d0f12)](#install)
[![Made by UniqAI](https://img.shields.io/badge/made_by-UniqAI-fdfc07?style=flat-square&labelColor=0d0f12)](https://uniqai.app/?utm_source=github&utm_medium=readme&utm_campaign=awesome-ai-video-prompts)

**Curated AI video prompts for Kling 3.0, Veo 3, Wan 2.5, Runway and Seedance, with model, settings and why each one works.**

[Quickstart](#quickstart) · [The list](#the-list) · [How it works](#how-it-works) · [Examples](#examples) · [Install](#install) · [FAQ](#faq)

</div>

English · [Русский](README.ru.md) · [简体中文](README.zh-CN.md) · [Español](README.es.md) · [Português (BR)](README.pt-BR.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

# Awesome AI Video Prompts: Kling 3.0, Veo 3, Wan, Runway, Seedance

A curated list of AI video prompts (text-to-video and image-to-video) for Kling 3.0, Veo 3, Wan 2.5, Runway Gen-4 and Seedance 2.x, plus a short set of image prompts for Flux, Nano Banana and GPT Image. Every entry carries the prompt in a code block, the model it is written for, mode, duration, aspect, a note on why the structure works, and a `rendered_on` field that stays empty until someone reports a real render. The data is JSON; the Markdown pages and the counts below are generated from it.

| **Model-specific, not generic** | **Honest about results** | **Works as an agent skill** |
|:---|:---|:---|
| Each prompt follows the vendor's own guide (cited with a date): one camera move for Kling, audio in its own sentence for Veo, labelled shots for Seedance. | "Written for" and "rendered on" are separate fields. The counts in this README come from `scripts/stats.py`, not from a keyboard. | `SKILL.md` lets Claude Code, Cursor or Codex search the list and adapt the closest prompt to your shot. |

## Quickstart

```bash
git clone https://github.com/uniqaiapp/awesome-ai-video-prompts
cd awesome-ai-video-prompts
python3 scripts/find.py --model kling-3 --use-case product
```

You get the matching prompts as text, each with a `Why it works` line and whether a render has been reported. No packages to install; Python 3.9+. Browse without the terminal: [by model](prompts/by-model/) or [by use case](prompts/by-use-case/).

## Demo

<img alt="awesome-ai-video-prompts demo: searching the list with scripts/find.py and printing one entry" src="assets/demo.svg" width="820">

## What is in the list

<!-- generated:stats:start -->
| Model | Prompts written for it |
|:---|---:|
| Kling 3.0 (`kling-3`) | 32 |
| Veo 3 (`veo-3`) | 7 |
| Wan 2.5 (`wan-2.5`) | 12 |
| Runway Gen-4 family (`runway-gen-4`) | 3 |
| Seedance 2.x (`seedance-2`) | 6 |
| Flux (`flux`) | 6 |
| Nano Banana (Gemini image) (`nano-banana`) | 8 |
| GPT Image (`gpt-image`) | 8 |

| Use case | Prompts |
|:---|---:|
| Camera moves | 9 |
| Product | 6 |
| Portrait | 5 |
| Nature | 5 |
| Action | 5 |
| Ads | 4 |
| Anime | 4 |
| Image to video | 6 |
| Stills (image prompts) | 8 |

| Mode | Prompts |
|:---|---:|
| text to video (`t2v`) | 38 |
| image to video (`i2v`) | 6 |
| text to image (`t2i`) | 6 |
| image edit (`i2i`) | 2 |

52 prompts in total: 44 video, 8 image. 7 carry a render report (`rendered_on` is not empty); 45 follow a vendor prompt guide or the UniqAI library but have no render report yet.
<!-- generated:stats:end -->

## The list

One line per prompt; the link opens the full entry with the prompt text, the why-it-works note and any render reports. Model keys: `kling-3` Kling 3.0, `veo-3` Veo 3, `wan-2.5` Wan 2.5, `runway-gen-4` Runway Gen-4 family, `seedance-2` Seedance 2.x, `flux`, `nano-banana`, `gpt-image`. Modes: `t2v` text to video, `i2v` image to video, `t2i` text to image, `i2i` image edit.

<!-- generated:list:start -->
### Camera moves

- [Brass compass, push in](prompts/by-use-case/camera-moves.md#brass-compass-push-in) · kling-3 · `t2v` · 5 s
- [Lit candle, pull back](prompts/by-use-case/camera-moves.md#lit-candle-pull-back) · kling-3 · `t2v` · 5 s
- [Harbour boats, pan left](prompts/by-use-case/camera-moves.md#harbour-boats-pan-left) · kling-3 · `t2v` · 5 s
- [Hiker on a ridge, tilt up](prompts/by-use-case/camera-moves.md#hiker-on-a-ridge-tilt-up) · kling-3 · `t2v` · 5 s
- [Bronze horse, orbit](prompts/by-use-case/camera-moves.md#bronze-horse-orbit) · kling-3 · `t2v` · 5 s
- [Lighthouse at dusk, dolly in with sound](prompts/by-use-case/camera-moves.md#lighthouse-at-dusk-dolly-in-with-sound) · veo-3 · `t2v` · 8 s
- [Old town rooftops, crane up](prompts/by-use-case/camera-moves.md#old-town-rooftops-crane-up) · wan-2.5, kling-3 · `t2v` · 5 s
- [Handheld follow through a corridor](prompts/by-use-case/camera-moves.md#handheld-follow-through-a-corridor) · runway-gen-4, seedance-2 · `t2v` · 5 s
- [Chrome droplet over a neon street, push in](prompts/by-use-case/camera-moves.md#chrome-droplet-over-a-neon-street-push-in) · kling-3 · `t2v` · 8 s

[All camera moves prompts with the full text →](prompts/by-use-case/camera-moves.md)

### Product

- [Headphones on a turntable](prompts/by-use-case/product.md#headphones-on-a-turntable) · kling-3 · `t2v` · 5 s
- [Perfume bottle, macro water drop](prompts/by-use-case/product.md#perfume-bottle-macro-water-drop) · kling-3 · `t2v` · 5 s
- [Sneaker, quarter orbit](prompts/by-use-case/product.md#sneaker-quarter-orbit) · kling-3 · `t2v` · 5 s
- [Coffee pour, slow motion with sound](prompts/by-use-case/product.md#coffee-pour-slow-motion-with-sound) · veo-3 · `t2v` · 8 s
- [Watch, two connected shots](prompts/by-use-case/product.md#watch-two-connected-shots) · seedance-2 · `t2v` · 10 s
- [Skincare jar, slow rotate on marble](prompts/by-use-case/product.md#skincare-jar-slow-rotate-on-marble) · kling-3, wan-2.5 · `t2v` · 5 s

[All product prompts with the full text →](prompts/by-use-case/product.md)

### Portrait

- [Studio portrait, blink and smile](prompts/by-use-case/portrait.md#studio-portrait-blink-and-smile) · kling-3 · `t2v` · 5 s
- [Golden hour, push in to close-up](prompts/by-use-case/portrait.md#golden-hour-push-in-to-close-up) · kling-3 · `t2v` · 5 s
- [Dancer, track forward](prompts/by-use-case/portrait.md#dancer-track-forward) · kling-3 · `t2v` · 5 s
- [Portrait with one line of dialogue](prompts/by-use-case/portrait.md#portrait-with-one-line-of-dialogue) · veo-3 · `t2v` · 8 s
- [Rain on a window, portrait behind it](prompts/by-use-case/portrait.md#rain-on-a-window-portrait-behind-it) · wan-2.5, kling-3 · `t2v` · 5 s

[All portrait prompts with the full text →](prompts/by-use-case/portrait.md)

### Nature

- [Mountain lake at sunrise, static wide](prompts/by-use-case/nature.md#mountain-lake-at-sunrise-static-wide) · kling-3 · `t2v` · 5 s
- [Coastal dune, tilt down](prompts/by-use-case/nature.md#coastal-dune-tilt-down) · kling-3 · `t2v` · 5 s
- [Autumn pond, push in](prompts/by-use-case/nature.md#autumn-pond-push-in) · kling-3 · `t2v` · 5 s
- [Thunderstorm over a plain, with sound](prompts/by-use-case/nature.md#thunderstorm-over-a-plain-with-sound) · veo-3 · `t2v` · 8 s
- [Tide pool, macro](prompts/by-use-case/nature.md#tide-pool-macro) · wan-2.5, kling-3 · `t2v` · 5 s

[All nature prompts with the full text →](prompts/by-use-case/nature.md)

### Action

- [Cyclist in the rain, tracking shot](prompts/by-use-case/action.md#cyclist-in-the-rain-tracking-shot) · kling-3 · `t2v` · 5 s
- [Wok flame, static camera](prompts/by-use-case/action.md#wok-flame-static-camera) · kling-3 · `t2v` · 5 s
- [Skateboarder, low-angle pass](prompts/by-use-case/action.md#skateboarder-low-angle-pass) · runway-gen-4, seedance-2 · `t2v` · 5 s
- [Alley chase, two connected shots](prompts/by-use-case/action.md#alley-chase-two-connected-shots) · seedance-2 · `t2v` · 10 s
- [Horse galloping on a beach, side tracking](prompts/by-use-case/action.md#horse-galloping-on-a-beach-side-tracking) · wan-2.5, kling-3, veo-3 · `t2v` · 5 s

[All action prompts with the full text →](prompts/by-use-case/action.md)

### Ads

- [UGC-style handheld product talk, with disclosure](prompts/by-use-case/ads.md#ugc-style-handheld-product-talk-with-disclosure) · veo-3 · `t2v` · 8 s
- [Vertical product hero reveal](prompts/by-use-case/ads.md#vertical-product-hero-reveal) · kling-3, wan-2.5 · `t2v` · 5 s
- [App promo, three beats](prompts/by-use-case/ads.md#app-promo-three-beats) · seedance-2 · `t2v` · 10 s
- [Fabric in slow motion, space left for a logo](prompts/by-use-case/ads.md#fabric-in-slow-motion-space-left-for-a-logo) · runway-gen-4, kling-3, wan-2.5 · `t2v` · 5 s

[All ads prompts with the full text →](prompts/by-use-case/ads.md)

### Anime

- [Anime rooftop, wind and hair](prompts/by-use-case/anime.md#anime-rooftop-wind-and-hair) · wan-2.5, kling-3 · `t2v` · 5 s
- [Anime rain street, slow pan](prompts/by-use-case/anime.md#anime-rain-street-slow-pan) · kling-3, wan-2.5 · `t2v` · 5 s
- [Anime two-shot, reaction without dialogue](prompts/by-use-case/anime.md#anime-two-shot-reaction-without-dialogue) · seedance-2 · `t2v` · 10 s
- [Mecha hangar, tilt up](prompts/by-use-case/anime.md#mecha-hangar-tilt-up) · kling-3, wan-2.5 · `t2v` · 5 s

[All anime prompts with the full text →](prompts/by-use-case/anime.md)

### Image to video

- [Portrait photo: blink and breeze](prompts/by-use-case/image-to-video.md#portrait-photo-blink-and-breeze) · kling-3 · `i2v` · 5 s
- [Table or still-life photo: steam and flame](prompts/by-use-case/image-to-video.md#table-or-still-life-photo-steam-and-flame) · kling-3 · `i2v` · 5 s
- [Landscape photo: clouds and ripples, pan](prompts/by-use-case/image-to-video.md#landscape-photo-clouds-and-ripples-pan) · kling-3 · `i2v` · 5 s
- [Illustration: gentle natural motion, keep the style](prompts/by-use-case/image-to-video.md#illustration-gentle-natural-motion-keep-the-style) · kling-3, wan-2.5 · `i2v` · 5 s
- [Product photo: quarter turn with sound](prompts/by-use-case/image-to-video.md#product-photo-quarter-turn-with-sound) · veo-3 · `i2v` · 8 s
- [City photo: traffic and lights come alive](prompts/by-use-case/image-to-video.md#city-photo-traffic-and-lights-come-alive) · wan-2.5, kling-3 · `i2v` · 5 s

[All image to video prompts with the full text →](prompts/by-use-case/image-to-video.md)

### Stills (image prompts)

- [Catalogue product shot: stoneware teapot](prompts/by-use-case/stills.md#catalogue-product-shot-stoneware-teapot) · nano-banana, flux, gpt-image · `t2i` · rendered
- [Editorial studio portrait, real skin](prompts/by-use-case/stills.md#editorial-studio-portrait-real-skin) · flux, nano-banana, gpt-image · `t2i` · rendered
- [Golden-hour field portrait](prompts/by-use-case/stills.md#golden-hour-field-portrait) · flux, nano-banana, gpt-image · `t2i` · rendered
- [Neon night portrait, anamorphic](prompts/by-use-case/stills.md#neon-night-portrait-anamorphic) · flux, nano-banana, gpt-image · `t2i` · rendered
- [Black-and-white character study](prompts/by-use-case/stills.md#black-and-white-character-study) · flux, nano-banana, gpt-image · `t2i` · rendered
- [Edit: enhance a dim phone photo, change nothing else](prompts/by-use-case/stills.md#edit-enhance-a-dim-phone-photo-change-nothing-else) · nano-banana, gpt-image · `i2i` · rendered
- [Edit: selfie to business headshot, keep the face](prompts/by-use-case/stills.md#edit-selfie-to-business-headshot-keep-the-face) · nano-banana, gpt-image · `i2i`
- [Beauty portrait, freckles kept](prompts/by-use-case/stills.md#beauty-portrait-freckles-kept) · flux, nano-banana, gpt-image · `t2i` · rendered

[All stills (image prompts) prompts with the full text →](prompts/by-use-case/stills.md)

### By model

- [Kling 3.0](prompts/by-model/kling-3.md) · 32 prompts · silent clips
- [Veo 3](prompts/by-model/veo-3.md) · 7 prompts · generates audio
- [Wan 2.5](prompts/by-model/wan-2.5.md) · 12 prompts · generates audio
- [Runway Gen-4 family](prompts/by-model/runway-gen-4.md) · 3 prompts · silent clips
- [Seedance 2.x](prompts/by-model/seedance-2.md) · 6 prompts · silent clips
- [Flux](prompts/by-model/flux.md) · 6 prompts · image model
- [Nano Banana (Gemini image)](prompts/by-model/nano-banana.md) · 8 prompts · image model
- [GPT Image](prompts/by-model/gpt-image.md) · 8 prompts · image model
<!-- generated:list:end -->

## How it works

1. **One structure for every model.** Subject and what it does → setting → one camera move (or "static camera") → lens and light → mood. Kuaishou's Kling guide asks for exactly that order and for motion "suitable for a 5-second video"; Google's Veo guide lists the same elements and adds audio as its own sentence. The order is the same across models; the syntax details differ, and [`references/model-notes.md`](references/model-notes.md) lists them with the vendor page and the date it was checked.
2. **One motion, one move.** Every video prompt names a single camera move with a speed and a stability word ("slow, stable push in, no sudden motion") and one subject action that can finish in 5 to 8 seconds. Secondary motion comes from cheap, continuous things: wind in hair, steam, drifting dust, a rotating beam.
3. **Say what stays still.** Instead of a negative prompt (Kling in many front-ends has none), entries state what must not change: "static camera, product centred", or for image-to-video, "keep the framing, background and art style exactly as in the photo".
4. **Audio and multi-shot where the model supports it.** Veo entries end with `Audio: …` and `No music`; dialogue uses `She says: "…"`. Seedance entries label `Shot 1` and `Shot 2` and keep wardrobe, lens and light identical across them.
5. **The JSON is the source.** `data/prompts/<use-case>.json` holds the records, `data/schema.json` is the spec, `scripts/validate.py` enforces it, `scripts/build.py` writes `prompts/**/*.md` and the two generated sections of this README. A test fails if they drift.

```
data/prompts/*.json  ──validate.py──▶  ok
        │
        └──build.py──▶  prompts/by-model/*.md
                        prompts/by-use-case/*.md
                        README.md (stats + list sections)
```

To compare the same prompt on Kling 3.0, Veo 3 and Wan 2.5 side by side, [UniqAI runs all three from one composer](https://uniqai.app/video?utm_source=github&utm_medium=readme&utm_campaign=awesome-ai-video-prompts); any other tool that exposes these models works the same way.

## Examples

<details>
<summary><b>Vague prompt → Kling 3.0 prompt with one camera move</b></summary>

**Before**

```text
A perfume bottle, cinematic, luxury, 4k, slow motion, beautiful lighting.
```

**After** (`kling-perfume-macro-drop`)

```text
A glass bottle of amber perfume standing on wet black slate, a single water drop running down the glass. Slow push in on the bottle. 90 mm macro lens, soft backlight through the liquid, small specular highlights. Elegant, quiet atmosphere.
```

One motion (the drop), one camera move (push in), a lens, a light direction, a mood. "4k" and "cinematic" are gone; they are settings and adjectives, not instructions.

</details>

<details>
<summary><b>Sora-style prompt → Veo 3 prompt with sound</b></summary>

**Before**

```text
A golden retriever runs along a beach at sunset, cinematic, shallow depth of field.
```

**After**

```text
Tracking shot at ground level: a golden retriever runs along a wet beach at sunset, waves rolling in behind it. Shallow depth of field, warm light. Sound: surf and paws on sand.
```

The camera move is named, the motion is specific, and the sound is listed. More on moving Sora prompts in [`references/sora-alternatives.md`](references/sora-alternatives.md).

</details>

<details>
<summary><b>Photo → image-to-video prompt</b></summary>

**Before**

```text
Make this photo move.
```

**After** (`kling-i2v-portrait-blink-breeze`)

```text
The person blinks and smiles slightly, hair moving in a light breeze. Static camera.
```

For a photo the prompt describes only the motion; the picture already holds the subject, light and framing. The three motions named are the ones that keep a face intact.

</details>

<details>
<summary><b>Using it from an agent</b></summary>

```text
You: I need a vertical product reveal for earbuds, Kling, 5 seconds.
Agent (with the skill): runs python3 scripts/find.py --use-case ads --model kling-3,
  picks kling-hero-product-reveal-vertical, swaps "earbud case" details for yours,
  returns the prompt in a code block and notes that the source entry has no render report yet.
```

</details>

## Install

Works with every agent that reads instruction files. Pick yours.

<details open>
<summary><b>Claude Code</b> (as a skill)</summary>

```bash
git clone https://github.com/uniqaiapp/awesome-ai-video-prompts ~/.claude/skills/awesome-ai-video-prompts
```

Then in Claude Code type `/awesome-ai-video-prompts` or just describe the task; the skill triggers on its description. Project-local instead of global: clone into `.claude/skills/awesome-ai-video-prompts` inside your project.

As a plugin, once the uniqaiapp marketplace is published:

```
/plugin marketplace add uniqaiapp/skills
/plugin install awesome-ai-video-prompts@uniqaiapp
```

</details>

<details>
<summary><b>Cursor</b></summary>

Copy `SKILL.md`, `scripts/`, `data/`, `references/` and [`.cursor/rules/awesome-ai-video-prompts.mdc`](.cursor/rules/awesome-ai-video-prompts.mdc) into your project. The rule file embeds the skill.

</details>

<details>
<summary><b>Codex / any AGENTS.md agent</b></summary>

Copy `SKILL.md`, `scripts/`, `data/` and `references/` into `.agents/skills/awesome-ai-video-prompts/` and add the snippet from [`codex/INSTRUCTIONS.md`](codex/INSTRUCTIONS.md) to your `AGENTS.md`.

</details>

<details>
<summary><b>Without an agent</b></summary>

Every script runs standalone: `python3 scripts/find.py --help`, `python3 scripts/stats.py`, `python3 scripts/validate.py`. Or paste [`SKILL.md`](SKILL.md) into the system prompt of any model; it has no agent-specific syntax outside the frontmatter.

</details>

Requirements: Python 3.9+. No packages to install.

## Limits and honesty

- **Written for is not rendered on.** Most entries start with an empty `rendered_on`. They follow a cited vendor guide or come from the UniqAI prompt library, which is a claim about structure, not about a clip you can watch. Entries with a report say so inline; the "Report a render" issue template is how they get one.
- **The image prompts were rendered on GPT Image** for the UniqAI site (dates in `rendered_on`); for Flux and Nano Banana they are the right vocabulary, not a tested result.
- **Runway has no cited guide** in this release: Runway's help centre refused the fetch, so Runway entries follow general practice and say so.
- **Versions move.** Each `guide` carries the date it was checked. Kling 4.0 was announced in October 2026 (press release cited in `references/model-notes.md` sources); the Kling entries were written against the 3.0 guides.
- Every number in this README is produced by `python3 scripts/stats.py` on `data/prompts/`; the test suite fails if the generated block is stale or if a count appears in hand-written text.

## FAQ

<details>
<summary><b>How long should a Kling 3.0 prompt be?</b></summary>

Two to four short sentences: the subject and what it does, the setting, one camera move, then lens, light and mood. Kuaishou's guide asks for simple words and short sentences rather than a word count. A long list of competing instructions renders less predictably than one clear scene.

</details>

<details>
<summary><b>Can I use a Kling prompt on Veo 3?</b></summary>

Mostly. Add an `Audio:` sentence (Veo generates sound and will invent some if you do not), and end with `No music` unless you want a score. Veo tolerates stacked camera moves better than Kling, but one move still reads cleaner.

</details>

<details>
<summary><b>Where are the negative prompts?</b></summary>

There are none. Several front-ends expose no negative field for Kling, so the entries describe what should stay still instead: "static camera, product centred" works better than "no camera shake", and it transfers to every model.

</details>

<details>
<summary><b>Is this a Sora prompt list?</b></summary>

No. OpenAI's deprecations page lists the Sora 2 API models as removed on September 24, 2026. The structure of a Sora prompt transfers; [`references/sora-alternatives.md`](references/sora-alternatives.md) shows where each kind of prompt goes now.

</details>

<details>
<summary><b>Why JSON and not just Markdown?</b></summary>

So agents and scripts can filter by model, mode and tag, so the schema can require a "why" and a render field, and so the Markdown can never disagree with the data. The Markdown is still committed, because that is how people read an awesome list on GitHub.

</details>

## Related

- [`video-director`](https://github.com/uniqaiapp/video-director): turn a one-line idea into a shot-by-shot prompt for AI video models (Kling, Veo, Sora and others), with camera, lighting and motion vocabulary. Use it for the storyboard; use this list for the individual shots.
- [`no-plastic`](https://github.com/uniqaiapp/no-plastic): prompt rules and a checker for natural-looking AI portraits: skin texture, lighting and lens choices that avoid the plastic look.
- [`ai-video-pricing`](https://github.com/uniqaiapp/ai-video-pricing): hand-checked price table for AI video generation, per second and per clip, with source URL and check date on every row.

## Contributing

Issues and pull requests are welcome: a new prompt with its "why", a render report, or a corrected source. See [CONTRIBUTING.md](CONTRIBUTING.md) for the entry format and the local checks (`python3 tests/run.py`, no dependencies).

## License

Prompts, data and references: [CC BY 4.0](LICENSE), attribution "UniqAI, https://github.com/uniqaiapp/awesome-ai-video-prompts". Scripts and tests: [MIT](LICENSE) © UniqAI.

---

<div align="center">

<sub>Made by <a href="https://uniqai.app/?utm_source=github&utm_medium=readme&utm_campaign=awesome-ai-video-prompts">UniqAI</a>, an AI photo, video and chat app. The Kling entries are the prompt library we publish for our own users.</sub>

</div>
