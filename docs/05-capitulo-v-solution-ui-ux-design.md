**Navegación:** [Índice](./00-student-outcome.md#s-tabla-contenidos) · Anterior: [Capítulo IV](./04-capitulo-iv-solution-software-design.md) · Siguiente: [Capítulo VI](./06-capitulo-vi-product-implementation.md)

---

<a id="s-cap-v"></a>
# Capítulo V: Solution UI/UX Design

<a id="s-5-1"></a>
## 5.1. Style Guidelines

<a id="s-5-1-1"></a>
### 5.1.1. General Style Guidelines

Para el desarrollo de SAFEPLANT elegimos cuidadosamente los colores que nos representarían, ya que conforman la paleta principal que el usuario visualizará al ingresar a la plataforma. Al tratarse de una solución de entrenamiento inteligente con un espejo conectado, buscamos colores que transmitan energía, motivación y confianza, pero que a la vez sean cómodos a la vista durante sesiones largas de ejercicio. Cada color cumple una función: los tonos principales guían la atención hacia las acciones importantes, los tonos claros aportan descanso visual y los tonos oscuros aseguran la legibilidad del texto.

![General Style Guidelines](<../assets/05-capitulo-v/style-guidelines/Style Guide_Sheet1 (1).png>)

<a id="s-5-1-2"></a>
### 5.1.2. Web, Mobile and IoT Style Guidelines

Para el diseño web, móvil y de los dispositivos IoT usamos la misma paleta de colores y tipografía, pues la consistencia permite que el usuario perciba continuidad entre las pantallas. Todos los elementos usan bordes redondeados de 10px para lograr un estilo amigable a la vista. Empleamos distintos tamaños de letra y variaciones de color para evitar la sobrecarga de información, y cuidamos que cada pantalla tenga un descanso visual adecuado.

**Headings:** del H1 al H6 definen la jerarquía de la información. El H1 se usa para el título principal de la página y el H6 para títulos pequeños dentro de secciones.

**Body text:** el texto de cuerpo usa 18px. Los párrafos van en Regular, el texto destacado en Bold, las citas en Italic y los enlaces se distinguen por su subrayado y color.

**Captions:** acompañan imágenes y tablas (por ejemplo, gráficos de [datos de sensores / monitoreo]) con un peso ExtraLight en cursiva para no competir con el contenido principal.

**Forms:** incluyen etiquetas, placeholders, mensajes de error (Bold y color de énfasis) y textos de ayuda, por ejemplo al registrarse o configurar un dispositivo.

**Buttons:** se definen tres tamaños de texto: primario (Bold, 24px), secundario (Regular, 24px) y pequeño (Regular, 20px). Los botones tienen tres estados (Normal, Hover y Clicked / Checked) que se oscurecen para dar retroalimentación inmediata.

**Caja de texto:** usa bordes de 10px, un ícono de búsqueda a la derecha y el texto guía "Ingrese texto aquí…".

**Ventanas desplegables y emergentes:** las desplegables agrupan opciones relacionadas (menús, filtros) con título, ítems separados por divisores y un botón de acción. Las emergentes mantienen la misma estructura, pero se muestran sobre un fondo atenuado para pedir confirmación o mostrar alertas importantes, como la [alerta de un sensor].


![General Style Guidelines](<../assets/05-capitulo-v/style-guidelines/Style Guide_Sheet1 (7).png>)
![General Style Guidelines](<../assets/05-capitulo-v/style-guidelines/Style Guide_Sheet1 (8).png>)
![General Style Guidelines](<../assets/05-capitulo-v/style-guidelines/Style Guide_Sheet1 (9).png>)
![General Style Guidelines](<../assets/05-capitulo-v/style-guidelines/Style Guide_Sheet1 (10).png>)
![General Style Guidelines](<../assets/05-capitulo-v/style-guidelines/Style Guide_Sheet1 (11).png>)
![General Style Guidelines](<../assets/05-capitulo-v/style-guidelines/Style Guide_Sheet1 (12).png>)
![General Style Guidelines](<../assets/05-capitulo-v/style-guidelines/Style Guide_Sheet1 (13).png>)
![General Style Guidelines](<../assets/05-capitulo-v/style-guidelines/Style Guide_Sheet1 (14).png>)
![General Style Guidelines](<../assets/05-capitulo-v/style-guidelines/Style Guide_Sheet1 (15).png>)
<a id="s-5-2"></a>


## 5.2. Information Architecture

<a id="s-5-2-1"></a>
### 5.2.1. Organization Systems

En nuestra plataforma SAFEPLANT, organizamos la información para que los usuarios puedan monitorear, analizar y controlar las condiciones ambientales de la planta de forma rápida y clara. La plataforma es utilizada por dos tipos de usuarios: el supervisor de seguridad, que consulta y configura el sistema desde la app móvil y la consola web, y el gerente de planta, que consulta los resultados desde la web. A continuación, explicamos los sistemas de organización que utilizamos en distintas secciones de la aplicación:

Utilizamos la **organización jerárquica** principalmente en el Panel de Control, donde destacamos primero los indicadores generales (nivel de CO₂, presión acústica y personal en zonas críticas), luego la matriz ambiental de zonas y finalmente la respuesta automatizada y el estado de los nodos IoT. Asimismo, también está presente en la pantalla de Alertas, donde los incidentes críticos tienen mayor relevancia visual que las advertencias y los mensajes informativos.

Por otro lado, aplicamos la **organización secuencial** en el ciclo de vida de un incidente, que sigue pasos consecutivos: detección del peligro, mitigación automática, pendiente de confirmación y, finalmente, resuelto o auditado. También se aplica en la configuración de umbrales, donde el supervisor selecciona una zona, ajusta el límite de CO₂ o de ruido y finalmente guarda el cambio.

Además, para la presentación de datos se utiliza una **organización matricial**, que permite visualizar y comparar varios elementos simultáneamente en una cuadrícula. Se aplica en la matriz ambiental de zonas, en la matriz comparativa de umbrales y en las tablas de alertas y de registro de incidentes.

En cuanto a la categorización, aplicamos la **organización por tópicos** para agrupar la información según el parámetro medido (CO₂, presión acústica y presencia de personal) y, en la sección Dispositivos, según su función: sensores de monitoreo y actuadores de control. También implementamos la **organización geográfica**, que divide la planta en zonas industriales y permite filtrar datos, alertas y dispositivos por zona. De igual forma, usamos la **organización alfabética** para ubicar zonas, nodos y eventos mediante sus códigos, y la **organización cronológica** para ordenar los incidentes y registros desde los más recientes hasta los más antiguos, además de permitir elegir la ventana temporal de las gráficas (1h, 6h, 12h y 24h).

Finalmente, aplicamos una **categorización por audiencia**. El supervisor de seguridad tiene acceso a todas las secciones y es el único que puede configurar umbrales, gestionar alertas y administrar dispositivos IoT. El gerente de planta accede únicamente en modo consulta al Panel de Control y al Historial, donde visualiza el dashboard, las gráficas y los resultados, sin posibilidad de modificar la configuración del sistema.



![Organization Systems](../assets/05-capitulo-v/information-architecture/organization-systems.png)


<a id="s-5-2-2"></a>
### 5.2.2. Labeling Systems

El sistema de etiquetado busca representar la información de forma clara y sin ambigüedades, usando etiquetas concisas de una a cuatro palabras, un lenguaje técnico reconocible para el personal de seguridad industrial y un estilo consistente en toda la plataforma. Cuando es necesario, las etiquetas se acompañan de íconos y de colores que refuerzan su significado. Las etiquetas utilizadas son:

- **Navegación principal:** Panel de Control, Umbrales, Alertas, Historial y Dispositivos. En la versión móvil se abrevian a Panel, Alertas, Umbrales, Historial y Equipos.
- **Niveles de severidad:** Crítico, Advertencia e Información. Se diferencian por color: rojo para crítico, amarillo para advertencia y azul para información.
- **Estados de lectura y zona:** Normal, Precaución y Elevado.
- **Estados del incidente:** Mitigación Activa, Pendiente de Confirmación, Normalizado y Resuelto / Auditado.
- **Estados de dispositivos y reglas:** En Línea, En Espera, Sincronizado, En Diagnóstico y Armada y Activa.
- **Botones de acción:** Reconocer, Aceptar, Filtrar, Exportar PDF, Reporte de Cumplimiento (PDF), Configurar Disparadores de Alerta, Guardar Límite de CO₂ y Guardar Límite de Ruido.
- **Parámetros y unidades:** CO₂ (PPM) y Presión Acústica (dBA), siempre acompañados de su límite normativo (por ejemplo, "Límite: 800 PPM").
- **Componentes de dispositivos:** Sensor de Sonido, Sensor de CO₂, Sensor de Movimiento, Ventilador de Extracción, Alarma Acústica y Mamparas de Seguridad.

Este lenguaje directo evita la sobrecarga de información y permite tomar decisiones rápidas ante una situación de riesgo.


<a id="s-5-2-3"></a>
### 5.2.3. SEO Tags and Meta Tags

Para la versión web de SAFEPLANT se definen las siguientes etiquetas base:

```html
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>SAFEPLANT | Telemetría de Seguridad Industrial</title>
```

Meta tags adicionales que pueden implementarse:

```html
<meta name="description" content="SAFEPLANT es una plataforma IoT que monitorea en tiempo real el CO₂, el ruido y la presencia de personal en zonas industriales, y activa respuestas automáticas de seguridad.">
<meta name="keywords" content="IoT, seguridad industrial, telemetría, CO2, ruido">
<meta property="og:title" content="SAFEPLANT | Telemetría de Seguridad Industrial">
<meta property="og:description" content="Monitoreo ambiental en tiempo real y mitigación automatizada en planta.">
<meta property="og:image" content="URL_imagen_destacada.jpg">
```

- `description` ofrece un resumen del proyecto para los buscadores.
- `keywords` ayuda a clasificar el tema de la plataforma.
- `og:title`, `og:description` y `og:image` controlan cómo se ve SAFEPLANT al compartirse en redes sociales.


<a id="s-5-2-4"></a>
### 5.2.4. Searching Systems

SAFEPLANT cuenta con un sistema de búsqueda simple, basado en barras de texto ubicadas dentro de las secciones donde hay grandes volúmenes de registros:

- **Alertas:** barra "Buscar código, zona o incidente..." que permite localizar una alerta específica.
- **Historial:** barra "Buscar por código, operador, nodo..." para encontrar eventos auditados.
- **Versión móvil:** barra "Buscar por código (ej. EVT) o nodo..." en el registro de eventos.

Además de la búsqueda por texto, el usuario puede refinar los resultados con filtros combinables: zona, severidad (Todos, Crítico, Advertencia, Auditados), ventana temporal y parámetro de telemetría. La búsqueda se ejecuta al escribir el término clave y presionar "Enter".

```html
<!-- Barra de búsqueda de alertas e incidentes -->
<form action="/alertas/search" method="GET">
  <input
    type="text"
    name="query"
    placeholder="Buscar código, zona o incidente..."
    aria-label="Buscar código, zona o incidente"
    style="width: 100%; padding: 10px; font-size: 16px;" />
</form>
```

<a id="s-5-2-5"></a>
### 5.2.5. Navigation Systems

**Navegación lateral (web):** la consola web incluye un menú lateral con las cinco secciones principales: Panel de Control, Umbrales, Alertas, Historial y Dispositivos. En la parte superior del menú se muestra el estado del sistema operativo (Planta Alfa y cantidad de nodos de telemetría activos), y la sección Alertas muestra un indicador numérico con las alertas pendientes. La barra superior presenta la ruta de ubicación (SAFEPLANT / Vista de Consola) y el usuario activo con su cargo.

**Navegación inferior (móvil):** en la aplicación móvil, las mismas secciones se acceden desde una barra inferior con íconos (Panel, Alertas, Umbrales, Historial y Equipos), que permite cambiar de sección con una sola mano y mantiene visible la ubicación actual.

**Navegación interna:** dentro de cada sección el usuario refina el contenido mediante:
- Pestañas de ventana temporal (1h, 6h, 12h, 24h; 7d, 30d).
- Filtros por zona, severidad y parámetro.
- Pestañas de estado de incidentes (Todos, Crítico, Advertencia, Auditados).
- Selector de zona en Dispositivos (Zona A a Zona E) y en la matriz comparativa de Umbrales, donde al tocar una zona se cargan sus límites.
- Paginación en las tablas de incidentes y registros.

**Navegación contextual:** desde el Panel de Control el usuario puede pasar al detalle, por ejemplo a Alertas desde un indicador crítico, o a Dispositivos desde la red de nodos IoT (Todos los Nodos). Desde Alertas y Historial se puede exportar el Reporte de Cumplimiento en PDF.

**Flujo de navegación esperado:** el usuario inicia sesión y llega al Panel de Control, donde evalúa el estado general de la planta. Si detecta una anomalía, entra a Alertas para reconocer el incidente y revisar la mitigación automática. Luego consulta el Historial para analizar la curva y auditar el evento, y si es necesario ajusta los límites en Umbrales. Finalmente revisa el estado de sensores y actuadores en Dispositivos.

<a id="s-5-3"></a>
## 5.3. Landing Page UI Design

<a id="s-5-3-1"></a>
### 5.3.1. Landing Page Wireframe

![Landing Page Wireframe](../assets/05-capitulo-v/landing/wireframe.png)

<a id="s-5-3-2"></a>
### 5.3.2. Landing Page Mock-up

La landing page de SAFEPLANT presenta la propuesta de valor y sus principales capacidades de forma visual, guiando al visitante desde una introducción al sistema hasta la invitación a conocer o iniciar la solución. El mock-up aplica los lineamientos visuales del proyecto y adapta su composición para navegadores de escritorio y móviles.

**Landing Page para Desktop Web Browser**

En la versión de escritorio se utiliza una paleta de tonos azul oscuro con acentos celestes y turquesa, asociada con la tecnología, la seguridad y el monitoreo ambiental. La jerarquía tipográfica, las tarjetas de contenido y los botones de acción permiten identificar rápidamente las funciones principales de SAFEPLANT, mientras que el contraste favorece la legibilidad y mantiene una presentación visual consistente.

![Landing Page para Desktop Web Browser](../assets/05-capitulo-v/landing/landing_mockup.png)

**Landing Page para Mobile Web Browser**

La versión móvil reorganiza el contenido en una columna para facilitar la lectura y la navegación en pantallas reducidas. Conserva la identidad visual, las secciones y las acciones principales de la versión de escritorio, priorizando el acceso mediante controles táctiles y manteniendo textos e indicadores legibles.

![Landing Page para Mobile Web Browser](<../assets/05-capitulo-v/landing/Landing Page para Mobile Web Browser.png>)

<a id="s-5-4"></a>
## 5.4. Applications UX/UI Design

<a id="s-5-4-1"></a>
### 5.4.1. Applications Wireframes

![Applications Wireframes](../assets/05-capitulo-v/applications/wireframes.png)

<a id="s-5-4-2"></a>
### 5.4.2. Applications Wireflow Diagrams

![Applications Wireflow](../assets/05-capitulo-v/applications/wireflow.png)

<a id="s-5-4-3"></a>
### 5.4.3. Applications Mock-ups

WEB:
![Applications mockup](../assets/05-capitulo-v/mockups/web/mockup1.png)
![Applications mockup](../assets/05-capitulo-v/mockups/web/mockup2.png)
![Applications mockup](../assets/05-capitulo-v/mockups/web/mockup3.png)
![Applications mockup](../assets/05-capitulo-v/mockups/web/mockup4.png)
![Gobernanza de cuentas - aplicación web](../assets/05-capitulo-v/mockups/web/mockup5.png)

MOVIL:

![Applications mockup](<../assets/05-capitulo-v/mockups/movil/movil (1).png>)
![Applications mockup](<../assets/05-capitulo-v/mockups/movil/movil (2).png>)
![Applications mockup](<../assets/05-capitulo-v/mockups/movil/movil (3).png>)
![Applications mockup](<../assets/05-capitulo-v/mockups/movil/movil (4).png>)
![Applications mockup](<../assets/05-capitulo-v/mockups/movil/movil (5).png>)
![Applications mockup](<../assets/05-capitulo-v/mockups/movil/movil (6).png>)
![Applications mockup](<../assets/05-capitulo-v/mockups/movil/movil (7).png>)

<a id="s-5-4-4"></a>
### 5.4.4. Applications User Flow Diagrams

![Applications User Flow](../assets/05-capitulo-v/applications/user-flow.png)

<a id="s-5-5"></a>
## 5.5. Applications Prototyping

En esta sección presentamos los prototipos de interfaz de SAFEPLANT para navegadores web de escritorio y dispositivos móviles. Estos permiten simular la navegación y las interacciones principales antes de implementar la solución, y complementan los wireframes, mock-ups y diagramas de User Flow presentados anteriormente. Los criterios de diseño se aplican de manera coherente a la landing page y a la aplicación web, respetando las necesidades de información de cada contexto.

<a id="s-5-5-1"></a>
### 5.5.1. Criterios de diseño y decisiones de interacción

Las decisiones de interacción se definieron a partir de la arquitectura de información de SAFEPLANT y de los recorridos descritos en los User Flow Diagrams. La navegación principal conserva las secciones Panel de Control, Alertas, Umbrales, Historial y Dispositivos; su organización prioriza primero la consulta del estado de la planta y permite acceder después al detalle o a las acciones de configuración según el rol del usuario. La navegación contextual conecta indicadores o incidentes con la información relacionada, evitando que el usuario tenga que regresar al inicio para continuar una tarea.

Para que las pantallas sean reconocibles, se mantienen etiquetas, iconos, colores y patrones visuales consistentes con los style guides. Los niveles de severidad y los estados del sistema conservan los mismos significados en las distintas vistas. Los controles utilizan convenciones conocidas —como pestañas, filtros, selectores, botones y ventanas de confirmación— para que sus funciones puedan identificarse sin instrucciones adicionales.

El diseño responsive adapta la distribución de los contenidos al espacio disponible en escritorio y móvil, preservando la jerarquía visual, la legibilidad y el acceso a las acciones relevantes. En pantallas amplias, la interfaz facilita la comparación simultánea de indicadores y tablas; en móvil, prioriza la consulta rápida y organiza la navegación y el contenido para una pantalla reducida, sin cambiar los nombres ni el significado de las secciones.

La información se presenta de forma clara y orientada a la tarea: los indicadores importantes se distinguen de los datos complementarios, las etiquetas describen el contenido y los mensajes comunican estados o acciones con lenguaje directo. Las interacciones simuladas —por ejemplo, cambiar el periodo de una gráfica, filtrar alertas, consultar el detalle de un incidente o ajustar un umbral— corresponden a tareas previstas en los User Flow Diagrams y muestran la respuesta esperada de la interfaz. De esta manera, la arquitectura de información determina tanto qué opciones se muestran como el orden y la relación entre ellas.

<a id="s-5-5-2"></a>
### 5.5.2. Prototipos web de escritorio y móvil

El prototipo web de escritorio presenta la navegación y las vistas de consulta y gestión de SAFEPLANT para el supervisor de seguridad y la consulta de resultados para el gerente de planta, de acuerdo con los permisos descritos en la arquitectura de información. El prototipo móvil conserva las mismas secciones y etiquetas, adaptando su distribución para facilitar el acceso desde una pantalla más pequeña.

En ambos prototipos se busca representar los recorridos principales: ingresar al Panel de Control para revisar las condiciones de la planta; abrir una alerta para consultar el incidente y su mitigación; revisar el Historial para analizar eventos; y, para el supervisor, acceder a Umbrales o Dispositivos cuando la tarea requiera configuración o verificación. La navegación y los controles son una simulación de interacción para comunicar el comportamiento esperado de la solución.

**Prototipo móvil:** [Abrir prototipo en Figma](https://www.figma.com/proto/LQrxGncQXV76uBaTK4ZvQe/SAFEPLANT-IoT?node-id=76-2192&t=gFTPorlHMMO2VxnX-1&scaling=scale-down&content-scaling=responsive&page-id=9%3A2&starting-point-node-id=76%3A2192).

**Prototipo web de escritorio:** [Abrir prototipo en Figma](https://www.figma.com/proto/LQrxGncQXV76uBaTK4ZvQe/SAFEPLANT-IoT?node-id=67-2086&p=f&t=DnfUCKPU45KIZ1SG-1&scaling=scale-down&content-scaling=responsive&page-id=62%3A234&starting-point-node-id=62%3A2071).

<a id="s-5-6"></a>
## 5.6. IoT Device Design

![IoT Device Design](../assets/05-capitulo-v/iot-device/device-design.png)

---

**Navegación:** [Índice](./00-student-outcome.md#s-tabla-contenidos) · Anterior: [Capítulo IV](./04-capitulo-iv-solution-software-design.md) · Siguiente: [Capítulo VI](./06-capitulo-vi-product-implementation.md)
