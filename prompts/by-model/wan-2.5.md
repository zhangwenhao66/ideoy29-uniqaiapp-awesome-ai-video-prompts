# Wan 2.5 prompts

12 prompts written for Wan 2.5 (Alibaba), grouped by use case. "Rendered" means somebody filed a report with what came out; see the README for what that does and does not mean.

[Back to the README](../../README.md) · [By model](../by-model/) · [By use case](../by-use-case/)

Contents: [Camera moves](#camera-moves) · [Product](#product) · [Portrait](#portrait) · [Nature](#nature) · [Action](#action) · [Ads](#ads) · [Anime](#anime) · [Image to video](#image-to-video)

## Camera moves

#### Old town rooftops, crane up

Model: `wan-2.5`, `kling-3` · Mode: `t2v` · Duration: 5 s · Aspect: 16:9 · Rendered: no report yet

```text
Terracotta rooftops of an old town at midday, laundry lines moving in a light wind, swallows crossing the frame. Camera starts at street level and cranes up slowly above the roofline to reveal the sea beyond. 28 mm lens, hard sunlight, deep shadows in the alleys.
```

**Why it works.** A crane move needs a before and an after; 'street level' to 'above the roofline' gives both. Laundry and swallows are small, cheap motions that keep a 5-second clip alive without complex physics.

<sub>id `wan-crane-up-rooftops` · tags: `crane`, `reveal`, `architecture`</sub>

## Product

#### Skincare jar, slow rotate on marble

Model: `kling-3`, `wan-2.5` · Mode: `t2v` · Duration: 5 s · Aspect: 16:9 · Rendered: no report yet

```text
A frosted glass skincare jar with a white lid standing on a pale marble slab, rotating slowly on a hidden turntable, a soft highlight sliding across the frosted surface. Static camera, product centred, 45-degree angle from above. 85 mm lens, large soft light from the top right, gentle shadow, blurred eucalyptus leaves far behind. Calm, clean mood.
```

**Why it works.** Frosted glass hides the fake reflections that clear glass invites. The '45-degree angle from above' line fixes the framing so the model does not drift to eye level mid-clip.

<sub>id `kling-skincare-jar-rotate` · tags: `turntable`, `beauty`, `static-camera`</sub>

## Portrait

#### Rain on a window, portrait behind it

Model: `wan-2.5`, `kling-3` · Mode: `t2v` · Duration: 5 s · Aspect: 16:9 · Rendered: no report yet

```text
A man in his thirties with short dark hair seen through a rain-streaked café window, looking down at a notebook, raindrops running down the glass in the foreground. Static camera, medium shot, focus on the face with the drops softly out of focus. 85 mm lens, grey overcast daylight, warm lamp inside. Thoughtful, quiet mood.
```

**Why it works.** The foreground rain supplies constant motion while the subject stays nearly still, which is the easiest kind of portrait clip to get right. Focus is stated explicitly so the drops do not steal the shot.

<sub>id `wan-portrait-rain-window` · tags: `rain`, `static-camera`, `foreground`</sub>

## Nature

#### Tide pool, macro

Model: `wan-2.5`, `kling-3` · Mode: `t2v` · Duration: 5 s · Aspect: 16:9 · Rendered: no report yet

```text
A tide pool at low tide: a red anemone slowly opening its tentacles, small bubbles rising, sunlight rippling on the sandy bottom. Static camera, macro, anemone centred. 100 mm macro lens, bright overhead daylight, caustic light patterns. Calm, curious mood.
```

**Why it works.** Caustics and an opening anemone are both slow and continuous, so nothing has to start or stop inside the clip. 'Static camera' keeps the macro focus from hunting.

<sub>id `wan-tide-pool-macro` · tags: `macro`, `water`, `static-camera`</sub>

## Action

#### Horse galloping on a beach, side tracking

Model: `wan-2.5`, `kling-3`, `veo-3` · Mode: `t2v` · Duration: 5 s · Aspect: 16:9 · Rendered: no report yet

```text
A dark brown horse galloping along the water line of a wide beach at golden hour, hooves throwing up sand and spray, mane streaming. Tracking shot from the side at the same speed, stable camera, horse centred. 135 mm lens, low warm sun behind the horse, long shadow on the sand.
```

**Why it works.** A side-on gallop hides most of the leg-crossing errors that a front-on gallop shows. Same-speed tracking keeps the horse centred so the model is not asked to animate a changing frame.

<sub>id `wan-horse-gallop-beach` · tags: `tracking`, `animal`, `golden-hour`</sub>

## Ads

#### Vertical product hero reveal

Model: `kling-3`, `wan-2.5` · Mode: `t2v` · Duration: 5 s · Aspect: 9:16 · Rendered: no report yet

```text
Vertical 9:16. A matte black wireless earbud case on a dark glass surface, the lid opening slowly to reveal the earbuds with a small light blinking on. Slow push in on the case, stable camera. 90 mm macro lens, one hard rim light from behind, soft fill from the front, dark background with a faint reflection. Premium, quiet mood.
```

**Why it works.** A lid opening is one mechanical motion with a clear end state, which keeps the hero shot clean. The blinking light gives a small secondary motion that reads as 'on' without text.

<sub>id `kling-hero-product-reveal-vertical` · tags: `vertical`, `push-in`, `reveal`</sub>

#### Fabric in slow motion, space left for a logo

Model: `runway-gen-4`, `kling-3`, `wan-2.5` · Mode: `t2v` · Duration: 5 s · Aspect: 16:9 · Rendered: no report yet

```text
Deep red silk fabric billowing in slow motion against a plain black background, filling the lower two thirds of the frame, the upper third left empty and dark. Static camera. 85 mm lens, one soft light from the left, rich folds and highlights, no other objects.
```

**Why it works.** Flowing fabric is a motion every current model renders well, and the prompt reserves clean space for a title or logo instead of asking the model to draw text, which it would misspell.

<sub>id `runway-fabric-slow-motion-logo-space` · tags: `slow-motion`, `fabric`, `composite-ready`</sub>

## Anime

#### Anime rooftop, wind and hair

Model: `wan-2.5`, `kling-3` · Mode: `t2v` · Duration: 5 s · Aspect: 16:9 · Rendered: no report yet

```text
2D anime style, clean line art and flat cel shading. A teenage girl in a school uniform stands on a rooftop at sunset, hair and ribbon moving in the wind, clouds drifting slowly behind her. Static camera, medium shot. Warm orange sky, soft gradient, light bloom on the horizon. Calm, nostalgic mood.
```

**Why it works.** Cel-shaded anime needs the style named first so the model commits to flat shading before it draws anything. Hair, ribbon and clouds are the classic anime 'cheap motions' that keep a still composition alive.

<sub>id `wan-anime-rooftop-wind` · tags: `cel-shading`, `wind`, `static-camera`</sub>

#### Anime rain street, slow pan

Model: `kling-3`, `wan-2.5` · Mode: `t2v` · Duration: 5 s · Aspect: 16:9 · Rendered: no report yet

```text
Anime background-art style, painterly skies and detailed buildings. A narrow Tokyo side street in heavy rain at night, a figure with a transparent umbrella walking away from the camera, neon reflections in the puddles. Slow pan right following the figure, stable. Cool blue and pink light, rain streaks visible against the signs.
```

**Why it works.** Walking away from the camera avoids the face, which is where anime generations most often break. Rain streaks and reflections give continuous motion across the whole frame.

<sub>id `kling-anime-rain-umbrella-pan` · tags: `pan`, `rain`, `night`</sub>

#### Mecha hangar, tilt up

Model: `kling-3`, `wan-2.5` · Mode: `t2v` · Duration: 5 s · Aspect: 16:9 · Rendered: no report yet

```text
Anime mecha style, detailed mechanical linework. A huge grey robot standing in a dim hangar, steam venting from its shoulder joints, warning lights blinking on the gantry. Slow tilt up from its feet to its head, stable camera. Cool blue work lights, orange glow from the eyes, haze in the air. Heavy, tense mood.
```

**Why it works.** A tilt up a tall static object is the same move as the hiker-on-a-ridge entry, applied to a different genre. Venting steam and blinking lights supply motion while the robot stays rigid and consistent.

<sub>id `kling-anime-mecha-hangar-tilt` · tags: `tilt`, `mecha`, `reveal`</sub>

## Image to video

#### Illustration: gentle natural motion, keep the style

Model: `kling-3`, `wan-2.5` · Mode: `i2v` · Duration: 5 s · Aspect: 16:9 · Rendered: no report yet

```text
Animate this illustration: gentle natural motion, hair and clothes move in a light breeze, the character blinks and turns slightly, a slow camera push-in. Keep the art style and the character design exactly as in the image.
```

**Why it works.** The last sentence is the important one: 'keep the art style and the character design exactly as in the image' is the instruction that stops an illustration from drifting toward photorealism.

<sub>id `kling-i2v-animate-illustration` · tags: `illustration`, `push-in`, `style-lock`</sub>

#### City photo: traffic and lights come alive

Model: `wan-2.5`, `kling-3` · Mode: `i2v` · Duration: 5 s · Aspect: 16:9 · Rendered: no report yet

```text
Cars move slowly through the street, their lights streaking slightly, pedestrians walk, shop signs flicker. Slow push in. Keep the buildings, the camera position and the time of day exactly as in the photo.
```

**Why it works.** A city still has obvious implied motion (traffic, people, signs), so the prompt lists it and locks everything else. 'Slightly' on the light streaks keeps the exposure from going to long-exposure trails.

<sub>id `wan-i2v-city-photo-traffic-lights` · tags: `city`, `push-in`, `crowd`</sub>

---

Prompts are CC BY 4.0, attribution "UniqAI, https://github.com/uniqaiapp/awesome-ai-video-prompts". Generated by `scripts/build.py`; edit `data/prompts/*.json`, not this file.
