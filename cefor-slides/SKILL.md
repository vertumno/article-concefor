---
name: cefor-slides
description: Cria rapidamente apresentações de slides com a identidade visual oficial do Cefor/Ifes (lima + azul institucional, Open Sans, seta CEFOR, 2 linguagens visuais), em HTML autossuficiente, a partir do conteúdo entregue. Ferramenta genérica para qualquer servidor do Cefor (reuniões, eventos, comunicados, relatórios, materiais informativos). Saída padrão em HTML; exporta também para LibreOffice Impress editável (.odp) sob demanda, alinhado com a política de software livre do governo federal. Descobre o estilo mostrando prévias, não pedindo descrições abstratas.
---

# Cefor Slides

Gera apresentações **HTML de alta qualidade com a marca oficial do Cefor/Ifes**, sem dependências (um
arquivo único que abre em qualquer navegador/projetor), **a partir do conteúdo entregue pela pessoa**.

Ferramenta **genérica**, para **qualquer servidor do Cefor** padronizar slides rapidamente — reuniões,
eventos, comunicados, relatórios, materiais informativos, etc. Não tem cunho educacional/pedagógico (uma
skill dedicada a apresentações educacionais será criada à parte).

Baseada no padrão "frontend-slides" (palco fixo 16:9, mostrar-não-contar, edição inline), aplicando o
**Sistema de Design de Apresentações oficial do Cefor** (ver
[brand/CEFOR-Design-System.dc.html](brand/CEFOR-Design-System.dc.html)).

**Saída:** HTML é o formato **padrão**. O **LibreOffice Impress editável (.odp)** é gerado **apenas
quando a pessoa pedir** (ver Fase 6), alinhado à política de software livre do governo federal.

## Princípios

1. **Marca Cefor sempre.** Toda apresentação usa a paleta oficial (lima `#B0CB1F` + azul `#2C459A` +
   oliva), a fonte **Open Sans** e os elementos de marca (seta CEFOR, logo IFES, rodapé). Ver
   [CEFOR_BRAND.md](CEFOR_BRAND.md). Consistência de marca > estética genérica. Escolha **uma** das duas
   linguagens oficiais (Versão A ou B) e use-a no deck inteiro.
2. **Rápido, a partir do conteúdo entregue.** O foco é converter o conteúdo da pessoa em um deck pronto
   com o mínimo de fricção.
3. **Zero dependências.** Arquivo HTML único, CSS/JS inline. Sem npm, sem build.
4. **Mostrar, não contar.** Gere prévias visuais reais (não opções abstratas). As pessoas escolhem vendo.
5. **Palco fixo 16:9 (INEGOCIÁVEL).** Slides em 1920×1080 escalados como um todo. Nunca refluir conteúdo
   por dispositivo. O CSS do palco (`viewport-base.css`) é injetado pelo scaffold `new-deck.py`; em todo
   deck ele deve estar presente por completo.
6. **Acessível e claro.** Contraste WCAG AA, `prefers-reduced-motion`, linguagem clara.
7. **Sem "AI slop".** Respeite os anti-patterns do Cefor (sem gradiente roxo, sem emoji-ícone, sem
   animação chamativa). Ver [CEFOR_BRAND.md](CEFOR_BRAND.md).

---

## Fase 0: Detectar a operação

- **A. Nova apresentação** — criar do zero → Fase 1.
- **B. Converter PowerPoint** — partir de um .pptx existente → Fase 4.
- **C. Melhorar/editar** — aprimorar um deck HTML existente → leia, entenda e melhore mantendo a marca
  Cefor e as regras de palco fixo (conte elementos antes de adicionar; se estourar, divida em mais slides).

---

## Fase 1: Descoberta de conteúdo (nova apresentação)

Pergunte tudo de uma vez (use a UI de perguntas estruturadas se houver; senão, uma mensagem com opções
numeradas):

1. **Tema/assunto** — sobre o que é a apresentação?
2. **Finalidade** — ex.: reunião, evento, comunicado, prestação de contas, relatório, material
   informativo (livre; ajuda a calibrar tom e densidade).
