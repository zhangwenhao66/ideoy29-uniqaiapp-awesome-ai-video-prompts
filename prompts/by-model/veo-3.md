# Veo 3 prompts

7 prompts written for Veo 3 (Google), grouped by use case. "Rendered" means somebody filed a report with what came out; see the README for what that does and does not mean.

[Back to the README](../../README.md) · [By model](../by-model/) · [By use case](../by-use-case/)

Contents: [Camera moves](#camera-moves) · [Product](#product) · [Portrait](#portrait) · [Nature](#nature) · [Action](#action) · [Ads](#ads) · [Image to video](#image-to-video)

## Camera moves

#### Lighthouse at dusk, dolly in with sound

Model: `veo-3` · Mode: `t2v` · Duration: 8 s · Aspect: 16:9 · Rendered: no report yet

```text
A white lighthouse on a rocky headland at dusk, its beam starting to rotate. Slow dolly in from a wide shot toward the lamp room, stable camera. 35 mm lens, last light on the clouds, sea spray in the air. Audio: wind over the rocks, distant waves, the low hum of the lamp mechanism. No music.
```

**Why it works.** Veo's guide asks for audio in its own sentence, separate from the visuals; 'No music' prevents the default score. The beam rotating gives a periodic motion that stays readable over the whole dolly.

Follows: [Google Cloud, Veo video generation prompt guide](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/video/video-gen-prompt-guide), checked 2026-10-26.

<sub>id `veo-dolly-in-lighthouse-audio` · tags: `dolly-in`, `audio`, `dusk`</sub>

## Product

#### Coffee pour, slow motion with sound

Model: `veo-3` · Mode: `t2v` · Duration: 8 s · Aspect: 16:9 · Rendered: no report yet

```text
A ceramic cup on a wooden counter, espresso pouring into it in slow motion, crema forming on the surface. Static camera, close-up, cup centred. 100 mm macro lens, warm window light from the left, dark background. Audio: the pour, a soft clink of the cup, quiet café room tone. No music, no voices.
```

**Why it works.** Slow pouring liquid is a flattering test for any model and Veo adds synced sound to it. Each audio element is listed explicitly; 'no voices' stops the model from adding chatter to a café scene.

<sub>id `veo-coffee-pour-audio` · tags: `pour`, `audio`, `slow-motion`, `food`</sub>

## Portrait

#### Portrait with one line of dialogue

Model: `veo-3` · Mode: `t2v` · Duration: 8 s · Aspect: 16:9 · Rendered: no report yet

```text
A woman in her fifties with silver hair, wearing a dark green cardigan, sitting at a kitchen table with a mug, looking just past the lens. Static camera, medium close-up. 50 mm lens, soft morning window light, warm wood tones. She says: "I never thought it would take this long." Audio: her voice, quiet kitchen room tone, a clock ticking. No music.
```

**Why it works.** Veo's guide uses 'says:' phrasing for dialogue, so the line is short and in one sentence. Looking 'just past the lens' avoids the uncanny direct-to-camera stare while keeping the face front-on.

<sub>id `veo-portrait-one-line-dialogue` · tags: `dialogue`, `audio`, `static-camera`</sub>

## Nature

#### Thunderstorm over a plain, with sound

Model: `veo-3` · Mode: `t2v` · Duration: 8 s · Aspect: 16:9 · Rendered: no report yet

```text
A storm front moving over a flat grassland, dark clouds rolling forward, a single lightning strike far on the horizon, grass flattening in the gusts. Static wide shot from a low angle. 24 mm lens, late afternoon light under the cloud edge. Audio: rising wind, distant thunder after the strike, rain starting to hit the lens at the very end. No music.
```

**Why it works.** Audio has a timeline here (strike, then thunder, then rain) and Veo can follow it when the visual order matches. Keeping the strike 'far on the horizon' avoids the over-bright flash that ruins exposure.

<sub>id `veo-thunderstorm-plain-audio` · tags: `storm`, `audio`, `wide-shot`</sub>

## Action

#### Horse galloping on a beach, side tracking

Model: `wan-2.5`, `kling-3`, `veo-3` · Mode: `t2v` · Duration: 5 s · Aspect: 16:9 · Rendered: no report yet

```text
A dark brown horse galloping along the water line of a wide beach at golden hour, hooves throwing up sand and spray, mane streaming. Tracking shot from the side at the same speed, stable camera, horse centred. 135 mm lens, low warm sun behind the horse, long shadow on the sand.
```

**Why it works.** A side-on gallop hides most of the leg-crossing errors that a front-on gallop shows. Same-speed tracking keeps the horse centred so the model is not asked to animate a changing frame.

<sub>id `wan-horse-gallop-beach` · tags: `tracking`, `animal`, `golden-hour`</sub>

## Ads

#### UGC-style handheld product talk, with disclosure

Model: `veo-3` · Mode: `t2v` · Duration: 8 s · Aspect: 9:16 · Rendered: no report yet

```text
Vertical 9:16, handheld phone look. A man in his twenties in a plain grey T-shirt holds a small blue water bottle up to the camera in a bright kitchen, turning it to show the lid. Natural daylight, slight camera wobble, close framing. He says: "Okay, this is the one I actually use." Audio: his voice, room tone, a tap of the lid. No music, no captions.
```

**Why it works.** The UGC look is a set of concrete choices: vertical, handheld wobble, daylight, plain clothes, one spoken line. The prompt asks for no captions so you can add real, honest ones in the edit. Label AI presenters as AI in the published ad; this prompt drafts footage, it does not create a real customer.

<sub>id `veo-ugc-handheld-testimonial-style` · tags: `ugc`, `vertical`, `dialogue`, `audio`</sub>

## Image to video

#### Product photo: quarter turn with sound

Model: `veo-3` · Mode: `i2v` · Duration: 8 s · Aspect: 16:9 · Rendered: no report yet

```text
The product turns a quarter turn to the left on its base, light sliding across its surface, then stops. Static camera, keep the framing and background exactly as in the photo. Audio: a soft mechanical whir while it turns, then silence. No music.
```

**Why it works.** Image-to-video on a product photo should ask for one motion with an end ('then stops') so the clip can loop or cut cleanly. The audio line gives Veo a sound that matches the only motion in the frame.

<sub>id `veo-i2v-product-photo-turn-audio` · tags: `product`, `turntable`, `audio`</sub>

---

Prompts are CC BY 4.0, attribution "UniqAI, https://github.com/uniqaiapp/awesome-ai-video-prompts". Generated by `scripts/build.py`; edit `data/prompts/*.json`, not this file.
