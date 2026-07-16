#!/usr/bin/env python3
"""
generate-odp.py - Converter apresentacoes HTML Cefor para LibreOffice Impress (.odp)

Uso:
    python generate-odp.py <entrada.html> [saida.odp]

Dependencias:
    pip install odfpy          # obrigatoria (gera ODF valido)
    pip install pillow         # opcional (so para embutir imagens raster locais)

O script:
1. Le o HTML (estrutura de slides, conteudo, cores de :root).
2. Extrai blocos semanticos por classe (titulo, antetitulo, corpo, bullets,
   KPIs .kpi-num/.kpi-label e tabelas <table> — estruturados).
3. Monta um .odp VALIDO via odfpy (master page, estilos, escaping automatico).
   Tabelas HTML viram TABELAS ODF reais (editaveis no Impress, cabecalho lima);
   KPIs viram linhas "numero — rotulo".
4. Aplica a paleta Cefor (lima/azul/oliva) e a fonte Open Sans.
5. Valida o arquivo reabrindo-o antes de declarar sucesso; avisa se um slide
   nao contribuir nenhum conteudo (nada e perdido em silencio).

Limitacoes conscientes (o HTML continua sendo a fonte da verdade):
- Vetores decorativos (SVG, grafismos, degrades, molduras) NAO sao transpostos:
  pertencem ao layout pixel-perfect do HTML, nao ao conteudo editavel.
- Imagens <img> raster locais (png/jpg) sao embutidas; SVG e remotas sao puladas
  com aviso.
"""

import sys
import os
import re
from html.parser import HTMLParser

# --- Saida ASCII-safe (evita UnicodeEncodeError em console cp1252 do Windows) ---
def _log(msg):
    try:
        sys.stdout.write(msg + "\n")
    except UnicodeEncodeError:
        sys.stdout.write(msg.encode("ascii", "replace").decode("ascii") + "\n")

try:
    from odf.opendocument import OpenDocumentPresentation, load as odf_load
    from odf.style import (
        Style, MasterPage, PageLayout, PageLayoutProperties,
        TextProperties, ParagraphProperties, GraphicProperties,
        DrawingPageProperties, FontFace,
        TableColumnProperties, TableCellProperties,
    )
    from odf.text import P, Span
    from odf.draw import Page, Frame, TextBox, Image
    from odf.table import Table, TableColumn, TableRow, TableCell
except ImportError:
    _log("[ERRO] odfpy nao instalado. Rode: pip install odfpy")
    sys.exit(1)

try:
    from PIL import Image as PILImage
    _HAS_PIL = True
except ImportError:
    _HAS_PIL = False


# ---------------------------------------------------------------------------
# Parser HTML -> blocos semanticos por slide
# ---------------------------------------------------------------------------

SKIP_CLASSES = {"rodape", "slide-counter", "bullet"}
SKIP_TAGS = {"script", "style", "svg", "defs", "pattern"}
TITLE_CLASSES = {"t-capa", "t-secao", "t-conteudo"}
KICKER_CLASSES = {"eyebrow", "num-secao"}
BODY_CLASSES = {"corpo"}
VOID_TAGS = {"br", "img", "hr", "input", "meta", "link", "source", "col", "area", "base", "wbr"}


def _normalize(text):
    return " ".join(text.split()).strip()


# Caracteres puramente decorativos (aspas tipograficas, marcas, pontuacao isolada)
_DECORATION_RE = re.compile(r'^[\s"“”‘’\'`´\-—–·.,:;!?()]+$')


def _is_decoration(text):
    """Descarta blocos sem conteudo real (ex.: aspa de abertura solta '"')."""
    return len(text) < 2 or bool(_DECORATION_RE.match(text))


KPI_CLASSES = {"kpi-num", "kpi-label"}


