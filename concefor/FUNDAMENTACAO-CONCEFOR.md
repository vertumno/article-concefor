# Fundamentação teórica e legal — Submissão Concefor (Eixo 1)

> Base de referências para a submissão da `cefor-slides` (genérica) como **Produção Técnica** no VIII
> Concefor, enquadrada no **Eixo 1 — EaD (dimensões institucionais e de gestão + ética/IA responsável)**.
> Cada pilar abaixo sustenta um trecho do resumo/argumento. Fontes priorizadas por confiabilidade
> (oficiais > acadêmicas > ilustrativas). Reconferir links antes do envio.
>
> **Alinhamento (2026-06-19):** este documento foi reconciliado com o artigo final
> ([ARTIGO-FINAL.md](ARTIGO-FINAL.md)), que é a fonte da verdade. O conjunto de **10 referências citadas
> no resumo** (Aldoobie; Batista; Brasil 2015/2020/2026a/2026b; Machado/Missel; Mayer; Santos & Tarouco;
> WCAG/W3C) é o canônico. As demais fontes abaixo são **apoio** (não citadas no resumo): embasam pilares
> de problema/solução, mas não entram na lista de referências do artigo.

---

## Pilar 1 — Problema: padrão existente, adoção de IA e a lacuna de integração

A instituição já disponibiliza modelos visuais oficiais (em formato editável, PPTX), mas a sua aplicação
no cotidiano por servidores não especialistas em design ainda é trabalhosa e gera peças inconsistentes,
consumindo tempo. Com a difusão da IA generativa, os servidores passaram a usar a IA para produzir
conteúdo, porém de forma desarticulada do padrão: a saída da IA não incorpora a identidade visual oficial
e a adequação aos modelos permanece manual. Há, portanto, uma lacuna entre a adoção da IA e a sua
integração ao padrão institucional, que a skill busca preencher. Sistemas de design e padronização visual
respondem a esse tipo de problema com consistência, eficiência e escala, inclusive no setor público, onde
a consistência reforça legitimidade e reduz retrabalho. Esse contexto encontra respaldo normativo na
**Competência 2 da Matriz de Competências em IA** (SGD, Brasil 2026b), que orienta o agente público a
aplicar IA generativa, de forma assistida e sob supervisão, para criar e refinar documentos padronizados
(detalhada no Pilar 5).

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

Independentemente do uso, a skill aplica princípios de design de slides baseados em evidência, apoiados
em aspectos da **Teoria Cognitiva da Aprendizagem Multimídia** (Mayer) e da **Teoria da Carga Cognitiva**:
layout limpo, sinalização do tópico (barra de título), uma ideia por slide e redução da carga extrínseca,
em vez de "parede de bullets".

**Referências canônicas (citadas no resumo):**
- SANTOS; TAROUCO (2007) — Teoria da Carga Cognitiva em educação tecnológica: https://seer.ufrgs.br/index.php/renote/article/view/14145
- MACHADO/MISSEL et al. (2023) — Recursos multimídia sob a TCAM de Mayer: https://seer.faccat.br/index.php/redin/article/view/2855
- MAYER (2009) — Teoria Cognitiva da Aprendizagem Multimédia (in Miranda, org.): http://webhosting.bombyte.org/~joao.gama/guilhermina/m3/Mod3G2/Mayer_TCAMultimedia.pdf

## Pilar 4 — Acessibilidade (obrigatória por lei no setor público)

A skill incorpora acessibilidade por padrão (contraste, alternativas textuais, navegação por teclado,
`prefers-reduced-motion`), alinhada à legislação e aos padrões brasileiros/internacionais. Em
instituição pública federal, isso é **exigência legal**, não diferencial opcional.

**Referências canônicas (citadas no resumo):**
- BRASIL (2015) — Lei nº 13.146/2015 (Lei Brasileira de Inclusão): http://www.planalto.gov.br/ccivil_03/_ato2015-2018/2015/lei/l13146.htm
- BRASIL (2020) — eMAG, Modelo de Acessibilidade em Governo Eletrônico (MGI/SGD): https://www.gov.br/governodigital/pt-br/acessibilidade-e-usuario/acessibilidade-digital/modelo-de-acessibilidade
- WORLD WIDE WEB CONSORTIUM (2025) — WCAG 2.2, tradução PT-BR autorizada (Ceweb.br): https://www.w3.org/Translations/WCAG22-pt-BR/

**Apoio (não citada no resumo):**
- Decreto 5.296/2004: https://www.planalto.gov.br/ccivil_03/_ato2004-2006/2004/decreto/d5296.htm

## Pilar 5 — Inteligência Artificial responsável e com supervisão humana

A skill usa IA generativa como **assistente sob curadoria humana** (*human in the loop*): toda saída é
revisada, testada e validada por pessoas, com transparência e rastreabilidade do uso. Ferramentas
nomeadas no artigo: **Claude Code** e **Claude Design**, empregadas na concepção, na geração de modelos e
código e em rascunhos textuais, sempre sob decisão humana. A verificação humana ocorre nas entregas ao
final de cada etapa de produção. Enquadra-se nas orientações brasileiras para uso de IA no serviço
público e na educação.

