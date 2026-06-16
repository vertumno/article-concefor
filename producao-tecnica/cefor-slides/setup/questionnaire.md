# Onboarding — Cefor Slides

Leia este arquivo quando o usuário digitar "setup". Faça TODAS as perguntas em uma única passada conversacional. Elas configuram o sistema de produção — não um curso específico (os detalhes do curso são coletados no início de cada run).

---

### Q1: Nome ou organização que aparece nos decks?
- Arquivo: `shared/producer-identity.md`
- Tipo: texto livre. Default: Cefor.

### Q2: Variante visual do Cefor (padrão)?
- Arquivo: `design-system/palette.md`
- Tipo: seleção. Default: **Sólida**.
- Opções:
  - **Sólida (institucional):** azul 314A99 + oliva A3A51A + grená 980000 (fundo claro EEEEEE).
  - **Degradê:** teal 134F5C → 08A18E (fundo branco).
- Obs.: as cores vêm dos templates oficiais (`referencias/CEFOR Apresentação *.pptx`). Pode-se alternar por deck.

### Q3: Fonte?
- Arquivo: `design-system/typography.md`
- Default: **Arial / Arial** (padrão dos templates Cefor; web-safe). Mudar só se necessário.

### Q4: Modo padrão de trabalho?
- Arquivo: `shared/producer-identity.md`
- Tipo: seleção. Default: **Modo 2 (Design pedagógico)**.
- Opções:
  - **Modo 1 — Produção:** trago conteúdo pronto, quero slides assertion-evidence no padrão Cefor (entra no Stage 03).
  - **Modo 2 — Design pedagógico:** trago tema/conceitos, quero a sequência instrucional desenhada (entra no Stage 02).

### Q5: Tipo de material-fonte habitual?
- Arquivo: `shared/producer-identity.md`
- Tipo: texto livre. Ex.: "artigos e PDFs", "minhas notas de aula", "ementa do curso".

### Q6: Onde costuma começar no pipeline?
- Arquivo: `shared/producer-identity.md`
- Tipo: seleção.
  - **Do zero** — material bruto, preciso de tudo (Stage 01).
  - **De notas** — conteúdo organizado, pula extração (Stage 02).
  - **De uma ementa** — já tenho currículo, só quero decks (Stage 03).

---

## Depois do onboarding

Diga ao usuário:

"Configurado. Seu config de produção:
- **Identidade:** [nome]
- **Visual:** variante [Sólida|Degradê], Arial
- **Modo padrão:** [1|2]
- **Início padrão:** Stage [01|02|03]

Para começar, diga o que quer construir e forneça o material (ou o tema/conceitos). Coleto os detalhes do curso (nome, público, nº de sessões) no início de cada run."

Depois, varra o workspace por `{{` remanescentes. Se houver, peça a informação que falta.
