# Vocabulary: words the models respond to

Short, concrete terms beat adjectives. "85 mm lens, one large soft light from the left, mid-grey backdrop" tells a model more than "beautiful professional lighting". Everything below is used somewhere in `data/prompts/`.

## Camera moves (one per clip)

| Term | What it renders | Use with |
|:---|:---|:---|
| static camera | no camera motion; subject motion only | product turntables, portraits, macro, anything delicate |
| push in / dolly in | camera moves toward the subject | reveals of detail, emotion, product hero |
| pull back / dolly out | camera moves away, revealing the space | establishing shots, "reveal the whole table" |
| pan left / pan right | camera turns horizontally from a fixed spot | landscapes, following a walking subject |
| tilt up / tilt down | camera turns vertically from a fixed spot | tall subjects (ridge, mecha), sky-to-ground |
| track forward / tracking shot alongside | camera travels with the subject | cyclists, horses, dancers; add "at the same speed" |
| orbit / quarter orbit | camera circles the subject | rigid objects; quarter turn hides the far side |
| crane up | camera rises, usually revealing a wider view | rooftops, crowds |
| handheld, slight shake | deliberate instability | UGC ads, chases, documentary feel |
| low angle / high angle / 45-degree from above | fixed viewpoint, not a move | pair with "static camera" |

Modifiers that keep moves stable: **slow**, **stable**, **no sudden motion**, **at the same speed**, **subject centred**.

## Lenses and optics

| Term | Effect |
|:---|:---|
| 20–24 mm | wide, exaggerated depth, architecture and landscapes |
| 35 mm | natural wide, street, tracking shots |
| 50 mm | neutral, "as the eye sees" |
| 85 mm | portraits, product, compressed background |
| 100–135 mm, macro | tight product detail, water drops, dials |
| anamorphic | oval bokeh, horizontal flare, cinematic look |
| f/1.8–f/2.8 | shallow depth of field, creamy background |
| f/5.6–f/8 | more in focus, catalogue product |
| lens flare, light bloom | name them so they are not treated as errors |

## Light

| Term | Effect |
|:---|:---|
| one large soft light from camera left | the default flattering key; say the side |
| softbox / octabox / ring light | names the quality of the key |
| rim light behind, thin | separates subject from a dark background |
| backlight / low sun behind the subject | golden-hour silhouette edge; add a fill or reflector for the face |
| practical light | a lamp or sign that is in the shot |
| Rembrandt light | single window side light, triangle on the shadow cheek |
| overcast silver light / open shade | soft, even, no squinting |
| cool blue key with warm rim | the two-colour product look |
| cyan and magenta signage | the neon night look |

## Motion words that render well

- **Micro-motion** on people: a blink, a small smile forming, hair moving in a light breeze, a slow turn.
- **Texture motion**: grass in gusts, fabric billowing, laundry lines, drifting dust, rising steam, mist drifting, ripples spreading.
- **Periodic motion**: a lighthouse beam rotating, a second hand ticking, a candle flickering, a blinking light.
- **One event with an end**: a flame flares once and settles, a drop runs down the glass, a lid opens, a skateboarder passes and exits frame.
- **Avoid**: counted repetitions, bouncing or colliding objects, fast limb motion toward the camera, readable text, logos, screens with interfaces.

## Mood and finish

Say it last and keep it to three or four words: "calm editorial mood", "energetic, cinematic", "quiet, premium", "nostalgic, warm". Name palettes in colour words (amber and rust; honey and ochre; teal and magenta) rather than film-stock names when you need consistency across re-runs.

## Audio (Veo 3, Wan 2.5)

`Audio:` as its own sentence, then a list: wind, surf, room tone, a clink, a mechanical whir. Dialogue as `He says: "…"`, one short line. Close with `No music` unless you want a score, and `no voices` in public places unless you want chatter.

## Image-to-video

Describe **only the motion**, then **lock the rest**: "Keep the framing, background, camera position and art style exactly as in the photo." For illustrations add "keep the character design exactly as in the image". One camera move at most, usually "static camera" or "slow push in".
