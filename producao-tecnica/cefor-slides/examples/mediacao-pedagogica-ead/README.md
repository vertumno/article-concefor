# Exemplo: Mediação Pedagógica na EaD (deck de demonstração)

Segundo deck de evidência do `cefor-slides`, agora no **design system v2** e em **deck misto** (Modo 2 — design pedagógico). Demonstra o pipeline ponta a ponta e a identidade visual atualizada do Cefor. Serve de prova de resultado para o artigo e de figura para a produção técnica.

## O que demonstra

- **Pipeline glass-box (ICM):** cada estágio é um arquivo legível e editável.
  - `01-extraction.md` — conteúdo estruturado e tagueado.
  - `02-curriculum.md` — arco instrucional (Merrill) + objetivos (Bloom).
  - `03-outline.md` — slides assertion-evidence (Alley).
- **Metodologia → regra visível:**
  - **Alley:** todo slide = título-afirmação + evidência visual (sem bullets).
  - **Sweller/Mayer:** baixa densidade, 1 ideia/slide, sinalização, contiguidade, notas ≠ tela.
  - **Merrill:** arco activation → demonstration → application → integration.
- **Design system Cefor v2 — deck misto:**
  - **Capa, divisórias e encerramento em Degradê (Versão B):** malha verde → ciano → azul, grafismos geométricos.
  - **Conteúdo em Sólida (Versão A):** **lima `#B0CB1F` como cor primária**, **seta CEFOR azul** na barra lateral cinza, marca d'água de setas, talão lima nos cards.
  - **Marca:** logo IF/ES (grid verde + círculo vermelho), Open Sans, rodapé oliva `cefor.ifes.edu.br`.

> Fonte canônica do visual: [`../../design-system/CEFOR-Design-System.dc.html`](../../design-system/CEFOR-Design-System.dc.html), `palette.md` e `typography.md`.

## Arquivos

| Arquivo | O que é |
|---------|---------|
| `01-extraction.md` / `02-curriculum.md` / `03-outline.md` | Artefatos do pipeline (Stages 01–03) |
| `build_example.py` | Gerador: mesmos dados → `.pptx` (editável) + PNGs (figuras) |
| `mediacao-pedagogica-ead.pptx` | **Deck entregável** (11 slides, 16:9, com notas do apresentador) |
| `thumbs/slide-NN.png` | Pré-visualização de cada slide |

## Regerar

```bash
python build_example.py
```

Requer `python-pptx` e `Pillow`. As cores/fonte vêm de `../../design-system/`.

## Validação (QA automático)

Ambos os validadores de `skills/qa/` passam neste exemplo:

```bash
python ../../skills/qa/validate_outline.py 03-outline.md            # status: pass | slides: 11
python ../../skills/qa/check_pptx.py mediacao-pedagogica-ead.pptx   # status: pass | slides: 11
```

## Nota técnica

Este exemplo usa `python-pptx` (formas nativas) por robustez no ambiente, espelhando os mesmos dados em PNG (Pillow) para as figuras. No `.pptx`, dois elementos da marca são **aproximados** por robustez de edição: a **seta CEFOR** vira um chevron rotacionado (no PNG ela usa o path oficial) e o **degradê** usa dois stops verde→azul (no PNG a malha tem quatro paradas). O motor primário do workspace continua sendo o `html2pptx` da skill `pptx` (fidelidade total ao design system), que consome o mesmo outline do Stage 03.
