# Story: Migrar exportação de PowerPoint (.pptx) para LibreOffice Impress (.odp)

**Status:** Done (validado nos exemplos Versão A e B)  
**Data:** 2026-06-19  
**Decisão:** Alinhamento com política de software livre do governo federal brasileiro

> **Nota de revisão (2026-06-19):** a 1ª implementação (`generate-odp.py` escrevendo ODF XML à mão)
> gerava arquivo **inválido** — `content.xml` não bem-formado (sem escaping), `<presentation:slide>`
> inexistente em ODF, sem master page, crash de console no Windows. Reescrita com **odfpy** (ODF válido
> por construção) + parser semântico robusto + autovalidação por releitura. Provado abrindo os dois
> exemplos.

---

## Contexto

A skill `cefor-slides` atualmente exporta para PowerPoint (.pptx) editável usando a skill proprietária de PPTX da Anthropic. Esta decision precisa mudar para:

1. **Remover dependência proprietária** — skill de PPTX fica fora do controle
2. **Usar ODF (.odp)** — formato aberto, alinhado com Libreoffice (recomendação do gov federal)
3. **Gerar .odp via Python direto** — sem dependências externas

---

## Aceitação

- [x] SKILL.md atualizado: remover menção a .pptx, adicionar .odp como formato de exportação
- [x] Script Python criado e **funcional**: `scripts/generate-odp.py` (odfpy) converte HTML → .odp válido
- [x] README.md atualizado: mencionar .odp em lugar de .pptx (mapa de pastas, seção 4, timeline, Concefor)
- [x] Fase 6A (SKILL.md) reescrita: usar script nativo em vez de skill de PPTX
- [ ] Concetor/FUNDAMENTACAO-CONCEFOR.md revisado: atualizar se menciona exportação
- [x] Documentação da skill (descrição breve no início) atualizada
- [x] Dependências Python documentadas e **consistentes** (odfpy obrigatória; pillow opcional)
- [x] Testado nos exemplos Versão A (7 slides) e Versão B (8 slides): ODF válido, releitura confirma slides

---

## Arquitetura

### Mudanças principais:

1. **Fase 6A (Exportar para .odp)**
   - Input: HTML da apresentação (da Fase 5)
   - Output: arquivo `.odp` editável em LibreOffice Impress
   - Método: Python script que lê HTML e constrói .odp usando `python-pptx` + ODF library
   - Alternativa: usar `libreoffice --headless` para converter HTML → ODP (requer LibreOffice no sistema)

2. **Remoção de dependências**
   - ~~skill de PPTX (proprietária)~~ ← REMOVIDA
   - ~~modelo .pptx do Cefor~~ ← REMOVIDA (substituir por modelo .odp se necessário)

3. **Novo workflow**
   ```
   Fase 5 (entregar HTML)
        ↓
   Fase 6A: Perguntar "Quer também em LibreOffice Impress (.odp)?"
        ↓
   scripts/generate-odp.py <deck.html> → deck.odp
   ```

---

## Tarefas

### Tarefa 1: Pesquisar bibliotecas Python para .odp
- [ ] Avaliar `odfpy` (criação nativa de ODF)
- [ ] Avaliar `lxml` + templates
- [ ] Avaliar `python-pptx` + plugin ODF (se existir)
- [ ] Decidir: qual é mais simples e confiável?

### Tarefa 2: Implementar `scripts/generate-odp.py`
- [ ] Parser de HTML (extrair slides, títulos, conteúdo, imagens)
- [ ] Gerador de .odp (usando biblioteca escolhida)
- [ ] Preservar marca Cefor (cores, fontes, espaçamento)
- [ ] Testes com Versão A e Versão B

### Tarefa 3: Atualizar documentação
- [ ] SKILL.md — Fase 6A reescrita
- [ ] README.md — linha 19-20 e seção 4
- [ ] cefor-slides.md (se existir descição)
- [ ] concefor/FUNDAMENTACAO-CONCEFOR.md (se menciona exportação)

### Tarefa 4: Testes
- [x] Gerar .odp a partir de exemplo Versão A (7 slides, ODF válido)
- [x] Gerar .odp a partir de exemplo Versão B (8 slides, ODF válido)
- [x] Autovalidação por releitura (odfpy `load`) integrada ao script
- [x] Auditoria: XML bem-formado em todas as partes, `draw:page` correto, escaping de acentos/`&`/`<`/`>`
- [ ] **Pendente (humano):** abrir os dois `.odp` no LibreOffice Impress real e conferir render final
  (cores, Open Sans, ausência de "estouro"). A geração é válida; falta o olho humano no app.

---

## Referências

- SKILL.md — linhas 160-182 (Fase 6A)
- html-template.md — estrutura HTML a parsear
- CEFOR_BRAND.md — tokens de marca a preservar
- LibreOffice SDK: https://api.libreoffice.org/

---

## Bloqueadores

- Nenhum no momento.

---

## Próximos passos

1. Executar Tarefa 1 (pesquisa de bibliotecas)
2. Escolher biblioteca + começar prototipagem
3. Implementar + testar
4. Documentar + atualizar SKILL.md

