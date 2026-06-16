# Metodologia do `cefor-slides` (definida)

> Fundamentação teórica da produção técnica. **Decisão fechada** (validada). Quatro teorias consolidadas e citáveis, empilhadas por nível — do "porquê" cognitivo até a estrutura concreta de cada slide. Cada camada vira **regra automatizável** na skill: é aí que a contribuição técnica fica visível.

## A pilha de 4 camadas

| Nível | Teoria | Autor | Pergunta que responde | Vira na skill |
|-------|--------|-------|------------------------|---------------|
| Fundamento (porquê) | **Teoria da Carga Cognitiva** | Sweller | Por que reduzir ruído? | Justificativa de toda regra |
| Design da tela | **Aprendizagem Multimídia (CTML)** | Mayer | Como projetar cada tela? | 12 princípios → regras |
| Estrutura do slide | **Assertion-Evidence** | Alley | Qual o molde de cada slide? | Título=afirmação, corpo=evidência |
| Sequência da instrução | **First Principles of Instruction** | Merrill | Como organizar o conjunto? | Arco do deck (modo 2) |

> Linha argumentativa do artigo: **Sweller** explica *por que* slides ruins atrapalham (carga extrínseca); **Mayer** dá as *regras* para evitá-la; **Alley** dá o *molde* de cada slide que materializa essas regras; **Merrill** organiza a *sequência* que leva à aprendizagem. Cada nível ancora o seguinte.

---

## 1. Sweller — Teoria da Carga Cognitiva (o alicerce)

A memória de trabalho é severamente limitada (poucos elementos por vez); a memória de longo prazo é praticamente ilimitada, organizada em **esquemas**. A carga se divide em três:

- **Intrínseca** — dificuldade inerente do conteúdo.
- **Extrínseca** — imposta por design ruim. **A vilã.**
- **Germânica** — esforço bom, que constrói esquema e gera aprendizagem.

Objetivo do design instrucional: **reduzir a carga extrínseca** para liberar memória de trabalho para a germânica.

**Argumento central de valor da produção técnica:** geradores genéricos de slides com IA — e os slides humanos ruins — impõem carga extrínseca pesada (texto demais, ruído decorativo, redundância). O `cefor-slides` é posicionado como ferramenta que **reduz carga extrínseca de forma sistemática**. Quando a skill proíbe a "parede de texto", a razão não é estética — é carga cognitiva. Sweller é o argumento de autoridade de cada regra.

## 2. Mayer — Aprendizagem Multimídia (as regras do slide)

Três pressupostos: **canais duplos** (verbal e visual processados em separado), **capacidade limitada** (cada canal satura), **processamento ativo** (aprender é selecionar, organizar, integrar). Dos 12 princípios, os automatizáveis e seu mapeamento para **comportamento de máquina**:

| Princípio | Vira na skill (regra automatizável) |
|-----------|-------------------------------------|
| **Coerência** | Remove elementos decorativos sem função |
| **Sinalização** | Destaca o essencial (cor/peso/posição da identidade Cefor) |
| **Contiguidade espacial** | Posiciona o rótulo junto ao elemento gráfico que descreve |
| **Redundância** | Não repete na tela o texto que será falado (notas ≠ slide) |
| **Segmentação** | Quebra o conteúdo em pedaços (1 ideia por slide) |
| **Multimídia** | Palavra + imagem em vez de palavra sozinha |

É o coração da camada pedagógica: cada princípio é uma regra que o sistema aplica sozinho. **A tradução teoria → regra é a contribuição técnica demonstrável.**

## 3. Alley — Assertion-Evidence (a estrutura de cada slide)

Rejeita o padrão título-tópico + bullets. No lugar:

- **Título = uma afirmação** (frase completa: a tese única daquele slide).
- **Corpo = evidência visual** que sustenta a afirmação (imagem, gráfico, diagrama) — **não** lista de tópicos.

Por que importa: é o único framework sobre a **estrutura interna** do slide e é diretamente codificável (`título = afirmação`, `corpo = evidência`). Tem estudos mostrando ganho de **compreensão e retenção** frente ao modelo de bullets. É **pouco usado no Brasil** → ineditismo. Complementa Mayer: Mayer dá os princípios cognitivos; Alley dá o molde concreto.

**Regra demonstrável do artefato:** todo slide gerado **nasce** com título-afirmação e corpo-evidência. A skill recusa o slide de bullets por padrão.

## 4. Merrill — First Principles of Instruction (a sequência)

Cinco princípios centrados em tarefa, que organizam o **conjunto** de slides (sobretudo no modo 2 — "a partir de conceitos"):

