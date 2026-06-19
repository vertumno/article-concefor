# Artigo final — Produção Técnica · VIII Concefor

> **Documento canônico (fonte da verdade) da submissão.** Texto final aprovado pelos autores.
> Os demais documentos do projeto (`FUNDAMENTACAO-CONCEFOR.md`, `RASCUNHO-SUBMISSAO-CONCEFOR.md`,
> `AVALIACAO-PROTOTIPO.md` e o `README.md`) derivam deste artigo e devem manter-se consistentes com ele.
>
> **Modalidade:** Produção Técnica. **Categoria:** Recursos Tecnológicos e Digitais. **Eixo:** 1 (EaD).
> **Revisão cega:** a identidade institucional é omitida no corpo do resumo; os autores entram apenas na
> versão final (camera-ready), não na versão de avaliação.

---

## Título

Skill de inteligência artificial para geração de apresentações institucionais padronizadas e acessíveis

## Autores

| Autor | Instituição | E-mail |
|-------|-------------|--------|
| Elton Vinicius Silva | Cefor/Ifes | eltonvinicius@ifes.edu.br |
| Marcos Vinícius Forecchi Accioly | Cefor/Ifes | marcos.accioly@ifes.edu.br |
| Rutinelli da Penha Fávero | Cefor/Ifes | rutinelli@ifes.edu.br |
| Andreia Cristina Carvalho Cáo | Cefor/Ifes | andreia.cao@ifes.edu.br |

> Na fase de avaliação (revisão cega), os autores e a instituição são omitidos do PDF e dos metadados.

## Resumo

