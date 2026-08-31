# Informe de Trabajo Final — 1ASI0572 Desarrollo de Soluciones IoT

Repositorio Markdown del **Final Project Document Report** (ciclo 2026-20), según el enunciado oficial.

## Entrada al informe

| Archivo | Uso |
| :--- | :--- |
| [`docs/00-student-outcome.md`](docs/00-student-outcome.md) | Carátula, versiones, Collaboration Insights, tabla de contenidos y Student Outcome |
| [`docs/informe.md`](docs/informe.md) | Informe ensamblado completo (base para exportar a PDF) |
| [`docs/01-…` … `09-…`](docs/) | Capítulos I–VI, conclusiones, bibliografía y anexos |

## Regenerar índice e informe ensamblado

```bash
python scripts/build-informe.py
```

## Estructura (alineada al enunciado)

```text
Report/
├── README.md
├── scripts/build-informe.py
├── assets/                            ← Evidencias e imágenes por capítulo
│   ├── 00-front-matter/
│   ├── 01-capitulo-i/
│   ├── 02-capitulo-ii/
│   ├── 03-capitulo-iii/
│   ├── 04-capitulo-iv/
│   ├── 05-capitulo-v/
│   ├── 06-capitulo-vi/
│   ├── 07-conclusiones/
│   └── 09-anexos/
└── docs/
    ├── 00-student-outcome.md          ← Front matter + Student Outcome
    ├── 01-capitulo-i-introduccion.md
    ├── 02-capitulo-ii-requirements-elicitation.md
    ├── 03-capitulo-iii-requirements-specification.md
    ├── 04-capitulo-iv-solution-software-design.md
    ├── 05-capitulo-v-solution-ui-ux-design.md
    ├── 06-capitulo-vi-product-implementation.md
    ├── 07-conclusiones.md
    ├── 08-bibliografia.md
    ├── 09-anexos.md
    ├── informe.md                     ← Ensamblado (no editar a mano)
    ├── bounded-contexts/              ← Un archivo por Bounded Context (4.2.X)
    ├── sprints/                       ← Un archivo por Sprint (6.2.X)
    └── templates/
        ├── bounded-context.md
        └── sprint.md
```

## Entregas PDF (nomenclatura)

`upc-pre-202620-1asi0572-<NRC>-<startup>-report-<avn/tbn>.pdf`
