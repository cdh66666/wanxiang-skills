---
name: evidence-atlas-research
description: Create a visual, source-verifiable technical investigation from original patent figures, academic paper figures, official materials, and real teardown photographs. Use when investigating how a product, mechanism, device, competitor, or technology works; when the user asks for patents, papers, prior art, teardown evidence, mechanism structure, an evidence atlas, or a Chinese illustrated report; or when a text-only answer would be hard to understand. Especially useful for PDF-heavy research that must preserve authentic source images, map numbered parts to actions, distinguish fact from inference, and deliver a visually checked PDF or document.
---

# Evidence Atlas Research

Turn scattered technical sources into an illustrated evidence dossier that lets a reader understand the mechanism by following authentic figures, short annotations, and explicit confidence labels.

## Non-negotiable rules

- Prefer primary evidence: granted/published patents, peer-reviewed papers, standards, official manuals, regulatory filings, and manufacturer material.
- Use original figures and real photographs. Do not redraw, beautify, or synthesize a substitute unless the user explicitly asks for one; label any reconstruction prominently.
- Preserve figure numbers and visible callouts. Cropping blank margins, rotating, scaling, and improving legibility are allowed when they do not alter evidence.
- Never imply that a patent embodiment proves the shipped product uses the same implementation.
- Mark every important claim as **confirmed**, **patent embodiment**, **reported by a secondary source**, or **inference**.
- Distinguish an exact product teardown from a related platform or adjacent model.
- Put citations next to the figure or claim they support, not only in a bibliography.

Read [references/evidence-standards.md](references/evidence-standards.md) before selecting sources. Read [references/dossier-spec.md](references/dossier-spec.md) before composing the final artifact.

## Workflow

### 1. Lock the investigation target

Record the exact product, generation, year, variant, region, and the mechanism question. Resolve ambiguous marketing names before collecting evidence. State unavoidable uncertainty early.

### 2. Build a source matrix

Search broadly, then promote primary sources. Track title, owner/author, publication number or DOI, date, URL, evidence type, exact-product relevance, useful figure/page, and reuse notes. Group patent family members so the same disclosure is not counted repeatedly.

Use this priority order:

1. Patent full text and drawings from an official patent office or Google Patents.
2. Peer-reviewed paper or author-hosted manuscript.
3. Official manual, filing, launch material, or technical support page.
4. Credible teardown, repair, or engineering analysis with original photographs.
5. News and commentary only for leads or context.

### 3. Download and inspect whole documents

Do not select figures from snippets alone. Download the full PDF, render candidate pages, and inspect surrounding text, figure captions, and reference numerals. Use `scripts/render_pdf_pages.py` to turn chosen PDF pages into PNGs and optionally a contact sheet.

### 4. Select figures by explanatory job

Choose the smallest set that answers these questions:

- What are the main physical parts and where are they located?
- What transmits force, motion, power, or information?
- What changes from rest to tighten/engage and loosen/release?
- What senses state, prevents overload, or permits manual override?
- Which observations come from an actual teardown?

Prefer complementary views—system layout, section/exploded view, action sequence, electrical/control diagram, and real hardware—over many near-duplicate figures.

### 5. Create the visual explanation

For each figure, include a compact caption block:

- **Source identity:** document title, patent/publication/DOI, figure and page.
- **Look here:** the two or three numbered features the reader should notice.
- **What happens:** one short cause-and-effect explanation.
- **Evidence status:** one of the four labels above.
- **Boundary:** what the figure cannot prove.

When several figures describe a sequence, order them by mechanism state rather than source order. Define each reference numeral once, then use the same Chinese term consistently.

### 6. Synthesize without overclaiming

Separate observations from interpretation. If a teardown photo and patent drawing appear to correspond, describe the mapping as an inference unless a primary source explicitly confirms it. List plausible alternatives when evidence is incomplete.

### 7. Render and visually verify

Render the final PDF/document to images and inspect every page at readable size. Check for missing images, tiny labels, clipped captions, incorrect page references, broken links, duplicated figures, and captions separated from their images. Iterate until the artifact is understandable without relying on a long prose appendix.

### 8. Deliver reproducibly

Provide the final artifact, the source list with direct links, a short findings summary, and an uncertainty list. Keep downloaded sources and a source matrix when the workspace permits so another researcher can reproduce the dossier.

## Stop conditions

Pause and explain the limitation when the exact product cannot be identified, the only available image is an unattributed repost, a paywall prevents verification of the referenced figure, or copyright/terms prohibit the requested reproduction. Continue with lawful alternatives such as patent drawings, official previews, links, or concise paraphrase.
