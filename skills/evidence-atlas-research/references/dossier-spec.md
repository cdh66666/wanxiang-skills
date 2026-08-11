# Atlas deliverable specification

## Default: structure atlas

1. Cover: exact subject, “专利结构图解/证据图册”, source and figure counts.
2. Short index: one line per source with identifier, title, and drawing count.
3. Source groups: start each patent/source on a clean page; show status clue and direct link.
4. Figure panels: two per page by default, each with:
   - **图示：** source-supported identity of the view or assembly.
   - **运动/作用：** input, transmission, output, or an explicit statement that the view is static.
   - **样机借鉴：** engineering advice clearly separated from source fact.
5. Closing legal/evidence note: patent drawings are prior-art evidence, not a freedom-to-operate opinion.

When different objects, species, or product families would confuse the reader, create separate files. Put shared modules such as sealing or a common drivetrain in the booklet where they are actually used, then cross-reference that choice in the other booklet's index.

## Optional: full evidence mode

Add only when the question requires it:

- exact product identity and source map;
- patent family and timeline;
- papers or standards explaining principles and failure modes;
- exact-product teardown photographs;
- confirmed findings, patent-only possibilities, inference, and uncertainty;
- source register when links beside figures are insufficient.

## Figure handling

- Preserve the untouched source file.
- Keep visible patent numbers, `FIG.`/图号, callouts, arrows, legends, and scale bars.
- If an extracted image contains more than one official figure, call it **图纸页 N**, not “图 N”.
- If labels are unreadable at the intended size, enlarge to one figure per page or add a disclosed detail crop while retaining the full view.
- Do not put editorial arrows inside an original drawing unless clearly styled and disclosed.

## QA

- Figure count equals annotation count.
- Each caption belongs to the adjacent image and correct source.
- Direct links open and identifiers match.
- Source statements and prototype advice are visibly distinct.
- Final DOCX/PDF opens, renders, and has no clipping, blank spill pages, missing glyphs, or tiny unreadable labels.
- Inspect every rendered page; do not deliver QA PDFs/contact sheets unless requested.
