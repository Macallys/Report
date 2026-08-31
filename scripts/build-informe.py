"""
Ensambla el informe y regenera el índice con anclas estables.

Uso (desde la raíz del repo):
    python scripts/build-informe.py
"""

from __future__ import annotations

import re
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
README = ROOT / "README.md"
FRONT = DOCS / "00-student-outcome.md"
INFORME = DOCS / "informe.md"

TOC_START = "<!-- TOC:start -->"
TOC_END = "<!-- TOC:end -->"

CHAPTER_FILES = [
    DOCS / "00-student-outcome.md",
    DOCS / "01-capitulo-i-introduccion.md",
    DOCS / "02-capitulo-ii-requirements-elicitation.md",
    DOCS / "03-capitulo-iii-requirements-specification.md",
    DOCS / "04-capitulo-iv-solution-software-design.md",
    DOCS / "05-capitulo-v-solution-ui-ux-design.md",
    DOCS / "06-capitulo-vi-product-implementation.md",
    DOCS / "07-conclusiones.md",
    DOCS / "08-bibliografia.md",
    DOCS / "09-anexos.md",
]

TEMPLATE_BC = DOCS / "templates" / "bounded-context.md"
TEMPLATE_SPRINT = DOCS / "templates" / "sprint.md"

SOURCE_FILES = list(
    dict.fromkeys(
        CHAPTER_FILES
        + [TEMPLATE_BC, TEMPLATE_SPRINT]
        + sorted(p for p in (DOCS / "bounded-contexts").glob("*.md") if p.name != "README.md")
        + sorted(p for p in (DOCS / "sprints").glob("*.md") if p.name != "README.md")
    )
)

HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")
NUMBER_RE = re.compile(r"^((?:\d+|X)(?:\.(?:\d+|X))*)\.?\s+(.+)$", re.IGNORECASE)
FENCE_RE = re.compile(r"^```")
NAV_RE = re.compile(r"^\*\*Navegación:\*\*")
EXISTING_ANCHOR_RE = re.compile(r'^<a id="[^"]+"></a>\s*$')

SPECIAL_IDS = {
    "Carátula": "s-caratula",
    "Registro de Versiones del Informe": "s-registro-versiones",
    "Project Report Collaboration Insights": "s-collaboration-insights",
    "Contenido": "s-contenido",
    "Tabla de contenidos": "s-tabla-contenidos",
    "Student Outcome": "s-student-outcome",
    "Student Outcome (ABET - Criterio 5)": "s-student-outcome",
    "Videos de Exposiciones": "s-anexo-videos-exposiciones",
    "Repositorios y artefactos": "s-anexo-repositorios",
    "Capítulo I: Introducción": "s-cap-i",
    "Capítulo II: Requirements Elicitation & Analysis": "s-cap-ii",
    "Capítulo III: Requirements Specification": "s-cap-iii",
    "Capítulo IV: Solution Software Design": "s-cap-iv",
    "Capítulo V: Solution UI/UX Design": "s-cap-v",
    "Capítulo VI: Product Implementation, Validation & Deployment": "s-cap-vi",
    "Conclusiones": "s-conclusiones",
    "Bibliografía": "s-bibliografia",
    "Anexos": "s-anexos",
    "Conclusiones y recomendaciones": "s-conclusiones-recomendaciones",
    "Video About-the-Team": "s-video-about-the-team",
    "Bounded Contexts documentados": "s-4-2-lista",
    "Sprints documentados": "s-6-2-lista",
    "Relación de integrantes": "s-relacion-integrantes",
}


def slugify(text: str) -> str:
    text = unicodedata.normalize("NFD", text)
    text = "".join(c for c in text if unicodedata.category(c) != "Mn")
    text = text.lower()
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")


def make_id(title: str, used: set[str]) -> str:
    title = title.strip()
    numbered = NUMBER_RE.match(title)
    if title in SPECIAL_IDS:
        base = SPECIAL_IDS[title]
    elif numbered:
        base = "s-" + numbered.group(1).lower().replace(".", "-")
    else:
        base = "s-" + slugify(title)

    candidate = base
    if candidate in used:
        extra = slugify(numbered.group(2) if numbered else title)
        extra = "-".join(extra.split("-")[:6])
        candidate = f"{base}-{extra}" if extra else f"{base}-dup"
    suffix = 2
    while candidate in used:
        candidate = f"{base}-{suffix}"
        suffix += 1
    used.add(candidate)
    return candidate


