# Slide Patterns — Assertion-Evidence (Cefor)

Padrões de slide para decks instrucionais do Cefor. **Regra-mãe (Alley):** todo slide de conteúdo tem **título = afirmação** (frase completa, a tese do slide) e **corpo = evidência visual** (imagem, gráfico, diagrama, esquema) — **não** lista de bullets. Ver `shared/methodology.md`.

## O que muda em relação ao modelo de bullets

| ❌ Padrão tópico+bullets | ✅ Assertion-Evidence |
|--------------------------|------------------------|
| Título: "Avaliação formativa" | Título: "A avaliação formativa redireciona o ensino durante o percurso" |
| Corpo: 6 bullets de texto | Corpo: um diagrama do ciclo feedback→ajuste |

A skill **recusa por padrão** o slide título-genérico + parede de bullets (carga extrínseca — Sweller).

## Biblioteca de padrões

### title-slide
**Quando:** 1º slide da sessão. **Layout:** capa no design Cefor (Sólida ou Degradê). **Conteúdo:** nome do curso, título da sessão, objetivo de aprendizagem em 1 linha.

### assertion-visual *(padrão principal de conteúdo)*
**Quando:** ensinar qualquer conceito. **Layout:** título-afirmação no topo (1–2 linhas) + uma evidência visual dominante abaixo. **Conteúdo:** 1 afirmação + 1 visual. Rótulos curtos junto ao visual (contiguidade — Mayer). Sem bullets.

### assertion-comparison
**Quando:** contrastar duas ideias/abordagens. **Layout:** título-afirmação + duas colunas visuais (lado a lado). **Conteúdo:** a afirmação já diz o veredito; as colunas mostram a evidência do contraste.

### assertion-process
**Quando:** mostrar um processo/sequência. **Layout:** título-afirmação + diagrama de etapas (setas/numeração visual). **Conteúdo:** etapas como blocos visuais, não lista textual.

### assertion-data
**Quando:** sustentar a afirmação com dados. **Layout:** título-afirmação + gráfico. **Conteúdo:** o gráfico É a evidência; uma frase de interpretação junto. Marcar área como `class="placeholder"` no Stage 04.

### definition
**Quando:** introduzir um termo. **Layout:** termo em destaque + significado curto + 1 exemplo concreto/visual. **Conteúdo:** 1 termo por slide.

### key-metric
**Quando:** destacar 1 número decisivo. **Layout:** número grande (44–66pt) + rótulo curto + fonte. **Conteúdo:** 1 número, 1 rótulo.

### activation *(Merrill — ativação)*
**Quando:** abertura de tópico, conectar ao que o aluno já sabe. **Layout:** pergunta-afirmação + imagem/situação evocativa. **Conteúdo:** provoca recuperação do conhecimento prévio.

### application *(Merrill — aplicação)*
**Quando:** o aluno pratica. **Layout:** título-tarefa + enunciado da atividade/caso. **Conteúdo:** consigna clara do que fazer.

### section-divider
**Quando:** transição entre tópicos. **Layout:** bloco de cor Cefor, título de seção (pode ser rótulo aqui). **Conteúdo:** só o nome da seção.

### summary-slide *(Merrill — integração)*
**Quando:** fechamento. **Layout:** título-afirmação de síntese + 3 evidências-chave (visuais/ícones). **Conteúdo:** retoma o objetivo de aprendizagem.

### end-slide
**Quando:** último slide. **Layout:** capa Cefor minimal. **Conteúdo:** nome do curso, sessão, contato/continuidade.

## Formato do outline (por slide)

```markdown
### Slide [N]: [título-afirmação completo]
- **Pattern:** [nome do padrão]
- **Função (Merrill):** activation | demonstration | application | integration | —
- **Assertion:** [a frase-tese do slide]
- **Evidence:** [qual visual sustenta — imagem/gráfico/diagrama/esquema]
- **Speaker notes:** [o que o apresentador fala — 2–4 frases; NÃO repetir o que está na tela]
- **Visual:** [variante Cefor, cor, flag de chart/image se necessário]
```

## Audit do outline (Alley + Mayer + Sweller)

- [ ] Todo título de conteúdo é uma **afirmação** (não rótulo-tópico).
- [ ] Todo corpo é **evidência visual** (não lista de bullets).
- [ ] ≤ ~40 palavras visíveis por slide (exceto tabela/anexo).
- [ ] Notas ≠ texto da tela (sem redundância).
- [ ] Variedade de layout: não mais que 2 slides seguidos com a mesma estrutura.
