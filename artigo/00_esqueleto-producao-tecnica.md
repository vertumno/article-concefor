# [Título da Produção Técnica] — RASCUNHO

> ⚠️ **VERSÃO PARA SUBMISSÃO = SEM AUTORIA.** Remover qualquer nome, instituição ou pista de identidade antes de submeter (blind review — descumprimento cancela a submissão). Ver `referencias/01_concefor-submissao.md`.
>
> ⚠️ Este esqueleto é um andaime de trabalho. A versão final DEVE ser transposta para o **template oficial de Produção Técnica do VIII Concefor** (`referencias/templates/`).

- **Modalidade:** Produção Técnica → Recursos Tecnológicos e Digitais
- **Eixo:** Eixo 2 — Tecnologias Digitais na Educação
- **Produção descrita:** Workspace ICM `cefor-deck` (ver `producao-tecnica/cefor-deck/`)

---

## Resumo
[150–250 palavras. O quê, por que, como, principal resultado/aplicação. Sem identificação.]

**Palavras-chave:** inteligência artificial na educação; design educacional; produção de slides; arquitetura de contexto; formação de educadores.

## 1. Apresentação / Contextualização do problema
- Contexto: produção recorrente de materiais de slides para formação de educadores em EaD.
- Problema: custo/tempo e inconsistência na produção de decks; ferramentas genéricas de IA produzem saída opaca e não reproduzível.
- Lacuna que a produção técnica preenche.

## 2. Objetivo da produção técnica
- Objetivo geral + objetivos específicos. O que a produção entrega e para quem.

## 3. Fundamentação (curta, suficiente para produção técnica)
- IA generativa na produção de materiais educacionais.
- **Diferencial metodológico — ICM (Interpretable Context Methodology):** arquitetura de contexto em camadas, "glass-box", cada saída é superfície editável por humano; herança de separação de responsabilidades / pipe-and-filter. *(Citar a fonte do ICM em referências.)*
- Por que isso importa em educação: transparência, autoria humana preservada, reprodutibilidade.

## 4. Descrição técnica da produção
- Arquitetura: 5 estágios (extração → currículo → outline → geração → QA/entrega).
- Camadas de contexto (Layer 0–4) e como cada estágio carrega só o necessário.
- Design-system institucional (paleta/tipografia) como "fábrica" reaproveitada.
- Skill `pptx` (html2pptx) para gerar `.pptx` final.
- Superfícies de edição humana entre estágios (human-in-the-loop).

## 5. Procedimentos / fluxo de uso (passo a passo reproduzível)
1. `setup` (configura identidade + design-system uma vez).
2. Fornecer material-fonte + tópico.
3. Percorrer estágios 01→05, revisando cada saída.
4. Entrega: deck `.pptx`.

## 6. Resultados e aplicabilidade
- O que foi produzido (ex.: deck(s) de exemplo gerados).
- Ganho de tempo / consistência / transparência.
- Onde se aplica na formação de educadores em EaD.

## 7. Considerações finais
- Limitações (ver "Where this does not work" do ICM: tempo real, alta concorrência, ramificação automática).
- Próximos passos.

## Referências
- Van Clief, J. (2026). *Model Workspace Protocol / Interpretable Context Methodology*. [completar citação — arXiv:2603.16021]
- [demais referências sobre IA na educação, design educacional]