class HTMLSlideParser(HTMLParser):
    """Extrai, por slide, uma lista ordenada de blocos (role, conteudo).

    Roles: 'title' | 'kicker' | 'body' | 'bullet' | 'kpi-num' | 'kpi-label'
    (conteudo = texto) e 'table' (conteudo = {'rows': [[celulas]], 'has_header'}).
    Imagens raster locais sao guardadas em slide['images'] (lista de src).
    Tabelas e KPIs sao capturados MESMO dentro de um wrapper '.reveal' (sub-captura),
    virando estruturas editaveis no .odp em vez de texto corrido.
    """

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
            # encerramento, KPIs). Fallback de menor prioridade.
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
    try:
        with open(html_path, "r", encoding="utf-8") as f:
            html = f.read()
    except FileNotFoundError:
        _log(f"[ERRO] Arquivo nao encontrado: {html_path}")
        sys.exit(1)
    parser = HTMLSlideParser()
    parser.feed(html)
    parser._end_slide()
    return parser.slides, parser.css_root


# ---------------------------------------------------------------------------
# Geracao do .odp (odfpy)
# ---------------------------------------------------------------------------

def _hex(css_root, key, default):
    val = (css_root.get(key) or default).strip()
    if not val.startswith("#"):
        val = default
    return val[:7]


