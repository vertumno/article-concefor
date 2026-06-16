# Stage 05: QA and Delivery

Visually validate generated decks, fix issues, and package for delivery.

## Inputs

| Source | File/Location | Section/Scope | Why |
|--------|--------------|---------------|-----|
| Previous stage | `../04-generation/output/[session-slug]/` | .pptx files and JS source | Decks to validate and fix |
| Design system | `../../design-system/CONTEXT.md` | Routes to palette, typography | Check design compliance |
| Skill | `../../skills/pptx/SKILL.md` | "Creating Thumbnail Grids" and "Converting Slides to Images" sections | Thumbnail generation commands |
| Skill | `../../skills/frontend-design/SKILL.md` | Full file | Validate design quality |
| Reference | `references/qa-checklist.md` | Full file | Rubrica pedagógica (4 camadas) + visual/marca |
| Reference | `references/anti-patterns.md` | Full file | Slides que não ensinam (sinais + correções) |
| Methodology | `../../shared/methodology.md` | Full file | Regras Sweller/Mayer/Alley/Merrill |
| Scripts | `../../skills/qa/` | validate_outline.py, check_pptx.py | Checagem automática |

## Process

1. Rode os validadores automáticos primeiro:
   - `python ../../skills/qa/validate_outline.py ../03-outline/output/[session]-outline.md`
   - `python ../../skills/qa/check_pptx.py ../04-generation/output/[session]/[session].pptx`
2. For each session .pptx:
   a. Generate thumbnail grid: `python ../../skills/pptx/scripts/thumbnail.py [session].pptx [session]-thumbnails`
   b. Or convert to PDF + images: `soffice --headless --convert-to pdf [session].pptx` then `pdftoppm -jpeg -r 150 [session].pdf slide`
3. Inspecione cada thumbnail com `qa-checklist.md` e `anti-patterns.md`
4. If issues found:
   a. Fix the HTML source file for the broken slide
   b. Re-run the JS file: `node [session].js`
   c. Re-generate thumbnails
   d. Repeat until clean
5. Collect all passing .pptx files into `output/final/`
6. Write the delivery manifest and QA report (use o template de scoring em `qa-checklist.md`)
7. Present final decks to user for approval

## Outputs

| Artifact | Location | Format |
|----------|----------|--------|
| QA report | `output/qa-report.md` | Pass/fail per session, issues found and fixed |
| Final decks | `output/final/` | All validated .pptx files |
| Delivery manifest | `output/delivery-manifest.md` | Session list with slide counts and file sizes |
