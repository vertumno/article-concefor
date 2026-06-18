# Análise Comparativa — Geradores de Slides (para a Skill do Cefor)

> **Objetivo do estudo:** avaliar 3 criadores/geradores de slides existentes e definir em qual deles
> basear a futura **skill do Cefor** — um gerador de apresentações com template do Cefor, para uso
> **administrativo** (diretora, coordenadores: reuniões, eventos) e **educacional** (professores:
> ensinar conceitos, apresentar conteúdo).
>
> **Data:** 2026-06-16
> **Ferramentas analisadas:**
> 1. `C:\Users\1627042\#PROJETOS-CODE-IA\Interpreted-Context-Methdology\workspaces\course-deck-production`
> 2. `C:\Users\1627042\Desktop\slide-creator`
> 3. `C:\Users\1627042\Desktop\frontend-slides`

---

## 1. Identidade de cada ferramenta (resumo)

| # | Ferramenta | Em uma frase |
|---|------------|--------------|
| 1 | **course-deck-production** | Pipeline pedagógico de 5 estágios que transforma material bruto (PDFs, notas) em **PowerPoint (.pptx)** profissional para cursos. |
| 2 | **slide-creator** | Motor "narrative-first" de altíssimo nível, focado em **persuasão/venda** (pitch, webinar, board), baseado em contratos YAML. |
| 3 | **frontend-slides** | Gerador de apresentações **HTML lindas** com filosofia "show, don't tell" (mostra 3 previews e o usuário escolhe). Barreira de entrada quase zero. |

---

## 2. Quadro comparativo geral

| Categoria | 1) course-deck-production | 2) slide-creator | 3) frontend-slides |
|-----------|---------------------------|------------------|--------------------|
| **Foco principal** | Cursos / educação (multi-sessão) | Vendas, pitch, persuasão | Apresentações em geral (pitch, aula, palestra, interno) |
| **Output** | `.pptx` (PowerPoint editável) | YAML/spec → HTML/PPTX (sem renderer nativo) | `.html` standalone + PDF + deploy Vercel |
| **Stack** | Node.js + Python + HTML→PPTX | Python + YAML (contratos) | HTML/CSS/JS puro (zero dependências) |
| **Como se usa** | Conversacional, 5 estágios com checkpoints | Skill avançada com decision-tree de 38 regras | Skill conversacional, 6 fases simples |
| **Templates / temas** | 11 padrões de slide + design system (5 cores, 2 fontes) | 45 roteiros + 240+ estruturas de slide | 12 presets + 34 templates "bold" curados |
| **Qualidade visual** | Profissional, mas fontes só "web-safe" | Editorial sofisticado (densidade controlada) | Excelente — distintivo, anti-genérico (Google Fonts) |
| **Customização de marca** | Design system (paleta + tipografia) na config | Theme profiles (tokens) | CSS variables + template dedicado (fácil) |
| **Complexidade p/ usuário final** | Baixa | **Alta** (intermediário→avançado) | **Mínima** (quase zero) |
| **Complexidade p/ quem monta a skill** | Alta (muitas competências) | Muito alta | Média-baixa |
| **Pré-requisitos** | Node + Python + LibreOffice + Poppler | PyYAML (+ providers p/ render) | Nada p/ criar; Python/Node só p/ PPT/PDF/deploy |
| **Estrutura** | Workspace composável (não skill única) | Skill madura v1.0 (SKILL.md robusto) | Skill limpa e portável (SKILL.md de 381 linhas) |

---

## 3. Detalhamento por ferramenta

### 3.1. course-deck-production

- **O que faz de melhor:** estrutura **pedagógica** real (extração → currículo → objetivos de
  aprendizagem → outline → slides), com revisão humana (checkpoint) em cada etapa. Entrega
  **PowerPoint nativo editável**.
- **Diferencial:** único pensado de raiz para **educação multi-sessão** e único que entrega `.pptx`.
- **Deixa a desejar:** fontes só web-safe (Arial, Georgia…); sem animações; design system rígido
  (5 cores + 2 fontes); **muitos pré-requisitos de instalação** (Node, Python, LibreOffice, Poppler);
  pesado demais para o caso "preciso de slides para a aula de amanhã".
- **Pré-requisitos:** Node.js (`pptxgenjs`, `playwright`, `sharp`), Python (`markitdown[pptx]`,
  `defusedxml`), LibreOffice e Poppler.
- **Proficiência exigida:** usuário final = baixa (conversacional); quem monta/mantém = alta.
- **Fluxo:** `setup` (onboarding único) → 5 estágios: Extração → Currículo → Outline → Geração → QA.

### 3.2. slide-creator

- **O que faz de melhor:** rigor narrativo, rastreamento de evidências (claim → fonte), gates de
  qualidade pontuados (score ponderado), 45 roteiros profissionais e 240+ estruturas de slide.
- **Diferencial:** o mais sofisticado dos três; raciocina em "mudança de crença" e conversão; absorve
  padrões de 10 projetos open-source de referência.
