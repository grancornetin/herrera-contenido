---
tipo: recursos
actualizado: 2026-11-12
fuentes: [sesión del 12-nov con el dueño; Windsor, ElevenLabs, Higgsfield, Metricool]
---
# Producción de anuncios: cómo se hizo, dónde está cada cosa y qué sigue

**Léelo antes de retomar los anuncios.** Todo lo que no está en un archivo vive en las cuentas del dueño (ElevenLabs, Higgsfield, Meta) y se recupera con los códigos de abajo.

## 0. Para abrir una sesión nueva (importante)
- Empezar la sesión en el **entorno de nube «Herrera Producciones contenido»** (con los dos repos). Es el que permite descargar de ElevenLabs y Higgsfield. En el entorno «Default» esas descargas quedan bloqueadas.
- Hosts permitidos en ese entorno: `elevenlabsusercontent.com`, `cdn.higgsfield.ai`, `d1xarpci4ikg0w.cloudfront.net`, `upload.higgsfield.ai`, `d8j0ntlcm91z4.cloudfront.net` (informes del predictor).
- Conectores que deben estar activos en la cuenta de Claude: **Metricool, Windsor.ai (Meta Ads), ElevenLabs, Higgsfield, GitHub**. Si no aparecen, avisar al dueño para que los reconecte en claude.ai/customize/connectors y abra otra sesión.
- Repos: `grancornetin/herrera-contenido` (este, debe pasar a privado: lo hace el dueño desde el PC) y `grancornetin/herrera-piezas` (público, solo piezas aprobadas; enlaces para Metricool).

## 1. Flujo de un anuncio
1. Guion con gancho (skill `ig-reel`: `hookscore.py`, `beats.py`; agente Ad Creative Strategist) → aprobación del dueño. Guiones aprobados: `contenido/guiones-anuncio-pack-estrella.md`.
2. Voz de Pía en ElevenLabs (§3). Medir las pausas de cada audio con `ffmpeg … silencedetect` para cortar los clips.
3. Montaje con `herramientas/anuncios/armar_anuncio.py` (ver `ejemplo_tanda_anuncios.py`): clips reales de `medios/servicios/` cortados en las pausas de la voz + texto en la mitad inferior + música a volumen 0,20.
4. Revisar fotogramas (que el texto no tape caras) → enviar al dueño por el chat.
5. Medir con el predictor de Higgsfield (máx. **16 s** por video y **2 trabajos a la vez**).
6. Los ganadores se suben a Meta como anuncios separados dentro del mismo conjunto, siempre **en pausa**; solo el dueño los activa.

## 2. Estilo de los anuncios (decisiones del dueño)
- Los **anuncios llevan texto, música y voz** (a diferencia de los reels orgánicos, que van limpios y sin voz).
- Texto **estilo A [CONFIRMADO, 13-nov]**: titular Sora 800 grande, una palabra clave en champagne #CFAF74, complementa a la voz (no la repite), precio grande. Letra con sombra suave, **en la mitad inferior**, terminando antes del 72 % de la altura (y≈1380 de 1920) para no chocar con la interfaz de Instagram. Sin cuadros ni animaciones de relleno.
- Primer segundo: el clip con más movimiento (360 girando). Primer clip y texto visibles desde el cuadro 1.
- Tarjetas de reseña: **motion graphics y con 5 estrellas** (el dueño confirmó que todas las tienen). Aún no hechas (la versión sin animación se descartó).
- **Luz:** el «lowkey» por corrección de color se **rechazó** (se pierden detalles, parece un degradé). Quiere luz **uniforme, cinematográfica y cuidada** en todo el video. La corrección de color no crea luz; la opción real es reiluminar con IA siguiendo la guía de 24 esquemas de luz de Higgsfield: (1) sacar un frame y relucirlo con Nano Banana Pro 4K («Relight this exact photo with [LUZ]. Keep everything else identical…»), (2) pasar el clip + la foto a Seedance 2.5 Edit 1080p («Edit only the lighting of this video… Lighting stays constant…»). Cotizado: `seedance_2_5` con `video_references` ≈ **35 créditos por tramo de 5 s**. **Pendiente** que el dueño apruebe una prueba de 35 créditos en el gancho.

