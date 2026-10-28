<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/banner.svg">
  <source media="(prefers-color-scheme: light)" srcset="assets/banner-light.svg">
  <img alt="awesome-ai-video-prompts by UniqAI" src="assets/banner.svg" width="1280" height="320">
</picture>

[![License: CC BY 4.0](https://img.shields.io/badge/license-CC_BY_4.0-d1fe17?style=flat-square&labelColor=0d0f12)](LICENSE)
[![Claude Code skill](https://img.shields.io/badge/Claude_Code-skill-d1fe17?style=flat-square&labelColor=0d0f12)](#instalação)
[![Cursor](https://img.shields.io/badge/Cursor-rules-d1fe17?style=flat-square&labelColor=0d0f12)](#instalação)
[![Codex](https://img.shields.io/badge/Codex-AGENTS.md-d1fe17?style=flat-square&labelColor=0d0f12)](#instalação)
[![Made by UniqAI](https://img.shields.io/badge/made_by-UniqAI-fdfc07?style=flat-square&labelColor=0d0f12)](https://uniqai.app/?utm_source=github&utm_medium=readme-pt-br&utm_campaign=awesome-ai-video-prompts)

**Prompts selecionados para vídeo com IA no Kling 3.0, Veo 3, Wan 2.5, Runway e Seedance, com o modelo, as configurações e o motivo de cada um funcionar.**

[Início rápido](#início-rápido) · [A lista](#a-lista) · [Como funciona](#como-funciona) · [Exemplos](#exemplos) · [Instalação](#instalação) · [FAQ](#faq)

</div>

[English](README.md) · [Русский](README.ru.md) · [简体中文](README.zh-CN.md) · [Español](README.es.md) · Português (BR) · [日本語](README.ja.md) · [한국어](README.ko.md)

# Awesome AI Video Prompts: prompts para vídeo com IA, Kling 3.0, Veo 3, Wan, Runway, Seedance

Uma lista selecionada de prompts para vídeo com IA (texto para vídeo e imagem para vídeo) para Kling 3.0, Veo 3, Wan 2.5, Runway Gen-4 e Seedance 2.x, mais um conjunto curto de prompts de imagem para Flux, Nano Banana e GPT Image. Cada entrada traz o prompt em um bloco de código, o modelo para o qual foi escrito, modo, duração, proporção, uma nota sobre por que a estrutura funciona e um campo `rendered_on` que fica vazio até alguém relatar uma renderização real. Os dados são JSON; as páginas em Markdown e as contagens abaixo são geradas a partir deles.

| **Específico por modelo, não genérico** | **Honesto sobre resultados** | **Funciona como skill de agente** |
|:---|:---|:---|
| Cada prompt segue o guia do próprio fornecedor (citado com data): um movimento de câmera só para o Kling, áudio em frase própria para o Veo, planos rotulados para o Seedance. | "Escrito para" e "renderizado em" são campos separados. As contagens deste README vêm de `scripts/stats.py`, não de um teclado. | `SKILL.md` permite que Claude Code, Cursor ou Codex pesquisem a lista e adaptem o prompt mais próximo ao seu plano. |

## Início rápido

```bash
git clone https://github.com/uniqaiapp/awesome-ai-video-prompts
cd awesome-ai-video-prompts
python3 scripts/find.py --model kling-3 --use-case product
```

Você recebe os prompts correspondentes como texto, cada um com uma linha `Why it works` e a indicação de se alguma renderização foi relatada. Nada para instalar; Python 3.9+. Para navegar sem terminal: [por modelo](prompts/by-model/) ou [por caso de uso](prompts/by-use-case/).

## Demo

<img alt="awesome-ai-video-prompts demo: searching the list with scripts/find.py and printing one entry" src="assets/demo.svg" width="820">

## O que tem na lista

<!-- generated:stats:start -->
| Modelo | Prompts escritos para ele |
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
| Movimentos de câmera | 9 |
| Produto | 6 |
| Retrato | 5 |
| Natureza | 5 |
| Ação | 5 |
| Anúncios | 4 |
| Anime | 4 |
| Imagem para vídeo | 6 |
| Imagens estáticas (prompts de imagem) | 8 |

| Modo | Prompts |
|:---|---:|
| texto para vídeo (`t2v`) | 38 |
| imagem para vídeo (`i2v`) | 6 |
| texto para imagem (`t2i`) | 6 |
| edição de imagem (`i2i`) | 2 |

52 prompts no total: 44 de vídeo, 8 de imagem. 7 têm relato de renderização (`rendered_on` preenchido); 45 seguem o guia de prompts do fornecedor ou a biblioteca da UniqAI, mas ainda não têm relato de renderização.
<!-- generated:stats:end -->

## A lista

Uma linha por prompt; o link abre a entrada completa com o texto do prompt, a nota de por que funciona e os relatos de renderização que existirem. Chaves de modelo: `kling-3` Kling 3.0, `veo-3` Veo 3, `wan-2.5` Wan 2.5, `runway-gen-4` família Runway Gen-4, `seedance-2` Seedance 2.x, `flux`, `nano-banana`, `gpt-image`. Modos: `t2v` texto para vídeo, `i2v` imagem para vídeo, `t2i` texto para imagem, `i2i` edição de imagem.

<!-- generated:list:start -->
### Movimentos de câmera

- [Brass compass, push in](prompts/by-use-case/camera-moves.md#brass-compass-push-in) · kling-3 · `t2v` · 5 s
- [Lit candle, pull back](prompts/by-use-case/camera-moves.md#lit-candle-pull-back) · kling-3 · `t2v` · 5 s
- [Harbour boats, pan left](prompts/by-use-case/camera-moves.md#harbour-boats-pan-left) · kling-3 · `t2v` · 5 s
- [Hiker on a ridge, tilt up](prompts/by-use-case/camera-moves.md#hiker-on-a-ridge-tilt-up) · kling-3 · `t2v` · 5 s
- [Bronze horse, orbit](prompts/by-use-case/camera-moves.md#bronze-horse-orbit) · kling-3 · `t2v` · 5 s
- [Lighthouse at dusk, dolly in with sound](prompts/by-use-case/camera-moves.md#lighthouse-at-dusk-dolly-in-with-sound) · veo-3 · `t2v` · 8 s
- [Old town rooftops, crane up](prompts/by-use-case/camera-moves.md#old-town-rooftops-crane-up) · wan-2.5, kling-3 · `t2v` · 5 s
- [Handheld follow through a corridor](prompts/by-use-case/camera-moves.md#handheld-follow-through-a-corridor) · runway-gen-4, seedance-2 · `t2v` · 5 s
- [Chrome droplet over a neon street, push in](prompts/by-use-case/camera-moves.md#chrome-droplet-over-a-neon-street-push-in) · kling-3 · `t2v` · 8 s

[Todos os prompts de movimentos de câmera com o texto completo →](prompts/by-use-case/camera-moves.md)

### Produto

- [Headphones on a turntable](prompts/by-use-case/product.md#headphones-on-a-turntable) · kling-3 · `t2v` · 5 s
- [Perfume bottle, macro water drop](prompts/by-use-case/product.md#perfume-bottle-macro-water-drop) · kling-3 · `t2v` · 5 s
- [Sneaker, quarter orbit](prompts/by-use-case/product.md#sneaker-quarter-orbit) · kling-3 · `t2v` · 5 s
- [Coffee pour, slow motion with sound](prompts/by-use-case/product.md#coffee-pour-slow-motion-with-sound) · veo-3 · `t2v` · 8 s
- [Watch, two connected shots](prompts/by-use-case/product.md#watch-two-connected-shots) · seedance-2 · `t2v` · 10 s
- [Skincare jar, slow rotate on marble](prompts/by-use-case/product.md#skincare-jar-slow-rotate-on-marble) · kling-3, wan-2.5 · `t2v` · 5 s

[Todos os prompts de produto com o texto completo →](prompts/by-use-case/product.md)

### Retrato

- [Studio portrait, blink and smile](prompts/by-use-case/portrait.md#studio-portrait-blink-and-smile) · kling-3 · `t2v` · 5 s
- [Golden hour, push in to close-up](prompts/by-use-case/portrait.md#golden-hour-push-in-to-close-up) · kling-3 · `t2v` · 5 s
- [Dancer, track forward](prompts/by-use-case/portrait.md#dancer-track-forward) · kling-3 · `t2v` · 5 s
- [Portrait with one line of dialogue](prompts/by-use-case/portrait.md#portrait-with-one-line-of-dialogue) · veo-3 · `t2v` · 8 s
- [Rain on a window, portrait behind it](prompts/by-use-case/portrait.md#rain-on-a-window-portrait-behind-it) · wan-2.5, kling-3 · `t2v` · 5 s

[Todos os prompts de retrato com o texto completo →](prompts/by-use-case/portrait.md)

### Natureza

- [Mountain lake at sunrise, static wide](prompts/by-use-case/nature.md#mountain-lake-at-sunrise-static-wide) · kling-3 · `t2v` · 5 s
- [Coastal dune, tilt down](prompts/by-use-case/nature.md#coastal-dune-tilt-down) · kling-3 · `t2v` · 5 s
- [Autumn pond, push in](prompts/by-use-case/nature.md#autumn-pond-push-in) · kling-3 · `t2v` · 5 s
- [Thunderstorm over a plain, with sound](prompts/by-use-case/nature.md#thunderstorm-over-a-plain-with-sound) · veo-3 · `t2v` · 8 s
- [Tide pool, macro](prompts/by-use-case/nature.md#tide-pool-macro) · wan-2.5, kling-3 · `t2v` · 5 s

[Todos os prompts de natureza com o texto completo →](prompts/by-use-case/nature.md)

### Ação

- [Cyclist in the rain, tracking shot](prompts/by-use-case/action.md#cyclist-in-the-rain-tracking-shot) · kling-3 · `t2v` · 5 s
- [Wok flame, static camera](prompts/by-use-case/action.md#wok-flame-static-camera) · kling-3 · `t2v` · 5 s
- [Skateboarder, low-angle pass](prompts/by-use-case/action.md#skateboarder-low-angle-pass) · runway-gen-4, seedance-2 · `t2v` · 5 s
- [Alley chase, two connected shots](prompts/by-use-case/action.md#alley-chase-two-connected-shots) · seedance-2 · `t2v` · 10 s
- [Horse galloping on a beach, side tracking](prompts/by-use-case/action.md#horse-galloping-on-a-beach-side-tracking) · wan-2.5, kling-3, veo-3 · `t2v` · 5 s

[Todos os prompts de ação com o texto completo →](prompts/by-use-case/action.md)

### Anúncios

- [UGC-style handheld product talk, with disclosure](prompts/by-use-case/ads.md#ugc-style-handheld-product-talk-with-disclosure) · veo-3 · `t2v` · 8 s
- [Vertical product hero reveal](prompts/by-use-case/ads.md#vertical-product-hero-reveal) · kling-3, wan-2.5 · `t2v` · 5 s
- [App promo, three beats](prompts/by-use-case/ads.md#app-promo-three-beats) · seedance-2 · `t2v` · 10 s
- [Fabric in slow motion, space left for a logo](prompts/by-use-case/ads.md#fabric-in-slow-motion-space-left-for-a-logo) · runway-gen-4, kling-3, wan-2.5 · `t2v` · 5 s

[Todos os prompts de anúncios com o texto completo →](prompts/by-use-case/ads.md)

### Anime

- [Anime rooftop, wind and hair](prompts/by-use-case/anime.md#anime-rooftop-wind-and-hair) · wan-2.5, kling-3 · `t2v` · 5 s
- [Anime rain street, slow pan](prompts/by-use-case/anime.md#anime-rain-street-slow-pan) · kling-3, wan-2.5 · `t2v` · 5 s
- [Anime two-shot, reaction without dialogue](prompts/by-use-case/anime.md#anime-two-shot-reaction-without-dialogue) · seedance-2 · `t2v` · 10 s
- [Mecha hangar, tilt up](prompts/by-use-case/anime.md#mecha-hangar-tilt-up) · kling-3, wan-2.5 · `t2v` · 5 s

[Todos os prompts de anime com o texto completo →](prompts/by-use-case/anime.md)

### Imagem para vídeo

- [Portrait photo: blink and breeze](prompts/by-use-case/image-to-video.md#portrait-photo-blink-and-breeze) · kling-3 · `i2v` · 5 s
- [Table or still-life photo: steam and flame](prompts/by-use-case/image-to-video.md#table-or-still-life-photo-steam-and-flame) · kling-3 · `i2v` · 5 s
- [Landscape photo: clouds and ripples, pan](prompts/by-use-case/image-to-video.md#landscape-photo-clouds-and-ripples-pan) · kling-3 · `i2v` · 5 s
- [Illustration: gentle natural motion, keep the style](prompts/by-use-case/image-to-video.md#illustration-gentle-natural-motion-keep-the-style) · kling-3, wan-2.5 · `i2v` · 5 s
- [Product photo: quarter turn with sound](prompts/by-use-case/image-to-video.md#product-photo-quarter-turn-with-sound) · veo-3 · `i2v` · 8 s
- [City photo: traffic and lights come alive](prompts/by-use-case/image-to-video.md#city-photo-traffic-and-lights-come-alive) · wan-2.5, kling-3 · `i2v` · 5 s

[Todos os prompts de imagem para vídeo com o texto completo →](prompts/by-use-case/image-to-video.md)

### Imagens estáticas (prompts de imagem)

- [Catalogue product shot: stoneware teapot](prompts/by-use-case/stills.md#catalogue-product-shot-stoneware-teapot) · nano-banana, flux, gpt-image · `t2i` · renderizado
- [Editorial studio portrait, real skin](prompts/by-use-case/stills.md#editorial-studio-portrait-real-skin) · flux, nano-banana, gpt-image · `t2i` · renderizado
- [Golden-hour field portrait](prompts/by-use-case/stills.md#golden-hour-field-portrait) · flux, nano-banana, gpt-image · `t2i` · renderizado
- [Neon night portrait, anamorphic](prompts/by-use-case/stills.md#neon-night-portrait-anamorphic) · flux, nano-banana, gpt-image · `t2i` · renderizado
- [Black-and-white character study](prompts/by-use-case/stills.md#black-and-white-character-study) · flux, nano-banana, gpt-image · `t2i` · renderizado
- [Edit: enhance a dim phone photo, change nothing else](prompts/by-use-case/stills.md#edit-enhance-a-dim-phone-photo-change-nothing-else) · nano-banana, gpt-image · `i2i` · renderizado
- [Edit: selfie to business headshot, keep the face](prompts/by-use-case/stills.md#edit-selfie-to-business-headshot-keep-the-face) · nano-banana, gpt-image · `i2i`
- [Beauty portrait, freckles kept](prompts/by-use-case/stills.md#beauty-portrait-freckles-kept) · flux, nano-banana, gpt-image · `t2i` · renderizado

[Todos os prompts de imagens estáticas (prompts de imagem) com o texto completo →](prompts/by-use-case/stills.md)

### Por modelo

- [Kling 3.0](prompts/by-model/kling-3.md) · 32 prompts · clipes sem áudio
- [Veo 3](prompts/by-model/veo-3.md) · 7 prompts · gera áudio
- [Wan 2.5](prompts/by-model/wan-2.5.md) · 12 prompts · gera áudio
- [Runway Gen-4 family](prompts/by-model/runway-gen-4.md) · 3 prompts · clipes sem áudio
- [Seedance 2.x](prompts/by-model/seedance-2.md) · 6 prompts · clipes sem áudio
- [Flux](prompts/by-model/flux.md) · 6 prompts · modelo de imagem
- [Nano Banana (Gemini image)](prompts/by-model/nano-banana.md) · 8 prompts · modelo de imagem
- [GPT Image](prompts/by-model/gpt-image.md) · 8 prompts · modelo de imagem
<!-- generated:list:end -->

## Como funciona

1. **Uma estrutura para todos os modelos.** Sujeito e o que ele faz → cenário → um movimento de câmera (ou "static camera") → lente e luz → clima. O guia do Kling da Kuaishou pede exatamente essa ordem e um movimento "adequado a um vídeo de 5 segundos"; o guia do Veo do Google lista os mesmos elementos e acrescenta o áudio como frase própria. A ordem é a mesma entre os modelos; os detalhes de sintaxe mudam, e [`references/model-notes.md`](references/model-notes.md) lista cada um com a página do fornecedor e a data em que foi verificada.
2. **Um movimento, um deslocamento.** Todo prompt de vídeo nomeia um único movimento de câmera com velocidade e uma palavra de estabilidade ("slow, stable push in, no sudden motion") e uma única ação do sujeito que caiba em 5 a 8 segundos. O movimento secundário vem de coisas baratas e contínuas: vento no cabelo, vapor, poeira flutuando, um feixe girando.
3. **Diga o que fica parado.** Em vez de prompt negativo (o Kling não tem um em muitos front-ends), as entradas declaram o que não deve mudar: "static camera, product centred", ou, para imagem para vídeo, "keep the framing, background and art style exactly as in the photo".
4. **Áudio e múltiplos planos onde o modelo suporta.** As entradas do Veo terminam com `Audio: …` e `No music`; diálogo usa `She says: "…"`. As entradas do Seedance rotulam `Shot 1` e `Shot 2` e mantêm figurino, lente e luz idênticos entre eles.
5. **O JSON é a fonte.** `data/prompts/<use-case>.json` guarda os registros, `data/schema.json` é a especificação, `scripts/validate.py` a aplica, `scripts/build.py` escreve `prompts/**/*.md` e as duas seções geradas deste README. Um teste falha se eles divergirem.

```
data/prompts/*.json  ──validate.py──▶  ok
        │
        └──build.py──▶  prompts/by-model/*.md
                        prompts/by-use-case/*.md
                        README.md (stats + list sections)
```

Para comparar o mesmo prompt no Kling 3.0, Veo 3 e Wan 2.5 lado a lado, [a UniqAI roda os três a partir de um único compositor](https://uniqai.app/video?utm_source=github&utm_medium=readme-pt-br&utm_campaign=awesome-ai-video-prompts); qualquer outra ferramenta que exponha esses modelos funciona do mesmo jeito.

## Exemplos

<details>
<summary><b>Prompt vago → prompt para Kling 3.0 com um único movimento de câmera</b></summary>

**Antes**

```text
A perfume bottle, cinematic, luxury, 4k, slow motion, beautiful lighting.
```

**Depois** (`kling-perfume-macro-drop`)

```text
A glass bottle of amber perfume standing on wet black slate, a single water drop running down the glass. Slow push in on the bottle. 90 mm macro lens, soft backlight through the liquid, small specular highlights. Elegant, quiet atmosphere.
```

Um movimento (a gota), um movimento de câmera (push in), uma lente, uma direção de luz, um clima. "4k" e "cinematic" sumiram; são configurações e adjetivos, não instruções.

</details>

<details>
<summary><b>Prompt no estilo Sora → prompt para Veo 3 com som</b></summary>

**Antes**

```text
A golden retriever runs along a beach at sunset, cinematic, shallow depth of field.
```

**Depois**

```text
Tracking shot at ground level: a golden retriever runs along a wet beach at sunset, waves rolling in behind it. Shallow depth of field, warm light. Sound: surf and paws on sand.
```

O movimento de câmera tem nome, o movimento é específico e o som está listado. Mais sobre migrar prompts do Sora em [`references/sora-alternatives.md`](references/sora-alternatives.md).

</details>

<details>
<summary><b>Foto → prompt de imagem para vídeo</b></summary>

**Antes**

```text
Make this photo move.
```

**Depois** (`kling-i2v-portrait-blink-breeze`)

```text
The person blinks and smiles slightly, hair moving in a light breeze. Static camera.
```

Para uma foto, o prompt descreve só o movimento; a imagem já tem o sujeito, a luz e o enquadramento. Os três movimentos nomeados são os que mantêm um rosto intacto.

</details>

<details>
<summary><b>Usando a partir de um agente</b></summary>

```text
You: I need a vertical product reveal for earbuds, Kling, 5 seconds.
Agent (with the skill): runs python3 scripts/find.py --use-case ads --model kling-3,
  picks kling-hero-product-reveal-vertical, swaps "earbud case" details for yours,
  returns the prompt in a code block and notes that the source entry has no render report yet.
```

</details>

## Instalação

Funciona com qualquer agente que leia arquivos de instrução. Escolha o seu.

<details open>
<summary><b>Claude Code</b> (como skill)</summary>

```bash
git clone https://github.com/uniqaiapp/awesome-ai-video-prompts ~/.claude/skills/awesome-ai-video-prompts
```

Depois, no Claude Code, digite `/awesome-ai-video-prompts` ou apenas descreva a tarefa; a skill é acionada pela própria descrição. Local ao projeto em vez de global: clone em `.claude/skills/awesome-ai-video-prompts` dentro do seu projeto.

Como plugin, quando o marketplace uniqaiapp for publicado:

```
/plugin marketplace add uniqaiapp/skills
/plugin install awesome-ai-video-prompts@uniqaiapp
```

</details>

<details>
<summary><b>Cursor</b></summary>

Copie `SKILL.md`, `scripts/`, `data/`, `references/` e [`.cursor/rules/awesome-ai-video-prompts.mdc`](.cursor/rules/awesome-ai-video-prompts.mdc) para o seu projeto. O arquivo de regra embute a skill.

</details>

<details>
<summary><b>Codex / qualquer agente com AGENTS.md</b></summary>

Copie `SKILL.md`, `scripts/`, `data/` e `references/` para `.agents/skills/awesome-ai-video-prompts/` e adicione o trecho de [`codex/INSTRUCTIONS.md`](codex/INSTRUCTIONS.md) ao seu `AGENTS.md`.

</details>

<details>
<summary><b>Sem agente</b></summary>

Todo script roda sozinho: `python3 scripts/find.py --help`, `python3 scripts/stats.py`, `python3 scripts/validate.py`. Ou cole [`SKILL.md`](SKILL.md) no system prompt de qualquer modelo; fora do frontmatter, não há sintaxe específica de agente.

</details>

Requisitos: Python 3.9+. Nada para instalar.

## Limites e honestidade

- **Escrito para não é renderizado em.** A maioria das entradas começa com `rendered_on` vazio. Elas seguem um guia citado do fornecedor ou vêm da biblioteca de prompts da UniqAI, o que é uma afirmação sobre estrutura, não sobre um clipe que você possa assistir. Entradas com relato dizem isso no próprio texto; o template de issue "Report a render" é o caminho para conseguir um.
- **Os prompts de imagem foram renderizados no GPT Image** para o site da UniqAI (datas em `rendered_on`); para Flux e Nano Banana eles são o vocabulário certo, não um resultado testado.
- **A Runway não tem guia citado** nesta versão: a central de ajuda da Runway recusou a requisição, então as entradas da Runway seguem a prática geral e dizem isso.
- **Versões mudam.** Cada `guide` carrega a data em que foi verificado. O Kling 4.0 foi anunciado em outubro de 2026 (comunicado citado nas fontes de `references/model-notes.md`); as entradas do Kling foram escritas com base nos guias do 3.0.
- Todo número deste README é produzido por `python3 scripts/stats.py` sobre `data/prompts/`; a suíte de testes falha se o bloco gerado estiver desatualizado ou se uma contagem aparecer no texto escrito à mão.

## FAQ

<details>
<summary><b>Qual deve ser o tamanho de um prompt para Kling 3.0?</b></summary>

Duas a quatro frases curtas: o sujeito e o que ele faz, o cenário, um movimento de câmera, depois lente, luz e clima. O guia da Kuaishou pede palavras simples e frases curtas, não uma contagem de palavras. Uma lista longa de instruções concorrentes renderiza de forma menos previsível do que uma cena clara.

</details>

<details>
<summary><b>Posso usar um prompt do Kling no Veo 3?</b></summary>

Na maior parte, sim. Acrescente uma frase `Audio:` (o Veo gera som e vai inventar algum se você não disser) e termine com `No music`, a menos que queira trilha. O Veo tolera movimentos de câmera empilhados melhor que o Kling, mas um movimento só ainda fica mais limpo.

</details>

<details>
<summary><b>Onde estão os prompts negativos?</b></summary>

Não existem. Vários front-ends não expõem campo negativo para o Kling, então as entradas descrevem o que deve ficar parado: "static camera, product centred" funciona melhor que "no camera shake", e transfere para qualquer modelo.

</details>

<details>
<summary><b>Isto é uma lista de prompts para o Sora?</b></summary>

Não. A página de descontinuações da OpenAI lista os modelos da API do Sora 2 como removidos em 24 de setembro de 2026. A estrutura de um prompt do Sora transfere; [`references/sora-alternatives.md`](references/sora-alternatives.md) mostra para onde cada tipo de prompt vai agora.

</details>

<details>
<summary><b>Por que JSON e não só Markdown?</b></summary>

Para que agentes e scripts possam filtrar por modelo, modo e tag, para que o schema possa exigir um "porquê" e um campo de renderização, e para que o Markdown nunca discorde dos dados. O Markdown continua commitado, porque é assim que as pessoas leem uma lista awesome no GitHub.

</details>

## Relacionados

- [`video-director`](https://github.com/uniqaiapp/video-director): transforma uma ideia de uma linha em um prompt plano a plano para modelos de vídeo com IA (Kling, Veo, Sora e outros), com vocabulário de câmera, iluminação e movimento. Use-o para o storyboard; use esta lista para os planos individuais.
- [`no-plastic`](https://github.com/uniqaiapp/no-plastic): regras de prompt e um verificador para retratos com IA de aparência natural: textura de pele, iluminação e escolhas de lente que evitam o visual plástico.
- [`ai-video-pricing`](https://github.com/uniqaiapp/ai-video-pricing): tabela de preços conferida à mão para geração de vídeo com IA, por segundo e por clipe, com URL de origem e data de verificação em cada linha.

## Contribuindo

Issues e pull requests são bem-vindos: um prompt novo com o seu "porquê", um relato de renderização ou uma fonte corrigida. Veja [CONTRIBUTING.md](CONTRIBUTING.md) para o formato das entradas e as verificações locais (`python3 tests/run.py`, sem dependências).

## Licença

Prompts, dados e referências: [CC BY 4.0](LICENSE), atribuição "UniqAI, https://github.com/uniqaiapp/awesome-ai-video-prompts". Scripts e testes: [MIT](LICENSE) © UniqAI.

---

<div align="center">

<sub>Feito pela <a href="https://uniqai.app/?utm_source=github&utm_medium=readme-pt-br&utm_campaign=awesome-ai-video-prompts">UniqAI</a>, um app de foto, vídeo e chat com IA. As entradas do Kling são a biblioteca de prompts que publicamos para os nossos próprios usuários.</sub>

</div>
