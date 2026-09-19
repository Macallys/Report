#!/usr/bin/env python3
"""Build docs/03-capitulo-iii-requirements-specification.md with HU01-HU42."""

from pathlib import Path

OUT = Path(__file__).resolve().parents[1] / "docs" / "03-capitulo-iii-requirements-specification.md"


def g(*scenarios):
    blocks = []
    for i, (title, dado, cuando, entonces) in enumerate(scenarios, 1):
        blocks.append(
            f"<strong>Escenario {i}: {title}</strong><br/>"
            f"{dado},<br/>"
            f"{cuando},<br/>"
            f"Entonces {entonces}."
        )
    return "<br/><br/>".join(blocks)


def S(hu, epic, title, desc, scenarios):
    return {
        "id": hu,
        "epic": epic,
        "title": title,
        "desc": desc,
        "ac": g(*scenarios),
    }


STORIES = [
    # E1
    S("HU01", "EP01", "Consulta de información del sistema SafePlant",
      "Como visitante quiero conocer el propósito y funcionamiento del sistema SafePlant para comprender cómo contribuye a la seguridad y al control ambiental de una planta industrial.",
      [("Presentación del propósito del sistema", "Dado que el visitante accede al sitio web estático de SafePlant", "Cuando el visitante consulta la sección de propósito del sistema", "el sitio presenta una descripción del objetivo de SafePlant en el control de seguridad y contaminación industrial"),
       ("Presentación de variables monitoreadas", "Dado que el visitante accede al sitio web estático de SafePlant", "Cuando el visitante consulta la sección de funcionamiento del sistema", "el sitio presenta información sobre el monitoreo de CO₂ en ppm, ruido en dB y presencia de personal en zonas críticas"),
       ("Presentación de acciones automáticas", "Dado que el visitante accede al sitio web estático de SafePlant", "Cuando el visitante consulta la sección de respuesta automática del sistema", "el sitio presenta información sobre la activación de extractores, sirenas preventivas y mamparas acústicas ante condiciones de riesgo"),
       ("Acceso desde dispositivo compatible", "Dado que el visitante accede al sitio desde un dispositivo compatible", "Cuando el visitante consulta las secciones informativas del sistema", "el sitio presenta el contenido de forma legible y funcional en el dispositivo utilizado")]),
    S("HU02", "EP01", "Consulta de beneficios y ventajas de SafePlant",
      "Como visitante quiero conocer los beneficios y ventajas competitivas de SafePlant para evaluar el valor que la solución aporta a la seguridad operativa de una planta industrial.",
      [("Beneficios en prevención de riesgos", "Dado que el visitante accede al sitio web de SafePlant", "Cuando el visitante consulta la sección de beneficios de la solución", "el sitio presenta los beneficios relacionados con la prevención de riesgos ambientales y de seguridad para operarios"),
       ("Beneficios en monitoreo continuo", "Dado que el visitante accede al sitio web de SafePlant", "Cuando el visitante consulta la sección de beneficios de la solución", "el sitio presenta los beneficios relacionados con el monitoreo ambiental continuo en tiempo real"),
       ("Beneficios en automatización industrial", "Dado que el visitante accede al sitio web de SafePlant", "Cuando el visitante consulta la sección de beneficios de la solución", "el sitio presenta los beneficios relacionados con la automatización de respuestas ante condiciones peligrosas")]),
    S("HU03", "EP01", "Consulta del equipo desarrollador",
      "Como visitante quiero conocer al equipo desarrollador de SafePlant para obtener información sobre la organización responsable de la solución.",
      [("Presentación del equipo de desarrollo", "Dado que el visitante accede al sitio web de SafePlant", "Cuando el visitante consulta la sección del equipo desarrollador", "el sitio presenta la información de los integrantes del equipo con sus roles en el proyecto"),
       ("Presentación de la startup responsable", "Dado que el visitante accede al sitio web de SafePlant", "Cuando el visitante consulta la sección institucional de la startup", "el sitio presenta el nombre de la startup, su misión y su relación con el proyecto SafePlant")]),
    S("HU04", "EP01", "Envío de formulario de contacto",
      "Como visitante quiero enviar una solicitud de contacto a través del sitio web para comunicarme con el equipo de SafePlant y obtener información adicional sobre la solución.",
      [("Envío exitoso de solicitud de contacto", "Dado que el visitante accede al formulario de contacto del sitio web<br/>Y el visitante proporciona nombre, correo electrónico y mensaje con datos válidos", "Cuando el visitante confirma el envío de la solicitud de contacto", "el sistema registra la solicitud y confirma al visitante que el mensaje fue recibido correctamente"),
       ("Envío con datos obligatorios incompletos", "Dado que el visitante accede al formulario de contacto del sitio web<br/>Y el visitante no proporciona uno o más datos obligatorios", "Cuando el visitante confirma el envío de la solicitud de contacto", "el sistema rechaza el envío e informa los campos obligatorios que deben completarse"),
       ("Envío con correo electrónico no válido", "Dado que el visitante accede al formulario de contacto del sitio web<br/>Y el visitante proporciona un correo electrónico con formato no válido", "Cuando el visitante confirma el envío de la solicitud de contacto", "el sistema rechaza el envío e informa que el correo electrónico no tiene un formato válido")]),
    S("HU05", "EP01", "Consulta de arquitectura técnica del sistema",
      "Como visitante quiero conocer la arquitectura técnica de SafePlant para comprender cómo se integran los dispositivos embebidos, el IoT Gateway y la plataforma en la nube.",
      [("Capa de dispositivos embebidos", "Dado que el visitante accede al sitio web de SafePlant", "Cuando el visitante consulta la sección de arquitectura técnica", "el sitio presenta información sobre los dispositivos ESP32, sensores de CO₂, ruido y presencia, y actuadores físicos del sistema"),
       ("Capa de IoT Gateway", "Dado que el visitante accede al sitio web de SafePlant", "Cuando el visitante consulta la sección de arquitectura técnica", "el sitio presenta información sobre el IoT Gateway basado en Raspberry Pi con procesamiento local y persistencia de contingencia"),
       ("Capa de plataforma en la nube", "Dado que el visitante accede al sitio web de SafePlant", "Cuando el visitante consulta la sección de arquitectura técnica", "el sitio presenta información sobre la API REST, la base de datos relacional y la plataforma de supervisión web")]),
    S("HU06", "EP01", "Navegación hacia la plataforma de supervisión",
      "Como visitante quiero acceder a la plataforma de supervisión desde el sitio informativo para ingresar al sistema de monitoreo con una cuenta autorizada.",
      [("Redirección hacia el punto de autenticación", "Dado que el visitante se encuentra en el sitio web de SafePlant", "Cuando el visitante solicita el acceso a la plataforma de supervisión", "el sistema redirige al visitante al punto de autenticación de la plataforma"),
       ("Acceso identificable en la navegación principal", "Dado que el visitante consulta el sitio web de SafePlant", "Cuando el visitante revisa la navegación principal del sitio", "el sitio presenta un acceso identificable hacia la plataforma de supervisión")]),
]

