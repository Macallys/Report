<a id="s-4-2-2"></a>
# 4.2.2. Bounded Context: Safety & Actuation

**Navegación:** [Capítulo IV](../04-capitulo-iv-solution-software-design.md) · [Índice](../00-student-outcome.md#s-tabla-contenidos)

---

Safety & Actuation protege al personal cruzando presencia con CO₂ y ruido: clasifica exposición, alerta y manda extractores, sirenas y mamparas, o las anula. Es el **segundo core** (cumplimiento de seguridad ocupacional). Quien opera SafePlant confía en que el riesgo se evalúa aquí.

El mismo bounded context tiene **dos runtimes** (DEC-007). En `Edge Application` corre el loop vivo: `PO-03`–`PO-08`, `Activate actuator` / `Normalize actuator` hacia el **firmware**. En el `Web Monolithic Backend` quedan estado, alertas y override del supervisor **cuando hay WAN**, más la copia de auditoría tras el sync. Device & Edge **no** evalúa riesgo. La anulación manual es un comando del supervisor en la aplicación **móvil**, no una regla automática; Identity deniega el mismo intento desde la aplicación web del encargado. Sin acceso a cloud, el loop automático sigue.

No hay entidad `Device` ni `deviceId` en este contexto: el comando identifica el área y el tipo de actuador. Varias sirenas del mismo tipo en un área se tratan como *la sirena del área*; no se direcciona una instancia suelta.

Ubiquitous language: *Personnel exposure* · *Exposure severity* · *Area risk* · *Environmental alert* · *Excessive carbon dioxide* · *Excessive noise* · *Air extractor* · *Preventive siren* · *Acoustic barrier* · *Manual override* · *Automatic actuator action*.

<a id="s-4-2-2-1"></a>
## 4.2.2.1. Domain Layer

Dos aggregate roots en el mismo módulo —`ExposureState` y `AreaActuators`— y las reglas de negocio como domain services en el mismo proceso (en planta: el runtime Edge). No hay un aggregate por cada tipo de actuador: `AreaActuators` lleva el tipo en el comando. Los umbrales no se copian como dueño; llegan en los eventos de Plant Monitoring (en planta, vía la **proyección**). La severidad es `None`, `Medium` o `High`. Los fallos de relé se registran; no se reintenta aquí.

<table>
  <thead>
    <tr>
      <th align="left">Clase</th>
      <th align="left">Tipo</th>
      <th align="left">Propósito</th>
      <th align="left">Atributos</th>
      <th align="left">Métodos</th>
      <th align="left">Relaciones</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td align="left">`ExposureState`</td>
      <td align="left">Aggregate Root</td>
      <td align="left">Cruce de presencia con ambiente, severidad y alerta **por área**.</td>
      <td align="left">`id`, `areaId`, `personnelPresent`, `severity`, `risk`, `alertActive`</td>
      <td align="left">`detectExcess()`, `evaluateExposure()`, `classifySeverity()`, `highlightRisk()`, `raiseAlert()`, `withdrawAlert()`, `resolve()`, `skipClassification()`</td>
      <td align="left">1—0..* `EnvironmentalAlert`</td>
    </tr>
    <tr>
      <td align="left">`EnvironmentalAlert`</td>
      <td align="left">Entity</td>
      <td align="left">Alerta ambiental levantada o retirada.</td>
      <td align="left">`id`, `areaId`, `raisedAt`, `withdrawnAt`</td>
      <td align="left">—</td>
      <td align="left">contenido en `ExposureState`</td>
    </tr>
    <tr>
      <td align="left">`AreaActuators`</td>
      <td align="left">Aggregate Root</td>
      <td align="left">Estado lógico de extractor, sirena y mampara del área, incluida la anulación manual. Sin `deviceId`.</td>
      <td align="left">`id`, `areaId`</td>
      <td align="left">`activate()`, `normalize()`, `override()`, `recordAutomaticAction()`</td>
      <td align="left">contiene 1..3 `ActuatorState`; 0..* `AutomaticActuatorAction`</td>
    </tr>
    <tr>
      <td align="left">`ActuatorState`</td>
      <td align="left">Entity</td>
      <td align="left">Relé lógico `(área, tipo)`: on/off/deployed y modo auto/overridden.</td>
      <td align="left">`type`, `runState`, `mode`, `lastChangedAt`</td>
      <td align="left">—</td>
      <td align="left">contenido en `AreaActuators`</td>
    </tr>
    <tr>
      <td align="left">`AutomaticActuatorAction`</td>
      <td align="left">Entity</td>
      <td align="left">Auditoría de actuación automática o fallo de relé.</td>
      <td align="left">`id`, `type`, `succeeded`, `recordedAt`</td>
      <td align="left">—</td>
      <td align="left">contenido en `AreaActuators`</td>
    </tr>
    <tr>
      <td align="left">`ExposureSeverity`</td>
      <td align="left">Value Object (Enum)</td>
      <td align="left">`None`, `Medium`, `High`. Sin yellow.</td>
      <td align="left">`value`</td>
      <td align="left">—</td>
      <td align="left">usado por `ExposureState`</td>
    </tr>
    <tr>
      <td align="left">`ActuatorType`</td>
      <td align="left">Value Object (Enum)</td>
      <td align="left">`Extractor`, `Siren`, `Barrier`.</td>
      <td align="left">`value`</td>
      <td align="left">—</td>
      <td align="left">usado por `ActuatorState` y los puertos</td>
    </tr>
    <tr>
      <td align="left">`ActuatorMode`</td>
      <td align="left">Value Object (Enum)</td>
      <td align="left">`Auto` o `Overridden`.</td>
      <td align="left">`value`</td>
      <td align="left">—</td>
      <td align="left">usado por `ActuatorState`</td>
    </tr>
    <tr>
      <td align="left">`ActuatorRunState`</td>
      <td align="left">Value Object (Enum)</td>
      <td align="left">`Off`, `On`, `Deployed`, `Retracted`, `Failed`.</td>
      <td align="left">`value`</td>
      <td align="left">—</td>
      <td align="left">usado por `ActuatorState`</td>
    </tr>
    <tr>
      <td align="left">`AreaRisk`</td>
      <td align="left">Value Object</td>
      <td align="left">Área destacada en el dashboard cuando la severidad no es nula.</td>
      <td align="left">`highlighted`</td>
      <td align="left">`equals()`</td>
      <td align="left">usado por `ExposureState`</td>
    </tr>
    <tr>
      <td align="left">`ExcessDetectionPolicy`</td>
      <td align="left">Domain Service</td>
      <td align="left">Cuando se registra una lectura, detecta exceso de CO₂ o de ruido.</td>
      <td align="left">—</td>
      <td align="left">`onReadingRecorded()`</td>
      <td align="left">comanda `ExposureState`</td>
    </tr>
    <tr>
      <td align="left">`ExposureEvaluationPolicy`</td>
      <td align="left">Domain Service</td>
      <td align="left">Cuando cambia una lectura o la presencia, evalúa la exposición del personal. No espera al evento de exceso: lee las mediciones directamente.</td>
      <td align="left">—</td>
      <td align="left">`onReadingOrPresenceChanged()`</td>
      <td align="left">comanda `ExposureState`</td>
    </tr>
    <tr>
      <td align="left">`SeverityClassificationPolicy`</td>
      <td align="left">Domain Service</td>
      <td align="left">Clasifica la severidad; si no es nula, destaca el riesgo del área y levanta la alerta ambiental.</td>
      <td align="left">—</td>
      <td align="left">`onExposureEvaluated()`</td>
      <td align="left">comanda `ExposureState`</td>
    </tr>
    <tr>
      <td align="left">`ActuationPolicy`</td>
      <td align="left">Domain Service</td>
      <td align="left">Extractor si hay CO₂ excesivo, con o sin personal. Sirena solo si hay exposición de personal a CO₂. Mampara y sirena si hay ruido excesivo y presencia.</td>
      <td align="left">—</td>
      <td align="left">`onExcessOrExposure()`</td>
      <td align="left">comanda `AreaActuators`</td>
    </tr>
    <tr>
      <td align="left">`NormalizePolicy`</td>
      <td align="left">Domain Service</td>
      <td align="left">Un solo normalize cuando las condiciones vuelven al rango: actuadores, retiro de alerta y resolución de la exposición.</td>
      <td align="left">—</td>
      <td align="left">`onConditionsWithinThresholds()`</td>
      <td align="left">comanda ambos aggregates</td>
    </tr>
    <tr>
      <td align="left">`IActuatorCommandPort`</td>
      <td align="left">Port (interface)</td>
      <td align="left">Activate / Normalize hacia firmware: `areaId` + `actuatorType`, sin `deviceId`.</td>
      <td align="left">—</td>
      <td align="left">`activate()`, `normalize()`</td>
      <td align="left">implementado en Infrastructure</td>
    </tr>
    <tr>
      <td align="left">`IOfflineAlertPort`</td>
      <td align="left">Port (interface)</td>
      <td align="left">Persistencia/sync de alerta vía `EdgeNode` si la nube no está alcanzable. El riesgo no cambia de dueño; `ExposureState` no vive dentro de `EdgeNode`.</td>
      <td align="left">—</td>
      <td align="left">`storeCopy()`</td>
      <td align="left">implementado en Infrastructure</td>
    </tr>
    <tr>
      <td align="left">`IExposureStateRepository`</td>
      <td align="left">Repository (interface)</td>
      <td align="left">Persistencia de `ExposureState`.</td>
      <td align="left">—</td>
      <td align="left">`findByAreaId()`, `save()`</td>
      <td align="left">implementada en Infrastructure</td>
    </tr>
    <tr>
      <td align="left">`IAreaActuatorsRepository`</td>
      <td align="left">Repository (interface)</td>
      <td align="left">Persistencia de `AreaActuators`.</td>
      <td align="left">—</td>
      <td align="left">`findByAreaId()`, `save()`</td>
      <td align="left">implementada en Infrastructure</td>
    </tr>
  </tbody>
</table>

<a id="s-4-2-2-2"></a>
## 4.2.2.2. Interface Layer

Un controller HTTP en **cloud** para el supervisor móvil (estado operativo, alertas y anulación) y un consumer en el runtime **Edge** para los eventos de la proyección de Plant Monitoring. 

<table>
  <thead>
    <tr>
      <th align="left">Clase</th>
      <th align="left">Tipo</th>
      <th align="left">Propósito</th>
      <th align="left">Métodos / Endpoints</th>
      <th align="left">Colabora con</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td align="left">`AreaSafetyController`</td>
      <td align="left">Controller</td>
      <td align="left">Estado operativo del área, alertas activas y anulación de actuador. Exige sesión de supervisor en la aplicación móvil.</td>
      <td align="left">`getAreaOperationalStatus()`, `getActiveAlerts()`, `overrideActuator()`</td>
      <td align="left">Supervisor Mobile App; Application Layer</td>
    </tr>
    <tr>
      <td align="left">`PlantTelemetryEventConsumer`</td>
      <td align="left">Consumer</td>
      <td align="left">Recibe lecturas, presencia y “conditions within thresholds” desde Plant Monitoring (proyección en Edge; in-process en planta).</td>
      <td align="left">`onCarbonDioxideReadingRecorded()`, `onNoiseReadingRecorded()`, `onPresenceChanged()`, `onConditionsWithinThresholds()`</td>
      <td align="left">Plant Monitoring; Application Layer</td>
    </tr>
  </tbody>
</table>

<a id="s-4-2-2-3"></a>
## 4.2.2.3. Application Layer

Los event handlers de entrada disparan las reglas de negocio; hay un command handler por cada flujo de exposición y actuación, y dos consultas que **no** se fusionan: estado operativo del área y listado de alertas activas. El estado operativo se proyecta aquí a partir de lecturas ya consumidas.

<table>
  <thead>
    <tr>
      <th align="left">Clase</th>
      <th align="left">Tipo</th>
      <th align="left">Comando / Evento</th>
      <th align="left">Propósito</th>
      <th align="left">Colabora con</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td align="left">`OnCarbonDioxideReadingRecordedHandler`</td>
      <td align="left">Event Handler</td>
      <td align="left">Carbon dioxide reading recorded</td>
      <td align="left">Dispara la detección de exceso y la evaluación de exposición.</td>
      <td align="left">`ExcessDetectionPolicy`, `ExposureEvaluationPolicy`</td>
    </tr>
    <tr>
      <td align="left">`OnNoiseReadingRecordedHandler`</td>
      <td align="left">Event Handler</td>
      <td align="left">Noise reading recorded</td>
      <td align="left">Dispara la detección de exceso y la evaluación de exposición.</td>
      <td align="left">`ExcessDetectionPolicy`, `ExposureEvaluationPolicy`</td>
    </tr>
    <tr>
      <td align="left">`OnPresenceChangedHandler`</td>
      <td align="left">Event Handler</td>
      <td align="left">Presence changed</td>
      <td align="left">Dispara la evaluación de exposición.</td>
      <td align="left">`ExposureEvaluationPolicy`</td>
    </tr>
    <tr>
      <td align="left">`OnConditionsWithinThresholdsHandler`</td>
      <td align="left">Event Handler</td>
      <td align="left">Conditions within thresholds</td>
      <td align="left">Dispara el normalize único (actuadores, alerta y exposición).</td>
      <td align="left">`NormalizePolicy`</td>
    </tr>
    <tr>
      <td align="left">`DetectEnvironmentalExcessHandler`</td>
      <td align="left">Command Handler</td>
      <td align="left">Detect environmental excess</td>
      <td align="left">Registra exceso de CO₂ o de ruido.</td>
      <td align="left">`IExposureStateRepository`</td>
    </tr>
    <tr>
      <td align="left">`EvaluatePersonnelExposureHandler`</td>
      <td align="left">Command Handler</td>
      <td align="left">Evaluate personnel exposure</td>
      <td align="left">Identifica exposición con personal, exceso sin personal, o estado seguro.</td>
      <td align="left">`IExposureStateRepository`</td>
    </tr>
    <tr>
      <td align="left">`ClassifyExposureSeverityHandler`</td>
      <td align="left">Command Handler</td>
      <td align="left">Classify exposure severity</td>
      <td align="left">Asigna severidad, o la omite si el área no tiene umbrales.</td>
      <td align="left">`IExposureStateRepository`</td>
    </tr>
    <tr>
      <td align="left">`HighlightAreaRiskHandler`</td>
      <td align="left">Command Handler</td>
      <td align="left">Highlight area risk</td>
      <td align="left">Marca el área como en riesgo en el dashboard móvil.</td>
      <td align="left">`IExposureStateRepository`</td>
    </tr>
    <tr>
      <td align="left">`RaiseEnvironmentalAlertHandler`</td>
      <td align="left">Command Handler</td>
      <td align="left">Raise environmental alert</td>
      <td align="left">Levanta la alerta; si la nube no alcanza, persiste vía `EdgeNode` para sync (`PO-09`).</td>
      <td align="left">`IExposureStateRepository`, `IOfflineAlertPort`</td>
    </tr>
    <tr>
      <td align="left">`WithdrawEnvironmentalAlertHandler`</td>
      <td align="left">Command Handler</td>
      <td align="left">Withdraw environmental alert</td>
      <td align="left">Retira la alerta al normalizar.</td>
      <td align="left">`IExposureStateRepository`</td>
    </tr>
    <tr>
      <td align="left">`ResolveExposureHandler`</td>
      <td align="left">Command Handler</td>
      <td align="left">Resolve exposure</td>
      <td align="left">Cierra el estado de exposición al normalizar.</td>
      <td align="left">`IExposureStateRepository`</td>
    </tr>
    <tr>
      <td align="left">`ActivateActuatorHandler`</td>
      <td align="left">Command Handler</td>
      <td align="left">Activate actuator</td>
      <td align="left">Enciende extractor, sirena o mampara del área vía firmware (**runtime Edge**).</td>
      <td align="left">`IAreaActuatorsRepository`, `IActuatorCommandPort`</td>
    </tr>
    <tr>
      <td align="left">`NormalizeActuatorHandler`</td>
      <td align="left">Command Handler</td>
      <td align="left">Normalize actuator</td>
      <td align="left">Apaga / retrae el tipo indicado.</td>
      <td align="left">`IAreaActuatorsRepository`, `IActuatorCommandPort`</td>
    </tr>
    <tr>
      <td align="left">`RecordAutomaticActuatorActionHandler`</td>
      <td align="left">Command Handler</td>
      <td align="left">Record automatic actuator action</td>
      <td align="left">Auditoría de éxito o fallo de relé; **sin reintento**.</td>
      <td align="left">`IAreaActuatorsRepository`</td>
    </tr>
    <tr>
      <td align="left">`OverrideActuatorHandler`</td>
      <td align="left">Command Handler</td>
      <td align="left">Override actuator</td>
      <td align="left">Control manual sin esperar sensores. Solo supervisor en la aplicación móvil; Identity ya denegó el canal web. Cloud reenvía el comando al Safety de Edge si hay WAN.</td>
      <td align="left">`IAreaActuatorsRepository`, `IActuatorCommandPort`</td>
    </tr>
    <tr>
      <td align="left">`GetAreaOperationalStatusHandler`</td>
      <td align="left">Query Handler</td>
      <td align="left">Get AreaOperationalStatus</td>
      <td align="left">Dashboard móvil: mediciones ya vistas y severidad. No se fusiona con el listado de alertas.</td>
      <td align="left">`IExposureStateRepository`</td>
    </tr>
    <tr>
      <td align="left">`GetActiveAlertsHandler`</td>
      <td align="left">Query Handler</td>
      <td align="left">Get ActiveAlerts</td>
      <td align="left">Lista de alertas ambientales aún no retiradas.</td>
      <td align="left">`IExposureStateRepository`</td>
    </tr>
  </tbody>
</table>

<a id="s-4-2-2-4"></a>
## 4.2.2.4. Infrastructure Layer

Repositorios en **Edge Database** (loop vivo) y **Cloud Database** (auditoría/sync; motor `TBD`). `FirmwareActuatorAdapter` solo en el runtime Edge. `OfflineAlertCopyAdapter` persiste en `EdgeNode` y sincroniza cuando vuelve el enlace.

<table>
  <thead>
    <tr>
      <th align="left">Clase</th>
      <th align="left">Tipo</th>
      <th align="left">Interfaz que implementa</th>
      <th align="left">Servicio externo</th>
      <th align="left">Propósito</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td align="left">`ExposureStateRepository`</td>
      <td align="left">Repository (implementación)</td>
      <td align="left">`IExposureStateRepository`</td>
      <td align="left">Edge Database (loop vivo) y Cloud Database (sync/auditoría; motor TBD)</td>
      <td align="left">Persistencia de exposición y alertas.</td>
    </tr>
    <tr>
      <td align="left">`AreaActuatorsRepository`</td>
      <td align="left">Repository (implementación)</td>
      <td align="left">`IAreaActuatorsRepository`</td>
      <td align="left">Edge Database (loop vivo) y Cloud Database (sync/auditoría; motor TBD)</td>
      <td align="left">Persistencia de estados lógicos por `(area, tipo)`.</td>
    </tr>
    <tr>
      <td align="left">`FirmwareActuatorAdapter`</td>
      <td align="left">Adapter</td>
      <td align="left">`IActuatorCommandPort`</td>
      <td align="left">Device Embedded Application</td>
      <td align="left">Entrega `activate` / `normalize` con `areaId` + `actuatorType` al firmware **desde el runtime Edge**, que mueve el relé.</td>
    </tr>
    <tr>
      <td align="left">`OfflineAlertCopyAdapter`</td>
      <td align="left">Adapter</td>
      <td align="left">`IOfflineAlertPort`</td>
      <td align="left">`EdgeNode`</td>
      <td align="left">Persiste la alerta para sync si la nube no alcanza. Safety sigue dueña del riesgo; no es un volcado desde el monolito.</td>
    </tr>
  </tbody>
</table>

<a id="s-4-2-2-5"></a>
## 4.2.2.5. Bounded Context Software Architecture Component Level Diagrams

Safety & Actuation se reparte en dos containers. En **cloud** (`Web Monolithic Backend`) las cuatro capas atienden estado, alertas y anulación del supervisor móvil; Infrastructure persiste la copia de auditoría en `Cloud Database` y reenvía el override al runtime Edge si hay WAN. En **planta** (`Edge Application`) las mismas cuatro capas corren el loop `: Interface consume la proyección de Plant Monitoring; Infrastructure escribe el estado vivo en `Edge Database`, manda `activate`/`normalize` al firmware y deja `PO-09` en `EdgeNode`.

![Component Level Diagram — cloud](../../assets/04-capitulo-iv/bounded-contexts/bc-02-component.png)

![Component Level Diagram — edge](../../assets/04-capitulo-iv/bounded-contexts/bc-02-component-edge.png)

<a id="s-4-2-2-6"></a>
## 4.2.2.6. Bounded Context Software Architecture Code Level Diagrams

<a id="s-4-2-2-6-1"></a>
### 4.2.2.6.1. Bounded Context Domain Layer Class Diagrams

![Domain Layer Class Diagram](../../assets/04-capitulo-iv/bounded-contexts/bc-02-domain-class.png)

<a id="s-4-2-2-6-2"></a>
### 4.2.2.6.2. Bounded Context Database Design Diagram

Modelo relacional lógico, **los mismos** hechos en dos almacenes: Edge Database (loop vivo) y Cloud Database (sync/auditoría). Tablas: `exposure_states` (`area_id` UNIQUE), `environmental_alerts`, `area_actuator_states` (clave lógica `area_id` + `actuator_type`, **sin** `device_id`) y `automatic_actuator_actions`.

![Database Design Diagram](../../assets/04-capitulo-iv/bounded-contexts/bc-02-database.png)
