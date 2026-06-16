#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Valida um outline do cefor-slides (Stage 03) contra as regras Assertion-Evidence.

Regras (ver shared/methodology.md, stages/03-outline/references/):
  - todo slide declara um Pattern;
  - slides de conteudo tem Assertion (titulo-afirmacao) e Evidence;
  - a Assertion nao pode ser rotulo generico (Alley / anti-pattern "titulos fracos");
  - nao mais que 2 slides consecutivos com o mesmo Pattern (variedade de layout);
  - 1o slide = title-slide; ultimo = end-slide (aviso).

Uso:
  python validate_outline.py caminho/para/03-outline.md [--json]
Adaptado da logica de validate_deck_package.py da skill slide-creator.
"""
from __future__ import annotations
import argparse
import json
import re
import sys
from pathlib import Path

NO_CONTENT_PATTERNS = {"title-slide", "end-slide", "section-divider"}
# rotulos genericos reprovados como Assertion (anti-pattern: titulos fracos)
GENERIC_LABELS = {
    "introducao", "introdução", "conceitos", "conteudo", "conteúdo", "agenda",
    "objetivos", "sumario", "sumário", "conclusao", "conclusão", "avaliacao",
    "avaliação", "resultados", "metodologia", "referencias", "referências",
    "tema", "topico", "tópico", "resumo",
}


def parse_slides(text: str) -> list[dict]:
    slides = []
    blocks = re.split(r'^###\s+', text, flags=re.M)[1:]
    for b in blocks:
        head, *rest = b.splitlines()
        body = "\n".join(rest)
        fields = {}
        for m in re.finditer(r'-\s*\*\*(.+?):\*\*\s*(.+)', body):
            fields[m.group(1).strip().lower()] = m.group(2).strip().strip('"').strip("'")
        slides.append({"head": head.strip(), "fields": fields})
    return slides


def field(s: dict, *names: str) -> str:
    for n in names:
        for k, v in s["fields"].items():
            if k.startswith(n):
                return v
    return ""


def validate(path: Path) -> dict:
    errors, warnings = [], []
    text = path.read_text(encoding="utf-8")
    slides = parse_slides(text)
    if not slides:
        return {"file": str(path), "slides": 0, "status": "fail",
                "errors": ["nenhum slide '### Slide' encontrado"], "warnings": []}

    prev_pattern, run = None, 0
    for i, s in enumerate(slides, 1):
        pattern = field(s, "pattern").lower()
        assertion = field(s, "assertion")
        evidence = field(s, "evidence")
        notes = field(s, "speaker notes", "notes")

        if not pattern:
            errors.append(f"slide {i}: sem Pattern")

        is_content = pattern not in NO_CONTENT_PATTERNS and pattern != ""
        if is_content:
            if not assertion:
                errors.append(f"slide {i}: sem Assertion (titulo-afirmacao)")
            else:
                words = assertion.split()
                if assertion.strip().lower().rstrip(":") in GENERIC_LABELS or len(words) < 3:
                    errors.append(f"slide {i}: Assertion parece rotulo generico -> '{assertion}'")
                if len(words) > 18:
                    warnings.append(f"slide {i}: Assertion longa ({len(words)} palavras)")
            if not evidence:
                errors.append(f"slide {i}: sem Evidence (corpo deve ser evidencia visual)")
        if notes and assertion and notes.strip().lower() == assertion.strip().lower():
            warnings.append(f"slide {i}: nota igual ao titulo (redundancia - Mayer)")

        if pattern and pattern == prev_pattern:
            run += 1
        else:
            run = 1
        prev_pattern = pattern
        if run > 2:
            errors.append(f"slide {i}: mais de 2 slides consecutivos com pattern '{pattern}'")

    if field(slides[0], "pattern").lower() != "title-slide":
        warnings.append("1o slide nao e title-slide")
    if field(slides[-1], "pattern").lower() != "end-slide":
        warnings.append("ultimo slide nao e end-slide")

    return {"file": str(path), "slides": len(slides),
            "status": "pass" if not errors else "fail",
            "errors": errors, "warnings": warnings}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("outline", help="arquivo markdown do outline (Stage 03)")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    rep = validate(Path(a.outline))
    if a.json:
        print(json.dumps(rep, ensure_ascii=False, indent=2))
    else:
        print(f"status: {rep['status']}  | slides: {rep['slides']}")
        for e in rep["errors"]:
            print(f"  ERRO:  {e}")
        for w in rep["warnings"]:
            print(f"  aviso: {w}")
    return 0 if rep["status"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
