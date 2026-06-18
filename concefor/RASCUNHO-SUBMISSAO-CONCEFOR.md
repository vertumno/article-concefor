# Rascunho de Submissão. Produção Técnica. VIII Concefor (versão genérica, Eixo 1)

> **Status:** rascunho anonimizado (fase de revisão cega). Preencher autores apenas na versão final.
> **Modalidade:** Produção Técnica. **Categoria:** Recursos Tecnológicos e Digitais.
> **Eixo:** 1, Educação a Distância (dimensões institucionais e de gestão; uso responsável de IA).
> **Formato final:** colar no template oficial do evento e exportar em PDF.
> **Fundamentação e links:** ver [FUNDAMENTACAO-CONCEFOR.md](FUNDAMENTACAO-CONCEFOR.md).
> **Avaliação (resultados):** ver [AVALIACAO-PROTOTIPO.md](AVALIACAO-PROTOTIPO.md).
> **ANONIMIZAÇÃO:** não citar Cefor/Ifes como "nossa instituição"; usar "um centro público federal de
> EaD". Anonimizar a marca em imagem e vídeo (placeholder "Instituto X") na fase de avaliação e restaurar
> a identidade real apenas na versão final (camera-ready).
> **Observação de estilo:** texto redigido sem travessão, conforme solicitado.

---

## TÍTULO (3 opções, escolher uma)

1. Skill de inteligência artificial para geração de apresentações institucionais padronizadas e
   acessíveis: protótipo para a comunicação de um centro público de educação a distância
2. Geração assistida por IA de apresentações institucionais com identidade visual, acessibilidade e
   supervisão humana: uma skill como produção técnica para a educação a distância
3. Do conteúdo ao slide institucional acessível: protótipo de skill com inteligência artificial
   responsável para a comunicação na educação a distância

---

## RESUMO (até 500 palavras, parágrafo único, Arial 12, justificado)

> Contagem atual aproximada: 480 palavras (revisar e ajustar ao colar no template).

A comunicação institucional de centros públicos de formação e educação a distância depende fortemente de
apresentações de slides. Embora a instituição já disponibilize modelos visuais oficiais em formato
editável, a aplicação desses modelos no cotidiano por servidores de diferentes setores, em geral sem
formação em design, é trabalhosa e ainda gera peças inconsistentes com a identidade institucional, além
de consumir tempo. Com a difusão da inteligência artificial generativa, esses profissionais passaram a
recorrer à IA para produzir conteúdo, porém de forma desarticulada do padrão institucional: a saída da IA
não incorpora a identidade visual oficial e conciliar o material gerado com os modelos existentes
permanece manual e inconsistente. Há, assim, uma lacuna entre a adoção da IA e a sua integração ao padrão
visual da instituição. Esta produção técnica apresenta um protótipo de skill, entendida como uma extensão
que adiciona instruções, modelos e padrões a um agente de inteligência artificial, para integrar a IA
generativa ao sistema de design oficial de um centro público federal de educação a distância (identidade
omitida para revisão cega). Dessa forma, qualquer servidor produz com rapidez, a partir do conteúdo
entregue, apresentações já padronizadas e acessíveis, sem a etapa manual de adequação à marca. O objetivo é ampliar a autonomia de
usuários não especialistas, assegurando consistência de marca, qualidade visual e conformidade com a
acessibilidade. O desenvolvimento seguiu a Design Science Research, com ciclos de projeto e avaliação do
artefato: primeiro, a formalização da identidade institucional em tokens de design (cores, tipografia e
elementos de marca) e em duas linguagens visuais oficiais; em seguida, a definição de um fluxo simples,
baseado na entrega do conteúdo, na escolha de estilo por pré-visualização e na geração automática; por
fim, a produção das apresentações como arquivos HTML autossuficientes, em proporção fixa de tela, com
edição de texto no navegador e exportação para PowerPoint editável e link. O design dos slides
apoia-se em princípios baseados em evidência (teoria cognitiva da aprendizagem multimídia, teoria da
carga cognitiva e abordagem assertion-evidence) e a acessibilidade é incorporada por padrão (contraste,
alternativas textuais, navegação por teclado e respeito à preferência por movimento reduzido), em
conformidade com a Lei 13.146/2015, o eMAG e as diretrizes WCAG. O uso de inteligência artificial adota o
modelo de supervisão humana (human in the loop), com transparência e rastreabilidade, alinhado às
recomendações da UNESCO e às orientações brasileiras para uso de IA no serviço público. A avaliação do
protótipo combinou inspeção heurística por especialista e auditoria de acessibilidade segundo a WCAG 2.2
e o eMAG, cujos achados orientaram refinamentos, somada a uma apresentação demonstrativa. Os resultados indicam viabilidade
técnica, padronização consistente e acessibilidade desde a concepção, com saída aberta e reproduzível,
independente da ferramenta de IA. A exportação para PowerPoint reaproveita o modelo editável já
distribuído pela instituição, preservando o padrão no formato que ela utiliza. Como limitações,
registram-se a ausência de validação empírica com usuários finais e a dependência de ferramenta externa
para a exportação em PowerPoint, indicadas como trabalhos futuros, ao lado de estudos de adoção e de
impacto. Quanto ao uso de inteligência artificial:
ferramentas de IA generativa foram empregadas na concepção e na implementação da skill, no apoio à
estruturação da solução, na geração de modelos e de código e em rascunhos textuais, sempre sob curadoria
e decisão humanas; toda saída gerada por IA foi revisada, testada e validada manualmente quanto à
fidelidade ao sistema de design, à acessibilidade e à correção técnica, e a identidade institucional e os
requisitos foram definidos por especialistas humanos, de modo a assegurar transparência, rastreabilidade
e integridade, em conformidade com a Política e Condições de Uso de IA do evento.

