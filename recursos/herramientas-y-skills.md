---
tipo: recursos
actualizado: 2026-11-11
fuentes: [CONTEXTO_CLAUDE_CODE §8, carpeta «trending-skills-main» (407 skills), «skills-instagram-zips» (13 skills ig-*), skills y agentes instalados en Claude Code]
---
# Herramientas y skills útiles para crear contenido

Una skill es un paquete de instrucciones que Claude carga para una tarea. «Incluida en el repo» = viene en `.claude/skills/` y funciona en el PC y en Claude Code en la nube; «Instalada» = plugin que se activa con `.claude/settings.json`; «Opcional» = existe en Descargas pero no se llevó al repo.

## Herramientas conectadas o en uso
Metricool (programar y métricas, plan gratis) · Windsor.ai (anuncios/Meta) · Higgsfield (plan Ultimate; ~924 créditos al 4-nov) · ElevenLabs (voz) · Canva (diseño editable) · Drive (compartir material) · WhatsApp Business y catálogo · agente de IA de Meta · ReplyRush (gratis) · Edits de Instagram (edición) · HyperFrames (motion design) · Apify (datos de cuentas, con tope de gasto; el token lo pone el dueño en el `.env`, nunca se lo pide ni se lee). *Content Factory de Higgsfield no calza: no usa clips reales.* *Motion-architect: descartado (Windows; ya hay Remotion).*

## Skills por tarea
### 1. Estrategia, investigación y calendario
| Skill | Para qué | Estado |
|---|---|---|
| `matriz-viralidad` (`start`, `espiar`, `construir`, `analiticas`, `calendario`, `guion`, `ganador`, `sentimiento`, `rutina`, `ver`, `doctor`) | Analizar cuentas propias y de la competencia, construir la matriz de viralidad, calendario del mes con respaldo, guiones y simulación | Instalada |
| `ig-viral` | Buscar los reels que funcionan hoy en el nicho y armar un archivo de ganchos | Incluida en el repo |
| `ig-plan` | Planificar la semana (qué publicar, formato, hora, a quién responder) | Incluida en el repo |
| `ig-audit` | Post-mortem de lo ya publicado: qué funcionó y qué dejar de hacer | Incluida en el repo |
| `ig-profile` | Puntuar y reescribir bio, nombre, destacadas y grilla | Incluida en el repo |
| `anthropic-skills:marketing-strategy`, `marketingskills-ai-agents`, `advertising-skills-ai-agents` | Estrategia, textos de conversión y publicidad de respuesta directa | Instaladas |
| `last30days-research-skill`, `agent-reach-internet-access` | Investigar qué se dice hoy en Reddit, X, YouTube (tendencias) | Opcional (en trending-skills) |
| `pm-market-research:*` | Competidores, personas, segmentos | Instaladas |

### 2. Escritura
| Skill | Para qué | Estado |
|---|---|---|
| `ig-reel` | Guion de reel con 26 fórmulas de gancho, texto en pantalla y beat sheet | Incluida en el repo |
| `ig-caption` | Caption (línea antes del «… más», cuerpo, petición única, hashtags) | Incluida en el repo |
| `ig-carousel` | Carrusel: portada, copy por lámina y archivos 1080×1350 | Incluida en el repo |
| `ig-story` | Secuencia de stories con stickers y paso a mensajes directos | Incluida en el repo |
| `ig-repurpose` | Convertir un activo largo en una semana de reels y carruseles | Incluida en el repo |
| `ig-comment`, `ig-reply`, `ig-dm` | Comentarios, respuestas y DMs que suenen humanos | Incluida en el repo |
| `ig-human`, `stop-slop`, `talk-normal-llm-prompt` | Quitar el sello «hecho por IA» de cualquier texto | `stop-slop` e `ig-human` incluidas en el repo; `talk-normal` opcional |
| `prompt-master-skill` | Prompts precisos para cualquier IA de imagen/video | Incluida en el repo |

### 3. Imagen, diseño y marca
| Skill | Para qué | Estado |
|---|---|---|
| `canva:*` (marca, edición, redimensionar a redes, feedback) | Piezas editables y adaptación a cada formato | Instaladas |
| `creative-architect:*` (`producto`, `ugc`, `animar`, `clonar-anuncio`, `direccion-de-arte`) | Direcc. de arte y producción de imagen/video con IA (respetando que el dueño pide material real) | Instalada |
| `higgsfield-product-photoshoot`, `higgsfield-generate`, `higgsfield-brandkit`, `higgsfield-youtube-thumbnail`, `higgsfield-soul-id` | Imágenes de producto, anuncios, kit de marca, portadas, identidad de la creadora | Instaladas |
| `anthropic-skills:awesome-gpt-image-2-prompts`, `canvas-design` | Prompts de imagen y piezas estáticas | Instaladas |
| `openbrand-asset-extraction`, `designlang-design-extract`, `logo-generator-skill` | Extraer/generar activos de marca | Opcional (baja prioridad: la marca ya existe) |

### 4. Video y motion
| Skill | Para qué | Estado |
|---|---|---|
| `hyperframes:*` (`hyperframes`, `cli`, `registry`, `media-use`, `slideshow`, `figma`) | Reels con motion design por capas, títulos, subtítulos y render | Instalada (en uso) |
| `ig-reel` + agentes `Short-Video Editing Coach`, `Video Optimization Specialist` | Ritmo, cortes y retención | Agentes instalados |
| `remotion-best-practices` (zip), `anthropic-skills:animation-patterns`, `svg-animations` | Animación con Remotion y SVG | Opcional / instaladas |
| `corridorkey-green-screen`, `recordly-screen-recorder` | Quitar fondo verde; grabar pantalla con auto-zoom | Opcional |

### 5. Voz
`omnivoice-tts`, `moss-tts-nano-speech`, `voicebox-voice-synthesis` (voz local y clonación; la voz «Pía» hoy es de ElevenLabs): opcionales, no incluidas.

### 6. Web
`impeccable`, `design-taste-frontend`, `ui-ux-pro-max-skill`, `web-design-skill`, `taste-skill-frontend-design`: páginas de servicios y landings sin aspecto genérico (instaladas las tres primeras). `geoflow-content-automation`: SEO/GEO (opcional, no incluida).

### 7. Cerebro y memoria
`llm-wiki-skill`, `claude-obsidian-wiki`, `agentic-stack-portable-brain`, `claude-memory-compiler`: método para crear y mantener un cerebro tipo wiki (base de este). Opcionales, si se quiere automatizar la mantención.

## Agentes especialistas disponibles (en Claude Code)
Instagram Curator · TikTok Strategist · Content Creator · Social Media Strategist · Paid Social Strategist · Ad Creative Strategist · Carousel Growth Engine · Short-Video Editing Coach · Video Optimization Specialist · Brand Guardian · Image Prompt Engineer · Visual Storyteller · Growth Hacker · Offer & Lead Gen Strategist · SEO Specialist · Trend Researcher · Customer Service · Pricing Analyst · Prompt Engineer. El trabajo con agentes lo dirige el **Agents Orchestrator**.

## Cómo queda el equipo
Las **13 `ig-*`** ya vienen en el repo (cubren casi todo el flujo de Instagram), junto con `stop-slop` y 18 agentes en `.claude/agents/` (incluido el Director de Contenido). Con los plugins `matriz-viralidad` y `hyperframes`, el flujo semanal queda completo: investigar → planificar → escribir → producir → medir.

Relacionado: [[formatos-y-cadencia]] · [[creadora-digital]]
