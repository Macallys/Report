"""
Convierte tablas Markdown a tablas HTML en los .md fuente del informe.
No toca docs/informe.md (se regenera con build-informe.py).
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

SKIP = {"informe.md"}


def split_row(line: str) -> list[str]:
    line = line.strip()
    if line.startswith("|"):
        line = line[1:]
    if line.endswith("|"):
        line = line[:-1]
    return [c.strip() for c in line.split("|")]


def is_separator(line: str) -> bool:
    cells = split_row(line)
    if not cells:
        return False
    return all(re.fullmatch(r":?-{3,}:?", c.replace(" ", "")) for c in cells if c)


def alignment(sep_cells: list[str]) -> list[str]:
    aligns: list[str] = []
    for c in sep_cells:
        c = c.strip()
        left = c.startswith(":")
        right = c.endswith(":")
        if left and right:
            aligns.append("center")
        elif right:
            aligns.append("right")
        else:
            aligns.append("left")
    return aligns


def to_html(header: list[str], rows: list[list[str]], aligns: list[str]) -> str:
    lines = [
        '<table>',
        '  <thead>',
        '    <tr>',
    ]
    for i, cell in enumerate(header):
        align = aligns[i] if i < len(aligns) else "left"
        lines.append(f'      <th align="{align}">{cell}</th>')
    lines.extend(
        [
            '    </tr>',
            '  </thead>',
            '  <tbody>',
        ]
    )
    for row in rows:
        lines.append('    <tr>')
        for i, cell in enumerate(row):
            align = aligns[i] if i < len(aligns) else "left"
            # pad missing cells
            lines.append(f'      <td align="{align}">{cell}</td>')
        # if row shorter than header, add empty cells
        for i in range(len(row), len(header)):
            align = aligns[i] if i < len(aligns) else "left"
            lines.append(f'      <td align="{align}"></td>')
        lines.append('    </tr>')
    lines.extend(
        [
            '  </tbody>',
            '</table>',
        ]
    )
    return "\n".join(lines)


def convert_text(text: str) -> tuple[str, int]:
    lines = text.splitlines()
    out: list[str] = []
    i = 0
    count = 0
    in_fence = False

    while i < len(lines):
        line = lines[i]
        if line.strip().startswith("```"):
            in_fence = not in_fence
            out.append(line)
            i += 1
            continue

        if (
            not in_fence
            and line.strip().startswith("|")
            and i + 1 < len(lines)
            and is_separator(lines[i + 1])
        ):
            header = split_row(line)
            sep = split_row(lines[i + 1])
            aligns = alignment(sep)
            i += 2
            rows: list[list[str]] = []
            while i < len(lines) and lines[i].strip().startswith("|") and not is_separator(lines[i]):
                rows.append(split_row(lines[i]))
                i += 1
            out.append(to_html(header, rows, aligns))
            count += 1
            continue

        out.append(line)
        i += 1

    new_text = "\n".join(out)
    if text.endswith("\n"):
        new_text += "\n"
    return new_text, count


def iter_targets() -> list[Path]:
    files: list[Path] = []
    for path in DOCS.rglob("*.md"):
        if path.name in SKIP:
            continue
        files.append(path)
    readme = ROOT / "README.md"
    if readme.exists():
        files.append(readme)
    return sorted(files)


def main() -> None:
    total = 0
    for path in iter_targets():
        original = path.read_text(encoding="utf-8")
        converted, n = convert_text(original)
        if n and converted != original:
            path.write_text(converted, encoding="utf-8")
            print(f"{path.relative_to(ROOT)}: {n} tabla(s)")
            total += n
        elif n == 0:
            pass
    print(f"Total: {total} tablas convertidas")


if __name__ == "__main__":
    main()
