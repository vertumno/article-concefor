# Story: Migrar exportação de PowerPoint (.pptx) para LibreOffice Impress (.odp)

**Status:** InProgress  
**Data:** 2026-06-19  
**Decisão:** Alinhamento com política de software livre do governo federal brasileiro

---

## Contexto

A skill `cefor-slides` atualmente exporta para PowerPoint (.pptx) editável usando a skill proprietária de PPTX da Anthropic. Esta decision precisa mudar para:

1. **Remover dependência proprietária** — skill de PPTX fica fora do controle
2. **Usar ODF (.odp)** — formato aberto, alinhado com Libreoffice (recomendação do gov federal)
3. **Gerar .odp via Python direto** — sem dependências externas

---

## Aceitação

- [x] SKILL.md atualizado: remover menção a .pptx, adicionar .odp como formato de exportação
- [x] Script Python criado: `scripts/generate-odp.py` para converter HTML → .odp
- [x] README.md atualizado: mencionar .odp em lugar de .pptx
- [x] Fase 6A (SKILL.md) reescrita: usar Python em vez de skill de PPTX
- [ ] Concetor/FUNDAMENTACAO-CONCEFOR.md revisado: atualizar if menciona exportação
- [x] Documentação da skill (descrição breve no início) atualizada
- [x] Dependências Python documentadas (lxml, pillow, requests)

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
- [ ] Gerar .odp a partir de exemplo Versão A
- [ ] Gerar .odp a partir de exemplo Versão B
- [ ] Abrir em LibreOffice Impress e validar:
  - [ ] Todas as cores corretas
  - [ ] Tipografia intacta
  - [ ] Imagens carregam
  - [ ] Layout não estourou
  - [ ] Acessibilidade mantida (alt text, contraste)

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

