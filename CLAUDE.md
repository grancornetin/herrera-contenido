# Cerebro de contenido · Herrera Producciones

Léelo completo antes de crear cualquier pieza. Es la única puerta de entrada.

## Al abrir una sesión nueva
1. Cuéntale al dueño en el chat, en 5 líneas, dónde quedó el trabajo (mira `log.md`, `contenido/calendario-y-estado.md` y `preguntas-abiertas.md`) y qué sigue. Pregúntale qué quiere hacer hoy.
2. Para crear contenido, **trabaja como «Director de Contenido»** (`.claude/agents/director-de-contenido.md`): reparte entre los especialistas y revisa cada pieza antes de entregarla.
3. Este repo pasa a **privado** (mientras siga público, cuidado): nunca subas claves, tokens, datos personales de clientes ni material sin permiso. No hagas commit ni push sin que el dueño lo pida.

## Qué trae listo este repo (`.claude/`)
- **Skills** (`.claude/skills/`): 13 de Instagram (`ig-plan`, `ig-reel`, `ig-caption`, `ig-carousel`, `ig-story`, `ig-viral`, `ig-audit`, `ig-profile`, `ig-repurpose`, `ig-comment`, `ig-reply`, `ig-dm`, `ig-human`) y `stop-slop`. Funcionan en el PC y en Claude Code en la nube. Están pensadas para inglés: mandan las reglas de este cerebro (CTA único «Escríbenos por WhatsApp»; no «comenta una palabra»).
- **Agentes** (`.claude/agents/`): Director de Contenido, Content Creator, Instagram Curator, Short-Video Editing Coach, Video Optimization Specialist, Social Media Strategist, TikTok Strategist, Carousel Growth Engine, Growth Hacker, SEO Specialist, Ad Creative Strategist, Paid Social Strategist, Brand Guardian, Image Prompt Engineer, Visual Storyteller, Trend Researcher, Feedback Synthesizer, Customer Service.
- **Plugins** (`matriz-viralidad`, `creative-architect`, `hyperframes`, `canva`): se activan con `.claude/settings.json` (ver `herramientas/LEEME.md`).
- **Conectores de tu cuenta** (Higgsfield, Canva, Metricool, Drive): dependen de tu cuenta de Claude, no del repo.
- Origen y licencias: `.claude/THIRD-PARTY.md`.

## Enlaces públicos para Metricool (repo aparte: `herrera-piezas`)
Este cerebro va a ser **privado**. Las piezas **aprobadas por el dueño** se suben al repo público `grancornetin/herrera-piezas` (carpeta `semana-NN/`), y de ahí sale el enlace directo para Metricool:
`https://raw.githubusercontent.com/grancornetin/herrera-piezas/main/<ruta del archivo>`
- Para sacarlos sin equivocarse, dentro de `herrera-piezas`: `python enlace_publico.py semana-02/reel-1.mp4` (o `--carpeta semana-02`). Avisa si el archivo no está subido, pesa más de 100 MB o tiene espacios en el nombre.
- **Primero commit y push, después el enlace** (GitHub tarda unos minutos). Nombres en minúsculas con guiones, sin espacios ni tildes. Límite: 100 MB por archivo.
- A `herrera-piezas` **solo** va material aprobado: nada de notas, precios internos ni borradores. Los borradores siguen en `piezas/` de este repo.
- Los enlaces antiguos de `feed/` dejan de funcionar cuando este repo pase a privado (ya fueron usados).

## Qué es esto
La memoria del negocio **Herrera Producciones** (arriendo de photobooths y experiencias para eventos, Región del Maule, Chile) escrita para una sola tarea: **crear contenido** (reels, stories, carruseles, posts, captions, anuncios, fichas y secciones web, guiones, mensajes de WhatsApp, productos y servicios).
Un agente que lea este cerebro debe saber: qué hacemos, qué servicios hay y cuáles vienen, cómo funciona cada uno, qué implementos necesita y cómo se trabaja, qué se puede y no se puede decir, y qué contenido ha funcionado.

**No contiene** (a propósito): código, tareas ni estado de la app Cotizador, costos, sueldos, datos bancarios, claves ni datos personales de clientes. Si algo de eso aparece en una conversación, no se anota aquí.

## Cómo está organizado
| Carpeta | Para qué |
|---|---|
| `negocio/` | Quiénes somos, marca y voz, audiencias, cobertura, cómo se reserva y se entrega, cómo se trabaja el día del evento |
| `servicios/` | Una ficha por servicio (qué es, qué vive el invitado, qué incluye y no, implementos, lugar, precios, frases, qué decir y no decir, ángulos de contenido, medios reales) |
| `packs/` | Packs y combinaciones; qué recomendar según el tipo de evento |
| `precios/` | Tarifario vigente y cómo se resolvieron las contradicciones |
| `en-camino/` | Servicios en preparación y novedades recientes |
| `reglas/` | Reglas de oro, tabla «no digas / di», estilo de mensajes de WhatsApp |
| `contenido/` | Formatos y cadencia, lo que ha funcionado, calendario, banco de ideas, plantillas de piezas, anuncios, web |
| `recursos/` | Mapa de fotos y videos reales, creadora digital, herramientas y skills útiles |
| `feed/` | Carruseles ya hechos y programados (`AAAA-MM-DD_tema/01.jpg…`): referencia de la línea visual aprobada; **no se editan** |
| `piezas/` | Lo que se produce semana a semana (`semana-01/…`), borradores y aprobadas por separado |
| `medios/` | Carpetas con los archivos reales (fotos, videos, audios, marca); ver `medios/LEEME.md` |
| `preguntas-abiertas.md` · `fuentes.md` · `log.md` · `index.md` | Dudas del dueño, de dónde sale cada dato, bitácora, catálogo |