def build_odp(slides, css_root, output_path):
    lime = _hex(css_root, "lime", "#B0CB1F")
    navy = _hex(css_root, "navy", "#2C459A")
    olive = _hex(css_root, "olive", "#8C9A0D")
    ink = _hex(css_root, "ink", "#2B2B2B")

    doc = OpenDocumentPresentation()

    # Fonte institucional
    doc.fontfacedecls.addElement(
        FontFace(name="Open Sans", fontfamily="Open Sans", fontfamilygeneric="swiss")
    )

    # Page layout 16:9 widescreen (33.867cm x 19.05cm == 13.333in x 7.5in)
    pagelayout = PageLayout(name="CeforLayout")
    pagelayout.addElement(PageLayoutProperties(
        margin="0cm", pagewidth="33.867cm", pageheight="19.05cm", printorientation="landscape"
    ))
    doc.automaticstyles.addElement(pagelayout)

    # Estilo da pagina de desenho (fundo branco)
    dpstyle = Style(name="dp-cefor", family="drawing-page")
    dpstyle.addElement(DrawingPageProperties(fill="solid", fillcolor="#FFFFFF"))
    doc.automaticstyles.addElement(dpstyle)

    masterpage = MasterPage(name="Cefor", pagelayoutname=pagelayout)
    doc.masterstyles.addElement(masterpage)

    # --- Estilos de paragrafo/texto ---
    def add_text_style(name, **text_props):
        st = Style(name=name, family="paragraph")
        st.addElement(ParagraphProperties(margintop="0cm", marginbottom="0.15cm"))
        st.addElement(TextProperties(fontfamily="Open Sans", fontname="Open Sans", **text_props))
        doc.styles.addElement(st)
        return st

    add_text_style("CeforKicker", fontsize="14pt", fontweight="bold", color=olive,
                   letterspacing="0.05cm")
    add_text_style("CeforTitle", fontsize="34pt", fontweight="bold", color=navy)
    add_text_style("CeforBody", fontsize="18pt", color=ink)
    add_text_style("CeforBullet", fontsize="18pt", color=ink)
    add_text_style("CeforFooter", fontsize="11pt", color=olive)
    add_text_style("CeforTh", fontsize="14pt", fontweight="bold", color=ink)
    add_text_style("CeforTd", fontsize="13pt", color=ink)
    # Span lima para o marcador de bullet
    bulletspan = Style(name="CeforBulletMark", family="text")
    bulletspan.addElement(TextProperties(fontfamily="Open Sans", fontname="Open Sans",
                                         color=lime, fontweight="bold"))
    doc.styles.addElement(bulletspan)
    # Span para o numero do KPI (azul, bold)
    kpispan = Style(name="CeforKpiNum", family="text")
    kpispan.addElement(TextProperties(fontfamily="Open Sans", fontname="Open Sans",
                                      color=navy, fontweight="bold", fontsize="22pt"))
    doc.styles.addElement(kpispan)

    # Estilos de celula de tabela (cabecalho lima / corpo branco)
    cell_hdr = Style(name="CeforCellHdr", family="table-cell")
    cell_hdr.addElement(TableCellProperties(backgroundcolor=lime, padding="0.15cm",
                                            border="0.035cm solid #D7D7DA"))
    doc.automaticstyles.addElement(cell_hdr)
    cell_std = Style(name="CeforCellStd", family="table-cell")
    cell_std.addElement(TableCellProperties(backgroundcolor="#FFFFFF", padding="0.15cm",
                                            border="0.035cm solid #D7D7DA"))
    doc.automaticstyles.addElement(cell_std)

    # Estilos grafados dos frames (graphic-properties: sem borda/preenchimento)
    framestyle = Style(name="CeforFrame", family="graphic")
    framestyle.addElement(GraphicProperties(stroke="none", fill="none"))
    doc.automaticstyles.addElement(framestyle)

    def make_frame(page, x, y, w, h):
        frame = Frame(stylename=framestyle, width=w, height=h, x=x, y=y)
        tb = TextBox()
        frame.addElement(tb)
        page.addElement(frame)
        return tb

    # Tabela ODF REAL (editavel no Impress), com cabecalho lima
    tbl_seq = [0]

    def add_table(page, tblock, y_cm):
        tbl_seq[0] += 1
        rows = tblock["rows"]
        ncols = max(len(r) for r in rows)
        width = 29.4
        colname = f"CeforCol{tbl_seq[0]}"
        colstyle = Style(name=colname, family="table-column")
        colstyle.addElement(TableColumnProperties(columnwidth=f"{width / ncols:.2f}cm"))
        doc.automaticstyles.addElement(colstyle)
        h = min(1.05 * len(rows) + 0.3, 10.5)
        frame = Frame(stylename=framestyle, width=f"{width}cm",
                      height=f"{h:.2f}cm", x="2.2cm", y=f"{y_cm:.2f}cm")
        table = Table()
        for _ in range(ncols):
            table.addElement(TableColumn(stylename=colname))
        for ri, row in enumerate(rows):
            tr = TableRow()
            table.addElement(tr)
            is_hdr = tblock["has_header"] and ri == 0
            for ci in range(ncols):
                cell = TableCell(stylename=(cell_hdr if is_hdr else cell_std))
                cell.addElement(P(stylename=("CeforTh" if is_hdr else "CeforTd"),
                                  text=row[ci] if ci < len(row) else ""))
                tr.addElement(cell)
        frame.addElement(table)
        page.addElement(frame)

    pic_dir = os.path.dirname(os.path.abspath(slides_src_path)) if slides else ""

    for idx, slide in enumerate(slides, 1):
        page = Page(name=f"slide{idx}", masterpagename=masterpage, stylename=dpstyle)
        doc.presentation.addElement(page)

        blocks = slide["blocks"]
        title_block = next((b for b in blocks if b[0] == "title"), None)
        kicker_block = next((b for b in blocks if b[0] == "kicker"), None)

        # Cabecalho: antetitulo + titulo
        head_tb = make_frame(page, "2.2cm", "1.3cm", "29.4cm", "4.5cm")
        if kicker_block:
            head_tb.addElement(P(stylename="CeforKicker", text=kicker_block[1].upper()))
        if title_block:
            head_tb.addElement(P(stylename="CeforTitle", text=title_block[1]))

        # Corpo: bullets, paragrafos e KPIs (fluxo) + tabelas (frames proprios)
        body_tb = make_frame(page, "2.2cm", "6.4cm", "29.4cm", "10.8cm")
        used = {id(title_block), id(kicker_block)}
        had_body = False
        had_flow = False
        tables = []
        kpi_num = None  # numero de KPI aguardando o rotulo seguinte
        for b in blocks:
            if id(b) in used:
                continue
            role, content = b
            if role == "table":
                tables.append(content)
                had_body = True
                continue
            if role == "kpi-num":
                kpi_num = content
                continue
            if role == "kpi-label":
                p = P(stylename="CeforBody")
                if kpi_num:
                    p.addElement(Span(stylename="CeforKpiNum", text=kpi_num))
                    p.addText("  —  ")
                    kpi_num = None
                p.addText(content)
                body_tb.addElement(p)
                had_body = had_flow = True
                continue
            if role == "bullet":
                p = P(stylename="CeforBullet")
                p.addElement(Span(stylename="CeforBulletMark", text="▸  "))
                p.addText(content)
                body_tb.addElement(p)
                had_body = had_flow = True
            elif role in ("body", "title", "kicker"):
                body_tb.addElement(P(stylename="CeforBody", text=content))
                had_body = had_flow = True
        if kpi_num:  # numero sem rotulo (raro): nao perder
            body_tb.addElement(P(stylename="CeforBody", text=kpi_num))
            had_body = had_flow = True

        # Tabelas reais abaixo do fluxo de texto (ou no topo do corpo, se so ha tabela)
        if tables:
            y = 8.6 if had_flow else 6.4
            if len(tables) > 1:
                _log(f"[AVISO] Slide {idx}: {len(tables)} tabelas — posicione-as manualmente no Impress")
            for t_i, tblock in enumerate(tables):
                add_table(page, tblock, y + t_i * 0.8)

        # Imagens raster locais
        for src in slide.get("images", []):
            path = os.path.join(pic_dir, src)
            if not os.path.isfile(path):
                _log(f"[AVISO] Slide {idx}: imagem nao encontrada, pulada: {src}")
                continue
            try:
                w_cm, h_cm = _image_size_cm(path)
                href = doc.addPicture(path)
                imgframe = Frame(stylename=framestyle, width=f"{w_cm:.2f}cm",
                                 height=f"{h_cm:.2f}cm", x="2.2cm", y="6.4cm")
                imgframe.addElement(Image(href=href))
                page.addElement(imgframe)
                had_body = True
            except Exception as e:  # noqa: BLE001
                _log(f"[AVISO] Slide {idx}: falha ao embutir {src}: {e}")

        # Rodape institucional
        foot_tb = make_frame(page, "2.2cm", "17.8cm", "29.4cm", "0.8cm")
        foot_tb.addElement(P(stylename="CeforFooter", text="cefor.ifes.edu.br"))

        if not title_block and not kicker_block and not had_body:
            _log(f"[AVISO] Slide {idx}: nenhum conteudo extraido (sem classes semanticas "
                 f"nem '.reveal') — placeholder inserido; revise o slide no Impress")
            body_tb.addElement(P(stylename="CeforBody", text=f"(Slide {idx})"))

    doc.save(output_path)
    return output_path


