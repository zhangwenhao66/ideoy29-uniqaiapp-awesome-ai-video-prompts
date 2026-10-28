# Flux prompts

6 prompts written for Flux (Black Forest Labs), grouped by use case. "Rendered" means somebody filed a report with what came out; see the README for what that does and does not mean.

[Back to the README](../../README.md) · [By model](../by-model/) · [By use case](../by-use-case/)

Contents: [Stills (image prompts)](#stills-image-prompts)

## Stills (image prompts)

#### Catalogue product shot: stoneware teapot

Model: `nano-banana`, `flux`, `gpt-image` · Mode: `t2i` · Aspect: 1:1 · Rendered: yes

```text
High-end catalogue product photograph of a speckled cream stoneware teapot with a bamboo handle on a seamless warm-white paper sweep; one large softbox from the left giving a single soft wrap-around shadow, subtle glaze reflections, true colours, crisp edges, 90 mm lens, f/8. Square frame, teapot centred with generous empty space.
```

**Why it works.** Everything a product photographer would set is in the prompt: one softbox, its direction, the shadow it makes, the lens and the aperture. Models respond to that vocabulary far better than to 'professional product photo'.

**Rendered on GPT Image (2026-10-24).** Rendered as a UniqAI site illustration at 1024x1024, medium quality; kept as published.

<sub>id `still-product-teapot-catalogue` · tags: `product`, `studio`, `catalogue`</sub>

#### Editorial studio portrait, real skin

Model: `flux`, `nano-banana`, `gpt-image` · Mode: `t2i` · Aspect: 3:4 · Rendered: yes

```text
Editorial studio portrait of a woman in her mid-forties with deep brown skin and short natural hair streaked with grey, wearing a charcoal merino turtleneck, calm direct gaze with the hint of a smile. 85 mm lens at f/4, one large octabox key light from camera left with a soft silver fill, neutral mid-grey seamless backdrop, true-to-life skin with visible pores and fine lines, no retouched plastic look, muted palette of charcoal, grey and warm brown. Head and shoulders in the upper two thirds of a vertical frame.
```

**Why it works.** 'Visible pores and fine lines, no retouched plastic look' is the line that fights the smooth-skin default. Lens, aperture, one key light and a fill give the model a concrete lighting diagram.

**Rendered on GPT Image (2026-10-24).** Rendered as a UniqAI site illustration at 1024x1536, medium quality; kept as published.

<sub>id `still-portrait-studio-editorial` · tags: `portrait`, `studio`, `skin-texture`</sub>

#### Golden-hour field portrait

Model: `flux`, `nano-banana`, `gpt-image` · Mode: `t2i` · Aspect: 3:4 · Rendered: yes

```text
Outdoor editorial portrait of a South Asian man in his early thirties with a short dark beard and wavy hair, wearing an open-collar oatmeal linen shirt, standing in a ripe wheat field at golden hour. 135 mm lens at f/2, low sun behind him lighting the edge of the hair and beard, a soft reflector fill on the face, gentle lens flare, creamy out-of-focus field, warm honey and ochre palette, natural skin texture with no smoothing. Head and shoulders in the upper two thirds of a vertical frame.
```

**Why it works.** Backlight plus a named reflector fill is how the face stays readable against the sun. The palette is written out (honey, ochre) so the grade is consistent across re-runs.

**Rendered on GPT Image (2026-10-24).** Rendered as a UniqAI site illustration at 1024x1536, medium quality; kept as published.

<sub>id `still-portrait-golden-hour-field` · tags: `portrait`, `golden-hour`, `backlight`</sub>

#### Neon night portrait, anamorphic

Model: `flux`, `nano-banana`, `gpt-image` · Mode: `t2i` · Aspect: 3:4 · Rendered: yes

```text
Cinematic night portrait of a Latino man in his mid-twenties with dark curly hair, a small silver hoop earring and a dark green bomber jacket, standing on a rain-wet street lit by shop signs. 50 mm anamorphic lens at f/1.8, cyan rim light on one side and magenta on the other, soft practical light on the face, rain droplets on the jacket, bokeh of blurred signs behind, teal-and-magenta film grade with natural skin texture preserved. Head and shoulders in the upper two thirds of a vertical frame.
```

**Why it works.** Two rim colours (cyan, magenta) plus a soft practical on the face is a lighting plan, not a vibe. 'Natural skin texture preserved' is restated because stylised grades push models toward plastic skin.

**Rendered on GPT Image (2026-10-24).** Rendered as a UniqAI site illustration at 1024x1536, medium quality; kept as published.

<sub>id `still-portrait-neon-night-anamorphic` · tags: `portrait`, `night`, `neon`</sub>

#### Black-and-white character study

Model: `flux`, `nano-banana`, `gpt-image` · Mode: `t2i` · Aspect: 3:4 · Rendered: yes

```text
Black-and-white character study of a man in his late sixties with a deeply lined weathered face, pale eyes and a thick white moustache, wearing a heavy wool coat with the collar up. 85 mm lens at f/2.8, Rembrandt light from a single north-facing window with a small triangle of light on the shadow cheek, near-black background, fine silver-gelatin film grain, every wrinkle and pore sharp, dignified and quiet. Head and shoulders in the upper two thirds of a vertical frame.
```

**Why it works.** Rembrandt light is named by its tell-tale triangle, so the model can place it. Silver-gelatin grain and 'every wrinkle and pore sharp' pull the result away from a smooth digital look.

**Rendered on GPT Image (2026-10-24).** Rendered as a UniqAI site illustration at 1024x1536, medium quality; kept as published.

<sub>id `still-portrait-mono-character-study` · tags: `portrait`, `black-and-white`, `rembrandt`</sub>

#### Beauty portrait, freckles kept

Model: `flux`, `nano-banana`, `gpt-image` · Mode: `t2i` · Aspect: 3:4 · Rendered: yes

```text
Beauty-editorial portrait of an East Asian woman in her mid-twenties with light freckles across the nose and cheeks, hair pulled back into a low bun, wearing a cream ribbed knit, minimal makeup with a hint of gloss. 100 mm macro lens at f/5.6, a large ring-shaped soft light straight on with a white bounce under the chin, pale blush-pink seamless backdrop, crisp catchlights, skin that keeps real pores, peach fuzz and texture, soft pastel palette. Head and shoulders in the upper two thirds of a vertical frame.
```

**Why it works.** Freckles and peach fuzz are named as things to keep, which is the only way to stop a beauty prompt from erasing them. A ring light with an under-chin bounce is a real setup, so the catchlights come out right.

**Rendered on GPT Image (2026-10-24).** Rendered as a UniqAI site illustration at 1024x1536, medium quality; kept as published.

<sub>id `still-portrait-beauty-freckles-macro` · tags: `portrait`, `beauty`, `skin-texture`</sub>

---

Prompts are CC BY 4.0, attribution "UniqAI, https://github.com/uniqaiapp/awesome-ai-video-prompts". Generated by `scripts/build.py`; edit `data/prompts/*.json`, not this file.
