#!/usr/bin/env python3
"""
deck_parser.py - Parser compartilhado: HTML Cefor -> blocos semanticos por slide.

Usado por generate-odp.py (LibreOffice Impress) e generate-pptx.py (PowerPoint).
Stdlib apenas — sem dependencias externas.

Roles produzidos: 'title' | 'kicker' | 'body' | 'bullet' | 'kpi-num' | 'kpi-label'
(conteudo = texto) e 'table' (conteudo = {'rows': [[celulas]], 'has_header'}).
Imagens raster locais ficam em slide['images'] (lista de src). Tabelas e KPIs sao
capturados MESMO dentro de um wrapper '.reveal' (sub-captura), virando estruturas
editaveis no destino em vez de texto corrido.
"""

import re
import sys
from html.parser import HTMLParser

SKIP_CLASSES = {"rodape", "slide-counter", "bullet"}
SKIP_TAGS = {"script", "style", "svg", "defs", "pattern"}
TITLE_CLASSES = {"t-capa", "t-secao", "t-conteudo"}
KICKER_CLASSES = {"eyebrow", "num-secao"}
BODY_CLASSES = {"corpo"}
KPI_CLASSES = {"kpi-num", "kpi-label"}
VOID_TAGS = {"br", "img", "hr", "input", "meta", "link", "source", "col", "area", "base", "wbr"}


def log(msg):
    """Saida ASCII-safe (evita UnicodeEncodeError em console cp1252 do Windows)."""
    try:
        sys.stdout.write(msg + "\n")
    except UnicodeEncodeError:
        sys.stdout.write(msg.encode("ascii", "replace").decode("ascii") + "\n")


def css_hex(css_root, key, default):
    """Cor #RRGGBB de uma variavel do :root, com fallback seguro."""
    val = (css_root.get(key) or default).strip()
    if not val.startswith("#"):
        val = default
    return val[:7]


def _normalize(text):
    return " ".join(text.split()).strip()


# Caracteres puramente decorativos (aspas tipograficas, marcas, pontuacao isolada)
_DECORATION_RE = re.compile(r'^[\s"“”‘’\'`´\-—–·.,:;!?()]+$')


def _is_decoration(text):
    """Descarta blocos sem conteudo real (ex.: aspa de abertura solta '"')."""
    return len(text) < 2 or bool(_DECORATION_RE.match(text))


