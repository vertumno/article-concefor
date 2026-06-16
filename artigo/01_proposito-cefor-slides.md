# Propósito do `cefor-slides` (objetivo pedagógico)

> Documento de fechamento de escopo. Define **para que serve** a produção técnica antes de definir método e código. Insumo para validar com a Rutinelli junto com `02_metodologia.md`.

## Contexto

O **Cefor** (Centro de Referência em Formação e em Educação a Distância) oferta vários cursos, com muitos professores produzindo material. Slides são o artefato mais recorrente — e o mais frequentemente mal resolvido: viram "depósito de texto", variam em qualidade pedagógica e fogem da identidade visual institucional. Produzi-los consome tempo docente que poderia ir para a mediação.

## Problema

1. **Carga de produção** sobre o professor (tempo, design, padronização).
2. **Qualidade pedagógica desigual** — slides que informam mas não ensinam (excesso de texto, ausência de sequência instrucional, sem objetivos claros).
3. **Inconsistência de identidade** — cada deck com cara diferente, sem o padrão Cefor.

## Objetivo pedagógico (a tese da produção)

> Um slide do Cefor não é um recipiente de conteúdo — é um **artefato instrucional**: reduz carga cognitiva, sinaliza o que importa, segmenta a informação e segue uma **sequência de ensino intencional** rumo a um objetivo de aprendizagem.

O `cefor-slides` automatiza a produção **sem terceirizar a decisão pedagógica**: o professor permanece autor (human-in-the-loop, herança glass-box do ICM); a IA aplica princípios de design instrucional consolidados e a identidade do Cefor.

## Os dois modos (confirmados)

| Modo | Entrada do professor | O que a skill faz | Valor |
|------|----------------------|-------------------|-------|
| **1 — Produção** ("slide normal") | Conteúdo já pronto (texto, tópicos, doc) | Estrutura segundo princípios de design multimídia + aplica **design system Cefor** | Baixo esforço; ganho de consistência visual e clareza cognitiva |
| **2 — Design pedagógico** ("a partir de conceitos") | Tema, objetivos e/ou conceitos pedagógicos | Projeta a **sequência instrucional** (objetivo → ativação → demonstração → prática → avaliação) e gera os slides | Alto valor pedagógico; o slide nasce de uma intenção de ensino |

Ambos terminam no mesmo padrão: deck `.pptx` no **design system Cefor**, com **notas do apresentador** e rastreabilidade de decisões.

## Público e medida

- **Quem:** professores/formadores do Cefor (vários cursos, EaD e presencial).
- **O que queremos que façam:** produzir slides melhores, mais rápido, mantendo autoria pedagógica.
- **Como medir (para o artigo):** tempo de produção; aderência ao design system; checklist de qualidade pedagógica (rubrica derivada da metodologia escolhida); aplicabilidade percebida.

## Diferencial (o que blinda contra "e daí?")

1. **Fundamentação pedagógica explícita e citável** (ver `02_metodologia.md`) — não é "IA faz slide bonito".
2. **Arquitetura glass-box (ICM)** — pipeline observável, editável a cada estágio, reprodutível, portável.
3. **Identidade institucional** — design system Cefor como "fábrica" reaproveitada.
4. **Reorientação da inteligência da `slide-creator`** — de persuasão (pitch/sales) para **aprendizagem** (ver mapeamento em `02_metodologia.md`).
