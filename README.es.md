<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/banner.svg">
  <source media="(prefers-color-scheme: light)" srcset="assets/banner-light.svg">
  <img alt="awesome-ai-video-prompts by UniqAI" src="assets/banner.svg" width="1280" height="320">
</picture>

[![License: CC BY 4.0](https://img.shields.io/badge/license-CC_BY_4.0-d1fe17?style=flat-square&labelColor=0d0f12)](LICENSE)
[![Claude Code skill](https://img.shields.io/badge/Claude_Code-skill-d1fe17?style=flat-square&labelColor=0d0f12)](#instalación)
[![Cursor](https://img.shields.io/badge/Cursor-rules-d1fe17?style=flat-square&labelColor=0d0f12)](#instalación)
[![Codex](https://img.shields.io/badge/Codex-AGENTS.md-d1fe17?style=flat-square&labelColor=0d0f12)](#instalación)
[![Made by UniqAI](https://img.shields.io/badge/made_by-UniqAI-fdfc07?style=flat-square&labelColor=0d0f12)](https://uniqai.app/?utm_source=github&utm_medium=readme-es&utm_campaign=awesome-ai-video-prompts)

**Prompts curados para video con IA en Kling 3.0, Veo 3, Wan 2.5, Runway y Seedance, con el modelo, los ajustes y por qué funciona cada uno.**

[Inicio rápido](#inicio-rápido) · [La lista](#la-lista) · [Cómo funciona](#cómo-funciona) · [Ejemplos](#ejemplos) · [Instalación](#instalación) · [FAQ](#faq)

</div>

[English](README.md) · [Русский](README.ru.md) · [简体中文](README.zh-CN.md) · Español · [Português (BR)](README.pt-BR.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

# Awesome AI Video Prompts: prompts para video con IA, Kling 3.0, Veo 3, Wan, Runway, Seedance

Una lista curada de prompts para video con IA (texto a video e imagen a video) para Kling 3.0, Veo 3, Wan 2.5, Runway Gen-4 y Seedance 2.x, más un conjunto corto de prompts de imagen para Flux, Nano Banana y GPT Image. Cada entrada lleva el prompt en un bloque de código, el modelo para el que fue escrito, modo, duración, relación de aspecto, una nota sobre por qué funciona la estructura y un campo `rendered_on` que permanece vacío hasta que alguien reporta un render real. Los datos están en JSON; las páginas Markdown y los conteos de abajo se generan a partir de ellos.

| **Específicos por modelo, no genéricos** | **Honestos con los resultados** | **Funciona como skill de agente** |
|:---|:---|:---|
| Cada prompt sigue la guía del propio proveedor (citada con fecha): un solo movimiento de cámara para Kling, el audio en su propia frase para Veo, planos etiquetados para Seedance. | "Escrito para" y "renderizado en" son campos separados. Los conteos de este README salen de `scripts/stats.py`, no de un teclado. | `SKILL.md` permite que Claude Code, Cursor o Codex busquen en la lista y adapten el prompt más cercano a tu plano. |

## Inicio rápido

```bash
git clone https://github.com/uniqaiapp/awesome-ai-video-prompts
cd awesome-ai-video-prompts
python3 scripts/find.py --model kling-3 --use-case product
```

Obtienes los prompts que coinciden como texto, cada uno con una línea `Why it works` y si se ha reportado un render. Nada que instalar; Python 3.9+. Para navegar sin terminal: [por modelo](prompts/by-model/) o [por caso de uso](prompts/by-use-case/).

## Demo

<img alt="awesome-ai-video-prompts demo: searching the list with scripts/find.py and printing one entry" src="assets/demo.svg" width="820">

## Qué hay en la lista

<!-- generated:stats:start -->
| Modelo | Prompts escritos para él |
|:---|---:|
| Kling 3.0 (`kling-3`) | 32 |
| Veo 3 (`veo-3`) | 7 |
| Wan 2.5 (`wan-2.5`) | 12 |
| Runway Gen-4 family (`runway-gen-4`) | 3 |
| Seedance 2.x (`seedance-2`) | 6 |
| Flux (`flux`) | 6 |
| Nano Banana (Gemini image) (`nano-banana`) | 8 |
| GPT Image (`gpt-image`) | 8 |

| Caso de uso | Prompts |
|:---|---:|
| Movimientos de cámara | 9 |
| Producto | 6 |
| Retrato | 5 |
| Naturaleza | 5 |
| Acción | 5 |
| Anuncios | 4 |
| Anime | 4 |
| Imagen a video | 6 |
| Imágenes fijas (prompts de imagen) | 8 |

| Modo | Prompts |
|:---|---:|
| texto a video (`t2v`) | 38 |
| imagen a video (`i2v`) | 6 |
| texto a imagen (`t2i`) | 6 |
| edición de imagen (`i2i`) | 2 |

52 prompts en total: 44 de video, 8 de imagen. 7 tienen un reporte de render (`rendered_on` no está vacío); 45 siguen la guía de prompts del proveedor o la biblioteca de UniqAI, pero todavía no tienen reporte de render.
<!-- generated:stats:end -->

## La lista

Una línea por prompt; el enlace abre la entrada completa con el texto del prompt, la nota de por qué funciona y los reportes de render que haya. Claves de modelo: `kling-3` Kling 3.0, `veo-3` Veo 3, `wan-2.5` Wan 2.5, `runway-gen-4` familia Runway Gen-4, `seedance-2` Seedance 2.x, `flux`, `nano-banana`, `gpt-image`. Modos: `t2v` texto a video, `i2v` imagen a video, `t2i` texto a imagen, `i2i` edición de imagen.

<!-- generated:list:start -->
### Movimientos de cámara

- [Brass compass, push in](prompts/by-use-case/camera-moves.md#brass-compass-push-in) · kling-3 · `t2v` · 5 s
- [Lit candle, pull back](prompts/by-use-case/camera-moves.md#lit-candle-pull-back) · kling-3 · `t2v` · 5 s
- [Harbour boats, pan left](prompts/by-use-case/camera-moves.md#harbour-boats-pan-left) · kling-3 · `t2v` · 5 s
- [Hiker on a ridge, tilt up](prompts/by-use-case/camera-moves.md#hiker-on-a-ridge-tilt-up) · kling-3 · `t2v` · 5 s
- [Bronze horse, orbit](prompts/by-use-case/camera-moves.md#bronze-horse-orbit) · kling-3 · `t2v` · 5 s
- [Lighthouse at dusk, dolly in with sound](prompts/by-use-case/camera-moves.md#lighthouse-at-dusk-dolly-in-with-sound) · veo-3 · `t2v` · 8 s
- [Old town rooftops, crane up](prompts/by-use-case/camera-moves.md#old-town-rooftops-crane-up) · wan-2.5, kling-3 · `t2v` · 5 s
- [Handheld follow through a corridor](prompts/by-use-case/camera-moves.md#handheld-follow-through-a-corridor) · runway-gen-4, seedance-2 · `t2v` · 5 s
- [Chrome droplet over a neon street, push in](prompts/by-use-case/camera-moves.md#chrome-droplet-over-a-neon-street-push-in) · kling-3 · `t2v` · 8 s

[Todos los prompts de movimientos de cámara con el texto completo →](prompts/by-use-case/camera-moves.md)

### Producto

- [Headphones on a turntable](prompts/by-use-case/product.md#headphones-on-a-turntable) · kling-3 · `t2v` · 5 s
- [Perfume bottle, macro water drop](prompts/by-use-case/product.md#perfume-bottle-macro-water-drop) · kling-3 · `t2v` · 5 s
- [Sneaker, quarter orbit](prompts/by-use-case/product.md#sneaker-quarter-orbit) · kling-3 · `t2v` · 5 s
- [Coffee pour, slow motion with sound](prompts/by-use-case/product.md#coffee-pour-slow-motion-with-sound) · veo-3 · `t2v` · 8 s
- [Watch, two connected shots](prompts/by-use-case/product.md#watch-two-connected-shots) · seedance-2 · `t2v` · 10 s
- [Skincare jar, slow rotate on marble](prompts/by-use-case/product.md#skincare-jar-slow-rotate-on-marble) · kling-3, wan-2.5 · `t2v` · 5 s

[Todos los prompts de producto con el texto completo →](prompts/by-use-case/product.md)

### Retrato

- [Studio portrait, blink and smile](prompts/by-use-case/portrait.md#studio-portrait-blink-and-smile) · kling-3 · `t2v` · 5 s
- [Golden hour, push in to close-up](prompts/by-use-case/portrait.md#golden-hour-push-in-to-close-up) · kling-3 · `t2v` · 5 s
- [Dancer, track forward](prompts/by-use-case/portrait.md#dancer-track-forward) · kling-3 · `t2v` · 5 s
- [Portrait with one line of dialogue](prompts/by-use-case/portrait.md#portrait-with-one-line-of-dialogue) · veo-3 · `t2v` · 8 s
- [Rain on a window, portrait behind it](prompts/by-use-case/portrait.md#rain-on-a-window-portrait-behind-it) · wan-2.5, kling-3 · `t2v` · 5 s

[Todos los prompts de retrato con el texto completo →](prompts/by-use-case/portrait.md)

### Naturaleza

- [Mountain lake at sunrise, static wide](prompts/by-use-case/nature.md#mountain-lake-at-sunrise-static-wide) · kling-3 · `t2v` · 5 s
- [Coastal dune, tilt down](prompts/by-use-case/nature.md#coastal-dune-tilt-down) · kling-3 · `t2v` · 5 s
- [Autumn pond, push in](prompts/by-use-case/nature.md#autumn-pond-push-in) · kling-3 · `t2v` · 5 s
- [Thunderstorm over a plain, with sound](prompts/by-use-case/nature.md#thunderstorm-over-a-plain-with-sound) · veo-3 · `t2v` · 8 s
- [Tide pool, macro](prompts/by-use-case/nature.md#tide-pool-macro) · wan-2.5, kling-3 · `t2v` · 5 s

[Todos los prompts de naturaleza con el texto completo →](prompts/by-use-case/nature.md)

### Acción

- [Cyclist in the rain, tracking shot](prompts/by-use-case/action.md#cyclist-in-the-rain-tracking-shot) · kling-3 · `t2v` · 5 s
- [Wok flame, static camera](prompts/by-use-case/action.md#wok-flame-static-camera) · kling-3 · `t2v` · 5 s
- [Skateboarder, low-angle pass](prompts/by-use-case/action.md#skateboarder-low-angle-pass) · runway-gen-4, seedance-2 · `t2v` · 5 s
- [Alley chase, two connected shots](prompts/by-use-case/action.md#alley-chase-two-connected-shots) · seedance-2 · `t2v` · 10 s
- [Horse galloping on a beach, side tracking](prompts/by-use-case/action.md#horse-galloping-on-a-beach-side-tracking) · wan-2.5, kling-3, veo-3 · `t2v` · 5 s

[Todos los prompts de acción con el texto completo →](prompts/by-use-case/action.md)

### Anuncios

- [UGC-style handheld product talk, with disclosure](prompts/by-use-case/ads.md#ugc-style-handheld-product-talk-with-disclosure) · veo-3 · `t2v` · 8 s
- [Vertical product hero reveal](prompts/by-use-case/ads.md#vertical-product-hero-reveal) · kling-3, wan-2.5 · `t2v` · 5 s
- [App promo, three beats](prompts/by-use-case/ads.md#app-promo-three-beats) · seedance-2 · `t2v` · 10 s
- [Fabric in slow motion, space left for a logo](prompts/by-use-case/ads.md#fabric-in-slow-motion-space-left-for-a-logo) · runway-gen-4, kling-3, wan-2.5 · `t2v` · 5 s

[Todos los prompts de anuncios con el texto completo →](prompts/by-use-case/ads.md)

### Anime

- [Anime rooftop, wind and hair](prompts/by-use-case/anime.md#anime-rooftop-wind-and-hair) · wan-2.5, kling-3 · `t2v` · 5 s
- [Anime rain street, slow pan](prompts/by-use-case/anime.md#anime-rain-street-slow-pan) · kling-3, wan-2.5 · `t2v` · 5 s
- [Anime two-shot, reaction without dialogue](prompts/by-use-case/anime.md#anime-two-shot-reaction-without-dialogue) · seedance-2 · `t2v` · 10 s
- [Mecha hangar, tilt up](prompts/by-use-case/anime.md#mecha-hangar-tilt-up) · kling-3, wan-2.5 · `t2v` · 5 s

[Todos los prompts de anime con el texto completo →](prompts/by-use-case/anime.md)

### Imagen a video

- [Portrait photo: blink and breeze](prompts/by-use-case/image-to-video.md#portrait-photo-blink-and-breeze) · kling-3 · `i2v` · 5 s
- [Table or still-life photo: steam and flame](prompts/by-use-case/image-to-video.md#table-or-still-life-photo-steam-and-flame) · kling-3 · `i2v` · 5 s
- [Landscape photo: clouds and ripples, pan](prompts/by-use-case/image-to-video.md#landscape-photo-clouds-and-ripples-pan) · kling-3 · `i2v` · 5 s
- [Illustration: gentle natural motion, keep the style](prompts/by-use-case/image-to-video.md#illustration-gentle-natural-motion-keep-the-style) · kling-3, wan-2.5 · `i2v` · 5 s
- [Product photo: quarter turn with sound](prompts/by-use-case/image-to-video.md#product-photo-quarter-turn-with-sound) · veo-3 · `i2v` · 8 s
- [City photo: traffic and lights come alive](prompts/by-use-case/image-to-video.md#city-photo-traffic-and-lights-come-alive) · wan-2.5, kling-3 · `i2v` · 5 s

[Todos los prompts de imagen a video con el texto completo →](prompts/by-use-case/image-to-video.md)

### Imágenes fijas (prompts de imagen)

- [Catalogue product shot: stoneware teapot](prompts/by-use-case/stills.md#catalogue-product-shot-stoneware-teapot) · nano-banana, flux, gpt-image · `t2i` · renderizado
- [Editorial studio portrait, real skin](prompts/by-use-case/stills.md#editorial-studio-portrait-real-skin) · flux, nano-banana, gpt-image · `t2i` · renderizado
- [Golden-hour field portrait](prompts/by-use-case/stills.md#golden-hour-field-portrait) · flux, nano-banana, gpt-image · `t2i` · renderizado
- [Neon night portrait, anamorphic](prompts/by-use-case/stills.md#neon-night-portrait-anamorphic) · flux, nano-banana, gpt-image · `t2i` · renderizado
- [Black-and-white character study](prompts/by-use-case/stills.md#black-and-white-character-study) · flux, nano-banana, gpt-image · `t2i` · renderizado
- [Edit: enhance a dim phone photo, change nothing else](prompts/by-use-case/stills.md#edit-enhance-a-dim-phone-photo-change-nothing-else) · nano-banana, gpt-image · `i2i` · renderizado
- [Edit: selfie to business headshot, keep the face](prompts/by-use-case/stills.md#edit-selfie-to-business-headshot-keep-the-face) · nano-banana, gpt-image · `i2i`
- [Beauty portrait, freckles kept](prompts/by-use-case/stills.md#beauty-portrait-freckles-kept) · flux, nano-banana, gpt-image · `t2i` · renderizado

[Todos los prompts de imágenes fijas (prompts de imagen) con el texto completo →](prompts/by-use-case/stills.md)

### Por modelo

- [Kling 3.0](prompts/by-model/kling-3.md) · 32 prompts · clips sin audio
- [Veo 3](prompts/by-model/veo-3.md) · 7 prompts · genera audio
- [Wan 2.5](prompts/by-model/wan-2.5.md) · 12 prompts · genera audio
- [Runway Gen-4 family](prompts/by-model/runway-gen-4.md) · 3 prompts · clips sin audio
- [Seedance 2.x](prompts/by-model/seedance-2.md) · 6 prompts · clips sin audio
- [Flux](prompts/by-model/flux.md) · 6 prompts · modelo de imagen
- [Nano Banana (Gemini image)](prompts/by-model/nano-banana.md) · 8 prompts · modelo de imagen
- [GPT Image](prompts/by-model/gpt-image.md) · 8 prompts · modelo de imagen
<!-- generated:list:end -->

## Cómo funciona

1. **Una estructura para todos los modelos.** Sujeto y qué hace → escenario → un movimiento de cámara (o "static camera") → lente y luz → atmósfera. La guía de Kling de Kuaishou pide exactamente ese orden y un movimiento "adecuado para un video de 5 segundos"; la guía de Veo de Google enumera los mismos elementos y añade el audio como frase propia. El orden es el mismo en todos los modelos; los detalles de sintaxis cambian, y [`references/model-notes.md`](references/model-notes.md) los enumera con la página del proveedor y la fecha en que se verificó.
2. **Un movimiento, un desplazamiento.** Cada prompt de video nombra un solo movimiento de cámara con una velocidad y una palabra de estabilidad ("slow, stable push in, no sudden motion") y una sola acción del sujeto que pueda terminar en 5 a 8 segundos. El movimiento secundario viene de cosas baratas y continuas: viento en el pelo, vapor, polvo flotando, un haz que gira.
3. **Di qué se queda quieto.** En lugar de un prompt negativo (Kling no tiene uno en muchos front-ends), las entradas indican qué no debe cambiar: "static camera, product centred", o para imagen a video, "keep the framing, background and art style exactly as in the photo".
4. **Audio y multiplano donde el modelo lo soporta.** Las entradas de Veo terminan con `Audio: …` y `No music`; el diálogo usa `She says: "…"`. Las entradas de Seedance etiquetan `Shot 1` y `Shot 2` y mantienen vestuario, lente y luz idénticos entre ambos.
5. **El JSON es la fuente.** `data/prompts/<use-case>.json` contiene los registros, `data/schema.json` es la especificación, `scripts/validate.py` la hace cumplir, `scripts/build.py` escribe `prompts/**/*.md` y las dos secciones generadas de este README. Un test falla si se desincronizan.

```
data/prompts/*.json  ──validate.py──▶  ok
        │
        └──build.py──▶  prompts/by-model/*.md
                        prompts/by-use-case/*.md
                        README.md (stats + list sections)
```

Para comparar el mismo prompt en Kling 3.0, Veo 3 y Wan 2.5 lado a lado, [UniqAI ejecuta los tres desde un solo compositor](https://uniqai.app/video?utm_source=github&utm_medium=readme-es&utm_campaign=awesome-ai-video-prompts); cualquier otra herramienta que exponga estos modelos funciona igual.

## Ejemplos

<details>
<summary><b>Prompt vago → prompt para Kling 3.0 con un solo movimiento de cámara</b></summary>

**Antes**

```text
A perfume bottle, cinematic, luxury, 4k, slow motion, beautiful lighting.
```

**Después** (`kling-perfume-macro-drop`)

```text
A glass bottle of amber perfume standing on wet black slate, a single water drop running down the glass. Slow push in on the bottle. 90 mm macro lens, soft backlight through the liquid, small specular highlights. Elegant, quiet atmosphere.
```

Un movimiento (la gota), un movimiento de cámara (push in), un lente, una dirección de luz, una atmósfera. "4k" y "cinematic" desaparecieron; son ajustes y adjetivos, no instrucciones.

</details>

<details>
<summary><b>Prompt estilo Sora → prompt para Veo 3 con sonido</b></summary>

**Antes**

```text
A golden retriever runs along a beach at sunset, cinematic, shallow depth of field.
```

**Después**

```text
Tracking shot at ground level: a golden retriever runs along a wet beach at sunset, waves rolling in behind it. Shallow depth of field, warm light. Sound: surf and paws on sand.
```

El movimiento de cámara tiene nombre, el movimiento es específico y el sonido está listado. Más sobre migrar prompts de Sora en [`references/sora-alternatives.md`](references/sora-alternatives.md).

</details>

<details>
<summary><b>Foto → prompt de imagen a video</b></summary>

**Antes**

```text
Make this photo move.
```

**Después** (`kling-i2v-portrait-blink-breeze`)

```text
The person blinks and smiles slightly, hair moving in a light breeze. Static camera.
```

Para una foto el prompt describe solo el movimiento; la imagen ya contiene el sujeto, la luz y el encuadre. Los tres movimientos nombrados son los que mantienen intacta una cara.

</details>

<details>
<summary><b>Usarlo desde un agente</b></summary>

```text
You: I need a vertical product reveal for earbuds, Kling, 5 seconds.
Agent (with the skill): runs python3 scripts/find.py --use-case ads --model kling-3,
  picks kling-hero-product-reveal-vertical, swaps "earbud case" details for yours,
  returns the prompt in a code block and notes that the source entry has no render report yet.
```

</details>

## Instalación

Funciona con cualquier agente que lea archivos de instrucciones. Elige el tuyo.

<details open>
<summary><b>Claude Code</b> (como skill)</summary>

```bash
git clone https://github.com/uniqaiapp/awesome-ai-video-prompts ~/.claude/skills/awesome-ai-video-prompts
```

Luego, en Claude Code, escribe `/awesome-ai-video-prompts` o simplemente describe la tarea; el skill se activa por su descripción. Local al proyecto en vez de global: clona en `.claude/skills/awesome-ai-video-prompts` dentro de tu proyecto.

Como plugin, cuando se publique el marketplace de uniqaiapp:

```
/plugin marketplace add uniqaiapp/skills
/plugin install awesome-ai-video-prompts@uniqaiapp
```

</details>

<details>
<summary><b>Cursor</b></summary>

Copia `SKILL.md`, `scripts/`, `data/`, `references/` y [`.cursor/rules/awesome-ai-video-prompts.mdc`](.cursor/rules/awesome-ai-video-prompts.mdc) en tu proyecto. El archivo de reglas incrusta el skill.

</details>

<details>
<summary><b>Codex / cualquier agente con AGENTS.md</b></summary>

Copia `SKILL.md`, `scripts/`, `data/` y `references/` en `.agents/skills/awesome-ai-video-prompts/` y añade el fragmento de [`codex/INSTRUCTIONS.md`](codex/INSTRUCTIONS.md) a tu `AGENTS.md`.

</details>

<details>
<summary><b>Sin agente</b></summary>

Cada script funciona por sí solo: `python3 scripts/find.py --help`, `python3 scripts/stats.py`, `python3 scripts/validate.py`. O pega [`SKILL.md`](SKILL.md) en el system prompt de cualquier modelo; fuera del frontmatter no tiene sintaxis específica de ningún agente.

</details>

Requisitos: Python 3.9+. Nada que instalar.

## Límites y honestidad

- **Escrito para no es renderizado en.** La mayoría de las entradas empiezan con `rendered_on` vacío. Siguen una guía citada del proveedor o vienen de la biblioteca de prompts de UniqAI, lo cual es una afirmación sobre la estructura, no sobre un clip que puedas ver. Las entradas con reporte lo dicen en línea; la plantilla de issue "Report a render" es la forma de conseguir uno.
- **Los prompts de imagen se renderizaron en GPT Image** para el sitio de UniqAI (fechas en `rendered_on`); para Flux y Nano Banana son el vocabulario correcto, no un resultado probado.
- **Runway no tiene guía citada** en esta versión: el centro de ayuda de Runway rechazó la descarga, así que las entradas de Runway siguen la práctica general y lo dicen.
- **Las versiones cambian.** Cada `guide` lleva la fecha en que se verificó. Kling 4.0 se anunció en octubre de 2026 (nota de prensa citada en las fuentes de `references/model-notes.md`); las entradas de Kling se escribieron contra las guías de 3.0.
- Cada número de este README lo produce `python3 scripts/stats.py` sobre `data/prompts/`; la suite de tests falla si el bloque generado está desactualizado o si aparece un conteo en el texto escrito a mano.

## FAQ

<details>
<summary><b>¿Qué tan largo debe ser un prompt para Kling 3.0?</b></summary>

De dos a cuatro frases cortas: el sujeto y qué hace, el escenario, un movimiento de cámara, y luego lente, luz y atmósfera. La guía de Kuaishou pide palabras simples y frases cortas, no una cantidad de palabras. Una lista larga de instrucciones que compiten entre sí renderiza con menos previsibilidad que una escena clara.

</details>

<details>
<summary><b>¿Puedo usar un prompt de Kling en Veo 3?</b></summary>

En general sí. Añade una frase `Audio:` (Veo genera sonido e inventará alguno si no lo haces) y termina con `No music` a menos que quieras música. Veo tolera mejor que Kling los movimientos de cámara apilados, pero un solo movimiento sigue leyéndose más limpio.

</details>

<details>
<summary><b>¿Dónde están los prompts negativos?</b></summary>

No hay. Varios front-ends no exponen un campo negativo para Kling, así que las entradas describen en su lugar qué debe quedarse quieto: "static camera, product centred" funciona mejor que "no camera shake", y se transfiere a cualquier modelo.

</details>

<details>
<summary><b>¿Es esta una lista de prompts para Sora?</b></summary>

No. La página de deprecaciones de OpenAI indica que los modelos de la API de Sora 2 se retiraron el 24 de septiembre de 2026. La estructura de un prompt de Sora se transfiere; [`references/sora-alternatives.md`](references/sora-alternatives.md) muestra adónde va ahora cada tipo de prompt.

</details>

<details>
<summary><b>¿Por qué JSON y no solo Markdown?</b></summary>

Para que agentes y scripts puedan filtrar por modelo, modo y etiqueta, para que el esquema pueda exigir un "por qué" y un campo de render, y para que el Markdown nunca contradiga los datos. El Markdown sigue estando en el repositorio, porque así es como la gente lee una lista awesome en GitHub.

</details>

## Relacionados

- [`video-director`](https://github.com/uniqaiapp/video-director): convierte una idea de una línea en un prompt plano a plano para modelos de video con IA (Kling, Veo, Sora y otros), con vocabulario de cámara, iluminación y movimiento. Úsalo para el storyboard; usa esta lista para los planos individuales.
- [`no-plastic`](https://github.com/uniqaiapp/no-plastic): reglas de prompt y un verificador para retratos con IA de aspecto natural: textura de piel, iluminación y elección de lente que evitan el aspecto plástico.
- [`ai-video-pricing`](https://github.com/uniqaiapp/ai-video-pricing): tabla de precios verificada a mano para generación de video con IA, por segundo y por clip, con URL de origen y fecha de verificación en cada fila.

## Contribuir

Los issues y pull requests son bienvenidos: un prompt nuevo con su "por qué", un reporte de render o una fuente corregida. Ver [CONTRIBUTING.md](CONTRIBUTING.md) para el formato de entrada y las comprobaciones locales (`python3 tests/run.py`, sin dependencias).

## Licencia

Prompts, datos y referencias: [CC BY 4.0](LICENSE), atribución "UniqAI, https://github.com/uniqaiapp/awesome-ai-video-prompts". Scripts y tests: [MIT](LICENSE) © UniqAI.

---

<div align="center">

<sub>Hecho por <a href="https://uniqai.app/?utm_source=github&utm_medium=readme-es&utm_campaign=awesome-ai-video-prompts">UniqAI</a>, una app de foto, video y chat con IA. Las entradas de Kling son la biblioteca de prompts que publicamos para nuestros propios usuarios.</sub>

</div>
