# Identidade visual do Cefor (extraída dos templates oficiais)

> Fonte canônica: `CEFOR Apresentação Cor Sólida.pptx` e `CEFOR Apresentação Degradê.pptx` (nesta pasta). Dados extraídos do XML/mídia dos arquivos em 2026-06-15. A versão operacional (regras de uso) vive em `producao-tecnica/cefor-slides/design-system/`.

## Duas variantes oficiais

### A — Cor Sólida (institucional)
- Fundo cinza claro (`#EAEAEC`) na área de conteúdo, sobre branco.
- Bloco **oliva** (`#8C9A0D` / lima `#B0CB1F`) no canto superior esquerdo + linha-guia vertical oliva.
- Bloco **azul royal** (`#2C459A`) no canto inferior esquerdo.
- Acento **Vermelho IF** (`#CC1111`).
- Rodapé: `cefor.ifes.edu.br` em oliva `#8C9A0D`.
- 15 slides, 14 layouts, 2 masters, 8 imagens.

### B — Degradê
- Faixa superior e fundo em **degradê** (`#C6D452` → `#7FC24A` → `#36B4A6` → `#3F93CE`) com retângulos arredondados decorativos.
- Fundo branco; rodapé/barra lateral cinza (`#EAEAEC`).
- Rodapé: `cefor.ifes.edu.br` em oliva `#8C9A0D`.
- 13 slides, 11 layouts, 2 masters, 9 imagens.

## Tipografia (ambas)
- Títulos e corpo: **Open Sans** (theme: major=Open Sans, minor=Open Sans). Fallback: Arial.

## Cores reais mais usadas (frequência no XML)
- **Sólida:** `#2C459A` (dominante), `#2B2B2B` (tinta), `#5A5A5A` (texto médio), `#CC1111` (Vermelho IF), `#8C9A0D` (oliva), `#EAEAEC` (cinza), `#B0CB1F` (lima).
- **Degradê:** `#2B2B2B`, `#5A5A5A`, `#3F93CE`, `#36B4A6`, `#7FC24A`, `#C6D452`.

> Observação: o `clrScheme` do theme é o esquema genérico antigo do Office (accent1 `#058DC7` etc.) — **não** representa a identidade real. As cores acima (dos slides/master) são as válidas.

## Como a skill usa
1. O `cefor-slides` aplica uma das variantes por deck (padrão = Sólida).
2. Logos/marcas oficiais ficam em `ppt/media/` dos `.pptx` — extrair quando necessário para reuso.
3. Para fidelidade total, a geração pode partir destes `.pptx` como template-base (edição OOXML) em vez de recriar do zero.
