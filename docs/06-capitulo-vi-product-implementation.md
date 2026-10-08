**Navegación:** [Índice](./00-student-outcome.md#s-tabla-contenidos) · Anterior: [Capítulo V](./05-capitulo-v-solution-ui-ux-design.md) · Siguiente: [Conclusiones](./07-conclusiones.md)

---

<a id="s-cap-vi"></a>
# Capítulo VI: Product Implementation, Validation & Deployment

<a id="s-6-1"></a>
## 6.1. Software Configuration Management

La configuración del software en SafePlant establece las herramientas que permiten al equipo mantener el control sobre los cambios en el código fuente, asegurar la calidad y organizar el despliegue hacia los entornos de producción (Cloud y Edge).

<a id="s-6-1-1"></a>
### 6.1.1. Software Development Environment Configuration

Para el desarrollo colaborativo del ecosistema SafePlant, el equipo utiliza las siguientes herramientas y entornos de desarrollo, alineados con la arquitectura del proyecto:

*   **Figma:** Herramienta colaborativa en la nube utilizada para el diseño de wireframes, wireflows, mock-ups y prototipado de las interfaces web y móvil.
*   **Visual Studio / VS Code:** Principales para la construcción del Web Monolithic Backend y la Edge Application en ASP.NET Core, así como para el desarrollo del frontend en Angular.
*   **Android Studio / VS Code:** Entornos configurados con los SDKs necesarios para la programación de la aplicación móvil multiplataforma utilizando Flutter.
*   **Arduino IDE / PlatformIO:** Entornos utilizados para escribir, compilar y cargar el firmware en C++ hacia los microcontroladores ESP32.
*   **GitHub:** Plataforma en la nube utilizada como repositorio central para el control de versiones y el trabajo colaborativo del código fuente.
*   **pgAdmin / DBeaver:** Gestores de bases de datos utilizados para modelar y administrar la Cloud Database en PostgreSQL localmente antes de su despliegue.

<a id="s-6-1-2"></a>
### 6.1.2. Source Code Management

El código fuente y la documentación del proyecto se gestionan centralizadamente utilizando **GitHub** bajo la organización `Macallys`. Actualmente, la organización alberga los siguientes repositorios principales:

[https://github.com/Macallys/Report](https://github.com/Macallys/Report)

*   **`Report`:** Repositorio central que contiene la documentación  y el informe del proyecto.
*   **`safeplant-web-backend`:** Contiene el código fuente del Web Monolithic Backend y la Edge Application desarrollados en ASP.NET Core.
*   **`safeplant-web-client`:** Contiene el código fuente de la aplicación web frontend en Angular.
*   **`landing-page`:** Repositorio dedicado al sitio web informativo estático.

**Estrategia de Ramas**
El equipo ha adaptado su flujo de trabajo para agilizar la integración continua. Inicialmente, se implementó un enfoque basado en ramas de características específicas para segmentar el trabajo. Sin embargo, la estrategia actual se ha simplificado: los miembros del equipo ahora integran sus aportes y actualizaciones de forma directa en la rama `develop` para acelerar el ciclo de desarrollo y consolidación. 

La estructura base del flujo de trabajo se compone de:
*   **`main`:** Contiene el código en estado de producción, asegurando que siempre sea estable y desplegable.
*   **`develop`:** Rama por defecto y principal vía de integración activa, donde se encuentran todas las modificaciones directas del equipo antes de un pase a producción.
*   **`feature/*`:** Ramas temporales utilizadas históricamente para la división de tareas específicas.

**Estándares de Commits**
Para mantener un historial de cambios legible y auditable, el equipo aplica la convención de *Conventional Commits* con la estructura:
*   `feat`: Una nueva funcionalidad.
*   `fix`: Corrección de un error.
*   `docs`: Cambios en la documentación.
*   `style`: Cambios de formato que no afectan la lógica.
*   `refactor`: Cambio en el código que no corrige errores ni añade funciones.
*   `test`: Añadir o corregir pruebas

<a id="s-6-1-3"></a>
### 6.1.3. Source Code Style Guide & Conventions

Para mantener la legibilidad y consistencia del código entre los  miembros del equipo, se siguen las convenciones oficiales de cada tecnología utilizada en SafePlant:

**C# (ASP.NET Core - Backend & Edge)**
La estructura del repositorio backend refleja fielmente el diseño estratégico (DDD), imponiendo las siguientes reglas a nivel de solución:
*   **Separación de Hosts:** Los puntos de entrada de la aplicación se mantienen aislados en la carpeta `src/Hosts`, diferenciando el proyecto `Cloud.Api` del proyecto `Plant.Host` (para ejecución en el servidor Edge local).
*   **Aislamiento Modular:** El código se organiza en la carpeta `src/Modules` según los Bounded Contexts definidos: `DeviceEdgeManagement`, `IAM`, `PlantMonitoring` y `SafetyActuation`, además de un `SharedKernel` para lógica transversal.
*   **Capas Tácticas:** Cada uno implementa estrictamente tres capas: `Application`, `Domain` e `Infrastructure`.

**TypeScript (Angular - Web Client)**
El desarrollo del cliente web se estructura mediante una arquitectura modular orientada a funcionalidades:
*   **Estructura por Features:** El código se organiza en la carpeta `src/app/features`, dividiendo la aplicación en módulos funcionales como `accounts`, `metrics` y `recovery`. La lógica se ubica en `core` y `shared`.
*   **Separación de Responsabilidades:** Se separan las responsabilidades en archivos específicos utilizando sufijos descriptivos: `.api.ts` para llamadas HTTP, `.models.ts` para interfaces de datos, y `.store.ts` para la gestión de estado local.
  
**Dart (Flutter - Mobile App)**
*   Utilizar *UpperCamelCase* para nombrar clases, enumeraciones y extensiones.
*   Utilizar *lowerCamelCase* para nombrar variables, constantes y métodos.
*   Nombrar los archivos y carpetas utilizando *snake_case*.

**C++ (Arduino/ESP32 - Firmware)**
*   Utilizar letras mayúsculas separadas por guiones bajos para definir constantes y pines.
*   Implementar código que garantice que el dispositivo no pierda la conexión con el broker Eclipse Mosquitto.
*   Comentar la lógica detrás de la lectura de sensores y activación de relés para facilitar el mantenimiento del hardware de campo.

<a id="s-6-1-4"></a>
### 6.1.4. Software Deployment Configuration

La arquitectura de despliegue se divide en tres niveles operativos, tal como se especifica en el Diagrama de Despliegue del sistema:

**1. Despliegue en la Nube (Cloud - Azure)**
Se utiliza la plataforma Microsoft Azure para hospedar los componentes centrales:
*   **Azure Static Web Apps:** Para la landing page y el cliente Angular para la aplicación web.
*   **Azure App Service:** Hospeda el monolito ASP.NET Core que gestiona la lógica en la nube.
*   **Azure Database for PostgreSQL:** Actúa como el sistema de registro central en la nube.

**2. Despliegue en Planta (Edge On-Premise)**
Para garantizar la operación continua sin dependencia de internet, se despliega infraestructura local en la planta:
*   **Servidor On-Premise:** Ejecuta la Edge Application que contiene el loop de seguridad vivo (Safety & Actuation).
*   **Base de Datos Local:** Utiliza SQLite en planta para mantener el estado y la contingencia offline.
*   **Broker de Mensajería:** Eclipse Mosquitto opera localmente como intermediario entre el firmware y la aplicación Edge.

**3. Despliegue de Clientes y Hardware**
*   **App Móvil:** La aplicación Flutter se ejecuta en el dispositivo móvil del supervisor.
*   **Hardware de Campo:** El firmware Arduino/ESP32 se despliega directamente en los dispositivos conectados a sensores y actuadores físicos.
*   **Servicios Externos:** Se utiliza un servicio SMTP externo para el envío de correos, mientras que la identidad es propia del sistema.

  **Estado del despliegue**

| Componente | Plataforma objetivo | Plataforma actual (Sprint 1) | Estado |
| --- | --- | --- | --- |
| Landing page | Azure Static Web Apps | GitHub Pages | Desplegado |
| Aplicación web | Azure Static Web Apps | Vercel | Desplegado |
| Backend (Cloud.Api) | Azure App Service | Azure App Service | Desplegado |

<a id="s-6-2"></a>
## 6.2. Landing Page, Services & Applications Implementation

**URL de la landing page desplegada:** https://macallys.github.io/landing-page/

> Documentar cada sprint en `sprints/` a partir de [`templates/sprint.md`](./templates/sprint.md).

<table>
  <thead>
    <tr>
      <th align="left">#</th>
      <th align="left">Sprint</th>
      <th align="left">Documento</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td align="left">6.2.1</td>
      <td align="left">Sprint 1</td>
      <td align="left"><a href="./sprints/sprint-01.md">Sprint 1</a></td>
    </tr>
  </tbody>
</table>

<a id="s-6-3"></a>
## 6.3. Validation Interviews

<a id="s-6-3-1"></a>
### 6.3.1. Diseño de Entrevistas

<a id="s-6-3-2"></a>
### 6.3.2. Registro de Entrevistas

<table>
  <thead>
    <tr>
      <th align="left">ID</th>
      <th align="left">Fecha</th>
      <th align="left">Entrevistado</th>
      <th align="left">Segmento objetivo</th>
      <th align="left">Evidencia</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td align="left">V-01</td>
      <td align="left"></td>
      <td align="left"></td>
      <td align="left"></td>
      <td align="left"></td>
    </tr>
  </tbody>
</table>

<a id="s-6-3-3"></a>
### 6.3.3. Evaluaciones según heurísticas

<a id="s-6-4"></a>
## 6.4. Video About-the-Product

**URL del video:** 

![Video About-the-Product](../assets/06-capitulo-vi/videos/about-the-product.png)

---

**Navegación:** [Índice](./00-student-outcome.md#s-tabla-contenidos) · Anterior: [Capítulo V](./05-capitulo-v-solution-ui-ux-design.md) · Siguiente: [Conclusiones](./07-conclusiones.md)
