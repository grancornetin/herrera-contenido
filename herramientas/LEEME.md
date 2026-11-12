# Herramientas

- `enlace_publico.py`: saca el enlace público (raw de GitHub) de archivos del repo para pegarlo en Metricool. Uso en `CLAUDE.md`.

## Plugins (se activan una vez por entorno)
`.claude/settings.json` declara los plugins `matriz-viralidad`, `creative-architect`, `hyperframes` y `canva`. Claude Code los descarga de sus repos la primera vez (en el PC aparece un aviso para confiar en el repo y aceptar). Si no aparecen, instalarlos a mano con `/plugin`.

## Claves (nunca van al repo)
- **Apify** (para `matriz-viralidad`): el dueño la pone en un archivo `.env` local o en las variables del entorno de Claude Code en la nube. **Nunca** se le pide ni se lee en el chat. `.env` está en `.gitignore`.
- Metricool, Higgsfield, Canva, Drive: se conectan desde la cuenta de Claude del dueño.

## Python
Las skills `ig-*` y `enlace_publico.py` necesitan Python 3 (solo biblioteca estándar).

## Anuncios (agregado el 12-nov)
- `anuncios/armar_anuncio.py`: monta un anuncio vertical (clips reales + voz + música + textos) con ffmpeg y Pillow.
- `anuncios/ejemplo_tanda_anuncios.py`: ejemplo con 6 anuncios armados (guiones de la ronda 2, ya reemplazados). Usar como plantilla.
- Antes de usarlos: abrir la sesión en el entorno de nube «Herrera Producciones contenido» y leer `recursos/produccion-de-anuncios.md`.
