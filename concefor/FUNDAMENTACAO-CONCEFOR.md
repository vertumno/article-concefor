# Fundamentação teórica e legal — Submissão Concefor (Eixo 1)

> Base de referências para a submissão da `cefor-slides` (genérica) como **Produção Técnica** no VIII
> Concefor, enquadrada no **Eixo 1 — EaD (dimensões institucionais e de gestão + ética/IA responsável)**.
> Cada pilar abaixo sustenta um trecho do resumo/argumento. Fontes priorizadas por confiabilidade
> (oficiais > acadêmicas > ilustrativas). Reconferir links antes do envio.

---

## Pilar 1 — Problema: padrão existente, adoção de IA e a lacuna de integração

A instituição já disponibiliza modelos visuais oficiais (em formato editável, PPTX), mas a sua aplicação
no cotidiano por servidores não especialistas em design ainda é trabalhosa e gera peças inconsistentes,
consumindo tempo. Com a difusão da IA generativa, os servidores passaram a usar a IA para produzir
conteúdo, porém de forma desarticulada do padrão: a saída da IA não incorpora a identidade visual oficial
e a adequação aos modelos permanece manual. Há, portanto, uma lacuna entre a adoção da IA e a sua
integração ao padrão institucional, que a skill busca preencher. Sistemas de design e padronização visual
respondem a esse tipo de problema com consistência, eficiência e escala, inclusive no setor público, onde
a consistência reforça legitimidade e reduz retrabalho.

- U.S. Web Design System (USWDS): https://designsystem.digital.gov/
- GOV.UK Design System / Government Design Principles: https://www.gov.uk/guidance/government-design-principles
- (ilustrativo, custo de inconsistência) https://webflow.com/blog/brand-inconsistency-costs ·
  https://www.slidegenius.com/uncategorized/the-hidden-cost-of-bad-presentations-inside-large-organizations

## Pilar 2 — Solução: sistema de design, design tokens e identidade visual institucional

A skill formaliza a identidade oficial em **tokens de design** (cores, tipografia, elementos de marca),
garantindo consistência em escala e governança de marca. Identidade visual institucional padronizada é
prática consolidada no governo digital brasileiro.

Além disso, a skill entrega exclusivamente **formatos abertos**: HTML autossuficiente (fonte da verdade)
e exportação para **LibreOffice Impress (.odp)**, gerada por script próprio sem dependência de software
proprietário. O ODF (OpenDocument Format) é padrão aberto OASIS e norma **ISO/IEC 26300**, e o uso de
formatos abertos e software livre alinha-se aos princípios de interoperabilidade do governo eletrônico
brasileiro. Isso reforça o enquadramento no Eixo 1 (dimensões institucionais e de gestão): reduz
dependência de fornecedor (*vendor lock-in*), favorece preservação digital e amplia o acesso equitativo.

- Design Tokens Community Group (W3C): https://www.designtokens.org/ · https://www.w3.org/community/design-tokens/
- Identidade Padrão de Comunicação Digital do Governo Federal: https://identidade-digital-de-governo-plone.readthedocs.io/en/latest/
- Secom (Governo Federal): https://www.gov.br/secom/
- OpenDocument Format (OASIS) / ISO/IEC 26300: https://www.oasis-open.org/standards/#opendocumentv1.2
- e-PING — Padrões de Interoperabilidade de Governo Eletrônico (formatos abertos): https://www.gov.br/governodigital/pt-br/ ·
  **[autor: confirmar o instrumento vigente que recomenda ODF/software livre — e-PING ou portaria atual — antes do envio]**

## Pilar 3 — Qualidade dos slides baseada em evidência

Independentemente do uso, a skill aplica princípios de design de slides validados: Teoria Cognitiva da
Aprendizagem Multimídia (Mayer), Teoria da Carga Cognitiva (Sweller) e abordagem Assertion-Evidence
(Alley) — título como asserção + evidência visual, menos "parede de bullets".

- Mayer (CTML) — princípios multimídia: https://multimedia.ucsd.edu/best-practices/multimedia-learning.html ·
  https://litfl.com/cognitive-theory-of-multimedia-learning/
- Sweller (Carga Cognitiva): https://en.wikipedia.org/wiki/Cognitive_load
- Alley — Assertion-Evidence (Penn State): https://www.assertion-evidence.com/guide.html ·
  http://www.writing.engr.psu.edu/speaking/rethinking_psu.pdf

## Pilar 4 — Acessibilidade (obrigatória por lei no setor público)

A skill incorpora acessibilidade por padrão (contraste, alternativas textuais, navegação por teclado,
`prefers-reduced-motion`), alinhada à legislação e aos padrões brasileiros/internacionais. Em
instituição pública federal, isso é **exigência legal**, não diferencial opcional.