# Load remaining stories from companion modules
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent))
from stories_part2 import STORIES_PART2  # noqa: E402
from stories_part3 import STORIES_PART3  # noqa: E402
from stories_nfr import STORIES_NFR  # noqa: E402

STORIES.extend(STORIES_PART2)
STORIES.extend(STORIES_PART3)
STORIES.extend(STORIES_NFR)

HEADER = """**Navegación:** [Índice](./00-student-outcome.md#s-tabla-contenidos) · Anterior: [Capítulo II](./02-capitulo-ii-requirements-elicitation.md) · Siguiente: [Capítulo IV](./04-capitulo-iv-solution-software-design.md)

---

<a id="s-cap-iii"></a>
# Capítulo III: Requirements Specification

<a id="s-3-0"></a>
## 3.0. Product Epics

<table>
  <thead>
    <tr>
      <th align="left">Epic ID</th>
      <th align="left">Título</th>
      <th align="left">Descripción</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td align="left">EP01</td>
      <td align="left">Landing Page de Startup y Producto</td>
      <td align="left">Como visitante quiero conocer el producto SafePlant, sus beneficios y al equipo responsable para evaluar la solución de control de seguridad y contaminación industrial.</td>
    </tr>
    <tr>
      <td align="left">EP02</td>
      <td align="left">Registro y Autenticación</td>
      <td align="left">Como usuario de la plataforma quiero autenticarme y acceder con un rol definido para utilizar de forma controlada las funciones de supervisión y administración del sistema.</td>
    </tr>
    <tr>
      <td align="left">EP03</td>
      <td align="left">Telemetría y Monitoreo en Tiempo Real</td>
      <td align="left">Como supervisor de seguridad quiero monitorear en tiempo real CO₂, ruido y presencia por zonas críticas para detectar oportunamente condiciones de riesgo en la planta industrial.</td>
    </tr>
    <tr>
      <td align="left">EP04</td>
      <td align="left">Evaluación de Exposición por Presencia</td>
      <td align="left">Como supervisor de seguridad quiero que el sistema cruce la presencia detectada por sensores con las condiciones ambientales de CO₂ y ruido para identificar exposición de personal en zonas críticas y priorizar alertas desde la aplicación móvil.</td>
    </tr>
    <tr>
      <td align="left">EP05</td>
      <td align="left">Automatización de Actuadores y Reglas de Negocio</td>
      <td align="left">Como supervisor de seguridad quiero que el sistema active automáticamente extractores, sirenas y mamparas acústicas ante condiciones de riesgo para proteger al personal y reducir la contaminación industrial.</td>
    </tr>
    <tr>
      <td align="left">EP06</td>
      <td align="left">Atributos de Calidad del Sistema</td>
      <td align="left">Como supervisor de seguridad quiero que SafePlant cumpla requisitos de rendimiento, confiabilidad offline, seguridad, disponibilidad y compatibilidad multiplataforma para operar la planta con continuidad y protección de la información.</td>
    </tr>
  </tbody>
</table>

<a id="s-3-1"></a>
## 3.1. User Stories

<table>
  <thead>
    <tr>
      <th align="left">ID</th>
      <th align="left">Épica</th>
      <th align="left">Título</th>
      <th align="left">Descripción</th>
      <th align="left">Criterios de Aceptación (Gherkin)</th>
    </tr>
  </thead>
  <tbody>
"""

