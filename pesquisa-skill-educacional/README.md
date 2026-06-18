# Pesquisa — futura Skill de Apresentações Educacionais do Cefor

Esta pasta guarda a pesquisa e o planejamento para uma **skill separada**, dedicada a **apresentações
educacionais** (com fundamentação pedagógica). Foi separada da `cefor-slides`, que passou a ser
**genérica** (sem cunho educacional).

## Conteúdo

- [REFERENCIAIS-PEDAGOGICOS.md](REFERENCIAIS-PEDAGOGICOS.md) — estado da arte: metodologias de aula
  (Camada 1) e princípios de design de aprendizagem (Camada 2), com links.
- [ARQUITETURA-SKILL-EDUCACIONAL.md](ARQUITETURA-SKILL-EDUCACIONAL.md) — arquitetura de duas camadas,
  menu de metodologias proposto, decisões pendentes e fluxo previsto.
- [padroes-pedagogicos-rascunho.md](padroes-pedagogicos-rascunho.md) — catálogo de padrões de slide
  pedagógicos (movido da `cefor-slides`); ponto de partida dos "blocos" que as metodologias arranjam.
- [exemplo-educacional.html](exemplo-educacional.html) — deck educacional de exemplo (Versão B), movido
  da `cefor-slides`.

## Ideia central

No início do uso, o **professor escolhe a metodologia/estrutura pedagógica** (ex.: Exposição eficaz,
BOPPPS, 5E, PBL, Sala invertida, Aprendizagem Significativa…), e cada escolha gera uma **sequência de
slides diferente**. A skill reutiliza a identidade visual oficial da `cefor-slides` (Versões A/B, Open
Sans, seta CEFOR) e sempre aplica os princípios de design de aprendizagem (Mayer, carga cognitiva,
Assertion-Evidence, UDL, acessibilidade WCAG/Lei 13.146).

## Decisões pendentes (antes de implementar)

1. Amplitude do menu de metodologias (4 / 6 / 8).
2. Metodologia padrão (proposto: Exposição eficaz).
3. Adotar Assertion-Evidence como padrão dos slides educacionais (proposto: sim).
4. Camada 2 sempre automática vs. ajustável (proposto: sempre automática).
