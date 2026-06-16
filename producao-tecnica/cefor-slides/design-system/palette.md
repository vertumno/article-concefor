# Color Palette — Cefor

Cores extraídas dos templates oficiais em `referencias/CEFOR Apresentação *.pptx` (fonte canônica). Hex de 6 dígitos. Sem `#` no PptxGenJS; com `#` em HTML/CSS.

O Cefor tem **duas variantes visuais**. A skill aplica uma delas por deck (escolha do professor; padrão = Sólida).

## Variante A — Sólida (institucional, padrão)

| Papel | Hex | Uso |
|-------|-----|-----|
| Primária (azul Cefor) | 314A99 | Blocos, barras, títulos de seção |
| Secundária (oliva) | A3A51A | Blocos, linha-guia, rodapé, realces |
| Secundária clara (lima) | B0C804 | Variação de realce/gráficos |
| Acento (grená) | 980000 | Destaques pontuais, alertas |
| Fundo do slide | FFFFFF | Base |
| Área de conteúdo | EEEEEE | Painel de conteúdo |

```
chartColors: ["314A99", "A3A51A", "980000", "595959", "B0C804"]
```

## Variante B — Degradê

| Papel | Hex | Uso |
|-------|-----|-----|
| Degradê (escuro → claro) | 134F5C → 125E65 → 08A18E | Faixa superior, capas |
| Realce | 08A18E | Títulos, ícones, rodapé |
| Fundo do slide | FFFFFF | Base |
| Área de rodapé | EEEEEE | Faixa inferior |

```
chartColors: ["134F5C", "08A18E", "125E65", "595959"]
```

## Texto (comum às duas variantes)

| Papel | Hex |
|-------|-----|
| Texto principal | 343434 |
| Texto secundário | 595959 |
| Texto máx. contraste | 000000 |

## Elementos de marca (em ambas)

- Rodapé: `cefor.ifes.edu.br` (oliva na Sólida; verde-lima na Degradê).
- Logos/marcas oficiais: `referencias/CEFOR Apresentação *.pptx` (`ppt/media/`).

## Regras de contraste

- Texto de corpo sobre fundo: mínimo 4.5:1.
- Texto sobre formas coloridas: mínimo 3:1. ⚠️ Texto branco sobre **oliva A3A51A** é limítrofe — preferir texto escuro (343434) sobre oliva, e texto branco sobre **azul 314A99** / **teal 134F5C**.
- Nunca texto claro em fundo claro, nem escuro em fundo escuro.
