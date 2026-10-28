# Model notes: how each model reads a prompt

What each model family expects, with the vendor page each note follows and the date it was checked. Where no vendor page could be checked, the note says so. Version names move fast; the `models` keys in `data/` are families, not exact build numbers.

| Key | Model | Clip length used here | Audio | Guide followed |
|:---|:---|:---|:---|:---|
| `kling-3` | Kling 3.0 (Kuaishou) | 5 s (8 s where noted) | no | Kuaishou text-to-video guide (2025-11-24), camera control guide (2026-08-13), image-to-video guide (2025-11-24) |
| `veo-3` | Veo 3 (Google) | 8 s | yes, synced | Google Cloud Veo prompt guide (page updated 2026-10-26) |
| `wan-2.5` | Wan 2.5 (Alibaba) | 5 s | yes | Alibaba Cloud Model Studio video generation page (updated 2026-10-11): Wan 2.5 fixed 5 s clips, audio supported; later Wan versions allow longer clips |
| `runway-gen-4` | Runway Gen-4 family | 5 s | no | none cited: Runway's help-centre prompting guide returned 403 when this list was built; entries follow general practice |
| `seedance-2` | Seedance 2.x (ByteDance) | 10 s | not claimed here | ByteDance Seed Seedance page (checked 2026-10-28): native multi-shot narrative, directed camera movement |
| `flux` | Flux (Black Forest Labs) | still | – | none cited; photographic vocabulary entries |
| `nano-banana` | Nano Banana (Google Gemini image) | still / edit | – | none cited; edit entries lock identity and framing in plain words |
| `gpt-image` | GPT Image (OpenAI) | still / edit | – | none cited; the `stills` entries were rendered on this family for the UniqAI site (see `rendered_on`) |

## Kling 3.0

Kuaishou's text-to-video guide breaks a prompt into **subject + description, the subject's movement, scene + description**, and three optional parts: **camera language, lighting, atmosphere**. It asks for simple words and short sentences, movement "straightforward and suitable for a 5-second video", and warns that the model is "not sensitive to numbers" and that complex physics (a bouncing ball) is hard.

The camera control guide names the moves the entries use: **push in, pull back, pan left/right, tilt up/down, track forward, orbit, static camera**. Rule the whole list follows: **one main camera move per clip**, with a speed and a stability word ("slow, stable push in, no sudden motion").

Practical consequences:

- Describe what should stay still instead of writing a negative prompt; many Kling front-ends expose no negative field.
- Give one motion with an end state ("the flame flares once and settles") so the model can time it.
- For image-to-video, write only the motion; the photo already holds subject, light and framing.

Sources: https://kling.ai/quickstart/text-to-video-prompt-guide (2025-11-24), https://kling.ai/blog/kling-ai-camera-control-video-guide (2026-08-13), https://kling.ai/quickstart/image-to-video-guide (2025-11-24).

## Veo 3

Google's Veo prompt guide lists these elements: **subject, action, scene/context, camera angles, camera movements, lens and optical effects, visual style (lighting, tone, artistic style, ambiance), temporal elements, cinematic terms, negative prompts**. On audio it says to **clearly specify if you want audio**, in **separate sentences** for sound effects, ambient noise and dialogue; its dialogue example uses **"says:"** phrasing.

How the entries apply it:

- Visual sentences first, then `Audio: …` as its own sentence listing each sound.
- Dialogue as `She says: "one short line."` Keep it to one line per 8 s clip.
- End with `No music` (and `no captions` for ad footage) unless you want them; otherwise Veo tends to add a score.
- Audio can follow the visual order (strike, then thunder, then rain) when the prompt states that order.

Source: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/video/video-gen-prompt-guide (page updated 2026-10-26).

## Wan 2.5

Alibaba's Model Studio page lists Wan 2.5 with **fixed 5-second clips and audio support**; Wan 2.6 and 2.7 allow 2–15 s and Wan 3.0 up to 30 s. The page gives no prompt-writing guidance, so the Wan entries use the same subject → setting → one move → lens/light → mood order as Kling, which transfers without change. For sound, use the Veo pattern (own sentence, explicit list) and expect less control than Veo gives.

Source: https://www.alibabacloud.com/help/en/model-studio/video-generation (updated 2026-10-11).

## Runway Gen-4 family

No vendor guide is cited: Runway's help centre refused the fetch (HTTP 403) on 2026-10-28. The Runway entries therefore stick to what every model renders reliably: a **static or single simple camera**, **one subject motion that enters and exits the frame**, and a plain description of the look. Treat these as starting points and report what you see.

## Seedance 2.x

The ByteDance Seed page describes **native multi-shot narrative video** (several connected shots in one generation) and a rich set of **directable camera movements**. The entries use `Shot 1: … Shot 2: …` labels, keep **clothing, lens and light identical across shots**, and change angle rather than scene between shots so continuity holds. Audio is not claimed here.

Source: https://seed.bytedance.com/en/seedance (checked 2026-10-28; the page's leaderboard data is dated 2025-06-09).

## Image models (Flux, Nano Banana, GPT Image)

The `stills` entries were written as photography briefs: **lens and aperture, one named key light and its direction, the shadow it makes, backdrop, palette**, and for portraits an explicit **"visible pores, no retouched plastic look"**. Edit prompts (`i2i`) are mostly a list of what must not change (face, hair, framing, crop). These were rendered on GPT Image for the UniqAI site (`rendered_on` carries the date); on Flux and Nano Banana the same vocabulary is the right starting point, but no render is claimed until someone reports one. For the plastic-skin problem in depth, see the sibling repo `no-plastic`.

## What the list does not cover

Sora: OpenAI's deprecations page lists the Videos API and the `sora-2` / `sora-2-pro` models as removed on September 24, 2026 (page checked 2026-03-24 by the UniqAI site). See `sora-alternatives.md` for running the same prompts elsewhere. Luma, Pika, Hailuo and Higgsfield are not in the list yet; PRs with cited guides are welcome.