3. **Mensagem-chave** — o que a audiência precisa entender/decidir ao final?
4. **Público** — interno, conselho/comitê, comunidade, evento externo, etc.
5. **Tamanho** — Curta (5–10) / Média (10–20) / Longa (20+).
6. **Conteúdo** — Já tenho o conteúdo pronto / Tenho anotações / Só tenho o tema.
7. **Densidade** —
   - *Baixa / para apresentar ao vivo*: poucas palavras, mais visual, mais slides.
   - *Alta / para ler depois*: slides autoexplicativos, tabelas, mais texto (relatório/material informativo).

Se a pessoa tiver o conteúdo, peça para compartilhar. Se houver imagens (logo, fotos, gráficos, telas),
peça a pasta: liste, avalie a usabilidade de cada uma e organize o roteiro **em torno** delas. Se houver
logo do Cefor, embuta nas prévias da Fase 2.

---

## Fase 2: Descoberta de estilo (mostrar, não contar)

O Cefor tem **duas linguagens visuais oficiais** — não invente estilos. Leia
[STYLE_PRESETS.md](STYLE_PRESETS.md) e gere **2 prévias** do slide-título real do deck:

- **Versão A — Cor Sólida** (lima + azul; sóbria, institucional; padrão para reuniões, relatórios, comunicados).
- **Versão B — Degradê** (malha verde-ciano-azul + grafismos; moderna; eventos, aberturas, telas grandes).

Use a tabela "Como escolher por ocasião" de STYLE_PRESETS.md para indicar a recomendada. Cada prévia deve
ser fiel ao design system oficial (modelo A1 ou B1), com seta CEFOR, logo IFES e rodapé.

**Regras de autenticidade das prévias (INEGOCIÁVEL):**
- Cada prévia parece um primeiro slide real do deck, não um cartão de diagnóstico.
- Nunca renderize texto de processo no slide: "prévia", "opção A/B", "estilo", "Versão A/B" como rótulo,
  nomes de arquivo, anotações de requisito. Os nomes das linguagens só vão na mensagem ao usuário.
- "Moldura" só com elementos reais: título do deck, data, responsável, logo/rodapé Cefor.

Salve as prévias em `.cefor-slides/previas/` (versao-a.html, versao-b.html), autossuficientes e compactas,
mostrando um slide-título animado. Abra cada uma para a pessoa.

**Escolha:** pergunte "Qual linguagem você prefere? Versão A (Cor Sólida) / Versão B (Degradê)". Se a
pessoa quiser, pode ajustar a lima/azul dentro das opções oficiais (ver CEFOR_BRAND.md).

---

## Fase 3: Gerar a apresentação

Gere o deck completo com o conteúdo da Fase 1 e o estilo da Fase 2.

### Caminho recomendado (econômico): scaffold

**Você escreve apenas os corpos de slide; o script monta o resto.** ~56% de todo deck é
boilerplate idêntico (head, CSS de palco/tipografia/componentes, controlador JS, edição inline,
SVGs de marca). Não recopie isso — `scripts/new-deck.py` injeta tudo de forma byte-correta:

```bash
python scripts/new-deck.py --version A --title "Título — Cefor/Ifes" --slides corpos.html --out deck.html
# --version B para Degradê; --lime/--navy para ajustar cores dentro dos eixos da marca
```

1. Escreva em `corpos.html` **só** os `<section class="slide">…</section>` (sem `<head>`, sem `<script>`).
2. Rode o script. Ele injeta `:root` (versão A/B), `deck-base.css` (palco, tipografia, componentes,
   edição, utilitários KPI/timeline/tabela/badge), os SVGs de marca (`<use href="#seta-cefor">`,
   `url(#wm-setas)`) e o controlador JS. Valida o resultado antes de gravar (`[OK] deck válido`).

**Para escrever os corpos, basta:** [slide-patterns/slide-patterns.md](slide-patterns/slide-patterns.md)
(catálogo de padrões + classes utilitárias) e os modelos de [STYLE_PRESETS.md](STYLE_PRESETS.md) (já lido
na Fase 2). Os tokens de marca e SVGs estão em [CEFOR_BRAND.md](CEFOR_BRAND.md) (já lido na Fase 2).
**Não** releia `viewport-base.css` nem o boilerplate de `html-template.md` — o script já os contém.

> **Fallback manual** (só se o script não puder rodar): monte o HTML inteiro à mão seguindo
> [html-template.md](html-template.md) e incluindo [viewport-base.css](viewport-base.css) por completo.

