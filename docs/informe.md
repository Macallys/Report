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

- [Carátula](#carátula)
  - [Relación de integrantes](#relación-de-integrantes)
- [Registro de Versiones del Informe](#registro-de-versiones-del-informe)
- [Project Report Collaboration Insights](#project-report-collaboration-insights)
- [Contenido](#contenido)
  - [Tabla de contenidos](#tabla-de-contenidos)
- [Student Outcome](#student-outcome)
- [Capítulo I: Introducción](#capítulo-i-introducción)
  - [1.1. Startup Profile](#11-startup-profile)
    - [1.1.1. Descripción de la Startup](#111-descripción-de-la-startup)
    - [1.1.2. Perfiles de integrantes del equipo](#112-perfiles-de-integrantes-del-equipo)
  - [1.2. Solution Profile](#12-solution-profile)
    - [1.2.1 Antecedentes y problemática](#121-antecedentes-y-problemática)
    - [1.2.2 Lean UX Process](#122-lean-ux-process)
      - [1.2.2.1. Lean UX Problem Statements](#1221-lean-ux-problem-statements)
      - [1.2.2.2. Lean UX Assumptions](#1222-lean-ux-assumptions)
      - [1.2.2.3. Lean UX Hypothesis Statements](#1223-lean-ux-hypothesis-statements)
      - [1.2.2.4. Lean UX Canvas](#1224-lean-ux-canvas)
  - [1.3. Segmentos objetivo](#13-segmentos-objetivo)
- [Capítulo II: Requirements Elicitation \& Analysis](#capítulo-ii-requirements-elicitation--analysis)
  - [2.1. Competidores](#21-competidores)
    - [2.1.1. Análisis competitivo](#211-análisis-competitivo)
    - [2.1.2. Estrategias y tácticas frente a competidores](#212-estrategias-y-tácticas-frente-a-competidores)
  - [2.2. Entrevistas](#22-entrevistas)
    - [2.2.1. Diseño de entrevistas](#221-diseño-de-entrevistas)
    - [2.2.2. Registro de entrevistas](#222-registro-de-entrevistas)
    - [2.2.3. Análisis de entrevistas](#223-análisis-de-entrevistas)
  - [2.3. Needfinding](#23-needfinding)
    - [2.3.1. User Personas](#231-user-personas)
    - [2.3.2. User Task Matrix](#232-user-task-matrix)
    - [2.3.3. User Journey Mapping](#233-user-journey-mapping)
    - [2.3.4. Empathy Mapping](#234-empathy-mapping)
  - [2.4. Big Picture EventStorming](#24-big-picture-eventstorming)
  - [2.5. Ubiquitous Language](#25-ubiquitous-language)
- [Capítulo III: Requirements Specification](#capítulo-iii-requirements-specification)
  - [3.1. User Stories](#31-user-stories)
  - [3.2. Impact Mapping](#32-impact-mapping)
  - [3.3. Product Backlog](#33-product-backlog)
- [Capítulo IV: Solution Software Design](#capítulo-iv-solution-software-design)
  - [4.1. Strategic-Level Domain-Driven Design](#41-strategic-level-domain-driven-design)
    - [4.1.1. Design-Level EventStorming](#411-design-level-eventstorming)
      - [4.1.1.1 Candidate Context Discovery](#4111-candidate-context-discovery)
      - [4.1.1.2 Domain Message Flows Modeling](#4112-domain-message-flows-modeling)
      - [4.1.1.3 Bounded Context Canvases](#4113-bounded-context-canvases)
    - [4.1.2. Context Mapping](#412-context-mapping)
    - [4.1.3. Software Architecture](#413-software-architecture)
      - [4.1.3.1. Software Architecture System Landscape Diagram](#4131-software-architecture-system-landscape-diagram)
      - [4.1.3.2. Software Architecture Context Level Diagrams](#4132-software-architecture-context-level-diagrams)
      - [4.1.3.2. Software Architecture Container Level Diagrams](#4132-software-architecture-container-level-diagrams)
      - [4.1.3.3. Software Architecture Deployment Diagrams](#4133-software-architecture-deployment-diagrams)
  - [4.2. Tactical-Level Domain-Driven Design](#42-tactical-level-domain-driven-design)
    - [4.2.X. Bounded Context: \<Bounded Context Name\>](#42x-bounded-context-bounded-context-name)
      - [4.2.X.1. Domain Layer](#42x1-domain-layer)
      - [4.2.X.2. Interface Layer](#42x2-interface-layer)
      - [4.2.X.3. Application Layer](#42x3-application-layer)
      - [4.2.X.4. Infrastructure Layer](#42x4-infrastructure-layer)
      - [4.2.X.5. Bounded Context Software Architecture Component Level Diagrams](#42x5-bounded-context-software-architecture-component-level-diagrams)
      - [4.2.X.6. Bounded Context Software Architecture Code Level Diagrams](#42x6-bounded-context-software-architecture-code-level-diagrams)
        - [4.2.X.6.1. Bounded Context Domain Layer Class Diagrams](#42x61-bounded-context-domain-layer-class-diagrams)
        - [4.2.X.6.2. Bounded Context Database Design Diagram](#42x62-bounded-context-database-design-diagram)
- [Capítulo V: Solution UI/UX Design](#capítulo-v-solution-uiux-design)
  - [5.1. Style Guidelines](#51-style-guidelines)
    - [5.1.1. General Style Guidelines](#511-general-style-guidelines)
    - [5.1.2. Web, Mobile and IoT Style Guidelines](#512-web-mobile-and-iot-style-guidelines)
  - [5.2. Information Architecture](#52-information-architecture)
    - [5.2.1. Organization Systems](#521-organization-systems)
    - [5.2.2. Labeling Systems](#522-labeling-systems)
    - [5.2.3. SEO Tags and Meta Tags](#523-seo-tags-and-meta-tags)
    - [5.2.4. Searching Systems](#524-searching-systems)
    - [5.2.5. Navigation Systems](#525-navigation-systems)
  - [5.3. Landing Page UI Design](#53-landing-page-ui-design)
    - [5.3.1. Landing Page Wireframe](#531-landing-page-wireframe)
    - [5.3.2. Landing Page Mock-up](#532-landing-page-mock-up)
  - [5.4. Applications UX/UI Design](#54-applications-uxui-design)
    - [5.4.1. Applications Wireframes](#541-applications-wireframes)
    - [5.4.2. Applications Wireflow Diagrams](#542-applications-wireflow-diagrams)
    - [5.4.2. Applications Mock-ups](#542-applications-mock-ups)
    - [5.4.3. Applications User Flow Diagrams](#543-applications-user-flow-diagrams)
  - [5.5. Applications Prototyping](#55-applications-prototyping)
  - [5.6. IoT Device Design](#56-iot-device-design)
- [Capítulo VI: Product Implementation, Validation \& Deployment](#capítulo-vi-product-implementation-validation--deployment)
  - [6.1. Software Configuration Management](#61-software-configuration-management)
    - [6.1.1. Software Development Environment Configuration](#611-software-development-environment-configuration)
    - [6.1.2. Source Code Management](#612-source-code-management)
    - [6.1.3. Source Code Style Guide \& Conventions](#613-source-code-style-guide--conventions)
    - [6.1.4. Software Deployment Configuration](#614-software-deployment-configuration)
  - [6.2. Landing Page, Services \& Applications Implementation](#62-landing-page-services--applications-implementation)
    - [6.2.X. Sprint n](#62x-sprint-n)
      - [6.2.X.1. Sprint Planning n](#62x1-sprint-planning-n)
      - [6.2.X.2. Aspect Leaders and Collaborators](#62x2-aspect-leaders-and-collaborators)
      - [6.2.X.3. Sprint Backlog n](#62x3-sprint-backlog-n)
      - [6.2.X.4. Development Evidence for Sprint Review](#62x4-development-evidence-for-sprint-review)
      - [6.2.X.5. Testing Suite Evidence for Sprint Review](#62x5-testing-suite-evidence-for-sprint-review)
      - [6.2.X.6. Execution Evidence for Sprint Review](#62x6-execution-evidence-for-sprint-review)
      - [6.2.X.7. Services Documentation Evidence for Sprint Review](#62x7-services-documentation-evidence-for-sprint-review)
      - [6.2.X.8. Software Deployment Evidence for Sprint Review](#62x8-software-deployment-evidence-for-sprint-review)
      - [6.2.X.9. Team Collaboration Insights during Sprint](#62x9-team-collaboration-insights-during-sprint)
  - [6.3. Validation Interviews](#63-validation-interviews)
    - [6.3.1. Diseño de Entrevistas](#631-diseño-de-entrevistas)
    - [6.3.2. Registro de Entrevistas](#632-registro-de-entrevistas)
    - [6.3.3. Evaluaciones según heurísticas](#633-evaluaciones-según-heurísticas)
  - [6.4. Video About-the-Product](#64-video-about-the-product)
- [Conclusiones](#conclusiones)
  - [Conclusiones y recomendaciones](#conclusiones-y-recomendaciones)
  - [Video About-the-Team](#video-about-the-team)
- [Bibliografía](#bibliografía)
- [Anexos](#anexos)
  - [Videos de Exposiciones](#videos-de-exposiciones)
  - [Repositorios y artefactos](#repositorios-y-artefactos)

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


**Preguntas Generales**

* Nombre
* Edad
* Distrito de residencia
* Ocupación o cargo actual
* Dispositivos tecnológicos de preferencia

**Supervisor de Seguridad**

* ¿Qué tiene que pasar al final de tu jornada para que sientas que cumpliste tu meta respecto a la prevención de riesgos ambientales?
* ¿Cuáles son los mayores problemas o frustraciones que enfrentas hoy en día al intentar detectar riesgos como niveles peligrosos de CO₂ o ruido excesivo en la planta?
* Cuéntame de la última vez que hubo una condición de riesgo en tu entorno de trabajo, ¿cómo te enteraste y cuáles fueron los pasos exactos que seguiste para resolverlo?
* Si utilizaras una aplicación móvil para monitorear las zonas críticas de la planta, ¿qué información necesitarías ver inmediatamente al abrirla para tomar decisiones rápidas?
* ¿En qué escenarios de emergencia consideras que la automatización de la planta no es suficiente y necesitarías tomar el control manual remoto de los actuadores (extractores, sirenas o mamparas) desde tu celular?
* ¿Cómo verificas actualmente que las medidas de seguridad o de evacuación realmente funcionaron después de que ocurre un incidente en la planta?
* ¿Qué tan útil te resultaría tener un mapa digitalizado en tu celular con los estados de riesgo de cada zona en tiempo real, y por qué?
* Si pudieras cambiar una sola cosa del proceso actual con el que evalúas si hay personal expuesto a condiciones de riesgo, ¿qué sería?
* ¿Cómo te gustaría recibir las notificaciones o alertas en tu dispositivo móvil para asegurar que las atiendas de inmediato sin que se pierdan en el día a día?

**Encargado de Planta**

* ¿Cuál es el impacto a largo plazo que buscas lograr en la operatividad de la planta al implementar nuevos sistemas de monitoreo y automatización?
* ¿Qué tareas administrativas, de configuración de equipos o de gestión de personal te generan mayor frustración o te quitan más tiempo en el día a día?
* ¿Cuáles son los mayores desafíos al registrar físicamente nuevos sensores IoT o actuadores en las zonas críticas de la planta?
* Al definir los límites ambientales permitidos (umbrales de CO₂ y ruido) para los operarios, ¿qué dificultades o variables problemáticas encuentras habitualmente?
* Al gestionar y configurar el sistema desde una aplicación web en tu computadora, ¿qué nivel de detalle o funciones consideras indispensables para sentir que tienes el control total de la plataforma?
* ¿Qué criterios utilizas actualmente para decidir qué roles, permisos o accesos le otorgas a los supervisores de seguridad que operan bajo tu gestión?
* ¿Cómo manejas actualmente las actualizaciones de normativas de seguridad industrial y cómo las aplicas a los parámetros de los sistemas de la planta?
* Cuéntame de alguna vez en la que hubo problemas de conectividad o fallas en el hardware de monitoreo, ¿cómo te impactó a nivel de gestión de la planta?
* ¿Qué tan importante es para ti tener un registro histórico o auditoría de los eventos ambientales y de las acciones de los supervisores, y para qué lo usarías?
* Si pudieras automatizar por completo una tarea de configuración o administración de la planta que hoy haces de forma manual, ¿cuál elegirías?

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

<a id="s-3-1"></a>
## 3.1. User Stories

<table>
  <thead>
    <tr>
      <th align="left">ID</th>
      <th align="left">User Story</th>
      <th align="left">Acceptance Criteria (Gherkin)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td align="left">US-01</td>
      <td align="left"></td>
      <td align="left"></td>
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
