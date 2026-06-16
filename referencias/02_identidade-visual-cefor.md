# Identidade visual do Cefor (extraída dos templates oficiais)

> Fonte canônica: `CEFOR Apresentação Cor Sólida.pptx` e `CEFOR Apresentação Degradê.pptx` (nesta pasta). Dados extraídos do XML/mídia dos arquivos em 2026-06-15. A versão operacional (regras de uso) vive em `producao-tecnica/cefor-slides/design-system/`.

## Duas variantes oficiais

### A — Cor Sólida (institucional)
- Fundo cinza claro (`#EEEEEE`) na área de conteúdo, sobre branco.
- Bloco **oliva** (`#A3A51A` / lima `#B0C804`) no canto superior esquerdo + linha-guia vertical oliva.
- Bloco **azul royal** (`#314A99`) no canto inferior esquerdo.
- Acento **grená** (`#980000`).
- Rodapé: `cefor.ifes.edu.br` em oliva.
- 15 slides, 14 layouts, 2 masters, 8 imagens.

### B — Degradê
- Faixa superior em **degradê teal → verde** (`#134F5C → #125E65 → #08A18E`) com retângulos arredondados decorativos.
- Fundo branco; faixa inferior cinza (`#EEEEEE`).
- Rodapé: `cefor.ifes.edu.br` em verde-lima.
- 13 slides, 11 layouts, 2 masters, 9 imagens.

## Tipografia (ambas)
- Títulos e corpo: **Arial** (theme: major=Arial, minor=Arial). Web-safe.

## Cores reais mais usadas (frequência no XML)
- **Sólida:** `#314A99` (dominante), `#000000`, `#595959`, `#980000`, `#343434`, `#A3A51A`, `#EEEEEE`, `#B0C804`.
- **Degradê:** `#343434`, `#000000`, `#595959`, `#134F5C`, `#08A18E`, `#125E65`.

> Observação: o `clrScheme` do theme é o esquema genérico antigo do Office (accent1 `#058DC7` etc.) — **não** representa a identidade real. As cores acima (dos slides/master) são as válidas.

## Como a skill usa
1. O `cefor-slides` aplica uma das variantes por deck (padrão = Sólida).
2. Logos/marcas oficiais ficam em `ppt/media/` dos `.pptx` — extrair quando necessário para reuso.
3. Para fidelidade total, a geração pode partir destes `.pptx` como template-base (edição OOXML) em vez de recriar do zero.
