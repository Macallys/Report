<a id="s-4-2-1"></a>
# 4.2.1. Bounded Context: Plant Monitoring

**Navegación:** [Capítulo IV](../04-capitulo-iv-solution-software-design.md) · [Índice](../00-student-outcome.md#s-tabla-contenidos)

---

Plant Monitoring da a la planta una definición estable de áreas, umbrales ambientales y qué dispositivo mide o actúa en cada zona, y registra el hecho histórico de CO₂, ruido y presencia. Es el **Core Domain**: quien usa SafePlant ve el estado de la planta aquí; no se decide exposición ni se disparan actuadores (Safety & Actuation). En `Edge Application` solo hay una **proyección** para el loop local de Safety.

Ubiquitous language: *Industrial area* · *Environmental thresholds* · *Area device assignment* · *Carbon dioxide reading* · *Noise reading* · *Presence (detected / cleared)* · *Telemetry ingested* · *Sensor associated to area* · *Actuator associated to area* · *Plant metrics history*.

<a id="s-4-2-1-1"></a>
## 4.2.1.1. Domain Layer

El core del contexto son cuatro aggregates —`IndustrialArea`, `AreaThresholds`, `AreaDeviceAssignment`, `AreaTelemetry`— con value objects, las entidades de lectura separadas (CO₂, ruido, presencia) y las interfaces de repositorio.

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
      <td align="left">`IndustrialArea`</td>
      <td align="left">Aggregate Root</td>
      <td align="left">Ficha de un área industrial: nombre único y ubicación.</td>
      <td align="left">`id`, `name`, `location`</td>
      <td align="left">`register()`, `update()`, `updateSystemConfiguration()`</td>
      <td align="left">1—0..1 `AreaThresholds`; 1—0..* `AreaDeviceAssignment`; 1—1 `AreaTelemetry`</td>
    </tr>
    <tr>
      <td align="left">`AreaThresholds`</td>
      <td align="left">Aggregate Root</td>
      <td align="left">Límites de CO₂ y ruido de esa área. Sin umbrales, Safety no clasifica.</td>
      <td align="left">`id`, `areaId`, `co2Limit`, `noiseLimit`</td>
      <td align="left">`configure()`, `update()`</td>
      <td align="left">pertenece a 1 `IndustrialArea`</td>
    </tr>
    <tr>
      <td align="left">`AreaDeviceAssignment`</td>
      <td align="left">Aggregate Root</td>
      <td align="left">Asociación de un sensor o actuador a un área. Un `deviceId` no se duplica.</td>
      <td align="left">`id`, `areaId`, `deviceId`, `kind`</td>
      <td align="left">`associate()`</td>
      <td align="left">pertenece a 1 `IndustrialArea`</td>
    </tr>
    <tr>
      <td align="left">`AreaTelemetry`</td>
      <td align="left">Aggregate Root</td>
      <td align="left">Invariante de ingest y registro histórico por área. Acepta, rechaza o reconoce duplicado.</td>
      <td align="left">`id`, `areaId`</td>
      <td align="left">`recordCarbonDioxide()`, `recordNoise()`, `recordPresence()`, `acceptIngest()`, `rejectIngest()`, `acknowledgeDuplicate()`, `markSensorUnavailable()`</td>
      <td align="left">pertenece a 1 `IndustrialArea`; contiene 0..* lecturas de cada tipo</td>
    </tr>
    <tr>
      <td align="left">`CarbonDioxideReading`</td>
      <td align="left">Entity</td>
      <td align="left">Hecho de CO₂; no se fusiona con ruido ni presencia. Lectura inválida se descarta.</td>
      <td align="left">`id`, `deviceId`, `ppm`, `recordedAt`</td>
      <td align="left">—</td>
      <td align="left">contenido en `AreaTelemetry`</td>
    </tr>
    <tr>
      <td align="left">`NoiseReading`</td>
      <td align="left">Entity</td>
      <td align="left">Hecho de ruido.</td>
      <td align="left">`id`, `deviceId`, `db`, `recordedAt`</td>
      <td align="left">—</td>
      <td align="left">contenido en `AreaTelemetry`</td>
    </tr>
    <tr>
      <td align="left">`PresenceChange`</td>
      <td align="left">Entity</td>
      <td align="left">Presencia detectada o despejada.</td>
      <td align="left">`id`, `deviceId`, `state`, `recordedAt`</td>
      <td align="left">—</td>
      <td align="left">contenido en `AreaTelemetry`</td>
    </tr>
    <tr>
      <td align="left">`AreaName`</td>
      <td align="left">Value Object</td>
      <td align="left">Nombre del área, único en la planta.</td>
      <td align="left">`value`</td>
      <td align="left">`equals()`</td>
      <td align="left">usado por `IndustrialArea`</td>
    </tr>
    <tr>
      <td align="left">`Location`</td>
      <td align="left">Value Object</td>
      <td align="left">Ficha de ubicación del área.</td>
      <td align="left">`value`</td>
      <td align="left">`equals()`</td>
      <td align="left">usado por `IndustrialArea`</td>
    </tr>
    <tr>
      <td align="left">`Co2Limit`</td>
      <td align="left">Value Object</td>
      <td align="left">Umbral de CO₂ del área.</td>
      <td align="left">`ppm`</td>
      <td align="left">`equals()`</td>
      <td align="left">usado por `AreaThresholds`</td>
    </tr>
    <tr>
      <td align="left">`NoiseLimit`</td>
      <td align="left">Value Object</td>
      <td align="left">Umbral de ruido del área.</td>
      <td align="left">`db`</td>
      <td align="left">`equals()`</td>
      <td align="left">usado por `AreaThresholds`</td>
    </tr>
    <tr>
      <td align="left">`DeviceId`</td>
      <td align="left">Value Object</td>
      <td align="left">Identificador de dispositivo; no se duplica en asociaciones.</td>
      <td align="left">`value`</td>
      <td align="left">`equals()`</td>
      <td align="left">usado por `AreaDeviceAssignment` y las lecturas</td>
    </tr>
    <tr>
      <td align="left">`DeviceKind`</td>
      <td align="left">Value Object (Enum)</td>
      <td align="left">`Sensor` o `Actuator`.</td>
      <td align="left">`value`</td>
      <td align="left">—</td>
      <td align="left">usado por `AreaDeviceAssignment`</td>
    </tr>
    <tr>
      <td align="left">`Co2Ppm`</td>
      <td align="left">Value Object</td>
      <td align="left">Concentración de CO₂; `isValid()` rechaza fuera de rango.</td>
      <td align="left">`value`</td>
      <td align="left">`isValid()`</td>
      <td align="left">usado por `CarbonDioxideReading`</td>
    </tr>
    <tr>
      <td align="left">`NoiseDb`</td>
      <td align="left">Value Object</td>
      <td align="left">Nivel de ruido en dB.</td>
      <td align="left">`value`</td>
      <td align="left">—</td>
      <td align="left">usado por `NoiseReading`</td>
    </tr>
    <tr>
      <td align="left">`PresenceState`</td>
      <td align="left">Value Object (Enum)</td>
      <td align="left">`Detected` o `Cleared`.</td>
      <td align="left">`value`</td>
      <td align="left">—</td>
      <td align="left">usado por `PresenceChange`</td>
    </tr>
    <tr>
      <td align="left">`IDomainEventPublisher`</td>
      <td align="left">Port (interface)</td>
      <td align="left">Publica eventos de dominio in-process (lecturas y presencia hacia Safety; ingest rechazado hacia Device & Edge). No habla con MQTT.</td>
      <td align="left">—</td>
      <td align="left">`publish()`</td>
      <td align="left">implementado en Infrastructure</td>
    </tr>
    <tr>
      <td align="left">`IIndustrialAreaRepository`</td>
      <td align="left">Repository (interface)</td>
      <td align="left">Persistencia de `IndustrialArea`.</td>
      <td align="left">—</td>
      <td align="left">`findById()`, `findByName()`, `save()`</td>
      <td align="left">implementada en Infrastructure</td>
    </tr>
    <tr>
      <td align="left">`IAreaThresholdsRepository`</td>
      <td align="left">Repository (interface)</td>
      <td align="left">Persistencia de `AreaThresholds`.</td>
      <td align="left">—</td>
      <td align="left">`findByAreaId()`, `save()`</td>
      <td align="left">implementada en Infrastructure</td>
    </tr>
    <tr>
      <td align="left">`IAreaDeviceAssignmentRepository`</td>
      <td align="left">Repository (interface)</td>
      <td align="left">Persistencia de `AreaDeviceAssignment`.</td>
      <td align="left">—</td>
      <td align="left">`findByDeviceId()`, `save()`</td>
      <td align="left">implementada en Infrastructure</td>
    </tr>
    <tr>
      <td align="left">`IAreaTelemetryRepository`</td>
      <td align="left">Repository (interface)</td>
      <td align="left">Persistencia de `AreaTelemetry` y sus lecturas.</td>
      <td align="left">—</td>
      <td align="left">`findLatestByAreaId()`, `save()`</td>
      <td align="left">implementada en Infrastructure</td>
    </tr>
  </tbody>
</table>

<a id="s-4-2-1-2"></a>
## 4.2.1.2. Interface Layer

Dos controllers HTTP cubren setup (supervisor móvil) e historial (plant manager web). Un Consumer in-process recibe `Ingest telemetry` desde Device & Edge.

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
      <td align="left">`PlantSetupController`</td>
      <td align="left">Controller</td>
      <td align="left">Configuración de planta: área, umbrales, asociación de dispositivos y ficha de setup. Exige `sessionToken` de supervisor móvil (OHS).</td>
      <td align="left">`manageIndustrialArea()`, `configureEnvironmentalThresholds()`, `associateDeviceToArea()`, `updateSystemConfiguration()`, `getAreaSetupSheet()`</td>
      <td align="left">Supervisor Mobile App; Application Layer</td>
    </tr>
    <tr>
      <td align="left">`PlantMetricsController`</td>
      <td align="left">Controller</td>
      <td align="left">Historial de métricas de planta, solo lectura, canal web.</td>
      <td align="left">`getPlantMetricsHistory()`</td>
      <td align="left">Plant Manager Web Client; Application Layer</td>
    </tr>
    <tr>
      <td align="left">`TelemetryIngestConsumer`</td>
      <td align="left">Consumer</td>
      <td align="left">Recibe `Ingest telemetry` desde Device & Edge (mismo proceso).</td>
      <td align="left">`ingestTelemetry()`</td>
      <td align="left">Device & Edge Management; Application Layer</td>
    </tr>
  </tbody>
</table>

<a id="s-4-2-1-3"></a>
## 4.2.1.3. Application Layer

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
      <td align="left">`ManageIndustrialAreaHandler`</td>
      <td align="left">Command Handler</td>
      <td align="left">Manage industrial area</td>
      <td align="left">Registra o actualiza un área; rechaza nombre duplicado.</td>
      <td align="left">`IIndustrialAreaRepository`</td>
    </tr>
    <tr>
      <td align="left">`ConfigureEnvironmentalThresholdsHandler`</td>
      <td align="left">Command Handler</td>
      <td align="left">Configure environmental thresholds</td>
      <td align="left">Crea o actualiza umbrales de un área; rechaza valores fuera de rango.</td>
      <td align="left">`IAreaThresholdsRepository`, `IIndustrialAreaRepository`</td>
    </tr>
    <tr>
      <td align="left">`AssociateDeviceToAreaHandler`</td>
      <td align="left">Command Handler</td>
      <td align="left">Associate device to area</td>
      <td align="left">Asocia sensor o actuador; rechaza `deviceId` duplicado.</td>
      <td align="left">`IAreaDeviceAssignmentRepository`, `IIndustrialAreaRepository`</td>
    </tr>
    <tr>
      <td align="left">`UpdateSystemConfigurationHandler`</td>
      <td align="left">Command Handler</td>
      <td align="left">Update system configuration</td>
      <td align="left">Actualiza la ficha de configuración de planta del área.</td>
      <td align="left">`IIndustrialAreaRepository`</td>
    </tr>
    <tr>
      <td align="left">`RecordCarbonDioxideReadingHandler`</td>
      <td align="left">Command Handler</td>
      <td align="left">Record carbon dioxide reading</td>
      <td align="left">Registra el hecho de CO₂ o lo descarta si es inválido.</td>
      <td align="left">`IAreaTelemetryRepository`, `IDomainEventPublisher`</td>
    </tr>
    <tr>
      <td align="left">`RecordNoiseReadingHandler`</td>
      <td align="left">Command Handler</td>
      <td align="left">Record noise reading</td>
      <td align="left">Registra el hecho de ruido.</td>
      <td align="left">`IAreaTelemetryRepository`, `IDomainEventPublisher`</td>
    </tr>
    <tr>
      <td align="left">`RecordPresenceHandler`</td>
      <td align="left">Command Handler</td>
      <td align="left">Record presence</td>
      <td align="left">Registra presencia detectada o despejada.</td>
      <td align="left">`IAreaTelemetryRepository`, `IDomainEventPublisher`</td>
    </tr>
    <tr>
      <td align="left">`MarkSensorUnavailableHandler`</td>
      <td align="left">Event Handler (scheduled)</td>
      <td align="left">Mark sensor unavailable</td>
      <td align="left">Marca un sensor sin transmisión en el intervalo.</td>
      <td align="left">`IAreaTelemetryRepository`</td>
    </tr>
    <tr>
      <td align="left">`IngestTelemetryHandler`</td>
      <td align="left">Command Handler</td>
      <td align="left">Ingest telemetry</td>
      <td align="left">Acepta, rechaza o reconoce duplicado el lote de Edge; invoca los tres `Record*` **sin** unificar lecturas.</td>
      <td align="left">`RecordCarbonDioxideReadingHandler`, `RecordNoiseReadingHandler`, `RecordPresenceHandler`, `IAreaTelemetryRepository`, `IDomainEventPublisher`</td>
    </tr>
    <tr>
      <td align="left">`GetAreaSetupSheetHandler`</td>
      <td align="left">Query Handler</td>
      <td align="left">Get AreaSetupSheet</td>
      <td align="left">Devuelve área, umbrales y dispositivos ya asociados.</td>
      <td align="left">`IIndustrialAreaRepository`, `IAreaThresholdsRepository`, `IAreaDeviceAssignmentRepository`</td>
    </tr>
    <tr>
      <td align="left">`GetPlantMetricsHistoryHandler`</td>
      <td align="left">Query Handler</td>
      <td align="left">Get PlantMetricsHistory</td>
      <td align="left">Historial de lecturas para el dashboard web; no dispara actuadores.</td>
      <td align="left">`IAreaTelemetryRepository`</td>
    </tr>
  </tbody>
</table>

<a id="s-4-2-1-4"></a>
## 4.2.1.4. Infrastructure Layer

Implementaciones de los cuatro repositorios y un publicador in-process. Motor de base de datos `TBD`. No hay adaptador MQTT: Device & Edge es quien consume el broker.

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
      <td align="left">`IndustrialAreaRepository`</td>
      <td align="left">Repository (implementación)</td>
      <td align="left">`IIndustrialAreaRepository`</td>
      <td align="left">Cloud Database (motor TBD)</td>
      <td align="left">Persistencia relacional de áreas.</td>
    </tr>
    <tr>
      <td align="left">`AreaThresholdsRepository`</td>
      <td align="left">Repository (implementación)</td>
      <td align="left">`IAreaThresholdsRepository`</td>
      <td align="left">Cloud Database (motor TBD)</td>
      <td align="left">Persistencia relacional de umbrales.</td>
    </tr>
    <tr>
      <td align="left">`AreaDeviceAssignmentRepository`</td>
      <td align="left">Repository (implementación)</td>
      <td align="left">`IAreaDeviceAssignmentRepository`</td>
      <td align="left">Cloud Database (motor TBD)</td>
      <td align="left">Persistencia relacional de asociaciones dispositivo–área.</td>
    </tr>
    <tr>
      <td align="left">`AreaTelemetryRepository`</td>
      <td align="left">Repository (implementación)</td>
      <td align="left">`IAreaTelemetryRepository`</td>
      <td align="left">Cloud Database (motor TBD)</td>
      <td align="left">Persistencia de lecturas en **tres** tablas distintas.</td>
    </tr>
    <tr>
      <td align="left">`InProcessEventPublisher`</td>
      <td align="left">Adapter</td>
      <td align="left">`IDomainEventPublisher`</td>
      <td align="left">In-process (Safety & Actuation; Device & Edge)</td>
      <td align="left">Publica hacia Safety y Device & Edge. Sin MQTT.</td>
    </tr>
  </tbody>
</table>

<a id="s-4-2-1-5"></a>
## 4.2.1.5. Bounded Context Software Architecture Component Level Diagrams

El Supervisor Mobile App llama a Interface para el setup, el Plant Manager Web Client consulta el historial, y Edge Application entrega el ingest. En el servidor de planta, una **proyección** cachea umbrales y últimas lecturas para Safety. Interface delega en Application, Application invoca Domain, e Infrastructure persiste en `Cloud Database`.

![Component Level Diagram](../../assets/04-capitulo-iv/bounded-contexts/bc-01-component.png)

<a id="s-4-2-1-6"></a>
## 4.2.1.6. Bounded Context Software Architecture Code Level Diagrams

<a id="s-4-2-1-6-1"></a>
### 4.2.1.6.1. Bounded Context Domain Layer Class Diagrams

Incluye los cuatro aggregates, las tres entidades de lectura (sin unificar), value objects, el puerto `IDomainEventPublisher` y las interfaces de repositorio, con scope, multiplicidad y dirección de cada relación.

![Domain Layer Class Diagram](../../assets/04-capitulo-iv/bounded-contexts/bc-01-domain-class.png)

<a id="s-4-2-1-6-2"></a>
### 4.2.1.6.2. Bounded Context Database Design Diagram

Modelo relacional lógico: `industrial_areas`, `area_thresholds` (FK UNIQUE hacia área), `area_device_assignments` (`device_id` UNIQUE), y **tres** tablas de hechos —`carbon_dioxide_readings`, `noise_readings`, `presence_events`— cada una con FK al área.

![Database Design Diagram](../../assets/04-capitulo-iv/bounded-contexts/bc-01-database.png)
