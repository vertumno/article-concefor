# Metodologia — fundamento operacional do `cefor-slides`

Fonte canônica das regras pedagógicas da skill. Toda decisão de slide rastreia a uma destas 4 camadas. (Tratamento acadêmico completo: `artigo/02_metodologia.md`.)

## Pilha de 4 camadas

| Nível | Teoria | Autor | Vira regra |
|-------|--------|-------|-----------|
| Porquê | Carga Cognitiva | Sweller | Reduzir carga extrínseca |
| Tela | Aprendizagem Multimídia (CTML) | Mayer | 12 princípios → regras |
| Slide | Assertion-Evidence | Alley | título=afirmação, corpo=evidência |
| Sequência | First Principles | Merrill | arco do deck |

## Regras automatizáveis (o que a skill aplica sozinha)

### Sweller (carga cognitiva) — transversal
- Carga extrínseca é a vilã. Cada slide deve minimizá-la.
- Densidade-alvo: **≤ ~40 palavras visíveis** por slide (exceto tabela/anexo).
- Uma ideia por slide (não acumular).

### Mayer (CTML) — design da tela
- **Coerência:** remover todo elemento decorativo sem função.
- **Sinalização:** destacar o essencial (cor/peso/posição da identidade Cefor).
- **Contiguidade espacial:** rótulo junto do elemento gráfico que descreve.
- **Redundância:** não repetir na tela o texto que será falado (vai nas notas).
- **Segmentação:** quebrar em pedaços; 1 ideia/slide.
- **Multimídia:** palavra + imagem em vez de palavra sozinha.

### Alley (Assertion-Evidence) — estrutura do slide **[regra-mãe]**
- **Título = afirmação** (frase completa que é a tese do slide). NUNCA rótulo-tópico ("Introdução", "Conceitos").
- **Corpo = evidência visual** (imagem, gráfico, diagrama, esquema). NÃO lista de bullets.
- A skill **recusa por padrão** o slide título-genérico + bullets.

### Merrill (First Principles) — sequência do deck (sobretudo Modo 2)
1. **Task-centered** — ancorar numa tarefa/problema real.
2. **Activation** — ativar conhecimento prévio.
3. **Demonstration** — demonstrar (mostrar, não só contar).
4. **Application** — o aluno aplica.
5. **Integration** — integrar ao contexto do aluno.

## Dois modos de operação

| Modo | Entrada | Camadas plenas | O que faz |
|------|---------|----------------|-----------|
| **1 — Produção** ("slide normal") | Conteúdo já pronto | Sweller + Mayer + Alley | Reestrutura em slides assertion-evidence de baixa carga, no design Cefor |
| **2 — Design pedagógico** ("a partir de conceitos") | Tema/objetivos/conceitos | As 4 camadas | Projeta o arco (Merrill) e gera os slides |

## Objetivos de aprendizagem (apoio, Bloom revisada)
Verbos por nível: lembrar, entender, aplicar, analisar, avaliar, criar. Todo objetivo começa com verbo de ação e descreve resultado observável.

## Recursos operacionais (regras → ferramentas)
As regras acima são operacionalizadas por (aproveitados/adaptados da skill `slide-creator`):
- `stages/03-outline/references/slide-structure-library.md` — estruturas de slide curadas por função (Merrill), todas assertion-evidence.
- `stages/05-qa-delivery/references/anti-patterns.md` — slides que não ensinam + correções (carga cognitiva).
- `skills/qa/validate_outline.py` — valida o outline contra assertion-evidence (Alley/Mayer).
- `skills/qa/check_pptx.py` — checa o `.pptx` (placeholders, slides vazios).
- `stages/05-qa-delivery/references/qa-checklist.md` — rubrica ponderada das 4 camadas.