class HTMLSlideParser(HTMLParser):
    """Extrai, por slide, uma lista ordenada de blocos (role, conteudo)."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.slides = []
        self.css_root = {}
        self.cur = None          # slide atual
        self.stack = []          # pilha de (tag, mode)
        self.skip = 0            # profundidade de elementos a ignorar
        self.capture = None      # {'role', 'buf'} do bloco em captura
        self.table = None        # {'rows': [...], 'has_header': bool} em captura
        self.cell = None         # buffer da celula atual (td/th)
        self.sub = None          # sub-captura KPI dentro de um capture ativo
        self.in_style = False
        self._style_buf = ""

    # -- CSS :root --
    def _parse_root(self, css_text):
        # Restringe ao primeiro bloco :root { ... } (evita capturar vars de outros escopos)
        m = re.search(r":root\s*\{([^}]*)\}", css_text, re.DOTALL)
        scope = m.group(1) if m else css_text
        for name, value in re.findall(r"--([\w-]+)\s*:\s*([^;]+);", scope):
            self.css_root[name.strip()] = value.strip()

    def handle_starttag(self, tag, attrs):
        ad = dict(attrs)
        classes = set((ad.get("class") or "").split())

        if tag == "style":
            self.in_style = True
            self._style_buf = ""
            return

        # Fronteira de slide
        if tag == "section" and "slide" in classes:
            self._end_slide()  # seguranca
            self.cur = {"blocks": [], "images": []}
            self.stack = [("section", "plain")]
            self.skip = 0
            self.capture = None
            self.table = None
            self.cell = None
            self.sub = None
            return

        if self.cur is None:
            return

        # Dentro de uma tabela: so estrutura tr/td/th interessa
        if self.table is not None:
            if tag == "tr":
                self.table["rows"].append([])
            elif tag in ("td", "th"):
                self.cell = ""
                if tag == "th":
                    self.table["has_header"] = True
            elif tag == "br" and self.cell is not None:
                self.cell += " "
            if tag not in VOID_TAGS:
                self.stack.append((tag, "table-int"))
            return

        # Imagem raster (conteudo)
        if tag == "img":
            src = ad.get("src", "")
            if src and not src.lower().endswith(".svg") and not src.startswith(("http://", "https://", "data:")):
                self.cur["images"].append(src)
            if self.capture is not None and self.skip == 0:
                self.capture["buf"] += " "
            return

        # Tabela: captura estruturada (mesmo dentro de um wrapper .reveal)
        if tag == "table" and self.skip == 0 and not (classes & SKIP_CLASSES):
            self.table = {"rows": [], "has_header": False}
            self.stack.append((tag, "table"))
            return

        # KPI: sub-captura (mesmo dentro de um wrapper .reveal)
        if self.skip == 0 and (classes & KPI_CLASSES) and self.sub is None:
            role = "kpi-num" if "kpi-num" in classes else "kpi-label"
            self.sub = {"role": role, "buf": ""}
            self.stack.append((tag, "sub"))
            return

        # Decide modo do elemento
        role = None
        if classes & SKIP_CLASSES or tag in SKIP_TAGS:
            mode = "skip"
        elif self.capture is not None:
            mode = "inside"  # ja capturando: texto contribui, sem novo bloco
        elif classes & TITLE_CLASSES or tag in ("h1", "h2", "h3"):
            mode, role = "capture", "title"
        elif classes & KICKER_CLASSES:
            mode, role = "capture", "kicker"
        elif tag == "li":
            mode, role = "capture", "bullet"
        elif (classes & BODY_CLASSES) or tag == "p":
            mode, role = "capture", "body"
        elif "reveal" in classes:
            # 'reveal' e o marcador de conteudo animado do template da skill:
            # carrega o texto real de slides sem classe semantica (mensagem-chave,
            # encerramento). Fallback de menor prioridade.
            mode, role = "capture", "body"
        else:
            mode = "plain"

        if mode == "skip":
            self.skip += 1
        elif mode == "capture":
            self.capture = {"role": role, "buf": ""}

        if tag in VOID_TAGS:
            if tag == "br" and self.capture is not None and self.skip == 0:
                self.capture["buf"] += " "
        else:
            self.stack.append((tag, mode))

    def handle_endtag(self, tag):
        if tag == "style":
            self.in_style = False
            self._parse_root(self._style_buf)
            return
        if self.cur is None or tag in VOID_TAGS or not self.stack:
            return

        popped_tag, mode = self.stack.pop()
        if mode == "table-int":
            if tag in ("td", "th") and self.cell is not None:
                if not self.table["rows"]:
                    self.table["rows"].append([])
                self.table["rows"][-1].append(_normalize(self.cell))
                self.cell = None
            return
        if mode == "table":
            rows = [r for r in self.table["rows"] if any(c for c in r)]
            if rows:
                self.cur["blocks"].append(("table", {"rows": rows,
                                                     "has_header": self.table["has_header"]}))
            self.table = None
            self.cell = None
            return
        if mode == "sub":
            text = _normalize(self.sub["buf"]) if self.sub else ""
            role = self.sub["role"] if self.sub else None
            self.sub = None
            if text and not _is_decoration(text):
                self.cur["blocks"].append((role, text))
            return
        if mode == "skip":
            self.skip = max(0, self.skip - 1)
        elif mode == "capture":
            text = _normalize(self.capture["buf"]) if self.capture else ""
            role = self.capture["role"] if self.capture else None
            self.capture = None
            if text and not _is_decoration(text):
                self.cur["blocks"].append((role, text))

        if popped_tag == "section":
            self._end_slide()

    def handle_data(self, data):
        if self.in_style:
            self._style_buf += data
            return
        if self.cur is None:
            return
        if self.cell is not None:            # texto de celula de tabela
            self.cell += data
            return
        if self.table is not None:           # dentro de tabela, fora de celula
            return
        if self.sub is not None:             # sub-captura KPI
            self.sub["buf"] += data
            return
        if self.capture is None or self.skip > 0:
            return
        self.capture["buf"] += data

    def _end_slide(self):
        if self.cur is not None:
            self.slides.append(self.cur)
            self.cur = None


def parse_html(html_path):
    """Le o HTML e retorna (slides, css_root). Sai com erro se o arquivo faltar."""
    try:
        with open(html_path, "r", encoding="utf-8") as f:
            html = f.read()
    except FileNotFoundError:
        log(f"[ERRO] Arquivo nao encontrado: {html_path}")
        sys.exit(1)
    parser = HTMLSlideParser()
    parser.feed(html)
    parser._end_slide()
    return parser.slides, parser.css_root
