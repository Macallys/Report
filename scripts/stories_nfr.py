# HU38-HU42 — Atributos de calidad (E6) for SafePlant Chapter 3.1


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
    return {"id": hu, "epic": epic, "title": title, "desc": desc, "ac": g(*scenarios)}


STORIES_NFR = [
    S(
        "HU38",
        "EP06",
        "Tiempo de respuesta crítica en activación de actuadores",
        "Como supervisor de seguridad quiero que el sistema active extractores, sirenas y mamparas acústicas dentro de un tiempo máximo de respuesta definido para reducir la exposición del personal a condiciones ambientales peligrosas en la planta industrial.",
        [
            (
                "Activación del extractor por exceso de CO₂ dentro del límite temporal",
                "Dado que una zona crítica presenta una concentración de CO₂ superior al límite permitido<br/>Y el sensor MQ-135 transmite una medición válida al IoT Gateway<br/>Y el extractor de aire de la zona se encuentra operativo",
                "Cuando el sistema confirma la condición de exceso de CO₂ en la zona",
                "el sistema activa el extractor de aire mediante el relé de control en un intervalo inferior a 2 segundos contados desde el instante de la medición válida que originó la alerta",
            ),
            (
                "Activación de sirena preventiva con personal presente dentro del límite temporal",
                "Dado que una zona crítica presenta una condición peligrosa de CO₂ o de ruido superior al límite permitido<br/>Y el sistema registra personal presente en la zona<br/>Y la sirena preventiva de la zona se encuentra operativa",
                "Cuando el sistema determina que existe exposición de operarios a la condición de riesgo",
                "el sistema activa la sirena preventiva de la zona en un intervalo inferior a 2 segundos contados desde el instante en que se confirma la condición de riesgo con personal presente",
            ),
            (
                "Despliegue de mamparas acústicas por exposición sonora dentro del límite temporal",
                "Dado que una zona crítica presenta un nivel de ruido superior al límite permitido<br/>Y el sistema registra personal presente en la zona<br/>Y los servomotores de mamparas acústicas de la zona se encuentran operativos",
                "Cuando el sistema confirma la condición de exposición sonora con personal presente",
                "el sistema activa los servomotores y despliega las mamparas acústicas en un intervalo inferior a 2 segundos contados desde el instante en que se confirma la condición de riesgo sonoro",
            ),
            (
                "Activación local del extractor durante indisponibilidad de conectividad hacia la nube",
                "Dado que el IoT Gateway mantiene conectividad local con los dispositivos ESP32 de una zona crítica<br/>Y la conexión a internet de la planta se encuentra interrumpida<br/>Y una zona crítica presenta una concentración de CO₂ superior al límite permitido con medición válida recibida localmente",
                "Cuando el IoT Gateway procesa la condición de riesgo con las reglas configuradas en el entorno local",
                "el sistema activa el extractor de aire de la zona en un intervalo inferior a 2 segundos contados desde la medición válida, sin depender de la disponibilidad de la plataforma en la nube",
            ),
            (
                "Medición inválida sin activación de actuadores",
                "Dado que el dispositivo ESP32 de una zona crítica envía una medición de CO₂ fuera del rango operativo del sensor MQ-135",
                "Cuando el IoT Gateway recibe y descarta la medición como inválida",
                "el sistema no activa extractores, sirenas ni mamparas acústicas por esa medición<br/>Y el sistema registra el evento como medición inválida de CO₂ con la zona y el instante correspondiente",
            ),
            (
                "Fallo del actuador con registro de incumplimiento del tiempo de respuesta útil",
                "Dado que una zona crítica presenta una condición de riesgo confirmada que requiere activación del extractor de aire<br/>Y el relé de control no confirma la activación del extractor dentro del intervalo operativo esperado",
                "Cuando transcurren 2 segundos desde la confirmación de la condición de riesgo sin respuesta operativa del actuador",
                "el sistema registra el fallo del actuador con la zona, el actuador afectado y el instante del evento<br/>Y el sistema mantiene la alerta de riesgo activa en la plataforma de supervisión disponible",
            ),
        ],
    ),
    S(
        "HU39",
        "EP06",
        "Persistencia local y resincronización de telemetría en contingencia offline",
        "Como supervisor de seguridad quiero que el IoT Gateway conserve mediciones y eventos del sistema durante una interrupción de conectividad a internet para mantener trazabilidad operativa y continuidad del monitoreo en la planta.",
        [
            (
                "Almacenamiento local de mediciones ambientales durante caída de internet",
                "Dado que el IoT Gateway recibe mediciones válidas de CO₂, ruido y presencia desde dispositivos ESP32 de una zona crítica<br/>Y la conexión a internet de la planta se interrumpe",
                "Cuando el IoT Gateway procesa las mediciones recibidas sin poder enviarlas a la API en la nube",
                "el sistema persiste cada medición en la base de datos local SQLite con identificador de zona, tipo de medición, valor, origen del dispositivo y marca temporal",
            ),
            (
                "Registro local de eventos de alerta durante contingencia offline",
                "Dado que el IoT Gateway detecta una condición ambiental fuera de los límites permitidos en una zona crítica<br/>Y la conexión a internet de la planta se encuentra interrumpida",
                "Cuando el sistema genera una alerta ambiental o de seguridad asociada a la zona",
                "el sistema registra el evento de alerta en SQLite con la zona, el tipo de alerta, la medición asociada y la marca temporal<br/>Y el sistema mantiene el estado de alerta disponible para consulta local mientras persista la contingencia",
            ),
            (
                "Registro local de acciones automáticas de actuadores durante contingencia offline",
                "Dado que el IoT Gateway ordena la activación o desactivación de un extractor, sirena o mampara acústica en una zona crítica<br/>Y la conexión a internet de la planta se encuentra interrumpida",
                "Cuando la acción automática se ejecuta o falla en el entorno local",
                "el sistema registra la acción en SQLite con el actuador, la operación realizada, la zona, el resultado y la marca temporal",
            ),
            (
                "Resincronización ordenada de mediciones al restablecer conectividad",
                "Dado que existen mediciones almacenadas en SQLite sin sincronizar con la plataforma en la nube<br/>Y la conexión a internet de la planta se restablece",
                "Cuando el IoT Gateway inicia el proceso de resincronización hacia la API en la nube",
                "el sistema envía las mediciones pendientes en orden cronológico<br/>Y el sistema marca cada registro local como sincronizado al recibir confirmación de persistencia en la nube",
            ),
            (
                "Resincronización de alertas y acciones automáticas pendientes",
                "Dado que existen eventos de alerta y registros de acciones automáticas almacenados en SQLite sin sincronizar<br/>Y la conexión a internet de la planta se restablece",
                "Cuando el IoT Gateway ejecuta la resincronización de eventos operativos hacia la API en la nube",
                "el sistema transmite los eventos pendientes preservando la secuencia temporal original<br/>Y el sistema conserva en la nube la trazabilidad completa de alertas y acciones ocurridas durante la contingencia offline",
            ),
            (
                "Saturación de almacenamiento local por contingencia prolongada",
                "Dado que la conexión a internet de la planta permanece interrumpida durante un periodo prolongado<br/>Y el volumen de mediciones y eventos generados supera la capacidad de retención configurada en SQLite",
                "Cuando el IoT Gateway alcanza el límite de almacenamiento local disponible",
                "el sistema conserva prioritariamente los registros de alertas, acciones automáticas y mediciones recientes<br/>Y el sistema registra un evento de contingencia de almacenamiento local con la fecha y el nivel de saturación alcanzado",
            ),
            (
                "Rechazo de resincronización por telemetría corrupta o incompleta",
                "Dado que un registro almacenado en SQLite presenta datos incompletos o inconsistentes para su envío a la nube<br/>Y la conexión a internet de la planta se encuentra disponible",
                "Cuando el IoT Gateway intenta resincronizar el registro hacia la API en la nube",
                "el sistema no elimina el registro local sin confirmación válida de persistencia remota<br/>Y el sistema registra el intento fallido de resincronización con el identificador del registro y el motivo detectado",
            ),
        ],
    ),
    S(
        "HU40",
        "EP06",
        "Protección de telemetría y sesiones de supervisión",
        "Como administrador de TI quiero que la telemetría transmitida hacia la nube y las sesiones de los supervisores estén protegidas contra acceso no autorizado para preservar la confidencialidad e integridad de la información operativa del sistema.",
        [
            (
                "Transmisión cifrada de telemetría desde el Gateway hacia la API",
                "Dado que el IoT Gateway dispone de credenciales válidas para comunicarse con la API en la nube<br/>Y existen mediciones y eventos listos para transmisión remota",
                "Cuando el IoT Gateway envía telemetría hacia el endpoint de ingesta de la plataforma",
                "la comunicación se establece mediante un canal cifrado TLS<br/>Y la telemetría viaja sin exposición en texto plano sobre la red externa de la planta",
            ),
            (
                "Rechazo de telemetría enviada por canal no cifrado",
                "Dado que un emisor intenta entregar telemetría de una zona crítica hacia la API en la nube",
                "Cuando la solicitud de ingesta no utiliza un canal cifrado TLS",
                "la API en la nube rechaza la recepción de la telemetría<br/>Y el sistema registra el intento rechazado con origen, instante y motivo de seguridad",
            ),
            (
                "Rechazo de telemetría con credencial de Gateway inválida",
                "Dado que un emisor presenta una solicitud de ingesta de telemetría hacia la API en la nube",
                "Cuando la credencial del IoT Gateway es inválida, expirada o no reconocida",
                "la API en la nube rechaza la solicitud de ingesta<br/>Y el sistema no persiste la telemetría recibida en la base de datos relacional de la plataforma",
            ),
            (
                "Expiración de sesión inactiva de supervisor de seguridad",
                "Dado que un supervisor de seguridad mantiene una sesión autenticada en la plataforma de supervisión<br/>Y transcurre el periodo configurado de inactividad sin interacción autorizada del supervisor",
                "Cuando el supervisor intenta acceder a una función protegida de monitoreo o configuración",
                "el sistema finaliza la sesión expirada<br/>Y el sistema exige una nueva autenticación antes de permitir el acceso a funciones protegidas",
            ),
            (
                "Acceso denegado con token de sesión expirado",
                "Dado que un supervisor de seguridad posee un token de sesión expirado",
                "Cuando el supervisor solicita acceso a información de telemetría o configuración de zonas críticas",
                "el sistema deniega el acceso a la funcionalidad solicitada<br/>Y el sistema informa que la sesión no se encuentra vigente",
            ),
            (
                "Protección de credenciales de dispositivos embebidos en tránsito local",
                "Dado que un dispositivo ESP32 envía mediciones al IoT Gateway mediante solicitudes de red locales",
                "Cuando la solicitud incluye un token de autenticación de dispositivo configurado para el entorno industrial",
                "el IoT Gateway acepta la telemetría únicamente si el token corresponde a un dispositivo registrado y vigente<br/>Y el sistema rechaza solicitudes de dispositivos no autorizados sin incorporar sus mediciones al flujo operativo",
            ),
        ],
    ),
    S(
        "HU41",
        "EP06",
        "Disponibilidad operativa de la plataforma de supervisión",
        "Como supervisor de seguridad quiero que la plataforma de supervisión mantenga una disponibilidad operativa definida para acceder de forma continua al monitoreo de CO₂, ruido, presencia y alertas activas en la planta industrial.",
        [
            (
                "Acceso al dashboard durante operación nominal de la plataforma",
                "Dado que la plataforma de supervisión se encuentra en operación nominal<br/>Y un supervisor de seguridad dispone de credenciales válidas",
                "Cuando el supervisor accede al dashboard consolidado de la planta",
                "el sistema presenta el estado de zonas críticas, alertas activas y telemetría reciente sin interrupción del servicio de supervisión",
            ),
            (
                "Indisponibilidad no planificada del servicio de supervisión",
                "Dado que la plataforma de supervisión experimenta una falla que impide el acceso al dashboard",
                "Cuando un supervisor de seguridad intenta acceder al monitoreo de la planta",
                "el sistema informa indisponibilidad temporal del servicio de supervisión<br/>Y el IoT Gateway continúa el monitoreo local, la persistencia en SQLite y la respuesta automática de actuadores configurada en el entorno industrial",
            ),
            (
                "Cumplimiento del objetivo mensual de disponibilidad",
                "Dado que la plataforma de supervisión opera durante un periodo mensual de evaluación<br/>Y el objetivo de disponibilidad operativa del servicio se encuentra definido en 99.9 por ciento",
                "Cuando el periodo mensual concluye",
                "el sistema mantiene la plataforma de supervisión disponible al menos en el porcentaje objetivo definido, excluyendo ventanas de mantenimiento planificado previamente registradas",
            ),
            (
                "Mantenimiento planificado con continuidad local del monitoreo industrial",
                "Dado que la plataforma de supervisión entra en una ventana de mantenimiento planificado previamente registrada",
                "Cuando los dispositivos ESP32 continúan enviando telemetría al IoT Gateway durante la ventana de mantenimiento",
                "el monitoreo local, la generación de alertas y la activación automática de actuadores continúan operando en la planta<br/>Y el sistema registra las mediciones y eventos para su posterior consulta cuando la plataforma de supervisión retome operación",
            ),
        ],
    ),
    S(
        "HU42",
        "EP06",
        "Compatibilidad multiplataforma de la experiencia de supervisión",
        "Como supervisor de seguridad quiero acceder a la plataforma de supervisión desde navegadores web modernos y dispositivos móviles actuales para consultar telemetría y alertas desde distintos entornos operativos de la planta.",
        [
            (
                "Consulta de telemetría desde navegador de escritorio compatible",
                "Dado que un supervisor de seguridad accede a la plataforma desde un navegador web moderno soportado en estación de trabajo",
                "Cuando el supervisor consulta el dashboard consolidado y el detalle de una zona crítica",
                "el sistema presenta valores de CO₂ en ppm, ruido en dB, presencia y alertas activas de forma legible y operable en el navegador utilizado",
            ),
            (
                "Consulta de alertas activas desde navegador móvil compatible",
                "Dado que un supervisor de seguridad accede a la plataforma desde un navegador móvil soportado en dispositivo Android o iOS",
                "Cuando el supervisor consulta las alertas activas de la planta",
                "el sistema presenta la lista de alertas con zona, tipo, medición asociada y fecha de detección sin pérdida de información esencial para la atención operativa",
            ),
            (
                "Acceso desde navegador no soportado",
                "Dado que un supervisor de seguridad intenta acceder a la plataforma desde un navegador no incluido en la matriz de compatibilidad soportada",
                "Cuando el supervisor solicita acceso al dashboard de supervisión",
                "el sistema informa que el navegador utilizado no se encuentra soportado<br/>Y el sistema indica los navegadores compatibles para acceder a la plataforma de supervisión",
            ),
            (
                "Consulta de mapa de riesgos en dispositivo móvil compatible",
                "Dado que un supervisor de seguridad accede a la plataforma desde un dispositivo móvil soportado",
                "Cuando el supervisor consulta el mapa digitalizado de riesgos por zona",
                "el sistema presenta el estado de riesgo de cada zona crítica configurada en el mapa de la planta de forma comprensible en el dispositivo utilizado",
            ),
            (
                "Continuidad funcional de monitoreo entre estación de trabajo y dispositivo móvil",
                "Dado que un supervisor de seguridad mantiene una sesión autenticada válida en la plataforma",
                "Cuando el supervisor alterna el acceso entre una estación de trabajo y un dispositivo móvil soportado durante la misma jornada operativa",
                "el sistema presenta información coherente de telemetría, alertas activas y estado de zonas críticas en ambos entornos de acceso autorizados",
            ),
        ],
    ),
]