def _image_size_cm(path, max_w_cm=18.0, max_h_cm=10.0):
    """Dimensao em cm preservando proporcao; cai para um padrao se faltar PIL."""
    if not _HAS_PIL:
        return (12.0, 7.0)
    with PILImage.open(path) as im:
        w_px, h_px = im.size
    ratio = (h_px / w_px) if w_px else 0.6
    w = max_w_cm
    h = w * ratio
    if h > max_h_cm:
        h = max_h_cm
        w = h / ratio if ratio else max_w_cm
    return (w, h)


def validate_odp(path):
    """Reabre o .odp para garantir que e um ODF valido (nao apenas um ZIP)."""
    try:
        doc = odf_load(path)
        pages = doc.getElementsByType(Page)
        return True, len(pages)
    except Exception as e:  # noqa: BLE001
        return False, str(e)


# ---------------------------------------------------------------------------

def main():
    global slides_src_path, slides
    if len(sys.argv) < 2:
        _log(__doc__)
        sys.exit(1)

    slides_src_path = sys.argv[1]
    output = sys.argv[2] if len(sys.argv) > 2 else re.sub(r"\.html?$", "", slides_src_path) + ".odp"

    _log(f"[INFO] Lendo: {slides_src_path}")
    slides, css_root = parse_html(slides_src_path)
    if not slides:
        _log("[ERRO] Nenhum slide (<section class=\"slide\">) encontrado no HTML.")
        sys.exit(1)

    _log(f"[INFO] Slides encontrados: {len(slides)}")
    _log(f"[INFO] Cores Cefor: lima={css_root.get('lime')} azul={css_root.get('navy')} oliva={css_root.get('olive')}")

    _log("[INFO] Gerando .odp via odfpy...")
    try:
        build_odp(slides, css_root, output)
    except Exception as e:  # noqa: BLE001
        _log(f"[ERRO] Falha ao gerar .odp: {e}")
        sys.exit(1)

    ok, info = validate_odp(output)
    if ok:
        _log(f"[OK] ODF valido: {output} ({info} slide(s) confirmados na releitura)")
        _log("[OK] Abra em LibreOffice Impress e revise o conteudo editavel.")
    else:
        _log(f"[ERRO] Arquivo gerado NAO e um ODF valido: {info}")
        sys.exit(1)


if __name__ == "__main__":
    slides = []
    slides_src_path = ""
    main()
