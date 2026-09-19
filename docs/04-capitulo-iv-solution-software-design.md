**Navegación:** [Índice](./00-student-outcome.md#s-tabla-contenidos) · Anterior: [Capítulo III](./03-capitulo-iii-requirements-specification.md) · Siguiente: [Capítulo V](./05-capitulo-v-solution-ui-ux-design.md)

---

<a id="s-cap-iv"></a>
# Capítulo IV: Solution Software Design

<a id="s-4-1"></a>
## 4.1. Strategic-Level Domain-Driven Design

<a id="s-4-1-1"></a>
### 4.1.1. Design-Level EventStorming

A partir del Big Picture EventStorming del Capítulo II y de las épicas EP02–EP07, el equipo realizó una sesión de **Design-Level EventStorming** para refinar el modelo hacia la implementación. Se avanzó por capas sobre el mismo tablero. El resultado son cuatro contextos: Identity & Access, Plant Monitoring, Safety & Actuation y Device & Edge Management. El objetivo fue validar flujos críticos —autenticación por rol, registro de telemetría, evaluación de exposición con actuación automática y ciclo de vida de dispositivos edge— antes de definir message flows y el context map.

**Captura 1 — Unstructured exploration y timelines** (eventos de dominio en orden de ocurrencia).

![Design-Level EventStorming — events and timelines](../assets/04-capitulo-iv/ddd/es-01-events-timelines.png)

**Captura 2 — Pain points y pivotal points**

![Design-Level EventStorming — pain points and pivotals](../assets/04-capitulo-iv/ddd/es-02-pains-pivotals.png)

**Captura 3 — Commands, policies, read models y sistemas externos.**

![Design-Level EventStorming — commands, policies, reads, externals](../assets/04-capitulo-iv/ddd/es-03-commands-policies-reads-externals.png)

**Captura 4 — Aggregates** 

![Design-Level EventStorming — aggregates](../assets/04-capitulo-iv/ddd/es-04-aggregates.png)

**Captura 5 — Bounded contexts**

![Design-Level EventStorming — bounded contexts](../assets/04-capitulo-iv/ddd/es-05-bounded-contexts.png)

EventStorming completo: [ver en Miro](https://miro.com/app/dashboard/space/2rIhoPYmRYvJJWSdjnYfNQ)

<a id="s-4-1-1-1"></a>
#### 4.1.1.1. Candidate Context Discovery

Los contextos candidatos se identificaron aplicando la heurística de **un Bounded Context por lenguaje ubicuo y dueño de datos**, tomando como entrada las user stories abordadas en el Capítulo III y el lenguaje del dominio SafePlant.

<table>
  <thead>
    <tr>
      <th align="left">Bounded Context</th>
      <th align="left">Tipo (DDD)</th>
      <th align="left">Propósito</th>
      <th align="left">Épica(s)</th>
      <th align="left">Fuera de alcance</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td align="left"><strong>Identity & Access</strong></td>
      <td align="left">Generic Subdomain</td>
      <td align="left">Autenticación, roles, recuperación de credenciales y autorización por canal (app móvil supervisor, app web encargado de planta).</td>
      <td align="left">EP02; usuarios y roles de EP03</td>
      <td align="left">Telemetría, reglas de seguridad ni gestión de dispositivos. Vive en el monolito Cloud; el Edge no administra usuarios, solo autentica dispositivos mediante tokens o API keys.</td>
    </tr>
    <tr>
      <td align="left"><strong>Plant Monitoring</strong></td>
      <td align="left">Core Domain</td>
      <td align="left">Definición topológica de la planta (áreas, umbrales) y registro histórico de telemetría: CO₂, ruido y presencia.</td>
      <td align="left">EP03</td>
      <td align="left">Evaluación de exposición, disparo de actuadores ni inventario de hardware de campo.</td>
    </tr>
    <tr>
      <td align="left"><strong>Safety & Actuation</strong></td>
      <td align="left">Dominio de reglas de seguridad</td>
      <td align="left">Cruce presencia × condiciones ambientales (exposición), motor de reglas de riesgo, activación de extractores, sirenas y mamparas acústicas, y anulación remota de actuadores. El loop automático corre en el servidor de planta; la nube supervisa, audita y acepta override cuando hay WAN.</td>
      <td align="left">EP04, EP05</td>
      <td align="left">Configuración de áreas/umbrales (Plant Monitoring) ni identidad de usuarios.</td>
    </tr>
    <tr>
      <td align="left"><strong>Device & Edge Management</strong></td>
      <td align="left">Supporting Subdomain</td>
      <td align="left">Credenciales de dispositivo, ingest MQTT hacia Plant Monitoring, cola local y sincronización cuando vuelve el enlace.</td>
      <td align="left">EP07</td>
      <td align="left">Reglas de seguridad ocupacional, semántica de umbrales, actualizaciones remotas de firmware (OTA) ni un chasis Raspberry Pi como nodo de diseño.</td>
    </tr>
  </tbody>
</table>

<a id="s-4-1-1-2"></a>
#### 4.1.1.2. Domain Message Flows Modeling

Con los cuatro bounded contexts ya delimitados, el equipo modeló cómo colaboran para resolver casos de uso de SafePlant mediante **Domain Message Flow Modelling** ([ddd-crew](https://github.com/ddd-crew/domain-message-flow-modelling)). Cada diagrama es un escenario de 5 a 9 mensajes numerados (comando, evento o consulta) en formato combinado: nombre, orden y payload. MQTT y el hardware de campo son sistemas; el Edge no es un quinto contexto ni un “IoT Gateway”.

**Notación.** Persona = Supervisor o Plant manager; nube = bounded context; engranaje = broker MQTT y hardware Device; recuadro = comando, evento o consulta (la consulta lleva request y response en el mismo recuadro); flecha discontinua = emisor hacia receptor.

![Domain message flow — notation](../assets/04-capitulo-iv/ddd/dmf-00-notation.png)

**Scenario 1 — Plant setup.** El supervisor, con sesión móvil en Identity & Access, define áreas, umbrales y asociación de dispositivos en Plant Monitoring.

![Domain message flow — plant setup](../assets/04-capitulo-iv/ddd/dmf-01-plant-setup.png)

**Scenario 2 — Telemetry ingest.** El dispositivo se autentica, publica lecturas de CO₂, ruido y presencia (sin unificarlas) en el broker MQTT; Device & Edge las ingiere en Plant Monitoring. La evaluación de riesgo queda fuera de este flujo.

![Domain message flow — telemetry ingest](../assets/04-capitulo-iv/ddd/dmf-02-telemetry-ingest.png)

**Scenario 3 — Exposure and actuation.** Plant Monitoring notifica lecturas y presencia a Safety & Actuation, que detecta excesos, clasifica exposición, alerta y activa extractores, sirenas o mamparas; cuando las lecturas vuelven a rango, normaliza. Quien emite `Activate`/`Normalize` es Safety **en el servidor de planta**; la actuación física la ejecuta el dispositivo, no Device & Edge Management.

![Domain message flow — exposure and actuation](../assets/04-capitulo-iv/ddd/dmf-03-exposure-actuation.png)

**Scenario 4 — Offline and sync.** Dos caminos alternativos: si el ingest falla, Device & Edge encola telemetría y reintenta al recuperar la conectividad; si hay alerta ambiental y cloud no alcanza, Safety **ya corre en Edge** y deja la alerta en Device & Edge para sincronizar después. Los actuadores no esperan internet. Safety & Actuation sigue siendo dueño del riesgo.

![Domain message flow — offline and sync](../assets/04-capitulo-iv/ddd/dmf-04-offline-sync.png)

**Scenario 5 — Supervisor override.** El supervisor, autenticado en canal móvil, consulta el estado operativo y las alertas activas y anula un actuador en Safety & Actuation. Identity no evalúa exposición; un intento desde el canal web se deniega.

![Domain message flow — supervisor override](../assets/04-capitulo-iv/ddd/dmf-05-supervisor-override.png)

<a id="s-4-1-1-3"></a>
#### 4.1.1.3. Bounded Context Canvases

Cada contexto candidato se documentó con un **Bounded Context Canvas**. El canvas fija propósito, clasificación estratégica, lenguaje, decisiones de negocio y la comunicación de entrada y salida.

**Plant Monitoring (core).** Áreas, umbrales y telemetría.

![Bounded Context Canvas — Plant Monitoring](../assets/04-capitulo-iv/ddd/bcc-01-plant-monitoring.png)

**Safety & Actuation.** Exposición, alertas y actuación automática u override.

![Bounded Context Canvas — Safety & Actuation](../assets/04-capitulo-iv/ddd/bcc-02-safety-actuation.png)

**Device & Edge Management (supporting).** Credenciales de dispositivo, ingest, cola y sincronización.

![Bounded Context Canvas — Device & Edge Management](../assets/04-capitulo-iv/ddd/bcc-03-device-edge-management.png)

**Identity & Access (generic).** Cuentas, sesión por canal y OHS hacia los demás contextos.

![Bounded Context Canvas — Identity & Access](../assets/04-capitulo-iv/ddd/bcc-04-identity-access.png)

<a id="s-4-1-2"></a>
### 4.1.2. Context Mapping

Las relaciones estructurales entre los cuatro bounded contexts se mapearon con los patrones de **ddd-crew**, tal como se muestra en el diagrama a continuación.

<table>
  <thead>
    <tr>
      <th align="left">Upstream</th>
      <th align="left">Downstream</th>
      <th align="left">Patrones</th>
      <th align="left">Descripción</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td align="left">Identity & Access</td>
      <td align="left">Plant Monitoring</td>
      <td align="left">OHS + Conformist (sesión/canal)</td>
      <td align="left">Setup de planta (áreas, umbrales, dispositivos) exige sesión de supervisor en canal móvil.</td>
    </tr>
    <tr>
      <td align="left">Identity & Access</td>
      <td align="left">Safety & Actuation</td>
      <td align="left">OHS + Conformist</td>
      <td align="left">Estado, alertas y override exigen la misma sesión móvil; Identity no evalúa exposición.</td>
    </tr>
    <tr>
      <td align="left">Plant Monitoring</td>
      <td align="left">Safety & Actuation</td>
      <td align="left">Customer/Supplier + Conformist al *evento* de lectura</td>
      <td align="left">Safety se ciñe al *evento* de lectura/presencia; Plant Monitoring puede registrar telemetría sin que haya actuación.</td>
    </tr>
    <tr>
      <td align="left">Plant Monitoring</td>
      <td align="left">Device & Edge Management</td>
      <td align="left">OHS de ingest + ACL en Edge</td>
      <td align="left">PM es dueño del hecho y del contrato de ingest; Edge traduce MQTT/cola (ACL). La flecha U→D es del modelo, no del hop MQTT.</td>
    </tr>
    <tr>
      <td align="left">Safety & Actuation</td>
      <td align="left">Device & Edge Management</td>
      <td align="left">ACL</td>
      <td align="left">Alerta persistida/sincronizada (`PO-09`); el dueño del riesgo sigue en Safety, no en `EdgeNode`.</td>
    </tr>
  </tbody>
</table>


![Context Map](../assets/04-capitulo-iv/ddd/context-map.png)

<a id="s-4-1-3"></a>
### 4.1.3. Software Architecture

Los diagramas C4 se generan desde `docs/diagrams/c4.dsl` (Structurizr). El stack visible es **provisional** (DEC-008): ASP.NET Core (C#) en cloud y Edge, PostgreSQL en nube, SQLite en planta, Eclipse Mosquitto, SMTP, landing Angular y firmware Arduino / ESP32. Los clientes ya estaban cerrados: Flutter (móvil) y Angular (web). Identity es propia (no Auth0/Cognito). No hay un sistema “IoT Gateway”; el Edge hace de puente (DEC-002). Safety & Actuation también corre en el servidor de planta (DEC-007).

**Leyenda** (formas; los cuatro bounded contexts usan el mismo hexágono, no un color por contexto).

<table>
  <thead>
    <tr>
      <th align="left">Forma</th>
      <th align="left">Qué representa</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td align="left">Persona</td>
      <td align="left">Supervisor, encargado de planta</td>
    </tr>
    <tr>
      <td align="left">Persona (gris)</td>
      <td align="left">Visitante de la landing</td>
    </tr>
    <tr>
      <td align="left">Caja de sistema externo</td>
      <td align="left">Hardware de campo, correo SMTP</td>
    </tr>
    <tr>
      <td align="left">Caja redondeada</td>
      <td align="left">Software interno: monolito, Edge Application, firmware</td>
    </tr>
    <tr>
      <td align="left">Cilindro</td>
      <td align="left">Base de datos (nube o planta)</td>
    </tr>
    <tr>
      <td align="left">Tubo</td>
      <td align="left">Broker MQTT</td>
    </tr>
    <tr>
      <td align="left">Móvil / navegador / carpeta</td>
      <td align="left">App Flutter, cliente Angular, landing</td>
    </tr>
    <tr>
      <td align="left">Hexágono</td>
      <td align="left">Capas Interface / Application / Domain / Infrastructure</td>
    </tr>
  </tbody>
</table>

<a id="s-4-1-3-1"></a>
#### 4.1.3.1. Software Architecture System Landscape Diagram

SafePlant aparece como un único sistema rodeado por el supervisor, el encargado de planta, el visitante de la landing y dos externos: el **hardware de campo** (ESP32, sensores y actuadores) y el **servicio de correo SMTP** para recuperación de credenciales.

![System Landscape Diagram](../assets/04-capitulo-iv/architecture/c4-system-landscape.png)

<a id="s-4-1-3-2"></a>
#### 4.1.3.2. Software Architecture Context Level Diagrams

El mismo conjunto de personas y sistemas externos, ahora con SafePlant al centro: Landscape y Context se parecen porque no hay un segundo software system interno. Los usuarios no hablan con el hardware ni con el correo; esas relaciones pasan por el firmware Arduino/ESP32 y el backend ASP.NET Core.

![Context Level Diagram](../assets/04-capitulo-iv/architecture/c4-context.png)

<a id="s-4-1-3-3"></a>
#### 4.1.3.3. Software Architecture Container Level Diagrams

Nueve containers. El **Web Monolithic Backend** (ASP.NET Core + PostgreSQL) es una sola caja: los cuatro bounded contexts viven dentro, no como servicios. En planta, **Edge Application** (ASP.NET Core + SQLite) hospeda el runtime de Device & Edge, una proyección de Plant Monitoring y el loop vivo de Safety & Actuation; **Eclipse Mosquitto** queda entre el firmware y ese Edge. El firmware publica lecturas y ejecuta relés; la landing es Angular.

![Container Level Diagram](../assets/04-capitulo-iv/architecture/c4-container.png)

<a id="s-4-1-3-4"></a>
#### 4.1.3.4. Software Architecture Deployment Diagrams

Cloud en **Azure**: Static Web Apps sirve la landing y el cliente Angular; App Service hospeda el monolito ASP.NET Core; Azure Database for PostgreSQL es el sistema de registro. En la **planta**, un servidor on-prem corre Edge Application, SQLite y Eclipse Mosquitto (sin IoT Hub): ahí vive el loop de Safety. El firmware Arduino/ESP32 está en el dispositivo de campo. La app Flutter corre en el teléfono del supervisor; el correo de recuperación sigue en SMTP externo. Identity es propia (no Azure AD). El override desde la nube hacia Edge exige WAN.

![Deployment Diagram](../assets/04-capitulo-iv/architecture/deployment.png)

<a id="s-4-2"></a>
## 4.2. Tactical-Level Domain-Driven Design

Cada bounded context se documenta con las cuatro capas tácticas, un diagrama de componentes C4 y los diagramas de código (clases de dominio y base de datos).

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
      <td align="left">Plant Monitoring</td>
      <td align="left"><a href="bounded-contexts/bc-01-plant-monitoring.md">bc-01-plant-monitoring.md</a></td>
    </tr>
    <tr>
      <td align="left">4.2.2</td>
      <td align="left">Safety & Actuation</td>
      <td align="left"><a href="bounded-contexts/bc-02-safety-actuation.md">bc-02-safety-actuation.md</a></td>
    </tr>
    <tr>
      <td align="left">4.2.3</td>
      <td align="left">Device & Edge Management</td>
      <td align="left"><a href="bounded-contexts/bc-03-device-edge-management.md">bc-03-device-edge-management.md</a></td>
    </tr>
    <tr>
      <td align="left">4.2.4</td>
      <td align="left">Identity & Access</td>
      <td align="left"><a href="bounded-contexts/bc-04-identity-access.md">bc-04-identity-access.md</a></td>
    </tr>
  </tbody>
</table>

---

**Navegación:** [Índice](./00-student-outcome.md#s-tabla-contenidos) · Anterior: [Capítulo III](./03-capitulo-iii-requirements-specification.md) · Siguiente: [Capítulo V](./05-capitulo-v-solution-ui-ux-design.md)