Argumento central de gestão pública: a **Competência 2 da Matriz de Competências em IA** (SGD, Brasil
2026b) estabelece que o agente público deve aplicar, de forma assistida e sob supervisão, soluções de IA
generativa para criar e refinar documentos e relatórios padronizados, mantendo o julgamento crítico e a
responsabilidade humana pela validação final, para melhorar produtividade e qualidade dos serviços. A
skill operacionaliza diretamente essa competência.

**Referências canônicas (citadas no resumo):**
- BRASIL (2026b) — Matriz de Competências em Inteligência Artificial (MGI/SGD): https://www.gov.br/governodigital/pt-br/infraestrutura-nacional-de-dados/inteligencia-artificial-1/matrizdeIA
- BRASIL (2026a) — Inteligência Artificial na Educação Básica: diretrizes (MEC): https://www.gov.br/mec/pt-br/escolas-conectadas/arquivos/ia-educacao-basica.pdf
- BATISTA et al. (2025) — Human-in-the-loop (HITL): participação humana em sistemas de IA (REGRASP/IFSP): https://regrasp.spo.ifsp.edu.br/index.php/regrasp/article/view/1307

## Pilar 6 — Método: modelo ADDIE (design instrucional)

O desenvolvimento do artefato foi guiado por aspectos do modelo **ADDIE** (*Analysis, Design, Development,
Implementation, Evaluation*) — Aldoobie (2015). A aplicação estruturou-se em ciclos contínuos de projeto
e avaliação, em três momentos: (1) **design e especificação** — formalização da identidade em design
tokens e duas linguagens visuais; (2) **fluxo de experiência do usuário** — entrega do conteúdo, escolha
de estilo por pré-visualização e geração automatizada; (3) **desenvolvimento e entrega técnica** — HTML
autossuficiente em proporção fixa de tela, edição no navegador e exportação para LibreOffice Impress. A
avaliação (inspeção heurística + auditoria de acessibilidade) realimenta o refinamento do artefato.

**Referência canônica (citada no resumo):**
- ALDOOBIE, N. (2015) — ADDIE model. *American International Journal of Contemporary Research*, v. 5, n. 6: https://aijcr.thebrpi.org/journals/Vol_5_No_6_December_2015/10.pdf

## Pilar 7 — Enquadramento como Produção Técnica (CAPES)

O artefato qualifica-se como Produção Técnica e Tecnológica (categoria mais próxima: software/recurso
tecnológico-digital), desde que documentado (problema, especificação, uso, avaliação) e diferenciado.
No Concefor, a categoria correspondente é **"Recursos Tecnológicos e Digitais"**.

- CAPES — GT de Produção Técnica (2019): https://www.gov.br/capes/pt-br/centrais-de-conteudo/10062019-producao-tecnica-pdf
- CAPES — Diretrizes para qualificação de PTT (2021): https://www.gov.br/capes/pt-br/centrais-de-conteudo/documentos/avaliacao/03___Diretrizes_para_qualificacao_de_PTT.16.07.2021.pdf

---

## Como os pilares entram no resumo (mapa argumentativo)

1. **Problema** (Pilar 1) + **mandato de gestão pública** (Competência 2 da Matriz de Competências em IA,
   Pilar 5) → 2. **Objetivo** → 3. **Artefato** (Pilar 2: tokens/design system; saída em formatos abertos
   — HTML + ODF/software livre) → 4. **Qualidade** (Pilar 3) + **Acessibilidade** (Pilar 4) → 5. **IA
   responsável** (Pilar 5) → 6. **Método ADDIE** (Pilar 6) → 7. **Avaliação/resultados** (inspeção
   heurística + auditoria de acessibilidade + apresentação demonstrativa) → 8. **Limitações** (necessidade
   de capacitação/conscientização dos servidores) **e trabalhos futuros** (validação empírica com
   usuários, estudos de adoção e impacto).

> Nota de integridade: o resumo só pode **afirmar** avaliação (inspeção heurística, auditoria de
> acessibilidade) **depois** de realizá-las de fato. Ver checklist na submissão.

## Observações sobre as fontes
- **Canônicas (citadas no resumo — ver [ARTIGO-FINAL.md](ARTIGO-FINAL.md)):** Aldoobie (ADDIE); Batista
  (HITL); Brasil 2015 (Lei 13.146), 2020 (eMAG), 2026a (IA na Educação Básica), 2026b (Matriz de
  Competências em IA); Machado/Missel e Mayer (TCAM); Santos & Tarouco (carga cognitiva); WCAG 2.2/W3C.
- **Apoio (oficiais, não citadas no resumo):** gov.br (identidade digital), OASIS/ISO (ODF), W3C
  (design tokens), CAPES (Produção Técnica), Decreto 5.296/2004, USWDS, GOV.UK.
- **Ilustrativas (usar com parcimônia, não como prova):** blogs de mercado sobre custo de inconsistência.

> **Mudanças desta revisão (alinhamento ao artigo final):** método passou de Design Science Research para
> **ADDIE** (Aldoobie); IA responsável passou a citar a **Matriz de Competências em IA** (Competência 2),
> **Brasil 2026a** e **Batista** (HITL), no lugar de UNESCO/PL 2338/IBM; princípios de slide citam
> **Santos & Tarouco, Missel e Mayer** (sem assertion-evidence/Alley); exportação é **LibreOffice
> Impress**, não PowerPoint.