A comunicação de instituições públicas depende fortemente de apresentações de slides. Embora a instituição já disponibilize modelos visuais oficiais em formato editável, a aplicação desses modelos no cotidiano por servidores de diferentes setores, em geral sem formação em design, é trabalhosa e ainda gera peças inconsistentes com a identidade institucional, além de consumir tempo. Com a difusão da inteligência artificial generativa, esses profissionais passaram a recorrer à IA para produzir conteúdo, porém de forma desarticulada do padrão institucional: a saída da IA não incorpora a identidade visual oficial e conciliar o material gerado com os modelos existentes permanece manual e inconsistente. Há, assim, uma lacuna entre a adoção da IA e a sua integração ao padrão visual da instituição. Além disso, a Competência 2 da Matriz de Competências em IA, lançada este ano pela Secretaria de Governo Digital (Brasil, 2026b), indica que o agente público deve aplicar, de forma assistida e sob supervisão, soluções de IA generativa e analítica para criar e refinar documentos e relatórios padronizados, mantendo o julgamento crítico e a responsabilidade humana pela validação final para melhorar a produtividade e a qualidade dos serviços. Assim, esta produção técnica apresenta uma skill - entendida como uma extensão que adiciona instruções, modelos e padrões a um agente de inteligência artificial, para integrar a IA generativa ao sistema de design oficial de uma instituição pública (identidade omitida para revisão cega). Dessa forma, qualquer servidor produz com rapidez, a partir do conteúdo entregue, apresentações já padronizadas e acessíveis, sem a etapa manual de adequação à marca. O objetivo é ampliar a autonomia de usuários não especialistas, assegurando consistência de marca, qualidade visual e conformidade com os padrões de acessibilidade. O desenvolvimento do artefato foi guiado por aspectos do modelo ADDIE (Aldoobie, 2015). A aplicação do framework estruturou-se em ciclos contínuos de projeto e avaliação através de três momentos principais: primeiro, na fase de design e especificação, formalizou-se a identidade institucional em design tokens (cores, tipografia e elementos da imagem) distribuídos em duas linguagens visuais oficiais; segundo, estruturou-se o fluxo de experiência do usuário, baseado na entrega direta do conteúdo, escolha de estilo por pré-visualização e geração automatizada; terceiro, na etapa de desenvolvimento e entrega técnica, viabilizou-se a produção das apresentações como arquivos HTML autossuficientes em proporção fixa de tela, com edição de texto no próprio navegador e exportação para o formato editável do LibreOffice Impress (conforme a recomendação oficial para órgãos do governo brasileiro). O design dos slides apoia-se em princípios baseados em aspectos da Teoria Cognitiva da Aprendizagem Multimídia e da Teoria da Carga Cognitiva (Santos; Tarouco, 2007; Missel, 2023; Mayer, 2023) e a acessibilidade é incorporada por padrão (contraste, alternativas textuais, navegação por teclado e respeito à preferência por movimento reduzido), em conformidade com a Lei 13.146/2015 (Brasil, 2015), o eMAG (Brasil, 2020) e as diretrizes WCAG (WORLD WIDE WEB CONSORTIUM, 2025). Quanto ao uso de inteligência artificial: ferramentas de IA generativa como Claude Code e Claude Design foram empregadas na concepção e na implementação da skill, no apoio à estruturação da solução, na geração de modelos e de código e em rascunhos textuais, sempre sob curadoria e decisão humanas; adotou-se um modelo de supervisão humana, conhecido como human in the loop (Batista, 2026), em que a verificação foi realizada nas entregas ao final das etapas de produção. Toda saída gerada por IA foi revisada, testada e validada manualmente quanto à fidelidade ao sistema de design, à acessibilidade e à correção técnica, e a identidade institucional e os requisitos foram definidos por especialistas humanos, de modo a assegurar transparência, rastreabilidade e integridade. Buscou-se, ainda, manter suficiente transparência e rastreabilidade da produção, conforme as recomendações brasileiras para uso de IA no serviço público e em educação (Brasil, 2026a; Brasil, 2026b). A avaliação do protótipo combinou inspeção heurística por especialistas internos e auditoria de acessibilidade segundo a WCAG 2.2 e o eMAG, cujos achados orientaram refinamentos, somada a uma apresentação demonstrativa. Os resultados indicam viabilidade técnica, padronização consistente e acessibilidade desde a concepção, com saída aberta e reproduzível, independente da ferramenta de IA. A exportação para Impress reaproveita o modelo editável já distribuído pela instituição, preservando o padrão no formato que ela utiliza. Como limitação pode haver necessidade de capacitação e/ou conscientização para acompanhamento do processo dos servidores que usarão a ferramenta. Registra-se a validação empírica com amostragem de usuários finais como próximo passo, assim como estudos de adoção e de impacto.

## Palavras-chave

educação a distância; comunicação institucional; inteligência artificial generativa; acessibilidade digital; identidade visual.

## A produção técnica

A produção técnica é uma skill que estende um agente de inteligência artificial e integra a IA generativa ao padrão visual já adotado pela instituição: a partir do conteúdo entregue por um servidor, gera uma apresentação pronta, aplicando de forma automática a identidade oficial por meio de um sistema de design (tokens de cor, tipografia e elementos de marca) e eliminando a etapa manual de adequação aos modelos institucionais. Oferece duas linguagens visuais oficiais e gera os slides em proporção fixa de tela, com edição de texto no próprio navegador. A saída é um arquivo HTML único, sem dependências, exportável para Impress editável. A acessibilidade é incorporada por padrão (contraste, alternativas textuais e navegação por teclado) e a IA é usada com supervisão humana. Voltada a usuários não especialistas, busca conciliar padronização, autonomia, qualidade e conformidade com normativas.

## Referências

ALDOOBIE, N. ADDIE model. *American International Journal of Contemporary Research*, v. 5, n. 6, p. 68-72, dec. 2015. Disponível em: https://aijcr.thebrpi.org/journals/Vol_5_No_6_December_2015/10.pdf. Acesso em: 19 jun. 2026.

