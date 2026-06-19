#!/usr/bin/env python3
"""
generate-odp.py — Converter apresentações HTML Cefor para LibreOffice Impress (.odp)

Uso:
    python generate-odp.py <arquivo-entrada.html> [arquivo-saida.odp]

Dependências:
    pip install python-pptx lxml pillow

O script:
1. Lê o HTML (estrutura de slides, conteúdo, cores)
2. Extrai as cores e tipografia de :root (CSS)
3. Reconstrói os slides em .odp preservando a marca Cefor
4. Salva o arquivo editável em LibreOffice Impress
"""

import sys
import os
import re
import json
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlparse
import io
from zipfile import ZipFile
from lxml import etree as lxml_etree

# Tentar importar bibliotecas necessárias
try:
    from PIL import Image
    import requests
except ImportError:
    print("⚠️  Aviso: PIL/Pillow ou requests não instalados. Imagens podem não funcionar.")


class HTMLSlideParser(HTMLParser):
    """Parser customizado para extrair slides do HTML Cefor"""

    def __init__(self):
        super().__init__()
        self.slides = []
        self.current_slide = None
        self.current_element = None
        self.css_root = {}
        self.in_style = False
        self.style_content = ""

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)

        if tag == "style":
            self.in_style = True
            self.style_content = ""
        elif tag == "section" and "class" in attrs_dict and "slide" in attrs_dict.get("class", ""):
            self.current_slide = {
                "content": [],
                "style": attrs_dict.get("style", ""),
                "class": attrs_dict.get("class", "")
            }
            self.current_element = None
        elif self.current_slide is not None:
            if tag in ["h1", "h2", "h3", "h4", "h5", "h6", "p", "div", "li", "ul", "ol"]:
                self.current_element = {
                    "tag": tag,
                    "class": attrs_dict.get("class", ""),
                    "style": attrs_dict.get("style", ""),
                    "text": ""
                }
                if tag == "img":
                    self.current_element["src"] = attrs_dict.get("src", "")
                    self.current_element["alt"] = attrs_dict.get("alt", "")

    def handle_endtag(self, tag):
        if tag == "style":
            self.in_style = False
            self._parse_css_root(self.style_content)
        elif tag == "section" and self.current_slide is not None:
            if self.current_element:
                self.current_slide["content"].append(self.current_element)
                self.current_element = None
            self.slides.append(self.current_slide)
            self.current_slide = None
        elif tag in ["h1", "h2", "h3", "h4", "h5", "h6", "p", "div", "li"] and self.current_element:
            self.current_slide["content"].append(self.current_element)
            self.current_element = None

    def handle_data(self, data):
        if self.in_style:
            self.style_content += data
        elif self.current_element and data.strip():
            self.current_element["text"] += data.strip() + " "

    def _parse_css_root(self, css_text):
        """Extrair variáveis CSS do bloco :root {}"""
        # Padrão: --variavel: valor;
        pattern = r"--(\w+):\s*([^;]+);"
        matches = re.findall(pattern, css_text)
        for name, value in matches:
            self.css_root[name] = value.strip()


def parse_html_slides(html_path):
    """Ler HTML e extrair slides + estilos"""
    try:
        with open(html_path, 'r', encoding='utf-8') as f:
            html_content = f.read()
    except FileNotFoundError:
        print(f"❌ Erro: Arquivo não encontrado: {html_path}")
        sys.exit(1)

    parser = HTMLSlideParser()
    parser.feed(html_content)

    return parser.slides, parser.css_root


def hex_to_rgb(hex_color):
    """Converter cor hex para RGB (tupla)"""
    hex_color = hex_color.lstrip('#')
    if len(hex_color) == 6:
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    return (255, 255, 255)  # padrão branco


def create_odp_from_slides(slides, css_root, output_path):
    """
    Criar arquivo .odp a partir dos slides e estilos CSS.

    LibreOffice Impress (.odp) é um formato ZIP contendo:
    - content.xml (conteúdo dos slides)
    - styles.xml (estilos aplicáveis)
    - META-INF/manifest.xml (estrutura)
    - mimetype (tipo MIME)
    """

    print(f"📝 Criando apresentação: {len(slides)} slide(s) encontrado(s)")

    # Template mínimo de content.xml para ODP
    content_xml = create_content_xml(slides, css_root)
    styles_xml = create_styles_xml(css_root)
    manifest_xml = create_manifest_xml()

    # Criar arquivo ZIP (estrutura ODP)
    try:
        with ZipFile(output_path, 'w') as odp_zip:
            # mimetype deve ser o primeiro arquivo, sem compressão
            odp_zip.writestr('mimetype', 'application/vnd.oasis.opendocument.presentation', compress_type=0)

            # Adicionar XML files
            odp_zip.writestr('content.xml', content_xml)
            odp_zip.writestr('styles.xml', styles_xml)
            odp_zip.writestr('META-INF/manifest.xml', manifest_xml)

            # Diretórios vazios necessários
            odp_zip.writestr('Pictures/', '')

        print(f"✅ Arquivo criado: {output_path}")
        return True
    except Exception as e:
        print(f"❌ Erro ao criar ODP: {e}")
        return False