FOOTER = """  </tbody>
</table>

<a id="s-3-2"></a>
## 3.2. Impact Mapping

![Impact Map](../assets/03-capitulo-iii/impact-map.png)

<a id="s-3-3"></a>
## 3.3. Product Backlog

<table>
  <thead>
    <tr>
      <th align="left">ID</th>
      <th align="left">User Story</th>
      <th align="left">Points</th>
      <th align="left">Sprint</th>
      <th align="left">Priority</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td align="left"></td>
      <td align="left"></td>
      <td align="left"></td>
      <td align="left"></td>
      <td align="left"></td>
    </tr>
  </tbody>
</table>

---

**Navegación:** [Índice](./00-student-outcome.md#s-tabla-contenidos) · Anterior: [Capítulo II](./02-capitulo-ii-requirements-elicitation.md) · Siguiente: [Capítulo IV](./04-capitulo-iv-solution-software-design.md)
"""


def row(s):
    return (
        "    <tr>\n"
        f"      <td align=\"left\">{s['id']}</td>\n"
        f"      <td align=\"left\">{s['epic']}</td>\n"
        f"      <td align=\"left\">{s['title']}</td>\n"
        f"      <td align=\"left\">{s['desc']}</td>\n"
        f"      <td align=\"left\">{s['ac']}</td>\n"
        "    </tr>\n"
    )


def main():
    assert len(STORIES) == 37, f"Expected 37 stories, got {len(STORIES)}"
    content = HEADER + "".join(row(s) for s in STORIES) + FOOTER
    OUT.write_text(content, encoding="utf-8")
    print(f"Wrote {OUT} ({len(content.splitlines())} lines, {len(STORIES)} stories)")


if __name__ == "__main__":
    main()
