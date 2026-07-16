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
│   ├── exemplos/                          # 2 decks de exemplo (Versão A e Versão B, acessibilidade auditada)
│   └── scripts/                           # new-deck.py (scaffold), deck-fonts.css (Open Sans offline),
│                                          #   generate-odp.py (.odp, recomendado), generate-pptx.py (.pptx,
│                                          #   se necessário), deck_parser.py, smoke-test.py, extract-pptx.py, deploy.sh
│
├── pesquisa-skill-educacional/            # Base para a FUTURA skill educacional
│   ├── README.md
│   ├── REFERENCIAIS-PEDAGOGICOS.md        # Estado da arte (metodologias + cognição) com links
│   ├── ARQUITETURA-SKILL-EDUCACIONAL.md   # Arquitetura de 2 camadas + decisões pendentes
│   ├── padroes-pedagogicos-rascunho.md    # Padrões pedagógicos (movidos da skill genérica)
│   └── exemplo-educacional.html           # Deck educacional de exemplo (Versão B)
│
├── concefor/                              # Submissão ao VIII Concefor (Produção Técnica, Eixo 1)
│   ├── ARTIGO-FINAL.md                    # TEXTO CANÔNICO: título, autores, resumo, palavras-chave, referências
│   ├── RASCUNHO-SUBMISSAO-CONCEFOR.md     # Operacional: figura, vídeo, anonimização, checklist (aponta p/ ARTIGO-FINAL)
│   ├── FUNDAMENTACAO-CONCEFOR.md          # 7 pilares teóricos/legais (referências alinhadas ao artigo)
│   ├── AVALIACAO-PROTOTIPO.md             # Auditoria de acessibilidade (WCAG) + inspeção heurística
│   └── figura-representativa.html         # Slide-título anonimizado para gerar a imagem (PNG)
│
└── cefor-slides.zip                       # Pacote da skill p/ upload no Claude Web (gerado por scripts/make-zip.py)
```

---

## 3. A skill genérica `cefor-slides`

- **Entrada:** conteúdo entregue pela pessoa (texto, tópicos, imagens).
- **Fluxo:** detectar operação, coletar conteúdo, mostrar 2 prévias (Versão A e B), gerar, entregar,
  exportar sob demanda. Detalhes em [cefor-slides/SKILL.md](cefor-slides/SKILL.md).
- **Saída:**
  - **HTML** (padrão, fonte da verdade): arquivo único, abre em qualquer navegador/projetor, com edição
    de texto inline (tecla E, Ctrl+S).
  - **LibreOffice Impress editável (.odp)** sob demanda, via script Python nativo, alinhado com a 
    política de software livre do governo federal (ver seção 4).
  - **Link** (Vercel) sob demanda.
- **Identidade oficial:** Lima `#B0CB1F`, Azul `#2C459A`, Oliva `#8C9A0D`, degradê CEFOR; fonte **Open
  Sans**; seta CEFOR, logo IFES, rodapé `cefor.ifes.edu.br`; duas linguagens visuais (A e B), 10 modelos
  1920×1080. Fonte da verdade: [cefor-slides/brand/CEFOR-Design-System.dc.html](cefor-slides/brand/CEFOR-Design-System.dc.html).
- **Acessibilidade:** contraste WCAG, navegação por teclado, `prefers-reduced-motion`, nomes acessíveis no
  logo (ver auditoria em `concefor/AVALIACAO-PROTOTIPO.md`).
- **Instalação:** copiar a pasta `cefor-slides/` para `~/.claude/skills/` (Claude Code) ou subir o
  `cefor-slides.zip` no Claude Web (Configurações, Capabilities, Skills, Upload).

---

## 4. Exportação para LibreOffice Impress (.odp) — Alinhamento com Software Livre

A exportação `.odp` é feita por **script Python nativo** (arquivo `cefor-slides/scripts/generate-odp.py`), 
sem dependências proprietárias. Decisão: **software livre como padrão**.

- **Motivo:** LibreOffice é a recomendação oficial do governo federal brasileiro para software de 
  apresentações. ODF (.odp) é formato aberto, sem restrições de licença. Sem dependências proprietárias 
  mantém a skill totalmente livre.