- **Deixa a desejar:** **complexidade alta demais** para diretores/coordenadores/professores; foco em
  **venda/persuasão** (não em ensinar conceito); spec-first sem renderizador embutido (não "abre o
  slide pronto"). **Overkill** para o Cefor.
- **Pré-requisitos:** `pyyaml` (e providers de IA/render para gerar artefatos finais).
- **Proficiência exigida:** intermediária → avançada.
- **Fluxo:** normalizar briefing → belief shift → story arc → mapa de funções de slide → seleção de
  templates → design direction → deck-spec → gates → QA → empacotamento.

### 3.3. frontend-slides

- **O que faz de melhor:** **facilidade extrema** + alta qualidade visual. Já distingue o propósito na
  Fase 1 (Pitch / **Ensino** / Palestra / Interno) e o modo de densidade (apresentador vs. leitura).
- **Diferencial:** "show, don't tell" (mostra 3 estilos reais para o usuário reagir); **HTML
  standalone** que abre em qualquer máquina/projetor; edição inline no navegador (tecla **E**);
  conversão de PPT; export PDF; deploy Vercel; design anti-"AI slop".
- **Deixa a desejar:** saída principal é HTML (não `.pptx` editável); animações limitadas; sem
  estrutura pedagógica profunda como a #1.
- **Pré-requisitos:** nada para criar slides; Python (`python-pptx`) só para converter PPT; Node/
  Vercel só para deploy; Playwright só para export PDF.
- **Proficiência exigida:** mínima (praticamente zero).
- **Fluxo:** 6 fases — Detecção de modo → Content discovery → Style discovery (3 previews) → Geração →
  Entrega → Compartilhar/Exportar.

---

## 4. Aderência ao caso Cefor

O Cefor tem **dois públicos não-técnicos** e **duas finalidades**:

| Necessidade do Cefor | Quem atende melhor |
|----------------------|--------------------|
| Facilidade para diretora, coordenadores, professores (zero conhecimento técnico) | **#3 frontend-slides** |
| Template com a **identidade visual do Cefor** (consistência de marca) | **#3** (CSS vars + template dedicado) > #1 (design system) |
| Uso **administrativo** (reuniões, eventos) — rápido e bonito | **#3** |
| Uso **educacional** (ensinar conceitos) | **#1** (pedagogia) / **#3** (já tem modo "Ensino") |
| Slides projetáveis e fáceis de compartilhar | **#3** (HTML + PDF + link) |
| PowerPoint editável que todos sabem mexer | **#1** (único com `.pptx`) |
| Pouca instalação/manutenção | **#3** (zero dependências) |

---

## 5. Recomendação

### ✅ Basear a skill do Cefor no **frontend-slides (#3)**

Motivos centrais:
1. **Usuários não-técnicos** — diretora, coordenadores e professores usam sem saber design ou código
   (fator decisivo).
2. **Já possui o modo "Ensino"** nativo (Fase 1) e modos de densidade — cobre os dois usos
   (administrativo e educacional) sem reinventar.
3. **Marca Cefor trivial de aplicar** — criar um template "Cefor" (cores, logo, tipografia) e usá-lo
   como preset padrão; o "show, don't tell" passa a oferecer variações dentro da identidade do Cefor.
4. **Saída HTML** projeta bem, abre em qualquer máquina, vira PDF e link compartilhável.
5. **Arquitetura de skill limpa e portável** — a mais fácil de adaptar/forkar e manter.

### Complementos a trazer do course-deck-production (#1)
- **Objetivos de aprendizagem** e **padrões pedagógicos de slide** (definição, exemplo passo-a-passo,
  resumo) para o **modo professor**.
- Opcionalmente, **export para `.pptx`** se o Cefor exigir PowerPoint editável institucional.

### Descartado como base: slide-creator (#2)
Poderoso, porém complexo e voltado a venda/conversão — não combina com o perfil do Cefor.

### Única condição que mudaria a recomendação
Se o Cefor tiver como **requisito rígido entregar `.pptx` editável** (e não HTML/PDF), a balança pende
para o **course-deck-production (#1)** — ou então adiciona-se o export PPTX à skill baseada no #3.

---

## 6. Esboço da Skill do Cefor (`cefor-slides`)

> Defaults assumidos (a confirmar): saída **HTML + PDF** como principal, com **export PPTX opcional**;
> marca Cefor montada a partir do material fornecido (se nada vier, criar identidade provisória).

- **Fase 0 — Detecção de finalidade:** Modo Administrativo (reuniões, eventos, prestação de contas,
  comunicados) vs. Modo Educacional (ensinar conceito, aula, oficina).
- **Fase 1 — Coleta de conteúdo:**
  - Administrativo: tema, público, duração, mensagem-chave.
  - Educacional: tema, nível da turma, **objetivos de aprendizagem**, densidade.
- **Fase 2 — Estilo (identidade Cefor):** template Cefor como padrão; 2–3 variações dentro da marca
  para escolher ("show, don't tell").
- **Fase 3 — Geração:**
  - Administrativo: padrões executivos (capa, agenda, indicadores, próximos passos).
  - Educacional: padrões pedagógicos (definição, exemplo passo-a-passo, atividade, resumo).
- **Fase 4 — Entrega:** HTML pronto (navegador/projetor) + edição inline + export PDF; opcional `.pptx`.

---

## 7. Decisões pendentes (para iniciar a implementação)

1. **Formato principal de saída:** HTML + PDF, PPTX editável, ou os dois.
2. **Identidade visual do Cefor:** material disponível (logo, paleta, fontes) ou criar provisório.

---

*Documento gerado durante a sessão de análise. Próximo passo: estruturar os arquivos da skill
`cefor-slides` com base no frontend-slides após confirmação das decisões pendentes.*
