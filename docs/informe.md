<a id="s-caratula"></a>
# Carátula

<div align="center">

![Logo de la Universidad](../assets/00-front-matter/upc-logo.png)

**Universidad Peruana de Ciencias Aplicadas**

**Facultad de Ingeniería**

**Carrera de Ingeniería de Software**

**Ciclo académico:** 2026-20

---

**Código del curso:** 1ASI0572

**Nombre del curso:** Desarrollo de Soluciones IoT

**NRC:** [NRC]

**Nombre del profesor:** [Apellidos y Nombres]

---

**Informe de Trabajo Final**

**Nombre del startup:** [Nombre del startup]

**Nombre del producto:** [Nombre del producto]

</div>

<a id="s-relacion-integrantes"></a>
## Relación de integrantes

<table>
  <thead>
    <tr>
      <th align="left">Código</th>
      <th align="left">Apellidos y Nombres</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td align="left"></td>
      <td align="left"></td>
    </tr>
    <tr>
      <td align="left"></td>
      <td align="left"></td>
    </tr>
    <tr>
      <td align="left"></td>
      <td align="left"></td>
    </tr>
    <tr>
      <td align="left"></td>
      <td align="left"></td>
    </tr>
  </tbody>
</table>

<div align="center">

**Mes y año:** [Mes, Año]

</div>

---

<a id="s-registro-versiones"></a>
# Registro de Versiones del Informe

<table>
  <thead>
    <tr>
      <th align="left">Versión</th>
      <th align="left">Fecha</th>
      <th align="left">Autor</th>
      <th align="left">Descripción de modificación</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td align="left">1.0</td>
      <td align="left">2026-08-31</td>
      <td align="left"></td>
      <td align="left">Inicialización del esqueleto del informe según enunciado del Trabajo Final.</td>
    </tr>
  </tbody>
</table>

---

<a id="s-collaboration-insights"></a>
# Project Report Collaboration Insights

**URL del repositorio (Project Report):** [URL de la organización / repositorio GitHub]

**Entrega AV1 / TB1 / AV2 / TB2**

![Analíticos de colaboración — captura](../assets/00-front-matter/github-collaboration-insights-1.png)

![Commits / contribución — captura](../assets/00-front-matter/github-collaboration-insights-2.png)

---

<a id="s-contenido"></a>
# Contenido

<a id="s-tabla-contenidos"></a>
## Tabla de contenidos

<!-- TOC:start -->

