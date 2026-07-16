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
2. Extrai blocos semanticos por classe via deck_parser.py (titulo, antetitulo,
   corpo, bullets, KPIs .kpi-num/.kpi-label e tabelas <table> — estruturados).
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

# Parser compartilhado (mesmo dos demais exports) — ver deck_parser.py
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from deck_parser import parse_html, log as _log, css_hex as _hex  # noqa: E402

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
# Geracao do .odp (odfpy)
# ---------------------------------------------------------------------------

def build_odp(slides, css_root, output_path, src_dir):
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

    pic_dir = src_dir

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
        build_odp(slides, css_root, output,
                  src_dir=os.path.dirname(os.path.abspath(slides_src_path)))
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
    main()
