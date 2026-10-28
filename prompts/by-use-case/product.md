# Product prompts

6 prompts for product, grouped by the model each one was written for first (other models it suits are listed on the entry).

[Back to the README](../../README.md) · [By model](../by-model/) · [By use case](../by-use-case/)

Contents: [Written first for Kling 3.0](#written-first-for-kling-30) · [Written first for Veo 3](#written-first-for-veo-3) · [Written first for Seedance 2.x](#written-first-for-seedance-2x)

## Written first for Kling 3.0

#### Headphones on a turntable

Model: `kling-3` · Mode: `t2v` · Duration: 5 s · Aspect: 16:9 · Rendered: no report yet

```text
A matte black pair of over-ear headphones rotating slowly on a mirrored turntable, light sweeping across the ear cups. Static camera, product centred. 100 mm lens, one soft key light from the top left and a thin rim light behind, dark grey seamless backdrop. Clean, premium mood.
```

**Why it works.** The product moves, the camera does not: a turntable rotation is a motion the model handles well, and 'static camera, product centred' replaces a negative prompt (Kling in UniqAI has no negative field).

Follows: [Kuaishou, Kling AI text-to-video prompt guide](https://kling.ai/quickstart/text-to-video-prompt-guide), checked 2025-11-24.

<sub>id `kling-headphones-turntable` · tags: `turntable`, `studio`, `static-camera`</sub>

#### Perfume bottle, macro water drop

Model: `kling-3` · Mode: `t2v` · Duration: 5 s · Aspect: 16:9 · Rendered: no report yet

```text
A glass bottle of amber perfume standing on wet black slate, a single water drop running down the glass. Slow push in on the bottle. 90 mm macro lens, soft backlight through the liquid, small specular highlights. Elegant, quiet atmosphere.
```

**Why it works.** One drop running down the glass is a single, slow, physically simple motion. Backlight through amber liquid gives the model a strong colour read on a dark surface.

Follows: [Kuaishou, Kling AI text-to-video prompt guide](https://kling.ai/quickstart/text-to-video-prompt-guide), checked 2025-11-24.

<sub>id `kling-perfume-macro-drop` · tags: `macro`, `push-in`, `glass`</sub>

#### Sneaker, quarter orbit

Model: `kling-3` · Mode: `t2v` · Duration: 5 s · Aspect: 16:9 · Rendered: no report yet

```text
A white canvas sneaker on a light grey studio sweep, the fabric laces lifting and settling as a soft breeze passes. Slow quarter-turn orbit around the shoe, stable framing. 85 mm lens, bright even softbox light with a faint ground shadow. Fresh catalogue mood.
```

**Why it works.** A quarter turn, not a full orbit, keeps the far side of the shoe out of the shot where models invent laces. The breeze on the laces is the secondary motion that makes it a video, not a slideshow.

Follows: [Kuaishou, Kling AI text-to-video prompt guide](https://kling.ai/quickstart/text-to-video-prompt-guide), checked 2025-11-24.

<sub>id `kling-sneaker-quarter-orbit` · tags: `orbit`, `catalogue`, `breeze`</sub>

#### Skincare jar, slow rotate on marble

Model: `kling-3`, `wan-2.5` · Mode: `t2v` · Duration: 5 s · Aspect: 16:9 · Rendered: no report yet

```text
A frosted glass skincare jar with a white lid standing on a pale marble slab, rotating slowly on a hidden turntable, a soft highlight sliding across the frosted surface. Static camera, product centred, 45-degree angle from above. 85 mm lens, large soft light from the top right, gentle shadow, blurred eucalyptus leaves far behind. Calm, clean mood.
```

**Why it works.** Frosted glass hides the fake reflections that clear glass invites. The '45-degree angle from above' line fixes the framing so the model does not drift to eye level mid-clip.

<sub>id `kling-skincare-jar-rotate` · tags: `turntable`, `beauty`, `static-camera`</sub>

## Written first for Veo 3

#### Coffee pour, slow motion with sound

Model: `veo-3` · Mode: `t2v` · Duration: 8 s · Aspect: 16:9 · Rendered: no report yet

```text
A ceramic cup on a wooden counter, espresso pouring into it in slow motion, crema forming on the surface. Static camera, close-up, cup centred. 100 mm macro lens, warm window light from the left, dark background. Audio: the pour, a soft clink of the cup, quiet café room tone. No music, no voices.
```

**Why it works.** Slow pouring liquid is a flattering test for any model and Veo adds synced sound to it. Each audio element is listed explicitly; 'no voices' stops the model from adding chatter to a café scene.

<sub>id `veo-coffee-pour-audio` · tags: `pour`, `audio`, `slow-motion`, `food`</sub>

## Written first for Seedance 2.x

#### Watch, two connected shots

Model: `seedance-2` · Mode: `t2v` · Duration: 10 s · Aspect: 16:9 · Rendered: no report yet

```text
Shot 1: a steel dive watch on wet black stone, water beading on the crystal, slow push in on the dial. Shot 2: cut to a close-up of the second hand ticking, light sweeping across the bezel. 90 mm macro lens, cool blue key light with a thin warm rim, dark background. Clean, premium mood.
```

**Why it works.** Seedance advertises native multi-shot output, so the prompt labels the shots and keeps each one to a single motion. Both shots share the lens and lighting line so the cut feels like one commercial.

Follows: [ByteDance Seed, Seedance model page (multi-shot narrative, camera movement)](https://seed.bytedance.com/en/seedance), checked 2026-10-28.

<sub>id `seedance-watch-two-shots` · tags: `multi-shot`, `macro`, `luxury`</sub>

---

Prompts are CC BY 4.0, attribution "UniqAI, https://github.com/uniqaiapp/awesome-ai-video-prompts". Generated by `scripts/build.py`; edit `data/prompts/*.json`, not this file.
