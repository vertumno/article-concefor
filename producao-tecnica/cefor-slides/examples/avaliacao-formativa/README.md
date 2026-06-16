# Exemplo: Avaliação Formativa (deck de demonstração)

Evidência de funcionamento do `cefor-slides` ponta a ponta (Modo 2 — design pedagógico). Serve de prova de resultado para o artigo e de figura para a produção técnica.

## O que demonstra

- **Pipeline glass-box (ICM):** cada estágio é um arquivo legível e editável.
  - `01-extraction.md` — conteúdo estruturado e tagueado.
  - `02-curriculum.md` — arco instrucional (Merrill) + objetivos (Bloom).
  - `03-outline.md` — slides assertion-evidence (Alley).
- **Metodologia → regra visível:**
  - **Alley:** todo slide = título-afirmação + evidência visual (sem bullets).
  - **Sweller/Mayer:** baixa densidade, 1 ideia/slide, sinalização, contiguidade, notas ≠ tela.
  - **Merrill:** arco activation → demonstration → application → integration.
- **Design system Cefor (variante Sólida):** azul `#314A99`, oliva `#A3A51A`, grená `#980000`, Arial, rodapé `cefor.ifes.edu.br`.

## Arquivos

| Arquivo | O que é |
|---------|---------|
| `01-extraction.md` / `02-curriculum.md` / `03-outline.md` | Artefatos do pipeline (Stages 01–03) |
| `build_example.py` | Gerador: mesmos dados → `.pptx` (editável) + PNGs (figuras) |
| `avaliacao-formativa.pptx` | **Deck entregável** (9 slides, 16:9, com notas do apresentador) |
| `thumbs/slide-NN.png` | Pré-visualização de cada slide |

## Regerar

```bash
python build_example.py
```

Requer `python-pptx` e `Pillow`. As cores/fonte vêm de `../../design-system/`.

## Validação (QA automático)

Ambos os validadores de `skills/qa/` passam neste exemplo:

```bash
python ../../skills/qa/validate_outline.py 03-outline.md   # status: pass | slides: 9
python ../../skills/qa/check_pptx.py avaliacao-formativa.pptx  # status: pass | slides: 9
```

## Nota técnica

Este exemplo usa `python-pptx` (formas nativas) por robustez no ambiente. O motor primário do workspace é o `html2pptx` da skill `pptx` (fidelidade total ao template `.pptx` Cefor); ambos consomem o mesmo outline do Stage 03.
