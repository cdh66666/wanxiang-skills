---
name: evidence-atlas-research
description: Research mechanical structures, mechanisms, products, robots, patents, papers, prior art, and teardown evidence, then create a Chinese visual evidence atlas using authentic source figures and concise accurate annotations. Use when the user asks to 调研结构、机构原理、专利图纸、仿生机器人、竞品拆解、机械方案、3D打印参考, or says pictures are more useful than long text. Default to separate visual booklets for distinct objects, large original figures, three-line per-figure explanations, embedded source links, and rendered-page QA.
---

# Evidence Atlas Research

Create a mechanism atlas that can be understood from the figures without reading a long report.

## Required behavior

- Prefer authentic patent drawings, paper figures, official diagrams, and exact-product teardown photographs.
- Keep original reference numerals and figure labels. Crop margins or improve legibility only; never silently redraw evidence.
- Separate distinct objects or species into different deliverables unless the user requests one combined file.
- Use images as the main content. Avoid a parallel long narrative report unless requested.
- Distinguish source fact from engineering advice. Never guess a component function from appearance alone.
- Put the direct source link beside each patent/source group.
- Treat patent status as a search clue, not legal advice.

Read [references/evidence-standards.md](references/evidence-standards.md) before annotating. Read [references/dossier-spec.md](references/dossier-spec.md) before building the deliverable.

## Choose one mode

### Structure atlas mode — default

Use for mechanism research, patent drawing surveys, robot structures, and 3D-printing references.

- Collect many relevant authentic drawings.
- Explain each extracted drawing page with exactly three compact fields:
  1. **图示：** what is visibly shown or identified by the source.
  2. **运动/作用：** input → transmission → output; if static, say that the figure only shows assembly or location.
  3. **样机借鉴：** a clearly labeled engineering suggestion, not a patent fact.
- Place two large figures per page by default. Use one when labels would otherwise be unreadable.
- Label extracted images as **图纸页 N** when one image may contain multiple original figures. Refer to the visible `FIG.`/`图号` inside the image for the official figure number.

### Full evidence mode — only when needed

Use when the user asks for a product conclusion, scientific evidence chain, standards comparison, freedom-to-operate lead, or teardown-to-patent mapping. Add papers, standards, manuals, teardown photographs, confidence labels, findings, and uncertainty. Do not force this longer mode onto a patent-picture request.

## Efficient workflow

1. **Split the target.** Decide the booklet boundaries first: species, product family, mechanism class, or medium. Put shared subsystems only in the most relevant booklet and state where they went.
2. **Find distinct primary sources.** Search patents and authoritative sources; collapse patent families and remove near-duplicates. Prefer sources that add a new mechanism view.
3. **Verify only what is needed.** Download the full source, but read the abstract, figure list, relevant detailed-description passages, claims needed for boundaries, and legal-status source. Do not summarize the whole document.
4. **Extract authentic figures.** Preserve original images and maintain a manifest mapping source → extracted image → visible figure number/page.
5. **Annotate from evidence.** Write the three fields only after checking the figure description and surrounding text. If the source does not establish motion, write “本图不显示/不单独说明运动”.
6. **Build the atlas.** Use `scripts/build_annotated_atlas.py` with a JSON manifest when producing DOCX. Use `scripts/render_pdf_pages.py` when source PDF pages must be rasterized.
7. **Verify directly.** Check annotation/image counts, links, figure mapping, and file integrity. Render the final document, inspect every page, fix clipping or unreadable labels, and rerender once if changed.
8. **Deliver only finals.** Return the requested booklet(s). Keep source PDFs, extracted figures, manifests, QA PDFs, and contact sheets as internal work files unless requested.

## Source selection

Use the smallest source set that gives broad structural coverage:

1. Patent publication/grant and drawings.
2. Peer-reviewed paper or institutional project page when it adds biomechanics, validation, or a different mechanism.
3. Official manual, standard, filing, or manufacturer material.
4. Exact-product teardown or repair evidence.
5. Secondary commentary only as a lead.

For a drawing-heavy request, do not delay delivery merely to fill every evidence category. State missing evidence briefly.

## Annotation accuracy gate

Before accepting a caption, confirm:

- The subject and view match the image.
- The motion sentence is supported by the description, claim, caption, or visible kinematic relation.
- “样机借鉴” is feasible advice and is not written as the patent's own design.
- Composite extraction pages are not mislabeled as a single official patent figure.
- Irrelevant accessories are labeled as non-core instead of being assigned an invented role.
- Terms for the same numbered part remain consistent across pages.

## Layout defaults

- Chinese DOCX, Letter portrait, compact reference-guide styling.
- Cover + short source index + source-group pages.
- Two figures per page, large white figure area, short annotation beneath each.
- Each source heading shows publication number, title, status clue, and direct link.
- No separate bibliography when every source group already carries its direct link, unless requested.
- No repeated executive summary, learning path, BOM, or generic theory section unless it directly answers the request.

## Stop conditions

Pause or label the limitation when the exact object cannot be identified, the figure is an unattributed repost, the source text cannot verify the proposed function, the page/figure mapping is uncertain, or reproduction is prohibited. Continue with lawful alternatives and never fill gaps with confident-sounding guesses.
