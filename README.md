# Gerador de Slides Cefor — Documentação Geral

Documento-índice do projeto. Reúne o estado de tudo: a skill genérica de apresentações, a pesquisa para a
futura skill educacional, os materiais de submissão ao Concefor e as decisões tomadas.

**Última atualização:** junho de 2026.

---

## 1. Visão geral

O projeto entrega uma **skill que gera apresentações com a identidade visual oficial do Cefor/Ifes**, em
HTML autossuficiente, a partir do conteúdo entregue pela pessoa. O objetivo é permitir que **qualquer
servidor** padronize slides rapidamente, integrando a IA generativa ao padrão institucional que a
instituição já distribui.

Dois produtos estão previstos:
1. **`cefor-slides` (genérica):** pronta. Para uso geral (reuniões, eventos, comunicados, relatórios,
   materiais informativos). Sem cunho educacional.
2. **Skill educacional (futura):** apenas pesquisa e arquitetura por enquanto. Para professores, com
   metodologias pedagógicas. Conteúdo guardado em `pesquisa-skill-educacional/`.

---

## 2. Mapa de pastas

```
article-concefor/
├── README.md                              # Este índice
├── ANALISE-COMPARATIVA-GERADORES-SLIDES.md# Comparação dos 3 geradores + escolha da base
│
├── cefor-slides/                          # A SKILL GENÉRICA (produto principal, pronto)
│   ├── SKILL.md                           # Fluxo da skill (ler primeiro)
│   ├── README.md                          # Doc da skill
│   ├── CEFOR_BRAND.md                     # Identidade oficial (cores, Open Sans, SVGs, voz)
│   ├── STYLE_PRESETS.md                   # Versão A (Cor Sólida) e Versão B (Degradê) + 10 modelos
│   ├── html-template.md                   # Arquitetura HTML/JS + edição inline
│   ├── viewport-base.css                  # CSS do palco fixo 16:9
│   ├── brand/CEFOR-Design-System.dc.html  # Design system OFICIAL (referência visual)
│   ├── slide-patterns/slide-patterns.md   # Catálogo genérico de padrões de slide
│   ├── exemplos/exemplo-versao-a.html     # Deck de exemplo (Versão A), já com acessibilidade corrigida
│   └── scripts/                           # deploy.sh (link), extract-pptx.py (entrada PPTX)
│
├── pptx/                                  # Skill de PPTX da ANTHROPIC (proprietária; NÃO é nossa)
│                                          # Usada para exportar .pptx editável. Não redistribuir.
│
├── pesquisa-skill-educacional/            # Base para a FUTURA skill educacional
│   ├── README.md
│   ├── REFERENCIAIS-PEDAGOGICOS.md        # Estado da arte (metodologias + cognição) com links
│   ├── ARQUITETURA-SKILL-EDUCACIONAL.md   # Arquitetura de 2 camadas + decisões pendentes
│   ├── padroes-pedagogicos-rascunho.md    # Padrões pedagógicos (movidos da skill genérica)
│   └── exemplo-educacional.html           # Deck educacional de exemplo (Versão B)
│
├── concefor/                              # Submissão ao VIII Concefor (Produção Técnica, Eixo 1)
│   ├── RASCUNHO-SUBMISSAO-CONCEFOR.md     # Título, resumo (<=500 palavras), descrição, vídeo, checklist
│   ├── FUNDAMENTACAO-CONCEFOR.md          # 7 pilares teóricos/legais com referências
│   ├── AVALIACAO-PROTOTIPO.md             # Auditoria de acessibilidade (WCAG) + inspeção heurística
│   └── figura-representativa.html         # Slide-título anonimizado para gerar a imagem (PNG)
│
├── cefor-slides.zip                       # Pacote da skill genérica para upload no Claude Web
└── skills-extract/                        # Material auxiliar (extração de skills); descartável
```

---

## 3. A skill genérica `cefor-slides`

- **Entrada:** conteúdo entregue pela pessoa (texto, tópicos, imagens).
- **Fluxo:** detectar operação, coletar conteúdo, mostrar 2 prévias (Versão A e B), gerar, entregar,
  exportar sob demanda. Detalhes em [cefor-slides/SKILL.md](cefor-slides/SKILL.md).
- **Saída:**
  - **HTML** (padrão, fonte da verdade): arquivo único, abre em qualquer navegador/projetor, com edição
    de texto inline (tecla E, Ctrl+S).
  - **PowerPoint editável (.pptx)** sob demanda, via a skill de PPTX, preenchendo o **modelo oficial** do
    Cefor (ver seção 4).
  - **Link** (Vercel) sob demanda.
