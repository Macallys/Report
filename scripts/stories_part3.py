# HU24-HU37 for SafePlant Chapter 3.1

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


STORIES_PART3 = [
    # E4 — evaluación de exposición por presencia (sensores PIR + CO₂/ruido)
    S("HU24", "E4", "Cruce de presencia de personal con niveles de CO₂",
      "Como supervisor de seguridad quiero que el sistema evalúe simultáneamente la presencia de personal y los niveles de CO₂ en una zona crítica para determinar si existen operarios expuestos a concentraciones peligrosas del gas.",
      [("Exposición de personal a CO₂ excesivo", "Dado que el sistema detecta personal presente en una zona crítica<br/>Y la concentración de CO₂ en la zona supera el límite permitido", "Cuando el sistema evalúa las condiciones de la zona", "el sistema identifica una condición de exposición a CO₂ y genera una alerta de seguridad para la zona"),
       ("CO₂ excesivo sin personal presente", "Dado que el sistema detecta ausencia de personal en una zona crítica<br/>Y la concentración de CO₂ en la zona supera el límite permitido", "Cuando el sistema evalúa las condiciones de la zona", "el sistema identifica una condición de CO₂ excesivo sin exposición de personal y activa el extractor de aire sin activar la sirena preventiva"),
       ("Personal presente con CO₂ dentro del límite", "Dado que el sistema detecta personal presente en una zona crítica<br/>Y la concentración de CO₂ se encuentra dentro del límite permitido", "Cuando el sistema evalúa las condiciones de la zona", "el sistema mantiene la zona en estado de exposición segura para el personal presente")]),
    # E5
    S("HU25", "E5", "Detección de exceso de CO₂",
      "Como sistema de monitoreo industrial quiero detectar cuando la concentración de CO₂ supera el límite permitido en una zona crítica para activar oportunamente las medidas automáticas de purificación y prevención.",
      [("CO₂ dentro del límite permitido", "Dado que el sistema monitorea una zona crítica con un límite de CO₂ configurado", "Cuando el sensor MQ-135 registra una concentración igual o inferior al límite permitido", "el sistema mantiene la zona en estado ambiental permitido"),
       ("CO₂ por encima del límite permitido", "Dado que el sistema monitorea una zona crítica con un límite de CO₂ configurado", "Cuando el sensor MQ-135 registra una concentración superior al límite permitido", "el sistema identifica una condición de CO₂ excesivo y genera una alerta ambiental"),
       ("Medición de CO₂ inválida descartada", "Dado que el sistema recibe una medición de CO₂ desde el dispositivo embebido", "Cuando la medición se encuentra fuera del rango válido del sensor MQ-135", "el sistema descarta la medición y registra el evento como medición inválida de CO₂")]),
    S("HU26", "E5", "Detección de ruido excesivo",
      "Como sistema de monitoreo industrial quiero detectar cuando el nivel sonoro supera el límite permitido en una zona crítica para prevenir la exposición de los operarios a niveles de ruido peligrosos.",
      [("Ruido dentro del límite permitido", "Dado que el sistema monitorea una zona crítica con un límite sonoro configurado", "Cuando el decibelímetro registra un nivel igual o inferior al límite permitido", "el sistema mantiene la zona en estado sonoro permitido"),
       ("Ruido excesivo sin personal presente", "Dado que el sistema detecta un nivel sonoro superior al límite permitido<br/>Y el sistema registra ausencia de personal en la zona", "Cuando el sistema evalúa la condición ambiental", "el sistema registra la exposición sonora sin activar la sirena preventiva dirigida a operarios"),
       ("Ruido excesivo con personal presente", "Dado que el sistema detecta un nivel sonoro superior al límite permitido<br/>Y el sistema detecta personal presente en la zona", "Cuando el sistema evalúa la condición ambiental", "el sistema genera una alerta de exposición sonora y activa la sirena preventiva")]),
    S("HU27", "E5", "Activación automática del extractor de aire por CO₂",
      "Como sistema de monitoreo industrial quiero activar automáticamente el extractor de aire mediante el relé de control cuando se detecte un exceso de CO₂ para reducir la concentración del gas y recuperar condiciones ambientales seguras.",
      [("Activación del extractor por exceso de CO₂", "Dado que una zona crítica presenta una concentración de CO₂ superior al límite permitido", "Cuando el sistema confirma la condición de exceso de CO₂", "el sistema activa el extractor de aire asociado a la zona mediante el relé de control"),
       ("Desactivación del extractor al normalizar CO₂", "Dado que el extractor de aire se encuentra activo por una condición de CO₂ excesivo", "Cuando la concentración de CO₂ retorna al rango permitido", "el sistema desactiva el extractor de aire de la zona"),
       ("Fallo en la activación del extractor", "Dado que el sistema determina que debe activar el extractor de aire", "Cuando el relé de control no confirma la activación del extractor", "el sistema registra el fallo y genera una alerta de actuador no disponible"),
       ("Pérdida de comunicación con el dispositivo embebido durante activación", "Dado que el sistema envía la orden de activación al extractor de aire", "Cuando el dispositivo embebido ESP32 no responde dentro del tiempo esperado", "el sistema registra el fallo de comunicación y mantiene la alerta de CO₂ excesivo activa en la zona")]),
    S("HU28", "E5", "Activación de sirena preventiva por exposición a condición peligrosa",
      "Como sistema de seguridad quiero activar la sirena preventiva cuando un operario se encuentre expuesto a una condición peligrosa de CO₂ o ruido excesivo para advertir inmediatamente sobre el riesgo existente y permitir la evacuación de la zona.",
      [("Sirena activada por CO₂ peligroso con personal presente", "Dado que el sistema detecta una concentración peligrosa de CO₂ en una zona crítica<br/>Y el sistema detecta personal presente en la zona", "Cuando el sistema determina que existe exposición de operarios", "el sistema activa la sirena preventiva de la zona"),
       ("Sirena activada por ruido peligroso con personal presente", "Dado que el sistema detecta un nivel de ruido superior al límite permitido<br/>Y el sistema detecta personal presente en la zona", "Cuando el sistema determina que existe exposición de operarios", "el sistema activa la sirena preventiva de la zona"),
       ("Sirena inactiva en condiciones seguras con personal presente", "Dado que el sistema detecta personal presente en una zona crítica", "Cuando las concentraciones de CO₂ y los niveles de ruido se encuentran dentro de los límites permitidos", "el sistema mantiene la sirena preventiva desactivada"),
       ("Desactivación de sirena al cesar condición de riesgo", "Dado que la sirena preventiva se encuentra activa por una condición de exposición", "Cuando la condición peligrosa desaparece y no existe otra condición de alarma activa en la zona", "el sistema desactiva la sirena preventiva de la zona")]),
    S("HU29", "E5", "Despliegue de mamparas acústicas por exposición sonora",
      "Como sistema de monitoreo industrial quiero desplegar mamparas móviles de aislamiento acústico mediante servomotores cuando se detecte ruido excesivo con personal presente para reducir la exposición sonora de los operarios en la zona afectada.",
      [("Despliegue de mamparas por ruido excesivo con personal", "Dado que una zona crítica presenta un nivel de ruido superior al límite permitido<br/>Y el sistema detecta personal presente en la zona", "Cuando el sistema confirma la condición de exposición sonora", "el sistema activa los servomotores y despliega las mamparas acústicas de la zona"),
       ("Retracción de mamparas al normalizar el ruido", "Dado que las mamparas acústicas se encuentran desplegadas por una condición de ruido excesivo", "Cuando el nivel sonoro retorna al rango permitido", "el sistema retrae las mamparas acústicas de la zona"),
       ("Fallo en el despliegue de mamparas acústicas", "Dado que el sistema determina que debe desplegar las mamparas acústicas", "Cuando el servomotor no confirma el despliegue dentro del tiempo esperado", "el sistema registra el fallo y genera una alerta de actuador no disponible")]),
    S("HU30", "E5", "Anulación manual de actuador en emergencia",
      "Como supervisor de seguridad quiero anular manualmente el estado de un actuador durante una emergencia para asumir el control directo de extractores, sirenas o mamparas cuando la respuesta automática no sea adecuada para la situación.",
      [("Anulación manual de extractor en emergencia", "Dado que el extractor de aire de una zona se encuentra activo automáticamente", "Cuando el supervisor de seguridad solicita la anulación manual y activación forzada del extractor", "el sistema aplica el estado solicitado al extractor y registra la anulación manual con el identificador del supervisor y la fecha del evento"),
       ("Anulación manual de sirena en emergencia", "Dado que la sirena preventiva de una zona se encuentra activa automáticamente", "Cuando el supervisor de seguridad solicita la desactivación manual de la sirena", "el sistema desactiva la sirena y registra la anulación manual con el identificador del supervisor y la fecha del evento"),
       ("Anulación manual por supervisor no autorizado", "Dado que un operario de planta mantiene una sesión activa en la plataforma", "Cuando el operario solicita la anulación manual de un actuador", "el sistema rechaza la operación e informa que la anulación manual requiere el rol de supervisor de seguridad")]),
    S("HU31", "E5", "Registro de acciones automáticas ejecutadas",
      "Como supervisor de seguridad quiero consultar las acciones automáticas ejecutadas por el sistema para verificar que los mecanismos de prevención respondieron ante las condiciones peligrosas detectadas.",
      [("Registro de activación automática de actuador", "Dado que el sistema activa un extractor, una sirena o una mampara acústica", "Cuando la acción automática se ejecuta en la zona", "el sistema registra el actuador, la acción realizada, la zona y el momento de ejecución"),
       ("Registro de desactivación automática de actuador", "Dado que un actuador se encuentra activo por una condición ambiental", "Cuando el sistema determina que la condición que originó la acción ha finalizado", "el sistema registra la desactivación del actuador con la zona y el momento del evento"),
       ("Registro de acción automática fallida", "Dado que el sistema envía una orden automática a un actuador", "Cuando el actuador no confirma la ejecución", "el sistema registra la acción como fallida con el actuador, la zona y el motivo del fallo")]),
    S("HU32", "E5", "Notificación física de alarma al operario expuesto",
      "Como operario de planta quiero recibir una alarma física audible cuando me encuentre expuesto a una condición peligrosa de CO₂ o ruido excesivo para conocer la situación de riesgo y retirarme de la zona afectada.",
      [("Alarma audible por exposición a CO₂ peligroso", "Dado que el operario se encuentra en una zona crítica con condición peligrosa de CO₂", "Cuando el sistema activa la sirena preventiva de la zona", "el operario recibe la señal audible de alarma en el entorno físico de la zona"),
       ("Alarma audible por exposición a ruido excesivo", "Dado que el operario se encuentra en una zona crítica con nivel de ruido superior al límite permitido", "Cuando el sistema activa la sirena preventiva de la zona", "el operario recibe la señal audible de alarma en el entorno físico de la zona"),
       ("Ausencia de alarma en condiciones seguras", "Dado que el operario se encuentra en una zona crítica", "Cuando las condiciones de CO₂ y ruido se encuentran dentro de los límites permitidos", "el sistema mantiene la sirena preventiva desactivada en la zona"),
       ("Fallo de sirena con operario expuesto", "Dado que el operario se encuentra en una zona con condición de riesgo activa", "Cuando el buzzer de la sirena no responde a la orden de activación", "el sistema registra el fallo del actuador y mantiene la alerta de exposición activa en la plataforma de supervisión")]),
]

assert len(STORIES_PART3) == 9  # HU24-32

