**Navegación:** [Índice](./00-student-outcome.md#s-tabla-contenidos) · Anterior: [Capítulo I](./01-capitulo-i-introduccion.md) · Siguiente: [Capítulo III](./03-capitulo-iii-requirements-specification.md)

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
      <th align="center">Macallys</th>
      <th align="center">Honeywell Forge</th>
      <th align="center">Sistemas SCADA</th>
      <th align="center">Medidores Manuales</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td align="left" colspan="5"><strong>Perfil</strong></td>
    </tr>
    <tr>
      <td align="left">Overview</td>
      <td align="left">Ecosistema IoT optimizado que cruza registros de sensores con tablas de umbrales para ejecutar acciones inmediatas.</td>
      <td align="left">Plataforma corporativa masiva para la gestión integral de edificios, energía y operaciones globales.</td>
      <td align="left">Sistemas de control y adquisición de datos centralizados, diseñados para la automatización a nivel de maquinaria pesada.</td>
      <td align="left">Equipos físicos aislados operados manualmente.</td>
    </tr>
    <tr>
      <td align="left">Ventaja competitiva<br/>¿Qué valor ofrece a los clientes?</td>
      <td align="left">Procesamiento relacional que dispara mitigadores automáticamente, sin depender de la interacción del usuario.</td>
      <td align="left">Ecosistema completo y altamente robusto con capacidad de integración para corporaciones multinacionales.</td>
      <td align="left">Alta capacidad de control directo y fiabilidad sobre procesos complejos.</td>
      <td align="left">Bajo costo inicial por equipo y operación independiente que no requiere infraestructura de red ni bases de datos.</td>
    </tr>
    <tr>
      <td align="left" colspan="5"><strong>Perfil de Marketing</strong></td>
    </tr>
    <tr>
      <td align="left">Mercado objetivo</td>
      <td align="left">Plantas industriales. Usuarios: Supervisores de seguridad y encargados de planta.</td>
      <td align="left">Grandes corporaciones y multinacionales sobre transformación digital.</td>
      <td align="left">Plantas de industria pesada, gestionadas por ingenieros de automatización.</td>
      <td align="left">Pequeñas industrias y prevencionistas de riesgos independientes.</td>
    </tr>
    <tr>
      <td align="left">Estrategias de marketing</td>
      <td align="left">Solución enfocada en salud ocupacional, destacando la velocidad de respuesta de los dispositivos IOT.</td>
      <td align="left">Ventas B2B corporativas, ofreciendo transformación digital integral y eficiencia energética a nivel macro.</td>
      <td align="left">Provisión a través de integradores de sistemas y venta por proyectos de ingeniería a medida.</td>
      <td align="left">Venta directa a través de catálogos y distribuidores de Equipos de Protección Personal.</td>
    </tr>
    <tr>
      <td align="left" colspan="5"><strong>Perfil de Producto</strong></td>
    </tr>
    <tr>
      <td align="left">Productos &amp; Servicios</td>
      <td align="left">Nodos IoT, actuadores y API REST para gestionar alertas, registros de sensores y mitigadores.</td>
      <td align="left">Software empresarial pesado, integración de sistemas de control industrial.</td>
      <td align="left">Controladores, servidores locales con bases de datos propietarias y paneles HMI.</td>
      <td align="left">Dispositivos de hardware de medición ambiental sin capacidades de conexión a red.</td>
    </tr>
    <tr>
      <td align="left">Precios &amp; Costos</td>
      <td align="left">Costo de entrada bajo/medio.</td>
      <td align="left">Costos de implementación y licencias corporativas muy altos.</td>
      <td align="left">Muy alto. Requiere instalación de red cableada estructurada y programación por equipo.</td>
      <td align="left">Costo unitario muy bajo, pero alto costo operativo oculto por ineficiencia humana.</td>
    </tr>
    <tr>
      <td align="left">Canales de distribución<br/>(Web y/o Móvil)</td>
      <td align="left">Plataforma Web y App Móvil.</td>
      <td align="left">Aplicaciones de escritorio y plataformas Web corporativas.</td>
      <td align="left">Interfaces locales en terminales de escritorio y paneles fijos.</td>
      <td align="left">Distribuidores físicos de hardware. Sin canales digitales de interacción.</td>
    </tr>
  </tbody>
</table>

**Análisis SWOT**

<table>
  <thead>
    <tr>
      <th align="left">SWOT</th>
      <th align="left">Macallys</th>
      <th align="left">Honeywell Forge</th>
      <th align="left">Sistemas SCADA</th>
      <th align="left">Medidores Manuales</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td align="left"><strong>Fortalezas</strong></td>
      <td align="left">Alta velocidad para disparar acciones en milisegundos. Arquitectura backend modular y ligera.</td>
      <td align="left">Ecosistema corporativo extremadamente robusto. Capacidad analítica profunda con gran volumen de datos.</td>
      <td align="left">Control directo a nivel de hardware con latencia casi nula. Localmente sin dependencia de internet.</td>
      <td align="left">Costo de adquisición casi nulo. No requiere configuración de bases de datos ni infraestructura de red.</td>
    </tr>
    <tr>
      <td align="left"><strong>Debilidades</strong></td>
      <td align="left">Dependencia de la conectividad en planta. Marca nueva en el sector.</td>
      <td align="left">Costos de licencia altos. Despliegue muy lento al requerir la construcción de almacenes de datos complejos.</td>
      <td align="left">Requiere reprogramación rígida por cada nuevo equipo integrado.</td>
      <td align="left">Dependencia total del humano, generando demora en la respuesta.</td>
    </tr>
    <tr>
      <td align="left"><strong>Oportunidades</strong></td>
      <td align="left">Preferencia por soluciones SaaS de integración rápida.</td>
      <td align="left">Absorber corporaciones multinacionales que buscan unificar sus operaciones globales.</td>
      <td align="left">Integración con maquinaria pesada antigua que aún requiere protocolos cableados.</td>
      <td align="left">Talleres o microempresas sin presupuesto que solo buscan cumplir el requisito mínimo de tener un equipo físico.</td>
    </tr>
    <tr>
      <td align="left"><strong>Amenazas</strong></td>
      <td align="left">Interferencia electromagnética que cause pérdida de paquetes de datos.</td>
      <td align="left">Startups ágiles con APIs más modernas y económicas.</td>
      <td align="left">Migración de la industria hacia arquitecturas de microservicios e IoT en la nube, dejando obsoletos los sistemas cerrados.</td>
      <td align="left">Nuevas normativas que prohíban los registros manuales en papel para validaciones de salud ocupacional.</td>
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


Las entrevistas fueron grabadas en video previo consentimiento de los participantes y se organizaron por segmento objetivo. Cada registro incluye los datos generales del entrevistado, la captura del video, el enlace de acceso, el timing dentro de la grabación consolidada, la duración y un resumen descriptivo de las respuestas obtenidas.

> Nota para el equipo: las celdas marcadas entre corchetes deben completarse con los datos reales de cada entrevista. Las capturas se colocan en assets/chapter-2/ respetando los nombres de archivo indicados en cada etiqueta de imagen.

<a id="s-2-2-2-1"></a>
#### 2.2.2.1. Segmento objetivo 1: Supervisor de Seguridad (App Móvil)

<a id="s-2-2-2-1-1"></a>
##### 2.2.2.1.1. Entrevista 1

<table border="1">
  <tr>
    <td width="40%">
      <b>Nombres y apellidos:</b> Anyeli Vilcapaza<br>
      <b>Edad:</b> 26 años<br>
      <b>Distrito:</b> Surco<br>
      <b>Ocupación:</b> Supervisora de Seguridad y Salud Ocupacional (SSOMA) de Planta<br>
      <b>Experiencia laboral:</b> 4 años en el sector industrial<br>
      <b>Área de trabajo:</b> Planta de producción (zonas de soldadura y procesos industriales)<br>
      <b>Tipo de establecimiento:</b> Fábrica metalmecánica<br>
      <b>Nivel tecnológico:</b> Básico / Intermedio<br>
      <b>Timing:</b> 00:00:00 - 00:07:20<br>
      <b>Duración:</b> 07:20<br>
      <b>Entrevistador:</b> Santiago Armando Baldeon
    </td>
    <td align="center">
      <img src="../assets/02-capitulo-ii/entrevistas/entrevista-supervisor-1.png" alt="Entrevista 1 - Supervisor de Seguridad" width="85%">
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <b>Enlace:</b>
      <a href="https://upcedupe-my.sharepoint.com/:v:/g/personal/u202319881_upc_edu_pe/IQDgMkxRgpj_SZWQGkOVH52TAWt6KcdsMqmX7T0vqytQdNY?nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJPbmVEcml2ZUZvckJ1c2luZXNzIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXciLCJyZWZlcnJhbFZpZXciOiJNeUZpbGVzTGlua0NvcHkifX0&e=SBHV8R">Ver entrevista en Microsoft Stream</a>
      <br><br>
      <b>Resumen:</b> La supervisora describe un proceso de monitoreo reactivo y manual: la planta cuenta con medidores fijos y puntuales de CO₂ y ruido que dejan "zonas ciegas" sin cobertura, y cuando se detecta una condición peligrosa, ella se entera por radio o porque alguien acude físicamente a avisarle, nunca mediante una alerta automática. Relata un incidente donde un extractor de la zona de soldadura falló y un operario llegó a marearse antes de que se activara cualquier respuesta; desde el aviso hasta resolver el problema (evacuar, buscar un medidor portátil en la oficina de mantenimiento, confirmar el nivel de CO₂ y activar el extractor de respaldo) pasaron unos 25 minutos, cuando con una alerta automática se habrían ganado al menos 15 minutos de anticipación. Tampoco existe forma de cruzar datos entre zonas, y la verificación post-incidente de que las medidas funcionaron es completamente manual: pasar lista, revisar medidores portátiles y redactar un reporte escrito, sin ningún registro automático auditable.
      <br><br>
      Sobre una futura aplicación móvil, espera ver de inmediato un resumen tipo semáforo (verde/amarillo/rojo) por zona, y al detectar una alerta roja necesita saber qué zona es, qué parámetro falló (CO₂, ruido o ambos), desde cuándo comenzó a subir y cuántas personas hay registradas trabajando ahí. Quiere un mapa digitalizado en tiempo real para ubicar el foco del problema sin depender de llamadas, y control manual remoto de extractores, sirenas o mamparas desde el celular para casos de fallo de sensores o escenarios no contemplados por la automatización. Exige que las alertas críticas tengan sonido y vibración distintivos, que no puedan silenciarse por accidente y que aparezcan con el teléfono bloqueado, diferenciándolas claramente de las alertas informativas. Se muestra receptiva a adoptar la tecnología, motivada por pasar de un enfoque de "cero incidentes" a uno de "cero sorpresas".
    </td>
  </tr>
</table>

<a id="s-2-2-2-1-2"></a>
##### 2.2.2.1.2. Entrevista 2

<table border="1">
  <tr>
    <td width="40%">
      <b>Nombres y apellidos:</b> [Nombres y apellidos]<br>
      <b>Edad:</b> [Edad] años<br>
      <b>Distrito:</b> [Distrito]<br>
      <b>Ocupación:</b> [Puesto exacto]<br>
      <b>Experiencia laboral:</b> [Años de experiencia] en el sector industrial<br>
      <b>Área de trabajo:</b> [Área]<br>
      <b>Tipo de establecimiento:</b> [Tipo de planta]<br>
      <b>Nivel tecnológico:</b> [Básico / Intermedio / Avanzado]<br>
      <b>Timing:</b> [hh:mm:ss - hh:mm:ss]<br>
      <b>Duración:</b> [mm:ss]<br>
      <b>Entrevistador:</b> [Nombre del integrante del Grupo 03]
    </td>
    <td align="center">
      <img src="assets/chapter-2/entrevista-supervisor-2.png" alt="Entrevista 2 - Supervisor de Seguridad" width="85%">
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <b>Enlace:</b>
      <a href="[URL del video en Microsoft Stream]">[Ver entrevista en Microsoft Stream]</a>
      <br><br>
      <b>Resumen:</b> [Descripción de su flujo de trabajo actual, problemas de comunicación en la planta, respuesta ante emergencias ambientales y disposición para utilizar una aplicación móvil de alertas automáticas.]
    </td>
  </tr>
</table>

<a id="s-2-2-2-1-3"></a>
##### 2.2.2.1.3. Entrevista 3

<table border="1">
  <tr>
    <td width="40%">
      <b>Nombres y apellidos:</b> Diego Ruiz del Solar<br>
      <b>Edad:</b> 28 años<br>
      <b>Distrito:</b> Callao<br>
      <b>Ocupación:</b> Supervisor de seguridad industrial<br>
      <b>Experiencia laboral:</b> 3 años en el sector industrial<br>
      <b>Área de trabajo:</b> Planta de ensamblaje y producción<br>
      <b>Tipo de establecimiento:</b> Planta de ensamblaje y producción<br>
      <b>Nivel tecnológico:</b> Básico<br>
      <b>Timing:</b> 00:00:00 - 00:06:16<br>
      <b>Duración:</b> 06:16<br>
      <b>Entrevistador:</b> Santiago Alonso Gordillo Ramos
    </td>
    <td align="center">
      <img src="../assets/02-capitulo-ii/entrevistas/entrevista-supervisor-3.jpeg" alt="Entrevista 3 - Diego Ruiz del Solar, Supervisor de Seguridad" width="85%">
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <b>Enlace:</b>
      <a href="https://upcedupe-my.sharepoint.com/:v:/g/personal/u202215160_upc_edu_pe/IQB8eUTe-4fqT5HM2dtXNVpxAbgPiOEQps-5yLaMtsDK22g?e=dcyOZL&nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJTdHJlYW1XZWJBcHAiLCJyZWZlcnJhbFZpZXciOiJTaGFyZURpYWxvZy1MaW5rIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXcifX0%3D">Ver entrevista en Microsoft Stream</a>
      <br><br>
      <b>Resumen:</b> El trabajo de Diego consiste de rondas de manera presencial y mediciones manuales tradicionales, lo que genera margen de error en la detección de gases y ruidos. Ante situaciones de peligro, la respuesta es lenta y se pierde tiempo crítico en traslados para accionar algún tablero físico.
      <br><br>
      Le parece una grata idea contar con una aplicación móvil, destacando la opción del mapa de calor en tiempo real, alertas vibratorias persistentes y la opción de control remoto de mitigadores para actuar ante incidentes impredecibles que requieren intervención del personal antes de que la automatización se ejecute.
    </td>
  </tr>
</table>

<a id="s-2-2-2-2"></a>
#### 2.2.2.2. Segmento objetivo 2: Encargado de Planta (App Web)

<a id="s-2-2-2-2-1"></a>
##### 2.2.2.2.1. Entrevista 1

<table border="1">
  <tr>
    <td width="40%">
      <b>Nombres y apellidos:</b> Fabrizio Buselleu<br>
      <b>Edad:</b> 28 años<br>
      <b>Distrito:</b> Lurín<br>
      <b>Ocupación:</b> Gerente de Operaciones / Jefe de Planta, Metalúrgica del Pacífico S.A. (MEPSA)<br>
      <b>Experiencia laboral:</b> 3 en gestión industrial<br>
      <b>Área de trabajo:</b> Oficina técnica / Control de operaciones<br>
      <b>Tipo de establecimiento:</b> Fundición y procesamiento de metales no ferrosos (cobre y zinc), con línea secundaria de tratamiento térmico y soldadura industrial para piezas estructurales destinadas a minería — Parque Industrial de Lurín<br>
      <b>Nivel tecnológico:</b> Intermedio<br>
      <b>Timing:</b> 00:00 - 9:59 <br>
      <b>Duración:</b> 9:59 <br>
      <b>Entrevistador:</b> Santiago Armando Baldeon
    </td>
    <td align="center">
      <img src="../assets/02-capitulo-ii/entrevistas/entrevista-encargado-1.png" alt="Entrevista 1 - Encargado de Planta" width="85%">
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <b>Enlace:</b>
      <a href="https://upcedupe-my.sharepoint.com/:v:/g/personal/u202319881_upc_edu_pe/IQAhj6V5o_7xTq1Y6UaKEpQMAQP3gcRDCNbpvQjGy2mHFiM?nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJPbmVEcml2ZUZvckJ1c2luZXNzIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXciLCJyZWZlcnJhbFZpZXciOiJNeUZpbGVzTGlua0NvcHkifX0&e=9b1b0f">Ver entrevista en Microsoft Stream</a>
      <br><br>
      <b>Resumen:</b> Fabrizio enfoca su gestión no solo en el cumplimiento normativo para evitar multas, sino en reducir los tiempos muertos por paradas de seguridad, que hoy le cuestan entre 40 minutos y 2 horas de producción cada vez que se dispara una alarma y hay que evacuar o detener una línea. Su meta a cinco años es reducir en 50% los incidentes ambientales y tener cero observaciones en auditorías de SUNAFIL por exposición a gases o ruido. Actualmente, el proceso de dar de alta un sensor nuevo es completamente manual (Excel, coordinación con mantenimiento, configuración manual de zona/umbral/destinatario de alerta), lo que ha generado sensores "huérfanos" que dejan de reportar sin que nadie lo note. A esto se suman desafíos físicos propios de una planta de fundición: degradación de señal WiFi por las estructuras metálicas del horno, sensores que se desalinean por vibración de maquinaria pesada, y puntos de medición de CO₂ cercanos a fuentes de calor que no todos los sensores comerciales soportan. Las actualizaciones normativas también se gestionan de forma manual, sensor por sensor, lo cual es lento y riesgoso si se omite alguno. Relata además un incidente donde tres sensores de la Zona B estuvieron caídos casi 6 horas sin que nadie lo detectara hasta el cambio de turno, dejando a la planta "operando a ciegas" en CO₂ durante ese periodo — al reportarlo a gerencia, no pudo responder con certeza si algo había ocurrido durante ese lapso.
      <br><br>
      Frente a un panel web centralizado, se muestra muy receptivo: quiere visualizar todos los sensores en un mapa de planta (no en tablas), con colores según estado, poder configurar umbrales de decibeles y ppm de CO₂ sin depender de soporte técnico —aunque restringiría este permiso solo a sí mismo y al jefe de SSOMA corporativo, dado el riesgo de que un supervisor baje un umbral indebidamente—, y contar con notificaciones configurables por severidad y rol para no saturarse de alertas irrelevantes. Considera fundamental un registro histórico y de auditoría con al menos 12 meses de retención, tanto para responder a requerimientos de SUNAFIL como para reconstruir incidentes o denuncias y detectar patrones anómalos en el proceso. Anticipa que la exportación de reportes en PDF y la automatización de estos registros impactarían positivamente su productividad y facilitarían considerablemente las auditorías externas, reduciendo el trabajo manual y el riesgo de errores humanos que hoy enfrenta.
    </td>
  </tr>
</table>

<a id="s-2-2-2-2-2"></a>
##### 2.2.2.2.2. Entrevista 2

<table border="1">
  <tr>
    <td width="40%">
      <b>Nombres y apellidos:</b> Carlos Mendoza<br>
      <b>Edad:</b> 28 años<br>
      <b>Distrito:</b> Ate<br>
      <b>Ocupación:</b> Encargado de Planta<br>
      <b>Experiencia laboral:</b> 4 años en gestión industrial<br>
      <b>Área de trabajo:</b> Gerencia de Operaciones y Mantenimiento<br>
      <b>Tipo de establecimiento:</b> Planta de Manufactura<br>
      <b>Nivel tecnológico:</b> Intermedio / Avanzado<br>
      <b>Timing:</b> 00:00:00 - 00:07:55<br>
      <b>Duración:</b> 07:55<br>
      <b>Entrevistador:</b> Santiago Alonso Gordillo Ramos
    </td>
    <td align="center">
      <img src="../assets/02-capitulo-ii/entrevistas/entrevista-encargado-2.jpeg" alt="Entrevista 2 - Carlos Mendoza, Encargado de Planta" width="85%">
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <b>Enlace:</b> <a href="https://upcedupe-my.sharepoint.com/:v:/g/personal/u202215160_upc_edu_pe/IQCDpfLyPE3JSbAYwBJjdvnCAegV0RnbcJdQn_prFi3eCJU?e=B84siT&nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJTdHJlYW1XZWJBcHAiLCJyZWZlcnJhbFZpZXciOiJTaGFyZURpYWxvZy1MaW5rIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXcifX0%3D">Ver entrevista en Microsoft Stream</a>
      <br><br>
      <b>Resumen:</b> El problema principal que comenta es la enorme pérdida de tiempo tratando de organizar datos ambientales que se encuentran dispersos para poder generar reportes. Sufre de frustraciones y estrés por la dificultad de tener que actualizar máquina por máquina y la falta de permisos. Sus expectativas sobre una plataforma web se centran en tener un dashboard donde pueda controlar de manera general la información de los sensores IoT con las mitigaciones automáticas, permitiendo exportar reportes de manera sencilla y configurar los límites legales de forma centralizada.
    </td>
  </tr>
</table>

<a id="s-2-2-2-2-3"></a>
##### 2.2.2.2.3. Entrevista 3

<table border="1">
  <tr>
    <td width="40%">
      <b>Nombres y apellidos:</b> Nathaly Solano Armas<br>
      <b>Edad:</b> 28 años<br>
      <b>Distrito:</b> Ate<br>
      <b>Ocupación:</b> Encargada de planta<br>
      <b>Experiencia laboral:</b> 6 años en gestión industrial<br>
      <b>Área de trabajo:</b> Monitoreo y control de planta<br>
      <b>Tipo de establecimiento:</b> Planta metalmecánica de tamaño medio<br>
      <b>Nivel tecnológico:</b> Intermedio<br>
      <b>Timing:</b> 00:00:00 - 00:11:06<br>
      <b>Duración:</b> 11:06<br>
      <b>Entrevistador:</b> Angelo Héctor Solano Armas
    </td>
    <td align="center">
      <img src="../assets/02-capitulo-ii/entrevistas/entrevista-encargado-3.jpg" alt="Entrevista 3 - Nathaly Solano Armas, Encargada de Planta" width="85%">
    </td>
  </tr>
  <tr>
    <td colspan="2">
      <b>Enlace:</b> <a href="https://upcedupe-my.sharepoint.com/:v:/g/personal/u20231b775_upc_edu_pe/IQC3qQs5We4vS6zsu7M-w2DgATcBFhIcHwh6Y3EL3vL9im8?nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJPbmVEcml2ZUZvckJ1c2luZXNzIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXciLCJyZWZlcnJhbFZpZXciOiJNeUZpbGVzTGlua0NvcHkifX0&e=frhwHe">Ver entrevista en Microsoft Stream</a>
      <br><br>
      <b>Resumen:</b> Para Nathaly, la planta debe dejar de reaccionar cuando ya hay personal expuesto: el monitoreo continuo y la automatización deben bajar el tiempo de respuesta ante CO₂ y ruido, reducir alertas críticas con ventilación preventiva y dejar evidencia para auditorías, en lugar de depender de recorridos manuales. Lo que más le quita tiempo es armar reportes a mano, alinear umbrales entre turnos, dar altas y bajas de acceso y coordinar sensores caídos; configurar equipos en papel o Excel no escala entre áreas como soldadura, compresores y calderas.
      <br><br>
      Registrar sensores o actuadores falla si no se asocian al área correcta y al tipo de dispositivo (CO₂, ruido, PIR, extractor, sirena o mampara); identificadores duplicados, firmware distinto y zonas sin señal desarman el inventario. Los umbrales no son únicos: varían por espacio, tipo de ruido y presencia de personal; un tope mal calibrado no dispara o satura de falsas alertas. En la web exige dashboard por área, historial de mediciones, alertas y acciones, usuarios y roles, y trazabilidad de quién cambió la configuración; el control de actuadores lo deja al supervisor en el celular. Solo otorga rol de supervisor a quien opera seguridad en campo. Las normas llegan por correo o PDF, se traducen a Excel y se copian tarde a cada zona, por lo que quiere actualizar parámetros con versión y fecha. Una caída de internet o de un ESP32 le quita visibilidad y evidencia ante SST: el sistema debe marcar el dispositivo como no disponible y aguantar offline en el gateway. El historial es crítico para auditorías, overrides y patrones por área. Automatizaría la aplicación de umbrales por norma y el armado del reporte de eventos.
    </td>
  </tr>
</table>

<a id="s-2-2-3"></a>
### 2.2.3. Análisis de entrevistas

| Entrevistado | Segmento | Tipo de planta | Nivel tecnológico | Duración |
|---|---|---|---|---|
| Anyeli Vilcapaza | Supervisora SSOMA | Fábrica metalmecánica (soldadura y procesos) | Básico / Intermedio | 07:20 |
| Diego Ruiz del Solar | Supervisor de seguridad industrial | Planta de ensamblaje y producción | Básico | 06:16 |
| Fabrizio Buselleu | Gerente de operaciones / jefe de planta | Fundición y metales no ferrosos (MEPSA) | Intermedio | 09:59 |
| Carlos Mendoza | Encargado de planta | Planta de manufactura | Intermedio / Avanzado | 07:55 |
| Nathaly Solano Armas | Encargada de planta | Planta metalmecánica de tamaño medio | Intermedio | 11:06 |

La muestra cubre metalmecánica, fundición y ensamblaje, con madurez tecnológica de básica a intermedia-avanzada. Eso evita un sesgo de una sola planta “ideal” y permite distinguir lo que es común al rol de lo que es propio del contexto físico (interferencia metálica, calor, vibración).

<a id="s-2-2-3-1"></a>
#### 2.2.3.1. Hallazgos del segmento Supervisor de Seguridad

En campo el monitoreo actual es **reactivo y presencial**. Anyeli se entera de un riesgo por radio o porque alguien llega a avisarle; no existe alerta automática ni cruce de datos entre áreas. Diego recorre la planta con mediciones manuales, con margen de error en gases y ruido, y pierde tiempo crítico al desplazarse hasta un tablero físico para accionar un mitigador. El incidente relatado por Anyeli cuantifica el costo de ese modelo: un extractor de soldadura falló, un operario se mareó y el ciclo aviso–evacuar–medir con portátil–activar respaldo tomó unos **25 minutos**; ella estima que una alerta automática habría adelantado al menos **15 minutos**.

La verificación post-incidente también es manual (pasar lista, revisar medidores, redactar un reporte) y no deja rastro auditable. Ambos supervisores coinciden en la forma de la solución móvil:

- Un **mapa o semáforo en tiempo real** (verde / amarillo / rojo o mapa de calor) para ubicar el foco sin llamadas.
- En alerta roja: **área, parámetro (CO₂, ruido o ambos), desde cuándo sube y si hay personal** en el lugar.
- **Override remoto** de extractores, sirenas o mamparas cuando el sensor falla o el escenario no está cubierto por la automatización.
- Alertas críticas con **sonido y vibración persistentes**, visibles con el teléfono bloqueado y distintas de las informativas.

Anyeli formula el cambio de mentalidad que el producto debe sostener: pasar de “cero incidentes” a **“cero sorpresas”**. Diego refuerza que la automatización no reemplaza al supervisor: necesita intervenir *antes* de que la regla automática se ejecute cuando el evento es impredecible.

<a id="s-2-2-3-2"></a>
#### 2.2.3.2. Hallazgos del segmento Encargado de Planta

El encargado no recorre la planta: **gobierna, parametriza y rinde cuentas**. Los tres entrevistados describen un backoffice fragmentado en Excel, papel, correo y coordinación con mantenimiento.

Fabrizio mide el problema en dinero y tiempo de línea: cada alarma que obliga a evacuar o parar le cuesta entre **40 minutos y 2 horas** de producción. Su meta a cinco años es bajar 50 % los incidentes ambientales y llegar a **cero observaciones SUNAFIL** por gases o ruido. El alta de un sensor es manual (zona, umbral, destinatario) y ha producido **sensores huérfanos**; en un caso, tres sensores de la Zona B estuvieron caídos **casi seis horas** sin que nadie lo notara hasta el cambio de turno, y no pudo responder a gerencia si algo ocurrió en ese lapso. Añade restricciones físicas de fundición: Wi-Fi degradada por estructuras metálicas, desalineación por vibración y puntos de CO₂ cerca de calor.

Carlos resume el mismo dolor en productividad gerencial: datos ambientales dispersos, estrés por actualizar **máquina por máquina** y falta de permisos. Espera un dashboard que unifique sensores y mitigaciones, exporte reportes y centralice límites legales.

Nathaly cierra el ciclo operativo. Quiere dejar de reaccionar cuando el personal ya está expuesto: monitoreo continuo, ventilación preventiva y evidencia para auditorías. Le quitan tiempo armar reportes a mano, alinear umbrales entre turnos, dar altas y bajas de acceso y coordinar dispositivos caídos. El inventario se rompe si el sensor o actuador no se asocia al **área correcta y al tipo** (CO₂, ruido, PIR, extractor, sirena, mampara). Los umbrales **no son únicos**: varían por espacio, tipo de ruido y presencia de personal; un tope mal calibrado no dispara o satura de falsas alertas. Las normas llegan por correo o PDF, se copian tarde a cada área y quiere versionar parámetros con fecha. Una caída de internet o de un ESP32 le quita visibilidad ante SST: el sistema debe marcar el dispositivo como no disponible y **aguantar offline en el gateway**.

Los tres encargados piden la misma superficie web: dashboard (mapa o por área, no solo tablas), configuración de umbrales sin soporte técnico, exportación de reportes (PDF) e **historial / auditoría** (Fabrizio pide al menos 12 meses). En permisos hay consenso de control: Fabrizio restringiría umbrales a él y al jefe SSOMA corporativo; Nathaly solo otorga rol de supervisor a quien opera seguridad en campo y deja el control de actuadores al celular del supervisor.

<a id="s-2-2-3-3"></a>
#### 2.2.3.3. Patrones transversales y divergencias de rol

| Tema | Evidencia | Implicación para SafePlant |
|---|---|---|
| Visibilidad en tiempo real por área | Zonas ciegas (Anyeli); rondas manuales (Diego); sensores caídos 6 h (Fabrizio); ESP32 offline (Nathaly) | Telemetría continua de CO₂, ruido y presencia; estado “no disponible” del dispositivo; semáforo / mapa en móvil y dashboard en web |
| Tiempo de respuesta | 25 min de ciclo en soldadura (Anyeli); traslado a tablero (Diego); paradas de 40 min–2 h (Fabrizio) | Detección + actuación automática de extractores, sirenas y mamparas; override remoto desde el móvil |
| Configuración manual que no escala | Excel y alta sensor a sensor (Fabrizio, Carlos, Nathaly); normas por correo/PDF (Nathaly) | App web para umbrales por área, inventario de dispositivos y versión / fecha de la norma |
| Umbrales y falsos positivos | Umbrales distintos por área y presencia (Nathaly); riesgo de bajar un tope (Fabrizio) | Umbrales por área, no globales; permiso de configuración solo en el encargado; correlación con PIR |
| Auditoría y reportes | Reporte escrito post-incidente (Anyeli); 12 meses y SUNAFIL (Fabrizio); datos dispersos (Carlos); overrides y patrones (Nathaly) | Historial de mediciones, alertas, acciones y cambios de configuración; exportación PDF |
| Canal según el rol | Móvil para decidir y actuar (Anyeli, Diego); web para gobernar (Fabrizio, Carlos, Nathaly) | Separación estricta: supervisor opera y hace override en móvil; encargado parametriza, usuarios y reportes en web |
| Resiliencia de planta | Wi-Fi metálica y calor (Fabrizio); offline de gateway (Nathaly) | Procesamiento en el edge, persistencia local y sincronización al recuperar enlace |

La divergencia más útil para el diseño no es de “gusto de interfaz”, sino de **responsabilidad**. El supervisor necesita decidir en segundos con el teléfono en la mano; el encargado necesita que nadie más rebaje un umbral y que un auditor pueda reconstruir qué pasó. SafePlant debe impedir que esas dos intenciones se mezclen en el mismo canal.

<a id="s-2-2-3-4"></a>
#### 2.2.3.4. Contrastación con las hipótesis Lean UX

Las entrevistas **confirman y precisan** las tres hipótesis del Capítulo I:

1. **Automatización preventiva.** El incidente del extractor y la demanda de Nathaly de ventilar antes de que haya personal expuesto sostienen la hipótesis de detectar CO₂/ruido y accionar extractores sin esperar un recorrido. Se añade una condición de diseño: la automatización debe convivir con override manual, no sustituirlo.
2. **Monitoreo remoto ágil.** Anyeli y Diego validan alertas inmediatas y control de mitigadores desde el móvil. El umbral “menos de 1 minuto” es creíble frente a los 25 minutos actuales, siempre que la alerta crítica no se pueda silenciar por accidente.
3. **Parametrización y cumplimiento.** Fabrizio, Carlos y Nathaly validan el panel web de umbrales, dashboard e histórico. La hipótesis de +30 % de eficiencia gerencial se ancla en dos tareas que hoy son manuales y que los tres automatizarían: aplicar la norma a todas las áreas y armar el reporte de eventos.

Quedan supuestos abiertos, no refutados: la magnitud exacta del 90 % de reducción de exposición y del 40 % menos de alertas críticas exige medición en piloto; la interferencia industrial (metal, calor, vibración) es un riesgo de infraestructura, no de discurso de usuario.

<a id="s-2-2-3-5"></a>
#### 2.2.3.5. Insights que alimentan el needfinding y el EventStorming

Del análisis se retienen cinco decisiones de dominio que luego aparecen en personas, journeys y en el Big Picture EventStorming:

1. La unidad de control no es “la planta” ni un mapa cartográfico: es el **área industrial** (soldadura, compresores, calderas, fundición) con umbral, dispositivos y personal propios.
2. Un valor ambiental sin **presencia** no tiene la misma urgencia que un valor con personal expuesto; por eso el PIR entra al lenguaje del supervisor.
3. El evento de negocio no termina en “se superó el umbral”: termina cuando se **actuó**, se verificó y quedó **evidencia**.
4. Un dispositivo que deja de reportar es tan grave como un exceso no detectado: debe existir el hecho “sensor no disponible”.
5. Identidad y permisos son parte del problema de seguridad ocupacional: mal rol o umbral editable por cualquiera convierte la plataforma en un riesgo.

Estos insights cierran el ciclo de elicitación: las entrevistas no solo describen frustraciones, sino que delimitan agregados y contextos (sesión y acceso, configuración de planta, ingesta de telemetría, detección y actuación) que se desarrollan en 2.3 y 2.4.

<a id="s-2-3"></a>
## 2.3. Needfinding

Para llevar a cabo el proceso de needfinding en Macallys, se realizaron entrevistas en profundidad con usuarios pertenecientes a los segmentos objetivo del proyecto: supervisores de seguridad industrial y encargados de planta en empresas manufactureras y de industria pesada. Estas conversaciones se centraron en comprender sus hábitos, objetivos y principales frustraciones relacionadas con el monitoreo ambiental, la prevención de riesgos y el cumplimiento de normativas de seguridad ocupacional.

Gracias a esta exploración, se identificaron áreas críticas de mejora, como la falta de visibilidad en tiempo real de las condiciones ambientales en zonas críticas, la dependencia de revisiones manuales esporádicas y la limitada capacidad de reacción automática ante niveles peligrosos de CO2 y ruido. Asimismo, se evidenció la existencia de brechas tecnológicas que retrasan la respuesta ante incidentes y dificultan la elaboración de reportes para auditorías. Durante las entrevistas, surgieron patrones y necesidades recurrentes, como la importancia de contar con un sistema que centralice la información, automatice la mitigación de riesgos y permita el control remoto desde dispositivos móviles y web. De esta manera, se logra identificar una oportunidad clara para desarrollar una solución como Macallys, que facilite la prevención automatizada y mejore la seguridad y el bienestar de los operarios en plantas industriales.

<a id="s-2-3-1"></a>
### 2.3.1. User Personas

Segmento Objetivo: Supervisor de Seguridad:

![User Persona](../assets/02-capitulo-ii/needfinding/persona-1.png)

Segmento Objetivo: Encargado de Planta:

![User Persona](../assets/02-capitulo-ii/needfinding/persona-2.png)

<a id="s-2-3-2"></a>
### 2.3.2. User Task Matrix

| Task | Carlos Ramírez (Supervisor de Seguridad) — Frecuencia | Carlos Ramírez (Supervisor de Seguridad) — Importancia | Rosa Delgado (Encargado de Planta) — Frecuencia | Rosa Delgado (Encargado de Planta) — Importancia |
|---|---|---|---|---|
| Monitorear niveles de CO2 y ruido en tiempo real | Alta | Alta | Media | Alta |
| Recibir alertas push ante niveles peligrosos | Alta | Alta | Media | Alta |
| Accionar mitigadores a distancia (bocinas, mamparas) | Alta | Alta | Baja | Media |
| Verificar uso de protección auditiva del personal | Alta | Alta | Baja | Media |
| Configurar umbrales de CO2 y decibeles por zona | Baja | Media | Alta | Alta |
| Revisar historial de datos ambientales | Media | Alta | Alta | Alta |
| Generar reportes para auditorías (SUNAFIL) | Baja | Media | Alta | Alta |
| Gestionar actualizaciones del software de sensores | Baja | Baja | Alta | Media |
| Coordinar con otros supervisores/encargados | Alta | Alta | Media | Alta |
| Detectar fallas o desconexión de sensores | Media | Alta | Media | Alta |
| Evaluar cumplimiento normativo de la planta | Baja | Media | Alta | Alta |
| Recorrer físicamente las zonas críticas | Alta | Alta | Baja | Baja |

<a id="s-2-3-3"></a>
### 2.3.3. User Journey Mapping

Segmento Objetivo: Supervisor de Seguridad:

![User Journey Map](../assets/02-capitulo-ii/needfinding/user-journey-map-1.png)

Segmento Objetivo: Encargado de Planta:

![User Journey Map](../assets/02-capitulo-ii/needfinding/user-journey-map-2.png)

<a id="s-2-3-4"></a>
### 2.3.4. Empathy Mapping

Segmento Objetivo: Supervisor de Seguridad:

![Empathy Map](../assets/02-capitulo-ii/needfinding/empathy-map-1.png)

Segmento Objetivo: Encargado de Planta:

![Empathy Map](../assets/02-capitulo-ii/needfinding/empathy-map-2.png)

<a id="s-2-4"></a>
## 2.4. Big Picture EventStorming

A partir de las entrevistas, personas y journeys del needfinding, el equipo realizó una sesión de **Big Picture EventStorming** para descubrir el lenguaje del dominio SafePlant. Se trabajó sobre un mismo [tablero digital en Miro](https://miro.com/app/board/uXjVHoeD1bM=/?share_link_id=724295404821), avanzando por capas: primero eventos, luego orden temporal, hotspots, pivotes, comandos, políticas, read models, sistemas externos, agregados y, finalmente, candidatos a bounded contexts. El resultado agrupa el flujo en cuatro bloques: Accounts and Sessions, Plant Setup, Sensing and Ingest, y Risk Detection and Actuation.

**Tablero Miro:** [Big Picture EventStorming — SafePlant](https://miro.com/app/board/uXjVHoeD1bM=/?share_link_id=724295404821)

![Big Picture EventStorming — vista general](../assets/02-capitulo-ii/eventstorming/big-picture-eventstorming.png)

**Paso 1 — Unstructured Exploration**

Se volcaron en notas amarillas todos los hechos de dominio relevantes sin imponer aún un orden estricto: autenticación de supervisor y encargado, configuración de áreas e umbrales, lecturas de CO₂/ruido, alertas ambientales y actuación de extractores, sirenas y barreras acústicas.

![Big Picture EventStorming — Paso 1: Unstructured Exploration](../assets/02-capitulo-ii/eventstorming/Storming%20-%20Step%201_%20Unstructured%20Exploration.jpg)

**Paso 2 — Timelines**

Los eventos se reordenaron en líneas temporales por flujo de negocio, dejando visible la secuencia desde el acceso de usuarios hasta la resolución de una exposición, pasando por configuración de planta e ingesta de telemetría.

![Big Picture EventStorming — Paso 2: Timelines](../assets/02-capitulo-ii/eventstorming/Storming%20-%20Step%202_%20Timelines.jpg)

**Paso 3 — Pain Points**

Se marcaron hotspots (rombos rosados) sobre dudas e incertidumbre: tokens por aplicación, fallos de umbrales, sensores offline o con mala señal, y qué ocurre si falla la activación de extractores o sirenas.

![Big Picture EventStorming — Paso 3: Pain Points](../assets/02-capitulo-ii/eventstorming/Storming%20-%20Step%203_%20Pain%20Points.jpg)

**Paso 4 — Pivotal Points**

Se identificaron los puntos pivote del dominio: cambios de estado que concentran decisión o riesgo (por ejemplo, exceso detectado, alerta generada, actuador activado o exposición resuelta) y que conectan un flujo con el siguiente.

![Big Picture EventStorming — Paso 4: Pivotal Points](../assets/02-capitulo-ii/eventstorming/Storming%20-%20Step%204_%20Pivotal%20Points.jpg)

**Paso 5 — Commands**

Sobre cada evento se añadieron los comandos (notas azules/verdes) que lo provocan: iniciar sesión, configurar umbrales, asociar sensores, registrar lecturas, evaluar riesgo y activar o anular mitigadores.

![Big Picture EventStorming — Paso 5: Commands](../assets/02-capitulo-ii/eventstorming/Storming%20-%20Step%205_%20Commands.jpg)

**Paso 6 — Policies**

Se documentaron las políticas de reacción automática: si se detecta exceso de CO₂ o ruido, entonces generar alerta y disparar extractores, sirenas o barreras según la severidad y la configuración de la zona.

![Big Picture EventStorming — Paso 6: Policies](../assets/02-capitulo-ii/eventstorming/Storming%20-%20Step%206_%20Policies.jpg)

**Paso 7 — Read Models**

Se identificaron las vistas que necesitan supervisor y encargado para decidir: mapa de zonas con riesgo, histórico de lecturas, estado de actuadores, umbrales vigentes y resumen de alertas abiertas o resueltas.

![Big Picture EventStorming — Paso 7: Read Models](../assets/02-capitulo-ii/eventstorming/Storming%20-%20Step%207_%20Read%20Models.jpg)

**Paso 8 — External Systems**

Se explicitaron dependencias externas al núcleo del dominio: dispositivos edge/sensores, brokers o colas de telemetría, notificaciones push y, cuando aplique, servicios de identidad o almacenamiento fuera del tablero principal.

![Big Picture EventStorming — Paso 8: External Systems](../assets/02-capitulo-ii/eventstorming/Storming%20-%20Step%208_%20External%20Systems.jpg)

**Paso 9 — Aggregates**

Los comandos y eventos se agruparon en agregados candidatos (cuenta/sesión, área industrial, dispositivo, telemetría, alerta/exposición, actuador), delimitando qué invariantes deben mantenerse juntos.

![Big Picture EventStorming — Paso 9: Aggregates](../assets/02-capitulo-ii/eventstorming/Storming%20-%20Step%209_%20Aggregates.jpg)

**Paso 10 — Bounded Contexts**

Finalmente se encerraron los bloques del tablero como candidatos a bounded contexts: Accounts and Sessions, Plant Setup, Sensing and Ingest, y Risk Detection and Actuation, base del diseño estratégico del Capítulo IV.

![Big Picture EventStorming — Paso 10: Bounded Contexts](../assets/02-capitulo-ii/eventstorming/Storming%20-%20Step%2010_%20Bounded%20Contexts.jpg)

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
      <td align="left">CO2 (Dióxido de carbono)</td>
      <td align="left">Gas cuya acumulación en espacios confinados representa riesgo respiratorio para el personal.</td>
      <td align="left">Se monitorea en tiempo real mediante sensores en zonas críticas.</td>
    </tr>
    <tr>
      <td align="left">Sensor de CO2</td>
      <td align="left">Dispositivo IoT que mide la concentración de dióxido de carbono en una zona.</td>
      <td align="left">Envía datos a la plataforma para activar alertas o mitigadores.</td>
    </tr>
    <tr>
      <td align="left">Sonómetro</td>
      <td align="left">Dispositivo que mide el nivel de contaminación sonora (decibeles) en una zona.</td>
      <td align="left">Utilizado para detectar exceso de ruido por maquinaria pesada.</td>
    </tr>
    <tr>
      <td align="left">Detector de presencia</td>
      <td align="left">Sensor que identifica la presencia de operarios en zonas críticas.</td>
      <td align="left">Permite activar bocinas o mamparas solo cuando hay personal expuesto.</td>
    </tr>
    <tr>
      <td align="left">Umbral</td>
      <td align="left">Valor límite configurado (de CO2 o dB) a partir del cual el sistema activa una respuesta automática.</td>
      <td align="left">Definido por el Encargado de Planta desde la App Web.</td>
    </tr>
    <tr>
      <td align="left">Zona crítica</td>
      <td align="left">Área de la planta con alto riesgo ambiental (cuartos de máquinas, calderas, pasillos confinados).</td>
      <td align="left">Punto de instalación de sensores y actuadores.</td>
    </tr>
    <tr>
      <td align="left">Actuador</td>
      <td align="left">Mecanismo que ejecuta una acción física de mitigación (ventilador, bocina, mampara).</td>
      <td align="left">Se activa automáticamente al superarse un umbral.</td>
    </tr>
    <tr>
      <td align="left">Ventilador de extracción</td>
      <td align="left">Actuador que purifica el ambiente ante exceso de CO2.</td>
      <td align="left">Se activa automáticamente sin intervención humana.</td>
    </tr>
    <tr>
      <td align="left">Bocina preventiva</td>
      <td align="left">Actuador sonoro que alerta a los operarios expuestos a niveles peligrosos.</td>
      <td align="left">Puede ser accionada a distancia por el Supervisor de Seguridad.</td>
    </tr>
    <tr>
      <td align="left">Mampara de aislamiento</td>
      <td align="left">Actuador físico que aísla una zona de riesgo.</td>
      <td align="left">Se activa junto con la bocina en casos críticos.</td>
    </tr>
    <tr>
      <td align="left">Alerta push</td>
      <td align="left">Notificación inmediata enviada a la App Móvil ante una anomalía.</td>
      <td align="left">Recibida por el Supervisor de Seguridad en tiempo real.</td>
    </tr>
    <tr>
      <td align="left">App Móvil</td>
      <td align="left">Aplicación utilizada por el Supervisor de Seguridad para monitorear y actuar en campo.</td>
      <td align="left">Permite control remoto de los dispositivos IoT.</td>
    </tr>
    <tr>
      <td align="left">App Web</td>
      <td align="left">Plataforma utilizada por el Encargado de Planta para configurar el sistema y generar reportes.</td>
      <td align="left">Centraliza la parametrización y el historial de datos.</td>
    </tr>
    <tr>
      <td align="left">Procesamiento Edge</td>
      <td align="left">Procesamiento básico de datos realizado en el propio dispositivo IoT antes de enviarlos a la nube.</td>
      <td align="left">Mitiga riesgos de latencia en zonas con alta interferencia.</td>
    </tr>
    <tr>
      <td align="left">Reporte histórico</td>
      <td align="left">Documento generado por el sistema con datos ambientales pasados.</td>
      <td align="left">Usado por el Encargado de Planta para auditorías.</td>
    </tr>
    <tr>
      <td align="left">SUNAFIL</td>
      <td align="left">Entidad peruana que fiscaliza el cumplimiento de normativas de seguridad y salud en el trabajo.</td>
      <td align="left">Referente regulatorio que motiva el uso del sistema.</td>
    </tr>
    <tr>
      <td align="left">Supervisor de Seguridad</td>
      <td align="left">Usuario que monitorea en campo las condiciones ambientales mediante la App Móvil.</td>
      <td align="left">Segmento objetivo 1 de Macallys.</td>
    </tr>
    <tr>
      <td align="left">Encargado de Planta</td>
      <td align="left">Usuario que configura el sistema y gestiona el cumplimiento normativo desde la App Web.</td>
      <td align="left">Segmento objetivo 2 de Macallys.</td>
    </tr>
    <tr>
      <td align="left">Tiempo de exposición</td>
      <td align="left">Duración durante la cual un operario está expuesto a niveles peligrosos de CO2 o ruido.</td>
      <td align="left">Métrica clave que Macallys busca reducir en un 90%.</td>
    </tr>
  </tbody>
</table>

---

**Navegación:** [Índice](./00-student-outcome.md#s-tabla-contenidos) · Anterior: [Capítulo I](./01-capitulo-i-introduccion.md) · Siguiente: [Capítulo III](./03-capitulo-iii-requirements-specification.md)
