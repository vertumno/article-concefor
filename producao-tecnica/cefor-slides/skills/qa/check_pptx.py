#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Checagem tecnica de um .pptx do cefor-slides (Stage 05).

Verifica:
  - placeholders residuais no XML dos slides ({{ }}, [INSTRUCTOR_NAME], etc.);
  - numero de slides;
  - slides sem nenhum texto (possivel <div>/<span> sem tag, ou shape vazio).

Uso:
  python check_pptx.py caminho/para/deck.pptx [--json]
Portado de check_pptx_placeholders.py da skill slide-creator, com checagens extra.
"""
from __future__ import annotations
import argparse
import json
import re
import zipfile
from pathlib import Path

PLACEHOLDER_PATTERNS = ["{{", "}}", "[INSTRUCTOR_NAME]", "[SESSION_TITLE]",
                        "[SESSION_SLUG]", "{{MATH:", "PLACEHOLDER"]


def check(path: Path) -> dict:
    matches, empty_slides = [], []
    with zipfile.ZipFile(path) as z:
        slide_xmls = sorted(n for n in z.namelist()
                            if re.match(r'ppt/slides/slide\d+\.xml$', n))
        for name in slide_xmls:
            raw = z.read(name)
            text = raw.decode("utf-8", "ignore")
            for pat in PLACEHOLDER_PATTERNS:
                if pat in text:
                    matches.append({"file": name, "pattern": pat})
            # texto visivel = conteudo de <a:t>...</a:t>
            visible = "".join(re.findall(r'<a:t>(.*?)</a:t>', text, re.S)).strip()
            if not visible:
                empty_slides.append(name)
    errors = []
    if matches:
        errors.append(f"{len(matches)} placeholder(s) residual(is)")
    if empty_slides:
        errors.append(f"{len(empty_slides)} slide(s) sem texto: {', '.join(empty_slides)}")
    return {"pptx": str(path), "slides": len(slide_xmls),
            "status": "pass" if not errors else "fail",
            "errors": errors, "placeholders": matches}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("pptx")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    rep = check(Path(a.pptx))
    if a.json:
        print(json.dumps(rep, ensure_ascii=False, indent=2))
    else:
        print(f"status: {rep['status']}  | slides: {rep['slides']}")
        for e in rep["errors"]:
            print(f"  ERRO: {e}")
        for m in rep["placeholders"]:
            print(f"    placeholder {m['pattern']} em {m['file']}")
    return 0 if rep["status"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
