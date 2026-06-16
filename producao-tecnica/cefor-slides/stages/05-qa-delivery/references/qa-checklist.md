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

## Processo

Para cada problema: anote sessão + nº do slide + tipo → corrija o HTML no Stage 04 → `node [session].js` → re-gere thumbnails → verifique → marque resolvido no QA report.
