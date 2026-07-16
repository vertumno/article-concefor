#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
make-zip.py - Regenera o pacote cefor-slides.zip a partir da pasta da skill.

Empacota a pasta cefor-slides/ inteira (prefixo "cefor-slides/" dentro do zip,
como o Claude Web espera) na raiz do repositorio. Rode apos QUALQUER alteracao
na skill para o zip nunca driftar do codigo.

Uso:
    python scripts/make-zip.py [saida.zip]     # default: ../cefor-slides.zip
"""
import os
import sys
import zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
SKILL = os.path.dirname(HERE)                    # .../cefor-slides
ROOT = os.path.dirname(SKILL)                    # raiz do repo
PREFIX = os.path.basename(SKILL)                 # "cefor-slides"

EXCLUDE_DIRS = {"__pycache__", ".git", ".cefor-slides"}
EXCLUDE_EXTS = {".pyc", ".odp"}


def main():
    out = sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, f"{PREFIX}.zip")
    count = 0
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        for dirpath, dirnames, filenames in os.walk(SKILL):
            dirnames[:] = sorted(d for d in dirnames if d not in EXCLUDE_DIRS)
            for fn in sorted(filenames):
                if os.path.splitext(fn)[1].lower() in EXCLUDE_EXTS:
                    continue
                full = os.path.join(dirpath, fn)
                rel = os.path.join(PREFIX, os.path.relpath(full, SKILL)).replace(os.sep, "/")
                z.write(full, rel)
                count += 1
    kb = os.path.getsize(out) // 1024
    print(f"[OK] {out} - {count} arquivo(s), {kb} KB")


if __name__ == "__main__":
    main()
