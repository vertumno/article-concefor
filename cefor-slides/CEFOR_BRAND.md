# Identidade Visual do Cefor — Tokens de Marca (OFICIAL)

> **Fonte da verdade (visual, p/ humanos):** `brand/CEFOR-Design-System.dc.html` —
> "Sistema de Design de Apresentações · CEFOR / IFES · 10 modelos em 2 linguagens visuais".
> Renderize no navegador para conferência visual; **não leia como texto** (artefato de ~60 KB sem
> ganho de fidelidade no markup). Os tokens abaixo já são a identidade completa para gerar.
> Estes tokens são a **identidade obrigatória** de toda apresentação gerada pela `cefor-slides`.
> A consistência de marca tem prioridade sobre preferências estéticas genéricas.

---

## Sobre o Cefor

**Cefor** = Centro de Referência em Formação e em Educação a Distância do **Ifes** (Instituto Federal
do Espírito Santo). Instituição **pública federal de educação**. A identidade é **institucional,
limpa e legível em projeção** — séria e moderna, nunca "marketeira".

## Duas linguagens visuais oficiais

Toda apresentação adota **uma** das duas linguagens (ver [STYLE_PRESETS.md](STYLE_PRESETS.md)):

- **Versão A — Cor Sólida:** Lima + azul institucional sobre branco e cinza. Painéis chapados, cantos
  arredondados, seta CEFOR como elemento gráfico. Mais sóbria/institucional.
- **Versão B — Degradê:** Malha de cor verde-lima → verde → ciano → azul, com grafismos geométricos
  (quadrados arredondados em contorno, círculos concêntricos, linhas pontilhadas). Mais moderna/vibrante.

---

## Paleta de cores (oficial)

| Token | Hex | Uso |
|-------|-----|-----|
| `--lime` | `#B0CB1F` | **Lima CEFOR** — cor primária: painéis, barras de título, capas |
| `--lime-dk` | `#9DB400` | Lima escura — hover, ênfase |
| `--olive` | `#8C9A0D` | **Oliva / URL** — rodapé, linha-guia, `cefor.ifes.edu.br` |
| `--navy` | `#2C459A` | **Azul Institucional** — seta, títulos, linhas de destaque |
| `--navy2` | `#2E3F8F` | Azul alternativo |
| `--gray` | `#EAEAEC` | **Cinza Painel** — trilhos laterais e áreas de conteúdo |
| `--gray-dk` | `#D7D7DA` | Cinza escuro — bordas |
| `--ink` | `#2B2B2B` | **Tinta** — texto principal |
| `--muted` | `#5A5A5A` | **Texto médio** — secundário, legendas |
| `--green` | `#2E9B30` | Verde IF — confirmação, destaque |
| `--red` | `#CC1111` | Vermelho IF — alerta (e ponto do logo) |
| branco | `#FFFFFF` | Fundos da Versão A |

**Degradê CEFOR (Versão B)** — paradas: `#C6D452` (lima) → `#7FC24A` (verde) → `#36B4A6` (ciano) →
`#3F93CE` (azul). CSS completo:
```css
--grad: radial-gradient(120% 95% at 88% 6%, #C6D452 0%, rgba(198,212,82,0) 46%),
        radial-gradient(95% 95% at 58% 28%, #7FC24A 0%, rgba(127,194,74,0) 56%),
        radial-gradient(130% 130% at 16% 98%, #3F9FD6 0%, rgba(63,159,214,0) 58%),
        linear-gradient(135deg, #57B86A 0%, #36B4A6 46%, #3F93CE 100%);
```

> Editáveis pela gestão: a lima primária (`#B0CB1F` / `#A6CE39` / `#8C9A0D`) e o azul
> (`#2C459A` / `#2E3F8F` / `#314A99`) — são os dois eixos da marca.

---

## Tipografia

**Família única: Open Sans** (humanista, neutra, legível em projeção). Pesos: 400, 600, 700, 800.

```html
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;600;700;800&display=swap">
```

**Escala (no palco real 1920×1080):**

| Papel | Peso | Tamanho |
|-------|------|---------|
| Título de capa | 800 (ExtraBold) | 80px |
| Título de seção | 700 (Bold) | 54px |
| Título de slide de conteúdo | 700 (Bold) | 36px |
| Corpo / itens de lista | 400 (Regular) | 26px |
| Rodapé (`cefor.ifes.edu.br`) | 600 (SemiBold) | 20px, cor oliva |
| Sobrescrito/eyebrow | 700 | 14–15px, MAIÚSCULAS, letter-spacing .2em |
| Número de seção (01, 02) | 800 | 78–80px, lima (A) ou cinza-claro (B) |

---

## Variáveis CSS (cole no `:root` de todo deck)

```css
:root {
    /* Cores oficiais Cefor/Ifes */
    --lime: #B0CB1F;
    --lime-dk: #9DB400;
    --olive: #8C9A0D;
    --navy: #2C459A;
    --navy2: #2E3F8F;
    --gray: #EAEAEC;
    --gray-dk: #D7D7DA;
    --ink: #2B2B2B;
    --muted: #5A5A5A;
    --green: #2E9B30;
    --red: #CC1111;
    --grad: radial-gradient(120% 95% at 88% 6%,#C6D452 0%,rgba(198,212,82,0) 46%),
            radial-gradient(95% 95% at 58% 28%,#7FC24A 0%,rgba(127,194,74,0) 56%),
            radial-gradient(130% 130% at 16% 98%,#3F9FD6 0%,rgba(63,159,214,0) 58%),
            linear-gradient(135deg,#57B86A 0%,#36B4A6 46%,#3F93CE 100%);

    /* Tipografia */
    --font: 'Open Sans', system-ui, sans-serif;

    /* Animação (sutil — institucional) */
    --ease-out: cubic-bezier(0.16, 1, 0.3, 1);
    --duration: 0.5s;
}
```

