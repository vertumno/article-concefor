# Cefor Slides

Skill para **criar rapidamente apresentações com a identidade oficial do Cefor/Ifes** — em HTML
autossuficiente, sem dependências, **a partir do conteúdo entregue**.

Ferramenta **genérica**, para **qualquer servidor do Cefor** padronizar slides: reuniões, eventos,
comunicados, prestação de contas, relatórios, materiais informativos, etc.

> **Não tem cunho educacional.** Uma **skill separada** para apresentações educacionais (com metodologias
> pedagógicas) será criada à parte — a pesquisa e a arquitetura já estão em
> [../pesquisa-skill-educacional/](../pesquisa-skill-educacional/).

Baseada no padrão `frontend-slides` (palco fixo 16:9, "mostrar não contar", edição inline), aplicando o
**Sistema de Design de Apresentações oficial do Cefor**. A escolha da base está em
[../ANALISE-COMPARATIVA-GERADORES-SLIDES.md](../ANALISE-COMPARATIVA-GERADORES-SLIDES.md).

---

## O que ela faz

- Conversa com a pessoa (não precisa saber design nem código).
- Recebe o **conteúdo entregue** e monta o deck com os padrões da marca.
- Mostra **2 prévias** (Versão A e Versão B) na identidade oficial do Cefor para escolher.
- Gera **um arquivo HTML** que abre em qualquer navegador/projetor.
- Permite **editar o texto no próprio navegador** (tecla **E**, Ctrl+S salva).
- **Sob demanda:** exporta para **PowerPoint editável (.pptx)** e/ou publica um **link**.

## Saída

- **Padrão: HTML.** É sempre o entregável principal e a fonte da verdade.
- **PowerPoint editável (.pptx)** quando a pessoa pedir, idealmente preenchendo o **modelo `.pptx`
  oficial** do Cefor (gerado pela skill de PPTX, de terceiros; ver abaixo).
- **Link** (Vercel) quando a pessoa pedir, com aval para conteúdo institucional.

## Identidade oficial (resumo)

Fonte da verdade: [brand/CEFOR-Design-System.dc.html](brand/CEFOR-Design-System.dc.html).

- **Cores:** Lima CEFOR `#B0CB1F` (primária), Azul Institucional `#2C459A`, Oliva `#8C9A0D` (rodapé/URL),
  Cinza `#EAEAEC`; + **degradê CEFOR** (verde→ciano→azul) na Versão B.
- **Fonte única:** **Open Sans** (400/600/700/800).
- **Marca:** logo IFES, **seta CEFOR** (símbolo-chave, aponta para baixo-direita), marca d'água de setas,
  ícones sociais, rodapé `cefor.ifes.edu.br`.
- **Duas linguagens visuais:** Versão A (Cor Sólida) e Versão B (Degradê), 10 modelos 1920×1080.

Detalhes em [CEFOR_BRAND.md](CEFOR_BRAND.md) e [STYLE_PRESETS.md](STYLE_PRESETS.md).

## Estrutura

```
cefor-slides/
├── SKILL.md                  # Fluxo principal da skill (ler primeiro)
├── README.md                 # Este arquivo
├── CEFOR_BRAND.md            # Identidade oficial: cores, Open Sans, SVGs, voz, anti-patterns
├── STYLE_PRESETS.md          # Versão A (Cor Sólida) e Versão B (Degradê) + 10 modelos
├── html-template.md          # Arquitetura HTML/JS + edição inline + modelos
├── viewport-base.css         # CSS obrigatório do palco fixo 16:9
├── brand/
│   └── CEFOR-Design-System.dc.html  # Design system OFICIAL (referência visual)
├── slide-patterns/
│   └── slide-patterns.md     # Catálogo genérico de padrões de slide
├── exemplos/
│   └── exemplo-versao-a.html # Deck de exemplo (Versão A — Cor Sólida)
└── scripts/
    ├── extract-pptx.py       # Converter PowerPoint → conteúdo (Fase 4)
    └── deploy.sh             # Publicar deck → link Vercel (Fase 6B)
```

> Export para `.pptx` editável usa a **skill de PPTX** (de terceiros, proprietária, Anthropic), dentro
> do Claude. Ela **não** faz parte desta skill e **não** deve ser empacotada/redistribuída com ela.

## Como usar

### Como skill do Claude Code
Copie a pasta `cefor-slides/` para `~/.claude/skills/` e invoque `/cefor-slides`. Em seguida, diga o que
quer e entregue o conteúdo (ex.: *"slides para a reunião de coordenação sobre as metas de 2026"* + o texto/
tópicos).

### Sem instalar
Aponte o agente para o `SKILL.md` desta pasta e siga o fluxo das fases.

## Pré-requisitos

| Funcionalidade | Requisito |
|----------------|-----------|
| Criar/editar slides (HTML) | Nada (só o agente) |
| Converter PowerPoint (entrada) | Python 3 + `pip install python-pptx` |
| Exportar `.pptx` editável | Skill de PPTX (Anthropic), dentro do Claude (usa LibreOffice/PptxGenJS) |
| Publicar link | Node.js + conta Vercel (gratuita) |

## Status e próximos passos

- [x] Skill **genérica** (sem cunho educacional), para todos os servidores.
- [x] **Identidade OFICIAL** aplicada (lima/azul/oliva, Open Sans, seta CEFOR, Versões A e B).
- [x] Catálogo genérico de padrões de slide.
- [x] Regra de saída: HTML padrão; **PPTX editável** e link sob demanda (PDF removido).
- [x] Scripts de deploy e extração de PPTX; 1 deck de exemplo (Versão A).
- [x] Export `.pptx` editável via composição com a **skill de PPTX** (editando o modelo oficial).
- [ ] Obter o **modelo `.pptx` oficial** do Cefor para o caminho de exportação editar a partir dele.
- [ ] Adicionar o **logo IFES em arquivo** (PNG/SVG) caso se prefira a imagem oficial ao SVG reconstruído.
- [ ] (Separado) Criar a **skill de apresentações educacionais** — ver
      [../pesquisa-skill-educacional/](../pesquisa-skill-educacional/).