1. **Task-centered** — ancorar em uma tarefa/problema real.
2. **Activation** — ativar conhecimento prévio.
3. **Demonstration** — demonstrar (mostrar, não só contar).
4. **Application** — aplicar (o aluno faz).
5. **Integration** — integrar ao mundo do aluno.

Vira o **arco do deck**: a sequência de slides percorre ativação → demonstração → aplicação → integração rumo ao objetivo. É o substituto pedagógico do "story arc" persuasivo.

---

## Como a inteligência da `slide-creator` é reaproveitada (persuasão → aprendizagem)

A skill `slide-creator` é narrative-first, mas voltada a **persuasão/conversão**. Reorientamos cada mecanismo para a chave pedagógica, agora com âncora teórica nominal:

| Mecanismo da `slide-creator` | Versão pedagógica no `cefor-slides` | Âncora |
|------------------------------|-------------------------------------|--------|
| Belief shift | **Objetivo de aprendizagem** | Merrill (task) |
| Story arc (reframe→prova→CTA) | **Arco instrucional** (ativação→demonstração→aplicação→integração) | Merrill |
| Slide-function map | **Função pedagógica** de cada slide | Merrill + Alley |
| Action title (título faz uma alegação) | **Título-afirmação** (assertion) | Alley |
| Corpo do slide | **Evidência visual** (não bullets) | Alley + Mayer (multimídia) |
| Design direction | **Princípios multimídia + design system Cefor** | Mayer |
| Density / layout gates | **Gestão de carga cognitiva** | Sweller / Mayer (coerência, segmentação) |
| QA rubric | **Rubrica de qualidade pedagógica** | as 4 camadas |

Mantém-se a disciplina (não renderizar direto do outline; gates; speaker notes); troca-se o *telos* de vender para ensinar.

### Ativos concretos aproveitados (não só princípios)

Além da filosofia, foram **portados e adaptados** ativos da `slide-creator` para o `cefor-slides`:

| Ativo da `slide-creator` | Como foi adaptado | Onde ficou |
|--------------------------|-------------------|------------|
| `slide-structure-library` (240+ estruturas) | Curada para ensino, organizada por função de Merrill, toda assertion-evidence; IDs de origem preservados (proveniência) | `stages/03-outline/references/slide-structure-library.md` |
| `anti-patterns.md` | Reorientado p/ aprendizagem; razão de fundo = carga cognitiva (Sweller) | `stages/05-qa-delivery/references/anti-patterns.md` |
| `validate_deck_package.py` | Virou validador de outline assertion-evidence (Pattern, Assertion, Evidence, variedade) | `skills/qa/validate_outline.py` |
| `check_pptx_placeholders.py` | Estendido (placeholders + slides vazios + contagem) | `skills/qa/check_pptx.py` |
| `rubrics.md` (scoring ponderado) | Dimensões trocadas p/ as 4 camadas pedagógicas | `qa-checklist.md` (seção C) |

Isso materializa a contribuição técnica: a teoria não fica no texto — vira biblioteca consultável e **validação automática executável**.

---

## Aplicação aos dois modos

- **Modo 1 (Produção / "slide normal"):** entra Sweller + Mayer + Alley + design system Cefor. A skill reestrutura o conteúdo enviado em slides assertion-evidence de baixa carga extrínseca. Merrill atua de forma leve (ordenação).
- **Modo 2 (Design pedagógico / "a partir de conceitos"):** entram as 4 camadas plenamente. Merrill define o arco; Bloom (opcional) pode tipar o objetivo; Mayer/Alley/Sweller governam cada slide.

---

## Referências (a completar no padrão ABNT do template)

- ALLEY, M. *The Craft of Scientific Presentations.* 2. ed. New York: Springer, 2013. (modelo Assertion-Evidence)
- MAYER, R. E. *Multimedia Learning.* 2. ed. Cambridge: Cambridge University Press, 2009. (3. ed. 2021)
- MERRILL, M. D. First Principles of Instruction. *Educational Technology Research and Development*, v. 50, n. 3, p. 43–59, 2002.
- SWELLER, J. Cognitive Load During Problem Solving. *Cognitive Science*, v. 12, p. 257–285, 1988.
- SWELLER, J.; VAN MERRIËNBOER, J. J. G.; PAAS, F. Cognitive Architecture and Instructional Design: 20 Years Later. *Educational Psychology Review*, v. 31, p. 261–292, 2019.
- VAN CLIEF, J. *Interpretable Context Methodology.* 2026. (arXiv:2603.16021 — confirmar citação)
