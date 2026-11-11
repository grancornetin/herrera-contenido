#!/usr/bin/env python3
"""Imprime el enlace público (raw de GitHub) de uno o más archivos del repo,
listo para pegar en Metricool. Solo biblioteca estándar.

Uso:  python herramientas/enlace_publico.py piezas/semana-02/reel-1.mp4 [otro archivo ...]
      python herramientas/enlace_publico.py --carpeta feed/2026-11-05_punto-foto-o-fotocabina
"""
import argparse
import subprocess
import sys
import urllib.parse
from pathlib import Path

REPO = "grancornetin/herrera-contenido"
RAMA = "main"
LIMITE_MB = 100  # GitHub rechaza archivos de más de 100 MB


def raiz():
    out = subprocess.run(["git", "rev-parse", "--show-toplevel"], capture_output=True, text=True)
    return Path(out.stdout.strip()) if out.returncode == 0 else Path(__file__).resolve().parents[1]


def enlace(ruta_rel: str) -> str:
    return f"https://raw.githubusercontent.com/{REPO}/{RAMA}/" + urllib.parse.quote(ruta_rel.replace("\\", "/"))


def sin_subir(r: Path, rel: str) -> bool:
    """True si el archivo no está en el último commit subido a origin."""
    s = subprocess.run(["git", "-C", str(r), "ls-tree", "-r", "--name-only", f"origin/{RAMA}", "--", rel],
                       capture_output=True, text=True)
    return s.returncode != 0 or not s.stdout.strip()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("archivos", nargs="*")
    ap.add_argument("--carpeta")
    a = ap.parse_args()
    r = raiz()
    lista = [Path(x) for x in a.archivos]
    if a.carpeta:
        lista += sorted(p for p in (r / a.carpeta).iterdir() if p.is_file())
    if not lista:
        ap.error("indica archivos o --carpeta")
    for p in lista:
        ab = (p if p.is_absolute() else Path.cwd() / p).resolve()
        if not ab.exists():
            print(f"NO EXISTE: {p}", file=sys.stderr)
            continue
        rel = ab.relative_to(r).as_posix()
        aviso = []
        if ab.stat().st_size > LIMITE_MB * 1024 * 1024:
            aviso.append(f"pesa más de {LIMITE_MB} MB: GitHub no lo aceptará")
        if " " in rel:
            aviso.append("el nombre tiene espacios: mejor renombrarlo con guiones")
        if sin_subir(r, rel):
            aviso.append("AÚN NO ESTÁ SUBIDO: el enlace no funcionará hasta hacer commit y push")
        print(enlace(rel) + (("   <-- " + "; ".join(aviso)) if aviso else ""))


if __name__ == "__main__":
    main()