- **Como funciona:** o script `generate-odp.py` lê o HTML da apresentação (Fase 5), extrai conteúdo, 
  cores (`:root` CSS) e tipografia, e reconstrói em formato `.odp` editável pronto para LibreOffice Impress. 
  O HTML permanece como **fonte da verdade**; o `.odp` é uma exportação sob demanda.
- **PowerPoint (.pptx) quando necessário:** para casos concretos de compatibilidade (destinatário só
  usa PowerPoint, modelo exigido por terceiros), `generate-pptx.py` gera um `.pptx` editável usando
  **python-pptx (licença MIT)** — a skill continua 100% software livre; o `.odp` segue sendo o
  formato recomendado.
- **Dependências:** Python + `odfpy` (obrigatória; gera ODF válido por construção) e `pillow` (opcional,
  só para embutir imagens raster locais). O script **valida o `.odp` reabrindo-o** antes de declarar
  sucesso. Sem restrições de distribuição; a skill é 100% aberta.
- **Escopo (consciente):** o `.odp` carrega o **conteúdo editável** (texto, bullets, cores, fonte). Os
  grafismos do layout (SVGs, degradês, molduras, tabelas/KPIs visuais) **não** são transpostos —
  pertencem à fidelidade pixel-perfect do HTML, que permanece a fonte da verdade.

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

- **Título final:** *Skill de inteligência artificial para geração de apresentações institucionais
  padronizadas e acessíveis*.
- **Autores (4, Cefor/Ifes):** Elton Vinicius Silva; Marcos Vinícius Forecchi Accioly; Rutinelli da Penha
  Fávero; Andreia Cristina Carvalho Cáo. (Omitidos na fase de revisão cega.)
- **Modalidade:** Produção Técnica. **Categoria:** Recursos Tecnológicos e Digitais. **Eixo:** 1 (EaD,
  dimensões institucionais e de gestão; uso responsável de IA).
- **Texto canônico:** [concefor/ARTIGO-FINAL.md](concefor/ARTIGO-FINAL.md) (título, autores, resumo,
  palavras-chave, descrição e as 10 referências). Os demais documentos derivam dele.
- **Método:** modelo **ADDIE** (Aldoobie, 2015). **Fundamentação teórica:** IA responsável ancorada na
  **Competência 2 da Matriz de Competências em IA** (SGD, 2026), *human in the loop* (Batista); qualidade
  de slides em Mayer e carga cognitiva (Santos & Tarouco, Missel); acessibilidade em Lei 13.146/2015,
  eMAG e WCAG 2.2.
- **Atenção:** revisão cega exige anonimato; omitir autores/instituição do PDF e anonimizar a marca em
  imagem e vídeo na fase de avaliação. A exportação `.odp` usa apenas software livre (`odfpy`),
  reforçando o enquadramento institucional.
- **Pendências do autor:** inscrever ao menos um dos autores, gravar o vídeo (até 3 min), capturar o PNG
  da figura, colar o ARTIGO-FINAL no template oficial e exportar em PDF, e e-mail à organização
  confirmando eixo, categoria e uso do nome da instituição na fase cega.

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
6. **PDF removido** da skill; exportação passou a ser **PowerPoint editável**, via composição com a skill
   de PPTX (mantida separada por licença).
7. **Migração para software livre:** exportação passa de `.pptx` (skill proprietária) para **LibreOffice
   Impress `.odp`**, via script nativo `generate-odp.py` (odfpy), alinhada à recomendação do governo
   federal. Dependência proprietária removida; geração validada nos exemplos Versão A e B.

---

## 8. Próximos passos

- [x] Testar `scripts/generate-odp.py` com exemplos Versão A e B — automatizado em
      `scripts/smoke-test.py` (17 checks); tabelas ODF reais e KPIs estruturados (2026-07-16).
- [ ] Abrir os `.odp` gerados no LibreOffice Impress real e conferir o render final (olho humano).
- [ ] Obter o **logo IFES em arquivo** (PNG/SVG) oficial (hoje é um SVG reconstruído fiel).
- [x] Concefor: FUNDAMENTACAO-CONCEFOR.md atualizada — Pilar 2 incorpora formatos abertos/software livre (ODF).
- [ ] Concefor: gravar vídeo, capturar figura, preencher template e submeter (ver `concefor/`).
- [ ] Quando for o momento, construir a **skill educacional** (ver `pesquisa-skill-educacional/`).