- Lei 13.146/2015 (Lei Brasileira de Inclusão): https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2015/lei/l13146.htm
- Decreto 5.296/2004: https://www.planalto.gov.br/ccivil_03/_ato2004-2006/2004/decreto/d5296.htm
- eMAG — Modelo de Acessibilidade em Governo Eletrônico: https://emag.governoeletronico.gov.br/ ·
  https://www.gov.br/governodigital/pt-br/acessibilidade-e-usuario/acessibilidade-digital/modelo-de-acessibilidade
- WCAG 2.2 (tradução PT-BR autorizada — Ceweb.br/NIC.br): https://www.w3c.br/traducoes/wcag/wcag22-pt-BR/

## Pilar 5 — Inteligência Artificial responsável e com supervisão humana

A skill usa IA generativa como **assistente sob curadoria humana** (human-in-the-loop): toda saída é
revisada e validada por pessoas, com transparência e rastreabilidade do uso. Enquadra-se nas diretrizes
éticas internacionais e no marco brasileiro emergente.

- UNESCO — Recomendação sobre a Ética da IA (2021, PT): https://unesdoc.unesco.org/ark:/48223/pf0000381137_por
- UNESCO — Guidance for generative AI in education and research (2023): https://www.unesco.org/en/articles/guidance-generative-ai-education-and-research
- Cartilha IA Generativa no Serviço Público (SGD/SERPRO, 2025): https://www.gov.br/governodigital/pt-br/infraestrutura-nacional-de-dados/inteligencia-artificial-1/publicacoes/cartilha-ia-generativa
- PL 2338/2023 (marco legal da IA) — Senado: https://www25.senado.leg.br/web/atividade/materias/-/materia/157233
- Human-in-the-loop (referência): https://www.ibm.com/think/topics/human-in-the-loop
- Transparência/integridade no uso de IA (SciELO em Perspectiva): https://blog.scielo.org/blog/2025/05/07/integridade-cientifica-e-agencia-humana-na-pesquisa-ia-gen/
- LGPD (Lei 13.709/2018): https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm

## Pilar 6 — Método: Design Science Research (DSR)

O desenvolvimento segue a DSR: construção e avaliação iterativa de um artefato para resolver um problema
real, com rigor e comunicação dos resultados (Hevner et al., 2004; Dresch, Lacerda & Antunes no Brasil).

- Hevner et al. (2004) — Design Science in Information Systems Research: https://misq.umn.edu/misq/article/28/1/75/261/Design-Science-in-Information-Systems-Research1
- Dresch, Lacerda & Antunes — Design Science Research (livro, PT): https://atenaeditora.com.br/catalogo/ebook/design-science-research-na-criacao-de-artefatos-educacionais

## Pilar 7 — Enquadramento como Produção Técnica (CAPES)

O artefato qualifica-se como Produção Técnica e Tecnológica (categoria mais próxima: software/recurso
tecnológico-digital), desde que documentado (problema, especificação, uso, avaliação) e diferenciado.
No Concefor, a categoria correspondente é **"Recursos Tecnológicos e Digitais"**.

- CAPES — GT de Produção Técnica (2019): https://www.gov.br/capes/pt-br/centrais-de-conteudo/10062019-producao-tecnica-pdf
- CAPES — Diretrizes para qualificação de PTT (2021): https://www.gov.br/capes/pt-br/centrais-de-conteudo/documentos/avaliacao/03___Diretrizes_para_qualificacao_de_PTT.16.07.2021.pdf

---

## Como os pilares entram no resumo (mapa argumentativo)

1. **Problema** (Pilar 1) → 2. **Objetivo** → 3. **Artefato** (Pilar 2: tokens/design system; saída em
   formatos abertos — HTML + ODF/software livre) → 4. **Qualidade** (Pilar 3) + **Acessibilidade**
   (Pilar 4) → 5. **IA responsável** (Pilar 5)
   → 6. **Método DSR** (Pilar 6) → 7. **Avaliação/resultados** (inspeção heurística + auditoria de
   acessibilidade + deck demonstrativo) → 8. **Limitações/trabalhos futuros**.

> Nota de integridade: o resumo só pode **afirmar** avaliação (inspeção heurística, auditoria de
> acessibilidade) **depois** de realizá-las de fato. Ver checklist na submissão.

## Observações sobre as fontes
- Mais fortes (oficiais): Planalto (leis), gov.br (eMAG, Cartilha IA, identidade digital), W3C/Ceweb.br
  (WCAG, design tokens), UNESCO, CAPES, Senado (PL 2338), MIS Quarterly (Hevner).
- Acadêmicas: SciELO em Perspectiva; Dresch et al.
- Ilustrativas (usar com parcimônia, não como prova): blogs de mercado sobre custo de inconsistência.
