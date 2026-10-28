# Seedance 2.x prompts

6 prompts written for Seedance 2.x (ByteDance), grouped by use case. "Rendered" means somebody filed a report with what came out; see the README for what that does and does not mean.

[Back to the README](../../README.md) · [By model](../by-model/) · [By use case](../by-use-case/)

Contents: [Camera moves](#camera-moves) · [Product](#product) · [Action](#action) · [Ads](#ads) · [Anime](#anime)

## Camera moves

#### Handheld follow through a corridor

Model: `runway-gen-4`, `seedance-2` · Mode: `t2v` · Duration: 5 s · Aspect: 16:9 · Rendered: no report yet

```text
Handheld camera following close behind a person in a long coat walking fast down a hospital corridor, fluorescent lights passing overhead, slight camera shake, doors sliding past on both sides. 24 mm lens, cool green-white light, shallow depth of field on the coat.
```

**Why it works.** 'Handheld' and 'slight shake' are a deliberate choice, not a defect, so the prompt says so. Repeating elements (lights, doors) make the forward motion visible even when the subject fills the frame.

<sub>id `runway-handheld-follow-corridor` · tags: `handheld`, `follow`, `interior`</sub>

## Product

#### Watch, two connected shots

Model: `seedance-2` · Mode: `t2v` · Duration: 10 s · Aspect: 16:9 · Rendered: no report yet

```text
Shot 1: a steel dive watch on wet black stone, water beading on the crystal, slow push in on the dial. Shot 2: cut to a close-up of the second hand ticking, light sweeping across the bezel. 90 mm macro lens, cool blue key light with a thin warm rim, dark background. Clean, premium mood.
```

**Why it works.** Seedance advertises native multi-shot output, so the prompt labels the shots and keeps each one to a single motion. Both shots share the lens and lighting line so the cut feels like one commercial.

Follows: [ByteDance Seed, Seedance model page (multi-shot narrative, camera movement)](https://seed.bytedance.com/en/seedance), checked 2026-10-28.

<sub>id `seedance-watch-two-shots` · tags: `multi-shot`, `macro`, `luxury`</sub>

## Action

#### Skateboarder, low-angle pass

Model: `runway-gen-4`, `seedance-2` · Mode: `t2v` · Duration: 5 s · Aspect: 16:9 · Rendered: no report yet

```text
Low-angle static camera at ground level on an empty concrete plaza at sunset; a skateboarder rolls past from left to right, close to the lens, wheels loud on the concrete, then exits frame. 20 mm wide lens, long shadows, warm backlight with lens flare. Energetic, simple.
```

**Why it works.** One subject crossing a static frame is the most reliable action shot across models: no camera move to coordinate with the motion. Entering and exiting the frame gives the clip a natural start and end.

<sub>id `runway-skateboarder-low-angle` · tags: `static-camera`, `low-angle`, `sport`</sub>

#### Alley chase, two connected shots

Model: `seedance-2` · Mode: `t2v` · Duration: 10 s · Aspect: 16:9 · Rendered: no report yet

```text
Shot 1: a woman in a yellow jacket runs through a narrow night alley toward the camera, puddles splashing, handheld camera backing away. Shot 2: cut to a high angle from a fire escape as she turns the corner under a neon sign. 35 mm lens, wet surfaces, cyan and magenta signage light, rain in the air.
```

**Why it works.** Multi-shot prompts work when both shots describe the same subject in the same clothes and light, so the model keeps continuity. The second shot changes the angle, not the scene.

<sub>id `seedance-chase-two-shots` · tags: `multi-shot`, `handheld`, `night`</sub>

## Ads

#### App promo, three beats

Model: `seedance-2` · Mode: `t2v` · Duration: 10 s · Aspect: 9:16 · Rendered: no report yet

```text
Shot 1: a hand picks up a phone from a café table, screen off, morning light. Shot 2: close-up of the same hand tapping the phone once, the screen lighting up plain white (no interface, no text). Shot 3: the person smiles and looks up at a friend arriving. 50 mm lens, warm daylight, shallow depth of field, consistent clothing and table across shots.
```

**Why it works.** Three short beats match the hook-demo-payoff rhythm of a short ad. The screen is asked to be plain white so you composite your real UI later instead of getting invented buttons and text.

<sub>id `seedance-app-promo-three-beats` · tags: `multi-shot`, `app`, `composite-ready`</sub>

## Anime

#### Anime two-shot, reaction without dialogue

Model: `seedance-2` · Mode: `t2v` · Duration: 10 s · Aspect: 16:9 · Rendered: no report yet

```text
Anime style with soft cel shading. Shot 1: a boy with messy black hair at a train window, close-up, watching the countryside pass. Shot 2: reverse angle, the girl across from him looks up from her book and smiles slightly. Afternoon train light, dust in the air, no speech, no text, consistent character design across shots.
```

**Why it works.** A shot and a reverse shot is the simplest two-shot grammar and asks nothing of lip sync. 'Consistent character design' is said out loud because multi-shot anime drifts in face shape otherwise.

<sub>id `seedance-anime-two-shot-dialogue-less` · tags: `multi-shot`, `cel-shading`, `train`</sub>

---

Prompts are CC BY 4.0, attribution "UniqAI, https://github.com/uniqaiapp/awesome-ai-video-prompts". Generated by `scripts/build.py`; edit `data/prompts/*.json`, not this file.