def create_content_xml(slides, css_root):
    """Gerar content.xml do ODP"""
    # XML básico do ODP
    xml_template = """<?xml version="1.0" encoding="UTF-8"?>
<office:document-content xmlns:office="urn:oasis:names:tc:opendocument:xmlns:office:1.0"
    xmlns:style="urn:oasis:names:tc:opendocument:xmlns:style:1.0"
    xmlns:text="urn:oasis:names:tc:opendocument:xmlns:text:1.0"
    xmlns:draw="urn:oasis:names:tc:opendocument:xmlns:drawing:1.0"
    xmlns:presentation="urn:oasis:names:tc:opendocument:xmlns:presentation:1.0"
    xmlns:fo="urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0"
    office:version="1.2">
    <office:automatic-styles/>
    <office:body>
        <presentation:presentation>
"""

    # Adicionar slides
    slides_xml = ""
    for i, slide in enumerate(slides, 1):
        slide_content = "<presentation:slide>"

        # Adicionar conteúdo do slide
        for element in slide.get("content", []):
            text = element.get("text", "").strip()
            tag = element.get("tag", "p")

            if text:
                # Mapear classe CSS para estilo
                css_class = element.get("class", "")
                if "t-capa" in css_class or tag == "h1":
                    slide_content += f'<text:p><text:span>{text}</text:span></text:p>'
                elif "t-secao" in css_class or tag == "h2":
                    slide_content += f'<text:p><text:span><text:a>{text}</text:a></text:span></text:p>'
                else:
                    slide_content += f'<text:p><text:span>{text}</text:span></text:p>'

        slide_content += "</presentation:slide>"
        slides_xml += slide_content

    xml_template += slides_xml
    xml_template += """        </presentation:presentation>
    </office:body>
</office:document-content>"""

    return xml_template


def create_styles_xml(css_root):
    """Gerar styles.xml com tokens Cefor"""
    lime = css_root.get('lime', '#B0CB1F')
    navy = css_root.get('navy', '#2C459A')
    olive = css_root.get('olive', '#8C9A0D')

    styles = f"""<?xml version="1.0" encoding="UTF-8"?>
<office:document-styles xmlns:office="urn:oasis:names:tc:opendocument:xmlns:office:1.0"
    xmlns:style="urn:oasis:names:tc:opendocument:xmlns:style:1.0"
    xmlns:text="urn:oasis:names:tc:opendocument:xmlns:text:1.0"
    xmlns:draw="urn:oasis:names:tc:opendocument:xmlns:drawing:1.0"
    xmlns:fo="urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0"
    office:version="1.2">
    <office:styles>
        <!-- Cores Cefor -->
        <style:color name="cefor-lime" rgb="{lime}"/>
        <style:color name="cefor-navy" rgb="{navy}"/>
        <style:color name="cefor-olive" rgb="{olive}"/>
    </office:styles>
    <office:automatic-styles/>
</office:document-styles>"""

    return styles


def create_manifest_xml():
    """Gerar META-INF/manifest.xml"""
    manifest = """<?xml version="1.0" encoding="UTF-8"?>
<manifest:manifest xmlns:manifest="urn:oasis:names:tc:opendocument:xmlns:manifest:1.0" manifest:version="1.2">
    <manifest:file-entry manifest:full-path="/" manifest:media-type="application/vnd.oasis.opendocument.presentation"/>
    <manifest:file-entry manifest:full-path="content.xml" manifest:media-type="text/xml"/>
    <manifest:file-entry manifest:full-path="styles.xml" manifest:media-type="text/xml"/>
    <manifest:file-entry manifest:full-path="META-INF/" manifest:media-type="application/vnd.oasis.opendocument.presentation"/>
    <manifest:file-entry manifest:full-path="META-INF/manifest.xml" manifest:media-type="text/xml"/>
</manifest:manifest>"""

    return manifest


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    html_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else html_file.replace('.html', '.odp')

    print(f"🔄 Lendo: {html_file}")
    slides, css_root = parse_html_slides(html_file)

    print(f"📋 Encontrados {len(slides)} slides")
    print(f"🎨 Cores extraídas: Lima={css_root.get('lime')}, Navy={css_root.get('navy')}, Olive={css_root.get('olive')}")

    print(f"\n⏳ Gerando .odp...")
    success = create_odp_from_slides(slides, css_root, output_file)

    if success:
        print(f"\n✨ Sucesso! Abra em LibreOffice Impress: {output_file}")
    else:
        print(f"\n❌ Falha ao gerar .odp")
        sys.exit(1)


if __name__ == "__main__":
    main()