**Monte a sequência a partir do conteúdo**, usando os padrões do catálogo. Estrutura típica:
capa → (índice) → (divisória) → conteúdo (listas, duas colunas, indicadores, gráficos, tabelas) →
mensagem-chave/destaque → próximos passos/conclusão → encerramento. Títulos são afirmações; dados com
contexto.

**Aplique a densidade escolhida:**
- *Baixa/ao vivo:* mais slides, poucas ideias por slide, títulos grandes, frases curtas, ritmo de
  apresentador.
- *Alta/para ler:* slides autoexplicativos, grades, tabelas, diagramas anotados, texto conciso mas
  completo. Nunca deixe virar bagunça visual — se estourar, divida.

**Requisitos:**
- Arquivo HTML único, todo CSS/JS inline (o scaffold já garante isso; no fallback manual, inclua o
  `viewport-base.css` inteiro no `<style>`).
- Fonte institucional **Open Sans** (400/600/700/800) via Google Fonts.
- Reproduza fielmente os modelos oficiais da linguagem escolhida (A1–A5 ou B1–B5), traduzindo as
  proporções do preview (960×540) para o palco real 1920×1080.
- Sempre: **seta CEFOR** (azul/lima), **logo IFES** na capa e encerramento, **rodapé**
  `cefor.ifes.edu.br` em oliva (SVGs prontos em CEFOR_BRAND.md).
- Texto na voz do Cefor (claro, humano, objetivo; sem juridiquês nem "folder de gestão").
- Edição inline incluída por padrão (tecla **E**; Ctrl+S salva).
- Comentários `/* === SEÇÃO === */` e `<!-- ID do modelo -->` em cada slide.
- Não misture Versão A e Versão B no mesmo deck.

**Depois de gerar, verifique** em screenshots renderizados: nada estoura o slide, painéis não se
sobrepõem, palco continua 16:9 (cheque 1280×720 e um viewport de celular). Checagem só de `scrollHeight`
não basta — grades podem se cobrir visualmente.

---

## Fase 4: Converter PowerPoint

1. **Extrair** — `python scripts/extract-pptx.py <entrada.pptx> <pasta_saida>` (instale se preciso:
   `pip install python-pptx`).
2. **Confirmar** — apresente títulos, resumo do conteúdo e contagem de imagens extraídos.
3. **Estilo** — vá para a Fase 2.
4. **Gerar** — converta para a variação Cefor escolhida, preservando texto, imagens (de `assets/`),
   ordem dos slides e notas do apresentador (como comentários HTML).

---

## Fase 5: Entrega

1. **Limpar** — apague `.cefor-slides/previas/` se existir.
2. **Abrir** — abra o `.html` no navegador.
3. **Resumir** para a pessoa:
   - Local do arquivo, nome do estilo, nº de slides.
   - Navegação: setas, espaço, swipe no celular.
   - Como personalizar: variáveis CSS no `:root` (cores), link de fonte (tipografia).
   - Edição inline: passe o mouse no canto superior esquerdo ou tecle **E**, clique no texto para editar,
     **Ctrl+S** salva uma cópia.
   - Ofereça os próximos passos: pedir ajustes, editar texto no navegador, ou exportar/compartilhar.

---

## Fase 6: Exportar e compartilhar (sob demanda)

**O HTML é a entrega padrão.** Só gere outros formatos se a pessoa pedir. Pergunte: "Quer também em
**LibreOffice Impress editável (.odp)** ou **publicar um link**? Ou ficamos só no HTML?"

### 6A: Exportar LibreOffice Impress editável (.odp)

Use o **script Python nativo** (`scripts/generate-odp.py`) para gerar um `.odp`
**editável** (texto editável, não imagem). É o formato recomendado, pois alinha-se com a política de
software livre do governo federal brasileiro (LibreOffice como padrão oficial):

```bash
python scripts/generate-odp.py <deck.html> <deck.odp>
```

**Processo:**

1. O script lê o HTML da apresentação (da Fase 5).
2. Extrai os slides, conteúdo, cores e tipografia (das variáveis CSS `:root`).
3. Reconstrói a apresentação em formato `.odp` (ODF — Open Document Format).
4. Preserva a marca Cefor (cores lima, azul, oliva; font Open Sans; elementos visuais).
5. Salva um arquivo editável pronto em LibreOffice Impress.

**Dependências:**
```bash
pip install odfpy        # obrigatória (gera ODF válido)
pip install pillow       # opcional (só para embutir imagens raster locais)
```

