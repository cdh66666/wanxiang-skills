#!/usr/bin/env python3
"""Render selected PDF pages with pdftoppm and optionally build a contact sheet."""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path


def parse_pages(spec: str) -> list[int]:
    pages: set[int] = set()
    for token in spec.split(","):
        token = token.strip()
        if not token:
            continue
        if "-" in token:
            start_text, end_text = token.split("-", 1)
            start, end = int(start_text), int(end_text)
            if start < 1 or end < start:
                raise ValueError(f"Invalid page range: {token}")
            pages.update(range(start, end + 1))
        else:
            page = int(token)
            if page < 1:
                raise ValueError(f"Invalid page number: {token}")
            pages.add(page)
    if not pages:
        raise ValueError("No pages selected")
    return sorted(pages)


def find_pdftoppm(override: Path | None) -> str:
    if override:
        if not override.is_file():
            raise ValueError(f"pdftoppm not found: {override}")
        return str(override)

    discovered = shutil.which("pdftoppm")
    if not discovered:
        raise ValueError("pdftoppm was not found on PATH; install Poppler or use --pdftoppm")

    # Codex on Windows may expose a .cmd shim while the real Poppler binary is
    # stored in the same bundled dependency tree. Prefer the executable because
    # subprocess argument forwarding through batch shims is not always reliable.
    discovered_path = Path(discovered)
    if discovered_path.suffix.lower() in {".cmd", ".bat"}:
        dependency_root = discovered_path.parent.parent.parent
        bundled_exe = dependency_root / "native" / "poppler" / "Library" / "bin" / "pdftoppm.exe"
        if bundled_exe.is_file():
            return str(bundled_exe)
    return discovered


def render_page(executable: str, pdf: Path, page: int, out_dir: Path, dpi: int) -> Path:
    prefix = out_dir / f"page-{page:04d}"
    command = [executable, "-f", str(page), "-l", str(page), "-r", str(dpi), "-png", "-singlefile", str(pdf), str(prefix)]
    subprocess.run(command, check=True)
    return prefix.with_suffix(".png")


def build_contact_sheet(images: list[Path], output: Path, columns: int) -> None:
    try:
        from PIL import Image, ImageDraw
    except ImportError as exc:
        raise RuntimeError("Contact sheets require Pillow: python -m pip install pillow") from exc

    opened = [Image.open(path).convert("RGB") for path in images]
    thumb_width = 900
    label_height = 48
    thumbs = []
    for path, img in zip(images, opened):
        ratio = thumb_width / img.width
        thumbs.append((path.name, img.resize((thumb_width, round(img.height * ratio)))))

    rows = (len(thumbs) + columns - 1) // columns
    cell_height = max(img.height for _, img in thumbs) + label_height
    sheet = Image.new("RGB", (columns * thumb_width, rows * cell_height), "white")
    draw = ImageDraw.Draw(sheet)
    for index, (label, img) in enumerate(thumbs):
        x = (index % columns) * thumb_width
        y = (index // columns) * cell_height
        sheet.paste(img, (x, y + label_height))
        draw.text((x + 12, y + 12), label, fill="black")
    output.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(output)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pdf", type=Path, help="Source PDF")
    parser.add_argument("--pages", required=True, help="1-based pages, for example 1,3-5,9")
    parser.add_argument("--out", type=Path, required=True, help="Output directory")
    parser.add_argument("--dpi", type=int, default=180)
    parser.add_argument("--contact-sheet", type=Path)
    parser.add_argument("--columns", type=int, default=3)
    parser.add_argument("--pdftoppm", type=Path, help="Optional path to the Poppler executable")
    args = parser.parse_args()

    if not args.pdf.is_file():
        parser.error(f"PDF not found: {args.pdf}")
    if args.dpi < 72 or args.dpi > 600:
        parser.error("--dpi must be between 72 and 600")
    if args.columns < 1:
        parser.error("--columns must be positive")

    try:
        executable = find_pdftoppm(args.pdftoppm)
        pages = parse_pages(args.pages)
        args.out.mkdir(parents=True, exist_ok=True)
        rendered = [render_page(executable, args.pdf, page, args.out, args.dpi) for page in pages]
        if args.contact_sheet:
            build_contact_sheet(rendered, args.contact_sheet, args.columns)
    except (ValueError, RuntimeError, subprocess.CalledProcessError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    for path in rendered:
        print(path)
    if args.contact_sheet:
        print(args.contact_sheet)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
