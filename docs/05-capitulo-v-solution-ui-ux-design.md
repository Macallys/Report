**Navegación:** [Índice](./00-student-outcome.md#s-tabla-contenidos) · Anterior: [Capítulo IV](./04-capitulo-iv-solution-software-design.md) · Siguiente: [Capítulo VI](./06-capitulo-vi-product-implementation.md)

---

<a id="s-cap-v"></a>
# Capítulo V: Solution UI/UX Design

<a id="s-5-1"></a>
## 5.1. Style Guidelines

<a id="s-5-1-1"></a>
### 5.1.1. General Style Guidelines

Los *style guidelines* son un conjunto de principios visuales y comunicacionales que permite mantener coherencia y claridad en la interfaz del producto. En el caso de SAFEPLANT, esta guía busca comunicar profesionalismo, precisión técnica y una identidad cercana al rubro de la seguridad industrial y el monitoreo de plantas.

La sección fija las decisiones de marca, tipografía, color y espaciado, y define el tono del lenguaje. El punto de partida es un design system de referencia: la escala modular tipográfica y los colores semánticos de Tailwind CSS. Esas referencias se adaptan al monitoreo industrial para que la consola web, la aplicación móvil y el dispositivo IoT se lean con rapidez cuando una condición de planta exige una respuesta. Las decisiones se apoyan en cuatro principios: jerarquía visual, para distinguir el dato crítico del contexto; consistencia, para que el mismo signo conserve su significado en todas las pantallas; contraste, para que el texto y los estados sigan siendo legibles; y retroalimentación, para que cada control confirme la acción del usuario.

**Branding: Nombre de marca**

SAFEPLANT representa una plataforma digital de telemetría y seguridad para plantas industriales. El nombre fusiona la protección del personal y de las condiciones de trabajo ("safe") con el entorno industrial donde opera el sistema ("plant").

El signo es un escudo con una marca de verificación. El contenedor en azul marino y el símbolo en cian separan la identidad de los colores de estado: el rojo, el ámbar y el verde quedan reservados para crítico, advertencia y condición normal. Se definen dos configuraciones del mismo logo, apilada y horizontal, para usarlo en el menú, la barra superior y la pantalla del dispositivo sin alterar el signo.


![Logo de SAFEPLANT](<../assets/05-capitulo-v/style-guidelines/Style Guide _ Sheet 6 - Logo (Light).png>)

![General Style Guidelines](<../assets/05-capitulo-v/style-guidelines/Style Guide_Sheet1 (1).png>)

**Misión:**
Brindar herramientas digitales que profesionalicen el trabajo del supervisor de seguridad y del encargado de planta, integrando la tecnología IoT con la prevención de riesgos ambientales.

**Visión:**
Ser la plataforma líder en monitoreo, mitigación automática y trazabilidad de condiciones de seguridad para plantas industriales en Latinoamérica.

**Colores:**

La paleta toma como referencia los tokens semánticos de Tailwind CSS y los adapta con un azul marino y un cian propios de SAFEPLANT. El azul marino (#0F2744) sostiene la navegación, el logo y el texto sobre fondo claro. El cian (#00E5FF) y el azul (#2563EB) marcan la acción y la tecnología de monitoreo. El verde (#10B981), el ámbar (#F59E0B) y el rojo (#EF4444) codifican una condición normal, una advertencia y un estado crítico, de modo que la severidad se reconoce antes de leer la etiqueta. El texto blanco (#FFFFFF) sobre el azul marino, y el azul marino sobre los fondos claros (#F8F9FF y #FFFFFF), conservan el contraste de lectura en la consola.

**Primario:** Azul Marino #0F2744

**Secundarios:** Azul Profundo #1B3B64, Azul #2563EB y Cian #00E5FF

**Terciarios:** Azul Claro #CBDBF5, Azul Hielo #EFF4FF y Fondo #F8F9FF

**Estados:** Verde #10B981, Ámbar #F59E0B, Rojo #EF4444 y Gris #64748B

**Color de texto:**

Sobre fondo oscuro: #FFFFFF

Sobre fondo claro: #0F2744

![Paleta de colores de SAFEPLANT](<../assets/05-capitulo-v/style-guidelines/Style Guide _ Sheet 1 - Color Palette (Light).png>)

**Color de botones:**

**Oscuro:** #0F2744

**Azul:** #2563EB

**Cian:** #00E5FF

**Gris:** #64748B

**Claro:** #CBDBF5

Cada variante se muestra en tres estados: Normal, Hover y Clicked / Checked.

![Estados de los botones de SAFEPLANT](<../assets/05-capitulo-v/style-guidelines/Style Guide _ Sheet 12 - Button states (Light).png>)

**Tipografía:**

La tipografía define la jerarquía visual y la legibilidad de la plataforma. SAFEPLANT usa una sola familia, Space Grotesk, para que la consola, la aplicación móvil y las referencias del dispositivo se perciban como el mismo producto. Es una sans geométrica de alto rendimiento en pantalla: sus formas abiertas favorecen la lectura de etiquetas cortas y de valores como PPM y dBA.

La escala parte de una base de 16px, con proporción Major Third (1.25) e interlineado de 1.5. Esa proporción, habitual en los design systems de interfaz, produce saltos perceptibles entre niveles y evita elegir tamaños de forma arbitraria. Los peldaños resultantes son 61, 49, 39, 31, 25, 20, 16 y 13px. Cada estilo se nombra como Nombre / Tamaño / Peso.

En la interfaz, esa escala es la referencia y algunos tamaños se ajustan al contexto de lectura. El título de página sube a 128px en la vista principal, y el texto de cuerpo se fija en 18px para leer indicadores con comodidad. Los estilos aplicados son:

- **Heading 01:** Space Grotesk Black – 128px. Título principal de página.
- **Heading 02:** Space Grotesk Bold – 60px. Título de sección.
- **Heading 03:** Space Grotesk Bold – 43px. Título de subsección.
- **Heading 04:** Space Grotesk Bold – 30px. Encabezado menor.
- **Heading 05:** Space Grotesk Bold – 32px. Subtítulo.
- **Heading 06:** Space Grotesk SemiBold – 24px. Encabezado pequeño dentro de una tarjeta o panel.
- **Texto principal:** Space Grotesk Regular – 18px. Párrafos, indicadores y valores técnicos. El texto destacado usa Bold, las citas Italic y los enlaces Regular con subrayado y color azul.
- **Captions:** Space Grotesk ExtraLight Italic – 18px. Acompañan gráficas y tablas sin competir con el dato.

Los pesos disponibles van de Thin a Black. En la práctica se usan Regular para leer, Medium y SemiBold para la jerarquía intermedia, y Bold o Black para lo que debe verse primero. Los valores técnicos, como PPM y dBA, permanecen en Space Grotesk para conservar una sola familia en cifras, unidades y etiquetas.

![Escala tipográfica](<../assets/05-capitulo-v/style-guidelines/Style Guide _ Sheet 2 - Type Scale.png>)

![Pesos tipográficos](<../assets/05-capitulo-v/style-guidelines/Style Guide _ Sheet 3 - Font Weights.png>)

![Convención de nombres](<../assets/05-capitulo-v/style-guidelines/Style Guide _ Sheet 4 - Naming Convention.png>)

![Ejemplos de la escala](<../assets/05-capitulo-v/style-guidelines/Style Guide _ Sheet 5 - Type Scale Examples.png>)

![Headings](<../assets/05-capitulo-v/style-guidelines/Style Guide _ Sheet 7 - Headings.png>)

**Espaciado:**

El espaciado ordena la relación entre texto, controles y bloques de información. La base de 16px fija una retícula de 8px, la misma lógica de espaciado de Tailwind, adaptada a esta interfaz. Los intervalos crecen en múltiplos de esa unidad —8, 16, 24 y 32px— para que márgenes, separación entre tarjetas y aire alrededor de los indicadores sigan el mismo ritmo en escritorio y en móvil. El interlineado de 1.5 evita comprimir los valores de CO₂, ruido y estado. Los botones, campos y paneles usan un radio de 10px: suaviza el contorno y conserva la sobriedad de una consola de planta.

**Tono de comunicación:**

El lenguaje se define sobre cuatro dimensiones, de acuerdo con el contexto de uso: un supervisor o un gerente que consulta el estado de la planta y, en ocasiones, debe actuar sobre un incidente.

- **Serio.** La interfaz informa riesgo ocupacional y cumplimiento. Las etiquetas nombran la condición con precisión —Crítico, Advertencia, Información, Normal, Precaución, Elevado— y reservan el énfasis visual para la severidad.
- **Formal y accesible.** Se mantiene el término técnico que el personal ya usa (CO₂, PPM, dBA, zona, nodo), en etiquetas de una a cuatro palabras. Un botón dice "Reconocer" o "Guardar Límite de CO₂", y un indicador muestra el límite junto al valor.
- **Respetuoso.** El sistema se dirige al supervisor de seguridad y al gerente de planta como responsables de la operación. Los mensajes describen el estado y la acción disponible, sin culpabilizar al usuario ni minimizar el evento.
- **Sereno.** Ante una alerta, el texto se mantiene directo y calmado. La urgencia la comunican el color, la jerarquía y el orden del incidente —detección, mitigación, confirmación y cierre—, no la exageración del mensaje. Esa calma favorece una respuesta oportuna.

En conjunto, el tono es profesional y técnico, y se mantiene claro para quien opera en planta.

<a id="s-5-1-2"></a>
### 5.1.2. Web, Mobile and IoT Style Guidelines

SAFEPLANT mantiene la misma paleta, la misma tipografía y los mismos colores de severidad en la consola web, la aplicación móvil y la lectura del nodo IoT. Cambia el gesto y el espacio disponible. En escritorio se comparan varias zonas a la vez. En el teléfono se consulta y se reconoce una alerta con una mano. En la planta, el dispositivo ejecuta la respuesta física y la confirmación queda en la pantalla del supervisor.

**Interfaz web**

El diseño web es limpio y está centrado en la operación. Las tarjetas resumen primero el estado —CO₂, presión acústica, personal en zona y alertas— y después dejan paso a la tabla y a la curva. Las gráficas marcan el límite normativo con una línea de contraste alto, para ver de inmediato si la lectura lo superó. Cada zona, sensor y actuador lleva un ícono y el color de severidad definido en la guía.

Los botones primarios son redondeados, con fondo #0F2744 y texto blanco. Los secundarios usan el azul #2563EB o el fondo claro #CBDBF5. El rojo #EF4444 identifica la severidad crítica y la confirmación de una acción que interrumpe una mitigación, y así queda separado del botón de trabajo habitual. Cada botón responde en Normal, Hover y Clicked / Checked.

Las tablas listan incidentes, zonas y nodos. El encabezado marca la jerarquía, la severidad ocupa un lugar visible y las filas se separan para recorrer código, lectura y estado. Zona, severidad y ventana temporal se filtran en la misma vista.

Las confirmaciones usan ventanas propias de la aplicación, sobre un fondo atenuado, con la acción y el cierre visibles. Sirven para reconocer un incidente o guardar un umbral. En web, móvil e IoT se usan los mismos controles genéricos: botones, campos de búsqueda, paneles de filtro y ventanas emergentes.

![Composición web: tarjetas, curva y tabla](../assets/05-capitulo-v/style-guidelines/web-layout-generico.jpg)

![Estados de los botones](<../assets/05-capitulo-v/style-guidelines/Style Guide _ Sheet 12 - Button states (Light).png>)

![Cajas de texto](<../assets/05-capitulo-v/style-guidelines/Style Guide _ Sheet 13 - Text input boxes (Light).png>)

![Paneles desplegables](<../assets/05-capitulo-v/style-guidelines/Style Guide _ Sheet 14 - Dropdown panels (Light).png>)

![Ventanas emergentes](<../assets/05-capitulo-v/style-guidelines/Style Guide _ Sheet 15 - Pop-up windows (Light).png>)

**Interfaz móvil**

La aplicación conserva los nombres de sección y el significado de cada color. El contenido pasa a una columna, la navegación baja a una barra de cinco íconos —Panel, Alertas, Umbrales, Historial y Equipos— y la alerta crítica queda arriba, al alcance del pulgar. Reconocer o aceptar se hace sobre la tarjeta. En un ancho menor, las tarjetas y las gráficas se apilan y las etiquetas se mantienen.

![Composición móvil](../assets/05-capitulo-v/style-guidelines/mobile-layout-generico.jpg)

**Interfaz de la aplicación IoT y del dispositivo físico**

En el panel y en Equipos, el nodo usa el mismo lenguaje que la consola: En línea, En diagnóstico, sensor, extractor, alarma y mampara. La vista es compacta porque el supervisor la consulta en planta, a menudo desde el teléfono.

La interfaz física del nodo comunica el riesgo con la actuación. El ESP32 mide CO₂, ruido y presencia, y quien está en la zona percibe el ventilador de extracción, la alarma acústica o la mampara de seguridad. Esos efectos siguen la misma regla que la alerta en pantalla. Reconocer el incidente y cambiar un umbral se hacen en la aplicación o en la web, para que el personal no tenga que operar el nodo dentro del área expuesta. Si el enlace falla, la interfaz muestra diagnóstico o pérdida de telemetría, y la actuación local sigue disponible en la planta.

![Interfaz física del nodo](../assets/05-capitulo-v/style-guidelines/iot-fisico-generico.jpg)
<a id="s-5-2"></a>


<a id="s-5-2"></a>
## 5.2. Information Architecture

La arquitectura de información de SAFEPLANT guía al supervisor de seguridad y al gerente de planta de forma lógica, eficiente y contextual. Cada módulo sigue el ciclo de la seguridad en planta: leer las condiciones de la zona (CO₂, ruido y presencia), detectar la exposición, ejecutar la mitigación, confirmar el incidente y dejar el registro listo para auditoría. Así, el dato técnico se captura en el momento y queda disponible para el análisis y la decisión posterior, tanto en la consola web como en el teléfono.

El Panel de Control es el punto de entrada porque la primera pregunta del usuario es el estado de la planta. Desde ahí, la arquitectura acerca el detalle solo cuando aparece una anomalía, hace falta ajustar un umbral o conviene revisar un nodo. El supervisor recorre todas las secciones y puede configurar el sistema. El gerente consulta el panel y el historial, sin modificar la operación.

A continuación se detallan los sistemas de organización, etiquetado, posicionamiento web, búsqueda y navegación que sostienen esa experiencia.

<a id="s-5-2-1"></a>
### 5.2.1. Organization Systems

En SAFEPLANT cada grupo de información usa el sistema que mejor sirve a la tarea. Hay dos familias. La organización visual define cómo se lee un conjunto en pantalla: de forma jerárquica, secuencial o matricial. La categorización define cómo se agrupa y se recupera ese contenido: por tópicos, por zona, por orden alfabético, por tiempo y por audiencia.

**Organización visual**

La **organización jerárquica** se aplica cuando el usuario debe ver primero lo urgente. En el Panel de Control el orden visual es indicadores generales (CO₂, presión acústica y personal en zonas críticas), luego la matriz de zonas y, al final, la respuesta automatizada y el estado de los nodos. En Alertas, el incidente crítico tiene más peso visual que la advertencia y que el mensaje informativo.

La **organización secuencial** se aplica cuando la tarea se completa por pasos. El incidente sigue detección del peligro, mitigación automática, pendiente de confirmación y, al cierre, resuelto o auditado. La configuración de umbrales sigue otro recorrido: el supervisor elige la zona, ajusta el límite de CO₂ o de ruido y guarda el cambio.

La **organización matricial** se aplica cuando hay que comparar varios elementos a la vez. Se usa en la matriz ambiental de zonas, en la matriz comparativa de umbrales y en las tablas de alertas y de registro de incidentes.

**Categorización del contenido**

La **categorización por tópicos** agrupa la telemetría según el parámetro medido: CO₂, presión acústica y presencia de personal. En Dispositivos, el mismo criterio separa sensores de monitoreo y actuadores de control.

La **categorización geográfica** divide la planta en zonas industriales. Alertas, historial, umbrales y dispositivos se filtran por zona, porque el riesgo se atiende en el lugar donde ocurre.

La **categorización alfabética** se usa para localizar un elemento conocido por su código. Zonas, nodos y eventos se ordenan por ese código cuando el usuario busca un identificador concreto, no cuando evalúa la urgencia.

La **categorización cronológica** ordena incidentes y registros del más reciente al más antiguo. En las gráficas, el mismo criterio ofrece las ventanas 1h, 6h, 12h y 24h, y en el historial también 7d y 30d.

La **categorización por audiencia** separa lo que ve cada grupo de usuarios. El supervisor de seguridad accede a todas las secciones y es quien configura umbrales, gestiona alertas y administra los nodos, desde la app móvil y la consola web. El gerente de planta consulta el Panel de Control y el Historial: ve el dashboard, las gráficas y los resultados, y no modifica la configuración.



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

La versión wireframe de la landing page de SAFEPLANT fija la estructura en baja fidelidad, antes de color, tipografía e imágenes. Ordena la lectura del visitante: entender qué resuelve la plataforma, ver cómo se monitorea la planta y llegar a una acción para ingresar. Arriba, la navegación es un bloque de logo, enlaces y un botón. El hero deja a la izquierda el titular, un texto de apoyo y dos botones. A la derecha, una tarjeta reúne indicadores y una gráfica simple para anticipar CO₂, ruido y presencia. Debajo hay franjas de tarjetas: tres de capacidades, tres de métricas, tres módulos con ícono y cuatro bloques de incidentes o zonas. Luego, tres pasos numerados acompañan un rectángulo de formulario o consola. El cierre es un botón y el pie repite logo y enlaces. Gráficos y tarjetas son cajas simples, para revisar la jerarquía antes del mock-up.

![Landing Page Wireframe](../assets/05-capitulo-v/landing/wireframe.png)

**Versión móvil**

En el wireframe móvil el mismo contenido pasa a una sola columna. El menú se reduce a un ícono, el hero apila el titular, los botones y la tarjeta de indicadores, y las franjas de tarjetas, los pasos y el cierre se leen de arriba hacia abajo. Se conservan las secciones y la acción de ingreso.

![Landing Page Wireframe móvil](../assets/05-capitulo-v/landing/WF_LandingMobile.png)

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

Los wireframes de las aplicaciones de SAFEPLANT definen la estructura base y la distribución funcional para las plataformas web y móvil. Aseguran que la atención se centre en la jerarquía de la información, el flujo de navegación y la ubicación de las acciones principales de los usuarios antes de aplicar el diseño visual final.

**Wireframes de Aplicación Web**

El esquema para la plataforma web, orientado al Encargado de Planta, distribuye el contenido aprovechando el formato de escritorio. Su estructura prioriza paneles de control amplios (dashboards) para el monitoreo consolidado, tablas detalladas para la auditoría de historiales y vistas estructuradas.

**Enlace para acceder al Figma:** [SAFEPLANT-Wireframes](https://www.figma.com/design/LQrxGncQXV76uBaTK4ZvQe/SAFEPLANT-IoT?node-id=16-2&p=f&t=DtY3CbltLXacNxro-0)

**Completar Registro - US11**

![Applications Wireframes](../assets/05-capitulo-v/applications/WF_1.png)

**Inicio de Sesión - US08**

![Applications Wireframes](../assets/05-capitulo-v/applications/WF_2.png)

**Panel Principal de Seguridad - US23**

![Applications Wireframes](../assets/05-capitulo-v/applications/WF_3.png)

**Alertas Activas y Registro de Incidentes - US23**

![Applications Wireframes](../assets/05-capitulo-v/applications/WF_4.png)

**Historial de Telemetría y Eventos - US23**

![Applications Wireframes](../assets/05-capitulo-v/applications/WF_5.png)

**Administración de Cuentas y Roles - US11 y US12**

![Applications Wireframes](../assets/05-capitulo-v/applications/WF_6.png)

**Wireframes de Aplicación Móvil**

El diseño para el dispositivo móvil, dirigido al Supervisor de Seguridad en campo, organiza la interfaz en una sola columna para facilitar la interacción rápida. Su estructura destaca los indicadores de telemetría en tiempo real por área industrial, la visualización clara de alertas críticas y el acceso directo a los controles manuales de los actuadores para situaciones de emergencia.


**Completar Registro - US11**

![Applications Wireframes](../assets/05-capitulo-v/applications/WFM_6.png)

**Inicio de Sesión - US07**

![Applications Wireframes](../assets/05-capitulo-v/applications/WFM_7.png)

**Panel de Control - US14**

![Applications Wireframes](../assets/05-capitulo-v/applications/WFM_1.png)

**Alertas Activas - US18**

![Applications Wireframes](../assets/05-capitulo-v/applications/WFM_2.png)

**Dispositivos por Área - US22**

![Applications Wireframes](../assets/05-capitulo-v/applications/WFM_3.png)

**Historial y Eventos - US26 y US33**

![Applications Wireframes](../assets/05-capitulo-v/applications/WFM_4.png)

**Umbrales de Seguridad - US21**

![Applications Wireframes](../assets/05-capitulo-v/applications/WFM_5.png)

<a id="s-5-4-2"></a>
### 5.4.2. Applications Wireflow Diagrams

Los wireflows de SAFEPLANT combinan las pantallas diseñadas para la aplicación web y la aplicación móvil con flechas de navegación, de modo que cada diagrama muestra cómo el usuario pasa de una pantalla a otra para cumplir un objetivo. Cada diagrama se presenta como un *User Goal* con una breve descripción de su recorrido.

El texto sobre cada flecha indica el elemento de la interfaz (botón, enlace, pestaña o menú lateral) que dispara la transición. El código USxx del título de cada pantalla identifica la user story a la que responde. Los flujos se agrupan por canal: la aplicación web de gobernanza y métricas, utilizada por el Encargado de Planta, y la aplicación móvil de operación, utilizada por el Supervisor de Seguridad.

**Aplicación Web (Encargado de Planta)**

*User Goal: Completar el registro y activar la cuenta (web).*

Una vez creada su cuenta desde Gobernanza, el usuario accede a la pantalla "Completar Registro", donde configura su rol o cargo operativo, confirma su correo corporativo y crea y confirma su contraseña. Al presionar "Activar Cuenta y Entrar" ingresa al Panel de control. Si ya tiene una cuenta activa, puede ir a "Iniciar Sesión" mediante el enlace "¿Ya tienes cuenta activa? Inicia sesión".

![Completar el registro y activar la cuenta (web).](../assets/05-capitulo-v/applications/wireflows/w_registro_web.png)

*User Goal: Iniciar sesión (web).*

El Encargado de Planta ingresa su correo electrónico corporativo y su contraseña, y presiona "Ingresar al Sistema" para acceder al Panel de control. Si todavía no tiene cuenta, el enlace "Regístrate" lo lleva a la pantalla de registro.

![Iniciar sesión (web).](../assets/05-capitulo-v/applications/wireflows/w_login_web.png)

*User Goal: Recuperar el acceso a la cuenta (web).*

Cuando el usuario olvida su contraseña, accede desde el inicio de sesión a "Recuperar credenciales", ingresa su correo corporativo y solicita el enlace de restablecimiento con "Enviar enlace de restablecimiento". Desde esta pantalla no se crean usuarios; el enlace "Volver a iniciar sesión" lo regresa al formulario de acceso.

![Recuperar el acceso a la cuenta (web).](../assets/05-capitulo-v/applications/wireflows/w_recuperar_web.png)

*User Goal: Monitorear la telemetría ambiental y revisar las alertas (web).*

Desde el Panel de control, el encargado visualiza el nivel promedio de CO₂, la presión acústica, el personal en zonas críticas, la matriz ambiental por zonas y las reglas de respuesta automática. Mediante el menú lateral accede a "Alertas", donde consulta el registro de alertas y eventos de seguridad, el flujo de auditoría de incidentes y el historial de telemetría, y puede regresar al Panel de Control en cualquier momento.

![Monitorear la telemetría ambiental y revisar las alertas (web).](../assets/05-capitulo-v/applications/wireflows/w_panel_alertas_web.png)

*User Goal: Gestionar las cuentas de supervisores en Gobernanza.*

Desde el menú lateral, el encargado selecciona "Gobernanza" y visualiza el directorio de supervisores, con búsqueda, edición, eliminación y exportación. Con el botón "+ Añadir supervisor" abre la ventana "Añadir Nuevo Usuario", ingresa el correo corporativo y presiona "Crear supervisor y ver clave"; el sistema muestra en pantalla la clave temporal generada y retorna al directorio. También puede cancelar la operación.

![Gestionar las cuentas de supervisores en Gobernanza.](../assets/05-capitulo-v/applications/wireflows/w_gobernanza_web.png)

*User Goal: Cerrar la sesión activa (web).*

Desde el menú lateral de la aplicación, el usuario presiona "Cerrar sesión". El sistema finaliza la sesión y lo devuelve a la pantalla de "Iniciar Sesión", desde donde deberá autenticarse nuevamente para acceder a las funciones protegidas.

![Cerrar la sesión activa (web).](../assets/05-capitulo-v/applications/wireflows/w_logout_web.png)

**Aplicación Móvil (Supervisor de Seguridad)**

*User Goal: Completar la cuenta e ingresar (móvil).*

El supervisor invitado abre la pantalla "Completa tu cuenta", donde ve su correo corporativo y su rol preasignado "Supervisor/a de Seguridad" por invitación. Crea y confirma su contraseña y presiona "Completar Registro e Ingresar" para entrar al Panel de la aplicación. Si ya tiene una cuenta activa, el enlace "Iniciar sesión" lo lleva al acceso.

![Completar la cuenta e ingresar (móvil).](../assets/05-capitulo-v/applications/wireflows/w_registro_mov.png)

*User Goal: Iniciar sesión (móvil).*

El supervisor ingresa su correo corporativo y su contraseña, puede marcar la opción "Recordar mi cuenta en este teléfono" y presiona "Entrar a SafePlant" para llegar al Panel. Si aún no tiene cuenta, el enlace "Registrarse" lo lleva a la pantalla de registro.

![Iniciar sesión (móvil).](../assets/05-capitulo-v/applications/wireflows/w_login_mov.png)

*User Goal: Monitorear la planta por zonas y revisar las alertas (móvil).*

Desde el Panel, el supervisor observa en tiempo real el nivel de CO₂, la presión acústica, el estado de cada zona y las reglas de causa-efecto activas. Con la pestaña "Alertas" de la barra inferior accede a las alertas e incidentes, donde ve su severidad, la mitigación del PLC en curso y las tendencias de las últimas 24 horas, y puede reconocer o aceptar cada alerta. Con la pestaña "Panel" regresa al resumen.

![Monitorear la planta por zonas y revisar las alertas (móvil).](../assets/05-capitulo-v/applications/wireflows/w_panel_alertas_mov.png)

*User Goal: Configurar los umbrales de CO₂ y ruido por zona.*

El supervisor puede llegar a "Umbrales" desde la pestaña de la barra inferior o directamente desde una alerta mediante el botón de ajuste. En esta pantalla elige la zona activa, modifica el límite de CO₂ y de ruido con los controles "−" y "+", guarda cada límite y verifica su estado de sincronización en la matriz comparativa de zonas.

![Configurar los umbrales de CO₂ y ruido por zona.](../assets/05-capitulo-v/applications/wireflows/w_umbrales_mov.png)

*User Goal: Consultar el historial de telemetría.*

Desde el Panel, el supervisor selecciona la pestaña "Historial" y revisa las curvas de CO₂ y presión acústica frente a su límite, el promedio y el tiempo de respuesta del PLC, filtra el periodo (24 h, 7 d o 30 d), busca en el registro de eventos y puede exportar el reporte en PDF.

![Consultar el historial de telemetría.](../assets/05-capitulo-v/applications/wireflows/w_historial_mov.png)

*User Goal: Supervisar los dispositivos por área.*

Desde el Panel, el supervisor selecciona la pestaña "Equipos" y visualiza, por cada zona, los sensores de monitoreo (sonido, CO₂ y movimiento) y los actuadores de control (ventilador de extracción, alarma acústica y mamparas de seguridad) con su estado en vivo.

![Supervisar los dispositivos por área.](../assets/05-capitulo-v/applications/wireflows/w_equipos_mov.png)



<a id="s-5-4-3"></a>
### 5.4.3. Applications Mock-ups

WEB:

![Iniciar sesión del encargado](<../assets/05-capitulo-v/mockups/web/Iniciar Sesion Encargado.png>)
![Completar registro](<../assets/05-capitulo-v/mockups/web/crear nuevo registro.png>)
![Panel de control del encargado](<../assets/05-capitulo-v/mockups/web/Panel de control del encargado.png>)
![Alertas del encargado de planta](<../assets/05-capitulo-v/mockups/web/Alertas del encargado de planta.png>)
![Gobernanza de cuentas - aplicación web](<../assets/05-capitulo-v/mockups/web/ADMINISTRACION DE ROLES.png>)
![Crear nuevo usuario](<../assets/05-capitulo-v/mockups/web/Crear nuevo usuario.png>)

MOVIL:

![Iniciar sesión](<../assets/05-capitulo-v/mockups/movil/SAFEPLANT Mobile _ Iniciar Sesión (Minimalista & Cálido).png>)
![Registro](<../assets/05-capitulo-v/mockups/movil/SAFEPLANT Mobile _ Registro (Estilo Limpio & Oficial).png>)
![Panel de Control](<../assets/05-capitulo-v/mockups/movil/SAFEPLANT Mobile _ Panel de Control.png>)
![Alertas Activas](<../assets/05-capitulo-v/mockups/movil/SAFEPLANT Mobile _ Alertas Activas.png>)
![Umbrales de Seguridad](<../assets/05-capitulo-v/mockups/movil/SAFEPLANT Mobile _ Umbrales de Seguridad.png>)
![Historial y Eventos](<../assets/05-capitulo-v/mockups/movil/SAFEPLANT Mobile _ Historial y Eventos.png>)
![Dispositivos por Área](<../assets/05-capitulo-v/mockups/movil/SAFEPLANT Mobile _ Dispositivos por Área.png>)

<a id="s-5-4-4"></a>
### 5.4.4. Applications User Flow Diagrams

Los user flow diagrams describen, en formato de historia de usuario, el recorrido completo que sigue cada actor para cumplir una tarea de SAFEPLANT. Los círculos numerados indican el orden de los pasos y el texto sobre cada flecha, la acción o condición que hace avanzar al usuario. A diferencia de los wireflows, que detallan la navegación entre pantallas, estos diagramas se centran en la secuencia de la tarea de principio a fin e incluyen transiciones entre el canal web y el móvil.

**USER GOAL: Alta de un supervisor y activación de su cuenta.** Como Encargado de Planta, puedo crear desde Gobernanza la cuenta de un supervisor de seguridad; el sistema muestra en pantalla una clave temporal que le entrego directamente, sin enviarla por correo. Con ella, el supervisor completa su registro en la aplicación móvil, donde su rol ya viene preasignado por invitación, y accede al Panel de telemetría de la planta.

![Alta de un supervisor y activación de su cuenta](../assets/05-capitulo-v/applications/user-flows/u_alta_cuenta.png)

**USER GOAL: Ingreso y supervisión desde la web.** Como Encargado de Planta, puedo iniciar sesión con mis credenciales corporativas y ver el panel de control con la telemetría de seguridad ambiental de la planta. Desde allí paso al registro de alertas y eventos para auditar los incidentes, su estado de mitigación y las curvas de telemetría, y así gobernar la operación con información consolidada.

![Ingreso y supervisión desde la web](../assets/05-capitulo-v/applications/user-flows/u_login_web.png)

**USER GOAL: Ingreso y atención de alertas desde el móvil.** Como Supervisor de Seguridad, puedo iniciar sesión en la aplicación móvil desde cualquier lugar y ver el estado de cada zona de la planta. Cuando una zona presenta una condición de precaución, entro a Alertas para conocer el incidente, el tiempo de respuesta y la mitigación automática que el sistema ya ejecutó.

![Ingreso y atención de alertas desde el móvil](../assets/05-capitulo-v/applications/user-flows/u_login_mov.png)

**USER GOAL: Recuperar el acceso a mi cuenta.** Como usuario registrado, puedo recuperar el acceso cuando olvido mi contraseña: solicito el enlace de restablecimiento con mi correo corporativo, lo recibo en mi bandeja, defino una nueva contraseña, vuelvo a iniciar sesión y retomo mi trabajo en el Panel de control.

![Recuperar el acceso a mi cuenta](../assets/05-capitulo-v/applications/user-flows/u_recuperar.png)

**USER GOAL: Atender una alerta crítica de CO₂.** Como Supervisor de Seguridad, puedo detectar en el Panel que una zona, por ejemplo la Zona C de Fundición e Inducción, supera el nivel normal de CO₂. En Alertas reconozco el incidente mientras el PLC mantiene activa la mitigación, ajusto el umbral de la zona en Umbrales si corresponde y verifico en Historial la curva del pico y el tiempo de respuesta del sistema, para dejar el evento auditado.

![Atender una alerta crítica de CO₂](../assets/05-capitulo-v/applications/user-flows/u_alerta_critica.png)

**USER GOAL: Verificar los equipos de una zona y auditar los eventos.** Como Supervisor de Seguridad, puedo revisar desde el Panel una zona con lecturas elevadas, comprobar en Equipos que los sensores y actuadores (ventilador, alarma y mamparas) funcionan y están en el estado esperado, y luego consultar el Historial para auditar los eventos y la efectividad de la respuesta automática.

![Verificar los equipos de una zona y auditar los eventos](../assets/05-capitulo-v/applications/user-flows/u_equipos.png)

**USER GOAL: Gestionar el directorio de supervisores.** Como Encargado de Planta, puedo abrir Gobernanza desde el Panel de control, consultar el directorio de supervisores activos y añadir uno nuevo con su correo corporativo. Al crearlo obtengo su clave temporal y regreso al directorio actualizado, con lo que controlo quién accede a la operación móvil de la planta.

![Gestionar el directorio de supervisores](../assets/05-capitulo-v/applications/user-flows/u_gobernanza.png)

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

**Explicación del prototipo móvil:** [Ver video en SharePoint](https://upcedupe-my.sharepoint.com/:v:/g/personal/u20231b775_upc_edu_pe/IQC0z40dQIqVQbQvuddVxnAmAejBnKbEFgnXIzfK4z9N5c4?nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJPbmVEcml2ZUZvckJ1c2luZXNzIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXciLCJyZWZlcnJhbFZpZXciOiJNeUZpbGVzTGlua0NvcHkifX0&e=jVhkvW).

![Evidencia de la explicación del prototipo móvil](../assets/05-capitulo-v/prototipos/explicacion-prototipo-movil.png)

**Prototipo web de escritorio:** [Abrir prototipo en Figma](https://www.figma.com/proto/LQrxGncQXV76uBaTK4ZvQe/SAFEPLANT-IoT?node-id=67-2086&p=f&t=DnfUCKPU45KIZ1SG-1&scaling=scale-down&content-scaling=responsive&page-id=62%3A234&starting-point-node-id=62%3A2071).

**Explicación del prototipo web:** [Ver video en SharePoint](https://upcedupe-my.sharepoint.com/:v:/g/personal/u20231b775_upc_edu_pe/IQACIq6Cv0-cQLxQ1Ce_OAIJAcl4q4FVlA-Jfpse8Tw30Xc?nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJPbmVEcml2ZUZvckJ1c2luZXNzIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXciLCJyZWZlcnJhbFZpZXciOiJNeUZpbGVzTGlua0NvcHkifX0&e=QlFb91).

![Evidencia de la explicación del prototipo web](../assets/05-capitulo-v/prototipos/explicacion-prototipo-web.png)

<a id="s-5-6"></a>
## 5.6. IoT Device Design

Link a proyecto de Wowki: [https://wokwi.com/projects/477285427305212929](https://wokwi.com/projects/477285427305212929)

![IoT Device Design](../assets/05-capitulo-v/iot-device/wokwi.png)

![IoT Device Design](../assets/05-capitulo-v/iot-device/wokwi1.png)

![IoT Device Design](../assets/05-capitulo-v/iot-device/wokwi2.png)

---

**Navegación:** [Índice](./00-student-outcome.md#s-tabla-contenidos) · Anterior: [Capítulo IV](./04-capitulo-iv-solution-software-design.md) · Siguiente: [Capítulo VI](./06-capitulo-vi-product-implementation.md)