def iter_source_headings(lines: list[str]):
    in_fence = False
    for i, line in enumerate(lines):
        if FENCE_RE.match(line.strip()):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        match = HEADING_RE.match(line)
        if match:
            yield i, match.group(1), match.group(2).strip()


def inject_anchors(path: Path, used: set[str]) -> list[tuple[int, str, str]]:
    original = path.read_text(encoding="utf-8")
    lines = original.splitlines()
    headings: list[tuple[int, str, str]] = []
    inserts: list[tuple[int, str]] = []

    for index, hashes, title in iter_source_headings(lines):
        anchor_id = make_id(title, used)
        headings.append((len(hashes), title, anchor_id))
        anchor_line = f'<a id="{anchor_id}"></a>'
        if index > 0 and EXISTING_ANCHOR_RE.match(lines[index - 1]):
            lines[index - 1] = anchor_line
        else:
            inserts.append((index, anchor_line))

    for index, anchor_line in reversed(inserts):
        lines.insert(index, anchor_line)

    new_text = "\n".join(lines) + ("\n" if original.endswith("\n") else "")
    if new_text != original:
        path.write_text(new_text, encoding="utf-8")
    return headings


def strip_nav(text: str) -> str:
    lines = text.splitlines()
    while lines and (not lines[0].strip() or NAV_RE.match(lines[0]) or lines[0].strip() == "---"):
        if lines[0].strip() == "---" and len(lines) > 1 and not NAV_RE.match(lines[1] if False else ""):
            # Keep the rest after a leading nav + rule
            pass
        lines.pop(0)
        if lines and lines[0].strip() == "---":
            lines.pop(0)
            break
    while lines and (not lines[-1].strip() or NAV_RE.match(lines[-1]) or lines[-1].strip() == "---"):
        lines.pop()
    return "\n".join(lines).strip() + "\n"


SKIP_TOC_TITLES = {
    "Carátula",
    "Relación de integrantes",
    "Registro de Versiones del Informe",
    "Project Report Collaboration Insights",
    "Contenido",
    "Tabla de contenidos",
    "Bounded Contexts documentados",
    "Sprints documentados",
}

NESTED_PARENTS = {"templates", "bounded-contexts", "sprints"}


def rewrite_asset_paths(text: str, source: Path) -> str:
    rel = source.parent.relative_to(DOCS)
    if rel == Path("."):
        return text
    return text.replace("](../../assets/", "](../assets/")


def demote_headings(text: str, extra: int) -> str:
    if extra <= 0:
        return text
    lines = text.splitlines()
    in_fence = False
    out: list[str] = []
    for line in lines:
        if FENCE_RE.match(line.strip()):
            in_fence = not in_fence
            out.append(line)
            continue
        match = None if in_fence else HEADING_RE.match(line)
        if match:
            hashes = match.group(1) + ("#" * extra)
            hashes = hashes[:6]
            line = f"{hashes} {match.group(2)}"
        out.append(line)
    return "\n".join(out) + "\n"


def folder_md(folder: Path, fallback: Path) -> list[Path]:
    files = sorted(p for p in folder.glob("*.md") if p.name != "README.md")
    return files or [fallback]


def split_before_heading(text: str, title: str) -> tuple[str, str]:
    lines = text.splitlines()
    in_fence = False
    for i, line in enumerate(lines):
        if FENCE_RE.match(line.strip()):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        match = HEADING_RE.match(line)
        if match and match.group(2).strip() == title:
            start = i - 1 if i > 0 and EXISTING_ANCHOR_RE.match(lines[i - 1]) else i
            before = "\n".join(lines[:start]).strip() + "\n"
            after = "\n".join(lines[start:]).strip() + "\n"
            return before, after
    return text, ""


