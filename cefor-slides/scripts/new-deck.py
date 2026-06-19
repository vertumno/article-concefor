#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
new-deck.py — Monta um deck Cefor completo (HTML único, autossuficiente) a
partir APENAS dos corpos de slide gerados pelo agente.

Por que existe: ~56% de todo deck é boilerplate idêntico (head + CSS de palco/
tipografia/componentes + controlador JS + edição inline + SVGs de marca). Em vez
de o agente reler e reescrever esse bloco a cada deck (gasto de tokens e risco de
drift), este script o injeta de forma DETERMINÍSTICA e byte-correta. O agente só
escreve os <section class="slide">…</section>.

Uso:
    python scripts/new-deck.py \
        --version A \
        --title "Planejamento Estratégico 2026 — Cefor/Ifes" \
        --slides corpos.html \
        --out deck.html \
        [--lime "#B0CB1F"] [--navy "#2C459A"]

  --slides : arquivo com SÓ os <section class="slide">…</section> (sem head/script).
             Use "-" para ler do stdin.
  --version: A (Cor Sólida, padrão) ou B (Degradê).
  --lime/--navy: sobrescrevem as cores oficiais dentro dos eixos da marca (opcional).

Sem dependências externas (stdlib apenas). Valida o resultado antes de gravar.
"""
import argparse
import os
import sys
from html.parser import HTMLParser

HERE = os.path.dirname(os.path.abspath(__file__))
BASE_CSS = os.path.join(HERE, "deck-base.css")

# Tokens de :root oficiais (de CEFOR_BRAND.md). --slide-bg muda por versão.
ROOT_TOKENS = """        :root {{
            --lime: {lime}; --lime-dk: #9DB400; --olive: #8C9A0D;
            --navy: {navy}; --navy2: #2E3F8F;
            --gray: #EAEAEC; --gray-dk: #D7D7DA;
            --ink: #2B2B2B; --muted: #5A5A5A;
            --green: #2E9B30; --red: #CC1111;
            --grad: radial-gradient(120% 95% at 88% 6%,#C6D452 0%,rgba(198,212,82,0) 46%),
                    radial-gradient(95% 95% at 58% 28%,#7FC24A 0%,rgba(127,194,74,0) 56%),
                    radial-gradient(130% 130% at 16% 98%,#3F9FD6 0%,rgba(63,159,214,0) 58%),
                    linear-gradient(135deg,#57B86A 0%,#36B4A6 46%,#3F93CE 100%);
            --font: 'Open Sans', system-ui, sans-serif;
            --ease-out: cubic-bezier(0.16, 1, 0.3, 1);
            --duration: 0.5s;
            --stage-bg: #11151c;   /* moldura fora do slide (letterbox) */
            --slide-bg: {slide_bg};
        }}"""

# SVGs de marca reutilizáveis (seta CEFOR + marca d'água). Use com:
#   <svg class="seta" style="..."><use href="#seta-cefor"/></svg>  (defina fill no <svg>)
#   <rect width="100%" height="100%" fill="url(#wm-setas)"/>        (marca d'água)
BRAND_DEFS = """    <svg width="0" height="0" style="position:absolute" aria-hidden="true">
      <defs>
        <path id="seta-cefor" d="M41.8 26.2 L73.8 58.2 L81.6 50.4 L82 82 L50.4 81.6 L58.2 73.8 L26.2 41.8 Z"/>
        <pattern id="wm-setas" width="56" height="56" patternUnits="userSpaceOnUse">
          <path d="M41.8 26.2 L73.8 58.2 L81.6 50.4 L82 82 L50.4 81.6 L58.2 73.8 L26.2 41.8 Z"
                transform="scale(0.42)" fill="rgba(0,0,0,0.06)"/>
        </pattern>
      </defs>
    </svg>"""

CONTROLLER_JS = """    <script>
        /* === CONTROLADOR DA APRESENTAÇÃO === */
        class ApresentacaoCefor {
            constructor() {
                this.slides = document.querySelectorAll('.slide');
                this.atual = 0;
                this.stage = document.getElementById('deckStage');
                this.criarContador();
                this.escalarPalco(); this.navTeclado(); this.navToque(); this.mostrar(0);
            }
            criarContador() {
                const prog = document.createElement('div');
                prog.className = 'deck-progress';
                prog.style.cssText = 'position:fixed;top:0;left:0;height:6px;background:var(--lime);z-index:9999;transition:width 0.3s ease;width:0;';
                document.body.appendChild(prog);
                this.progressBar = prog;
                this.counters = document.querySelectorAll('.slide-counter');
            }
            escalarPalco() {
                const escalar = () => {
                    const f = Math.min(window.innerWidth/1920, window.innerHeight/1080);
                    const x = (window.innerWidth - 1920*f)/2, y = (window.innerHeight - 1080*f)/2;
                    this.stage.style.transform = `translate(${x}px, ${y}px) scale(${f})`;
                };
                escalar(); window.addEventListener('resize', escalar);
            }
            navTeclado() {
                document.addEventListener('keydown', (e) => {
                    if (e.target.getAttribute('contenteditable')) return;
                    if (['ArrowRight',' ','PageDown'].includes(e.key)) this.mostrar(this.atual+1);
                    if (['ArrowLeft','PageUp'].includes(e.key)) this.mostrar(this.atual-1);
                });
            }
            navToque() {
                let x0 = null;
                document.addEventListener('touchstart', e => x0 = e.touches[0].clientX);
                document.addEventListener('touchend', e => {
                    if (x0===null) return;
                    const dx = e.changedTouches[0].clientX - x0;
                    if (dx < -50) this.mostrar(this.atual+1);
                    if (dx > 50) this.mostrar(this.atual-1);
                    x0 = null;
                });
            }
            mostrar(i) {
                this.atual = Math.max(0, Math.min(i, this.slides.length-1));
                this.slides.forEach((s, idx) => {
                    s.classList.toggle('active', idx===this.atual);
                    s.classList.toggle('visible', idx===this.atual);
                });
                const pct = ((this.atual + 1) / this.slides.length) * 100;
                if (this.progressBar) this.progressBar.style.width = `${pct}%`;
                if (this.counters) {
                    this.counters.forEach(c => { c.textContent = `${this.atual + 1} / ${this.slides.length}`; });
                }
            }
        }
        const app = new ApresentacaoCefor();

        /* === EDIÇÃO INLINE === */
        const editor = {
            isActive: false,
            toggle() {
                this.isActive = !this.isActive;
                document.querySelectorAll('h1,h2,h3,p,li,span,td,th,div.num-secao').forEach(el => {
                    if (!el.classList.contains('edit-toggle') && !el.classList.contains('slide-counter')) {
                        el.setAttribute('contenteditable', this.isActive);
                    }
                });
                document.getElementById('editToggle').classList.toggle('active', this.isActive);
            },
            salvar() {
                const html = '<!DOCTYPE html>\\n' + document.documentElement.outerHTML;
                const a = document.createElement('a');
                a.href = URL.createObjectURL(new Blob([html], {type:'text/html'}));
                a.download = 'apresentacao-cefor.html'; a.click();
            }
        };
        const hotzone = document.querySelector('.edit-hotzone');
        const editToggle = document.getElementById('editToggle');
        let hideTimeout = null;
        hotzone.addEventListener('mouseenter', () => { clearTimeout(hideTimeout); editToggle.classList.add('show'); });
        hotzone.addEventListener('mouseleave', () => { hideTimeout = setTimeout(() => { if(!editor.isActive) editToggle.classList.remove('show'); }, 400); });
        editToggle.addEventListener('mouseenter', () => clearTimeout(hideTimeout));
        editToggle.addEventListener('mouseleave', () => { hideTimeout = setTimeout(() => { if(!editor.isActive) editToggle.classList.remove('show'); }, 400); });
        editToggle.addEventListener('click', () => editor.toggle());
        hotzone.addEventListener('click', () => editor.toggle());
        document.addEventListener('keydown', (e) => {
            if ((e.key==='e'||e.key==='E') && !e.target.getAttribute('contenteditable')) editor.toggle();
            if ((e.ctrlKey||e.metaKey) && e.key==='s') { e.preventDefault(); editor.salvar(); }
        });
    </script>"""


def montar(version, title, slides_html, lime, navy):
    with open(BASE_CSS, encoding="utf-8") as f:
        base_css = f.read()
    slide_bg = "var(--grad)" if version.upper() == "B" else "#FFFFFF"
    root = ROOT_TOKENS.format(lime=lime, navy=navy, slide_bg=slide_bg)
    css = "        /* === TOKENS DE MARCA === */\n" + root + "\n\n" + \
          "\n".join("        " + ln if ln else ln for ln in base_css.splitlines())
    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>

    <!-- Fonte institucional do Cefor: Open Sans -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;600;700;800&display=swap">

    <style>
{css}
    </style>
</head>
<body>
{BRAND_DEFS}
    <div class="deck-viewport">
        <main class="deck-stage" id="deckStage">
{slides_html}
        </main>
    </div>

    <!-- Edição inline (incluída por padrão) -->
    <div class="edit-hotzone"></div>
    <button class="edit-toggle" id="editToggle" title="Modo edição (E)">&#9998;</button>

{CONTROLLER_JS}
</body>
</html>
"""


class _Validador(HTMLParser):
    def __init__(self):
        super().__init__()
        self.slides = 0
    def handle_starttag(self, tag, attrs):
        if tag == "section" and any(k == "class" and "slide" in (v or "") for k, v in attrs):
            self.slides += 1


def validar(html):
    erros = []
    obrig = [".deck-stage", "ApresentacaoCefor", "prefers-reduced-motion",
             "deck-viewport", "editToggle", "Open+Sans"]
    for token in obrig:
        if token not in html:
            erros.append(f"faltando: {token}")
    v = _Validador()
    v.feed(html)
    if v.slides == 0:
        erros.append("nenhum <section class=\"slide\"> encontrado")
    return v.slides, erros


def main():
    p = argparse.ArgumentParser(description="Monta um deck Cefor a partir dos corpos de slide.")
    p.add_argument("--version", default="A", choices=["A", "B", "a", "b"])
    p.add_argument("--title", required=True)
    p.add_argument("--slides", required=True, help='arquivo com os <section class="slide">; "-" = stdin')
    p.add_argument("--out", required=True)
    p.add_argument("--lime", default="#B0CB1F")
    p.add_argument("--navy", default="#2C459A")
    a = p.parse_args()

    if a.slides == "-":
        slides_html = sys.stdin.read()
    else:
        with open(a.slides, encoding="utf-8") as f:
            slides_html = f.read()

    html = montar(a.version, a.title, slides_html.strip("\n"), a.lime, a.navy)
    n, erros = validar(html)
    if erros:
        print("[ERRO] deck inválido:\n  - " + "\n  - ".join(erros), file=sys.stderr)
        sys.exit(1)

    with open(a.out, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"[OK] deck válido — {n} slide(s), Versão {a.version.upper()} -> {a.out}")


if __name__ == "__main__":
    main()
