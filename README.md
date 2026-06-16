# Trabalho VIII Concefor — Produção Técnica

Repositório de produção do trabalho submetido ao **VIII Concefor** (Congresso Regional de Formação e Educação a Distância, 17–20/08/2026).

- **Modalidade:** Produção Técnica → *Recursos Tecnológicos e Digitais*
- **Eixo:** Eixo 2 — Tecnologias Digitais na Educação
- **Produção:** `cefor-slides` — um workspace de IA (metodologia ICM) que transforma material bruto em decks de slides para a formação de educadores.

## ⚠️ Prazos (hoje = 2026-06-15)

| Etapa | Data |
|-------|------|
| **Submissão (aberta)** | fecha **19/06/2026** — 4 dias |
| Notificação de aceite | 06/07/2026 |
| Envio final | 17/07/2026 |

Regra crítica: **a primeira submissão vai SEM identificação de autoria** (blind review; descumprimento = cancelamento). Detalhes em [`referencias/01_concefor-submissao.md`](referencias/01_concefor-submissao.md).

## As três zonas

```
article-concefor/
├── producao-tecnica/        # O ARTEFATO entregue (o que se submete como produção técnica)
│   └── cefor-slides/          # Workspace ICM: material → slides do Cefor (5 estágios)
├── artigo/                  # O TEXTO que descreve a produção (vai no template oficial)
│   └── 00_esqueleto-producao-tecnica.md
└── referencias/             # Regras do congresso, eixos, datas, templates oficiais
    ├── 01_concefor-submissao.md
    └── templates/           # ← baixar aqui os templates oficiais do site
```

| Zona | É o quê | Quando mexer |
|------|---------|--------------|
| `producao-tecnica/cefor-slides/` | A produção técnica em si (o recurso digital) | Construir/configurar o workspace |
| `artigo/` | Documento descritivo para os Anais | Escrever e revisar o texto |
| `referencias/` | Fontes oficiais e regras | Consulta; não adaptar ao trabalho |

## A produção: `cefor-slides`

Especialização do workspace `course-deck-production` (ICM) para o contexto Cefor. A metodologia **ICM (Interpretable Context Methodology)** — "estrutura de pastas como arquitetura de agente" — é o diferencial arquitetural: pipeline glass-box, observável, com superfície de edição humana entre cada estágio.

Fundamentação pedagógica (4 camadas, citáveis): **Sweller** (carga cognitiva) → **Mayer** (multimídia) → **Alley** (assertion-evidence) → **Merrill** (sequência). Cada camada vira regra automatizável — incluindo biblioteca de estruturas curada e **validadores executáveis** (`skills/qa/`). Inteligência reaproveitada da skill `slide-creator`, reorientada de persuasão para aprendizagem. Ver [`artigo/02_metodologia.md`](artigo/02_metodologia.md).

Para usar/configurar: abrir o Claude Code em `producao-tecnica/cefor-slides/` e digitar `setup`. Ver [`producao-tecnica/cefor-slides/CLAUDE.md`](producao-tecnica/cefor-slides/CLAUDE.md).

## Próximos passos

1. Baixar templates oficiais (Produção Técnica + apresentação) → `referencias/templates/`.
2. Especializar `cefor-slides` para o Cefor (design-system institucional, sem dados identificáveis).
3. Gerar ao menos um deck de exemplo (evidência de resultado para o artigo).
4. Escrever o artigo a partir do esqueleto, transpor para o template oficial **sem autoria**.
5. Submeter até 19/06.