def prepare(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    text = strip_nav(text)
    text = rewrite_asset_paths(text, path)
    if path.parent.name in NESTED_PARENTS:
        text = demote_headings(text, 2)
    # En el ensamblado, los enlaces del índice deben ser anclas internas.
    if path.name == FRONT.name:
        text = text.replace("](informe.md#", "](#")
    return text


def write_toc_block(path: Path, toc_body: str) -> None:
    text = path.read_text(encoding="utf-8")
    if TOC_START not in text or TOC_END not in text:
        raise SystemExit(f"{path.name} no tiene marcadores {TOC_START} / {TOC_END}")
    before, rest = text.split(TOC_START, 1)
    _, after = rest.split(TOC_END, 1)
    path.write_text(
        f"{before}{TOC_START}\n\n{toc_body}\n\n{TOC_END}{after}",
        encoding="utf-8",
    )


def collect_part(
    text: str,
    path: Path,
    toc_entries: list[tuple[int, str, str, str]],
    used_informe: set[str],
    parts: list[str],
) -> None:
    lines = text.splitlines()
    in_fence = False
    for i, line in enumerate(lines):
        if FENCE_RE.match(line.strip()):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        match = HEADING_RE.match(line)
        if not match:
            continue
        anchor_id = None
        if i > 0:
            am = re.match(r'^<a id="([^"]+)"></a>\s*$', lines[i - 1])
            if am:
                anchor_id = am.group(1)
        title = match.group(2).strip()
        if title in SKIP_TOC_TITLES:
            continue
        if not anchor_id:
            anchor_id = make_id(title, used_informe)
        else:
            used_informe.add(anchor_id)
        toc_entries.append((len(match.group(1)), title, anchor_id, path.name))
    if text.strip():
        parts.append(text.strip())


def main() -> None:
    used: set[str] = set()
    for path in SOURCE_FILES:
        if path.exists():
            inject_anchors(path, used)

    used_informe: set[str] = set()
    toc_entries: list[tuple[int, str, str, str]] = []
    parts: list[str] = []

    bc_files = folder_md(DOCS / "bounded-contexts", TEMPLATE_BC)
    sprint_files = folder_md(DOCS / "sprints", TEMPLATE_SPRINT)

    for path in CHAPTER_FILES:
        if not path.exists():
            continue
        text = prepare(path)

        if path.name == "04-capitulo-iv-solution-software-design.md":
            collect_part(text, path, toc_entries, used_informe, parts)
            for nested in bc_files:
                if nested.exists():
                    collect_part(prepare(nested), nested, toc_entries, used_informe, parts)
            continue

        if path.name == "06-capitulo-vi-product-implementation.md":
            before, after = split_before_heading(text, "6.3. Validation Interviews")
            collect_part(before, path, toc_entries, used_informe, parts)
            for nested in sprint_files:
                if nested.exists():
                    collect_part(prepare(nested), nested, toc_entries, used_informe, parts)
            collect_part(after, path, toc_entries, used_informe, parts)
            continue

        collect_part(text, path, toc_entries, used_informe, parts)

    # Índice en 00 (para editar / navegar desde el front matter)
    toc_for_front = "\n".join(
        f'{"    " * (level - 1)}1. [{title}](informe.md#{anchor_id})'
        for level, title, anchor_id, _ in toc_entries
    )
    write_toc_block(FRONT, toc_for_front)

    # Releer 00 ya con TOC y usarlo en el ensamblado (sin TOC duplicado al inicio)
    parts = []
    toc_entries = []
    used_informe = set()
    for path in CHAPTER_FILES:
        if not path.exists():
            continue
        text = prepare(path)
        if path.name == "04-capitulo-iv-solution-software-design.md":
            collect_part(text, path, toc_entries, used_informe, parts)
            for nested in bc_files:
                if nested.exists():
                    collect_part(prepare(nested), nested, toc_entries, used_informe, parts)
            continue
        if path.name == "06-capitulo-vi-product-implementation.md":
            before, after = split_before_heading(text, "6.3. Validation Interviews")
            collect_part(before, path, toc_entries, used_informe, parts)
            for nested in sprint_files:
                if nested.exists():
                    collect_part(prepare(nested), nested, toc_entries, used_informe, parts)
            collect_part(after, path, toc_entries, used_informe, parts)
            continue
        collect_part(text, path, toc_entries, used_informe, parts)

    INFORME.write_text("\n\n---\n\n".join(parts).strip() + "\n", encoding="utf-8")
    print(f"Anclas: {len(used)}  |  TOC: {len(toc_entries)} entradas")
    print(f"Escrito: {INFORME.relative_to(ROOT)}")
    print(f"Actualizado: {FRONT.relative_to(ROOT)} (Tabla de contenidos)")


if __name__ == "__main__":
    main()