---

## Elementos de marca (SVG prontos)

### Logo IFES/Cefor (assinatura)
Grade de quadrados verdes + ponto vermelho. Vem com o texto ao lado. Três versões: **positiva** (cores),
**monocromática** (tinta) e **negativa** (branca sobre fundo). Use `fill="currentColor"` nas versões mono.

```html
<!-- Marca (positiva). Para mono: troque os fills por currentColor e defina a cor no contêiner -->
<div style="display:flex;align-items:center;gap:13px;color:#1a1a1a;">
  <svg width="40" height="54" viewBox="0 0 31 42" style="flex:none;display:block;">
    <circle cx="4.5" cy="4.5" r="4.5" fill="#CE1126"/>
    <rect x="0" y="11" width="9" height="9" rx="1.4" fill="#3A9E3A"/>
    <rect x="0" y="22" width="9" height="9" rx="1.4" fill="#3A9E3A"/>
    <rect x="0" y="33" width="9" height="9" rx="1.4" fill="#3A9E3A"/>
    <rect x="11" y="0" width="9" height="9" rx="1.4" fill="#3A9E3A"/>
    <rect x="11" y="11" width="9" height="9" rx="1.4" fill="#3A9E3A"/>
    <rect x="11" y="22" width="9" height="9" rx="1.4" fill="#3A9E3A"/>
    <rect x="11" y="33" width="9" height="9" rx="1.4" fill="#3A9E3A"/>
    <rect x="22" y="0" width="9" height="9" rx="1.4" fill="#3A9E3A"/>
    <rect x="22" y="22" width="9" height="9" rx="1.4" fill="#3A9E3A"/>
  </svg>
  <div style="line-height:1.14;">
    <div style="font-weight:800;font-size:17px;">INSTITUTO FEDERAL</div>
    <div style="font-weight:600;font-size:12.5px;">Espírito Santo</div>
    <div style="font-weight:400;font-size:11.5px;">Centro de Referência em Formação<br>e em Educação a Distância</div>
  </div>
</div>
```

### Seta CEFOR (símbolo-chave)
Sempre apontando para **baixo-direita**, em **azul** (`--navy`) ou **lima** (`--lime`). É o elemento
gráfico mais forte da marca — use em capas, divisórias e como acento. **Exclusiva da Versão A** (Cor
Sólida). Na Versão B (Degradê) não aparece — o acento gráfico da B são os grafismos do degradê
(quadrados em contorno, círculos concêntricos, linha pontilhada), abaixo.

```html
<svg width="84" height="84" viewBox="0 0 100 100">
  <path d="M0 14L14 0L100 86L86 100Z M78 8H100V100H78Z M6 78H100V100H6Z" fill="#2C459A"/>
</svg>
```

### Marca d'água (setas em mosaico)
Padrão de setas em baixa opacidade sobre painéis (lima, cinza ou degradê).

```html
<svg style="position:absolute;inset:0;width:100%;height:100%;" aria-hidden="true">
  <defs>
    <pattern id="wm" width="56" height="56" patternUnits="userSpaceOnUse">
      <path d="M0 14L14 0L100 86L86 100Z M78 8H100V100H78Z M6 78H100V100H6Z"
            transform="scale(0.42)" fill="rgba(0,0,0,0.06)"/>
    </pattern>
  </defs>
  <rect width="100%" height="100%" fill="url(#wm)"/>
</svg>
```

### Ícones sociais (badges circulares)
Instagram, YouTube, site. Fundo **tinta** na Versão A; **azul** (`--navy`) na Versão B. (Ver SVGs no
design system.)

### Grafismos da Versão B
Quadrados arredondados em contorno (3 tamanhos), círculos concêntricos, linha pontilhada — em branco
translúcido sobre o degradê, ou em verde/ciano sobre cinza.

### Rodapé institucional
Texto `cefor.ifes.edu.br` em **oliva**, SemiBold, canto inferior direito; frequentemente com uma
linha-guia oliva fina.

---

## Voz e tom (textual nos slides)

- **Institucional, mas humano.** Sério e acolhedor; nunca "folder de marketing" nem juridiquês.
- **Pessoas e prática, não funções abstratas.**
- **Dados dentro de contexto**, não números soltos.
- **Clareza acima de tudo** — público diverso (gestão, servidores, comunidade).
- **Objetivo e direto**, orientado à mensagem-chave da apresentação.

---

## Anti-patterns (PROIBIDO)

- ❌ Trocar a paleta/fonte oficiais por cores ou fontes genéricas.
- ❌ Gradientes "AI slop" (roxo/rosa) — o único degradê é o degradê CEFOR oficial.
- ❌ Emojis como ícones (usar os SVGs da marca / ícones de traço).
- ❌ Seta CEFOR em direção errada (deve apontar para baixo-direita) ou em cor fora de azul/lima.
- ❌ Seta CEFOR na Versão B (Degradê) — é exclusiva da Versão A; na B use os grafismos do degradê.
- ❌ Logo esticado/desproporcional ou sem área de respiro.
- ❌ Baixo contraste; texto abaixo do tamanho de leitura confortável.
- ❌ Animações chamativas — movimento sutil e funcional.
- ❌ Misturar Versão A e Versão B no mesmo deck (escolha uma linguagem).
