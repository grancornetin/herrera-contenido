# Medios (fotos y videos reales listos para usar)

Todo es material **real** de eventos de Herrera, en versión **liviana** (videos H.264 de hasta 1080 px de ancho, **sin audio**, colores en SDR sin alterar; fotos de hasta 2000 px). Los **originales 4K/HDR siguen en el PC del dueño**: no están en este repo.
Catálogo de qué muestra cada archivo: `recursos/mapa-de-medios.md` (el ID `mNN` del nombre coincide con el catálogo).

## Estructura
```
medios/
  servicios/<servicio>/mNN-descripcion.mp4|jpg   39 clips y fotos por servicio:
      aero360, album, ceremonia, eco-de-amor, fotocabina, plataforma-360,
      punto-foto, selfie-mirror, varios-servicios
  eventos-reales/        8 fotos de eventos con permiso (cumpleaños, 360, Selfie Mirror de Karen y Franco, arco, Eco de Amor)
  marca/
    logos/               logo horizontal negro y blanco (PNG transparente), logo de la app
    uniforme/            maqueta de la polera del staff
    renders-producto/    tótem y cabina inflable (para no inventar equipos distintos)
    fuentes/             Sora y Montserrat
  referencias-stories/<servicio>/   ~80 frames mejorados como referencia para stories (1080 px)
piezas/
  semana-01/borrador/    los 4 reels de la semana 1 (sin música) y sus portadas
```

## Reglas
- **Enlace público de cualquier archivo:** `python herramientas/enlace_publico.py medios/servicios/fotocabina/m15-fotocabina-vista-exterior-con-invitados.mp4` (ver `CLAUDE.md`).
- Los videos van **sin audio**: la música (libre de derechos) se agrega en Instagram o al montar.
- Originales intactos en el PC; aquí solo copias livianas. Las ediciones nuevas van en `piezas/semana-NN/` (borrador y aprobado por separado).
- Nombres en minúsculas con guiones, sin espacios ni tildes. Límite de GitHub: 100 MB por archivo.
- Solo entra material con permiso. Lo que no es de Herrera (inspiración, competencia) **no se sube**: queda solo en el PC como referencia.
- Las referencias de stories son frames «mejorados» (no son originales): úsalas como guía de encuadre y no las presentes como fotos tomadas en un evento sin confirmar con el dueño. Los 4 marcados «para limpiar» (overlays/reflejos) **no se subieron**.

## Qué NO está aquí (sigue solo en el PC)
Originales 4K, la carpeta de la creadora digital (activa), fotos de inspiración de otros creadores, historias rescatadas y la versión 1 de los reels (rechazada).
Falta una foto: M20 (Plataforma 360, formato HEIC) no se pudo convertir.
