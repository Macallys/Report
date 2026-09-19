# HU07-HU37 for SafePlant Chapter 3.1

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


STORIES_PART2 = [
    # E2 HU07-13
    S("HU07", "EP02", "Inicio de sesión de supervisor de seguridad",
      "Como supervisor de seguridad quiero iniciar sesión en la plataforma de supervisión para acceder a las funciones de monitoreo, configuración y consulta del sistema.",
      [("Autenticación exitosa de supervisor", "Dado que el supervisor de seguridad dispone de credenciales válidas registradas en el sistema", "Cuando el supervisor proporciona sus credenciales de acceso", "el sistema concede el acceso a la plataforma de supervisión con el rol de supervisor de seguridad"),
       ("Credenciales no reconocidas de supervisor", "Dado que el supervisor de seguridad intenta acceder a la plataforma", "Cuando el supervisor proporciona credenciales no reconocidas por el sistema", "el sistema deniega el acceso e informa que las credenciales no son válidas"),
       ("Cuenta de supervisor deshabilitada", "Dado que el supervisor de seguridad posee una cuenta deshabilitada en el sistema", "Cuando el supervisor proporciona credenciales asociadas a la cuenta deshabilitada", "el sistema deniega el acceso e informa que la cuenta se encuentra deshabilitada")]),
    S("HU08", "EP02", "Inicio de sesión de administrador de planta",
      "Como administrador de planta quiero iniciar sesión en la plataforma de supervisión para acceder a las funciones de administración de usuarios, zonas y configuración general del sistema.",
      [("Autenticación exitosa de administrador", "Dado que el administrador de planta dispone de credenciales válidas registradas en el sistema", "Cuando el administrador proporciona sus credenciales de acceso", "el sistema concede el acceso a la plataforma con el rol de administrador de planta"),
       ("Credenciales no reconocidas de administrador", "Dado que el administrador de planta intenta acceder a la plataforma", "Cuando el administrador proporciona credenciales no reconocidas por el sistema", "el sistema deniega el acceso e informa que las credenciales no son válidas")]),
    S("HU09", "EP02", "Inicio de sesión de operario de planta",
      "Como operario de planta quiero iniciar sesión en la plataforma para consultar información de seguridad y acceso relacionada con las zonas críticas de la planta.",
      [("Autenticación exitosa de operario", "Dado que el operario de planta dispone de credenciales válidas registradas en el sistema", "Cuando el operario proporciona sus credenciales de acceso", "el sistema concede el acceso a la plataforma con el rol de operario de planta"),
       ("Restricción de funciones administrativas para operario", "Dado que el operario de planta mantiene una sesión activa en la plataforma", "Cuando el operario intenta acceder a funciones de administración del sistema", "el sistema deniega el acceso e informa que la operación no está autorizada para el rol de operario")]),
    S("HU10", "EP02", "Cierre de sesión de usuario autenticado",
      "Como usuario autenticado del sistema quiero finalizar mi sesión activa en la plataforma para proteger el acceso a las funciones del sistema ante el uso no autorizado de mi cuenta.",
      [("Cierre de sesión exitoso", "Dado que un usuario autenticado mantiene una sesión activa en la plataforma", "Cuando el usuario solicita finalizar su sesión", "el sistema cierra la sesión activa y restringe el acceso a las funciones protegidas"),
       ("Intento de acceso posterior al cierre de sesión", "Dado que un usuario ha finalizado su sesión en la plataforma", "Cuando el usuario intenta acceder a una función protegida sin autenticarse nuevamente", "el sistema deniega el acceso e informa que se requiere autenticación")]),
    S("HU11", "EP02", "Creación de cuenta de usuario por administrador",
      "Como administrador de planta quiero crear cuentas de usuario para supervisores y operarios para habilitar el acceso controlado a la plataforma de supervisión.",
      [("Creación de cuenta de supervisor", "Dado que el administrador de planta accede a la administración de usuarios", "Cuando el administrador registra una nueva cuenta con nombre, correo electrónico y rol de supervisor de seguridad", "el sistema crea la cuenta y habilita el acceso del usuario con el rol asignado"),
       ("Creación de cuenta de operario", "Dado que el administrador de planta accede a la administración de usuarios", "Cuando el administrador registra una nueva cuenta con nombre, correo electrónico y rol de operario de planta", "el sistema crea la cuenta y habilita el acceso del usuario con el rol asignado"),
       ("Creación de cuenta con correo duplicado", "Dado que el administrador intenta registrar una nueva cuenta de usuario", "Cuando el correo electrónico proporcionado ya se encuentra registrado en el sistema", "el sistema rechaza la creación e informa que el correo electrónico ya está en uso")]),
    S("HU12", "EP02", "Asignación de roles y permisos de usuario",
      "Como administrador de planta quiero asignar y modificar roles y permisos de los usuarios del sistema para controlar el acceso a las funciones de supervisión, configuración y administración.",
      [("Asignación de rol a usuario existente", "Dado que existe una cuenta de usuario registrada en el sistema", "Cuando el administrador asigna un rol válido a la cuenta del usuario", "el sistema actualiza el rol del usuario y aplica los permisos correspondientes"),
       ("Asignación de rol no reconocido", "Dado que el administrador intenta asignar un rol a un usuario", "Cuando el rol proporcionado no se encuentra definido en el sistema", "el sistema rechaza la asignación e informa que el rol no es válido")]),
    S("HU13", "EP02", "Recuperación de credenciales de acceso",
      "Como usuario registrado del sistema quiero recuperar el acceso a mi cuenta cuando olvide mis credenciales para restablecer mi acceso a la plataforma de supervisión.",
      [("Solicitud de recuperación con correo registrado", "Dado que un usuario registrado ha olvidado sus credenciales de acceso", "Cuando el usuario solicita la recuperación de acceso con un correo electrónico registrado en el sistema", "el sistema genera un proceso de recuperación y envía las instrucciones al correo electrónico asociado"),
       ("Solicitud de recuperación con correo no registrado", "Dado que una persona solicita la recuperación de acceso", "Cuando el correo electrónico proporcionado no se encuentra registrado en el sistema", "el sistema informa que no existe una cuenta asociada al correo electrónico proporcionado"),
       ("Restablecimiento con proceso de recuperación expirado", "Dado que un usuario intenta restablecer sus credenciales", "Cuando el proceso de recuperación ha superado el tiempo de validez configurado", "el sistema rechaza el restablecimiento e informa que el proceso de recuperación ha expirado")]),
    # E3 HU14-23
    S("HU14", "EP03", "Dashboard consolidado de la planta",
      "Como supervisor de seguridad quiero visualizar el estado consolidado de todas las zonas críticas de la planta para obtener una visión general del estado ambiental y de seguridad en tiempo real.",
      [("Vista general de zonas críticas", "Dado que el supervisor de seguridad accede a la plataforma autenticado", "Cuando el sistema carga el estado de las zonas críticas registradas", "la plataforma presenta el resumen de CO₂ en ppm, ruido en dB, presencia y estado de alerta de cada zona"),
       ("Identificación de zonas en condición de riesgo", "Dado que una o más zonas críticas presentan condiciones fuera de los límites permitidos", "Cuando el supervisor consulta el dashboard consolidado", "el sistema identifica las zonas que requieren atención inmediata"),
       ("Planta sin zonas críticas registradas", "Dado que el sistema no posee zonas críticas registradas", "Cuando el supervisor consulta el dashboard consolidado", "el sistema informa que no existen zonas críticas configuradas para monitoreo")]),
    S("HU15", "EP03", "Monitoreo de CO₂ en tiempo real por zona",
      "Como supervisor de seguridad quiero monitorear en tiempo real la concentración de CO₂ en ppm de una zona crítica para identificar oportunamente acumulaciones peligrosas del gas en el ambiente industrial.",
      [("Consulta de concentración de CO₂ actual", "Dado que el supervisor consulta una zona crítica con sensor de CO₂ activo", "Cuando el sensor MQ-135 registra una concentración de CO₂ en ppm", "el sistema registra y presenta el valor actual de CO₂ de la zona"),
       ("Actualización de medición de CO₂", "Dado que el supervisor monitorea una zona crítica<br/>Y el sensor de CO₂ genera una nueva medición", "Cuando el sistema recibe la nueva medición a través del IoT Gateway", "el sistema actualiza el valor de CO₂ correspondiente a la zona monitoreada"),
       ("Sensor de CO₂ sin transmisión de datos", "Dado que el supervisor monitorea una zona crítica", "Cuando el sensor de CO₂ deja de enviar mediciones dentro del intervalo esperado", "el sistema identifica el sensor como no disponible y conserva la última medición válida registrada"),
       ("Medición de CO₂ fuera del rango válido del sensor", "Dado que el sistema recibe una medición de CO₂ desde el dispositivo embebido", "Cuando el valor de la medición se encuentra fuera del rango operativo del sensor MQ-135", "el sistema descarta la medición y registra el evento como medición inválida de CO₂")]),
    S("HU16", "EP03", "Monitoreo de ruido en tiempo real por zona",
      "Como supervisor de seguridad quiero monitorear en tiempo real el nivel de ruido en dB de una zona crítica para identificar oportunamente condiciones de exposición sonora peligrosa para los operarios.",
      [("Consulta de nivel de ruido actual", "Dado que el supervisor consulta una zona crítica con sensor de ruido activo", "Cuando el decibelímetro registra un nivel sonoro en dB", "el sistema registra y presenta el valor actual de ruido de la zona"),
       ("Actualización de medición de ruido", "Dado que el supervisor monitorea una zona crítica<br/>Y el sensor de ruido genera una nueva medición", "Cuando el sistema recibe la nueva medición a través del IoT Gateway", "el sistema actualiza el valor de ruido correspondiente a la zona monitoreada"),
       ("Sensor de ruido sin transmisión de datos", "Dado que el supervisor monitorea una zona crítica", "Cuando el decibelímetro deja de enviar mediciones dentro del intervalo esperado", "el sistema identifica el sensor como no disponible y conserva la última medición válida registrada")]),
    S("HU17", "EP03", "Monitoreo de presencia de personal por zona",
      "Como supervisor de seguridad quiero monitorear la presencia de personal en una zona crítica para determinar si existen operarios expuestos a condiciones ambientales de riesgo.",
      [("Detección de presencia por sensor PIR", "Dado que el supervisor monitorea una zona crítica con sensor PIR activo", "Cuando el sensor PIR detecta movimiento en la zona", "el sistema registra la presencia de personal en la zona"),
       ("Ausencia de personal en zona monitoreada", "Dado que el supervisor monitorea una zona crítica", "Cuando el sensor PIR no detecta actividad en el intervalo configurado", "el sistema registra la zona como sin personal presente"),
       ("Sensor PIR sin transmisión de datos", "Dado que el supervisor monitorea una zona crítica", "Cuando el sensor PIR deja de enviar señales dentro del intervalo esperado", "el sistema identifica el sensor como no disponible y conserva el último estado de presencia registrado")]),
    S("HU18", "EP03", "Visualización de alertas activas",
      "Como supervisor de seguridad quiero visualizar las alertas ambientales y de seguridad activas en la planta para atender oportunamente las condiciones de riesgo detectadas por el sistema.",
      [("Listado de alertas activas en la planta", "Dado que el sistema ha detectado una o más condiciones de riesgo sin resolver", "Cuando el supervisor consulta las alertas activas", "el sistema presenta la zona, el tipo de alerta, la medición asociada y la fecha de detección de cada alerta activa"),
       ("Retiro de alerta por normalización de condición", "Dado que el supervisor visualiza las alertas activas", "Cuando una condición de riesgo finaliza en una zona monitoreada", "el sistema retira la alerta correspondiente del listado de alertas activas"),
       ("Ausencia de alertas activas en la planta", "Dado que no existen condiciones de riesgo activas en ninguna zona", "Cuando el supervisor consulta las alertas activas", "el sistema informa que no existen alertas activas en ese momento")]),
    S("HU19", "EP03", "Mapa digitalizado de riesgos por zona",
      "Como supervisor de seguridad quiero visualizar un mapa digitalizado de la planta con el estado de riesgo de cada zona crítica para identificar geográficamente las áreas que requieren atención inmediata.",
      [("Mapa con zonas en estado seguro", "Dado que todas las zonas críticas registradas se encuentran dentro de los límites permitidos", "Cuando el supervisor consulta el mapa digitalizado de riesgos", "el sistema presenta todas las zonas con su estado ambiental seguro en el mapa de la planta"),
       ("Mapa con zonas en condición de riesgo", "Dado que una o más zonas críticas presentan condiciones fuera de los límites permitidos", "Cuando el supervisor consulta el mapa digitalizado de riesgos", "el sistema identifica en el mapa las zonas que presentan condición de riesgo activa"),
       ("Zona sin posición definida en el mapa", "Dado que existe una zona crítica registrada sin posición definida en el mapa", "Cuando el supervisor consulta el mapa digitalizado de riesgos", "el sistema presenta la zona en el listado de zonas sin ubicación e informa que la posición de la zona no se encuentra configurada en el mapa")]),
    S("HU20", "EP03", "Gestión de zonas críticas",
      "Como supervisor de seguridad quiero registrar y administrar las zonas críticas de la planta para asociar dispositivos IoT, umbrales ambientales y reglas de acceso a cada área monitoreada.",
      [("Registro de zona crítica", "Dado que el supervisor accede a la administración de zonas críticas", "Cuando el supervisor registra una nueva zona con nombre, descripción y ubicación en el mapa", "el sistema almacena la zona y la habilita para la asignación de dispositivos y configuraciones"),
       ("Modificación de zona crítica existente", "Dado que existe una zona crítica registrada en el sistema", "Cuando el supervisor modifica los datos de la zona", "el sistema actualiza la información de la zona conservando su historial de eventos asociado"),
       ("Registro de zona con nombre duplicado", "Dado que el supervisor intenta registrar una zona crítica", "Cuando el nombre de la zona ya existe en el sistema", "el sistema rechaza el registro e informa que la zona ya se encuentra registrada")]),
    S("HU21", "EP03", "Configuración de umbrales ambientales por zona",
      "Como supervisor de seguridad quiero configurar los límites permitidos de CO₂ en ppm y ruido en dB para cada zona crítica para determinar cuándo una condición ambiental representa un riesgo para los operarios.",
      [("Configuración de límites ambientales", "Dado que el supervisor dispone de una zona crítica registrada", "Cuando el supervisor configura los límites permitidos de CO₂ en ppm y ruido en dB", "el sistema almacena los límites asociados a la zona"),
       ("Modificación de límite ambiental existente", "Dado que una zona crítica tiene límites ambientales configurados", "Cuando el supervisor modifica uno de los límites", "el sistema reemplaza el valor anterior por el nuevo límite configurado"),
       ("Límite ambiental fuera del rango permitido por el sistema", "Dado que el supervisor configura un límite ambiental", "Cuando el valor ingresado no cumple las restricciones establecidas por el sistema", "el sistema rechaza la configuración e informa que el valor no es válido")]),
    S("HU22", "EP03", "Registro de dispositivos IoT por zona",
      "Como supervisor de seguridad quiero registrar sensores y actuadores en una zona crítica para habilitar el monitoreo ambiental y las respuestas automáticas en esa área de la planta.",
      [("Registro de sensor en zona crítica", "Dado que existe una zona crítica registrada en el sistema", "Cuando el supervisor asocia un sensor con su tipo, identificador y dirección del dispositivo embebido", "el sistema registra el sensor y lo habilita para recibir mediciones"),
       ("Registro de actuador en zona crítica", "Dado que existe una zona crítica registrada en el sistema", "Cuando el supervisor asocia un actuador con su tipo, identificador y dirección del dispositivo embebido", "el sistema registra el actuador y lo habilita para recibir órdenes de control"),
       ("Registro de dispositivo con identificador duplicado", "Dado que el supervisor intenta registrar un dispositivo IoT", "Cuando el identificador del dispositivo ya se encuentra asociado en el sistema", "el sistema rechaza el registro e informa que el dispositivo ya está en uso")]),
    S("HU23", "EP03", "Consulta de historial de mediciones y eventos ambientales",
      "Como supervisor de seguridad quiero consultar el historial de mediciones, alertas y acciones automáticas de una zona crítica para analizar incidentes y verificar el comportamiento del sistema ante condiciones de riesgo.",
      [("Registro automático de evento ambiental", "Dado que el sistema detecta una condición ambiental fuera de los límites permitidos", "Cuando el sistema procesa la condición", "el sistema registra el evento con la zona, el tipo de condición, la medición y la fecha correspondiente"),
       ("Consulta de historial por zona y periodo", "Dado que existen eventos registrados en una zona crítica", "Cuando el supervisor consulta el historial de eventos de la zona para un periodo determinado", "el sistema proporciona los eventos registrados correspondientes al periodo consultado"),
       ("Historial sin registros en el periodo consultado", "Dado que una zona crítica no posee eventos en el periodo consultado", "Cuando el supervisor consulta el historial de la zona", "el sistema informa que no existen eventos registrados para el periodo indicado")]),
]

assert len(STORIES_PART2) == 17  # HU07-23
