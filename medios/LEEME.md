# Medios (carpeta para los archivos reales)

Este cerebro guarda **texto**; los archivos pesados (fotos, videos, audios, logos, fuentes) van aquí cuando se suban al repo. Catálogo de qué hay y para qué sirve: `recursos/mapa-de-medios.md`.

## Estructura propuesta
```
medios/
  marca/            logos (SVG/PNG), monograma, patrones, fuentes, uniforme
  servicios/        un subdirectorio por servicio: fotocabina/, punto-foto/, plataforma-360/,
                    aero360/, selfie-mirror/, eco-de-amor/, ceremonia/, album/
  eventos-reales/   fotos y frames de eventos (con ficha de permiso)
  stories-referencias/   frames por servicio (los 4 marcados para limpiar, aparte)
  creadora/         aprobadas/ · pruebas/   (en pausa)
  voz-y-audio/      voz aprobada, música libre de derechos (con licencia anotada)
  piezas-por-semana/  semana-01/ …  (borradores y aprobadas por separado)
```

## Reglas
- **Originales intactos:** nunca sobrescribir; las ediciones van en `piezas-por-semana/`.
- Nombre de archivo: `servicio_descripcion_AAAAMMDD.ext` en minúsculas, sin espacios.
- Cada carpeta lleva un `fichas.csv`: archivo, qué es, origen, **permiso (sí/no)**, personas reconocibles (sí/no), estado (borrador/aprobado), nota.
- Solo entra material con permiso. Lo que no es de Herrera (inspiración, competencia) va marcado «solo referencia» y **no se republica**.
- Videos pesados: usar Git LFS o un almacenamiento aparte (Drive) y dejar aquí el enlace en la ficha.
- Tamaño actual de la biblioteca de origen: ~1,5 GB en la biblioteca de marca + ~0,8 GB en la carpeta «Recursos» (39 videos y fotos).
