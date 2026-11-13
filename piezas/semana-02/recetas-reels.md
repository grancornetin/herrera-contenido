---
tipo: piezas
actualizado: 2026-11-13
fuentes: [sesión del 13-nov con el dueño]
---
# Recetas de los reels de la semana 2

Sirven para **rearmar cada reel en cualquier sesión** sin depender de archivos temporales. Cada toma dura 0,8 s salvo que se indique. Formato 1080 × 1920, 30 cps, sin texto, sin voz.

Corte con ffmpeg (siempre con `-nostdin`, entrada y salida explícitas, nunca con comodines `*` en la entrada; ver «Lección» abajo):
`ffmpeg -nostdin -ss INICIO -t DURACION -i ORIGEN -map 0:v:0 -vf "scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,setsar=1,fps=30,format=yuv420p" -an toma.mp4`
Clips grabados en HDR (IMG_3327, IMG_3329): antes del escalado agregar
`zscale=tin=arib-std-b67:min=bt2020nc:pin=bt2020:t=linear:npl=203,format=gbrpf32le,zscale=p=bt709,tonemap=hable:desat=0,zscale=t=bt709:m=bt709:r=tv,`

## 1. Reel Fotocabina v5 · APROBADO (13-nov) · falta música
Solo **cabina inflable** (no mezclar con el fondo del tótem solo; regla del dueño). 10 tomas, 8 s.
| # | Origen (`medios/servicios/fotocabina/`) | Desde (s) | Qué se ve |
|---|---|---|---|
| 1 | m12 (cámara rápida) | 0,0 | Grupo grande con máscaras y gorros |
| 2 | m39 | **7,5** | Grupo completo posando (antes 0,3: pose rara, rechazado) |
| 3 | m11 | 0,3 | Novios posando |
| 4 | m16 | (ver v2) | Niño con gorra y señora con cotillón |
| 5 | **IMG_3828** (evento 13-nov) | **15,2** | Segunda tira saliendo de la impresora (antes m10 → rechazado por poco aspiracional; luego IMG_3865 → rechazado por fondo del tótem) |
| 6 | m16 | (ver v2) | Tótem dentro de la cabina con pantalla |
| 7 | m19 | (ver v2) | Grupo con sombreros y antifaces |
| 8 | m16 | (ver v2) | Novia con velo y grupo |
| 9 | m37 | (ver v2) | Novios con invitada de verde |
| 10 | m12 | ~3,5 | Grupo final con novia |
Las tomas «ver v2» son las del reel v2 aprobado el 12-nov (`herrera-piezas/semana-02/reel-fotocabina.mp4`): para rearmar se parte de ese archivo y se reemplazan solo los tramos 0,8–1,6 s (toma 2) y 3,2–4,0 s (toma 5).
**Pendiente:** música de nuestro estilo sincronizada a los cortes (ver abajo) → subir a `herrera-piezas/semana-02/reel-fotocabina.mp4` (mismo nombre, mismo enlace) → programar en Metricool.

## 2. Reel Fotocabina · Empresas v4 · APROBADO (13-nov) · falta música
Todo del **evento de empresa del 13-nov** (solo tótem, sin cabina inflable). 9 tomas, 8 s. Cada grupo aparece una vez, salvo el trío que abre y cierra (pedido del dueño).
| # | Origen | Desde (s) | Dura | Qué se ve |
|---|---|---|---|---|
| 1 | IMG_3903 | 5,5 | 0,8 | Trío mirando sus tiras y riéndose (gancho) |
| 2 | IMG_3866 | 2,5 | 0,8 | **Grupo wow**: sombreros, antifaz, escarapela «100% fiel» |
| 3 | IMG_3853 | 3,0 | 0,8 | Grupo de mujeres con carteles |
| 4 | IMG_3894 | 1,0 | 0,8 | Grupo riéndose, cartel «Jefa, ¿me va a creer?» |
| 5 | IMG_3830 (4K) | 3,0 | 0,8 | Mesa de cotillón (al medio, pedido del dueño) |
| 6 | IMG_3828 | 15,2 | 0,8 | Segunda tira saliendo de la impresora |
| 7 | IMG_3838 | 4,6 | 0,7 | Dos tiras en la mano (logo del cliente) |
| 8 | IMG_3327 (HDR) | 0,5 | 0,8 | Grupo grande mostrando sus tiras |
| 9 | IMG_3904 | 2,3 | 1,6 | Cierre: el mismo trío mostrando sus tiras |
Descartadas por el dueño: pantalla del tótem con cuenta regresiva (IMG_3906, «no me gusta»), primera tira saliendo (IMG_3828 desde 14,0). Sin usar: IMG_3901 (repite al del sombrero amarillo de 3894), IMG_3329 (movida), IMG_3839 (de espalda), IMG_3891 (sale el equipo), IMG_3898 (tótem solo en pasillo).
**Pendiente:** el dueño puede mandar **más grupos** distintos para reemplazar o sumar; luego música y programación.