- **Identidade oficial:** Lima `#B0CB1F`, Azul `#2C459A`, Oliva `#8C9A0D`, degradê CEFOR; fonte **Open
  Sans**; seta CEFOR, logo IFES, rodapé `cefor.ifes.edu.br`; duas linguagens visuais (A e B), 10 modelos
  1920×1080. Fonte da verdade: [cefor-slides/brand/CEFOR-Design-System.dc.html](cefor-slides/brand/CEFOR-Design-System.dc.html).
- **Acessibilidade:** contraste WCAG, navegação por teclado, `prefers-reduced-motion`, nomes acessíveis no
  logo (ver auditoria em `concefor/AVALIACAO-PROTOTIPO.md`).
- **Instalação:** copiar a pasta `cefor-slides/` para `~/.claude/skills/` (Claude Code) ou subir o
  `cefor-slides.zip` no Claude Web (Configurações, Capabilities, Skills, Upload).

---

## 4. Exportação para PowerPoint e a skill de PPTX (decisão de arquitetura)

A exportação `.pptx` é feita por **composição** com a **skill de PPTX da Anthropic** (pasta `pptx/`), não
por código próprio. Decisão: **manter separada, nunca fundir**.

- **Motivo (licença):** a skill de PPTX é proprietária; a LICENSE.txt proíbe copiar, criar derivados,
  redistribuir ou manter cópias fora do Claude. Fundir violaria a licença.
- **Como funciona:** dentro do Claude, a `cefor-slides` delega a geração do `.pptx` à skill de PPTX,
  preferencialmente **editando o modelo `.pptx` oficial** do Cefor. Isso entrega um PowerPoint editável já
  no padrão institucional e fecha a lacuna entre a IA e os modelos que a instituição já distribui.
- **Regra de distribuição:** a pasta `pptx/` **não** deve ser empacotada/redistribuída com a
  `cefor-slides` nem incluída na submissão do Concefor. No Claude Web a skill de PPTX já é nativa.

---

## 5. Futura skill educacional

A `cefor-slides` é genérica de propósito. A vertente educacional foi separada e está em
`pesquisa-skill-educacional/`, com:
- Referenciais pedagógicos (Gagné, BOPPPS, 5E, PBL, Sala invertida, Ausubel, Kolb, Freire; Mayer, carga
  cognitiva, Assertion-Evidence, UDL, WCAG, Bloom) com links.
- Arquitetura proposta em **duas camadas**: menu de metodologias escolhível pelo professor + princípios de
  design de aprendizagem sempre aplicados.
- Decisões pendentes (amplitude do menu, metodologia padrão, Assertion-Evidence por padrão, camada 2
  automática). Ver [pesquisa-skill-educacional/README.md](pesquisa-skill-educacional/README.md).

---

## 6. Submissão ao Concefor (VIII Concefor, ago/2026)

- **Modalidade:** Produção Técnica. **Categoria:** Recursos Tecnológicos e Digitais. **Eixo:** 1 (EaD,
  dimensões institucionais e de gestão; uso responsável de IA).
- **Materiais prontos** em `concefor/`: rascunho da submissão (resumo até 500 palavras, sem travessão, com
  a palavra "skill" e a descrição obrigatória de uso de IA), fundamentação com referências, avaliação do
  protótipo e figura representativa anonimizada.
- **Atenção:** revisão cega exige anonimato; anonimizar a marca em imagem e vídeo na fase de avaliação e
  declarar a skill de PPTX como dependência de terceiros (não como autoria).
- **Pendências do autor:** definir autores e inscrever, gravar o vídeo (até 3 min), capturar o PNG da
  figura, colar no template oficial e exportar em PDF, e e-mail à organização confirmando eixo, categoria
  e uso do nome da instituição na fase cega.

---

## 7. Linha do tempo de decisões

1. Comparados 3 geradores; escolhido o **frontend-slides** como base (facilidade + qualidade visual).
2. Criada a `cefor-slides` com a **identidade oficial** do Cefor (substituiu uma marca extraída por
   engano do site MOOC).
3. **Pivot:** a skill passou a ser **genérica** (sem cunho educacional); a parte educacional virou
   pesquisa para uma skill futura.
4. Decidido enquadrar a submissão ao Concefor no **Eixo 1** e fundamentá-la com pesquisa dedicada.
5. Incorporada a justificativa concreta: a instituição já tem modelos PPTX, mas a IA é usada por fora
   deles; a skill integra a IA ao padrão.
6. **PDF removido** da skill; exportação passa a ser **PowerPoint editável**, via composição com a skill
   de PPTX (mantida separada por licença).

---

## 8. Próximos passos

- [ ] Obter o **modelo `.pptx` oficial** do Cefor para o caminho de exportação editar a partir dele.
- [ ] Obter o **logo IFES em arquivo** (PNG/SVG) oficial (hoje é um SVG reconstruído fiel).
- [ ] Concefor: gravar vídeo, capturar figura, preencher template e submeter (ver `concefor/`).
- [ ] Quando for o momento, construir a **skill educacional** (ver `pesquisa-skill-educacional/`).
