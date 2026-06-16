# Cefor Slides

Produção de **slides instrucionais** para o Cefor (Centro de Referência em Formação e em Educação a Distância). Não gera "slides bonitos" — gera artefatos que ensinam, fundamentados em pedagogia consolidada e na identidade visual do Cefor. Rode `setup` uma vez; depois produza por curso/aula.

## Princípio central

Um slide é um artefato instrucional, não um recipiente de texto. Toda regra rastreia a 4 camadas teóricas (`shared/methodology.md`):

- **Sweller** (carga cognitiva) — reduzir carga extrínseca.
- **Mayer** (CTML) — 12 princípios multimídia → regras.
- **Alley** (Assertion-Evidence) — título = afirmação, corpo = evidência (não bullets).
- **Merrill** (First Principles) — arco instrucional do deck.

## Dois modos

| Modo | Entrada do professor | O que a skill faz |
|------|----------------------|-------------------|
| **1 — Produção** | Conteúdo já pronto | Reestrutura em slides assertion-evidence de baixa carga + design Cefor |
| **2 — Design pedagógico** | Tema / objetivos / conceitos | Projeta o arco (Merrill) e gera os slides |

Modo 1 pode entrar direto no Stage 03 (outline). Modo 2 percorre 02→05 (o currículo desenha a sequência).

## Folder Map

```
cefor-slides/
├── CLAUDE.md              (você está aqui)
├── CONTEXT.md             (roteamento de tarefas)
├── setup/questionnaire.md (onboarding — identidade e variante visual)
├── shared/
│   ├── methodology.md     (FONTE das regras pedagógicas — 4 camadas)
│   ├── producer-identity.md
│   └── course-meta.md
├── design-system/         (paleta e tipografia Cefor: Sólida | Degradê)
├── skills/                (pptx + frontend-design + qa: validadores automáticos)
└── stages/
    ├── 01-extraction/     (material bruto → conteúdo estruturado)
    ├── 02-curriculum/     (conteúdo → arco instrucional Merrill)
    ├── 03-outline/        (arco → slides assertion-evidence)
    ├── 04-generation/     (outline → .pptx no design Cefor)
    └── 05-qa-delivery/    (QA pedagógico + visual, entrega)
```

## Triggers

| Keyword | Ação |
|---------|------|
| `setup` | Onboarding único — identidade, variante visual (Sólida/Degradê), modo padrão |
| `status` | Mostra conclusão dos 5 estágios (scan de `stages/*/output/`) |
| `modo 1` / `produção` | Conteúdo pronto → entra no Stage 03 |
| `modo 2` / `pedagógico` | Conceitos → entra no Stage 02 |

## Routing

| Tarefa | Vá para |
|--------|---------|
| Extrair conteúdo do material-fonte | `stages/01-extraction/CONTEXT.md` |
| Desenhar o arco instrucional (Merrill) | `stages/02-curriculum/CONTEXT.md` |
| Criar slides assertion-evidence | `stages/03-outline/CONTEXT.md` |
| Gerar o .pptx no design Cefor | `stages/04-generation/CONTEXT.md` |
| QA pedagógico + visual e entrega | `stages/05-qa-delivery/CONTEXT.md` |

## What to Load

| Tarefa | Carregar | NÃO carregar |
|--------|----------|--------------|
| Extrair | `stages/01-extraction/references/*`, `shared/methodology.md`, `shared/producer-identity.md`, `shared/course-meta.md` | `design-system/`, `skills/pptx/`, stages 03–05 |
| Currículo / arco | `stages/01-extraction/output/`, `stages/02-curriculum/references/*`, `shared/methodology.md` | `design-system/`, `skills/pptx/`, stages 03–05 |
| Outline (slides) | `stages/03-outline/references/*` (slide-patterns + slide-structure-library), `stages/02-curriculum/output/`, `shared/methodology.md`, `design-system/*` | `skills/pptx/`, stages 01, 04, 05 |
| Gerar .pptx | `stages/03-outline/output/`, `stages/04-generation/references/*`, `design-system/*`, `skills/pptx/SKILL.md` | stages 01, 02 |
| QA e entrega | `stages/04-generation/output/`, `stages/05-qa-delivery/references/*` (qa-checklist + anti-patterns), `skills/qa/*`, `shared/methodology.md`, `design-system/*` | stages 01, 02, 03 |

## Validadores automáticos (`skills/qa/`)

- `validate_outline.py` — checa o outline (Stage 03) contra Assertion-Evidence.
- `check_pptx.py` — checa o `.pptx` (placeholders, slides vazios, contagem).
Rode-os no Stage 05 (ou no 03) antes de declarar um deck pronto. Detalhes: `skills/qa/README.md`.

## Stage Handoffs

Cada estágio escreve em seu `output/`; o próximo lê de lá. Edite qualquer saída entre estágios e o próximo assume sua edição (glass-box, human-in-the-loop). Para começar do zero, limpe os `output/`.