## Música y publicación del reel de empresas (13-nov) · PROGRAMADO
- El dueño no subió canción: se usó la **música disco-funk 2 de ElevenLabs** (`nyvuKUdxHq1BqtLnw9v6`, 125 BPM exactos, un golpe = 0,48 s; ver `recursos/produccion-de-anuncios.md` §3). Se eligió la 2 porque arranca con toda la energía (la 1 es suave los primeros ~6 s).
- **Sincronización elegida por el dueño:** cada toma se estira a **2 golpes = 0,96 s** (imagen al 83 % de velocidad, cámara lenta suave) y el cierre del trío a **4 golpes**. Música desde 0,012 s, desvanecido final de 0,7 s. Resultado: 9,6 s, 1080 × 1920, H.264 ~8 Mbps, AAC 48 kHz. Script: `herramientas/reels/sincronizar_musica.py`.
- Cortes del v4 sin música (para el script): `0,0.8333,1.6333,2.4333,3.2333,4.0667,4.9,5.6,6.4,7.9667` · golpes `2,2,2,2,2,2,2,2,4`.
- Probadas y **rechazadas**: video a velocidad normal con la música acelerada a 150 BPM (canción 2 y canción 1). El dueño prefirió la cámara lenta suave.
- Subido a `herrera-piezas/semana-02/reel-fotocabina-empresas.mp4`. Programado en Metricool el **vie 13-nov 21:00**, publicación automática.
- **Caption aprobado** (pasó por `ig-caption`, `ig-human` y Brand Guardian):
> Fotocabina para empresas: cada persona que participa se lleva su tira impresa al instante, con el logo de tu empresa.
>
> Cotillón, carteles y risas entre compañeros. Hasta 6 personas por sesión, con fotos impresas ilimitadas durante el servicio.
>
> Nosotros llevamos el equipo y lo operamos. Tú disfrutas con tu gente.
>
> Para la fiesta de fin de año, aniversarios, sindicatos y activaciones en Talca y la Región del Maule.
>
> Escríbenos por WhatsApp y cuéntanos tu tipo de evento, la fecha y la comuna.
>
> #fotocabina #eventosdeempresa #talca

**Reel Fotocabina v5: EN PAUSA** (13-nov, el dueño: «contenido muy reciclado»). Si se retoma, se le pone música con el mismo script (cortes cada 0,8 s, 10 tomas de 2 golpes).

## Música (historial: opción B elegida el 13-nov)
- El dueño eligió **poner la música nosotros dentro del video** (antes la ponía él en Instagram). Estilo: disco / funk / fiesta 70–90.
- **Opción B:** el dueño sube una canción que se pueda usar comercialmente; se sincronizan los cortes al ritmo (cada corte en un tiempo del compás; a 125 BPM un tiempo = 0,48 s, dos tiempos = 0,96 s).
- Alternativa: la música disco-funk ya generada en ElevenLabs (ver `recursos/produccion-de-anuncios.md` §3). El 13-nov ElevenLabs y Metricool estaban **desconectados** en la sesión.

## Lección (13-nov) [INTERNO]
Un comando con comodín (`ls *…mov`) que no encontró el archivo listó todas las subidas y ffmpeg las tomó como **salidas**, sobrescribiendo dos videos del dueño (IMG_3903 y IMG_3906; los reenvió). Desde entonces: copiar las subidas a una carpeta aparte en solo lectura, trabajar sobre las copias, `-nostdin`, una entrada explícita por comando.

## Traspaso a la sesión siguiente (13-nov)
- Los dos reels aprobados **sin música** están en `piezas/semana-02/aprobadas/` (rama `claude/great-maxwell-uxblur`): `reel-fotocabina-v5-sin-musica.mp4` y `reel-fotocabina-empresas-v4-sin-musica.mp4`. Se trabaja sobre ellos; no hace falta rearmarlos.
- **Ritmo de los cortes:** casi todas las tomas duran 0,8 s → la música calza sin recortar a **75 BPM** (1 tiempo = 0,8 s) o **150 BPM** (2 tiempos = 0,8 s). En el de empresas la toma 7 dura 0,7 s y el cierre 1,6 s: ajustar a la grilla si hace falta. Si la canción tiene otro tempo, se mueve el inicio de la canción para que el primer golpe fuerte caiga en el corte 1 y se revisa cada corte.
- Música dentro del video, volumen normal (no hay voz). Exportar 1080 × 1920, AAC 48 kHz.
- Después: subir a `herrera-piezas/semana-02/` como `reel-fotocabina.mp4` (reemplaza al v2, mismo enlace) y `reel-fotocabina-empresas.mp4`, sacar los enlaces con `enlace_publico.py`, redactar los dos captions (CTA único «Escríbenos por WhatsApp», sin precios, sin nombrar a la empresa cliente) y programar en Metricool con aviso al celular, **todo con aprobación del dueño**.
