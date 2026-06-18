# Linguagens Visuais Cefor (Versão A e Versão B)

> O Cefor tem **duas linguagens visuais oficiais** para apresentações. Não invente estilos: escolha
> entre A e B. Ambas usam a mesma paleta, fonte (Open Sans) e elementos de marca — ver
> [CEFOR_BRAND.md](CEFOR_BRAND.md). Os modelos são desenhados em **1920×1080 (16:9)**.
>
> Na fase "mostrar, não contar", gere **2 prévias** (uma da Versão A e uma da Versão B) com o
> slide-título real do deck para a pessoa escolher a linguagem. Não misture A e B no mesmo deck.

---

## Versão A — Cor Sólida

**Clima:** sóbria, institucional, alta legibilidade. Lima + azul sobre branco/cinza. Ótima para
reuniões, prestação de contas, comitês, comunicados e materiais informativos.

**Assinatura:** painéis chapados em lima e cinza com cantos arredondados; **seta CEFOR** em azul como
acento; números de seção grandes em lima; barra de título lima com texto tinta; bullets quadrados lima;
linha-guia e URL em oliva no rodapé.

```css
:root { --slide-bg: #FFFFFF; --panel: var(--lime); --rail: var(--gray);
        --title: var(--navy); --accent: var(--navy); --footer: var(--olive); }
```

**5 modelos oficiais:**

| ID | Modelo | Layout-resumo |
|----|--------|---------------|
| **A1** | Capa | Bloco lima no topo (canto inf-esq. arredondado grande); moldura oliva; seta lima d'água; eyebrow MAIÚSCULAS, título branco 800, subtítulo; logo IFES no canto inf-direito. |
| **A2** | Divisória de seção | Trilho lima à esquerda (34%) com marca d'água de setas; seta azul; número "01" lima 80px; título da seção em azul; sublinhado lima; linha oliva + URL no rodapé. |
| **A3** | Conteúdo com lista | Trilho cinza à esquerda (30%) com marca d'água; seta azul; barra de título lima (texto tinta) + sublinhado azul com "tique"; lista com bullets quadrados lima; linha oliva + URL. |
| **A4** | Destaque / citação | Cantos lima (sup-esq) e azul (inf-esq); linha vertical oliva; painel cinza à direita; aspas lima grandes; frase em azul 700; atribuição em texto médio. |
| **A5** | Encerramento | Trilho lima; seta azul; "Obrigado!" em azul 800; logo IFES; ícones sociais (badges tinta). |

---

## Versão B — Degradê

**Clima:** moderna, vibrante, marcante. Malha verde-ciano-azul com grafismos geométricos. Ótima para
eventos, aberturas, lançamentos, palestras e telas grandes.

**Assinatura:** fundo (ou trilho) com o **degradê CEFOR**; grafismos em branco translúcido (quadrados
arredondados em contorno, círculos concêntricos, linha pontilhada); seta/ logo em negativo (branco);
barra de título em degradê com texto branco; bullets quadrados ciano; URL em oliva no rodapé.

```css
:root { --slide-bg: var(--grad); --panel: var(--grad); --rail: var(--gray);
        --title: #1f3a52; --accent: #36B4A6; --footer: var(--olive); }
```

**5 modelos oficiais:**

| ID | Modelo | Layout-resumo |
|----|--------|---------------|
| **B1** | Capa | Fundo degradê inteiro; grafismos brancos (quadrados em contorno + círculos concêntricos + linha pontilhada); eyebrow, título branco 800 (sombra leve), subtítulo; logo IFES branco no canto inf-esq. |
| **B2** | Capa com barra lateral | Fundo degradê + trilho cinza-claro à esquerda (23%) com logo e ícones sociais; título branco à direita; barra de legenda branca translúcida (autoria/data). |
| **B3** | Divisória de seção | Trilho degradê à esquerda (34%) com grafismos; número "02" claro 80px; título da seção em azul-escuro; sublinhados verde + azul; URL oliva. |
| **B4** | Conteúdo com lista | Trilho cinza com grafismos esverdeados; barra de título em degradê (texto branco) + sublinhado tinta com "tique"; bullets quadrados ciano; URL oliva. |
| **B5** | Encerramento | Trilho degradê com grafismos; "Obrigado!" em azul-escuro 800; logo IFES; ícones sociais (badges azul). |

---

## Como escolher por ocasião

| Ocasião | Linguagem sugerida | Densidade |
|---------|--------------------|-----------|
| Reunião / decisão | **A** (Cor Sólida) | Média |
| Prestação de contas / comitê / relatório | **A** (Cor Sólida) | Alta |
| Comunicado / material informativo (para ler) | **A** (Cor Sólida) | Média–Alta |
| Evento, abertura, lançamento, palestra | **B** (Degradê) | Baixa |
| Comunicação institucional vibrante / telas grandes | **B** (Degradê) | Baixa |

> Os 10 modelos cobrem capa, divisória, conteúdo, destaque/citação e encerramento. Slides de **dados**
> (KPI, gráfico, tabela, linha do tempo) são construídos **estendendo o modelo de Conteúdo** (A3/B4) na
> mesma linguagem — mantendo barra de título, trilho lateral, bullets e rodapé. Ver
> [slide-patterns/slide-patterns.md](slide-patterns/slide-patterns.md).
