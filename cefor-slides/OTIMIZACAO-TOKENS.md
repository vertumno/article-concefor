# Otimização de Tokens — `cefor-slides`

> **Data:** 2026-06-19 · **Escopo:** reduzir o consumo de tokens por uso do skill **sem** perder
> qualidade de saída (design fiel à marca Cefor é prioridade máxima). Registro do que foi avaliado,
> alterado, por quê e o impacto medido.

---

## 1. Problema avaliado

Quando o skill gera **uma nova apresentação**, o consumo de tokens vem de dois lugares:

- **Input** — arquivos de apoio carregados em contexto durante as Fases 2 e 3.
- **Output** — o HTML do deck que o modelo emite (tokens de output custam ~5× os de input).

Dois gargalos foram identificados:

### Gargalo A — Design system lido como texto (~16.700 tokens/run)
`brand/CEFOR-Design-System.dc.html` (60 KB) estava marcado como *"consulta de fidelidade"*. É um
artefato **visual renderizado para humanos**. Lido como **markup**, não acrescenta fidelidade: os 10
modelos (A1–A5 / B1–B5) já estão descritos em texto em `STYLE_PRESETS.md`. Um modelo diligente abria
o arquivo e gastava ~16,7 k tokens sem ganho real.

### Gargalo B — Boilerplate reescrito a cada deck (~10.000 tokens/run)
Medição no deck-exemplo (`exemplos/exemplo-versao-a.html`, 662 linhas): **~56% de todo deck é fixo e
idêntico** — head, CSS de palco/tipografia/componentes, controlador JS, edição inline, SVGs de marca.
O modelo **lia** esse boilerplate (`viewport-base.css` + `html-template.md` ≈ 5.000 tokens de input) e
depois **reescrevia** (~5.000 tokens de output) o mesmo conteúdo, deck após deck — além do risco de
*drift* (esquecer `prefers-reduced-motion`, variar o JS, etc.).

---

## 2. Mudanças implementadas

| # | Mudança | Arquivo | Tipo |
|---|---------|---------|------|
| 1 | **Scaffold determinístico**: o modelo escreve só os `<section class="slide">`; o script injeta head + CSS + JS + SVGs de marca byte-corretos e **valida** o resultado | `scripts/new-deck.py` *(novo)* | script (CODE > LLM) |
| 2 | **CSS fixo como fonte única**, extraído verbatim do deck homologado | `scripts/deck-base.css` *(novo)* | componentização |
| 3 | Design system marcado **"nunca carregar como texto"** | `SKILL.md`, `html-template.md`, `CEFOR_BRAND.md` | guardrail / doc |
| 4 | **Índice de classes utilitárias** para escrever corpos sem ler a CSS inteira | `slide-patterns/slide-patterns.md` | doc |
| 5 | Fase 3 reescrita com o **caminho recomendado (scaffold)** + fallback manual; Princípio 5 e tabela de apoio atualizados | `SKILL.md` | doc |

### Como o scaffold é usado (Fase 3)

```bash
python scripts/new-deck.py --version A --title "Título — Cefor/Ifes" --slides corpos.html --out deck.html
# --version B (Degradê) · --lime/--navy ajustam cores dentro dos eixos da marca · --slides - lê do stdin
```

1. O modelo escreve em `corpos.html` **apenas** os `<section class="slide">…</section>`.
2. O script injeta `:root` (versão A/B), `deck-base.css` (palco, tipografia, componentes, edição,
   utilitários KPI/timeline/tabela/badge), os SVGs de marca (`<use href="#seta-cefor">`,
   `url(#wm-setas)`) e o controlador JS. Valida e grava (`[OK] deck válido`).

O resultado continua sendo **um único HTML autossuficiente** — o princípio de zero dependências e
palco fixo 16:9 é preservado; o boilerplate apenas deixa de ser retransmitido pelo modelo.

---

## 3. Validação de qualidade (prioridade máxima)

Feito *round-trip* do deck-exemplo (7 slides) pelo scaffold:

- Deck gerado **válido**; **todos os slides e classes preservados** — paridade verificada em
  `deck-stage`, `ApresentacaoCefor`, `prefers-reduced-motion`, `kpi-grid`, `admin-table`,
  `edit-hotzone`, `Open+Sans`.
- Versões **A e B** corretas (`--slide-bg: #FFFFFF` vs `var(--grad)`).
- Entrada por **arquivo e stdin** funcionando.
- O boilerplate injetado é **idêntico ao deck homologado** → consistência **melhora**, não piora.

> O `new-deck.py` valida estruturalmente antes de gravar (parse + presença dos tokens obrigatórios +
> contagem de slides > 0). Revisão visual final no navegador continua recomendada, como antes.

---

## 4. Mensuração — antes × depois (run típico: 1 deck médio)

| Etapa | ANTES (tok) | DEPOIS (tok) |
|-------|------------:|-------------:|
| SKILL.md | 3.900 | 4.180 |
| CEFOR_BRAND.md | 2.400 | 2.400 |
| STYLE_PRESETS.md | 1.300 | 1.300 |
| slide-patterns.md | 1.000 | 1.350 |
| viewport-base.css | 820 | 0 *(fallback)* |
| html-template.md | 4.140 | 0 *(fallback)* |
| **design system .dc.html** | **16.730** | **0** |
| **Input (leitura)** | **~30.300** | **~9.200** |
| Output do deck (boilerplate + corpos) | ~9.000 | ~4.000 *(só corpos)* |
| **Total instrução + deck** | **~39.300** | **~13.200** |

- **Economia: ~26.000 tokens/deck (~66%)** quando o design system era aberto.
- Cenário conservador (modelo nunca abria o `.dc.html`): de ~22.600 → ~13.200 = **~9.400 tokens
  (~42%)**, só pelo scaffold.
- Os ~5.000 tokens de **output** cortados valem desproporcionalmente mais (output ≈ 5× input).
- Custo recorrente adicionado: **+630 tokens/run** (SKILL e slide-patterns cresceram) — habilitam a
  economia de 26 k. Saldo amplamente positivo.

> Estimativa de tokens ≈ caracteres ÷ 3,6 (PT/markup misto). Valores arredondados.

---

## 5. Arquivos

**Criados**
- `scripts/new-deck.py` — scaffold (zero dependências, stdlib).
- `scripts/deck-base.css` — CSS fixo de todo deck (fonte única, injetada pelo scaffold).

**Editados**
- `SKILL.md` — Fase 3 (scaffold), Princípio 5, tabela de apoio, design system no-read.
- `html-template.md` — design system no-read; passa a ser referência de **fallback manual**.
- `CEFOR_BRAND.md` — fonte da verdade marcada como visual/não-ler-como-texto.
- `slide-patterns/slide-patterns.md` — índice de classes utilitárias + SVGs de marca.

---

## 6. O que **não** foi alterado (de propósito)

- Previews da Fase 2, fluxo de conversação, tokens de marca e os modelos A/B — intactos.
- Duplicação do `:root` entre `CEFOR_BRAND.md` e `html-template.md` — intencional (modelo "inline
  tudo" no fallback); o scaffold passa a ser a fonte única de fato.

## 7. Pendências recomendadas (não tocadas — fora do escopo de tokens)

1. **README.md desatualizado:** ainda menciona export `.pptx`/PDF (Anthropic); o `SKILL.md` já migrou
   para `.odp`. Inconsistência de doc (não lida em runtime, custo de token ~0).
2. **Duplicatas no disco:** `cefor-slides.backup-2026-06-19/` (backup) e
   `producao-tecnica/cefor-slides/` (outra árvore com `skills/`, `stages/`). Não afetam tokens.
