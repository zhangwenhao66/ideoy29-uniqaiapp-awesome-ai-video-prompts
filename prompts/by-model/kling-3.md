# Kling 3.0 prompts

32 prompts written for Kling 3.0 (Kuaishou), grouped by use case. "Rendered" means somebody filed a report with what came out; see the README for what that does and does not mean.

[Back to the README](../../README.md) · [By model](../by-model/) · [By use case](../by-use-case/)

Contents: [Camera moves](#camera-moves) · [Product](#product) · [Portrait](#portrait) · [Nature](#nature) · [Action](#action) · [Ads](#ads) · [Anime](#anime) · [Image to video](#image-to-video)

## Camera moves

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

#### Old town rooftops, crane up

Model: `wan-2.5`, `kling-3` · Mode: `t2v` · Duration: 5 s · Aspect: 16:9 · Rendered: no report yet

```text
Terracotta rooftops of an old town at midday, laundry lines moving in a light wind, swallows crossing the frame. Camera starts at street level and cranes up slowly above the roofline to reveal the sea beyond. 28 mm lens, hard sunlight, deep shadows in the alleys.
```

**Why it works.** A crane move needs a before and an after; 'street level' to 'above the roofline' gives both. Laundry and swallows are small, cheap motions that keep a 5-second clip alive without complex physics.

<sub>id `wan-crane-up-rooftops` · tags: `crane`, `reveal`, `architecture`</sub>

#### Chrome droplet over a neon street, push in

Model: `kling-3` · Mode: `t2v` · Duration: 8 s · Aspect: 16:9 · Rendered: no report yet

```text
A giant chrome water droplet hangs over a wet neon-lit street at dusk, mist rising from the asphalt, low camera slowly pushing in. 24 mm lens, reflections of the signs in the chrome, cyan and magenta light, haze. Still, surreal mood.
```

**Why it works.** A reflective object over a wet street gives the model two mirrors to keep consistent; a slow push in from a low camera is the one move that does not break the reflection. This text describes a real Kling 3.0 clip (8 s) that is the featured sample on the UniqAI video page; the exact prompt that produced that clip was not published, so the entry is not marked as rendered.

<sub>id `kling-chrome-droplet-neon-street` · tags: `push-in`, `surreal`, `night`</sub>

## Product

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

## Portrait

#### Studio portrait, blink and smile

Model: `kling-3` · Mode: `t2v` · Duration: 5 s · Aspect: 16:9 · Rendered: no report yet

```text
An adult woman with short grey hair in a charcoal turtleneck looking into the lens, a slow blink and a small smile forming. Static camera, head and shoulders. 85 mm lens, one large soft light from camera left, mid-grey backdrop, natural skin texture. Calm editorial mood.
```

**Why it works.** A blink and a forming smile are the smallest motions a face can make, and the ones models render without warping. The static camera keeps all the attention on them.

Follows: [Kuaishou, Kling AI text-to-video prompt guide](https://kling.ai/quickstart/text-to-video-prompt-guide), checked 2025-11-24.

<sub>id `kling-studio-portrait-blink` · tags: `static-camera`, `studio`, `micro-motion`</sub>

#### Golden hour, push in to close-up

Model: `kling-3` · Mode: `t2v` · Duration: 5 s · Aspect: 16:9 · Rendered: no report yet

```text
An adult man with a short beard standing in a wheat field at golden hour, wind moving his hair and the stalks around him. Slow push in from a medium shot to a close-up. 135 mm lens, low sun behind him with gentle lens flare, creamy bokeh. Warm, nostalgic atmosphere.
```

**Why it works.** Wind in hair and wheat does the work; the push in from medium shot to close-up is slow enough that the face stays consistent. Lens flare is named so the model does not treat it as an error.

Follows: [Kuaishou, Kling AI text-to-video prompt guide](https://kling.ai/quickstart/text-to-video-prompt-guide), checked 2025-11-24.

<sub>id `kling-golden-hour-push-in` · tags: `push-in`, `golden-hour`, `wind`</sub>

#### Dancer, track forward

Model: `kling-3` · Mode: `t2v` · Duration: 5 s · Aspect: 16:9 · Rendered: no report yet

```text
A dancer in a loose white shirt turning once, slowly, in an empty rehearsal studio, the fabric following the turn. Slow track forward toward the dancer, stable camera. 35 mm lens, daylight from tall windows, dust in the air. Light, graceful mood.
```

**Why it works.** One slow turn in a loose shirt: the fabric follows and sells the motion. Fast dance is where limbs break; a single turn is where they do not.

Follows: [Kuaishou, Kling AI text-to-video prompt guide](https://kling.ai/quickstart/text-to-video-prompt-guide), checked 2025-11-24.

<sub>id `kling-dancer-track-forward` · tags: `track`, `dance`, `fabric`</sub>

#### Rain on a window, portrait behind it

Model: `wan-2.5`, `kling-3` · Mode: `t2v` · Duration: 5 s · Aspect: 16:9 · Rendered: no report yet

```text
A man in his thirties with short dark hair seen through a rain-streaked café window, looking down at a notebook, raindrops running down the glass in the foreground. Static camera, medium shot, focus on the face with the drops softly out of focus. 85 mm lens, grey overcast daylight, warm lamp inside. Thoughtful, quiet mood.
```

**Why it works.** The foreground rain supplies constant motion while the subject stays nearly still, which is the easiest kind of portrait clip to get right. Focus is stated explicitly so the drops do not steal the shot.

<sub>id `wan-portrait-rain-window` · tags: `rain`, `static-camera`, `foreground`</sub>

## Nature

#### Mountain lake at sunrise, static wide

Model: `kling-3` · Mode: `t2v` · Duration: 5 s · Aspect: 16:9 · Rendered: no report yet

```text
A mountain lake at sunrise with thin mist drifting across the surface and mirror reflections of snow peaks. Static camera, wide shot. 24 mm lens, soft pink and gold morning light, a touch of lens flare on the ridge. Serene, cold-morning atmosphere.
```

**Why it works.** Drifting mist and a mirror reflection are two slow, large-scale motions that read well in a wide static shot. The pink-gold light names a palette so the model does not default to noon.

Follows: [Kuaishou, Kling AI text-to-video prompt guide](https://kling.ai/quickstart/text-to-video-prompt-guide), checked 2025-11-24.

<sub>id `kling-mountain-lake-sunrise` · tags: `static-camera`, `mist`, `reflection`</sub>

#### Coastal dune, tilt down

Model: `kling-3` · Mode: `t2v` · Duration: 5 s · Aspect: 16:9 · Rendered: no report yet

```text
Tall grass on a coastal dune bending in gusts of wind, grey waves rolling in behind it. Slow tilt down from the clouds to the grass. 50 mm lens, overcast silver light, muted palette. Moody, wild atmosphere.
```

**Why it works.** Tilt down from clouds to grass gives the move a start and an end. Grass bending in gusts is a texture motion the model renders well; waves behind add depth.

Follows: [Kuaishou, Kling AI text-to-video prompt guide](https://kling.ai/quickstart/text-to-video-prompt-guide), checked 2025-11-24.

<sub>id `kling-coastal-dune-tilt-down` · tags: `tilt`, `wind`, `overcast`</sub>

#### Autumn pond, push in

Model: `kling-3` · Mode: `t2v` · Duration: 5 s · Aspect: 16:9 · Rendered: no report yet

```text
Autumn leaves falling slowly from a maple tree onto a still forest pond, ripples spreading where they land. Slow push in toward the water. 85 mm lens, soft backlit afternoon sun with rays through the branches, amber and rust palette. Gentle, melancholic mood.
```

**Why it works.** Falling leaves plus spreading ripples is cause and effect in one frame, which makes the physics legible. Backlit rays through branches are named to justify the warm palette.

Follows: [Kuaishou, Kling AI text-to-video prompt guide](https://kling.ai/quickstart/text-to-video-prompt-guide), checked 2025-11-24.

<sub>id `kling-autumn-pond-push-in` · tags: `push-in`, `leaves`, `backlight`</sub>

#### Tide pool, macro

Model: `wan-2.5`, `kling-3` · Mode: `t2v` · Duration: 5 s · Aspect: 16:9 · Rendered: no report yet

```text
A tide pool at low tide: a red anemone slowly opening its tentacles, small bubbles rising, sunlight rippling on the sandy bottom. Static camera, macro, anemone centred. 100 mm macro lens, bright overhead daylight, caustic light patterns. Calm, curious mood.
```

**Why it works.** Caustics and an opening anemone are both slow and continuous, so nothing has to start or stop inside the clip. 'Static camera' keeps the macro focus from hunting.

<sub>id `wan-tide-pool-macro` · tags: `macro`, `water`, `static-camera`</sub>

## Action

#### Cyclist in the rain, tracking shot

Model: `kling-3` · Mode: `t2v` · Duration: 5 s · Aspect: 16:9 · Rendered: no report yet

```text
A cyclist in a yellow rain jacket riding through a city street at night, the tyres throwing up spray. Tracking shot alongside at the same speed, stable camera. 35 mm lens, wet reflections of shop signs, shallow depth of field. Energetic, cinematic mood.
```

**Why it works.** Tracking 'at the same speed' is the phrase that keeps the subject in frame; without it the model lets the cyclist outrun the camera. Spray and wet reflections give motion cues on every frame.

Follows: [Kuaishou, Kling AI text-to-video prompt guide](https://kling.ai/quickstart/text-to-video-prompt-guide), checked 2025-11-24.

<sub>id `kling-cyclist-rain-tracking` · tags: `tracking`, `night`, `rain`</sub>

#### Wok flame, static camera

Model: `kling-3` · Mode: `t2v` · Duration: 5 s · Aspect: 16:9 · Rendered: no report yet

```text
A chef tossing vegetables in a wok, a flame flaring once and settling. Static camera, medium shot, slight slow motion. 50 mm lens, warm overhead kitchen light with the fire as the key light, steam and sparks. Intense, lively atmosphere.
```

**Why it works.** The flame 'flaring once and settling' is a single event the model can time. Using the fire as the key light ties the lighting to the action, so highlights move with the flame.

Follows: [Kuaishou, Kling AI text-to-video prompt guide](https://kling.ai/quickstart/text-to-video-prompt-guide), checked 2025-11-24.

<sub>id `kling-wok-flame-static` · tags: `static-camera`, `slow-motion`, `fire`</sub>

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

#### Portrait photo: blink and breeze

Model: `kling-3` · Mode: `i2v` · Duration: 5 s · Aspect: 16:9 · Rendered: no report yet

```text
The person blinks and smiles slightly, hair moving in a light breeze. Static camera.
```

**Why it works.** For a photo input the prompt only names the motion; the image already holds the subject, light and framing. Blink, small smile and moving hair are the three motions that keep a face intact.

Follows: [Kuaishou, Kling AI image-to-video guide](https://kling.ai/quickstart/image-to-video-guide), checked 2025-11-24.

<sub>id `kling-i2v-portrait-blink-breeze` · tags: `portrait`, `static-camera`, `micro-motion`</sub>

#### Table or still-life photo: steam and flame

Model: `kling-3` · Mode: `i2v` · Duration: 5 s · Aspect: 16:9 · Rendered: no report yet

```text
Steam rises from the cup and the candle flame flickers. Slow push in.
```

**Why it works.** Steam and a flickering flame are additive motions that do not move the objects themselves, so the composition of the photo survives the clip.

Follows: [Kuaishou, Kling AI image-to-video guide](https://kling.ai/quickstart/image-to-video-guide), checked 2025-11-24.

<sub>id `kling-i2v-still-life-steam` · tags: `still-life`, `push-in`, `steam`</sub>

#### Landscape photo: clouds and ripples, pan

Model: `kling-3` · Mode: `i2v` · Duration: 5 s · Aspect: 16:9 · Rendered: no report yet

```text
Clouds drift slowly across the sky and the water ripples. Slow pan right.
```

**Why it works.** Clouds and water are the motions a landscape photo already implies. A slow pan on a wide still gives the model room to out-paint a little without inventing new objects.

Follows: [Kuaishou, Kling AI image-to-video guide](https://kling.ai/quickstart/image-to-video-guide), checked 2025-11-24.

<sub>id `kling-i2v-landscape-clouds-pan` · tags: `landscape`, `pan`, `water`</sub>

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