**Orden de lectura:** este archivo → `reglas/reglas-de-oro.md` → la ficha del servicio que toca → `precios/tarifario-vigente.md` → `contenido/` según la pieza.

## Resumen de una pantalla (todo lo esencial)
- **Quiénes:** Herrera Producciones, base en Talca / San Clemente, trabajamos en el Maule (evaluamos fuera). Instagram `@herrera.producciones`. WhatsApp +56 9 5534 7032 · https://wa.me/message/MGETLZAA7XJ2A1.
- **Qué vendemos:** no el arriendo de una máquina: **lo que vive el invitado y el recuerdo que queda**. Entretención y recuerdos para eventos. Prioridad: matrimonios (sobre todo +100 invitados); también empresas, escolares, cumpleaños, baby showers, bautizos, galas.
- **Servicios activos (8):** Fotocabina · Punto Foto (nuevo, lanzado 22-oct-2026) · Plataforma 360 · Aero360 · Selfie Mirror · Eco de Amor · Arco hexagonal y Puertas de roble + arco (ceremonia) · extras (álbum, pendrive, fotos imantadas, horas adicionales).
- **Packs (8):** Dúo Content, Dúo de Fotos, Dúo Fiesta, Dúo Fiesta Digital, Dúo Digital, Pack Estrella, Todo Incluido Fotocabina, Todo Incluido Punto Foto. **Todos llevan Plataforma 360; la Aero360 se vende sola.**
- **Foco 2026-27:** matrimonios + más peso a empresas, malls, sindicatos y activaciones. Tú en público, usted en WhatsApp.
- **En camino (no anunciar como activos):** GlamCam / pasarela slow motion y Cápsula de Recuerdos (video guestbook). Ver `en-camino/`.
- **Dinero:** precios netos en CLP; particulares sin IVA, empresas con boleta/factura +19 %; traslado siempre aparte; abono fijo $25.000 que se descuenta; saldo 48 h antes. Detalle en `precios/`.
- **Qué necesita el lugar:** 3 × 3 m, energía cerca, acceso y estacionamiento, una persona que reciba, señal para los QR; exterior solo sin lluvia.
- **Cómo llegan los clientes:** casi siempre por anuncios y WhatsApp. Objetivo de las redes: **primero reservas, luego marca**.
- **CTA único:** «Escríbenos por WhatsApp».
- **Material:** clips y fotos **reales** de eventos de Herrera; las creadoras digitales solo como presentadoras. Ningún testimonio inventado.

## Reglas que nunca se rompen (versión corta; completas en `reglas/reglas-de-oro.md`)
1. Solo material real de eventos; nada inventado; sin filtros que cambien el color. Única excepción: las creadoras digitales como presentadoras (nunca como clientas ni testimonio).
2. No decir «matrimonio real», ni mencionar la pasarela, ni «backdrop»; los packs llevan solo Plataforma 360 (nunca Aero360).
3. Capacidades exactas: Aero360 máx. 12 · Plataforma 360 hasta 4 adultos por video · Fotocabina hasta 6 por sesión · Punto Foto más de 6 si el espacio lo permite.
4. «Ilimitadas» solo «durante el servicio contratado». Punto Foto no es ilimitado: hasta 216 tiras impresas por evento, luego solo digital.
5. Precios en el feed orgánico: no. En historias sí (nunca en destacadas) y en anuncios como «desde $…».
6. Nada de urgencia o escasez falsas, rankings ni cifras de conversión inventadas.
7. Nada se publica, se gasta ni se envía sin aprobación del dueño. Se trabaja **una semana a la vez, aprobando antes de producir**.

## Cómo trabajar una pieza (protocolo)
1. **Entender el pedido:** servicio, tipo de evento, formato, objetivo (reserva o marca).
2. **Leer** la ficha del servicio y `reglas/afirmaciones-di-y-no-digas.md`.
3. **Buscar respaldo:** `contenido/lo-que-ha-funcionado.md` y `contenido/banco-de-ideas.md`; si hay un patrón que aplique, usarlo y decirlo.
4. **Elegir material real** en `recursos/mapa-de-medios.md` (que exista y tenga permiso).
5. **Escribir** con la plantilla de `contenido/plantillas-de-piezas.md`, en el tono de `negocio/marca-y-voz.md`.
6. **Revisar** contra las reglas de oro y entregar listo para copiar, con una línea que diga qué supuestos se hicieron.
7. Si falta un dato: escribir «(sin confirmar)» y preguntar lo mínimo. **Nunca rellenar con suposiciones.**

## Jerarquía de la verdad
Corrección reciente del dueño sobre el mismo dato → `precios/tarifario-vigente.md` y fichas de `servicios/` → resto. Si dos páginas se contradicen, manda la de fecha más nueva y se anota en `preguntas-abiertas.md`. Marcas usadas: **[CONFIRMADO]** lo dijo el dueño · **[CALCULADO]** sale de una regla suya · **[HIPÓTESIS]** idea no comprobada (no publicar como hecho) · **[INTERNO]** sirve para vender, no para publicar · **[PENDIENTE]** falta decisión.

## Mantención
- Cada hecho nuevo o corregido se escribe en la página que toca y se anota al final de `log.md` (fecha, qué cambió, fuente). Si cambia una tarifa, se corrige solo en `precios/tarifario-vigente.md` y se revisan las fichas.
- No se duplican datos: una cosa vive en un solo lugar y las demás páginas la enlazan.
- Este cerebro es **INTERNO**: no pegar texto de aquí tal cual en publicaciones; escribir la versión editorial.
- El dueño no es programador, habla español de Chile y lee solo el chat: todo lo que requiera su decisión se le presenta en el chat, en lenguaje simple, con la recomendación primero.
