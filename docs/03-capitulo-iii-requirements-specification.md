**Navegación:** [Índice](./00-student-outcome.md#s-tabla-contenidos) · Anterior: [Capítulo II](./02-capitulo-ii-requirements-elicitation.md) · Siguiente: [Capítulo IV](./04-capitulo-iv-solution-software-design.md)

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
      <td align="left">Como visitante quiero conocer el producto SafePlant, sus beneficios y al equipo responsable para evaluar la solución de control de seguridad y contaminación industrial.</td>
    </tr>
    <tr>
      <td align="left">E2</td>
      <td align="left">Registro y Autenticación</td>
      <td align="left">Como usuario de la plataforma quiero autenticarme y acceder con un rol definido para utilizar de forma controlada las funciones de supervisión y administración del sistema.</td>
    </tr>
    <tr>
      <td align="left">E3</td>
      <td align="left">Telemetría y Monitoreo en Tiempo Real</td>
      <td align="left">Como supervisor de seguridad quiero monitorear en tiempo real CO₂, ruido y presencia por zonas críticas para detectar oportunamente condiciones de riesgo en la planta industrial.</td>
    </tr>
    <tr>
      <td align="left">E4</td>
      <td align="left">Acceso y Seguridad Física en Zonas Críticas</td>
      <td align="left">Como operario de planta quiero que el sistema controle mi ingreso a zonas críticas mediante credencial RFID para evitar exposición a condiciones ambientales peligrosas.</td>
    </tr>
    <tr>
      <td align="left">E5</td>
      <td align="left">Automatización de Actuadores y Reglas de Negocio</td>
      <td align="left">Como supervisor de seguridad quiero que el sistema active automáticamente extractores, sirenas y mamparas acústicas ante condiciones de riesgo para proteger al personal y reducir la contaminación industrial.</td>
    </tr>
    <tr>
      <td align="left">E6</td>
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
      <td align="left"><strong>Escenario 1: Beneficios en prevención de riesgos</strong><br/>Dado que el visitante accede al sitio web de SafePlant,<br/>Cuando el visitante consulta la sección de beneficios de la solución,<br/>Entonces el sitio presenta los beneficios relacionados con la prevención de riesgos ambientales y de seguridad para operarios.<br/><br/><strong>Escenario 2: Beneficios en monitoreo continuo</strong><br/>Dado que el visitante accede al sitio web de SafePlant,<br/>Cuando el visitante consulta la sección de beneficios de la solución,<br/>Entonces el sitio presenta los beneficios relacionados con el monitoreo ambiental continuo en tiempo real.<br/><br/><strong>Escenario 3: Beneficios en automatización industrial</strong><br/>Dado que el visitante accede al sitio web de SafePlant,<br/>Cuando el visitante consulta la sección de beneficios de la solución,<br/>Entonces el sitio presenta los beneficios relacionados con la automatización de respuestas ante condiciones peligrosas.</td>
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
      <td align="left">Como visitante quiero conocer la arquitectura técnica de SafePlant para comprender cómo se integran los dispositivos embebidos, el IoT Gateway y la plataforma en la nube.</td>
      <td align="left"><strong>Escenario 1: Capa de dispositivos embebidos</strong><br/>Dado que el visitante accede al sitio web de SafePlant,<br/>Cuando el visitante consulta la sección de arquitectura técnica,<br/>Entonces el sitio presenta información sobre los dispositivos ESP32, sensores de CO₂, ruido y presencia, y actuadores físicos del sistema.<br/><br/><strong>Escenario 2: Capa de IoT Gateway</strong><br/>Dado que el visitante accede al sitio web de SafePlant,<br/>Cuando el visitante consulta la sección de arquitectura técnica,<br/>Entonces el sitio presenta información sobre el IoT Gateway basado en Raspberry Pi con procesamiento local y persistencia de contingencia.<br/><br/><strong>Escenario 3: Capa de plataforma en la nube</strong><br/>Dado que el visitante accede al sitio web de SafePlant,<br/>Cuando el visitante consulta la sección de arquitectura técnica,<br/>Entonces el sitio presenta información sobre la API REST, la base de datos relacional y la plataforma de supervisión web.</td>
    </tr>
    <tr>
      <td align="left">HU06</td>
      <td align="left">E1</td>
      <td align="left">Navegación hacia la plataforma de supervisión</td>
      <td align="left">Como visitante quiero acceder a la plataforma de supervisión desde el sitio informativo para ingresar al sistema de monitoreo con una cuenta autorizada.</td>
      <td align="left"><strong>Escenario 1: Redirección hacia el punto de autenticación</strong><br/>Dado que el visitante se encuentra en el sitio web de SafePlant,<br/>Cuando el visitante solicita el acceso a la plataforma de supervisión,<br/>Entonces el sistema redirige al visitante al punto de autenticación de la plataforma.<br/><br/><strong>Escenario 2: Acceso identificable en la navegación principal</strong><br/>Dado que el visitante consulta el sitio web de SafePlant,<br/>Cuando el visitante revisa la navegación principal del sitio,<br/>Entonces el sitio presenta un acceso identificable hacia la plataforma de supervisión.</td>
    </tr>
    <tr>
      <td align="left">HU07</td>
      <td align="left">E2</td>
      <td align="left">Inicio de sesión de supervisor de seguridad</td>
      <td align="left">Como supervisor de seguridad quiero iniciar sesión en la plataforma de supervisión para acceder a las funciones de monitoreo, configuración y consulta del sistema.</td>
      <td align="left"><strong>Escenario 1: Autenticación exitosa de supervisor</strong><br/>Dado que el supervisor de seguridad dispone de credenciales válidas registradas en el sistema,<br/>Cuando el supervisor proporciona sus credenciales de acceso,<br/>Entonces el sistema concede el acceso a la plataforma de supervisión con el rol de supervisor de seguridad.<br/><br/><strong>Escenario 2: Credenciales no reconocidas de supervisor</strong><br/>Dado que el supervisor de seguridad intenta acceder a la plataforma,<br/>Cuando el supervisor proporciona credenciales no reconocidas por el sistema,<br/>Entonces el sistema deniega el acceso e informa que las credenciales no son válidas.<br/><br/><strong>Escenario 3: Cuenta de supervisor deshabilitada</strong><br/>Dado que el supervisor de seguridad posee una cuenta deshabilitada en el sistema,<br/>Cuando el supervisor proporciona credenciales asociadas a la cuenta deshabilitada,<br/>Entonces el sistema deniega el acceso e informa que la cuenta se encuentra deshabilitada.</td>
    </tr>
    <tr>
      <td align="left">HU08</td>
      <td align="left">E2</td>
      <td align="left">Inicio de sesión de administrador de planta</td>
      <td align="left">Como administrador de planta quiero iniciar sesión en la plataforma de supervisión para acceder a las funciones de administración de usuarios, zonas y configuración general del sistema.</td>
      <td align="left"><strong>Escenario 1: Autenticación exitosa de administrador</strong><br/>Dado que el administrador de planta dispone de credenciales válidas registradas en el sistema,<br/>Cuando el administrador proporciona sus credenciales de acceso,<br/>Entonces el sistema concede el acceso a la plataforma con el rol de administrador de planta.<br/><br/><strong>Escenario 2: Credenciales no reconocidas de administrador</strong><br/>Dado que el administrador de planta intenta acceder a la plataforma,<br/>Cuando el administrador proporciona credenciales no reconocidas por el sistema,<br/>Entonces el sistema deniega el acceso e informa que las credenciales no son válidas.</td>
    </tr>
    <tr>
      <td align="left">HU09</td>
      <td align="left">E2</td>
      <td align="left">Inicio de sesión de operario de planta</td>
      <td align="left">Como operario de planta quiero iniciar sesión en la plataforma para consultar información de seguridad y acceso relacionada con las zonas críticas de la planta.</td>
      <td align="left"><strong>Escenario 1: Autenticación exitosa de operario</strong><br/>Dado que el operario de planta dispone de credenciales válidas registradas en el sistema,<br/>Cuando el operario proporciona sus credenciales de acceso,<br/>Entonces el sistema concede el acceso a la plataforma con el rol de operario de planta.<br/><br/><strong>Escenario 2: Restricción de funciones administrativas para operario</strong><br/>Dado que el operario de planta mantiene una sesión activa en la plataforma,<br/>Cuando el operario intenta acceder a funciones de administración del sistema,<br/>Entonces el sistema deniega el acceso e informa que la operación no está autorizada para el rol de operario.</td>
    </tr>
    <tr>
      <td align="left">HU10</td>
      <td align="left">E2</td>
      <td align="left">Cierre de sesión de usuario autenticado</td>
      <td align="left">Como usuario autenticado del sistema quiero finalizar mi sesión activa en la plataforma para proteger el acceso a las funciones del sistema ante el uso no autorizado de mi cuenta.</td>
      <td align="left"><strong>Escenario 1: Cierre de sesión exitoso</strong><br/>Dado que un usuario autenticado mantiene una sesión activa en la plataforma,<br/>Cuando el usuario solicita finalizar su sesión,<br/>Entonces el sistema cierra la sesión activa y restringe el acceso a las funciones protegidas.<br/><br/><strong>Escenario 2: Intento de acceso posterior al cierre de sesión</strong><br/>Dado que un usuario ha finalizado su sesión en la plataforma,<br/>Cuando el usuario intenta acceder a una función protegida sin autenticarse nuevamente,<br/>Entonces el sistema deniega el acceso e informa que se requiere autenticación.</td>
    </tr>
    <tr>
      <td align="left">HU11</td>
      <td align="left">E2</td>
      <td align="left">Creación de cuenta de usuario por administrador</td>
      <td align="left">Como administrador de planta quiero crear cuentas de usuario para supervisores y operarios para habilitar el acceso controlado a la plataforma de supervisión.</td>
      <td align="left"><strong>Escenario 1: Creación de cuenta de supervisor</strong><br/>Dado que el administrador de planta accede a la administración de usuarios,<br/>Cuando el administrador registra una nueva cuenta con nombre, correo electrónico y rol de supervisor de seguridad,<br/>Entonces el sistema crea la cuenta y habilita el acceso del usuario con el rol asignado.<br/><br/><strong>Escenario 2: Creación de cuenta de operario</strong><br/>Dado que el administrador de planta accede a la administración de usuarios,<br/>Cuando el administrador registra una nueva cuenta con nombre, correo electrónico y rol de operario de planta,<br/>Entonces el sistema crea la cuenta y habilita el acceso del usuario con el rol asignado.<br/><br/><strong>Escenario 3: Creación de cuenta con correo duplicado</strong><br/>Dado que el administrador intenta registrar una nueva cuenta de usuario,<br/>Cuando el correo electrónico proporcionado ya se encuentra registrado en el sistema,<br/>Entonces el sistema rechaza la creación e informa que el correo electrónico ya está en uso.</td>
    </tr>
    <tr>
      <td align="left">HU12</td>
      <td align="left">E2</td>
      <td align="left">Asignación de roles y permisos de usuario</td>
      <td align="left">Como administrador de planta quiero asignar y modificar roles y permisos de los usuarios del sistema para controlar el acceso a las funciones de supervisión, configuración y administración.</td>
      <td align="left"><strong>Escenario 1: Asignación de rol a usuario existente</strong><br/>Dado que existe una cuenta de usuario registrada en el sistema,<br/>Cuando el administrador asigna un rol válido a la cuenta del usuario,<br/>Entonces el sistema actualiza el rol del usuario y aplica los permisos correspondientes.<br/><br/><strong>Escenario 2: Asignación de rol no reconocido</strong><br/>Dado que el administrador intenta asignar un rol a un usuario,<br/>Cuando el rol proporcionado no se encuentra definido en el sistema,<br/>Entonces el sistema rechaza la asignación e informa que el rol no es válido.</td>
    </tr>
    <tr>
      <td align="left">HU13</td>
      <td align="left">E2</td>
      <td align="left">Recuperación de credenciales de acceso</td>
      <td align="left">Como usuario registrado del sistema quiero recuperar el acceso a mi cuenta cuando olvide mis credenciales para restablecer mi acceso a la plataforma de supervisión.</td>
      <td align="left"><strong>Escenario 1: Solicitud de recuperación con correo registrado</strong><br/>Dado que un usuario registrado ha olvidado sus credenciales de acceso,<br/>Cuando el usuario solicita la recuperación de acceso con un correo electrónico registrado en el sistema,<br/>Entonces el sistema genera un proceso de recuperación y envía las instrucciones al correo electrónico asociado.<br/><br/><strong>Escenario 2: Solicitud de recuperación con correo no registrado</strong><br/>Dado que una persona solicita la recuperación de acceso,<br/>Cuando el correo electrónico proporcionado no se encuentra registrado en el sistema,<br/>Entonces el sistema informa que no existe una cuenta asociada al correo electrónico proporcionado.<br/><br/><strong>Escenario 3: Restablecimiento con proceso de recuperación expirado</strong><br/>Dado que un usuario intenta restablecer sus credenciales,<br/>Cuando el proceso de recuperación ha superado el tiempo de validez configurado,<br/>Entonces el sistema rechaza el restablecimiento e informa que el proceso de recuperación ha expirado.</td>
    </tr>
    <tr>
      <td align="left">HU14</td>
      <td align="left">E3</td>
      <td align="left">Dashboard consolidado de la planta</td>
      <td align="left">Como supervisor de seguridad quiero visualizar el estado consolidado de todas las zonas críticas de la planta para obtener una visión general del estado ambiental y de seguridad en tiempo real.</td>
      <td align="left"><strong>Escenario 1: Vista general de zonas críticas</strong><br/>Dado que el supervisor de seguridad accede a la plataforma autenticado,<br/>Cuando el sistema carga el estado de las zonas críticas registradas,<br/>Entonces la plataforma presenta el resumen de CO₂ en ppm, ruido en dB, presencia y estado de alerta de cada zona.<br/><br/><strong>Escenario 2: Identificación de zonas en condición de riesgo</strong><br/>Dado que una o más zonas críticas presentan condiciones fuera de los límites permitidos,<br/>Cuando el supervisor consulta el dashboard consolidado,<br/>Entonces el sistema identifica las zonas que requieren atención inmediata.<br/><br/><strong>Escenario 3: Planta sin zonas críticas registradas</strong><br/>Dado que el sistema no posee zonas críticas registradas,<br/>Cuando el supervisor consulta el dashboard consolidado,<br/>Entonces el sistema informa que no existen zonas críticas configuradas para monitoreo.</td>
    </tr>
    <tr>
      <td align="left">HU15</td>
      <td align="left">E3</td>
      <td align="left">Monitoreo de CO₂ en tiempo real por zona</td>
      <td align="left">Como supervisor de seguridad quiero monitorear en tiempo real la concentración de CO₂ en ppm de una zona crítica para identificar oportunamente acumulaciones peligrosas del gas en el ambiente industrial.</td>
      <td align="left"><strong>Escenario 1: Consulta de concentración de CO₂ actual</strong><br/>Dado que el supervisor consulta una zona crítica con sensor de CO₂ activo,<br/>Cuando el sensor MQ-135 registra una concentración de CO₂ en ppm,<br/>Entonces el sistema registra y presenta el valor actual de CO₂ de la zona.<br/><br/><strong>Escenario 2: Actualización de medición de CO₂</strong><br/>Dado que el supervisor monitorea una zona crítica<br/>Y el sensor de CO₂ genera una nueva medición,<br/>Cuando el sistema recibe la nueva medición a través del IoT Gateway,<br/>Entonces el sistema actualiza el valor de CO₂ correspondiente a la zona monitoreada.<br/><br/><strong>Escenario 3: Sensor de CO₂ sin transmisión de datos</strong><br/>Dado que el supervisor monitorea una zona crítica,<br/>Cuando el sensor de CO₂ deja de enviar mediciones dentro del intervalo esperado,<br/>Entonces el sistema identifica el sensor como no disponible y conserva la última medición válida registrada.<br/><br/><strong>Escenario 4: Medición de CO₂ fuera del rango válido del sensor</strong><br/>Dado que el sistema recibe una medición de CO₂ desde el dispositivo embebido,<br/>Cuando el valor de la medición se encuentra fuera del rango operativo del sensor MQ-135,<br/>Entonces el sistema descarta la medición y registra el evento como medición inválida de CO₂.</td>
    </tr>
    <tr>
      <td align="left">HU16</td>
      <td align="left">E3</td>
      <td align="left">Monitoreo de ruido en tiempo real por zona</td>
      <td align="left">Como supervisor de seguridad quiero monitorear en tiempo real el nivel de ruido en dB de una zona crítica para identificar oportunamente condiciones de exposición sonora peligrosa para los operarios.</td>
      <td align="left"><strong>Escenario 1: Consulta de nivel de ruido actual</strong><br/>Dado que el supervisor consulta una zona crítica con sensor de ruido activo,<br/>Cuando el decibelímetro registra un nivel sonoro en dB,<br/>Entonces el sistema registra y presenta el valor actual de ruido de la zona.<br/><br/><strong>Escenario 2: Actualización de medición de ruido</strong><br/>Dado que el supervisor monitorea una zona crítica<br/>Y el sensor de ruido genera una nueva medición,<br/>Cuando el sistema recibe la nueva medición a través del IoT Gateway,<br/>Entonces el sistema actualiza el valor de ruido correspondiente a la zona monitoreada.<br/><br/><strong>Escenario 3: Sensor de ruido sin transmisión de datos</strong><br/>Dado que el supervisor monitorea una zona crítica,<br/>Cuando el decibelímetro deja de enviar mediciones dentro del intervalo esperado,<br/>Entonces el sistema identifica el sensor como no disponible y conserva la última medición válida registrada.</td>
    </tr>
    <tr>
      <td align="left">HU17</td>
      <td align="left">E3</td>
      <td align="left">Monitoreo de presencia de personal por zona</td>
      <td align="left">Como supervisor de seguridad quiero monitorear la presencia de personal en una zona crítica para determinar si existen operarios expuestos a condiciones ambientales de riesgo.</td>
      <td align="left"><strong>Escenario 1: Detección de presencia por sensor PIR</strong><br/>Dado que el supervisor monitorea una zona crítica con sensor PIR activo,<br/>Cuando el sensor PIR detecta movimiento en la zona,<br/>Entonces el sistema registra la presencia de personal en la zona.<br/><br/><strong>Escenario 2: Ausencia de personal en zona monitoreada</strong><br/>Dado que el supervisor monitorea una zona crítica,<br/>Cuando el sensor PIR no detecta actividad en el intervalo configurado,<br/>Entonces el sistema registra la zona como sin personal presente.<br/><br/><strong>Escenario 3: Sensor PIR sin transmisión de datos</strong><br/>Dado que el supervisor monitorea una zona crítica,<br/>Cuando el sensor PIR deja de enviar señales dentro del intervalo esperado,<br/>Entonces el sistema identifica el sensor como no disponible y conserva el último estado de presencia registrado.</td>
    </tr>
    <tr>
      <td align="left">HU18</td>
      <td align="left">E3</td>
      <td align="left">Visualización de alertas activas</td>
      <td align="left">Como supervisor de seguridad quiero visualizar las alertas ambientales y de seguridad activas en la planta para atender oportunamente las condiciones de riesgo detectadas por el sistema.</td>
      <td align="left"><strong>Escenario 1: Listado de alertas activas en la planta</strong><br/>Dado que el sistema ha detectado una o más condiciones de riesgo sin resolver,<br/>Cuando el supervisor consulta las alertas activas,<br/>Entonces el sistema presenta la zona, el tipo de alerta, la medición asociada y la fecha de detección de cada alerta activa.<br/><br/><strong>Escenario 2: Retiro de alerta por normalización de condición</strong><br/>Dado que el supervisor visualiza las alertas activas,<br/>Cuando una condición de riesgo finaliza en una zona monitoreada,<br/>Entonces el sistema retira la alerta correspondiente del listado de alertas activas.<br/><br/><strong>Escenario 3: Ausencia de alertas activas en la planta</strong><br/>Dado que no existen condiciones de riesgo activas en ninguna zona,<br/>Cuando el supervisor consulta las alertas activas,<br/>Entonces el sistema informa que no existen alertas activas en ese momento.</td>
    </tr>
    <tr>
      <td align="left">HU19</td>
      <td align="left">E3</td>
      <td align="left">Mapa digitalizado de riesgos por zona</td>
      <td align="left">Como supervisor de seguridad quiero visualizar un mapa digitalizado de la planta con el estado de riesgo de cada zona crítica para identificar geográficamente las áreas que requieren atención inmediata.</td>
      <td align="left"><strong>Escenario 1: Mapa con zonas en estado seguro</strong><br/>Dado que todas las zonas críticas registradas se encuentran dentro de los límites permitidos,<br/>Cuando el supervisor consulta el mapa digitalizado de riesgos,<br/>Entonces el sistema presenta todas las zonas con su estado ambiental seguro en el mapa de la planta.<br/><br/><strong>Escenario 2: Mapa con zonas en condición de riesgo</strong><br/>Dado que una o más zonas críticas presentan condiciones fuera de los límites permitidos,<br/>Cuando el supervisor consulta el mapa digitalizado de riesgos,<br/>Entonces el sistema identifica en el mapa las zonas que presentan condición de riesgo activa.<br/><br/><strong>Escenario 3: Zona sin posición definida en el mapa</strong><br/>Dado que existe una zona crítica registrada sin posición definida en el mapa,<br/>Cuando el supervisor consulta el mapa digitalizado de riesgos,<br/>Entonces el sistema presenta la zona en el listado de zonas sin ubicación e informa que la posición de la zona no se encuentra configurada en el mapa.</td>
    </tr>
    <tr>
      <td align="left">HU20</td>
      <td align="left">E3</td>
      <td align="left">Gestión de zonas críticas</td>
      <td align="left">Como supervisor de seguridad quiero registrar y administrar las zonas críticas de la planta para asociar dispositivos IoT, umbrales ambientales y reglas de acceso a cada área monitoreada.</td>
      <td align="left"><strong>Escenario 1: Registro de zona crítica</strong><br/>Dado que el supervisor accede a la administración de zonas críticas,<br/>Cuando el supervisor registra una nueva zona con nombre, descripción y ubicación en el mapa,<br/>Entonces el sistema almacena la zona y la habilita para la asignación de dispositivos y configuraciones.<br/><br/><strong>Escenario 2: Modificación de zona crítica existente</strong><br/>Dado que existe una zona crítica registrada en el sistema,<br/>Cuando el supervisor modifica los datos de la zona,<br/>Entonces el sistema actualiza la información de la zona conservando su historial de eventos asociado.<br/><br/><strong>Escenario 3: Registro de zona con nombre duplicado</strong><br/>Dado que el supervisor intenta registrar una zona crítica,<br/>Cuando el nombre de la zona ya existe en el sistema,<br/>Entonces el sistema rechaza el registro e informa que la zona ya se encuentra registrada.</td>
    </tr>
    <tr>
      <td align="left">HU21</td>
      <td align="left">E3</td>
      <td align="left">Configuración de umbrales ambientales por zona</td>
      <td align="left">Como supervisor de seguridad quiero configurar los límites permitidos de CO₂ en ppm y ruido en dB para cada zona crítica para determinar cuándo una condición ambiental representa un riesgo para los operarios.</td>
      <td align="left"><strong>Escenario 1: Configuración de límites ambientales</strong><br/>Dado que el supervisor dispone de una zona crítica registrada,<br/>Cuando el supervisor configura los límites permitidos de CO₂ en ppm y ruido en dB,<br/>Entonces el sistema almacena los límites asociados a la zona.<br/><br/><strong>Escenario 2: Modificación de límite ambiental existente</strong><br/>Dado que una zona crítica tiene límites ambientales configurados,<br/>Cuando el supervisor modifica uno de los límites,<br/>Entonces el sistema reemplaza el valor anterior por el nuevo límite configurado.<br/><br/><strong>Escenario 3: Límite ambiental fuera del rango permitido por el sistema</strong><br/>Dado que el supervisor configura un límite ambiental,<br/>Cuando el valor ingresado no cumple las restricciones establecidas por el sistema,<br/>Entonces el sistema rechaza la configuración e informa que el valor no es válido.</td>
    </tr>
    <tr>
      <td align="left">HU22</td>
      <td align="left">E3</td>
      <td align="left">Registro de dispositivos IoT por zona</td>
      <td align="left">Como supervisor de seguridad quiero registrar sensores y actuadores en una zona crítica para habilitar el monitoreo ambiental y las respuestas automáticas en esa área de la planta.</td>
      <td align="left"><strong>Escenario 1: Registro de sensor en zona crítica</strong><br/>Dado que existe una zona crítica registrada en el sistema,<br/>Cuando el supervisor asocia un sensor con su tipo, identificador y dirección del dispositivo embebido,<br/>Entonces el sistema registra el sensor y lo habilita para recibir mediciones.<br/><br/><strong>Escenario 2: Registro de actuador en zona crítica</strong><br/>Dado que existe una zona crítica registrada en el sistema,<br/>Cuando el supervisor asocia un actuador con su tipo, identificador y dirección del dispositivo embebido,<br/>Entonces el sistema registra el actuador y lo habilita para recibir órdenes de control.<br/><br/><strong>Escenario 3: Registro de dispositivo con identificador duplicado</strong><br/>Dado que el supervisor intenta registrar un dispositivo IoT,<br/>Cuando el identificador del dispositivo ya se encuentra asociado en el sistema,<br/>Entonces el sistema rechaza el registro e informa que el dispositivo ya está en uso.</td>
    </tr>
    <tr>
      <td align="left">HU23</td>
      <td align="left">E3</td>
      <td align="left">Consulta de historial de mediciones y eventos ambientales</td>
      <td align="left">Como supervisor de seguridad quiero consultar el historial de mediciones, alertas y acciones automáticas de una zona crítica para analizar incidentes y verificar el comportamiento del sistema ante condiciones de riesgo.</td>
      <td align="left"><strong>Escenario 1: Registro automático de evento ambiental</strong><br/>Dado que el sistema detecta una condición ambiental fuera de los límites permitidos,<br/>Cuando el sistema procesa la condición,<br/>Entonces el sistema registra el evento con la zona, el tipo de condición, la medición y la fecha correspondiente.<br/><br/><strong>Escenario 2: Consulta de historial por zona y periodo</strong><br/>Dado que existen eventos registrados en una zona crítica,<br/>Cuando el supervisor consulta el historial de eventos de la zona para un periodo determinado,<br/>Entonces el sistema proporciona los eventos registrados correspondientes al periodo consultado.<br/><br/><strong>Escenario 3: Historial sin registros en el periodo consultado</strong><br/>Dado que una zona crítica no posee eventos en el periodo consultado,<br/>Cuando el supervisor consulta el historial de la zona,<br/>Entonces el sistema informa que no existen eventos registrados para el periodo indicado.</td>
    </tr>
    <tr>
      <td align="left">HU24</td>
      <td align="left">E4</td>
      <td align="left">Registro de operarios con credencial RFID</td>
      <td align="left">Como supervisor de seguridad quiero registrar operarios con su credencial RFID para identificar al personal autorizado que puede ingresar a zonas críticas de la planta.</td>
      <td align="left"><strong>Escenario 1: Registro de operario con credencial RFID válida</strong><br/>Dado que el supervisor accede a la administración de personal autorizado,<br/>Cuando el supervisor registra un operario con nombre, identificador laboral y código de credencial RFID,<br/>Entonces el sistema almacena al operario y habilita su credencial para el control de acceso físico.<br/><br/><strong>Escenario 2: Registro de operario con credencial RFID duplicada</strong><br/>Dado que el supervisor intenta registrar un operario,<br/>Cuando el código de credencial RFID ya se encuentra asignado a otro operario,<br/>Entonces el sistema rechaza el registro e informa que la credencial RFID ya está en uso.<br/><br/><strong>Escenario 3: Desactivación de credencial RFID de operario</strong><br/>Dado que un operario registrado posee una credencial RFID activa,<br/>Cuando el supervisor solicita la desactivación de la credencial del operario,<br/>Entonces el sistema desactiva la credencial e impide el acceso físico del operario a zonas críticas.</td>
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
      <td align="left">Como supervisor de seguridad quiero consultar el personal presente en una zona crítica para conocer qué operarios se encuentran expuestos a condiciones ambientales de riesgo.</td>
      <td align="left"><strong>Escenario 1: Personal identificado presente en zona</strong><br/>Dado que uno o más operarios registrados se encuentran en una zona crítica,<br/>Cuando el supervisor consulta el personal presente en la zona,<br/>Entonces el sistema presenta el listado de operarios identificados en esa zona.<br/><br/><strong>Escenario 2: Presencia detectada sin identificación de operario</strong><br/>Dado que el sensor PIR detecta presencia en una zona crítica<br/>Y ningún operario ha sido identificado por el lector RFID en la zona,<br/>Cuando el supervisor consulta el personal presente en la zona,<br/>Entonces el sistema informa que existe presencia no identificada en la zona.<br/><br/><strong>Escenario 3: Zona sin personal presente</strong><br/>Dado que no existen operarios en una zona crítica,<br/>Cuando el supervisor consulta el personal presente en la zona,<br/>Entonces el sistema informa que no existe personal presente en la zona.</td>
    </tr>
    <tr>
      <td align="left">HU28</td>
      <td align="left">E4</td>
      <td align="left">Registro histórico de accesos RFID a zonas críticas</td>
      <td align="left">Como supervisor de seguridad quiero consultar el historial de accesos físicos a zonas críticas registrados por el lector RFID para analizar los patrones de ingreso y las exposiciones de personal a áreas de riesgo.</td>
      <td align="left"><strong>Escenario 1: Registro de acceso autorizado</strong><br/>Dado que un operario registrado ingresa a una zona crítica con condiciones ambientales seguras,<br/>Cuando el lector RFID procesa la credencial del operario,<br/>Entonces el sistema registra el acceso con el identificador del operario, la zona, el resultado autorizado y la fecha del evento.<br/><br/><strong>Escenario 2: Registro de acceso denegado</strong><br/>Dado que un operario registrado intenta ingresar a una zona crítica con condición ambiental peligrosa,<br/>Cuando el lector RFID procesa la credencial del operario,<br/>Entonces el sistema registra el intento de acceso con el identificador del operario, la zona, el resultado denegado, el motivo y la fecha del evento.<br/><br/><strong>Escenario 3: Historial de accesos sin registros en el periodo</strong><br/>Dado que una zona crítica no posee registros de acceso en el periodo consultado,<br/>Cuando el supervisor consulta el historial de accesos de la zona,<br/>Entonces el sistema informa que no existen registros de acceso para el periodo indicado.</td>
    </tr>
    <tr>
      <td align="left">HU29</td>
      <td align="left">E4</td>
      <td align="left">Cruce de presencia de personal con niveles de CO₂</td>
      <td align="left">Como supervisor de seguridad quiero que el sistema evalúe simultáneamente la presencia de personal y los niveles de CO₂ en una zona crítica para determinar si existen operarios expuestos a concentraciones peligrosas del gas.</td>
      <td align="left"><strong>Escenario 1: Exposición de personal a CO₂ excesivo</strong><br/>Dado que el sistema detecta personal presente en una zona crítica<br/>Y la concentración de CO₂ en la zona supera el límite permitido,<br/>Cuando el sistema evalúa las condiciones de la zona,<br/>Entonces el sistema identifica una condición de exposición a CO₂ y genera una alerta de seguridad para la zona.<br/><br/><strong>Escenario 2: CO₂ excesivo sin personal presente</strong><br/>Dado que el sistema detecta ausencia de personal en una zona crítica<br/>Y la concentración de CO₂ en la zona supera el límite permitido,<br/>Cuando el sistema evalúa las condiciones de la zona,<br/>Entonces el sistema identifica una condición de CO₂ excesivo sin exposición de personal y activa el extractor de aire sin activar la sirena preventiva.<br/><br/><strong>Escenario 3: Personal presente con CO₂ dentro del límite</strong><br/>Dado que el sistema detecta personal presente en una zona crítica<br/>Y la concentración de CO₂ se encuentra dentro del límite permitido,<br/>Cuando el sistema evalúa las condiciones de la zona,<br/>Entonces el sistema mantiene la zona en estado de exposición segura para el personal presente.</td>
    </tr>
    <tr>
      <td align="left">HU30</td>
      <td align="left">E5</td>
      <td align="left">Detección de exceso de CO₂</td>
      <td align="left">Como sistema de monitoreo industrial quiero detectar cuando la concentración de CO₂ supera el límite permitido en una zona crítica para activar oportunamente las medidas automáticas de purificación y prevención.</td>
      <td align="left"><strong>Escenario 1: CO₂ dentro del límite permitido</strong><br/>Dado que el sistema monitorea una zona crítica con un límite de CO₂ configurado,<br/>Cuando el sensor MQ-135 registra una concentración igual o inferior al límite permitido,<br/>Entonces el sistema mantiene la zona en estado ambiental permitido.<br/><br/><strong>Escenario 2: CO₂ por encima del límite permitido</strong><br/>Dado que el sistema monitorea una zona crítica con un límite de CO₂ configurado,<br/>Cuando el sensor MQ-135 registra una concentración superior al límite permitido,<br/>Entonces el sistema identifica una condición de CO₂ excesivo y genera una alerta ambiental.<br/><br/><strong>Escenario 3: Medición de CO₂ inválida descartada</strong><br/>Dado que el sistema recibe una medición de CO₂ desde el dispositivo embebido,<br/>Cuando la medición se encuentra fuera del rango válido del sensor MQ-135,<br/>Entonces el sistema descarta la medición y registra el evento como medición inválida de CO₂.</td>
    </tr>
    <tr>
      <td align="left">HU31</td>
      <td align="left">E5</td>
      <td align="left">Detección de ruido excesivo</td>
      <td align="left">Como sistema de monitoreo industrial quiero detectar cuando el nivel sonoro supera el límite permitido en una zona crítica para prevenir la exposición de los operarios a niveles de ruido peligrosos.</td>
      <td align="left"><strong>Escenario 1: Ruido dentro del límite permitido</strong><br/>Dado que el sistema monitorea una zona crítica con un límite sonoro configurado,<br/>Cuando el decibelímetro registra un nivel igual o inferior al límite permitido,<br/>Entonces el sistema mantiene la zona en estado sonoro permitido.<br/><br/><strong>Escenario 2: Ruido excesivo sin personal presente</strong><br/>Dado que el sistema detecta un nivel sonoro superior al límite permitido<br/>Y el sistema registra ausencia de personal en la zona,<br/>Cuando el sistema evalúa la condición ambiental,<br/>Entonces el sistema registra la exposición sonora sin activar la sirena preventiva dirigida a operarios.<br/><br/><strong>Escenario 3: Ruido excesivo con personal presente</strong><br/>Dado que el sistema detecta un nivel sonoro superior al límite permitido<br/>Y el sistema detecta personal presente en la zona,<br/>Cuando el sistema evalúa la condición ambiental,<br/>Entonces el sistema genera una alerta de exposición sonora y activa la sirena preventiva.</td>
    </tr>
    <tr>
      <td align="left">HU32</td>
      <td align="left">E5</td>
      <td align="left">Activación automática del extractor de aire por CO₂</td>
      <td align="left">Como sistema de monitoreo industrial quiero activar automáticamente el extractor de aire mediante el relé de control cuando se detecte un exceso de CO₂ para reducir la concentración del gas y recuperar condiciones ambientales seguras.</td>
      <td align="left"><strong>Escenario 1: Activación del extractor por exceso de CO₂</strong><br/>Dado que una zona crítica presenta una concentración de CO₂ superior al límite permitido,<br/>Cuando el sistema confirma la condición de exceso de CO₂,<br/>Entonces el sistema activa el extractor de aire asociado a la zona mediante el relé de control.<br/><br/><strong>Escenario 2: Desactivación del extractor al normalizar CO₂</strong><br/>Dado que el extractor de aire se encuentra activo por una condición de CO₂ excesivo,<br/>Cuando la concentración de CO₂ retorna al rango permitido,<br/>Entonces el sistema desactiva el extractor de aire de la zona.<br/><br/><strong>Escenario 3: Fallo en la activación del extractor</strong><br/>Dado que el sistema determina que debe activar el extractor de aire,<br/>Cuando el relé de control no confirma la activación del extractor,<br/>Entonces el sistema registra el fallo y genera una alerta de actuador no disponible.<br/><br/><strong>Escenario 4: Pérdida de comunicación con el dispositivo embebido durante activación</strong><br/>Dado que el sistema envía la orden de activación al extractor de aire,<br/>Cuando el dispositivo embebido ESP32 no responde dentro del tiempo esperado,<br/>Entonces el sistema registra el fallo de comunicación y mantiene la alerta de CO₂ excesivo activa en la zona.</td>
    </tr>
    <tr>
      <td align="left">HU33</td>
      <td align="left">E5</td>
      <td align="left">Activación de sirena preventiva por exposición a condición peligrosa</td>
      <td align="left">Como sistema de seguridad quiero activar la sirena preventiva cuando un operario se encuentre expuesto a una condición peligrosa de CO₂ o ruido excesivo para advertir inmediatamente sobre el riesgo existente y permitir la evacuación de la zona.</td>
      <td align="left"><strong>Escenario 1: Sirena activada por CO₂ peligroso con personal presente</strong><br/>Dado que el sistema detecta una concentración peligrosa de CO₂ en una zona crítica<br/>Y el sistema detecta personal presente en la zona,<br/>Cuando el sistema determina que existe exposición de operarios,<br/>Entonces el sistema activa la sirena preventiva de la zona.<br/><br/><strong>Escenario 2: Sirena activada por ruido peligroso con personal presente</strong><br/>Dado que el sistema detecta un nivel de ruido superior al límite permitido<br/>Y el sistema detecta personal presente en la zona,<br/>Cuando el sistema determina que existe exposición de operarios,<br/>Entonces el sistema activa la sirena preventiva de la zona.<br/><br/><strong>Escenario 3: Sirena inactiva en condiciones seguras con personal presente</strong><br/>Dado que el sistema detecta personal presente en una zona crítica,<br/>Cuando las concentraciones de CO₂ y los niveles de ruido se encuentran dentro de los límites permitidos,<br/>Entonces el sistema mantiene la sirena preventiva desactivada.<br/><br/><strong>Escenario 4: Desactivación de sirena al cesar condición de riesgo</strong><br/>Dado que la sirena preventiva se encuentra activa por una condición de exposición,<br/>Cuando la condición peligrosa desaparece y no existe otra condición de alarma activa en la zona,<br/>Entonces el sistema desactiva la sirena preventiva de la zona.</td>
    </tr>
    <tr>
      <td align="left">HU34</td>
      <td align="left">E5</td>
      <td align="left">Despliegue de mamparas acústicas por exposición sonora</td>
      <td align="left">Como sistema de monitoreo industrial quiero desplegar mamparas móviles de aislamiento acústico mediante servomotores cuando se detecte ruido excesivo con personal presente para reducir la exposición sonora de los operarios en la zona afectada.</td>
      <td align="left"><strong>Escenario 1: Despliegue de mamparas por ruido excesivo con personal</strong><br/>Dado que una zona crítica presenta un nivel de ruido superior al límite permitido<br/>Y el sistema detecta personal presente en la zona,<br/>Cuando el sistema confirma la condición de exposición sonora,<br/>Entonces el sistema activa los servomotores y despliega las mamparas acústicas de la zona.<br/><br/><strong>Escenario 2: Retracción de mamparas al normalizar el ruido</strong><br/>Dado que las mamparas acústicas se encuentran desplegadas por una condición de ruido excesivo,<br/>Cuando el nivel sonoro retorna al rango permitido,<br/>Entonces el sistema retrae las mamparas acústicas de la zona.<br/><br/><strong>Escenario 3: Fallo en el despliegue de mamparas acústicas</strong><br/>Dado que el sistema determina que debe desplegar las mamparas acústicas,<br/>Cuando el servomotor no confirma el despliegue dentro del tiempo esperado,<br/>Entonces el sistema registra el fallo y genera una alerta de actuador no disponible.</td>
    </tr>
    <tr>
      <td align="left">HU35</td>
      <td align="left">E5</td>
      <td align="left">Anulación manual de actuador en emergencia</td>
      <td align="left">Como supervisor de seguridad quiero anular manualmente el estado de un actuador durante una emergencia para asumir el control directo de extractores, sirenas o mamparas cuando la respuesta automática no sea adecuada para la situación.</td>
      <td align="left"><strong>Escenario 1: Anulación manual de extractor en emergencia</strong><br/>Dado que el extractor de aire de una zona se encuentra activo automáticamente,<br/>Cuando el supervisor de seguridad solicita la anulación manual y activación forzada del extractor,<br/>Entonces el sistema aplica el estado solicitado al extractor y registra la anulación manual con el identificador del supervisor y la fecha del evento.<br/><br/><strong>Escenario 2: Anulación manual de sirena en emergencia</strong><br/>Dado que la sirena preventiva de una zona se encuentra activa automáticamente,<br/>Cuando el supervisor de seguridad solicita la desactivación manual de la sirena,<br/>Entonces el sistema desactiva la sirena y registra la anulación manual con el identificador del supervisor y la fecha del evento.<br/><br/><strong>Escenario 3: Anulación manual por supervisor no autorizado</strong><br/>Dado que un operario de planta mantiene una sesión activa en la plataforma,<br/>Cuando el operario solicita la anulación manual de un actuador,<br/>Entonces el sistema rechaza la operación e informa que la anulación manual requiere el rol de supervisor de seguridad.</td>
    </tr>
    <tr>
      <td align="left">HU36</td>
      <td align="left">E5</td>
      <td align="left">Registro de acciones automáticas ejecutadas</td>
      <td align="left">Como supervisor de seguridad quiero consultar las acciones automáticas ejecutadas por el sistema para verificar que los mecanismos de prevención respondieron ante las condiciones peligrosas detectadas.</td>
      <td align="left"><strong>Escenario 1: Registro de activación automática de actuador</strong><br/>Dado que el sistema activa un extractor, una sirena o una mampara acústica,<br/>Cuando la acción automática se ejecuta en la zona,<br/>Entonces el sistema registra el actuador, la acción realizada, la zona y el momento de ejecución.<br/><br/><strong>Escenario 2: Registro de desactivación automática de actuador</strong><br/>Dado que un actuador se encuentra activo por una condición ambiental,<br/>Cuando el sistema determina que la condición que originó la acción ha finalizado,<br/>Entonces el sistema registra la desactivación del actuador con la zona y el momento del evento.<br/><br/><strong>Escenario 3: Registro de acción automática fallida</strong><br/>Dado que el sistema envía una orden automática a un actuador,<br/>Cuando el actuador no confirma la ejecución,<br/>Entonces el sistema registra la acción como fallida con el actuador, la zona y el motivo del fallo.</td>
    </tr>
    <tr>
      <td align="left">HU37</td>
      <td align="left">E5</td>
      <td align="left">Notificación física de alarma al operario expuesto</td>
      <td align="left">Como operario de planta quiero recibir una alarma física audible cuando me encuentre expuesto a una condición peligrosa de CO₂ o ruido excesivo para conocer la situación de riesgo y retirarme de la zona afectada.</td>
      <td align="left"><strong>Escenario 1: Alarma audible por exposición a CO₂ peligroso</strong><br/>Dado que el operario se encuentra en una zona crítica con condición peligrosa de CO₂,<br/>Cuando el sistema activa la sirena preventiva de la zona,<br/>Entonces el operario recibe la señal audible de alarma en el entorno físico de la zona.<br/><br/><strong>Escenario 2: Alarma audible por exposición a ruido excesivo</strong><br/>Dado que el operario se encuentra en una zona crítica con nivel de ruido superior al límite permitido,<br/>Cuando el sistema activa la sirena preventiva de la zona,<br/>Entonces el operario recibe la señal audible de alarma en el entorno físico de la zona.<br/><br/><strong>Escenario 3: Ausencia de alarma en condiciones seguras</strong><br/>Dado que el operario se encuentra en una zona crítica,<br/>Cuando las condiciones de CO₂ y ruido se encuentran dentro de los límites permitidos,<br/>Entonces el sistema mantiene la sirena preventiva desactivada en la zona.<br/><br/><strong>Escenario 4: Fallo de sirena con operario expuesto</strong><br/>Dado que el operario se encuentra en una zona con condición de riesgo activa,<br/>Cuando el buzzer de la sirena no responde a la orden de activación,<br/>Entonces el sistema registra el fallo del actuador y mantiene la alerta de exposición activa en la plataforma de supervisión.</td>
    </tr>
    <tr>
      <td align="left">HU38</td>
      <td align="left">E6</td>
      <td align="left">Tiempo de respuesta crítica en activación de actuadores</td>
      <td align="left">Como supervisor de seguridad quiero que el sistema active extractores, sirenas y mamparas acústicas dentro de un tiempo máximo de respuesta definido para reducir la exposición del personal a condiciones ambientales peligrosas en la planta industrial.</td>
      <td align="left"><strong>Escenario 1: Activación del extractor por exceso de CO₂ dentro del límite temporal</strong><br/>Dado que una zona crítica presenta una concentración de CO₂ superior al límite permitido<br/>Y el sensor MQ-135 transmite una medición válida al IoT Gateway<br/>Y el extractor de aire de la zona se encuentra operativo,<br/>Cuando el sistema confirma la condición de exceso de CO₂ en la zona,<br/>Entonces el sistema activa el extractor de aire mediante el relé de control en un intervalo inferior a 2 segundos contados desde el instante de la medición válida que originó la alerta.<br/><br/><strong>Escenario 2: Activación de sirena preventiva con personal presente dentro del límite temporal</strong><br/>Dado que una zona crítica presenta una condición peligrosa de CO₂ o de ruido superior al límite permitido<br/>Y el sistema registra personal presente en la zona<br/>Y la sirena preventiva de la zona se encuentra operativa,<br/>Cuando el sistema determina que existe exposición de operarios a la condición de riesgo,<br/>Entonces el sistema activa la sirena preventiva de la zona en un intervalo inferior a 2 segundos contados desde el instante en que se confirma la condición de riesgo con personal presente.<br/><br/><strong>Escenario 3: Despliegue de mamparas acústicas por exposición sonora dentro del límite temporal</strong><br/>Dado que una zona crítica presenta un nivel de ruido superior al límite permitido<br/>Y el sistema registra personal presente en la zona<br/>Y los servomotores de mamparas acústicas de la zona se encuentran operativos,<br/>Cuando el sistema confirma la condición de exposición sonora con personal presente,<br/>Entonces el sistema activa los servomotores y despliega las mamparas acústicas en un intervalo inferior a 2 segundos contados desde el instante en que se confirma la condición de riesgo sonoro.<br/><br/><strong>Escenario 4: Activación local del extractor durante indisponibilidad de conectividad hacia la nube</strong><br/>Dado que el IoT Gateway mantiene conectividad local con los dispositivos ESP32 de una zona crítica<br/>Y la conexión a internet de la planta se encuentra interrumpida<br/>Y una zona crítica presenta una concentración de CO₂ superior al límite permitido con medición válida recibida localmente,<br/>Cuando el IoT Gateway procesa la condición de riesgo con las reglas configuradas en el entorno local,<br/>Entonces el sistema activa el extractor de aire de la zona en un intervalo inferior a 2 segundos contados desde la medición válida, sin depender de la disponibilidad de la plataforma en la nube.<br/><br/><strong>Escenario 5: Medición inválida sin activación de actuadores</strong><br/>Dado que el dispositivo ESP32 de una zona crítica envía una medición de CO₂ fuera del rango operativo del sensor MQ-135,<br/>Cuando el IoT Gateway recibe y descarta la medición como inválida,<br/>Entonces el sistema no activa extractores, sirenas ni mamparas acústicas por esa medición<br/>Y el sistema registra el evento como medición inválida de CO₂ con la zona y el instante correspondiente.<br/><br/><strong>Escenario 6: Fallo del actuador con registro de incumplimiento del tiempo de respuesta útil</strong><br/>Dado que una zona crítica presenta una condición de riesgo confirmada que requiere activación del extractor de aire<br/>Y el relé de control no confirma la activación del extractor dentro del intervalo operativo esperado,<br/>Cuando transcurren 2 segundos desde la confirmación de la condición de riesgo sin respuesta operativa del actuador,<br/>Entonces el sistema registra el fallo del actuador con la zona, el actuador afectado y el instante del evento<br/>Y el sistema mantiene la alerta de riesgo activa en la plataforma de supervisión disponible.</td>
    </tr>
    <tr>
      <td align="left">HU39</td>
      <td align="left">E6</td>
      <td align="left">Persistencia local y resincronización de telemetría en contingencia offline</td>
      <td align="left">Como supervisor de seguridad quiero que el IoT Gateway conserve mediciones y eventos del sistema durante una interrupción de conectividad a internet para mantener trazabilidad operativa y continuidad del monitoreo en la planta.</td>
      <td align="left"><strong>Escenario 1: Almacenamiento local de mediciones ambientales durante caída de internet</strong><br/>Dado que el IoT Gateway recibe mediciones válidas de CO₂, ruido y presencia desde dispositivos ESP32 de una zona crítica<br/>Y la conexión a internet de la planta se interrumpe,<br/>Cuando el IoT Gateway procesa las mediciones recibidas sin poder enviarlas a la API en la nube,<br/>Entonces el sistema persiste cada medición en la base de datos local SQLite con identificador de zona, tipo de medición, valor, origen del dispositivo y marca temporal.<br/><br/><strong>Escenario 2: Registro local de eventos de alerta durante contingencia offline</strong><br/>Dado que el IoT Gateway detecta una condición ambiental fuera de los límites permitidos en una zona crítica<br/>Y la conexión a internet de la planta se encuentra interrumpida,<br/>Cuando el sistema genera una alerta ambiental o de seguridad asociada a la zona,<br/>Entonces el sistema registra el evento de alerta en SQLite con la zona, el tipo de alerta, la medición asociada y la marca temporal<br/>Y el sistema mantiene el estado de alerta disponible para consulta local mientras persista la contingencia.<br/><br/><strong>Escenario 3: Registro local de acciones automáticas de actuadores durante contingencia offline</strong><br/>Dado que el IoT Gateway ordena la activación o desactivación de un extractor, sirena o mampara acústica en una zona crítica<br/>Y la conexión a internet de la planta se encuentra interrumpida,<br/>Cuando la acción automática se ejecuta o falla en el entorno local,<br/>Entonces el sistema registra la acción en SQLite con el actuador, la operación realizada, la zona, el resultado y la marca temporal.<br/><br/><strong>Escenario 4: Resincronización ordenada de mediciones al restablecer conectividad</strong><br/>Dado que existen mediciones almacenadas en SQLite sin sincronizar con la plataforma en la nube<br/>Y la conexión a internet de la planta se restablece,<br/>Cuando el IoT Gateway inicia el proceso de resincronización hacia la API en la nube,<br/>Entonces el sistema envía las mediciones pendientes en orden cronológico<br/>Y el sistema marca cada registro local como sincronizado al recibir confirmación de persistencia en la nube.<br/><br/><strong>Escenario 5: Resincronización de alertas y acciones automáticas pendientes</strong><br/>Dado que existen eventos de alerta y registros de acciones automáticas almacenados en SQLite sin sincronizar<br/>Y la conexión a internet de la planta se restablece,<br/>Cuando el IoT Gateway ejecuta la resincronización de eventos operativos hacia la API en la nube,<br/>Entonces el sistema transmite los eventos pendientes preservando la secuencia temporal original<br/>Y el sistema conserva en la nube la trazabilidad completa de alertas y acciones ocurridas durante la contingencia offline.<br/><br/><strong>Escenario 6: Saturación de almacenamiento local por contingencia prolongada</strong><br/>Dado que la conexión a internet de la planta permanece interrumpida durante un periodo prolongado<br/>Y el volumen de mediciones y eventos generados supera la capacidad de retención configurada en SQLite,<br/>Cuando el IoT Gateway alcanza el límite de almacenamiento local disponible,<br/>Entonces el sistema conserva prioritariamente los registros de alertas, acciones automáticas y accesos RFID recientes<br/>Y el sistema registra un evento de contingencia de almacenamiento local con la fecha y el nivel de saturación alcanzado.<br/><br/><strong>Escenario 7: Rechazo de resincronización por telemetría corrupta o incompleta</strong><br/>Dado que un registro almacenado en SQLite presenta datos incompletos o inconsistentes para su envío a la nube<br/>Y la conexión a internet de la planta se encuentra disponible,<br/>Cuando el IoT Gateway intenta resincronizar el registro hacia la API en la nube,<br/>Entonces el sistema no elimina el registro local sin confirmación válida de persistencia remota<br/>Y el sistema registra el intento fallido de resincronización con el identificador del registro y el motivo detectado.</td>
    </tr>
    <tr>
      <td align="left">HU40</td>
      <td align="left">E6</td>
      <td align="left">Protección de telemetría y sesiones de supervisión</td>
      <td align="left">Como administrador de TI quiero que la telemetría transmitida hacia la nube y las sesiones de los supervisores estén protegidas contra acceso no autorizado para preservar la confidencialidad e integridad de la información operativa del sistema.</td>
      <td align="left"><strong>Escenario 1: Transmisión cifrada de telemetría desde el Gateway hacia la API</strong><br/>Dado que el IoT Gateway dispone de credenciales válidas para comunicarse con la API en la nube<br/>Y existen mediciones y eventos listos para transmisión remota,<br/>Cuando el IoT Gateway envía telemetría hacia el endpoint de ingesta de la plataforma,<br/>Entonces la comunicación se establece mediante un canal cifrado TLS<br/>Y la telemetría viaja sin exposición en texto plano sobre la red externa de la planta.<br/><br/><strong>Escenario 2: Rechazo de telemetría enviada por canal no cifrado</strong><br/>Dado que un emisor intenta entregar telemetría de una zona crítica hacia la API en la nube,<br/>Cuando la solicitud de ingesta no utiliza un canal cifrado TLS,<br/>Entonces la API en la nube rechaza la recepción de la telemetría<br/>Y el sistema registra el intento rechazado con origen, instante y motivo de seguridad.<br/><br/><strong>Escenario 3: Rechazo de telemetría con credencial de Gateway inválida</strong><br/>Dado que un emisor presenta una solicitud de ingesta de telemetría hacia la API en la nube,<br/>Cuando la credencial del IoT Gateway es inválida, expirada o no reconocida,<br/>Entonces la API en la nube rechaza la solicitud de ingesta<br/>Y el sistema no persiste la telemetría recibida en la base de datos relacional de la plataforma.<br/><br/><strong>Escenario 4: Expiración de sesión inactiva de supervisor de seguridad</strong><br/>Dado que un supervisor de seguridad mantiene una sesión autenticada en la plataforma de supervisión<br/>Y transcurre el periodo configurado de inactividad sin interacción autorizada del supervisor,<br/>Cuando el supervisor intenta acceder a una función protegida de monitoreo o configuración,<br/>Entonces el sistema finaliza la sesión expirada<br/>Y el sistema exige una nueva autenticación antes de permitir el acceso a funciones protegidas.<br/><br/><strong>Escenario 5: Acceso denegado con token de sesión expirado</strong><br/>Dado que un supervisor de seguridad posee un token de sesión expirado,<br/>Cuando el supervisor solicita acceso a información de telemetría o configuración de zonas críticas,<br/>Entonces el sistema deniega el acceso a la funcionalidad solicitada<br/>Y el sistema informa que la sesión no se encuentra vigente.<br/><br/><strong>Escenario 6: Protección de credenciales de dispositivos embebidos en tránsito local</strong><br/>Dado que un dispositivo ESP32 envía mediciones al IoT Gateway mediante solicitudes de red locales,<br/>Cuando la solicitud incluye un token de autenticación de dispositivo configurado para el entorno industrial,<br/>Entonces el IoT Gateway acepta la telemetría únicamente si el token corresponde a un dispositivo registrado y vigente<br/>Y el sistema rechaza solicitudes de dispositivos no autorizados sin incorporar sus mediciones al flujo operativo.</td>
    </tr>
    <tr>
      <td align="left">HU41</td>
      <td align="left">E6</td>
      <td align="left">Disponibilidad operativa de la plataforma de supervisión</td>
      <td align="left">Como supervisor de seguridad quiero que la plataforma de supervisión mantenga una disponibilidad operativa definida para acceder de forma continua al monitoreo de CO₂, ruido, presencia y alertas activas en la planta industrial.</td>
      <td align="left"><strong>Escenario 1: Acceso al dashboard durante operación nominal de la plataforma</strong><br/>Dado que la plataforma de supervisión se encuentra en operación nominal<br/>Y un supervisor de seguridad dispone de credenciales válidas,<br/>Cuando el supervisor accede al dashboard consolidado de la planta,<br/>Entonces el sistema presenta el estado de zonas críticas, alertas activas y telemetría reciente sin interrupción del servicio de supervisión.<br/><br/><strong>Escenario 2: Indisponibilidad no planificada del servicio de supervisión</strong><br/>Dado que la plataforma de supervisión experimenta una falla que impide el acceso al dashboard,<br/>Cuando un supervisor de seguridad intenta acceder al monitoreo de la planta,<br/>Entonces el sistema informa indisponibilidad temporal del servicio de supervisión<br/>Y el IoT Gateway continúa el monitoreo local, la persistencia en SQLite y la respuesta automática de actuadores configurada en el entorno industrial.<br/><br/><strong>Escenario 3: Cumplimiento del objetivo mensual de disponibilidad</strong><br/>Dado que la plataforma de supervisión opera durante un periodo mensual de evaluación<br/>Y el objetivo de disponibilidad operativa del servicio se encuentra definido en 99.9 por ciento,<br/>Cuando el periodo mensual concluye,<br/>Entonces el sistema mantiene la plataforma de supervisión disponible al menos en el porcentaje objetivo definido, excluyendo ventanas de mantenimiento planificado previamente registradas.<br/><br/><strong>Escenario 4: Mantenimiento planificado con continuidad local del monitoreo industrial</strong><br/>Dado que la plataforma de supervisión entra en una ventana de mantenimiento planificado previamente registrada,<br/>Cuando los dispositivos ESP32 continúan enviando telemetría al IoT Gateway durante la ventana de mantenimiento,<br/>Entonces el monitoreo local, la generación de alertas y la activación automática de actuadores continúan operando en la planta<br/>Y el sistema registra las mediciones y eventos para su posterior consulta cuando la plataforma de supervisión retome operación.</td>
    </tr>
    <tr>
      <td align="left">HU42</td>
      <td align="left">E6</td>
      <td align="left">Compatibilidad multiplataforma de la experiencia de supervisión</td>
      <td align="left">Como supervisor de seguridad quiero acceder a la plataforma de supervisión desde navegadores web modernos y dispositivos móviles actuales para consultar telemetría y alertas desde distintos entornos operativos de la planta.</td>
      <td align="left"><strong>Escenario 1: Consulta de telemetría desde navegador de escritorio compatible</strong><br/>Dado que un supervisor de seguridad accede a la plataforma desde un navegador web moderno soportado en estación de trabajo,<br/>Cuando el supervisor consulta el dashboard consolidado y el detalle de una zona crítica,<br/>Entonces el sistema presenta valores de CO₂ en ppm, ruido en dB, presencia y alertas activas de forma legible y operable en el navegador utilizado.<br/><br/><strong>Escenario 2: Consulta de alertas activas desde navegador móvil compatible</strong><br/>Dado que un supervisor de seguridad accede a la plataforma desde un navegador móvil soportado en dispositivo Android o iOS,<br/>Cuando el supervisor consulta las alertas activas de la planta,<br/>Entonces el sistema presenta la lista de alertas con zona, tipo, medición asociada y fecha de detección sin pérdida de información esencial para la atención operativa.<br/><br/><strong>Escenario 3: Acceso desde navegador no soportado</strong><br/>Dado que un supervisor de seguridad intenta acceder a la plataforma desde un navegador no incluido en la matriz de compatibilidad soportada,<br/>Cuando el supervisor solicita acceso al dashboard de supervisión,<br/>Entonces el sistema informa que el navegador utilizado no se encuentra soportado<br/>Y el sistema indica los navegadores compatibles para acceder a la plataforma de supervisión.<br/><br/><strong>Escenario 4: Consulta de mapa de riesgos en dispositivo móvil compatible</strong><br/>Dado que un supervisor de seguridad accede a la plataforma desde un dispositivo móvil soportado,<br/>Cuando el supervisor consulta el mapa digitalizado de riesgos por zona,<br/>Entonces el sistema presenta el estado de riesgo de cada zona crítica configurada en el mapa de la planta de forma comprensible en el dispositivo utilizado.<br/><br/><strong>Escenario 5: Continuidad funcional de monitoreo entre estación de trabajo y dispositivo móvil</strong><br/>Dado que un supervisor de seguridad mantiene una sesión autenticada válida en la plataforma,<br/>Cuando el supervisor alterna el acceso entre una estación de trabajo y un dispositivo móvil soportado durante la misma jornada operativa,<br/>Entonces el sistema presenta información coherente de telemetría, alertas activas y estado de zonas críticas en ambos entornos de acceso autorizados.</td>
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

**Navegación:** [Índice](./00-student-outcome.md#s-tabla-contenidos) · Anterior: [Capítulo II](./02-capitulo-ii-requirements-elicitation.md) · Siguiente: [Capítulo IV](./04-capitulo-iv-solution-software-design.md)
