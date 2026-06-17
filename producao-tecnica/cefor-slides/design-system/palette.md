# Color Palette — Cefor

Cores extraídas dos templates oficiais em `referencias/CEFOR Apresentação *.pptx` (fonte canônica). Hex de 6 dígitos. Sem `#` no PptxGenJS; com `#` em HTML/CSS.

O Cefor tem **duas variantes visuais**. A skill aplica uma delas por deck (escolha do professor; padrão = Sólida).

## Variante A — Sólida (institucional, padrão)

| Papel | Hex | Uso |
|-------|-----|-----|
| Primária (azul Cefor) | 2C459A | Blocos, barras, títulos de seção |
| Secundária (oliva) | 8C9A0D | Blocos, linha-guia, rodapé, realces |
| Secundária clara (lima) | B0CB1F | Variação de realce/gráficos |
| Acento (Vermelho IF) | CC1111 | Destaques pontuais, alertas |
| Fundo do slide | FFFFFF | Base |
| Área de conteúdo | EAEAEC | Painel de conteúdo |

```
chartColors: ["2C459A", "8C9A0D", "CC1111", "5A5A5A", "B0CB1F"]
```

## Variante B — Degradê

| Papel | Hex | Uso |
|-------|-----|-----|
| Degradê (azul → ciano → verde → lima) | 3F93CE → 36B4A6 → 7FC24A → C6D452 | Faixa superior, capas |
| Realce | 36B4A6 | Títulos, ícones, rodapé |
| Fundo do slide | FFFFFF | Base |
| Área de rodapé | EAEAEC | Faixa inferior |

```
chartColors: ["3F93CE", "36B4A6", "7FC24A", "C6D452", "5A5A5A"]
```

## Texto (comum às duas variantes)

| Papel | Hex |
|-------|-----|
| Texto principal | 2B2B2B |
| Texto secundário | 5A5A5A |
| Texto máx. contraste | 000000 |

## Elementos de marca (em ambas)

- Rodapé: `cefor.ifes.edu.br` (oliva `#8C9A0D` em ambas as variantes).
- Logos/marcas oficiais: `referencias/CEFOR Apresentação *.pptx` (`ppt/media/`).

## Regras de contraste

- Texto de corpo sobre fundo: mínimo 4.5:1.
- Texto sobre formas coloridas: mínimo 3:1. ⚠️ Texto branco sobre **oliva 8C9A0D** é limítrofe — preferir texto escuro (2B2B2B) sobre oliva, e texto branco sobre **azul 2C459A** / **azul degradê 3F93CE**.
- Nunca texto claro em fundo claro, nem escuro em fundo escuro.