---

## PALAVRAS-CHAVE (até 5)

educação a distância; comunicação institucional; inteligência artificial generativa; acessibilidade
digital; identidade visual

---

## A PRODUÇÃO TÉCNICA (imagem representativa e descrição de até 10 linhas)

> **Imagem:** inserir um slide-título renderizado do protótipo. Na fase de avaliação, com marca
> anonimizada (placeholder "Instituto X"); na versão final, com a identidade real. Arquivo pronto em
> [figura-representativa.html](figura-representativa.html) (abrir e capturar a tela para gerar o PNG).

**Descrição (até 10 linhas):** A produção técnica é uma skill que estende um agente de inteligência
artificial e integra a IA generativa ao padrão visual já adotado pela instituição: a partir do conteúdo
entregue por um servidor, gera uma apresentação pronta, aplicando de forma automática a identidade oficial
por meio de um sistema de design (tokens de cor, tipografia e elementos de marca) e eliminando a etapa
manual de adequação aos modelos institucionais. Oferece duas linguagens visuais oficiais e gera os slides
em proporção fixa de tela, com edição de texto no próprio navegador. A saída é um arquivo HTML único, sem
dependências, exportável para PowerPoint editável ou link. A acessibilidade é incorporada por padrão (contraste,
alternativas textuais e navegação por teclado) e a IA é usada com supervisão humana. Voltada a usuários
não especialistas, busca conciliar padronização, autonomia, qualidade e conformidade legal.

---

## ENDEREÇO ELETRÔNICO (vídeo demonstrativo de até 3 minutos)

> Inserir link do Google Drive (compartilhamento aberto, sem revelar o nome do dono ou do canal).

**Roteiro do vídeo (cerca de 2min30):**
- 0:00 a 0:20. Problema: apresentações institucionais inconsistentes e demoradas para quem não é designer.
- 0:20 a 0:50. O servidor entrega o conteúdo e abre a skill.
- 0:50 a 1:20. Mostrar, não contar: duas pré-visualizações (linguagens A e B) e a escolha do estilo.
- 1:20 a 2:00. Apresentação gerada: navegação pelos slides (capa, conteúdo, dados, encerramento), tudo na
  identidade institucional.
- 2:00 a 2:30. Edição de texto no navegador e exportação em PowerPoint editável (no modelo oficial).
  Encerramento com a proposta de valor (padronização, acessibilidade e IA responsável).
- Anonimização: sem voz ou nome identificáveis; marca em placeholder; sem logotipo de canal; o uso de
  legendas em vez de narração ajuda a manter o anonimato.

---

## AGRADECIMENTOS (até 6 linhas, OMITIR na fase de avaliação)

> Agradecimentos identificam autoria, portanto não devem constar na versão cega. Modelo para a versão
> final, focado em apoio técnico e intelectual: "Agradecemos à equipe responsável pela identidade visual
> institucional pelo apoio técnico e à instituição pelo suporte ao desenvolvimento."

---

## CHECKLIST PRÉ-SUBMISSÃO

- [ ] Texto sem qualquer identificação de autor ou instituição (inclusive metadados do PDF).
- [ ] Marca anonimizada na imagem e no vídeo (placeholder) na fase de avaliação.
- [ ] Resumo com até 500 palavras, parágrafo único, Arial 12, justificado.
- [ ] Descrição do uso de IA presente no resumo (finalidade, etapa e validação humana). Já incluída.
- [ ] Até 5 palavras-chave.
- [ ] Imagem representativa e descrição de até 10 linhas.
- [ ] Vídeo de até 3 minutos, com link do Drive aberto e anônimo.
- [ ] Agradecimentos omitidos (entram apenas na versão final).
- [ ] Arquivo final em PDF, no template oficial, com os textos de instrução (azul e vermelho) removidos.
- [ ] Pelo menos um autor inscrito no evento.
- [ ] Inspeção heurística e auditoria de acessibilidade realizadas de fato (ver AVALIACAO-PROTOTIPO.md).
- [ ] E-mail à organização (submissoes.concefor@ifes.edu.br): (a) é permitido citar a instituição objeto
      de estudo na fase cega? (b) confirmar o Eixo 1 e a categoria "Recursos Tecnológicos e Digitais".
- [ ] LICENSE e NOTICE (licença MIT do projeto de origem) adicionados ao repositório do produto.
- [ ] Texto revisado sem travessão.

---

## O QUE SÓ VOCÊ PODE FAZER

1. Definir os autores (até 5) e inscrever pelo menos um.
2. Gravar o vídeo (até 3 minutos) seguindo o roteiro.
3. Baixar o template oficial, colar este conteúdo e exportar em PDF.
4. Enviar o e-mail à organização com as duas dúvidas (marca na fase cega; eixo e categoria).
5. Capturar o PNG da figura representativa a partir do arquivo HTML.
