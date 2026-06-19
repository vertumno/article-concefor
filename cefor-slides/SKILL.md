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

**Saída:** HTML é o formato **padrão**. O **PowerPoint editável (.pptx)** é gerado **apenas quando a
pessoa pedir** (ver Fase 6).

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
   por dispositivo. Inclua o conteúdo inteiro de [viewport-base.css](viewport-base.css) em todo deck.
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

**Antes de gerar, leia:**
- [CEFOR_BRAND.md](CEFOR_BRAND.md) — tokens de marca (cole no `:root`).
- [html-template.md](html-template.md) — arquitetura HTML/JS e edição inline.
- [viewport-base.css](viewport-base.css) — CSS obrigatório (inclua inteiro).
- [slide-patterns/slide-patterns.md](slide-patterns/slide-patterns.md) — catálogo genérico de padrões de slide.

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
- Arquivo HTML único, todo CSS/JS inline; inclua o `viewport-base.css` inteiro no `<style>`.
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
pip install lxml pillow requests
```

Depois de gerar, abra o `.odp` em **LibreOffice Impress** e valide:
- [ ] Cores estão corretas (lima, azul, oliva)
- [ ] Fontes (Open Sans) carregaram
- [ ] Imagens estão presentes
- [ ] Layout não estourou slides
- [ ] Acessibilidade mantida (alt text, contraste WCAG)

> **Alinhamento institucional:** formato .odp segue a recomendação do governo federal para software
> livre. O HTML permanece como fonte da verdade; o `.odp` é uma exportação editável sem dependências
> proprietárias.

### 6B: Publicar link (Vercel)
```bash
bash scripts/deploy.sh <caminho-da-apresentacao>
```
Aceita uma pasta (com index.html) ou um HTML único. Para muitos assets, publique a pasta. Confira no
link publicado se todas as imagens carregam. **Nota institucional:** confirme antes de publicar conteúdo
do Cefor em hospedagem externa; para uso interno, o `.pptx` ou o HTML costuma bastar.

---

## Arquivos de apoio

| Arquivo | Para quê | Quando ler |
|---------|----------|-----------|
| [brand/CEFOR-Design-System.dc.html](brand/CEFOR-Design-System.dc.html) | Design system oficial (referência visual: 10 modelos, 2 linguagens) | Consulta de fidelidade |
| [CEFOR_BRAND.md](CEFOR_BRAND.md) | Tokens de marca, Open Sans, SVGs de logo/seta, voz, anti-patterns | Sempre (Fase 2 e 3) |
| [STYLE_PRESETS.md](STYLE_PRESETS.md) | Versão A (Cor Sólida) e Versão B (Degradê) + 10 modelos | Fase 2 (estilo) |
| [viewport-base.css](viewport-base.css) | CSS obrigatório do palco fixo | Fase 3 (gerar) |
| [html-template.md](html-template.md) | Arquitetura HTML/JS + edição inline + modelos | Fase 3 (gerar) |
| [slide-patterns/slide-patterns.md](slide-patterns/slide-patterns.md) | Catálogo genérico de padrões de slide | Fase 3 (gerar) |
| `scripts/extract-pptx.py` | Extrair conteúdo de .pptx | Fase 4 (converter) |
| `scripts/deploy.sh` | Publicar link (Vercel) | Fase 6 (sob demanda) |

> **Export para `.pptx` editável** é feito pela **skill de PPTX** (de terceiros, proprietária, Anthropic),
> usada dentro do Claude e **não** empacotada com a `cefor-slides` (ver Fase 6A).
> Skill **educacional** (com metodologias pedagógicas) será criada à parte; pesquisa e arquitetura já
> documentadas em [../pesquisa-skill-educacional/](../pesquisa-skill-educacional/).
