# QA Checklist — pedagógico + visual (Cefor)

Inspeção dos thumbnails/renders dos decks. Duas frentes: **qualidade pedagógica** (as 4 camadas) e **qualidade visual/técnica**.

## A. Qualidade pedagógica (rubrica das 4 camadas)

### Alley (estrutura do slide) — bloqueante
- [ ] Todo slide de conteúdo tem **título-afirmação** (frase completa), não rótulo-tópico.
- [ ] Corpo é **evidência visual**, não parede de bullets.

### Sweller (carga cognitiva)
- [ ] ≤ ~40 palavras visíveis por slide (exceto tabela/anexo).
- [ ] Uma ideia por slide; sem acúmulo.
- [ ] Sem ruído decorativo (carga extrínseca).

### Mayer (CTML)
- [ ] Rótulos junto ao elemento gráfico (contiguidade).
- [ ] Notas do apresentador ≠ texto da tela (sem redundância).
- [ ] Palavra + imagem, não palavra sozinha, onde cabível.
- [ ] Sinalização do essencial (cor/peso da identidade Cefor).

### Merrill (sequência) — sobretudo Modo 2
- [ ] O deck tem arco: ativação → demonstração → aplicação → integração.
- [ ] Cada objetivo de aprendizagem é endereçado por ≥ 1 slide.

## B. Visual / técnico

### Críticos (corrigir)
- [ ] **Texto cortado** por barras, formas ou bordas.
- [ ] **Overflow** além do container.
- [ ] **Texto ausente** (provável `<div>`/`<span>` sem tag de texto).
- [ ] **Layout quebrado** (sobreposição, colunas desalinhadas, flex colapsado).
- [ ] **Sobreposição** de gráfico/tabela com texto.
- [ ] **Texto ilegível** (pequeno/claro/baixo contraste).

### Avisos (preferível corrigir)
- [ ] Espaçamento inconsistente entre slides do mesmo tipo.
- [ ] **Cores fora da paleta Cefor** (Sólida ou Degradê — ver `design-system/palette.md`).
- [ ] Fallback de fonte (não-Arial substituída).
- [ ] Excesso de espaço vazio.

### Conformidade de marca Cefor
- [ ] Variante visual consistente em todo o deck (não misturar Sólida e Degradê).
- [ ] Rodapé `cefor.ifes.edu.br` presente onde o template prevê.
- [ ] Cores conforme `design-system/palette.md`; fonte Arial.
- [ ] Contraste: texto escuro sobre oliva; texto branco sobre azul/teal.
- [ ] 1º slide = title-slide; último = end-slide.

## C. Scoring ponderado (verdict do deck)

Adaptado da rubrica da `slide-creator` para dimensões pedagógicas. Pontue 0–100 cada dimensão; verdict = soma(score × peso) / 100.

| Dimensão | Peso | Foco |
|----------|-----:|------|
| Estrutura assertion-evidence (Alley) | 25 | título-afirmação + evidência, sem bullets |
| Carga cognitiva (Sweller) | 20 | densidade, 1 ideia/slide, sem ruído |
| Design multimídia (Mayer) | 20 | sinalização, contiguidade, sem redundância |
| Sequência instrucional (Merrill) | 15 | arco activation→demonstration→application→integration |
| Clareza didática | 10 | objetivos claros, aluno consegue reconta |
| Identidade + técnico | 10 | design Cefor consistente, 16:9, sem placeholders |

Verdict: **≥85 PASS** · 75–84 REVIEW (revisar) · **<75 FAIL** (não entregar; tratar como rascunho diagnóstico).

```yaml
qa_report:
  weighted_score: 0
  verdict: "PASS | REVIEW | FAIL"
  scores: {assertion_evidence: 0, carga_cognitiva: 0, multimidia: 0, sequencia: 0, clareza: 0, identidade_tecnico: 0}
  killer_issues: [""]
  revisions_applied: [""]
```

## Processo

1. Rode os validadores (`skills/qa/validate_outline.py`, `check_pptx.py`) — bloqueiam se falham.
2. Inspecione thumbnails com as seções A/B e `anti-patterns.md`.
3. Para cada problema: anote sessão + nº do slide + tipo → corrija o HTML no Stage 04 → `node [session].js` → re-gere thumbnails → verifique → marque resolvido.
4. Pontue as dimensões (seção C) e registre o verdict no QA report.