O script **valida o arquivo reabrindo-o** antes de declarar sucesso (`[OK] ODF válido`). Ainda assim,
depois de gerar, abra o `.odp` em **LibreOffice Impress** e revise:
- [ ] Texto editável correto (títulos, antetítulos, bullets, mensagem-chave, encerramento)
- [ ] Cores Cefor aplicadas (azul nos títulos, lima nos marcadores, oliva no rodapé)
- [ ] Fonte Open Sans (instale-a no sistema se o LibreOffice substituir)
- [ ] Imagens raster locais presentes (se houver `<img>`)

> **Escopo da exportação (consciente):** o `.odp` carrega o **conteúdo editável** (texto, bullets,
> cores, fonte). Os **grafismos do layout** (SVGs, degradês, molduras, KPIs/tabelas como blocos
> visuais) **não** são transpostos — pertencem à fidelidade pixel-perfect do HTML, que permanece como
> **fonte da verdade**. Tabelas/KPIs chegam ao `.odp` como texto corrido (editável), não como tabela.
>
> **Alinhamento institucional:** o formato .odp segue a recomendação do governo federal para software
> livre; é padrão aberto (ODF), sem dependências proprietárias.

### 6B: Publicar link (Vercel)
```bash
bash scripts/deploy.sh <caminho-da-apresentacao>
```
Aceita uma pasta (com index.html) ou um HTML único. Para muitos assets, publique a pasta. Confira no
link publicado se todas as imagens carregam. **Nota institucional:** confirme antes de publicar conteúdo
do Cefor em hospedagem externa; para uso interno, o `.odp` ou o HTML costuma bastar.

---

## Arquivos de apoio

| Arquivo | Para quê | Quando ler |
|---------|----------|-----------|
| [brand/CEFOR-Design-System.dc.html](brand/CEFOR-Design-System.dc.html) | Design system oficial (artefato **visual** renderizado, ~60 KB, p/ humanos) | **Nunca carregar como texto** — não há ganho de fidelidade lendo o markup (~17 k tokens). A fonte de layout do agente é STYLE_PRESETS.md + html-template.md. Abra no navegador só se a pessoa pedir referência visual. |
| [CEFOR_BRAND.md](CEFOR_BRAND.md) | Tokens de marca, Open Sans, SVGs de logo/seta, voz, anti-patterns | Sempre (Fase 2 e 3) |
| [STYLE_PRESETS.md](STYLE_PRESETS.md) | Versão A (Cor Sólida) e Versão B (Degradê) + 10 modelos | Fase 2 (estilo) |
| [slide-patterns/slide-patterns.md](slide-patterns/slide-patterns.md) | Catálogo de padrões + classes utilitárias prontas | Fase 3 (gerar) — **principal p/ escrever corpos** |
| `scripts/new-deck.py` | **Scaffold**: monta o deck a partir só dos corpos de slide (injeta head/CSS/JS/marca fixos) | Fase 3 (caminho recomendado) |
| `scripts/deck-base.css` | CSS fixo de todo deck (injetado pelo scaffold) | Não ler — injetado por `new-deck.py` |
| [html-template.md](html-template.md) | Arquitetura HTML/JS completa | Só no **fallback manual** (sem o scaffold) |
| [viewport-base.css](viewport-base.css) | CSS do palco fixo | Só no **fallback manual** (o scaffold já o contém) |
| `scripts/extract-pptx.py` | Extrair conteúdo de .pptx (entrada da Fase 4) | Fase 4 (converter) |
| `scripts/generate-odp.py` | Exportar HTML → `.odp` editável (LibreOffice) | Fase 6A (sob demanda) |
| `scripts/deploy.sh` | Publicar link (Vercel) | Fase 6 (sob demanda) |

> **Export para `.odp` editável** é feito pelo script nativo `scripts/generate-odp.py` (odfpy),
> empacotado com a skill — sem dependências proprietárias, alinhado à política de software livre do
> governo federal (ver Fase 6A). `extract-pptx.py` é apenas **entrada** (converter um `.pptx` recebido),
> não exportação.
> Skill **educacional** (com metodologias pedagógicas) será criada à parte; pesquisa e arquitetura já
> documentadas em [../pesquisa-skill-educacional/](../pesquisa-skill-educacional/).
