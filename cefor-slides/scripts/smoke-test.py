#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
smoke-test.py — Testes de fumaça da skill cefor-slides (stdlib apenas).

Roda em segundos e pega regressões nos dois scripts principais:

  new-deck.py      : round-trip A/B, escape de título, @media print, fonte
                     embutida (offline), 'active' no 1º slide, tokens obrigatórios.
  generate-odp.py  : exemplos A e B → ODF válido, tabela ODF real presente,
                     KPIs extraídos, nenhum slide perdido em silêncio.

Uso:
    python scripts/smoke-test.py

Sai com código 0 (tudo verde) ou 1 (alguma falha). generate-odp é pulado
com aviso se o odfpy não estiver instalado.
"""
import os
import re
import subprocess
import sys
import tempfile
import zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
SKILL = os.path.dirname(HERE)
NEW_DECK = os.path.join(HERE, "new-deck.py")
GEN_ODP = os.path.join(HERE, "generate-odp.py")
EXEMPLOS = [os.path.join(SKILL, "exemplos", "exemplo-versao-a.html"),
            os.path.join(SKILL, "exemplos", "exemplo-versao-b.html")]

CORPOS = """<section class="slide">
  <h1 class="t-capa">Capa de Teste</h1>
</section>
<section class="slide">
  <div class="barra-titulo"><h2 class="t-conteudo">Conteúdo</h2></div>
  <ul><li>Item um</li><li>Item dois</li></ul>
</section>
"""

resultados = []


def check(nome, cond, detalhe=""):
    resultados.append((nome, bool(cond)))
    status = "OK  " if cond else "FALHA"
    msg = f"[{status}] {nome}"
    if detalhe and not cond:
        msg += f" — {detalhe}"
    print(msg)


def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
    return r.returncode, (r.stdout or "") + (r.stderr or "")


def test_new_deck(tmp):
    corpos = os.path.join(tmp, "corpos.html")
    with open(corpos, "w", encoding="utf-8") as f:
        f.write(CORPOS)

    for versao in ("A", "B"):
        out = os.path.join(tmp, f"deck-{versao}.html")
        rc, log = run([sys.executable, NEW_DECK, "--version", versao,
                       "--title", "Metas & <Resultados> 2026", "--slides", corpos, "--out", out])
        check(f"new-deck {versao}: exit 0 e '[OK]'", rc == 0 and "[OK]" in log, log.strip()[:200])
        if rc != 0:
            continue
        html = open(out, encoding="utf-8").read()
        if versao == "A":
            check("new-deck A: título escapado no <title>",
                  "<title>Metas &amp; &lt;Resultados&gt; 2026</title>" in html)
            check("new-deck A: @media print presente", "@media print" in html)
            check("new-deck A: fonte Open Sans EMBUTIDA (offline)",
                  "data:font/woff2;base64," in html and "fonts.googleapis.com" not in html)
            check("new-deck A: 'active' garantido no 1º slide",
                  re.search(r'<section class="slide active"', html) is not None)
            check("new-deck A: tokens obrigatórios",
                  all(t in html for t in (".deck-stage", "ApresentacaoCefor",
                                          "prefers-reduced-motion", "editToggle")))
            check("new-deck A: salvar() serializa cópia limpa", "cloneNode(true)" in html)
            check("new-deck A: teclas Home/End/Esc/F presentes",
                  all(t in html for t in ("'Home'", "'End'", "'Escape'", "requestFullscreen")))
        else:
            check("new-deck B: fundo degradê (--slide-bg: var(--grad))",
                  "--slide-bg: var(--grad)" in html)


def test_generate_odp(tmp):
    try:
        import odf  # noqa: F401
    except ImportError:
        print("[AVISO] odfpy não instalado — testes do generate-odp PULADOS (pip install odfpy)")
        return
    for exemplo in EXEMPLOS:
        nome = os.path.basename(exemplo)
        if not os.path.isfile(exemplo):
            check(f"generate-odp: exemplo existe ({nome})", False, "arquivo não encontrado")
            continue
        out = os.path.join(tmp, nome.replace(".html", ".odp"))
        rc, log = run([sys.executable, GEN_ODP, exemplo, out])
        check(f"generate-odp {nome}: ODF válido na releitura", rc == 0 and "[OK] ODF valido" in log,
              log.strip()[:200])
        if rc != 0:
            continue
        check(f"generate-odp {nome}: nenhum slide vazio (sem [AVISO])",
              "[AVISO] Slide" not in log, log.strip()[:200])
        xml = zipfile.ZipFile(out).read("content.xml").decode("utf-8")
        check(f"generate-odp {nome}: tabela ODF REAL presente",
              "<table:table" in xml and xml.count("<table:table-cell") >= 8)
        check(f"generate-odp {nome}: KPIs extraídos (número — rótulo)",
              "CeforKpiNum" in xml)


def test_generate_pptx(tmp):
    try:
        import pptx  # noqa: F401
    except ImportError:
        print("[AVISO] python-pptx não instalado — testes do generate-pptx PULADOS (pip install python-pptx)")
        return
    gen = os.path.join(HERE, "generate-pptx.py")
    for exemplo in EXEMPLOS:
        nome = os.path.basename(exemplo)
        if not os.path.isfile(exemplo):
            continue  # já reportado no teste do ODP
        out = os.path.join(tmp, nome.replace(".html", ".pptx"))
        rc, log = run([sys.executable, gen, exemplo, out])
        check(f"generate-pptx {nome}: PPTX válido na releitura",
              rc == 0 and "[OK] PPTX valido" in log, log.strip()[:200])
        if rc != 0:
            continue
        check(f"generate-pptx {nome}: nenhum slide vazio (sem [AVISO])",
              "[AVISO] Slide" not in log, log.strip()[:200])
        z = zipfile.ZipFile(out)
        xml = "".join(z.read(n).decode("utf-8", "replace")
                      for n in z.namelist() if n.startswith("ppt/slides/slide"))
        check(f"generate-pptx {nome}: tabela PowerPoint REAL presente",
              "<a:tbl>" in xml and xml.count("<a:tc>") >= 8)


def test_make_zip(tmp):
    out = os.path.join(tmp, "pacote.zip")
    rc, log = run([sys.executable, os.path.join(HERE, "make-zip.py"), out])
    ok = rc == 0 and os.path.isfile(out)
    if ok:
        nomes = zipfile.ZipFile(out).namelist()
        ok = ("cefor-slides/SKILL.md" in nomes and
              any(n.endswith("deck-fonts.css") for n in nomes) and len(nomes) >= 15)
    check("make-zip: pacote gerado com SKILL.md e fontes", ok, log.strip()[:200])


def main():
    print(f"== Smoke test cefor-slides ==\n   skill: {SKILL}\n")
    with tempfile.TemporaryDirectory() as tmp:
        test_new_deck(tmp)
        test_generate_odp(tmp)
        test_generate_pptx(tmp)
        test_make_zip(tmp)
    falhas = [n for n, ok in resultados if not ok]
    total = len(resultados)
    print(f"\n== {total - len(falhas)}/{total} verdes ==")
    if falhas:
        print("Falhas: " + "; ".join(falhas))
        sys.exit(1)


if __name__ == "__main__":
    main()
