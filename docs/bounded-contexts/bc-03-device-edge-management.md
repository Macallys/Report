<a id="s-4-2-3"></a>
# 4.2.3. Bounded Context: Device & Edge Management

**Navegación:** [Capítulo IV](../04-capitulo-iv-solution-software-design.md) · [Índice](../00-student-outcome.md#s-tabla-contenidos)

---

Device & Edge Management autentica dispositivos de campo, consume las lecturas publicadas al broker MQTT y las entrega a Plant Monitoring, y mantiene continuidad si la nube no alcanza: cola local, reintento al recuperar el enlace y copia de alerta. Es un contexto **supporting**: no interpreta umbrales ni exposición.

El mismo contexto está **repartido** en dos containers. En el **Web Monolithic Backend** vive el registro maestro de `DeviceCredential`: emitir, revocar y validar contra la fuente de verdad. En la **Edge Application** vive `EdgeNode`: autenticar el firmware, consumir MQTT sin unificar CO₂, ruido y presencia, ingest hacia Plant Monitoring, cola y sync, y la copia de alerta que el Safety **runtime (hermano en el mismo container)** deja para sincronizar.

Ubiquitous language: *Device credential* · *Device authenticated* · *Edge node* · *Telemetry queued locally* · *Local telemetry sync* · *Offline alert stored* · *Duplicate telemetry acknowledged* · *Ingest telemetry*.

<a id="s-4-2-3-1"></a>
## 4.2.3.1. Domain Layer

Dos aggregate roots en el mismo bounded context y en distintos procesos: `DeviceCredential` en la nube y `EdgeNode` en el runtime de planta. Las lecturas encoladas son hechos **separados** (`QueuedReading` con un tipo CO₂, ruido o presencia), no un `EnvironmentReading` unificado. Las políticas de cola y sync son domain services **in-process** en el Edge: si el ingest falla o no hay enlace, se encola; al recuperar conectividad se reintenta el **mismo** comando de ingest. El sync no inventa un segundo hecho de negocio por la misma lectura (`acknowledgeDuplicate`). La copia de alerta solo guarda `areaId` y `alertId`.

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
      <td align="left">`DeviceCredential`</td>
      <td align="left">Aggregate Root (cloud)</td>
      <td align="left">Registro maestro de identidad del dispositivo. Fuente de verdad para emitir, autenticar y revocar.</td>
      <td align="left">`id`, `deviceId`, `secret`, `issuedAt`, `expiresAt`, `revokedAt`</td>
      <td align="left">`issue()`, `authenticate()`, `revoke()`</td>
      <td align="left">1 `DeviceId`; 1 `DeviceSecret`</td>
    </tr>
    <tr>
      <td align="left">`EdgeNode`</td>
      <td align="left">Aggregate Root (edge)</td>
      <td align="left">Cola local, sync idempotente y copias de alerta en el servidor de planta. No evalúa exposición.</td>
      <td align="left">`id`</td>
      <td align="left">`queueTelemetry()`, `syncLocalTelemetry()`, `storeOfflineAlert()`, `acknowledgeDuplicate()`</td>
      <td align="left">0..* `QueuedReading`; 0..* `OfflineAlertCopy`</td>
    </tr>
    <tr>
      <td align="left">`DeviceId`</td>
      <td align="left">Value Object</td>
      <td align="left">Identificador del dispositivo de campo. Distinto de una cuenta de usuario.</td>
      <td align="left">`value`</td>
      <td align="left">`equals()`</td>
      <td align="left">usado por `DeviceCredential` y `QueuedReading`</td>
    </tr>
    <tr>
      <td align="left">`DeviceSecret`</td>
      <td align="left">Value Object</td>
      <td align="left">Secreto almacenado como hash. Nunca se persiste en claro.</td>
      <td align="left">`hash`</td>
      <td align="left">`matches()`, `equals()`</td>
      <td align="left">usado por `DeviceCredential`</td>
    </tr>
    <tr>
      <td align="left">`QueuedReading`</td>
      <td align="left">Value Object</td>
      <td align="left">Hecho pendiente de ingest: un solo tipo (CO₂, ruido o presencia) y clave de idempotencia.</td>
      <td align="left">`deviceId`, `kind`, `measuredAt`, `payload`, `idempotencyKey`</td>
      <td align="left">`equals()`</td>
      <td align="left">contenido en `EdgeNode`</td>
    </tr>
    <tr>
      <td align="left">`OfflineAlertCopy`</td>
      <td align="left">Value Object</td>
      <td align="left">Copia local de una alerta ambiental. No incluye estado de exposición.</td>
      <td align="left">`areaId`, `alertId`, `storedAt`</td>
      <td align="left">`equals()`</td>
      <td align="left">contenido en `EdgeNode`</td>
    </tr>
    <tr>
      <td align="left">`ReadingKind`</td>
      <td align="left">Value Object (Enum)</td>
      <td align="left">`CarbonDioxide`, `Noise`, `Presence`. Tres hechos; no se fusionan.</td>
      <td align="left">`value`</td>
      <td align="left">—</td>
      <td align="left">usado por `QueuedReading`</td>
    </tr>
    <tr>
      <td align="left">`LocalQueuePolicy`</td>
      <td align="left">Domain Service (edge)</td>
      <td align="left">Si Plant Monitoring rechaza el ingest o la nube no alcanza, encola la lectura en `EdgeNode`.</td>
      <td align="left">—</td>
      <td align="left">`onIngestFailedOrUnreachable()`</td>
      <td align="left">comanda `EdgeNode`</td>
    </tr>
    <tr>
      <td align="left">`TelemetrySyncPolicy`</td>
      <td align="left">Domain Service (edge)</td>
      <td align="left">Al recuperar el enlace, sincroniza la cola y reintenta el mismo ingest. No duplica el hecho de negocio.</td>
      <td align="left">—</td>
      <td align="left">`onConnectivityRestored()`</td>
      <td align="left">comanda `EdgeNode`</td>
    </tr>
    <tr>
      <td align="left">`IDeviceCredentialRepository`</td>
      <td align="left">Repository (interface)</td>
      <td align="left">Persistencia del registro maestro en Cloud Database.</td>
      <td align="left">—</td>
      <td align="left">`findByDeviceId()`, `save()`</td>
      <td align="left">implementada en Infrastructure (cloud)</td>
    </tr>
    <tr>
      <td align="left">`IEdgeNodeRepository`</td>
      <td align="left">Repository (interface)</td>
      <td align="left">Persistencia del nodo, la cola y las copias en Edge Database.</td>
      <td align="left">—</td>
      <td align="left">`load()`, `save()`, `findPendingReadings()`, `saveQueuedReading()`</td>
      <td align="left">implementada en Infrastructure (edge)</td>
    </tr>
    <tr>
      <td align="left">`IMqttSubscriber`</td>
      <td align="left">Port (interface)</td>
      <td align="left">Suscripción a tres tópicos/hechos. El firmware publica; este contexto consume.</td>
      <td align="left">—</td>
      <td align="left">`subscribeCarbonDioxide()`, `subscribeNoise()`, `subscribePresence()`</td>
      <td align="left">implementado en Infrastructure (edge)</td>
    </tr>
    <tr>
      <td align="left">`ITelemetryIngestPort`</td>
      <td align="left">Port (interface)</td>
      <td align="left">Ingest de un hecho hacia Plant Monitoring. El reintento usa este mismo puerto.</td>
      <td align="left">—</td>
      <td align="left">`ingest()`</td>
      <td align="left">implementado en Infrastructure (edge)</td>
    </tr>
    <tr>
      <td align="left">`ICredentialSyncPort`</td>
      <td align="left">Port (interface)</td>
      <td align="left">Sincroniza la credencial del dispositivo entre Edge y el maestro cloud.</td>
      <td align="left">—</td>
      <td align="left">`syncFromCloud()`</td>
      <td align="left">implementado en Infrastructure (edge)</td>
    </tr>
  </tbody>
</table>

<a id="s-4-2-3-2"></a>
## 4.2.3.2. Interface Layer

En la nube, un controller interno emite y revoca credenciales de dispositivo (no cuentas de usuario). En el Edge, el firmware se autentica, un consumer MQTT recibe tres hechos sin unificarlos y un consumer recibe `Store offline alert` desde el Safety runtime **local**. No hay un «IoT Gateway» como colaborador.

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
      <td align="left">`DeviceCredentialController`</td>
      <td align="left">Controller (cloud)</td>
      <td align="left">API interna de emisión y revocación del registro maestro. No gestiona usuarios.</td>
      <td align="left">`issue()`, `revoke()`</td>
      <td align="left">Application Layer (cloud)</td>
    </tr>
    <tr>
      <td align="left">`DeviceAuthenticationController`</td>
      <td align="left">Controller (edge)</td>
      <td align="left">Autentica el firmware contra la credencial (con sync al maestro si hace falta).</td>
      <td align="left">`authenticate()`</td>
      <td align="left">Device Embedded Application; Application Layer (edge)</td>
    </tr>
    <tr>
      <td align="left">`MqttTelemetryConsumer`</td>
      <td align="left">Consumer (edge)</td>
      <td align="left">Consume tres tópicos: CO₂, ruido y presencia. No unifica las lecturas.</td>
      <td align="left">`onCarbonDioxideReading()`, `onNoiseReading()`, `onPresenceChanged()`</td>
      <td align="left">MQTT Broker; Application Layer (edge)</td>
    </tr>
    <tr>
      <td align="left">`OfflineAlertConsumer`</td>
      <td align="left">Consumer (edge)</td>
      <td align="left">Recibe `Store offline alert` desde el Safety runtime **local** (in-process). No es un POST desde el monolito.</td>
      <td align="left">`onStoreOfflineAlert()`</td>
      <td align="left">Safety & Actuation; Application Layer (edge)</td>
    </tr>
  </tbody>
</table>

<a id="s-4-2-3-3"></a>
## 4.2.3.3. Application Layer

Handlers de emisión, autenticación y revocación en la nube; en el Edge, autenticar, ingerir hacia Plant Monitoring, encolar, sincronizar y guardar la copia de alerta. El reintento de ingest es el mismo comando, no un segundo tipo.

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
      <td align="left">`IssueDeviceCredentialHandler`</td>
      <td align="left">Command Handler (cloud)</td>
      <td align="left">Issue device credential</td>
      <td align="left">Emite el registro maestro del dispositivo.</td>
      <td align="left">`IDeviceCredentialRepository`</td>
    </tr>
    <tr>
      <td align="left">`AuthenticateDeviceCredentialHandler`</td>
      <td align="left">Command Handler (cloud)</td>
      <td align="left">Authenticate device credential</td>
      <td align="left">Valida el secreto contra la fuente de verdad. No es un inicio de sesión de usuario.</td>
      <td align="left">`IDeviceCredentialRepository`</td>
    </tr>
    <tr>
      <td align="left">`RevokeDeviceCredentialHandler`</td>
      <td align="left">Command Handler (cloud)</td>
      <td align="left">Revoke device credential</td>
      <td align="left">Revoca la credencial en el maestro.</td>
      <td align="left">`IDeviceCredentialRepository`</td>
    </tr>
    <tr>
      <td align="left">`AuthenticateDeviceHandler`</td>
      <td align="left">Command Handler (edge)</td>
      <td align="left">Authenticate device</td>
      <td align="left">Autentica el firmware en el Edge; sincroniza con el maestro si es necesario.</td>
      <td align="left">`ICredentialSyncPort`, `IEdgeNodeRepository`</td>
    </tr>
    <tr>
      <td align="left">`IngestTelemetryHandler`</td>
      <td align="left">Command Handler (edge)</td>
      <td align="left">Ingest telemetry</td>
      <td align="left">Entrega un hecho (CO₂, ruido o presencia) a Plant Monitoring. El reintento usa este mismo handler.</td>
      <td align="left">`ITelemetryIngestPort`, `LocalQueuePolicy`</td>
    </tr>
    <tr>
      <td align="left">`QueueLocallyHandler`</td>
      <td align="left">Command Handler (edge)</td>
      <td align="left">Queue locally</td>
      <td align="left">Encola la lectura cuando el ingest falla o la nube no alcanza.</td>
      <td align="left">`IEdgeNodeRepository`</td>
    </tr>
    <tr>
      <td align="left">`SyncLocalTelemetryHandler`</td>
      <td align="left">Command Handler (edge)</td>
      <td align="left">Sync local telemetry</td>
      <td align="left">Al recuperar el enlace, reintenta ingest y reconoce duplicados.</td>
      <td align="left">`IEdgeNodeRepository`, `IngestTelemetryHandler`</td>
    </tr>
    <tr>
      <td align="left">`StoreOfflineAlertHandler`</td>
      <td align="left">Command Handler (edge)</td>
      <td align="left">Store offline alert</td>
      <td align="left">Persiste la copia de alerta. No altera el dueño del riesgo.</td>
      <td align="left">`IEdgeNodeRepository`</td>
    </tr>
  </tbody>
</table>

<a id="s-4-2-3-4"></a>
## 4.2.3.4. Infrastructure Layer

Repositorio de credenciales sobre Cloud Database; cola y copias sobre Edge Database; adapter MQTT; ingest hacia Plant Monitoring; sync de credenciales Edge ↔ nube.

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
      <td align="left">`DeviceCredentialRepository`</td>
      <td align="left">Repository (implementación)</td>
      <td align="left">`IDeviceCredentialRepository`</td>
      <td align="left">Cloud Database (motor TBD)</td>
      <td align="left">Persistencia del registro maestro de credenciales.</td>
    </tr>
    <tr>
      <td align="left">`EdgeNodeRepository`</td>
      <td align="left">Repository (implementación)</td>
      <td align="left">`IEdgeNodeRepository`</td>
      <td align="left">Edge Database (motor TBD)</td>
      <td align="left">Persistencia del nodo, la cola y las copias de alerta.</td>
    </tr>
    <tr>
      <td align="left">`MqttBrokerAdapter`</td>
      <td align="left">Adapter</td>
      <td align="left">`IMqttSubscriber`</td>
      <td align="left">MQTT Broker (producto TBD)</td>
      <td align="left">Consume los tres tópicos de lecturas. El broker es container interno de SafePlant.</td>
    </tr>
    <tr>
      <td align="left">`PlantMonitoringIngestAdapter`</td>
      <td align="left">Adapter</td>
      <td align="left">`ITelemetryIngestPort`</td>
      <td align="left">Plant Monitoring (mismo sistema; Interface del monolito)</td>
      <td align="left">Entrega un hecho de telemetría al ingest de Plant Monitoring.</td>
    </tr>
    <tr>
      <td align="left">`CloudCredentialSyncAdapter`</td>
      <td align="left">Adapter</td>
      <td align="left">`ICredentialSyncPort`</td>
      <td align="left">Device & Edge (cloud)</td>
      <td align="left">Sincroniza la credencial con el maestro en el monolito.</td>
    </tr>
  </tbody>
</table>

<a id="s-4-2-3-5"></a>
## 4.2.3.5. Bounded Context Software Architecture Component Level Diagrams

En la nube, Interface expone emisión y revocación; Application invoca `DeviceCredential`; Infrastructure persiste en `Cloud Database` y atiende el sync desde el Edge.

En runtime, el firmware se autentica en Interface; el broker MQTT entrega lecturas; Application orquesta ingest, cola y copia de alerta. Infrastructure escribe en `Edge Database`, ingiere en Plant Monitoring (Interface del monolito) y sincroniza credenciales.

![Component Level Diagram — cloud](../../assets/04-capitulo-iv/bounded-contexts/bc-03-component-cloud.png)

![Component Level Diagram — edge](../../assets/04-capitulo-iv/bounded-contexts/bc-03-component-edge.png)

<a id="s-4-2-3-6"></a>
## 4.2.3.6. Bounded Context Software Architecture Code Level Diagrams

<a id="s-4-2-3-6-1"></a>
### 4.2.3.6.1. Bounded Context Domain Layer Class Diagrams

![Domain Layer Class Diagram](../../assets/04-capitulo-iv/bounded-contexts/bc-03-domain-class.png)

<a id="s-4-2-3-6-2"></a>
### 4.2.3.6.2. Bounded Context Database Design Diagram

Dos esquemas lógicos. Cloud Database: `device_credentials` (`device_id` UNIQUE, `secret_hash`, vigencia, `revoked_at`). Edge Database: `telemetry_queue` (tipo de hecho separado, `idempotency_key`) y `offline_alert_copies` (`area_id`, `alert_id`, `stored_at`).

![Database Design Diagram](../../assets/04-capitulo-iv/bounded-contexts/bc-03-database.png)
