# Material de terceros incluido en `.claude/`

| Qué | Origen | Licencia |
|---|---|---|
| `agents/` (17 de los 18 archivos, todos menos `director-de-contenido.md`) | colección «agency-agents» (AgentLand Contributors) | MIT |
| `skills/stop-slop/` | skill «stop-slop» (trae su propio `LICENSE`) | ver `skills/stop-slop/LICENSE` |
| `skills/ig-*` (13 skills de Instagram) | paquete de skills `ig-*` descargado por el dueño; **sin archivo de licencia incluido** | sin confirmar |
| `agents/director-de-contenido.md`, `herramientas/` | escritos para este repo | del dueño |

Las `ig-*` se revisaron antes de incluirlas: sus 6 scripts usan solo la biblioteca estándar de Python y no hacen llamadas de red, no borran archivos ni leen claves. Están pensadas para inglés: en español sirven para estructura, largo y revisión, pero sus listas de «palabras de IA» y fórmulas de gancho son en inglés.

Los plugins (`matriz-viralidad`, `creative-architect`, `hyperframes`, `canva`) **no se copian**: se activan desde `settings.json` y se descargan de sus propios repositorios la primera vez.
