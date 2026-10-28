# Sora alternatives: running the same prompts elsewhere

OpenAI's API deprecations page lists the Videos API and the `sora-2` and `sora-2-pro` models as removed on September 24, 2026 (https://developers.openai.com/api/docs/deprecations, as cited by the UniqAI cost-per-second page on 2026-03-24). People arriving here with "Sora prompts" want the same clips from a model that is still running. The prompt structure transfers; the syntax details below do not.

## What changes when you move a Sora-style prompt

A typical Sora-style prompt reads:

```text
A golden retriever runs along a beach at sunset, cinematic, shallow depth of field.
```

The same idea written for the models in this list:

```text
Tracking shot at ground level: a golden retriever runs along a wet beach at sunset, waves rolling in behind it. Shallow depth of field, warm light. Sound: surf and paws on sand.
```

Three edits: the **camera move is named** (tracking, ground level), the **motion is specific** (runs along the water line, waves behind), and for an audio model the **sound is listed**. Drop the word "cinematic"; name a lens or a light instead.

## Where to take each kind of Sora prompt

| You used Sora for | Closest fit in this list | Why |
|:---|:---|:---|
| Clips with synced sound or a spoken line | `veo-3` (`prompts/by-model/veo-3.md`) | Veo generates audio from the prompt; write `Audio:` as its own sentence |
| Short silent cinematic shots, one camera move | `kling-3` | The camera-control vocabulary (push, pull, pan, tilt, orbit) is documented and reliable |
| Several shots in one generation | `seedance-2` | Native multi-shot; label shots and keep light and wardrobe constant |
| Animating a photo | `kling-3` or `wan-2.5` (`prompts/by-use-case/image-to-video.md`) | Describe the motion, lock the rest |
| Vertical ad footage | `veo-3` (with a line of dialogue) or `kling-3` (silent hero shot) | See `prompts/by-use-case/ads.md` |

## What does not transfer

- Sora-era prompts often stacked three or four camera moves. Pick one.
- "4k, 8k, masterpiece" tags do nothing useful here; durations and resolutions are set in the tool, not the prompt.
- Long story prompts (20+ seconds of events) need to be cut into 5–8 s clips (or a labelled multi-shot prompt for Seedance). The sibling repo `video-director` does that cut.

To compare the same prompt across Kling 3.0, Veo 3 and Wan 2.5 side by side, UniqAI runs all three from one composer: https://uniqai.app/video?utm_source=github&utm_medium=readme&utm_campaign=awesome-ai-video-prompts
