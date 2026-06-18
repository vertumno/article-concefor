# Arquitetura proposta — futura Skill de Apresentações Educacionais

> Material de planejamento salvo para uma **futura skill** separada da `cefor-slides` (que agora é
> genérica). Base teórica completa em [REFERENCIAIS-PEDAGOGICOS.md](REFERENCIAIS-PEDAGOGICOS.md).

## Ideia central

No início do uso, **o professor escolhe a metodologia/estrutura pedagógica** da aula. Cada escolha gera
uma **sequência de slides diferente**. A skill herda a identidade visual oficial do Cefor (Versões A/B,
Open Sans, seta CEFOR etc.) reutilizando os artefatos de marca da `cefor-slides`.

## Duas camadas

**Camada 1 — Metodologia da aula (ESCOLHÍVEL).** Define a *sequência* dos slides. O professor escolhe UMA.

**Camada 2 — Princípios de design de aprendizagem (SEMPRE aplicados).** Definem a *qualidade* de cada
slide, independentemente da escolha: Mayer (multimídia), Sweller (carga cognitiva), Paivio (dupla
codificação), Alley (Assertion-Evidence), UDL/CAST, acessibilidade WCAG/Lei 13.146, e verbos de Bloom
nos objetivos.

> O professor escolhe *como a aula flui*; a skill sempre garante *slides baseados em evidência e acessíveis*.

## Menu proposto (Camada 1) — curadoria a confirmar

Sugestão de menu curado (6), com possibilidade de ampliar para 8:

1. **Exposição eficaz** (Gagné 9 Eventos + Rosenshine) — uso geral; **DEFAULT proposto**.
2. **BOPPPS** — aula participativa/síncrona.
3. **5E** — investigativa (ciências/STEM; alinha BNCC).
4. **Aprendizagem Baseada em Problemas (PBL)** (+ Merrill) — formação profissional/IF.
5. **Sala de Aula Invertida (Flipped)** — EaD/híbrido.
6. **Aprendizagem Significativa (Ausubel)** — conhecimento prévio + mapas conceituais.
   *(Ampliação: 7. Ciclo de Kolb — experiencial; 8. Problematizadora — Freire.)*
- Sempre disponível: **"Estrutura livre/simples"** (sem framework, para rapidez).

Apoios: **Backward Design** (lógica de planejamento) + **Bloom** (objetivos) + **BNCC** (alinhamento
opcional) + **TPACK** (uso intencional de tecnologia).

## Decisões pendentes (a definir antes de implementar a skill educacional)

1. **Amplitude do menu** (4 essencial / 6 ampliado / 8 completo).
2. **Metodologia padrão** (proposto: Exposição eficaz).
3. **Assertion-Evidence** como padrão dos slides educacionais (proposto: sim).
4. **Camada 2** sempre automática vs. ajustável (proposto: sempre automática).

## Fluxo previsto da skill educacional

- Fase 1: tema, público/turma, **objetivos de aprendizagem** (com verbos de Bloom; alinhamento BNCC
  opcional), densidade.
- Fase 1b: **escolha da metodologia** (menu acima, com descrição + "quando usar" + recomendação).
- Fase 2: estilo (Versão A/B — reutiliza a marca Cefor).
- Fase 3: geração da **sequência conforme a metodologia**, aplicando a Camada 2 a todo slide.
- Fases 4–6: entrega/edição/export (iguais à `cefor-slides`).

## Reaproveitamento da `cefor-slides`

A skill educacional deve reutilizar: `viewport-base.css`, `CEFOR_BRAND.md`, `STYLE_PRESETS.md` (Versões
A/B), `html-template.md`, `brand/` e `scripts/`. O que é exclusivo da educacional: o menu de metodologias
(Camada 1), os princípios de aprendizagem (Camada 2) e os padrões pedagógicos de slide.

## Sementes já existentes

- `padroes-pedagogicos-rascunho.md` (nesta pasta) — catálogo de padrões de slide pedagógicos, movido da
  `cefor-slides`. Serve de ponto de partida para os "blocos" que as metodologias arranjam.
- `exemplo-educacional.html` (se movido para cá) — exemplo de deck educacional na Versão B.
