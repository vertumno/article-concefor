# Story: Melhorias da skill cefor-slides (Sprints 1 e 2 da avaliação sênior)

**Status:** Done (pendência humana: conferir os `.odp` no LibreOffice Impress)
**Data:** 2026-07-16
**Origem:** Avaliação sênior completa da skill (16/07/2026) — 3 bugs confirmados em teste,
1 regressão latente de acessibilidade e melhorias de robustez. O artigo Concefor foi aprovado
e está congelado; esta story toca **apenas** `cefor-slides/`.

---

## Contexto

A skill é sólida (scaffold determinístico, HTML fonte da verdade, otimização de tokens real),
mas testes práticos confirmaram defeitos que um servidor real sentiria: impressão/PDF quebrada
nos decks do scaffold, Ctrl+S salvando estado sujo, título sem escape, e os docs de layout
(STYLE_PRESETS/html-template) ainda descrevendo o design pré-auditoria WCAG (branco sobre lima,
crítico 1,8:1) que a auditoria do artigo corrigiu só no exemplo.

---

## Aceitação — Sprint 1 (correções P0)

- [x] S1.1 `deck-base.css` ganha bloco `@media print` (1 slide/página; esconde edit-toggle,
      edit-hotzone e deck-progress) — deck do scaffold imprime/exporta PDF corretamente
- [x] S1.2 `new-deck.py`: `--title` escapado com `html.escape()` (testar com `&` e `<`)
- [x] S1.3 `salvar()` (Ctrl+S) serializa cópia limpa: sem `contenteditable`, sem `.active`/`.show`,
      sem `.deck-progress` injetada; nome do arquivo derivado do `<title>` — sincronizado em
      `new-deck.py`, `html-template.md` e `exemplos/exemplo-versao-a.html`
- [x] S1.4 Docs alinhados à auditoria WCAG: `STYLE_PRESETS.md` A1 (tinta sobre lima, não branco);
      `html-template.md` capa em tinta + rodapé oliva AA `#6E7A0A`
- [x] S1.5 Recomendações A6/A7 da auditoria incorporadas ao gabarito: `<h2>` nos títulos de
      conteúdo e `aria-hidden="true"` em SVGs decorativos — em `slide-patterns.md`,
      `html-template.md` e no exemplo A

## Aceitação — Sprint 2 (robustez)

- [x] S2.1 Open Sans (400/600/700/800) embutida como woff2 base64 injetada pelo scaffold
      (`scripts/deck-fonts.css`); sem chamada ao Google Fonts nos decks gerados (offline +
      privacidade); validador do `new-deck.py` atualizado; fallback manual documenta a limitação
- [x] S2.2 `generate-odp.py`: tabelas HTML viram **tabelas ODF reais** (editáveis no Impress);
      pares KPI (`.kpi-num`/`.kpi-label`) viram linhas "num — label"; aviso `[AVISO]` quando um
      slide contribui 0 blocos (fim da perda silenciosa)
- [x] S2.3 `exemplos/exemplo-versao-b.html` criado **via scaffold** (dogfooding), fiel a B1/B3/B4/B5
- [x] S2.4 `scripts/smoke-test.py` (stdlib): round-trip A/B, escape de título, `@media print`,
      `active` no 1º slide, tokens obrigatórios; generate-odp nos 2 exemplos com blocos/slide > 0
      e tabela ODF presente
- [x] S2.5 Bônus trivial: scaffold garante `active` no 1º slide se o agente esquecer
- [x] S2.6 Docs atualizados (SKILL.md, README da skill) e `cefor-slides.zip` regenerado em sincronia

---

## Fora do escopo (Sprint 3 — futuro)

extract-pptx (tabelas/grupos), prévias via scaffold, make-zip.py, teclas Home/End/Esc/F,
refactor de globals no generate-odp, remoção de `producao-tecnica/` e `slides-generator.zip`.

## Testes executados

- [x] `python scripts/smoke-test.py` — todos verdes (17/17)
- [x] `generate-odp.py` nos exemplos A e B — ODF válido na releitura (7 e 7 slides)
- [x] Verificação visual (screenshots via Chrome headless) dos exemplos A e B — capa,
      divisória, KPIs, tabela e encerramento conferidos
- [ ] **Pendente (humano):** abrir os `.odp` no LibreOffice Impress real e conferir tabelas/KPIs

## Bloqueadores

- Nenhum.