## 3. ElevenLabs (voz de Pía y música)
- Voz: **Pia**, `voice_id 7lM6ne5oGCjAMr4g5EQc` (generada, español). Modelo `eleven_v4`.
- **Acento:** sin etiqueta sonaba argentino en LL/Y. La mejor prueba (elegida por el dueño): comenzar el texto con `[strong Chilean accent] [warmly]`. Escribir «tres sesenta» y las cifras en palabras («doscientos cuarenta mil»).
- **Tono:** v4 acepta etiquetas libres. Para ironía seca: `[dry] [sarcastic]`, `[deadpan] [matter-of-fact]`. Para ritmo, las etiquetas `[energetic] [fast pace]` casi no cambian nada: se aceleró con ffmpeg (`atempo 1.14` en los primeros 5,9 s).
- El plan gratuito se bloqueó por «actividad inusual» (uso desde la nube). **El dueño pasó a plan pagado.** Límite de 2–3 generaciones a la vez: las demás reintentan solas.
- Música: `eleven_music_v2_5`, prompt «disco-funk de fines de los 70, bronces, bajo funky, 125 BPM, sin voces». **No se confirmó que no traiga voz cantada** (el transcriptor falló por saturación): el dueño no se quejó al oírla bajo la voz.
- Flow de trabajo: `Ewr863D1kOokTeEczqoF` (https://elevenlabs.io/app/flows/Ewr863D1kOokTeEczqoF). Para volver a bajar un audio: `creative_get_flow_run_status` con el flow y el `session_id`; entrega una URL firmada nueva.

| Qué | generation_id | session_id | Estado |
|---|---|---|---|
| **G10 Maule** (15,8 s) | 3JGDwvOurYjZX8dE1Jp2 | 871LpqtOoX7k62gxHOLS | **APROBADA** |
| **G11 Indecisión** (11,7 s) | P6omBlLyaqm6oBwGa68G | rvea2sUEPJaX5bet8me4 | **APROBADA** |
| **G7 Infaltables v2** (21,4 s; después se aceleró el arranque → 20,8 s) | 1BufwcpCjTABWchHr5Iy | zWInuhBla8qDzJAKt777 | Aprobada «acelerando el arranque» (la versión acelerada se hace de nuevo con ffmpeg) |
| **G12 Organizadora, toma A** seca (15,6 s) | NvOCN8KL4zzrKmE0943l | oqv75FHWNtehW9namPmd | **Esperando elección A o B** |
| **G12 Organizadora, toma B** «Okey, organizaste todo… ¿pero ya resolviste…?» (17,3 s) | BPavxbflxxRirN4bQMm5 | X2Ef7WvJXl8gBRDY2VrI | **Esperando elección A o B** |
| **G12 FINAL** (15,96 s) = inicio de la toma B + puente 1 | inicio: BPavxbflxxRirN4bQMm5 · final: EVrg31F88rvKgeyRwY8d | X2Ef7WvJXl8gBRDY2VrI · 6Rr2D3168zq0Z8mfeF4v | **APROBADA 13-nov.** Archivo: `piezas/semana-02/aprobadas/g12-voz-final.mp3`. Armado: de la toma B se quita la pausa 1,72–2,44 s (y se acorta la de 0,46–0,69), los primeros 4,6 s ×1,10 (atempo), se corta en 4,30 s; el final se le acortan pausas a 0,14 s; ambos a −16 LUFS; todo ×1,067 (atempo) para quedar en 16 s. **No usar rubberband ×1,5 en una palabra: suena a ardilla.** |
| G12 puentes descartados | «Tranqui…» 4Ytojdul0jCHVoCfuNCe, sFJ5AMbFWVHmIKXzM6b2, WhG8elkCEsNABdEe8QxB, MFPGkwfY2QDtplzRtHk7 · «Para eso estamos» Ev9jDxXIbEWbZl8MHYOm · «Eso déjanoslo a nosotros» OEYxiAnwe7t1s5cUPtfR | — | Descartados 13-nov |
| Música disco-funk 1 (30 s) | vwCM6r8vx26UJsYXgrOk | rewTad0pQg9ASirjs1Xr | Usada en todo |
| Música disco-funk 2 (30 s) | nyvuKUdxHq1BqtLnw9v6 | XinFKzWrv7R53HGnKBUt | Alternativa |
| G7 original (22 s) | 2xtqHG447X4orQHDZyRt | rprqrMy5to10AkuHZzOS | Reemplazada |
| G12 original (tono «sorprendido») | MTch1YEv6eJ4uHu5S6TX | 5WkbH6UsIwqWMkoj7yr8 | Rechazada |
| G3 decoración / G5 momento muerto | MPmZ6Vm7IWvqVsrcAyTb / 4b7opvHwLuvANxe71akU | 5rgfKHPVaYuYsKTKfCNU / APl7WF2BgjL7p8CLDRKl | Descartadas |
Pruebas de acento: etiqueta chilena P1avJkE3FpASahFC1KM5 (**elegida**), fonética raFUY2Lmq9XptavQwkGk, multilingüe L69M3c1OLVOUHCOZgXh3.

## 4. Higgsfield
- Créditos al 12-nov: ~850 (plan Ultimate). La voz de Pía NO está en Higgsfield (está en ElevenLabs). Las caras de las creadoras están como Soul en Higgsfield.
- Predictor de viralidad (`virality_predictor`): sube un video (`media_upload` → PUT → `media_confirm`) y crea el trabajo; el informe es un HTML en `d8j0ntlcm91z4.cloudfront.net`. Resultado del primer anuncio (E2, versión mudita con texto, 15,9 s): **total 43, gancho 28, viral 42, retención 95**. Trabajos aún sin leer: `c40a1e96-ebba-4470-937f-d62286679371` (E4), `165583a2-c9f8-4c40-8a46-bbfddce07a8f` (E1). Son de versiones anteriores a las actuales. **G12 «La organizadora» (estilo A, 16 s, 13-nov): total 42, gancho 27, viral 39, retención 96** (trabajo `1ec09707-4e2a-4981-98f5-3dd7ed0ef82b`). Igual que E2: retención muy alta y gancho débil; el pico de actividad está en el segundo 0 y baja después.
- Medios subidos (por si se reutilizan): e2 `bd1019e6-6f51-4c91-a401-429df7563166`, e4 `5277ffc1-7946-43d3-aabc-d0af141d2417`, e1 `2c011cb2-7083-48ff-9f75-f4daad444fce`, e5 `839c80c7-8a74-443b-9e12-e8c033c40fbd`.

## 5. Meta Ads (vía Windsor, cuenta publicitaria «Nicolás Herrera» 972714354585643)
Todo **en pausa**. Detalle en `contenido/anuncios-meta.md`. IDs: campaña `120248484295110146` · conjunto `120248484297960146` (mujeres 24–55, Maule, $49.000 del 14-nov al 13-dic, destino WhatsApp) · anuncio `120248485975740146` con el **video antiguo sin voz** (id de video Meta `1725820612434100`). **Hay que reemplazarlo por los anuncios nuevos** (con `create_ad_video` + `create_ad`, o `update_ad_creative`). El video debe estar en una URL pública: subirlo a `herrera-piezas/semana-02/` **solo cuando el dueño lo apruebe**. Meta rechaza menos de ~$1.670 diarios por conjunto.

## 6. Qué sigue (en orden)
1. El dueño elige **G12: toma A o B**.
2. Montar G7, G10, G11 y G12 (voz + música + clips + textos). Hay un ejemplo completo en `herramientas/anuncios/ejemplo_tanda_anuncios.py` (versiones anteriores de los guiones).
3. Hacer las **tarjetas de reseña en motion graphics con 5 estrellas** (solo si se retoma el guion de reseñas, hoy en pausa).
4. Decidir la **prueba de luz con IA** (35 créditos).
5. Medir en Higgsfield, elegir 2–3 y subirlos a Meta (en pausa) para que el dueño los active.
6. Elegir cuáles ganchos nuevos de la guía de ARIA se desarrollan (ver `contenido/banco-de-ideas.md`).
7. Grabar en el próximo evento: tira impresa en la mano, impresora, celular recibiendo la foto y la **reacción de un invitado** viendo su video.
