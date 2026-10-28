# Camera moves prompts

9 prompts for camera moves, grouped by the model each one was written for first (other models it suits are listed on the entry).

[Back to the README](../../README.md) · [By model](../by-model/) · [By use case](../by-use-case/)

Contents: [Written first for Kling 3.0](#written-first-for-kling-30) · [Written first for Veo 3](#written-first-for-veo-3) · [Written first for Wan 2.5](#written-first-for-wan-25) · [Written first for Runway Gen-4 family](#written-first-for-runway-gen-4-family)

## Written first for Kling 3.0

#### Brass compass, push in

Model: `kling-3` · Mode: `t2v` · Duration: 5 s · Aspect: 16:9 · Rendered: no report yet

```text
A brass compass lying open on a weathered paper map, the needle swinging once and settling. Slow, stable push in on the compass face. 85 mm macro lens, warm lamp light from the right, shallow depth of field. Quiet, focused mood, no sudden motion.
```

**Why it works.** Subject, one small motion (the needle settles), one camera move, then lens and light: the order Kuaishou's guide asks for. The needle gives the model something to animate inside a static scene, so the push in reads as intentional rather than as drift.

Follows: [Kuaishou, Kling AI camera control video guide](https://kling.ai/blog/kling-ai-camera-control-video-guide), checked 2026-08-13.

<sub>id `kling-push-in-compass` · tags: `push-in`, `macro`, `still-life`</sub>

#### Lit candle, pull back

Model: `kling-3` · Mode: `t2v` · Duration: 5 s · Aspect: 16:9 · Rendered: no report yet

```text
A single lit candle on a long oak dining table in an empty hall, the flame flickering gently. Slow pull back that reveals the whole table and the tall windows behind it. Wide 24 mm lens, cool moonlight through the windows against the warm candle glow. Still, solemn atmosphere.
```

**Why it works.** A pull back is a reveal, so the prompt names what gets revealed (table, windows). Warm flame against cool moonlight gives the model two light sources to keep consistent as the frame widens.

Follows: [Kuaishou, Kling AI camera control video guide](https://kling.ai/blog/kling-ai-camera-control-video-guide), checked 2026-08-13.

<sub>id `kling-pull-back-candle` · tags: `pull-back`, `reveal`, `interior`</sub>

#### Harbour boats, pan left

Model: `kling-3` · Mode: `t2v` · Duration: 5 s · Aspect: 16:9 · Rendered: no report yet

```text
A row of small fishing boats moored in a harbour at dawn, rocking slightly on the water. Slow, stable pan left across the boats to the lighthouse, no sudden motion. 35 mm lens, pale morning mist, low sun just above the horizon. Peaceful, unhurried mood.
```

**Why it works.** The pan has a start (boats) and an end point (lighthouse), which keeps the move from wandering. 'No sudden motion' and 'stable' are the stability words Kuaishou's camera guide recommends.

Follows: [Kuaishou, Kling AI camera control video guide](https://kling.ai/blog/kling-ai-camera-control-video-guide), checked 2026-08-13.

<sub>id `kling-pan-harbour` · tags: `pan`, `dawn`, `water`</sub>

#### Hiker on a ridge, tilt up

Model: `kling-3` · Mode: `t2v` · Duration: 5 s · Aspect: 16:9 · Rendered: no report yet

```text
An adult hiker standing still at the edge of a mountain ridge, wind moving the jacket. Slow tilt up from the boots on the rock to the peaks and the sky. 28 mm lens, soft overcast daylight, crisp detail on the rock. Open, airy mood.
```

**Why it works.** Tilt is described as a path from boots to peaks, so the model knows both the start frame and the end frame. The hiker stands still; only wind and camera move, which Kling renders cleanly.

Follows: [Kuaishou, Kling AI camera control video guide](https://kling.ai/blog/kling-ai-camera-control-video-guide), checked 2026-08-13.

<sub>id `kling-tilt-up-hiker` · tags: `tilt`, `landscape`, `wind`</sub>

#### Bronze horse, orbit

Model: `kling-3` · Mode: `t2v` · Duration: 5 s · Aspect: 16:9 · Rendered: no report yet

```text
A bronze sculpture of a horse on a plinth in a bright gallery, dust drifting in the light. Slow orbit around the sculpture, stable camera. 50 mm lens, skylight from above, soft reflections on the bronze. Calm museum atmosphere.
```

**Why it works.** An orbit around a rigid object is the easiest orbit to get right: no limbs to deform. Drifting dust is the only secondary motion, so the clip does not fight itself.

Follows: [Kuaishou, Kling AI camera control video guide](https://kling.ai/blog/kling-ai-camera-control-video-guide), checked 2026-08-13.

<sub>id `kling-orbit-bronze-horse` · tags: `orbit`, `gallery`, `sculpture`</sub>

#### Chrome droplet over a neon street, push in

Model: `kling-3` · Mode: `t2v` · Duration: 8 s · Aspect: 16:9 · Rendered: no report yet

```text
A giant chrome water droplet hangs over a wet neon-lit street at dusk, mist rising from the asphalt, low camera slowly pushing in. 24 mm lens, reflections of the signs in the chrome, cyan and magenta light, haze. Still, surreal mood.
```

**Why it works.** A reflective object over a wet street gives the model two mirrors to keep consistent; a slow push in from a low camera is the one move that does not break the reflection. This text describes a real Kling 3.0 clip (8 s) that is the featured sample on the UniqAI video page; the exact prompt that produced that clip was not published, so the entry is not marked as rendered.

<sub>id `kling-chrome-droplet-neon-street` · tags: `push-in`, `surreal`, `night`</sub>

## Written first for Veo 3

#### Lighthouse at dusk, dolly in with sound

Model: `veo-3` · Mode: `t2v` · Duration: 8 s · Aspect: 16:9 · Rendered: no report yet

```text
A white lighthouse on a rocky headland at dusk, its beam starting to rotate. Slow dolly in from a wide shot toward the lamp room, stable camera. 35 mm lens, last light on the clouds, sea spray in the air. Audio: wind over the rocks, distant waves, the low hum of the lamp mechanism. No music.
```

**Why it works.** Veo's guide asks for audio in its own sentence, separate from the visuals; 'No music' prevents the default score. The beam rotating gives a periodic motion that stays readable over the whole dolly.

Follows: [Google Cloud, Veo video generation prompt guide](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/video/video-gen-prompt-guide), checked 2026-10-26.

<sub>id `veo-dolly-in-lighthouse-audio` · tags: `dolly-in`, `audio`, `dusk`</sub>

## Written first for Wan 2.5

#### Old town rooftops, crane up

Model: `wan-2.5`, `kling-3` · Mode: `t2v` · Duration: 5 s · Aspect: 16:9 · Rendered: no report yet

```text
Terracotta rooftops of an old town at midday, laundry lines moving in a light wind, swallows crossing the frame. Camera starts at street level and cranes up slowly above the roofline to reveal the sea beyond. 28 mm lens, hard sunlight, deep shadows in the alleys.
```

**Why it works.** A crane move needs a before and an after; 'street level' to 'above the roofline' gives both. Laundry and swallows are small, cheap motions that keep a 5-second clip alive without complex physics.

<sub>id `wan-crane-up-rooftops` · tags: `crane`, `reveal`, `architecture`</sub>

## Written first for Runway Gen-4 family

#### Handheld follow through a corridor

Model: `runway-gen-4`, `seedance-2` · Mode: `t2v` · Duration: 5 s · Aspect: 16:9 · Rendered: no report yet

```text
Handheld camera following close behind a person in a long coat walking fast down a hospital corridor, fluorescent lights passing overhead, slight camera shake, doors sliding past on both sides. 24 mm lens, cool green-white light, shallow depth of field on the coat.
```

**Why it works.** 'Handheld' and 'slight shake' are a deliberate choice, not a defect, so the prompt says so. Repeating elements (lights, doors) make the forward motion visible even when the subject fills the frame.

<sub>id `runway-handheld-follow-corridor` · tags: `handheld`, `follow`, `interior`</sub>

---

Prompts are CC BY 4.0, attribution "UniqAI, https://github.com/uniqaiapp/awesome-ai-video-prompts". Generated by `scripts/build.py`; edit `data/prompts/*.json`, not this file.
