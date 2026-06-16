# Stage 03: Outline

Create a detailed slide-by-slide outline for each session in the curriculum.

## Inputs

| Source | File/Location | Section/Scope | Why |
|--------|--------------|---------------|-----|
| Previous stage | `../02-curriculum/output/[course-slug]-curriculum.md` | Full file | Session structure and content allocation |
| Previous stage | `../02-curriculum/output/[course-slug]-meta.md` | Full file | Course name, audience, session count |
| Shared | `../../shared/producer-identity.md` | Full file | Producer name |
| Template | `../../shared/course-meta.md` | Full file | Template for collecting course details (if entering here) |
| Design system | `../../design-system/CONTEXT.md` | Routes to palette, typography | Visual direction |
| Skill | `../../skills/pptx/SKILL.md` | Design principles, layout constraints | Slide layout rules |
| Skill | `../../skills/frontend-design/SKILL.md` | Full file | Design thinking, aesthetics |
| Reference | `references/slide-patterns.md` | Full file | Padrões assertion-evidence e formato do outline |
| Reference | `references/slide-structure-library.md` | Full file | Estruturas de slide curadas, por função (Merrill) |
| Methodology | `../../shared/methodology.md` | Full file | Regras Sweller/Mayer/Alley/Merrill |

## Process

1. If this is the entry stage (no Stage 02 output exists), collect course metadata from the user and write it to `output/[course-slug]-meta.md`. Also ask for the curriculum or have the user provide it directly.
2. Read the curriculum document
3. Load the design system via its CONTEXT.md
4. For each session in the curriculum:
   a. Determine slide count (target 15-25)
   b. Atribua a função pedagógica (Merrill) e escolha a estrutura em `references/slide-structure-library.md`
   c. Escreva o slide como **assertion-evidence**: título-afirmação + evidência visual (sem bullets)
   d. Add visual direction (variante Cefor, cor, chart/image needed)
   e. Flag any slide that needs a chart, table, or image (becomes a `class="placeholder"` in Stage 04)
5. Verify no single-column chart-below-text layouts (pptx SKILL.md constraint)
6. **[Checkpoint]** -- Present the outlines to the user. Ask: Do the slide flows make sense? Any slides to add, remove, or restructure?
7. Run the audit checks below. Rode `python ../../skills/qa/validate_outline.py output/[session-slug]-outline.md`. If any fail, revise before saving.
8. Save one outline file per session

## Checkpoints

| After Step | Agent Presents | Human Decides |
|------------|---------------|---------------|
| 5 | Complete slide outlines for all sessions with types, content, and visual direction | Whether slide flow, content density, and visual direction are right |

## Audit

| Check | Pass Condition |
|-------|---------------|
| Assertion-evidence | Todo slide de conteúdo tem título-afirmação + evidência (não bullets) |
| Estrutura declarada | Cada slide declara uma estrutura da biblioteca + função Merrill |
| Variedade de layout | Não mais que 2 slides consecutivos com a mesma estrutura |
| Densidade | ≤ ~40 palavras visíveis por slide (Sweller/Mayer) |
| Content completeness | Cada objetivo de aprendizagem é endereçado por ≥ 1 slide |
| validate_outline.py | O script passa (status pass) |

## Outputs

| Artifact | Location | Format |
|----------|----------|--------|
| Course metadata | `output/[course-slug]-meta.md` | Carried forward or newly collected |
| Session outlines | `output/[session-slug]-outline.md` (one per session) | Markdown: slide-by-slide with type, content, notes, visual direction |