BATISTA, Elisa de Souza Senra Lopes et al. HUMAN-IN-THE-LOOP (HITL): Uma abordagem que integra a participação humana em sistemas de inteligência artificial e automação. *Revista para Graduandos/Instituto Federal de Educação, Ciência e Tecnologia de São Paulo - Campus São Paulo - REGRASP*, [S. l.], v. 10, n. 4, p. 84–90, 2025. DOI: 10.47734/regrasp.v10.04.p84-90. Disponível em: https://regrasp.spo.ifsp.edu.br/index.php/regrasp/article/view/1307. Acesso em: 19 jun. 2026.

BRASIL. Lei nº 13.146, de 6 de julho de 2015. Institui a Lei Brasileira de Inclusão da Pessoa com Deficiência (Estatuto da Pessoa com Deficiência). Brasília, DF: Presidência da República, 2015. Disponível em: http://www.planalto.gov.br/ccivil_03/_ato2015-2018/2015/lei/l13146.htm. Acesso em: 19 jun. 2026.

BRASIL. Ministério da Gestão e da Inovação em Serviços Públicos. Secretaria de Governo Digital. eMAG: Modelo de Acessibilidade em Governo Eletrônico. Brasília, DF: MGI/SGD, 2020. Disponível em: https://www.gov.br/governodigital/pt-br/acessibilidade-e-usuario/acessibilidade-digital/modelo-de-acessibilidade. Acesso em: 19 jun. 2026.

BRASIL. Ministério da Educação. Inteligência Artificial na Educação Básica: diretrizes para uso e aprendizagem sobre IA. Brasília, DF: MEC, 2026a. Disponível em: https://www.gov.br/mec/pt-br/escolas-conectadas/arquivos/ia-educacao-basica.pdf. Acesso em: 19 jun. 2026.

BRASIL. Ministério da Gestão e da Inovação em Serviços Públicos. Secretaria de Governo Digital. Matriz de Competências em Inteligência Artificial. Brasília, DF: MGI/SGD, 2026b. Disponível em: https://www.gov.br/governodigital/pt-br/infraestrutura-nacional-de-dados/inteligencia-artificial-1/matrizdeIA. Acesso em: 19 jun. 2026.

MACHADO, Luís Antônio Licks Missel et al. Recursos multimídia na educação sob o enfoque da teoria cognitiva de aprendizagem de Richard Mayer. *Redin - Revista Educacional Interdisciplinar*, [S. l.], v. 12, n. 2, p. 121–140, 2023. Disponível em: https://seer.faccat.br/index.php/redin/article/view/2855. Acesso em: 19 jun. 2026.

MAYER, Richard E. Teoria Cognitiva da Aprendizagem Multimédia. In: MIRANDA, Guilhermina Lobato (org.). *Ensino online e aprendizagem multimédia*. Lisboa: Relógio D'Água, 2009. p. 207-237. Disponível em: http://webhosting.bombyte.org/~joao.gama/guilhermina/m3/Mod3G2/Mayer_TCAMultimedia.pdf. Acesso em: 19 jun. 2026.

SANTOS, Leila Maria Araújo; TAROUCO, Liane Margarida Rockenbach. A IMPORTÂNCIA DO ESTUDO DA TEORIA DA CARGA COGNITIVA EM UMA EDUCAÇÃO TECNOLÓGICA. *RENOTE*, Porto Alegre, v. 5, n. 1, 2007. DOI: 10.22456/1679-1916.14145. Disponível em: https://seer.ufrgs.br/index.php/renote/article/view/14145. Acesso em: 19 jun. 2026.

WORLD WIDE WEB CONSORTIUM. Diretrizes de Acessibilidade para Conteúdo Web (WCAG) 2.2. Tradução autorizada de Web Content Accessibility Guidelines (WCAG) 2.2. Coordenação de tradução: Ceweb.br. [S. l.]: W3C, 2025. Disponível em: https://www.w3.org/Translations/WCAG22-pt-BR/. Acesso em: 19 jun. 2026.
