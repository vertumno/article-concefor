# skills/qa — validadores automáticos

Scripts determinísticos que verificam regras da metodologia (Sweller/Mayer/Alley/Merrill) sem julgamento subjetivo. Usados no Stage 05 (e podem rodar no Stage 03).

> Portados/adaptados da skill `slide-creator` (`validate_deck_package.py`, `check_pptx_placeholders.py`).

## validate_outline.py
Valida um outline (Stage 03) contra Assertion-Evidence.

```bash
python skills/qa/validate_outline.py stages/03-outline/output/[sessao]-outline.md
```
Verifica: todo slide tem Pattern; conteúdo tem Assertion + Evidence; Assertion não é rótulo genérico; ≤2 patterns consecutivos iguais; nota ≠ título; 1º=title, último=end. Sai 0 (pass) / 1 (fail). `--json` para relatório.

## check_pptx.py
Checagem técnica de um `.pptx` gerado (Stage 04/05).

```bash
python skills/qa/check_pptx.py examples/avaliacao-formativa/avaliacao-formativa.pptx
```
Verifica: placeholders residuais (`{{ }}`, `[INSTRUCTOR_NAME]`…); contagem de slides; slides sem texto. Sai 0/1. `--json` para relatório.

## Requisitos
Apenas biblioteca padrão do Python 3. Sem dependências externas.
