# Avaliação do Protótipo — Inspeção Heurística e Auditoria de Acessibilidade

> Evidência para a seção de resultados da submissão Concefor (Eixo 1). Avaliação de **protótipo** (não é
> piloto com usuários finais). Objeto: deck de exemplo `cefor-slides/exemplos/exemplo-versao-a.html`
> (Versão A — Cor Sólida), representativo da saída da skill.
> Método alinhado à Design Science Research: avaliação → refinamento do artefato.

## 1. Método

- **Auditoria de acessibilidade** contra **WCAG 2.2 nível AA** e **eMAG**, com cálculo de razão de
  contraste pela fórmula oficial do W3C (luminância relativa; (L1+0,05)/(L2+0,05)). Verificação de
  estrutura, alternativas, navegação por teclado e movimento reduzido.
- **Inspeção heurística por especialista** com as 10 heurísticas de Nielsen e princípios de design de
  slides baseados em evidência (Mayer/CTML, Sweller/CLT, Alley/Assertion-Evidence).
- Referências em [FUNDAMENTACAO-CONCEFOR.md](FUNDAMENTACAO-CONCEFOR.md).

## 2. Auditoria de acessibilidade — contraste (cores reais do protótipo)

| Combinação (texto / fundo) | Razão | WCAG AA (texto normal ≥ 4,5:1) |
|----------------------------|-------|-------------------------------|
| Tinta `#2B2B2B` / branco | **14,2:1** | ✅ AAA |
| Tinta `#2B2B2B` / cinza `#EAEAEC` | **11,8:1** | ✅ AAA |
| Azul `#2C459A` / branco | **8,7:1** | ✅ AAA |
| Tinta `#2B2B2B` / lima `#B0CB1F` (barra de título) | **7,7:1** | ✅ AAA |
| Azul `#2C459A` / cinza (KPI) | **7,2:1** | ✅ AAA |
| Texto médio `#5A5A5A` / branco | **6,9:1** | ✅ AAA |
| Texto médio `#5A5A5A` / cinza | **5,7:1** | ✅ AA |
| Vermelho `#CC1111` / branco | **5,7:1** | ✅ AA |
| **Branco / lima `#B0CB1F`** (capa, versão inicial) | **1,8:1** | ❌ FALHA |
| **Oliva `#8C9A0D` / branco** (rodapé, versão inicial) | **3,1:1** | ❌ falha p/ texto normal |
| **Verde `#2E9B30` / branco** (selo "concluído", inicial) | **3,6:1** | ❌ falha p/ texto pequeno |
| Lima `#B0CB1F` / branco (número de seção, decorativo) | 1,8:1 | ⚠️ aceitável só como decoração |

## 3. Achados e severidade (com correções aplicadas)

| # | Achado | Severidade | Ação |
|---|--------|-----------|------|
| A1 | Capa: texto **branco sobre lima** (título, eyebrow, subtítulo) ~1,8:1 | **Crítico** | ✅ Corrigido: texto em **tinta** sobre lima (7,7:1) |
| A2 | Movimento reduzido (`prefers-reduced-motion`) ausente | Médio | ✅ Corrigido: media query adicionada |
| A3 | Rodapé `cefor.ifes.edu.br` em oliva ~3,1:1 | Médio | ✅ Corrigido: oliva escurecida `#6E7A0A` (~4,7:1) |
| A4 | Selo "Concluído" em verde ~3,6:1 | Médio | ✅ Corrigido: verde escurecido `#1B6E1F` (~5,5:1) |
| A5 | Logo (SVG) sem nome acessível | Médio | ✅ Corrigido: `role="img"` + `aria-label` |
| A6 | Títulos de conteúdo em `<div>`/`<span>` (sem hierarquia semântica além do `<h1>`) | Médio | ⏳ Recomendado: usar `<h2>`/`role=heading`. Demonstrado na figura de referência |
| A7 | Setas/números decorativos sem `aria-hidden` | Baixo | ⏳ Recomendado: `aria-hidden="true"`. Demonstrado na figura |
| A8 | Palco fixo não reflui texto ao ampliar (zoom) — limitação inerente do formato 16:9 | Médio (limitação) | Mitigação: exportação em PPTX/HTML e alternativa textual; registrado como limitação |

**Pontos fortes confirmados:** estrutura `lang="pt-BR"`, HTML semântico (`<main>`/`<section>`), navegação
completa por teclado (setas, espaço, PageUp/Down) e toque, marca d'água decorativa com `aria-hidden`,
status comunicado por **texto + cor** (não apenas cor), botão de edição como `<button>` focalizável,
e a maioria das combinações de texto em **AA/AAA**.

## 4. Inspeção heurística (Nielsen) — síntese

| Heurística | Avaliação |
|------------|-----------|
| Visibilidade do status | ✅ Barra de progresso + contador de slides |
| Correspondência com o mundo real | ✅ Linguagem clara em PT-BR |
| Controle e liberdade do usuário | ✅ Navegação reversível; edição via `contenteditable` (desfazer nativo) |
| Consistência e padrões | ✅ Identidade e modelos consistentes (segue o design system) |
| Prevenção de erros | ✅ "Salvar" baixa novo arquivo (não sobrescreve o original) |
| Reconhecer em vez de lembrar | ⚠️ Affordance de edição é oculta (hotzone) — mitigada por tecla **E** e tooltip |
| Flexibilidade e eficiência | ✅ Atalhos (setas, E, Ctrl+S) |
| Estética e minimalismo | ✅ Slides limpos, uma ideia por slide |
| Recuperação de erros | n/a |
| Ajuda e documentação | ✅ README/SKILL |

## 5. Princípios de design de slides (evidência)

- **Mayer (coerência/sinalização)** e **Sweller (carga cognitiva)**: ✅ baixa carga extrínseca — layout
  limpo, barra de título sinaliza o tópico, sem poluição visual.
- **Alley (Assertion-Evidence)**: ⚠️ **parcial** — vários títulos ainda são *rótulos* ("Objetivos da
  Reunião", "Indicadores...") em vez de *asserções* (frases-tese). Oportunidade de melhoria registrada
  como trabalho futuro (oferecer modo de título-asserção).

## 6. Veredito

**Conformidade parcial com WCAG 2.2 AA, com a maioria dos textos em AA/AAA e estrutura adequada.** A
auditoria identificou achados pontuais — sobretudo o contraste da capa — que foram **corrigidos no ciclo
de refinamento** (DSR): capa em tinta sobre lima, movimento reduzido, rodapé e selo escurecidos, e nome
acessível no logo. Recomendações remanescentes (hierarquia semântica de títulos e `aria-hidden` em
elementos decorativos) estão demonstradas na **figura de referência** ([figura-representativa.html](figura-representativa.html))
e devem ser incorporadas ao gabarito da skill. Limitação inerente: o palco fixo 16:9 não reflui texto
sob ampliação — mitigada por exportação e alternativas.

> Reflexo no resumo: descrever como *"avaliação por inspeção heurística e auditoria de acessibilidade
> (WCAG 2.2/eMAG), cujos achados orientaram refinamentos do protótipo"* — afirmação verídica e que
> evidencia rigor metodológico (ciclo avaliação→refinamento da DSR), em vez de alegar conformidade total.