1. [Student Outcome](#s-student-outcome)
1. [Capítulo I: Introducción](#s-cap-i)
    1. [1.1. Startup Profile](#s-1-1)
        1. [1.1.1. Descripción de la Startup](#s-1-1-1)
        1. [1.1.2. Perfiles de integrantes del equipo](#s-1-1-2)
    1. [1.2. Solution Profile](#s-1-2)
        1. [1.2.1 Antecedentes y problemática](#s-1-2-1)
        1. [1.2.2 Lean UX Process](#s-1-2-2)
            1. [1.2.2.1. Lean UX Problem Statements](#s-1-2-2-1)
            1. [1.2.2.2. Lean UX Assumptions](#s-1-2-2-2)
            1. [1.2.2.3. Lean UX Hypothesis Statements](#s-1-2-2-3)
            1. [1.2.2.4. Lean UX Canvas](#s-1-2-2-4)
    1. [1.3. Segmentos objetivo](#s-1-3)
1. [Capítulo II: Requirements Elicitation & Analysis](#s-cap-ii)
    1. [2.1. Competidores](#s-2-1)
        1. [2.1.1. Análisis competitivo](#s-2-1-1)
        1. [2.1.2. Estrategias y tácticas frente a competidores](#s-2-1-2)
    1. [2.2. Entrevistas](#s-2-2)
        1. [2.2.1. Diseño de entrevistas](#s-2-2-1)
        1. [2.2.2. Registro de entrevistas](#s-2-2-2)
        1. [2.2.3. Análisis de entrevistas](#s-2-2-3)
    1. [2.3. Needfinding](#s-2-3)
        1. [2.3.1. User Personas](#s-2-3-1)
        1. [2.3.2. User Task Matrix](#s-2-3-2)
        1. [2.3.3. User Journey Mapping](#s-2-3-3)
        1. [2.3.4. Empathy Mapping](#s-2-3-4)
    1. [2.4. Big Picture EventStorming](#s-2-4)
    1. [2.5. Ubiquitous Language](#s-2-5)
1. [Capítulo III: Requirements Specification](#s-cap-iii)
    1. [3.1. User Stories](#s-3-1)
    1. [3.2. Impact Mapping](#s-3-2)
    1. [3.3. Product Backlog](#s-3-3)
1. [Capítulo IV: Solution Software Design](#s-cap-iv)
    1. [4.1. Strategic-Level Domain-Driven Design](#s-4-1)
        1. [4.1.1. Design-Level EventStorming](#s-4-1-1)
            1. [4.1.1.1 Candidate Context Discovery](#s-4-1-1-1)
            1. [4.1.1.2 Domain Message Flows Modeling](#s-4-1-1-2)
            1. [4.1.1.3 Bounded Context Canvases](#s-4-1-1-3)
        1. [4.1.2. Context Mapping](#s-4-1-2)
        1. [4.1.3. Software Architecture](#s-4-1-3)
            1. [4.1.3.1. Software Architecture System Landscape Diagram](#s-4-1-3-1)
            1. [4.1.3.2. Software Architecture Context Level Diagrams](#s-4-1-3-2)
            1. [4.1.3.2. Software Architecture Container Level Diagrams](#s-4-1-3-2-software-architecture-container-level-diagrams)
            1. [4.1.3.3. Software Architecture Deployment Diagrams](#s-4-1-3-3)
    1. [4.2. Tactical-Level Domain-Driven Design](#s-4-2)
        1. [4.2.X. Bounded Context: \<Bounded Context Name\>](#s-4-2-x)
            1. [4.2.X.1. Domain Layer](#s-4-2-x-1)
            1. [4.2.X.2. Interface Layer](#s-4-2-x-2)
            1. [4.2.X.3. Application Layer](#s-4-2-x-3)
            1. [4.2.X.4. Infrastructure Layer](#s-4-2-x-4)
            1. [4.2.X.5. Bounded Context Software Architecture Component Level Diagrams](#s-4-2-x-5)
            1. [4.2.X.6. Bounded Context Software Architecture Code Level Diagrams](#s-4-2-x-6)
                1. [4.2.X.6.1. Bounded Context Domain Layer Class Diagrams](#s-4-2-x-6-1)
                1. [4.2.X.6.2. Bounded Context Database Design Diagram](#s-4-2-x-6-2)
1. [Capítulo V: Solution UI/UX Design](#s-cap-v)
    1. [5.1. Style Guidelines](#s-5-1)
        1. [5.1.1. General Style Guidelines](#s-5-1-1)
        1. [5.1.2. Web, Mobile and IoT Style Guidelines](#s-5-1-2)
    1. [5.2. Information Architecture](#s-5-2)
        1. [5.2.1. Organization Systems](#s-5-2-1)
        1. [5.2.2. Labeling Systems](#s-5-2-2)
        1. [5.2.3. SEO Tags and Meta Tags](#s-5-2-3)
        1. [5.2.4. Searching Systems](#s-5-2-4)
        1. [5.2.5. Navigation Systems](#s-5-2-5)
    1. [5.3. Landing Page UI Design](#s-5-3)
        1. [5.3.1. Landing Page Wireframe](#s-5-3-1)
        1. [5.3.2. Landing Page Mock-up](#s-5-3-2)
    1. [5.4. Applications UX/UI Design](#s-5-4)
        1. [5.4.1. Applications Wireframes](#s-5-4-1)
        1. [5.4.2. Applications Wireflow Diagrams](#s-5-4-2)
        1. [5.4.2. Applications Mock-ups](#s-5-4-2-applications-mock-ups)
        1. [5.4.3. Applications User Flow Diagrams](#s-5-4-3)
    1. [5.5. Applications Prototyping](#s-5-5)
    1. [5.6. IoT Device Design](#s-5-6)
1. [Capítulo VI: Product Implementation, Validation & Deployment](#s-cap-vi)
    1. [6.1. Software Configuration Management](#s-6-1)
        1. [6.1.1. Software Development Environment Configuration](#s-6-1-1)
        1. [6.1.2. Source Code Management](#s-6-1-2)
        1. [6.1.3. Source Code Style Guide & Conventions](#s-6-1-3)
        1. [6.1.4. Software Deployment Configuration](#s-6-1-4)
    1. [6.2. Landing Page, Services & Applications Implementation](#s-6-2)
        1. [6.2.X. Sprint n](#s-6-2-x)
            1. [6.2.X.1. Sprint Planning n](#s-6-2-x-1)
            1. [6.2.X.2. Aspect Leaders and Collaborators](#s-6-2-x-2)
            1. [6.2.X.3. Sprint Backlog n](#s-6-2-x-3)
            1. [6.2.X.4. Development Evidence for Sprint Review](#s-6-2-x-4)
            1. [6.2.X.5. Testing Suite Evidence for Sprint Review](#s-6-2-x-5)
            1. [6.2.X.6. Execution Evidence for Sprint Review](#s-6-2-x-6)
            1. [6.2.X.7. Services Documentation Evidence for Sprint Review](#s-6-2-x-7)
            1. [6.2.X.8. Software Deployment Evidence for Sprint Review](#s-6-2-x-8)
            1. [6.2.X.9. Team Collaboration Insights during Sprint](#s-6-2-x-9)
    1. [6.3. Validation Interviews](#s-6-3)
        1. [6.3.1. Diseño de Entrevistas](#s-6-3-1)
        1. [6.3.2. Registro de Entrevistas](#s-6-3-2)
        1. [6.3.3. Evaluaciones según heurísticas](#s-6-3-3)
    1. [6.4. Video About-the-Product](#s-6-4)
1. [Conclusiones](#s-conclusiones)
    1. [Conclusiones y recomendaciones](#s-conclusiones-recomendaciones)
    1. [Video About-the-Team](#s-video-about-the-team)
1. [Bibliografía](#s-bibliografia)
1. [Anexos](#s-anexos)
    1. [Videos de Exposiciones](#s-anexo-videos-exposiciones)
    1. [Repositorios y artefactos](#s-anexo-repositorios)

<!-- TOC:end -->

---

<a id="s-student-outcome"></a>
# Student Outcome

El curso contribuye al cumplimiento del Student Outcome ABET:

**ABET – EAC - Student Outcome 5**

**Criterio:** La capacidad de funcionar efectivamente en un equipo cuyos miembros juntos proporcionan liderazgo, crean un entorno de colaboración e inclusivo, establecen objetivos, planifican tareas y cumplen objetivos.

En el siguiente cuadro se describe las acciones realizadas y enunciados de conclusiones por parte del grupo, que permiten sustentar el haber alcanzado el logro del ABET – EAC - Student Outcome 5.

<table>
  <thead>
    <tr>
      <th align="left">Criterio específico</th>
      <th align="left">Acciones realizadas</th>
      <th align="left">Conclusiones</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td align="left">Trabaja en equipo para proporcionar liderazgo en forma conjunta</td>
      <td align="left"></td>
      <td align="left"></td>
    </tr>
    <tr>
      <td align="left">Crea un entorno colaborativo e inclusivo, establece metas, planifica tareas y cumple objetivos.</td>
      <td align="left"></td>
      <td align="left"></td>
    </tr>
  </tbody>
</table>

---

<a id="s-cap-i"></a>
# Capítulo I: Introducción

<a id="s-1-1"></a>
## 1.1. Startup Profile

<a id="s-1-1-1"></a>
### 1.1.1. Descripción de la Startup

<a id="s-1-1-2"></a>
### 1.1.2. Perfiles de integrantes del equipo

<table>
  <thead>
    <tr>
      <th align="center">Foto</th>
      <th align="left">Apellidos y Nombres</th>
      <th align="left">Código</th>
      <th align="left">Carrera</th>
      <th align="left">Conocimientos técnicos y habilidades</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td align="center">![Integrante 1](../assets/01-capitulo-i/equipo/integrante-1.png)</td>
      <td align="left"></td>
      <td align="left"></td>
      <td align="left">Ingeniería de Software</td>
      <td align="left"></td>
    </tr>
    <tr>
      <td align="center">![Integrante 2](../assets/01-capitulo-i/equipo/integrante-2.png)</td>
      <td align="left"></td>
      <td align="left"></td>
      <td align="left">Ingeniería de Software</td>
      <td align="left"></td>
    </tr>
    <tr>
      <td align="center">![Integrante 3](../assets/01-capitulo-i/equipo/integrante-3.png)</td>
      <td align="left"></td>
      <td align="left"></td>
      <td align="left">Ingeniería de Software</td>
      <td align="left"></td>
    </tr>
    <tr>
      <td align="center">![Integrante 4](../assets/01-capitulo-i/equipo/integrante-4.png)</td>
      <td align="left"></td>
      <td align="left"></td>
      <td align="left">Ingeniería de Software</td>
      <td align="left"></td>
    </tr>
  </tbody>
</table>

<a id="s-1-2"></a>
## 1.2. Solution Profile

<a id="s-1-2-1"></a>
### 1.2.1 Antecedentes y problemática

<a id="s-1-2-2"></a>
### 1.2.2 Lean UX Process

<a id="s-1-2-2-1"></a>
#### 1.2.2.1. Lean UX Problem Statements

<a id="s-1-2-2-2"></a>
#### 1.2.2.2. Lean UX Assumptions

<table>
  <thead>
    <tr>
      <th align="left">Tipo de assumption</th>
      <th align="left">Enunciados (creencias)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td align="left">Business Assumptions</td>
      <td align="left"></td>
    </tr>
    <tr>
      <td align="left">Business Outcome Assumptions</td>
      <td align="left"></td>
    </tr>
    <tr>
      <td align="left">User Assumptions</td>
      <td align="left"></td>
    </tr>
    <tr>
      <td align="left">User Outcome and Benefit Assumptions</td>
      <td align="left"></td>
    </tr>
    <tr>
      <td align="left">Feature Assumptions</td>
      <td align="left"></td>
    </tr>
  </tbody>
</table>

<a id="s-1-2-2-3"></a>
#### 1.2.2.3. Lean UX Hypothesis Statements

<a id="s-1-2-2-4"></a>
#### 1.2.2.4. Lean UX Canvas

![Lean UX Canvas](../assets/01-capitulo-i/lean-ux/lean-ux-canvas.png)

<a id="s-1-3"></a>
## 1.3. Segmentos objetivo

---

<a id="s-cap-ii"></a>
# Capítulo II: Requirements Elicitation & Analysis

<a id="s-2-1"></a>
## 2.1. Competidores

<a id="s-2-1-1"></a>
### 2.1.1. Análisis competitivo

**Competitive Analysis Landscape**

**¿Por qué llevar a cabo este análisis?**



<table>
  <thead>
    <tr>
      <th align="left">Dimensión</th>
      <th align="center">Su startup<br/>(Nombre / Logo)</th>
      <th align="center">Competidor 1<br/>(Nombre / Logo)</th>
      <th align="center">Competidor 2<br/>(Nombre / Logo)</th>
      <th align="center">Competidor 3<br/>(Nombre / Logo)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td align="left" colspan="5"><strong>Perfil</strong></td>
    </tr>
    <tr>
      <td align="left">Overview</td>
      <td align="left"></td>
      <td align="left"></td>
      <td align="left"></td>
      <td align="left"></td>
    </tr>
    <tr>
      <td align="left">Ventaja competitiva<br/>¿Qué valor ofrece a los clientes?</td>
      <td align="left"></td>
      <td align="left"></td>
      <td align="left"></td>
      <td align="left"></td>
    </tr>
    <tr>
      <td align="left" colspan="5"><strong>Perfil de Marketing</strong></td>
    </tr>
    <tr>
      <td align="left">Mercado objetivo</td>
      <td align="left"></td>
      <td align="left"></td>
      <td align="left"></td>
      <td align="left"></td>
    </tr>
    <tr>
      <td align="left">Estrategias de marketing</td>
      <td align="left"></td>
      <td align="left"></td>
      <td align="left"></td>
      <td align="left"></td>
    </tr>
    <tr>
      <td align="left" colspan="5"><strong>Perfil de Producto</strong></td>
    </tr>
    <tr>
      <td align="left">Productos &amp; Servicios</td>
      <td align="left"></td>
      <td align="left"></td>
      <td align="left"></td>
      <td align="left"></td>
    </tr>
    <tr>
      <td align="left">Precios &amp; Costos</td>
      <td align="left"></td>
      <td align="left"></td>
      <td align="left"></td>
      <td align="left"></td>
    </tr>
    <tr>
      <td align="left">Canales de distribución<br/>(Web y/o Móvil)</td>
      <td align="left"></td>
      <td align="left"></td>
      <td align="left"></td>
      <td align="left"></td>
    </tr>
  </tbody>
</table>

**Análisis SWOT**

<table>
  <thead>
    <tr>
      <th align="left">SWOT</th>
      <th align="left">Su startup</th>
      <th align="left">Competidor 1</th>
      <th align="left">Competidor 2</th>
      <th align="left">Competidor 3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td align="left"><strong>Fortalezas</strong></td>
      <td align="left"></td>
      <td align="left"></td>
      <td align="left"></td>
      <td align="left"></td>
    </tr>
    <tr>
      <td align="left"><strong>Debilidades</strong></td>
      <td align="left"></td>
      <td align="left"></td>
      <td align="left"></td>
      <td align="left"></td>
    </tr>
    <tr>
      <td align="left"><strong>Oportunidades</strong></td>
      <td align="left"></td>
      <td align="left"></td>
      <td align="left"></td>
      <td align="left"></td>
    </tr>
    <tr>
      <td align="left"><strong>Amenazas</strong></td>
      <td align="left"></td>
      <td align="left"></td>
      <td align="left"></td>
      <td align="left"></td>
    </tr>
  </tbody>
</table>

<a id="s-2-1-2"></a>
### 2.1.2. Estrategias y tácticas frente a competidores

<a id="s-2-2"></a>
## 2.2. Entrevistas

<a id="s-2-2-1"></a>
### 2.2.1. Diseño de entrevistas

<a id="s-2-2-2"></a>
### 2.2.2. Registro de entrevistas

<table>
  <thead>
    <tr>
      <th align="left">ID</th>
      <th align="left">Fecha</th>
      <th align="left">Entrevistado</th>
      <th align="left">Segmento objetivo</th>
      <th align="left">Evidencia (enlace / captura)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td align="left">E-01</td>
      <td align="left"></td>
      <td align="left"></td>
      <td align="left"></td>
      <td align="left"></td>
    </tr>
  </tbody>
</table>

<a id="s-2-2-3"></a>
### 2.2.3. Análisis de entrevistas

<a id="s-2-3"></a>
## 2.3. Needfinding

<a id="s-2-3-1"></a>
### 2.3.1. User Personas

![User Persona](../assets/02-capitulo-ii/needfinding/persona-1.png)

<a id="s-2-3-2"></a>
### 2.3.2. User Task Matrix

![User Task Matrix](../assets/02-capitulo-ii/needfinding/user-task-matrix.png)

<a id="s-2-3-3"></a>
### 2.3.3. User Journey Mapping

![User Journey Map](../assets/02-capitulo-ii/needfinding/user-journey-map.png)

<a id="s-2-3-4"></a>
### 2.3.4. Empathy Mapping

![Empathy Map](../assets/02-capitulo-ii/needfinding/empathy-map.png)

<a id="s-2-4"></a>
## 2.4. Big Picture EventStorming

![Big Picture EventStorming](../assets/02-capitulo-ii/eventstorming/big-picture-eventstorming.png)

<a id="s-2-5"></a>
## 2.5. Ubiquitous Language

<table>
  <thead>
    <tr>
      <th align="left">Término</th>
      <th align="left">Definición</th>
      <th align="left">Contexto</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td align="left"></td>
      <td align="left"></td>
      <td align="left"></td>
    </tr>
  </tbody>
</table>

---

<a id="s-cap-iii"></a>
# Capítulo III: Requirements Specification


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
      <td align="left">E1</td>
      <td align="left">Landing Page de Startup y Producto</td>
      <td align="left">Como visitante quiero conocer el producto SafePlant, sus beneficios y al equipo responsable para evaluar la solución de control de seguridad y contaminación industrial, e identificar el acceso a la aplicación móvil de operación y a la aplicación web de configuración.</td>
    </tr>
    <tr>
      <td align="left">E2</td>
      <td align="left">Registro y Autenticación</td>
      <td align="left">Como usuario autorizado quiero autenticarme en el canal correspondiente a mi rol —aplicación móvil para el supervisor de seguridad y aplicación web para el encargado de planta— para utilizar de forma controlada las funciones de operación remota o de configuración del sistema.</td>
    </tr>
    <tr>
      <td align="left">E3</td>
      <td align="left">Telemetría y Monitoreo en Tiempo Real</td>
      <td align="left">Como supervisor de seguridad quiero monitorear en tiempo real CO₂, ruido y presencia por zonas críticas desde la aplicación móvil para detectar oportunamente condiciones de riesgo en la planta industrial; y como encargado de planta quiero configurar zonas, umbrales y dispositivos desde la aplicación web para habilitar ese monitoreo.</td>
    </tr>
    <tr>
      <td align="left">E4</td>
      <td align="left">Acceso y Seguridad Física en Zonas Críticas</td>
      <td align="left">Como encargado de planta quiero registrar credenciales RFID en la aplicación web y como supervisor de seguridad quiero consultar presencia y accesos desde la aplicación móvil para controlar el ingreso a zonas críticas y evitar la exposición del personal a condiciones ambientales peligrosas.</td>
    </tr>
    <tr>
      <td align="left">E5</td>
      <td align="left">Automatización de Actuadores y Reglas de Negocio</td>
      <td align="left">Como supervisor de seguridad quiero que el sistema active automáticamente extractores, sirenas y mamparas acústicas ante condiciones de riesgo y poder anular actuadores de forma remota desde la aplicación móvil para proteger al personal y reducir la contaminación industrial.</td>
    </tr>
    <tr>
      <td align="left">E6</td>
      <td align="left">Atributos de Calidad del Sistema</td>
      <td align="left">Como supervisor de seguridad y como encargado de planta quiero que SafePlant cumpla requisitos de rendimiento, confiabilidad offline, seguridad, disponibilidad y compatibilidad de la aplicación móvil de operación y de la aplicación web de configuración para operar y administrar la planta con continuidad y protección de la información.</td>
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
    <tr>
      <td align="left">HU01</td>
      <td align="left">E1</td>
      <td align="left">Consulta de información del sistema SafePlant</td>
      <td align="left">Como visitante quiero conocer el propósito y funcionamiento del sistema SafePlant para comprender cómo contribuye a la seguridad y al control ambiental de una planta industrial.</td>
      <td align="left"><strong>Escenario 1: Presentación del propósito del sistema</strong><br/>Dado que el visitante accede al sitio web estático de SafePlant,<br/>Cuando el visitante consulta la sección de propósito del sistema,<br/>Entonces el sitio presenta una descripción del objetivo de SafePlant en el control de seguridad y contaminación industrial.<br/><br/><strong>Escenario 2: Presentación de variables monitoreadas</strong><br/>Dado que el visitante accede al sitio web estático de SafePlant,<br/>Cuando el visitante consulta la sección de funcionamiento del sistema,<br/>Entonces el sitio presenta información sobre el monitoreo de CO₂ en ppm, ruido en dB y presencia de personal en zonas críticas.<br/><br/><strong>Escenario 3: Presentación de acciones automáticas</strong><br/>Dado que el visitante accede al sitio web estático de SafePlant,<br/>Cuando el visitante consulta la sección de respuesta automática del sistema,<br/>Entonces el sitio presenta información sobre la activación de extractores, sirenas preventivas y mamparas acústicas ante condiciones de riesgo.<br/><br/><strong>Escenario 4: Acceso desde dispositivo compatible</strong><br/>Dado que el visitante accede al sitio desde un dispositivo compatible,<br/>Cuando el visitante consulta las secciones informativas del sistema,<br/>Entonces el sitio presenta el contenido de forma legible y funcional en el dispositivo utilizado.</td>
    </tr>
    <tr>
      <td align="left">HU02</td>
      <td align="left">E1</td>
      <td align="left">Consulta de beneficios y ventajas de SafePlant</td>
      <td align="left">Como visitante quiero conocer los beneficios y ventajas competitivas de SafePlant para evaluar el valor que la solución aporta a la seguridad operativa de una planta industrial.</td>
      <td align="left"><strong>Escenario 1: Beneficios en prevención de riesgos</strong><br/>Dado que el visitante accede al sitio web de SafePlant,<br/>Cuando el visitante consulta la sección de beneficios de la solución,<br/>Entonces el sitio presenta los beneficios relacionados con la prevención de riesgos ambientales y de seguridad para operarios.<br/><br/><strong>Escenario 2: Beneficios en monitoreo continuo</strong><br/>Dado que el visitante accede al sitio web de SafePlant,<br/>Cuando el visitante consulta la sección de beneficios de la solución,<br/>Entonces el sitio presenta los beneficios relacionados con el monitoreo ambiental continuo en tiempo real desde la aplicación móvil.<br/><br/><strong>Escenario 3: Beneficios en automatización industrial</strong><br/>Dado que el visitante accede al sitio web de SafePlant,<br/>Cuando el visitante consulta la sección de beneficios de la solución,<br/>Entonces el sitio presenta los beneficios relacionados con la automatización de respuestas ante condiciones peligrosas y el control operativo remoto.</td>
    </tr>
    <tr>
      <td align="left">HU03</td>
      <td align="left">E1</td>
      <td align="left">Consulta del equipo desarrollador</td>
      <td align="left">Como visitante quiero conocer al equipo desarrollador de SafePlant para obtener información sobre la organización responsable de la solución.</td>
      <td align="left"><strong>Escenario 1: Presentación del equipo de desarrollo</strong><br/>Dado que el visitante accede al sitio web de SafePlant,<br/>Cuando el visitante consulta la sección del equipo desarrollador,<br/>Entonces el sitio presenta la información de los integrantes del equipo con sus roles en el proyecto.<br/><br/><strong>Escenario 2: Presentación de la startup responsable</strong><br/>Dado que el visitante accede al sitio web de SafePlant,<br/>Cuando el visitante consulta la sección institucional de la startup,<br/>Entonces el sitio presenta el nombre de la startup, su misión y su relación con el proyecto SafePlant.</td>
    </tr>
    <tr>
      <td align="left">HU04</td>
      <td align="left">E1</td>
      <td align="left">Envío de formulario de contacto</td>
      <td align="left">Como visitante quiero enviar una solicitud de contacto a través del sitio web para comunicarme con el equipo de SafePlant y obtener información adicional sobre la solución.</td>
      <td align="left"><strong>Escenario 1: Envío exitoso de solicitud de contacto</strong><br/>Dado que el visitante accede al formulario de contacto del sitio web<br/>Y el visitante proporciona nombre, correo electrónico y mensaje con datos válidos,<br/>Cuando el visitante confirma el envío de la solicitud de contacto,<br/>Entonces el sistema registra la solicitud y confirma al visitante que el mensaje fue recibido correctamente.<br/><br/><strong>Escenario 2: Envío con datos obligatorios incompletos</strong><br/>Dado que el visitante accede al formulario de contacto del sitio web<br/>Y el visitante no proporciona uno o más datos obligatorios,<br/>Cuando el visitante confirma el envío de la solicitud de contacto,<br/>Entonces el sistema rechaza el envío e informa los campos obligatorios que deben completarse.<br/><br/><strong>Escenario 3: Envío con correo electrónico no válido</strong><br/>Dado que el visitante accede al formulario de contacto del sitio web<br/>Y el visitante proporciona un correo electrónico con formato no válido,<br/>Cuando el visitante confirma el envío de la solicitud de contacto,<br/>Entonces el sistema rechaza el envío e informa que el correo electrónico no tiene un formato válido.</td>
    </tr>
    <tr>
      <td align="left">HU05</td>
      <td align="left">E1</td>
      <td align="left">Consulta de arquitectura técnica del sistema</td>
      <td align="left">Como visitante quiero conocer la arquitectura técnica de SafePlant para comprender cómo se integran los dispositivos embebidos, el IoT Gateway, la nube, la aplicación móvil de operación y la aplicación web de configuración.</td>
      <td align="left"><strong>Escenario 1: Capa de dispositivos embebidos</strong><br/>Dado que el visitante accede al sitio web de SafePlant,<br/>Cuando el visitante consulta la sección de arquitectura técnica,<br/>Entonces el sitio presenta información sobre los dispositivos ESP32, sensores de CO₂, ruido y presencia, y actuadores físicos del sistema.<br/><br/><strong>Escenario 2: Capa de IoT Gateway</strong><br/>Dado que el visitante accede al sitio web de SafePlant,<br/>Cuando el visitante consulta la sección de arquitectura técnica,<br/>Entonces el sitio presenta información sobre el IoT Gateway basado en Raspberry Pi con procesamiento local y persistencia de contingencia.<br/><br/><strong>Escenario 3: Capa de plataforma en la nube y canales de usuario</strong><br/>Dado que el visitante accede al sitio web de SafePlant,<br/>Cuando el visitante consulta la sección de arquitectura técnica,<br/>Entonces el sitio presenta información sobre la API REST, la base de datos relacional, la aplicación móvil de monitoreo y control operativo, y la aplicación web de configuración y actualizaciones del sistema.</td>
    </tr>
    <tr>
      <td align="left">HU06</td>
      <td align="left">E1</td>
      <td align="left">Navegación hacia la aplicación móvil de operación</td>
      <td align="left">Como visitante quiero acceder a la aplicación móvil de monitoreo y control operativo desde el sitio informativo para iniciar sesión como supervisor de seguridad.</td>
      <td align="left"><strong>Escenario 1: Redirección hacia el acceso de la aplicación móvil</strong><br/>Dado que el visitante se encuentra en el sitio web de SafePlant,<br/>Cuando el visitante solicita el acceso a la aplicación móvil de operación,<br/>Entonces el sistema redirige al visitante al punto de acceso o autenticación de la aplicación móvil de SafePlant.<br/><br/><strong>Escenario 2: Acceso identificable en la navegación principal</strong><br/>Dado que el visitante consulta el sitio web de SafePlant,<br/>Cuando el visitante revisa la navegación principal del sitio,<br/>Entonces el sitio presenta un acceso identificable hacia la aplicación móvil de monitoreo y control operativo.</td>
    </tr>
    <tr>
      <td align="left">HU07</td>
      <td align="left">E2</td>
      <td align="left">Inicio de sesión de supervisor de seguridad en la aplicación móvil</td>
      <td align="left">Como supervisor de seguridad quiero iniciar sesión en la aplicación móvil para acceder de forma remota a las funciones de monitoreo y control operativo de la planta.</td>
      <td align="left"><strong>Escenario 1: Autenticación exitosa de supervisor en la aplicación móvil</strong><br/>Dado que el supervisor de seguridad dispone de credenciales válidas registradas en el sistema,<br/>Cuando el supervisor proporciona sus credenciales de acceso en la aplicación móvil,<br/>Entonces el sistema concede el acceso a la aplicación móvil con el rol de supervisor de seguridad y habilita las funciones de monitoreo y control operativo remoto.<br/><br/><strong>Escenario 2: Credenciales no reconocidas de supervisor</strong><br/>Dado que el supervisor de seguridad intenta acceder a la aplicación móvil,<br/>Cuando el supervisor proporciona credenciales no reconocidas por el sistema,<br/>Entonces el sistema deniega el acceso e informa que las credenciales no son válidas.<br/><br/><strong>Escenario 3: Cuenta de supervisor deshabilitada</strong><br/>Dado que el supervisor de seguridad posee una cuenta deshabilitada en el sistema,<br/>Cuando el supervisor proporciona credenciales asociadas a la cuenta deshabilitada en la aplicación móvil,<br/>Entonces el sistema deniega el acceso e informa que la cuenta se encuentra deshabilitada.<br/><br/><strong>Escenario 4: Restricción de funciones de configuración en la aplicación móvil</strong><br/>Dado que el supervisor de seguridad mantiene una sesión activa en la aplicación móvil,<br/>Cuando el supervisor intenta acceder a funciones de configuración del sistema,<br/>Entonces el sistema deniega la operación e informa que la configuración se realiza en la aplicación web.</td>
    </tr>
    <tr>
      <td align="left">HU08</td>
      <td align="left">E2</td>
      <td align="left">Inicio de sesión de encargado de planta en la aplicación web</td>
      <td align="left">Como encargado de planta quiero iniciar sesión en la aplicación web para acceder a las funciones de configuración del sistema, administración de usuarios y actualizaciones.</td>
      <td align="left"><strong>Escenario 1: Autenticación exitosa de encargado de planta</strong><br/>Dado que el encargado de planta dispone de credenciales válidas registradas en el sistema,<br/>Cuando el encargado proporciona sus credenciales de acceso en la aplicación web,<br/>Entonces el sistema concede el acceso a la aplicación web con el rol de encargado de planta y habilita las funciones de configuración y actualizaciones.<br/><br/><strong>Escenario 2: Credenciales no reconocidas de encargado de planta</strong><br/>Dado que el encargado de planta intenta acceder a la aplicación web,<br/>Cuando el encargado proporciona credenciales no reconocidas por el sistema,<br/>Entonces el sistema deniega el acceso e informa que las credenciales no son válidas.<br/><br/><strong>Escenario 3: Restricción de control operativo en la aplicación web</strong><br/>Dado que el encargado de planta mantiene una sesión activa en la aplicación web,<br/>Cuando el encargado intenta ejecutar control operativo remoto de actuadores,<br/>Entonces el sistema deniega la operación e informa que el control operativo se realiza en la aplicación móvil.</td>
    </tr>
    <tr>
      <td align="left">HU09</td>
      <td align="left">E1</td>
      <td align="left">Navegación hacia la aplicación web de configuración</td>
      <td align="left">Como visitante quiero acceder a la aplicación web de configuración desde el sitio informativo para iniciar sesión como encargado de planta.</td>
      <td align="left"><strong>Escenario 1: Redirección hacia el acceso de la aplicación web</strong><br/>Dado que el visitante se encuentra en el sitio web de SafePlant,<br/>Cuando el visitante solicita el acceso a la aplicación web de configuración,<br/>Entonces el sistema redirige al visitante al punto de autenticación de la aplicación web de SafePlant.<br/><br/><strong>Escenario 2: Acceso identificable en la navegación principal</strong><br/>Dado que el visitante consulta el sitio web de SafePlant,<br/>Cuando el visitante revisa la navegación principal del sitio,<br/>Entonces el sitio presenta un acceso identificable hacia la aplicación web de configuración y actualizaciones.</td>
    </tr>
    <tr>
      <td align="left">HU10</td>
      <td align="left">E2</td>
      <td align="left">Cierre de sesión de usuario autenticado</td>
      <td align="left">Como usuario autenticado del sistema quiero finalizar mi sesión activa en la aplicación móvil o en la aplicación web para proteger el acceso a las funciones del sistema ante el uso no autorizado de mi cuenta.</td>
      <td align="left"><strong>Escenario 1: Cierre de sesión exitoso en la aplicación móvil</strong><br/>Dado que un supervisor de seguridad mantiene una sesión activa en la aplicación móvil,<br/>Cuando el supervisor solicita finalizar su sesión,<br/>Entonces el sistema cierra la sesión activa y restringe el acceso a las funciones protegidas de la aplicación móvil.<br/><br/><strong>Escenario 2: Cierre de sesión exitoso en la aplicación web</strong><br/>Dado que un encargado de planta mantiene una sesión activa en la aplicación web,<br/>Cuando el encargado solicita finalizar su sesión,<br/>Entonces el sistema cierra la sesión activa y restringe el acceso a las funciones protegidas de la aplicación web.<br/><br/><strong>Escenario 3: Intento de acceso posterior al cierre de sesión</strong><br/>Dado que un usuario ha finalizado su sesión en la aplicación móvil o en la aplicación web,<br/>Cuando el usuario intenta acceder a una función protegida sin autenticarse nuevamente,<br/>Entonces el sistema deniega el acceso e informa que se requiere autenticación.</td>
    </tr>
    <tr>
      <td align="left">HU11</td>
      <td align="left">E2</td>
      <td align="left">Creación de cuenta de usuario por encargado de planta</td>
      <td align="left">Como encargado de planta quiero crear cuentas de usuario para supervisores de seguridad y encargados de planta en la aplicación web para habilitar el acceso controlado a la operación móvil y a la configuración web.</td>
      <td align="left"><strong>Escenario 1: Creación de cuenta de supervisor de seguridad</strong><br/>Dado que el encargado de planta accede a la administración de usuarios en la aplicación web,<br/>Cuando el encargado registra una nueva cuenta con nombre, correo electrónico y rol de supervisor de seguridad,<br/>Entonces el sistema crea la cuenta y habilita el acceso del usuario a la aplicación móvil con el rol asignado.<br/><br/><strong>Escenario 2: Creación de cuenta de encargado de planta</strong><br/>Dado que el encargado de planta accede a la administración de usuarios en la aplicación web,<br/>Cuando el encargado registra una nueva cuenta con nombre, correo electrónico y rol de encargado de planta,<br/>Entonces el sistema crea la cuenta y habilita el acceso del usuario a la aplicación web con el rol asignado.<br/><br/><strong>Escenario 3: Creación de cuenta con correo duplicado</strong><br/>Dado que el encargado de planta intenta registrar una nueva cuenta de usuario en la aplicación web,<br/>Cuando el correo electrónico proporcionado ya se encuentra registrado en el sistema,<br/>Entonces el sistema rechaza la creación e informa que el correo electrónico ya está en uso.</td>
    </tr>
    <tr>
      <td align="left">HU12</td>
      <td align="left">E2</td>
      <td align="left">Asignación de roles y permisos de usuario</td>
      <td align="left">Como encargado de planta quiero asignar y modificar roles y permisos de los usuarios del sistema en la aplicación web para controlar el acceso a la operación móvil y a la configuración web.</td>
      <td align="left"><strong>Escenario 1: Asignación de rol a usuario existente</strong><br/>Dado que existe una cuenta de usuario registrada en el sistema<br/>Y el encargado de planta accede a la administración de roles en la aplicación web,<br/>Cuando el encargado asigna un rol válido de supervisor de seguridad o encargado de planta a la cuenta del usuario,<br/>Entonces el sistema actualiza el rol del usuario y aplica los permisos correspondientes al canal autorizado.<br/><br/><strong>Escenario 2: Asignación de rol no reconocido</strong><br/>Dado que el encargado de planta intenta asignar un rol a un usuario en la aplicación web,<br/>Cuando el rol proporcionado no se encuentra definido en el sistema,<br/>Entonces el sistema rechaza la asignación e informa que el rol no es válido.</td>
    </tr>
    <tr>
      <td align="left">HU13</td>
      <td align="left">E2</td>
      <td align="left">Recuperación de credenciales de acceso</td>
      <td align="left">Como usuario registrado del sistema quiero recuperar el acceso a mi cuenta cuando olvide mis credenciales para restablecer mi acceso a la aplicación móvil o a la aplicación web según mi rol.</td>
      <td align="left"><strong>Escenario 1: Solicitud de recuperación con correo registrado</strong><br/>Dado que un usuario registrado ha olvidado sus credenciales de acceso,<br/>Cuando el usuario solicita la recuperación de acceso con un correo electrónico registrado en el sistema desde la aplicación móvil o la aplicación web,<br/>Entonces el sistema genera un proceso de recuperación y envía las instrucciones al correo electrónico asociado.<br/><br/><strong>Escenario 2: Solicitud de recuperación con correo no registrado</strong><br/>Dado que una persona solicita la recuperación de acceso,<br/>Cuando el correo electrónico proporcionado no se encuentra registrado en el sistema,<br/>Entonces el sistema informa que no existe una cuenta asociada al correo electrónico proporcionado.<br/><br/><strong>Escenario 3: Restablecimiento con proceso de recuperación expirado</strong><br/>Dado que un usuario intenta restablecer sus credenciales,<br/>Cuando el proceso de recuperación ha superado el tiempo de validez configurado,<br/>Entonces el sistema rechaza el restablecimiento e informa que el proceso de recuperación ha expirado.</td>
    </tr>
    <tr>
      <td align="left">HU14</td>
      <td align="left">E3</td>
      <td align="left">Dashboard consolidado de la planta</td>
      <td align="left">Como supervisor de seguridad quiero visualizar el estado consolidado de todas las zonas críticas de la planta en la aplicación móvil para obtener una visión general del estado ambiental y de seguridad en tiempo real de forma remota.</td>
      <td align="left"><strong>Escenario 1: Vista general de zonas críticas</strong><br/>Dado que el supervisor de seguridad accede a la aplicación móvil autenticado,<br/>Cuando el sistema carga el estado de las zonas críticas registradas,<br/>Entonces la aplicación móvil presenta el resumen de CO₂ en ppm, ruido en dB, presencia y estado de alerta de cada zona.<br/><br/><strong>Escenario 2: Identificación de zonas en condición de riesgo</strong><br/>Dado que una o más zonas críticas presentan condiciones fuera de los límites permitidos,<br/>Cuando el supervisor consulta el dashboard consolidado en la aplicación móvil,<br/>Entonces el sistema identifica las zonas que requieren atención inmediata.<br/><br/><strong>Escenario 3: Planta sin zonas críticas registradas</strong><br/>Dado que el sistema no posee zonas críticas registradas,<br/>Cuando el supervisor consulta el dashboard consolidado en la aplicación móvil,<br/>Entonces el sistema informa que no existen zonas críticas configuradas para monitoreo.</td>
    </tr>
    <tr>
      <td align="left">HU15</td>
      <td align="left">E3</td>
      <td align="left">Monitoreo de CO₂ en tiempo real por zona</td>
      <td align="left">Como supervisor de seguridad quiero monitorear en tiempo real la concentración de CO₂ en ppm de una zona crítica desde la aplicación móvil para identificar oportunamente acumulaciones peligrosas del gas en el ambiente industrial.</td>
      <td align="left"><strong>Escenario 1: Consulta de concentración de CO₂ actual</strong><br/>Dado que el supervisor consulta una zona crítica con sensor de CO₂ activo desde la aplicación móvil,<br/>Cuando el sensor MQ-135 registra una concentración de CO₂ en ppm,<br/>Entonces el sistema registra y presenta el valor actual de CO₂ de la zona en la aplicación móvil.<br/><br/><strong>Escenario 2: Actualización de medición de CO₂</strong><br/>Dado que el supervisor monitorea una zona crítica en la aplicación móvil<br/>Y el sensor de CO₂ genera una nueva medición,<br/>Cuando el sistema recibe la nueva medición a través del IoT Gateway,<br/>Entonces el sistema actualiza el valor de CO₂ correspondiente a la zona monitoreada en la aplicación móvil.<br/><br/><strong>Escenario 3: Sensor de CO₂ sin transmisión de datos</strong><br/>Dado que el supervisor monitorea una zona crítica en la aplicación móvil,<br/>Cuando el sensor de CO₂ deja de enviar mediciones dentro del intervalo esperado,<br/>Entonces el sistema identifica el sensor como no disponible y conserva la última medición válida registrada.<br/><br/><strong>Escenario 4: Medición de CO₂ fuera del rango válido del sensor</strong><br/>Dado que el sistema recibe una medición de CO₂ desde el dispositivo embebido,<br/>Cuando el valor de la medición se encuentra fuera del rango operativo del sensor MQ-135,<br/>Entonces el sistema descarta la medición y registra el evento como medición inválida de CO₂.</td>
    </tr>
    <tr>
      <td align="left">HU16</td>
      <td align="left">E3</td>
      <td align="left">Monitoreo de ruido en tiempo real por zona</td>
      <td align="left">Como supervisor de seguridad quiero monitorear en tiempo real el nivel de ruido en dB de una zona crítica desde la aplicación móvil para identificar oportunamente condiciones de exposición sonora peligrosa para los operarios.</td>
      <td align="left"><strong>Escenario 1: Consulta de nivel de ruido actual</strong><br/>Dado que el supervisor consulta una zona crítica con sensor de ruido activo desde la aplicación móvil,<br/>Cuando el decibelímetro registra un nivel sonoro en dB,<br/>Entonces el sistema registra y presenta el valor actual de ruido de la zona en la aplicación móvil.<br/><br/><strong>Escenario 2: Actualización de medición de ruido</strong><br/>Dado que el supervisor monitorea una zona crítica en la aplicación móvil<br/>Y el sensor de ruido genera una nueva medición,<br/>Cuando el sistema recibe la nueva medición a través del IoT Gateway,<br/>Entonces el sistema actualiza el valor de ruido correspondiente a la zona monitoreada en la aplicación móvil.<br/><br/><strong>Escenario 3: Sensor de ruido sin transmisión de datos</strong><br/>Dado que el supervisor monitorea una zona crítica en la aplicación móvil,<br/>Cuando el decibelímetro deja de enviar mediciones dentro del intervalo esperado,<br/>Entonces el sistema identifica el sensor como no disponible y conserva la última medición válida registrada.</td>
    </tr>
    <tr>
      <td align="left">HU17</td>
      <td align="left">E3</td>
      <td align="left">Monitoreo de presencia de personal por zona</td>
      <td align="left">Como supervisor de seguridad quiero monitorear la presencia de personal en una zona crítica desde la aplicación móvil para determinar si existen operarios expuestos a condiciones ambientales de riesgo.</td>
      <td align="left"><strong>Escenario 1: Detección de presencia por sensor PIR</strong><br/>Dado que el supervisor monitorea una zona crítica con sensor PIR activo desde la aplicación móvil,<br/>Cuando el sensor PIR detecta movimiento en la zona,<br/>Entonces el sistema registra la presencia de personal en la zona y la presenta en la aplicación móvil.<br/><br/><strong>Escenario 2: Ausencia de personal en zona monitoreada</strong><br/>Dado que el supervisor monitorea una zona crítica en la aplicación móvil,<br/>Cuando el sensor PIR no detecta actividad en el intervalo configurado,<br/>Entonces el sistema registra la zona como sin personal presente.<br/><br/><strong>Escenario 3: Sensor PIR sin transmisión de datos</strong><br/>Dado que el supervisor monitorea una zona crítica en la aplicación móvil,<br/>Cuando el sensor PIR deja de enviar señales dentro del intervalo esperado,<br/>Entonces el sistema identifica el sensor como no disponible y conserva el último estado de presencia registrado.</td>
    </tr>
    <tr>
      <td align="left">HU18</td>
      <td align="left">E3</td>
      <td align="left">Visualización de alertas activas</td>
      <td align="left">Como supervisor de seguridad quiero visualizar las alertas ambientales y de seguridad activas en la planta desde la aplicación móvil para atender oportunamente las condiciones de riesgo detectadas por el sistema.</td>
      <td align="left"><strong>Escenario 1: Listado de alertas activas en la planta</strong><br/>Dado que el sistema ha detectado una o más condiciones de riesgo sin resolver,<br/>Cuando el supervisor consulta las alertas activas en la aplicación móvil,<br/>Entonces el sistema presenta la zona, el tipo de alerta, la medición asociada y la fecha de detección de cada alerta activa.<br/><br/><strong>Escenario 2: Retiro de alerta por normalización de condición</strong><br/>Dado que el supervisor visualiza las alertas activas en la aplicación móvil,<br/>Cuando una condición de riesgo finaliza en una zona monitoreada,<br/>Entonces el sistema retira la alerta correspondiente del listado de alertas activas.<br/><br/><strong>Escenario 3: Ausencia de alertas activas en la planta</strong><br/>Dado que no existen condiciones de riesgo activas en ninguna zona,<br/>Cuando el supervisor consulta las alertas activas en la aplicación móvil,<br/>Entonces el sistema informa que no existen alertas activas en ese momento.</td>
    </tr>
    <tr>
      <td align="left">HU19</td>
      <td align="left">E3</td>
      <td align="left">Mapa digitalizado de riesgos por zona</td>
      <td align="left">Como supervisor de seguridad quiero visualizar un mapa digitalizado de la planta con el estado de riesgo de cada zona crítica en la aplicación móvil para identificar geográficamente las áreas que requieren atención inmediata.</td>
      <td align="left"><strong>Escenario 1: Mapa con zonas en estado seguro</strong><br/>Dado que todas las zonas críticas registradas se encuentran dentro de los límites permitidos,<br/>Cuando el supervisor consulta el mapa digitalizado de riesgos en la aplicación móvil,<br/>Entonces el sistema presenta todas las zonas con su estado ambiental seguro en el mapa de la planta.<br/><br/><strong>Escenario 2: Mapa con zonas en condición de riesgo</strong><br/>Dado que una o más zonas críticas presentan condiciones fuera de los límites permitidos,<br/>Cuando el supervisor consulta el mapa digitalizado de riesgos en la aplicación móvil,<br/>Entonces el sistema identifica en el mapa las zonas que presentan condición de riesgo activa.<br/><br/><strong>Escenario 3: Zona sin posición definida en el mapa</strong><br/>Dado que existe una zona crítica registrada sin posición definida en el mapa,<br/>Cuando el supervisor consulta el mapa digitalizado de riesgos en la aplicación móvil,<br/>Entonces el sistema presenta la zona en el listado de zonas sin ubicación e informa que la posición de la zona no se encuentra configurada en el mapa.</td>
    </tr>
    <tr>
      <td align="left">HU20</td>
      <td align="left">E3</td>
      <td align="left">Gestión de zonas críticas</td>
      <td align="left">Como encargado de planta quiero registrar y administrar las zonas críticas de la planta en la aplicación web para asociar dispositivos IoT, umbrales ambientales y reglas de acceso a cada área monitoreada.</td>
      <td align="left"><strong>Escenario 1: Registro de zona crítica</strong><br/>Dado que el encargado de planta accede a la administración de zonas críticas en la aplicación web,<br/>Cuando el encargado registra una nueva zona con nombre, descripción y ubicación en el mapa,<br/>Entonces el sistema almacena la zona y la habilita para la asignación de dispositivos y configuraciones.<br/><br/><strong>Escenario 2: Modificación de zona crítica existente</strong><br/>Dado que existe una zona crítica registrada en el sistema,<br/>Cuando el encargado de planta modifica los datos de la zona en la aplicación web,<br/>Entonces el sistema actualiza la información de la zona conservando su historial de eventos asociado.<br/><br/><strong>Escenario 3: Registro de zona con nombre duplicado</strong><br/>Dado que el encargado de planta intenta registrar una zona crítica en la aplicación web,<br/>Cuando el nombre de la zona ya existe en el sistema,<br/>Entonces el sistema rechaza el registro e informa que la zona ya se encuentra registrada.</td>
    </tr>
    <tr>
      <td align="left">HU21</td>
      <td align="left">E3</td>
      <td align="left">Configuración de umbrales ambientales por zona</td>
      <td align="left">Como encargado de planta quiero configurar los límites permitidos de CO₂ en ppm y ruido en dB para cada zona crítica en la aplicación web para determinar cuándo una condición ambiental representa un riesgo para los operarios.</td>
      <td align="left"><strong>Escenario 1: Configuración de límites ambientales</strong><br/>Dado que el encargado de planta dispone de una zona crítica registrada en la aplicación web,<br/>Cuando el encargado configura los límites permitidos de CO₂ en ppm y ruido en dB,<br/>Entonces el sistema almacena los límites asociados a la zona.<br/><br/><strong>Escenario 2: Modificación de límite ambiental existente</strong><br/>Dado que una zona crítica tiene límites ambientales configurados,<br/>Cuando el encargado de planta modifica uno de los límites en la aplicación web,<br/>Entonces el sistema reemplaza el valor anterior por el nuevo límite configurado.<br/><br/><strong>Escenario 3: Límite ambiental fuera del rango permitido por el sistema</strong><br/>Dado que el encargado de planta configura un límite ambiental en la aplicación web,<br/>Cuando el valor ingresado no cumple las restricciones establecidas por el sistema,<br/>Entonces el sistema rechaza la configuración e informa que el valor no es válido.</td>
    </tr>
    <tr>
      <td align="left">HU22</td>
      <td align="left">E3</td>
      <td align="left">Registro de dispositivos IoT por zona</td>
      <td align="left">Como encargado de planta quiero registrar sensores y actuadores en una zona crítica desde la aplicación web para habilitar el monitoreo ambiental y las respuestas automáticas en esa área de la planta.</td>
      <td align="left"><strong>Escenario 1: Registro de sensor en zona crítica</strong><br/>Dado que existe una zona crítica registrada en el sistema<br/>Y el encargado de planta accede a la administración de dispositivos en la aplicación web,<br/>Cuando el encargado asocia un sensor con su tipo, identificador y dirección del dispositivo embebido,<br/>Entonces el sistema registra el sensor y lo habilita para recibir mediciones.<br/><br/><strong>Escenario 2: Registro de actuador en zona crítica</strong><br/>Dado que existe una zona crítica registrada en el sistema<br/>Y el encargado de planta accede a la administración de dispositivos en la aplicación web,<br/>Cuando el encargado asocia un actuador con su tipo, identificador y dirección del dispositivo embebido,<br/>Entonces el sistema registra el actuador y lo habilita para recibir órdenes de control.<br/><br/><strong>Escenario 3: Registro de dispositivo con identificador duplicado</strong><br/>Dado que el encargado de planta intenta registrar un dispositivo IoT en la aplicación web,<br/>Cuando el identificador del dispositivo ya se encuentra asociado en el sistema,<br/>Entonces el sistema rechaza el registro e informa que el dispositivo ya está en uso.</td>
    </tr>
    <tr>
      <td align="left">HU23</td>
      <td align="left">E3</td>
      <td align="left">Consulta de historial de mediciones y eventos ambientales</td>
      <td align="left">Como supervisor de seguridad quiero consultar el historial de mediciones, alertas y acciones automáticas de una zona crítica en la aplicación móvil para analizar incidentes y verificar el comportamiento del sistema ante condiciones de riesgo.</td>
      <td align="left"><strong>Escenario 1: Registro automático de evento ambiental</strong><br/>Dado que el sistema detecta una condición ambiental fuera de los límites permitidos,<br/>Cuando el sistema procesa la condición,<br/>Entonces el sistema registra el evento con la zona, el tipo de condición, la medición y la fecha correspondiente.<br/><br/><strong>Escenario 2: Consulta de historial por zona y periodo</strong><br/>Dado que existen eventos registrados en una zona crítica,<br/>Cuando el supervisor consulta el historial de eventos de la zona para un periodo determinado en la aplicación móvil,<br/>Entonces el sistema proporciona los eventos registrados correspondientes al periodo consultado.<br/><br/><strong>Escenario 3: Historial sin registros en el periodo consultado</strong><br/>Dado que una zona crítica no posee eventos en el periodo consultado,<br/>Cuando el supervisor consulta el historial de la zona en la aplicación móvil,<br/>Entonces el sistema informa que no existen eventos registrados para el periodo indicado.</td>
    </tr>
    <tr>
      <td align="left">HU24</td>
      <td align="left">E4</td>
      <td align="left">Registro de operarios con credencial RFID</td>
      <td align="left">Como encargado de planta quiero registrar operarios con su credencial RFID en la aplicación web para identificar al personal autorizado que puede ingresar a zonas críticas de la planta.</td>
      <td align="left"><strong>Escenario 1: Registro de operario con credencial RFID válida</strong><br/>Dado que el encargado de planta accede a la administración de personal autorizado en la aplicación web,<br/>Cuando el encargado registra un operario con nombre, identificador laboral y código de credencial RFID,<br/>Entonces el sistema almacena al operario y habilita su credencial para el control de acceso físico.<br/><br/><strong>Escenario 2: Registro de operario con credencial RFID duplicada</strong><br/>Dado que el encargado de planta intenta registrar un operario en la aplicación web,<br/>Cuando el código de credencial RFID ya se encuentra asignado a otro operario,<br/>Entonces el sistema rechaza el registro e informa que la credencial RFID ya está en uso.<br/><br/><strong>Escenario 3: Desactivación de credencial RFID de operario</strong><br/>Dado que un operario registrado posee una credencial RFID activa,<br/>Cuando el encargado de planta solicita la desactivación de la credencial del operario en la aplicación web,<br/>Entonces el sistema desactiva la credencial e impide el acceso físico del operario a zonas críticas.</td>
    </tr>
    <tr>
      <td align="left">HU25</td>
      <td align="left">E4</td>
      <td align="left">Autorización de ingreso a zona crítica</td>
      <td align="left">Como operario de planta quiero que el sistema autorice mi ingreso a una zona crítica cuando las condiciones ambientales sean seguras para acceder al área de trabajo sin exponerme a riesgos ambientales inmediatos.</td>
      <td align="left"><strong>Escenario 1: Ingreso autorizado en condiciones ambientales seguras</strong><br/>Dado que un operario registrado se presenta en el punto de acceso de una zona crítica<br/>Y las condiciones de CO₂ y ruido de la zona se encuentran dentro de los límites permitidos,<br/>Cuando el lector RFID procesa la credencial del operario,<br/>Entonces el sistema autoriza el ingreso del operario a la zona.<br/><br/><strong>Escenario 2: Ingreso denegado por credencial RFID no reconocida</strong><br/>Dado que una persona se presenta en el punto de acceso de una zona crítica,<br/>Cuando el lector RFID procesa una credencial no registrada en el sistema,<br/>Entonces el sistema deniega el ingreso e informa que la credencial no se encuentra autorizada.<br/><br/><strong>Escenario 3: Ingreso denegado por credencial RFID desactivada</strong><br/>Dado que un operario con credencial desactivada se presenta en el punto de acceso,<br/>Cuando el lector RFID procesa la credencial del operario,<br/>Entonces el sistema deniega el ingreso e informa que la credencial se encuentra desactivada.</td>
    </tr>
    <tr>
      <td align="left">HU26</td>
      <td align="left">E4</td>
      <td align="left">Denegación de acceso por condición ambiental peligrosa</td>
      <td align="left">Como operario de planta quiero que el sistema restrinja mi ingreso a una zona crítica cuando exista una condición ambiental peligrosa para evitar exponerme a niveles peligrosos de CO₂ o ruido excesivo.</td>
      <td align="left"><strong>Escenario 1: Acceso denegado por concentración peligrosa de CO₂</strong><br/>Dado que un operario registrado se presenta en el punto de acceso de una zona crítica<br/>Y la concentración de CO₂ en la zona supera el límite permitido,<br/>Cuando el lector RFID procesa la credencial del operario,<br/>Entonces el sistema deniega el ingreso e informa que la zona presenta una condición peligrosa de CO₂.<br/><br/><strong>Escenario 2: Acceso denegado por nivel de ruido peligroso</strong><br/>Dado que un operario registrado se presenta en el punto de acceso de una zona crítica<br/>Y el nivel de ruido en la zona supera el límite permitido,<br/>Cuando el lector RFID procesa la credencial del operario,<br/>Entonces el sistema deniega el ingreso e informa que la zona presenta una condición peligrosa de ruido.<br/><br/><strong>Escenario 3: Acceso denegado por fallo en sensor ambiental de la zona</strong><br/>Dado que un operario registrado se presenta en el punto de acceso de una zona crítica<br/>Y el sensor de CO₂ o ruido de la zona se encuentra no disponible,<br/>Cuando el lector RFID procesa la credencial del operario,<br/>Entonces el sistema deniega el ingreso e informa que la zona no puede evaluarse por indisponibilidad de sensores ambientales.</td>
    </tr>
    <tr>
      <td align="left">HU27</td>
      <td align="left">E4</td>
      <td align="left">Consulta de personal presente en zona crítica</td>
      <td align="left">Como supervisor de seguridad quiero consultar el personal presente en una zona crítica desde la aplicación móvil para conocer qué operarios se encuentran expuestos a condiciones ambientales de riesgo.</td>
      <td align="left"><strong>Escenario 1: Personal identificado presente en zona</strong><br/>Dado que uno o más operarios registrados se encuentran en una zona crítica,<br/>Cuando el supervisor consulta el personal presente en la zona desde la aplicación móvil,<br/>Entonces el sistema presenta el listado de operarios identificados en esa zona.<br/><br/><strong>Escenario 2: Presencia detectada sin identificación de operario</strong><br/>Dado que el sensor PIR detecta presencia en una zona crítica<br/>Y ningún operario ha sido identificado por el lector RFID en la zona,<br/>Cuando el supervisor consulta el personal presente en la zona desde la aplicación móvil,<br/>Entonces el sistema informa que existe presencia no identificada en la zona.<br/><br/><strong>Escenario 3: Zona sin personal presente</strong><br/>Dado que no existen operarios en una zona crítica,<br/>Cuando el supervisor consulta el personal presente en la zona desde la aplicación móvil,<br/>Entonces el sistema informa que no existe personal presente en la zona.</td>
    </tr>
    <tr>
      <td align="left">HU28</td>
      <td align="left">E4</td>
      <td align="left">Registro histórico de accesos RFID a zonas críticas</td>
      <td align="left">Como supervisor de seguridad quiero consultar el historial de accesos físicos a zonas críticas registrados por el lector RFID desde la aplicación móvil para analizar los patrones de ingreso y las exposiciones de personal a áreas de riesgo.</td>
      <td align="left"><strong>Escenario 1: Registro de acceso autorizado</strong><br/>Dado que un operario registrado ingresa a una zona crítica con condiciones ambientales seguras,<br/>Cuando el lector RFID procesa la credencial del operario,<br/>Entonces el sistema registra el acceso con el identificador del operario, la zona, el resultado autorizado y la fecha del evento.<br/><br/><strong>Escenario 2: Registro de acceso denegado</strong><br/>Dado que un operario registrado intenta ingresar a una zona crítica con condición ambiental peligrosa,<br/>Cuando el lector RFID procesa la credencial del operario,<br/>Entonces el sistema registra el intento de acceso con el identificador del operario, la zona, el resultado denegado, el motivo y la fecha del evento.<br/><br/><strong>Escenario 3: Historial de accesos sin registros en el periodo</strong><br/>Dado que una zona crítica no posee registros de acceso en el periodo consultado,<br/>Cuando el supervisor consulta el historial de accesos de la zona en la aplicación móvil,<br/>Entonces el sistema informa que no existen registros de acceso para el periodo indicado.</td>
    </tr>
    <tr>
      <td align="left">HU29</td>
      <td align="left">E4</td>
      <td align="left">Cruce de presencia de personal con niveles de CO₂</td>
      <td align="left">Como supervisor de seguridad quiero que el sistema evalúe simultáneamente la presencia de personal y los niveles de CO₂ en una zona crítica y me presente la alerta resultante en la aplicación móvil para determinar si existen operarios expuestos a concentraciones peligrosas del gas.</td>
      <td align="left"><strong>Escenario 1: Exposición de personal a CO₂ excesivo</strong><br/>Dado que el sistema detecta personal presente en una zona crítica<br/>Y la concentración de CO₂ en la zona supera el límite permitido,<br/>Cuando el sistema evalúa las condiciones de la zona,<br/>Entonces el sistema identifica una condición de exposición a CO₂, genera una alerta de seguridad para la zona y la presenta en la aplicación móvil del supervisor.<br/><br/><strong>Escenario 2: CO₂ excesivo sin personal presente</strong><br/>Dado que el sistema detecta ausencia de personal en una zona crítica<br/>Y la concentración de CO₂ en la zona supera el límite permitido,<br/>Cuando el sistema evalúa las condiciones de la zona,<br/>Entonces el sistema identifica una condición de CO₂ excesivo sin exposición de personal y activa el extractor de aire sin activar la sirena preventiva.<br/><br/><strong>Escenario 3: Personal presente con CO₂ dentro del límite</strong><br/>Dado que el sistema detecta personal presente en una zona crítica<br/>Y la concentración de CO₂ se encuentra dentro del límite permitido,<br/>Cuando el sistema evalúa las condiciones de la zona,<br/>Entonces el sistema mantiene la zona en estado de exposición segura para el personal presente.</td>
    </tr>
    <tr>
      <td align="left">HU30</td>
      <td align="left">E5</td>
      <td align="left">Detección de exceso de CO₂</td>
      <td align="left">Como supervisor de seguridad quiero que el sistema detecte cuando la concentración de CO₂ supera el límite permitido en una zona crítica para activar oportunamente las medidas automáticas de purificación y prevención.</td>
      <td align="left"><strong>Escenario 1: CO₂ dentro del límite permitido</strong><br/>Dado que el sistema monitorea una zona crítica con un límite de CO₂ configurado,<br/>Cuando el sensor MQ-135 registra una concentración igual o inferior al límite permitido,<br/>Entonces el sistema mantiene la zona en estado ambiental permitido.<br/><br/><strong>Escenario 2: CO₂ por encima del límite permitido</strong><br/>Dado que el sistema monitorea una zona crítica con un límite de CO₂ configurado,<br/>Cuando el sensor MQ-135 registra una concentración superior al límite permitido,<br/>Entonces el sistema identifica una condición de CO₂ excesivo y genera una alerta ambiental visible en la aplicación móvil del supervisor.<br/><br/><strong>Escenario 3: Medición de CO₂ inválida descartada</strong><br/>Dado que el sistema recibe una medición de CO₂ desde el dispositivo embebido,<br/>Cuando la medición se encuentra fuera del rango válido del sensor MQ-135,<br/>Entonces el sistema descarta la medición y registra el evento como medición inválida de CO₂.</td>
    </tr>
    <tr>
      <td align="left">HU31</td>
      <td align="left">E5</td>
      <td align="left">Detección de ruido excesivo</td>
      <td align="left">Como supervisor de seguridad quiero que el sistema detecte cuando el nivel sonoro supera el límite permitido en una zona crítica para prevenir la exposición de los operarios a niveles de ruido peligrosos.</td>
      <td align="left"><strong>Escenario 1: Ruido dentro del límite permitido</strong><br/>Dado que el sistema monitorea una zona crítica con un límite sonoro configurado,<br/>Cuando el decibelímetro registra un nivel igual o inferior al límite permitido,<br/>Entonces el sistema mantiene la zona en estado sonoro permitido.<br/><br/><strong>Escenario 2: Ruido excesivo sin personal presente</strong><br/>Dado que el sistema detecta un nivel sonoro superior al límite permitido<br/>Y el sistema registra ausencia de personal en la zona,<br/>Cuando el sistema evalúa la condición ambiental,<br/>Entonces el sistema registra la exposición sonora sin activar la sirena preventiva dirigida a operarios.<br/><br/><strong>Escenario 3: Ruido excesivo con personal presente</strong><br/>Dado que el sistema detecta un nivel sonoro superior al límite permitido<br/>Y el sistema detecta personal presente en la zona,<br/>Cuando el sistema evalúa la condición ambiental,<br/>Entonces el sistema genera una alerta de exposición sonora visible en la aplicación móvil del supervisor y activa la sirena preventiva.</td>
    </tr>
    <tr>
      <td align="left">HU32</td>
      <td align="left">E5</td>
      <td align="left">Activación automática del extractor de aire por CO₂</td>
      <td align="left">Como supervisor de seguridad quiero que el sistema active automáticamente el extractor de aire mediante el relé de control cuando se detecte un exceso de CO₂ para reducir la concentración del gas y recuperar condiciones ambientales seguras.</td>
      <td align="left"><strong>Escenario 1: Activación del extractor por exceso de CO₂</strong><br/>Dado que una zona crítica presenta una concentración de CO₂ superior al límite permitido,<br/>Cuando el sistema confirma la condición de exceso de CO₂,<br/>Entonces el sistema activa el extractor de aire asociado a la zona mediante el relé de control.<br/><br/><strong>Escenario 2: Desactivación del extractor al normalizar CO₂</strong><br/>Dado que el extractor de aire se encuentra activo por una condición de CO₂ excesivo,<br/>Cuando la concentración de CO₂ retorna al rango permitido,<br/>Entonces el sistema desactiva el extractor de aire de la zona.<br/><br/><strong>Escenario 3: Fallo en la activación del extractor</strong><br/>Dado que el sistema determina que debe activar el extractor de aire,<br/>Cuando el relé de control no confirma la activación del extractor,<br/>Entonces el sistema registra el fallo y genera una alerta de actuador no disponible visible en la aplicación móvil del supervisor.<br/><br/><strong>Escenario 4: Pérdida de comunicación con el dispositivo embebido durante activación</strong><br/>Dado que el sistema envía la orden de activación al extractor de aire,<br/>Cuando el dispositivo embebido ESP32 no responde dentro del tiempo esperado,<br/>Entonces el sistema registra el fallo de comunicación y mantiene la alerta de CO₂ excesivo activa en la aplicación móvil del supervisor.</td>
    </tr>
    <tr>
      <td align="left">HU33</td>
      <td align="left">E5</td>
      <td align="left">Activación de sirena preventiva por exposición a condición peligrosa</td>
      <td align="left">Como supervisor de seguridad quiero que el sistema active la sirena preventiva cuando un operario se encuentre expuesto a una condición peligrosa de CO₂ o ruido excesivo para advertir inmediatamente sobre el riesgo existente y permitir la evacuación de la zona.</td>
      <td align="left"><strong>Escenario 1: Sirena activada por CO₂ peligroso con personal presente</strong><br/>Dado que el sistema detecta una concentración peligrosa de CO₂ en una zona crítica<br/>Y el sistema detecta personal presente en la zona,<br/>Cuando el sistema determina que existe exposición de operarios,<br/>Entonces el sistema activa la sirena preventiva de la zona.<br/><br/><strong>Escenario 2: Sirena activada por ruido peligroso con personal presente</strong><br/>Dado que el sistema detecta un nivel de ruido superior al límite permitido<br/>Y el sistema detecta personal presente en la zona,<br/>Cuando el sistema determina que existe exposición de operarios,<br/>Entonces el sistema activa la sirena preventiva de la zona.<br/><br/><strong>Escenario 3: Sirena inactiva en condiciones seguras con personal presente</strong><br/>Dado que el sistema detecta personal presente en una zona crítica,<br/>Cuando las concentraciones de CO₂ y los niveles de ruido se encuentran dentro de los límites permitidos,<br/>Entonces el sistema mantiene la sirena preventiva desactivada.<br/><br/><strong>Escenario 4: Desactivación de sirena al cesar condición de riesgo</strong><br/>Dado que la sirena preventiva se encuentra activa por una condición de exposición,<br/>Cuando la condición peligrosa desaparece y no existe otra condición de alarma activa en la zona,<br/>Entonces el sistema desactiva la sirena preventiva de la zona.</td>
    </tr>
    <tr>
      <td align="left">HU34</td>
      <td align="left">E5</td>
      <td align="left">Despliegue de mamparas acústicas por exposición sonora</td>
      <td align="left">Como supervisor de seguridad quiero que el sistema despliegue mamparas móviles de aislamiento acústico mediante servomotores cuando se detecte ruido excesivo con personal presente para reducir la exposición sonora de los operarios en la zona afectada.</td>
      <td align="left"><strong>Escenario 1: Despliegue de mamparas por ruido excesivo con personal</strong><br/>Dado que una zona crítica presenta un nivel de ruido superior al límite permitido<br/>Y el sistema detecta personal presente en la zona,<br/>Cuando el sistema confirma la condición de exposición sonora,<br/>Entonces el sistema activa los servomotores y despliega las mamparas acústicas de la zona.<br/><br/><strong>Escenario 2: Retracción de mamparas al normalizar el ruido</strong><br/>Dado que las mamparas acústicas se encuentran desplegadas por una condición de ruido excesivo,<br/>Cuando el nivel sonoro retorna al rango permitido,<br/>Entonces el sistema retrae las mamparas acústicas de la zona.<br/><br/><strong>Escenario 3: Fallo en el despliegue de mamparas acústicas</strong><br/>Dado que el sistema determina que debe desplegar las mamparas acústicas,<br/>Cuando el servomotor no confirma el despliegue dentro del tiempo esperado,<br/>Entonces el sistema registra el fallo y genera una alerta de actuador no disponible visible en la aplicación móvil del supervisor.</td>
    </tr>
    <tr>
      <td align="left">HU35</td>
      <td align="left">E5</td>
      <td align="left">Anulación manual remota de actuador en emergencia</td>
      <td align="left">Como supervisor de seguridad quiero anular manualmente el estado de un actuador de forma remota desde la aplicación móvil durante una emergencia para asumir el control directo de extractores, sirenas o mamparas cuando la respuesta automática no sea adecuada para la situación.</td>
      <td align="left"><strong>Escenario 1: Anulación manual remota de extractor en emergencia</strong><br/>Dado que el extractor de aire de una zona se encuentra activo automáticamente<br/>Y el supervisor de seguridad mantiene una sesión activa en la aplicación móvil,<br/>Cuando el supervisor solicita la anulación manual y activación forzada del extractor desde la aplicación móvil,<br/>Entonces el sistema aplica el estado solicitado al extractor y registra la anulación manual con el identificador del supervisor y la fecha del evento.<br/><br/><strong>Escenario 2: Anulación manual remota de sirena en emergencia</strong><br/>Dado que la sirena preventiva de una zona se encuentra activa automáticamente<br/>Y el supervisor de seguridad mantiene una sesión activa en la aplicación móvil,<br/>Cuando el supervisor solicita la desactivación manual de la sirena desde la aplicación móvil,<br/>Entonces el sistema desactiva la sirena y registra la anulación manual con el identificador del supervisor y la fecha del evento.<br/><br/><strong>Escenario 3: Anulación manual denegada sin rol de supervisor en la aplicación móvil</strong><br/>Dado que un usuario autenticado en la aplicación web o sin rol de supervisor de seguridad intenta anular un actuador,<br/>Cuando el usuario solicita la anulación manual de un actuador,<br/>Entonces el sistema rechaza la operación e informa que la anulación manual remota requiere el rol de supervisor de seguridad en la aplicación móvil.</td>
    </tr>
    <tr>
      <td align="left">HU36</td>
      <td align="left">E5</td>
      <td align="left">Registro de acciones automáticas ejecutadas</td>
      <td align="left">Como supervisor de seguridad quiero consultar las acciones automáticas ejecutadas por el sistema desde la aplicación móvil para verificar que los mecanismos de prevención respondieron ante las condiciones peligrosas detectadas.</td>
      <td align="left"><strong>Escenario 1: Registro de activación automática de actuador</strong><br/>Dado que el sistema activa un extractor, una sirena o una mampara acústica,<br/>Cuando la acción automática se ejecuta en la zona,<br/>Entonces el sistema registra el actuador, la acción realizada, la zona y el momento de ejecución.<br/><br/><strong>Escenario 2: Registro de desactivación automática de actuador</strong><br/>Dado que un actuador se encuentra activo por una condición ambiental,<br/>Cuando el sistema determina que la condición que originó la acción ha finalizado,<br/>Entonces el sistema registra la desactivación del actuador con la zona y el momento del evento.<br/><br/><strong>Escenario 3: Consulta de acciones automáticas desde la aplicación móvil</strong><br/>Dado que existen acciones automáticas registradas en una zona crítica,<br/>Cuando el supervisor consulta el registro de acciones desde la aplicación móvil,<br/>Entonces el sistema presenta las acciones ejecutadas con actuador, zona, resultado y momento de ejecución.<br/><br/><strong>Escenario 4: Registro de acción automática fallida</strong><br/>Dado que el sistema envía una orden automática a un actuador,<br/>Cuando el actuador no confirma la ejecución,<br/>Entonces el sistema registra la acción como fallida con el actuador, la zona y el motivo del fallo.</td>
    </tr>
    <tr>
      <td align="left">HU37</td>
      <td align="left">E5</td>
      <td align="left">Notificación física de alarma al operario expuesto</td>
      <td align="left">Como operario de planta quiero recibir una alarma física audible cuando me encuentre expuesto a una condición peligrosa de CO₂ o ruido excesivo para conocer la situación de riesgo y retirarme de la zona afectada.</td>
      <td align="left"><strong>Escenario 1: Alarma audible por exposición a CO₂ peligroso</strong><br/>Dado que el operario se encuentra en una zona crítica con condición peligrosa de CO₂,<br/>Cuando el sistema activa la sirena preventiva de la zona,<br/>Entonces el operario recibe la señal audible de alarma en el entorno físico de la zona.<br/><br/><strong>Escenario 2: Alarma audible por exposición a ruido excesivo</strong><br/>Dado que el operario se encuentra en una zona crítica con nivel de ruido superior al límite permitido,<br/>Cuando el sistema activa la sirena preventiva de la zona,<br/>Entonces el operario recibe la señal audible de alarma en el entorno físico de la zona.<br/><br/><strong>Escenario 3: Ausencia de alarma en condiciones seguras</strong><br/>Dado que el operario se encuentra en una zona crítica,<br/>Cuando las condiciones de CO₂ y ruido se encuentran dentro de los límites permitidos,<br/>Entonces el sistema mantiene la sirena preventiva desactivada en la zona.<br/><br/><strong>Escenario 4: Fallo de sirena con operario expuesto</strong><br/>Dado que el operario se encuentra en una zona con condición de riesgo activa,<br/>Cuando el buzzer de la sirena no responde a la orden de activación,<br/>Entonces el sistema registra el fallo del actuador y mantiene la alerta de exposición activa en la aplicación móvil del supervisor de seguridad.</td>
    </tr>
    <tr>
      <td align="left">HU38</td>
      <td align="left">E5</td>
      <td align="left">Actualización de parámetros de configuración del sistema</td>
      <td align="left">Como encargado de planta quiero aplicar actualizaciones de parámetros de configuración del sistema desde la aplicación web para mantener zonas, umbrales, dispositivos y reglas alineados con la operación de la planta.</td>
      <td align="left"><strong>Escenario 1: Actualización exitosa de parámetros de configuración</strong><br/>Dado que el encargado de planta mantiene una sesión activa en la aplicación web<br/>Y existen parámetros de configuración válidos para zonas, umbrales o dispositivos,<br/>Cuando el encargado confirma la actualización de los parámetros del sistema,<br/>Entonces el sistema almacena la nueva configuración y la deja disponible para el monitoreo y control operativo en la aplicación móvil.<br/><br/><strong>Escenario 2: Actualización con parámetros incompletos o inválidos</strong><br/>Dado que el encargado de planta intenta actualizar la configuración del sistema en la aplicación web,<br/>Cuando uno o más parámetros obligatorios están incompletos o no cumplen las restricciones del sistema,<br/>Entonces el sistema rechaza la actualización e informa los parámetros que deben corregirse.<br/><br/><strong>Escenario 3: Consulta de versión o estado de configuración aplicada</strong><br/>Dado que el encargado de planta accede a la sección de actualizaciones en la aplicación web,<br/>Cuando el encargado consulta el estado de la configuración del sistema,<br/>Entonces el sistema presenta la configuración vigente y la fecha de la última actualización aplicada.</td>
    </tr>
    <tr>
      <td align="left">HU39</td>
      <td align="left">E6</td>
      <td align="left">Tiempo de respuesta crítica en activación de actuadores</td>
      <td align="left">Como supervisor de seguridad quiero que el sistema active extractores, sirenas y mamparas acústicas dentro de un tiempo máximo de respuesta definido para reducir la exposición del personal a condiciones ambientales peligrosas en la planta industrial.</td>
      <td align="left"><strong>Escenario 1: Activación del extractor por exceso de CO₂ dentro del límite temporal</strong><br/>Dado que una zona crítica presenta una concentración de CO₂ superior al límite permitido<br/>Y el sensor MQ-135 transmite una medición válida al IoT Gateway<br/>Y el extractor de aire de la zona se encuentra operativo,<br/>Cuando el sistema confirma la condición de exceso de CO₂ en la zona,<br/>Entonces el sistema activa el extractor de aire mediante el relé de control en un intervalo inferior a 2 segundos contados desde el instante de la medición válida que originó la alerta.<br/><br/><strong>Escenario 2: Activación de sirena preventiva con personal presente dentro del límite temporal</strong><br/>Dado que una zona crítica presenta una condición peligrosa de CO₂ o de ruido superior al límite permitido<br/>Y el sistema registra personal presente en la zona<br/>Y la sirena preventiva de la zona se encuentra operativa,<br/>Cuando el sistema determina que existe exposición de operarios a la condición de riesgo,<br/>Entonces el sistema activa la sirena preventiva de la zona en un intervalo inferior a 2 segundos contados desde el instante en que se confirma la condición de riesgo con personal presente.<br/><br/><strong>Escenario 3: Despliegue de mamparas acústicas por exposición sonora dentro del límite temporal</strong><br/>Dado que una zona crítica presenta un nivel de ruido superior al límite permitido<br/>Y el sistema registra personal presente en la zona<br/>Y los servomotores de mamparas acústicas de la zona se encuentran operativos,<br/>Cuando el sistema confirma la condición de exposición sonora con personal presente,<br/>Entonces el sistema activa los servomotores y despliega las mamparas acústicas en un intervalo inferior a 2 segundos contados desde el instante en que se confirma la condición de riesgo sonoro.<br/><br/><strong>Escenario 4: Activación local del extractor durante indisponibilidad de conectividad hacia la nube</strong><br/>Dado que el IoT Gateway mantiene conectividad local con los dispositivos ESP32 de una zona crítica<br/>Y la conexión a internet de la planta se encuentra interrumpida<br/>Y una zona crítica presenta una concentración de CO₂ superior al límite permitido con medición válida recibida localmente,<br/>Cuando el IoT Gateway procesa la condición de riesgo con las reglas configuradas en el entorno local,<br/>Entonces el sistema activa el extractor de aire de la zona en un intervalo inferior a 2 segundos contados desde la medición válida, sin depender de la disponibilidad de la plataforma en la nube.<br/><br/><strong>Escenario 5: Medición inválida sin activación de actuadores</strong><br/>Dado que el dispositivo ESP32 de una zona crítica envía una medición de CO₂ fuera del rango operativo del sensor MQ-135,<br/>Cuando el IoT Gateway recibe y descarta la medición como inválida,<br/>Entonces el sistema no activa extractores, sirenas ni mamparas acústicas por esa medición<br/>Y el sistema registra el evento como medición inválida de CO₂ con la zona y el instante correspondiente.<br/><br/><strong>Escenario 6: Fallo del actuador con registro de incumplimiento del tiempo de respuesta útil</strong><br/>Dado que una zona crítica presenta una condición de riesgo confirmada que requiere activación del extractor de aire<br/>Y el relé de control no confirma la activación del extractor dentro del intervalo operativo esperado,<br/>Cuando transcurren 2 segundos desde la confirmación de la condición de riesgo sin respuesta operativa del actuador,<br/>Entonces el sistema registra el fallo del actuador con la zona, el actuador afectado y el instante del evento<br/>Y el sistema mantiene la alerta de riesgo activa en la aplicación móvil del supervisor de seguridad.</td>
    </tr>
    <tr>
      <td align="left">HU40</td>
      <td align="left">E6</td>
      <td align="left">Persistencia local y resincronización de telemetría en contingencia offline</td>
      <td align="left">Como supervisor de seguridad quiero que el IoT Gateway conserve mediciones y eventos del sistema durante una interrupción de conectividad a internet para mantener trazabilidad operativa y continuidad del monitoreo en la planta.</td>
      <td align="left"><strong>Escenario 1: Almacenamiento local de mediciones ambientales durante caída de internet</strong><br/>Dado que el IoT Gateway recibe mediciones válidas de CO₂, ruido y presencia desde dispositivos ESP32 de una zona crítica<br/>Y la conexión a internet de la planta se interrumpe,<br/>Cuando el IoT Gateway procesa las mediciones recibidas sin poder enviarlas a la API en la nube,<br/>Entonces el sistema persiste cada medición en la base de datos local SQLite con identificador de zona, tipo de medición, valor, origen del dispositivo y marca temporal.<br/><br/><strong>Escenario 2: Registro local de eventos de alerta durante contingencia offline</strong><br/>Dado que el IoT Gateway detecta una condición ambiental fuera de los límites permitidos en una zona crítica<br/>Y la conexión a internet de la planta se encuentra interrumpida,<br/>Cuando el sistema genera una alerta ambiental o de seguridad asociada a la zona,<br/>Entonces el sistema registra el evento de alerta en SQLite con la zona, el tipo de alerta, la medición asociada y la marca temporal<br/>Y el sistema mantiene el estado de alerta disponible para consulta local mientras persista la contingencia.<br/><br/><strong>Escenario 3: Registro local de acciones automáticas de actuadores durante contingencia offline</strong><br/>Dado que el IoT Gateway ordena la activación o desactivación de un extractor, sirena o mampara acústica en una zona crítica<br/>Y la conexión a internet de la planta se encuentra interrumpida,<br/>Cuando la acción automática se ejecuta o falla en el entorno local,<br/>Entonces el sistema registra la acción en SQLite con el actuador, la operación realizada, la zona, el resultado y la marca temporal.<br/><br/><strong>Escenario 4: Resincronización ordenada de mediciones al restablecer conectividad</strong><br/>Dado que existen mediciones almacenadas en SQLite sin sincronizar con la plataforma en la nube<br/>Y la conexión a internet de la planta se restablece,<br/>Cuando el IoT Gateway inicia el proceso de resincronización hacia la API en la nube,<br/>Entonces el sistema envía las mediciones pendientes en orden cronológico<br/>Y el sistema marca cada registro local como sincronizado al recibir confirmación de persistencia en la nube.<br/><br/><strong>Escenario 5: Resincronización de alertas y acciones automáticas pendientes</strong><br/>Dado que existen eventos de alerta y registros de acciones automáticas almacenados en SQLite sin sincronizar<br/>Y la conexión a internet de la planta se restablece,<br/>Cuando el IoT Gateway ejecuta la resincronización de eventos operativos hacia la API en la nube,<br/>Entonces el sistema transmite los eventos pendientes preservando la secuencia temporal original<br/>Y el sistema conserva en la nube la trazabilidad completa de alertas y acciones ocurridas durante la contingencia offline.<br/><br/><strong>Escenario 6: Saturación de almacenamiento local por contingencia prolongada</strong><br/>Dado que la conexión a internet de la planta permanece interrumpida durante un periodo prolongado<br/>Y el volumen de mediciones y eventos generados supera la capacidad de retención configurada en SQLite,<br/>Cuando el IoT Gateway alcanza el límite de almacenamiento local disponible,<br/>Entonces el sistema conserva prioritariamente los registros de alertas, acciones automáticas y accesos RFID recientes<br/>Y el sistema registra un evento de contingencia de almacenamiento local con la fecha y el nivel de saturación alcanzado.<br/><br/><strong>Escenario 7: Rechazo de resincronización por telemetría corrupta o incompleta</strong><br/>Dado que un registro almacenado en SQLite presenta datos incompletos o inconsistentes para su envío a la nube<br/>Y la conexión a internet de la planta se encuentra disponible,<br/>Cuando el IoT Gateway intenta resincronizar el registro hacia la API en la nube,<br/>Entonces el sistema no elimina el registro local sin confirmación válida de persistencia remota<br/>Y el sistema registra el intento fallido de resincronización con el identificador del registro y el motivo detectado.</td>
    </tr>
    <tr>
      <td align="left">HU41</td>
      <td align="left">E6</td>
      <td align="left">Protección de telemetría y sesiones de operación y configuración</td>
      <td align="left">Como encargado de planta quiero que la telemetría transmitida hacia la nube y las sesiones de la aplicación móvil y de la aplicación web estén protegidas contra acceso no autorizado para preservar la confidencialidad e integridad de la información operativa y de configuración del sistema.</td>
      <td align="left"><strong>Escenario 1: Transmisión cifrada de telemetría desde el Gateway hacia la API</strong><br/>Dado que el IoT Gateway dispone de credenciales válidas para comunicarse con la API en la nube<br/>Y existen mediciones y eventos listos para transmisión remota,<br/>Cuando el IoT Gateway envía telemetría hacia el endpoint de ingesta de la plataforma,<br/>Entonces la comunicación se establece mediante un canal cifrado TLS<br/>Y la telemetría viaja sin exposición en texto plano sobre la red externa de la planta.<br/><br/><strong>Escenario 2: Rechazo de telemetría enviada por canal no cifrado</strong><br/>Dado que un emisor intenta entregar telemetría de una zona crítica hacia la API en la nube,<br/>Cuando la solicitud de ingesta no utiliza un canal cifrado TLS,<br/>Entonces la API en la nube rechaza la recepción de la telemetría<br/>Y el sistema registra el intento rechazado con origen, instante y motivo de seguridad.<br/><br/><strong>Escenario 3: Rechazo de telemetría con credencial de Gateway inválida</strong><br/>Dado que un emisor presenta una solicitud de ingesta de telemetría hacia la API en la nube,<br/>Cuando la credencial del IoT Gateway es inválida, expirada o no reconocida,<br/>Entonces la API en la nube rechaza la solicitud de ingesta<br/>Y el sistema no persiste la telemetría recibida en la base de datos relacional de la plataforma.<br/><br/><strong>Escenario 4: Expiración de sesión inactiva de supervisor en la aplicación móvil</strong><br/>Dado que un supervisor de seguridad mantiene una sesión autenticada en la aplicación móvil<br/>Y transcurre el periodo configurado de inactividad sin interacción autorizada del supervisor,<br/>Cuando el supervisor intenta acceder a una función protegida de monitoreo o control operativo,<br/>Entonces el sistema finaliza la sesión expirada<br/>Y el sistema exige una nueva autenticación antes de permitir el acceso a funciones protegidas.<br/><br/><strong>Escenario 5: Expiración de sesión inactiva de encargado en la aplicación web</strong><br/>Dado que un encargado de planta mantiene una sesión autenticada en la aplicación web<br/>Y transcurre el periodo configurado de inactividad sin interacción autorizada del encargado,<br/>Cuando el encargado intenta acceder a una función protegida de configuración,<br/>Entonces el sistema finaliza la sesión expirada<br/>Y el sistema exige una nueva autenticación antes de permitir el acceso a funciones protegidas.<br/><br/><strong>Escenario 6: Protección de credenciales de dispositivos embebidos en tránsito local</strong><br/>Dado que un dispositivo ESP32 envía mediciones al IoT Gateway mediante solicitudes de red locales,<br/>Cuando la solicitud incluye un token de autenticación de dispositivo configurado para el entorno industrial,<br/>Entonces el IoT Gateway acepta la telemetría únicamente si el token corresponde a un dispositivo registrado y vigente<br/>Y el sistema rechaza solicitudes de dispositivos no autorizados sin incorporar sus mediciones al flujo operativo.</td>
    </tr>
    <tr>
      <td align="left">HU42</td>
      <td align="left">E6</td>
      <td align="left">Disponibilidad operativa de la aplicación móvil y de la aplicación web</td>
      <td align="left">Como supervisor de seguridad quiero que la aplicación móvil mantenga una disponibilidad operativa definida para monitorear y controlar la planta de forma remota, y como encargado de planta quiero que la aplicación web mantenga disponibilidad para configurar y actualizar el sistema.</td>
      <td align="left"><strong>Escenario 1: Acceso al dashboard móvil durante operación nominal</strong><br/>Dado que la aplicación móvil se encuentra en operación nominal<br/>Y un supervisor de seguridad dispone de credenciales válidas,<br/>Cuando el supervisor accede al dashboard consolidado de la planta,<br/>Entonces el sistema presenta el estado de zonas críticas, alertas activas y telemetría reciente sin interrupción del servicio de operación.<br/><br/><strong>Escenario 2: Acceso a la configuración web durante operación nominal</strong><br/>Dado que la aplicación web se encuentra en operación nominal<br/>Y un encargado de planta dispone de credenciales válidas,<br/>Cuando el encargado accede a la administración de zonas o umbrales,<br/>Entonces el sistema presenta las funciones de configuración sin interrupción del servicio de administración.<br/><br/><strong>Escenario 3: Indisponibilidad no planificada del servicio en la nube</strong><br/>Dado que la plataforma en la nube experimenta una falla que impide el acceso a la aplicación móvil o a la aplicación web,<br/>Cuando un supervisor o un encargado intenta acceder a su canal correspondiente,<br/>Entonces el sistema informa indisponibilidad temporal del servicio<br/>Y el IoT Gateway continúa el monitoreo local, la persistencia en SQLite y la respuesta automática de actuadores configurada en el entorno industrial.<br/><br/><strong>Escenario 4: Cumplimiento del objetivo mensual de disponibilidad</strong><br/>Dado que la aplicación móvil y la aplicación web operan durante un periodo mensual de evaluación<br/>Y el objetivo de disponibilidad operativa del servicio se encuentra definido en 99.9 por ciento,<br/>Cuando el periodo mensual concluye,<br/>Entonces el sistema mantiene ambos canales disponibles al menos en el porcentaje objetivo definido, excluyendo ventanas de mantenimiento planificado previamente registradas.<br/><br/><strong>Escenario 5: Mantenimiento planificado con continuidad local del monitoreo industrial</strong><br/>Dado que la plataforma en la nube entra en una ventana de mantenimiento planificado previamente registrada,<br/>Cuando los dispositivos ESP32 continúan enviando telemetría al IoT Gateway durante la ventana de mantenimiento,<br/>Entonces el monitoreo local, la generación de alertas y la activación automática de actuadores continúan operando en la planta<br/>Y el sistema registra las mediciones y eventos para su posterior consulta cuando la aplicación móvil retome operación.</td>
    </tr>
    <tr>
      <td align="left">HU43</td>
      <td align="left">E6</td>
      <td align="left">Compatibilidad de la aplicación móvil y de la aplicación web</td>
      <td align="left">Como supervisor de seguridad quiero usar la aplicación móvil en dispositivos Android e iOS actuales para operar de forma remota, y como encargado de planta quiero usar la aplicación web en navegadores modernos para configurar y actualizar el sistema.</td>
      <td align="left"><strong>Escenario 1: Operación desde aplicación móvil en dispositivo compatible</strong><br/>Dado que un supervisor de seguridad accede a la aplicación móvil en un dispositivo Android o iOS soportado,<br/>Cuando el supervisor consulta el dashboard consolidado y el detalle de una zona crítica,<br/>Entonces el sistema presenta valores de CO₂ en ppm, ruido en dB, presencia y alertas activas de forma legible y operable en el dispositivo utilizado.<br/><br/><strong>Escenario 2: Configuración desde aplicación web en navegador compatible</strong><br/>Dado que un encargado de planta accede a la aplicación web desde un navegador web moderno soportado,<br/>Cuando el encargado consulta la administración de zonas, umbrales o dispositivos,<br/>Entonces el sistema presenta las funciones de configuración de forma legible y operable en el navegador utilizado.<br/><br/><strong>Escenario 3: Acceso desde navegador o dispositivo no soportado</strong><br/>Dado que un usuario intenta acceder a la aplicación web o a la aplicación móvil desde un entorno no incluido en la matriz de compatibilidad soportada,<br/>Cuando el usuario solicita acceso a funciones protegidas,<br/>Entonces el sistema informa que el entorno utilizado no se encuentra soportado<br/>Y el sistema indica los entornos compatibles correspondientes a cada canal.<br/><br/><strong>Escenario 4: Consulta de mapa de riesgos en dispositivo móvil compatible</strong><br/>Dado que un supervisor de seguridad accede a la aplicación móvil desde un dispositivo soportado,<br/>Cuando el supervisor consulta el mapa digitalizado de riesgos por zona,<br/>Entonces el sistema presenta el estado de riesgo de cada zona crítica configurada en el mapa de la planta de forma comprensible en el dispositivo utilizado.<br/><br/><strong>Escenario 5: Separación funcional entre canales compatibles</strong><br/>Dado que un supervisor de seguridad opera desde la aplicación móvil y un encargado de planta configura desde la aplicación web,<br/>Cuando ambos usuarios realizan sus funciones autorizadas durante la misma jornada,<br/>Entonces el sistema mantiene coherente la telemetría y las alertas en la aplicación móvil<br/>Y aplica la configuración actualizada desde la aplicación web sin mezclar las responsabilidades de cada canal.</td>
    </tr>
  </tbody>
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

<a id="s-cap-iv"></a>
# Capítulo IV: Solution Software Design

<a id="s-4-1"></a>
## 4.1. Strategic-Level Domain-Driven Design

<a id="s-4-1-1"></a>
### 4.1.1. Design-Level EventStorming

![Design-Level EventStorming](../assets/04-capitulo-iv/ddd/design-level-eventstorming.png)

<a id="s-4-1-1-1"></a>
#### 4.1.1.1 Candidate Context Discovery

<a id="s-4-1-1-2"></a>
#### 4.1.1.2 Domain Message Flows Modeling

![Domain Message Flows](../assets/04-capitulo-iv/ddd/domain-message-flows.png)

<a id="s-4-1-1-3"></a>
#### 4.1.1.3 Bounded Context Canvases

![Bounded Context Canvas](../assets/04-capitulo-iv/ddd/bounded-context-canvas.png)

<a id="s-4-1-2"></a>
### 4.1.2. Context Mapping

![Context Map](../assets/04-capitulo-iv/ddd/context-map.png)

<a id="s-4-1-3"></a>
### 4.1.3. Software Architecture

<a id="s-4-1-3-1"></a>
#### 4.1.3.1. Software Architecture System Landscape Diagram

![System Landscape Diagram](../assets/04-capitulo-iv/architecture/c4-system-landscape.png)

<a id="s-4-1-3-2"></a>
#### 4.1.3.2. Software Architecture Context Level Diagrams

![Context Level Diagram](../assets/04-capitulo-iv/architecture/c4-context.png)

<a id="s-4-1-3-2-software-architecture-container-level-diagrams"></a>
#### 4.1.3.2. Software Architecture Container Level Diagrams

![Container Level Diagram](../assets/04-capitulo-iv/architecture/c4-container.png)

<a id="s-4-1-3-3"></a>
#### 4.1.3.3. Software Architecture Deployment Diagrams

![Deployment Diagram](../assets/04-capitulo-iv/architecture/deployment.png)

<a id="s-4-2"></a>
## 4.2. Tactical-Level Domain-Driven Design

> Documentar cada Bounded Context en `bounded-contexts/` a partir de [`templates/bounded-context.md`](./templates/bounded-context.md).

<table>
  <thead>
    <tr>
      <th align="left">#</th>
      <th align="left">Bounded Context</th>
      <th align="left">Documento</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td align="left">4.2.1</td>
      <td align="left"></td>
      <td align="left"></td>
    </tr>
  </tbody>
</table>

---

<a id="s-4-2-x"></a>
### 4.2.X. Bounded Context: \<Bounded Context Name\>

> Plantilla. Copiar a `../bounded-contexts/bc-0N-<nombre>.md` y registrar en el Capítulo IV § 4.2.

**Navegación:** [Capítulo IV](../04-capitulo-iv-solution-software-design.md) · [Índice](../00-student-outcome.md#s-tabla-contenidos)

---

<a id="s-4-2-x-1"></a>
#### 4.2.X.1. Domain Layer

<a id="s-4-2-x-2"></a>
#### 4.2.X.2. Interface Layer

<a id="s-4-2-x-3"></a>
#### 4.2.X.3. Application Layer

<a id="s-4-2-x-4"></a>
#### 4.2.X.4. Infrastructure Layer

<a id="s-4-2-x-5"></a>
#### 4.2.X.5. Bounded Context Software Architecture Component Level Diagrams

![Component Level Diagram](../assets/04-capitulo-iv/bounded-contexts/bc-x-component.png)

<a id="s-4-2-x-6"></a>
#### 4.2.X.6. Bounded Context Software Architecture Code Level Diagrams

<a id="s-4-2-x-6-1"></a>
##### 4.2.X.6.1. Bounded Context Domain Layer Class Diagrams

![Domain Layer Class Diagram](../assets/04-capitulo-iv/bounded-contexts/bc-x-domain-class.png)

<a id="s-4-2-x-6-2"></a>
##### 4.2.X.6.2. Bounded Context Database Design Diagram

![Database Design Diagram](../assets/04-capitulo-iv/bounded-contexts/bc-x-database.png)

---

<a id="s-cap-v"></a>
# Capítulo V: Solution UI/UX Design

<a id="s-5-1"></a>
## 5.1. Style Guidelines

<a id="s-5-1-1"></a>
### 5.1.1. General Style Guidelines

![General Style Guidelines](../assets/05-capitulo-v/style-guidelines/general.png)

<a id="s-5-1-2"></a>
### 5.1.2. Web, Mobile and IoT Style Guidelines

![Web, Mobile and IoT Style Guidelines](../assets/05-capitulo-v/style-guidelines/web-mobile-iot.png)

<a id="s-5-2"></a>
## 5.2. Information Architecture

<a id="s-5-2-1"></a>
### 5.2.1. Organization Systems

![Organization Systems](../assets/05-capitulo-v/information-architecture/organization-systems.png)

<a id="s-5-2-2"></a>
### 5.2.2. Labeling Systems

<a id="s-5-2-3"></a>
### 5.2.3. SEO Tags and Meta Tags

<a id="s-5-2-4"></a>
### 5.2.4. Searching Systems

<a id="s-5-2-5"></a>
### 5.2.5. Navigation Systems

![Navigation Systems](../assets/05-capitulo-v/information-architecture/navigation-systems.png)

<a id="s-5-3"></a>
## 5.3. Landing Page UI Design

<a id="s-5-3-1"></a>
### 5.3.1. Landing Page Wireframe

![Landing Page Wireframe](../assets/05-capitulo-v/landing/wireframe.png)

<a id="s-5-3-2"></a>
### 5.3.2. Landing Page Mock-up

![Landing Page Mock-up](../assets/05-capitulo-v/landing/mockup.png)

<a id="s-5-4"></a>
## 5.4. Applications UX/UI Design

<a id="s-5-4-1"></a>
### 5.4.1. Applications Wireframes

![Applications Wireframes](../assets/05-capitulo-v/applications/wireframes.png)

<a id="s-5-4-2"></a>
### 5.4.2. Applications Wireflow Diagrams

![Applications Wireflow](../assets/05-capitulo-v/applications/wireflow.png)

<a id="s-5-4-2-applications-mock-ups"></a>
### 5.4.2. Applications Mock-ups

![Applications Mock-ups](../assets/05-capitulo-v/applications/mockups.png)

<a id="s-5-4-3"></a>
### 5.4.3. Applications User Flow Diagrams

![Applications User Flow](../assets/05-capitulo-v/applications/user-flow.png)

<a id="s-5-5"></a>
## 5.5. Applications Prototyping

![Applications Prototype](../assets/05-capitulo-v/applications/prototype.png)

**URL del prototipo:** 

<a id="s-5-6"></a>
## 5.6. IoT Device Design

![IoT Device Design](../assets/05-capitulo-v/iot-device/device-design.png)

---

<a id="s-cap-vi"></a>
# Capítulo VI: Product Implementation, Validation & Deployment

<a id="s-6-1"></a>
## 6.1. Software Configuration Management

<a id="s-6-1-1"></a>
### 6.1.1. Software Development Environment Configuration

<a id="s-6-1-2"></a>
### 6.1.2. Source Code Management

<a id="s-6-1-3"></a>
### 6.1.3. Source Code Style Guide & Conventions

<a id="s-6-1-4"></a>
### 6.1.4. Software Deployment Configuration

![Software Deployment Configuration](../assets/06-capitulo-vi/scm/deployment-configuration.png)

<a id="s-6-2"></a>
## 6.2. Landing Page, Services & Applications Implementation

> Documentar cada sprint en `sprints/` a partir de [`templates/sprint.md`](./templates/sprint.md).

<table>
  <thead>
    <tr>
      <th align="left">#</th>
      <th align="left">Sprint</th>
      <th align="left">Documento</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td align="left">6.2.1</td>
      <td align="left">Sprint 1</td>
      <td align="left"></td>
    </tr>
  </tbody>
</table>

---

<a id="s-6-2-x"></a>
### 6.2.X. Sprint n

> Plantilla. Copiar a `../sprints/sprint-0N.md` y registrar en el Capítulo VI § 6.2.

**Navegación:** [Capítulo VI](../06-capitulo-vi-product-implementation.md) · [Índice](../00-student-outcome.md#s-tabla-contenidos)

---

<a id="s-6-2-x-1"></a>
#### 6.2.X.1. Sprint Planning n

<a id="s-6-2-x-2"></a>
#### 6.2.X.2. Aspect Leaders and Collaborators

<table>
  <thead>
    <tr>
      <th align="left">Aspecto</th>
      <th align="left">Leader</th>
      <th align="left">Collaborators</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td align="left"></td>
      <td align="left"></td>
      <td align="left"></td>
    </tr>
  </tbody>
</table>

<a id="s-6-2-x-3"></a>
#### 6.2.X.3. Sprint Backlog n

<table>
  <thead>
    <tr>
      <th align="left">ID</th>
      <th align="left">User Story / Work Item</th>
      <th align="left">Points</th>
      <th align="left">Estado</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td align="left"></td>
      <td align="left"></td>
      <td align="left"></td>
      <td align="left"></td>
    </tr>
  </tbody>
</table>

<a id="s-6-2-x-4"></a>
#### 6.2.X.4. Development Evidence for Sprint Review

![Development Evidence](../assets/06-capitulo-vi/sprints/sprint-n-development.png)

<a id="s-6-2-x-5"></a>
#### 6.2.X.5. Testing Suite Evidence for Sprint Review

![Testing Suite Evidence](../assets/06-capitulo-vi/sprints/sprint-n-testing.png)

<a id="s-6-2-x-6"></a>
#### 6.2.X.6. Execution Evidence for Sprint Review

![Execution Evidence](../assets/06-capitulo-vi/sprints/sprint-n-execution.png)

<a id="s-6-2-x-7"></a>
#### 6.2.X.7. Services Documentation Evidence for Sprint Review

![Services Documentation](../assets/06-capitulo-vi/sprints/sprint-n-services-docs.png)

<a id="s-6-2-x-8"></a>
#### 6.2.X.8. Software Deployment Evidence for Sprint Review

![Deployment Evidence](../assets/06-capitulo-vi/sprints/sprint-n-deployment.png)

<a id="s-6-2-x-9"></a>
#### 6.2.X.9. Team Collaboration Insights during Sprint

![Team Collaboration Insights](../assets/06-capitulo-vi/sprints/sprint-n-collaboration.png)

---

<a id="s-6-3"></a>
## 6.3. Validation Interviews

<a id="s-6-3-1"></a>
### 6.3.1. Diseño de Entrevistas

<a id="s-6-3-2"></a>
### 6.3.2. Registro de Entrevistas

<table>
  <thead>
    <tr>
      <th align="left">ID</th>
      <th align="left">Fecha</th>
      <th align="left">Entrevistado</th>
      <th align="left">Segmento objetivo</th>
      <th align="left">Evidencia</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td align="left">V-01</td>
      <td align="left"></td>
      <td align="left"></td>
      <td align="left"></td>
      <td align="left"></td>
    </tr>
  </tbody>
</table>

<a id="s-6-3-3"></a>
### 6.3.3. Evaluaciones según heurísticas

<a id="s-6-4"></a>
## 6.4. Video About-the-Product

**URL del video:** 

![Video About-the-Product](../assets/06-capitulo-vi/videos/about-the-product.png)

---

<a id="s-conclusiones"></a>
# Conclusiones

<a id="s-conclusiones-recomendaciones"></a>
## Conclusiones y recomendaciones

<a id="s-video-about-the-team"></a>
## Video About-the-Team

**URL del video:** 

![Video About-the-Team](../assets/07-conclusiones/about-the-team.png)

---

<a id="s-bibliografia"></a>
# Bibliografía

---

<a id="s-anexos"></a>
# Anexos

<a id="s-anexo-videos-exposiciones"></a>
## Videos de Exposiciones

<table>
  <thead>
    <tr>
      <th align="left">Entrega</th>
      <th align="left">Descripción</th>
      <th align="left">URL (Stream / Clipchamp)</th>
      <th align="left">Archivo .mp4</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td align="left">AV1</td>
      <td align="left"></td>
      <td align="left"></td>
      <td align="left"></td>
    </tr>
    <tr>
      <td align="left">TB1</td>
      <td align="left"></td>
      <td align="left"></td>
      <td align="left"></td>
    </tr>
    <tr>
      <td align="left">AV2</td>
      <td align="left"></td>
      <td align="left"></td>
      <td align="left"></td>
    </tr>
    <tr>
      <td align="left">TB2</td>
      <td align="left"></td>
      <td align="left"></td>
      <td align="left"></td>
    </tr>
  </tbody>
</table>

<a id="s-anexo-repositorios"></a>
## Repositorios y artefactos

<table>
  <thead>
    <tr>
      <th align="left">Artefacto</th>
      <th align="left">URL / ubicación</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td align="left">Repositorio del informe (Project Report)</td>
      <td align="left"></td>
    </tr>
    <tr>
      <td align="left">Repositorio(s) de código de la solución</td>
      <td align="left"></td>
    </tr>
    <tr>
      <td align="left">Prototipos (Figma / UXPressia / LucidChart)</td>
      <td align="left"></td>
    </tr>
  </tbody>
</table>
