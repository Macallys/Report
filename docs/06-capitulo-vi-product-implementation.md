**Navegación:** [Índice](./00-student-outcome.md#s-tabla-contenidos) · Anterior: [Capítulo V](./05-capitulo-v-solution-ui-ux-design.md) · Siguiente: [Conclusiones](./07-conclusiones.md)

---

<a id="s-cap-vi"></a>
# Capítulo VI: Product Implementation, Validation & Deployment

<a id="s-6-1"></a>
## 6.1. Software Configuration Management

<a id="s-6-1-1"></a>
### 6.1.1. Software Development Environment Configuration

<a id="s-6-1-2"></a>
### 6.1.2. Source Code Management

<a id="s-6-1-3"></a>
### 6.1.3. Source Code Style Guide & Conventions

<a id="s-6-1-4"></a>
### 6.1.4. Software Deployment Configuration

![Software Deployment Configuration](../assets/06-capitulo-vi/scm/deployment-configuration.png)

<a id="s-6-2"></a>
## 6.2. Landing Page, Services & Applications Implementation


### 6.2.1. Sprint 1

En esta sección se registra y explica el avance en términos de producto y trabajo colaborativo del Sprint 1 de SafePlant, desarrollado entre el 20 de septiembre y el 8 de octubre de 2026. El sprint se centró en tres frentes: la presencia pública del producto mediante la landing page desplegada; la capa de presentación de la aplicación web del Encargado de Planta, con sus vistas implementadas y desplegadas; y la base del backend, con el bounded context Identity & Access y los endpoints de autenticación y gestión de cuentas. La integración entre la aplicación web y el backend, que en este sprint opera con datos de muestra, queda como trabajo del Sprint 2.

<a id="s-6-2-1-1"></a>
#### 6.2.1.1. Sprint Planning 1

El Sprint Planning Meeting del Sprint 1 tuvo como propósito definir el primer incremento visible de SafePlant. El equipo priorizó lo que permite presentar el producto a los segmentos objetivo y validar la experiencia del Encargado de Planta: la landing page informativa, las vistas de la aplicación web de gobernanza y la autenticación de usuarios en el backend. Al ser el primer sprint, no existen Sprint Review ni Sprint Retrospective previos.

<table>
  <thead>
    <tr>
      <th align="left" colspan="2">Sprint # - Sprint 1</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td align="left" colspan="2"><strong>Sprint Planning Background</strong></td>
    </tr>
    <tr>
      <td align="left">Date</td>
      <td align="left">2026-09-21</td>
    </tr>
    <tr>
      <td align="left">Time</td>
      <td align="left">09:00 PM</td>
    </tr>
    <tr>
      <td align="left">Location</td>
      <td align="left">Reunión virtual vía Discord</td>
    </tr>
    <tr>
      <td align="left">Prepared By</td>
      <td align="left">Sanchez Gonzales, Gabriel</td>
    </tr>
    <tr>
      <td align="left">Attendees (to planning meeting)</td>
      <td align="left">Solano Armas, Angelo Héctor / Gordillo Ramos, Santiago Alonso / Huaman Cuba, Johan Giovani / Baldeon Vivar, Santiago Armando / Iglesias Pérez, Sergio Sebastián / Sanchez Gonzales, Gabriel</td>
    </tr>
    <tr>
      <td align="left">Sprint 0 Review Summary</td>
      <td align="left">No aplica. Es el primer sprint del proyecto.</td>
    </tr>
    <tr>
      <td align="left">Sprint 0 Retrospective Summary</td>
      <td align="left">No aplica. Es el primer sprint del proyecto.</td>
    </tr>
    <tr>
      <td align="left" colspan="2"><strong>Sprint Goal &amp; User Stories</strong></td>
    </tr>
    <tr>
      <td align="left">Sprint 1 Goal</td>
      <td align="left">
        <strong>Our focus is on</strong> dar a conocer SafePlant mediante una landing page desplegada que explique su propósito, sus beneficios y su arquitectura, y en ofrecer al Encargado de Planta las vistas de su aplicación web (inicio de sesión, gestión de cuentas y roles, dashboard de métricas e historial), respaldadas por un backend capaz de autenticar usuarios y gestionar cuentas.<br><br>
        <strong>We believe it delivers</strong> una comprensión clara de la propuesta de valor de SafePlant y una primera experiencia navegable de gobernanza de la planta <strong>to</strong> los visitantes interesados en la solución y los Encargados de Planta.<br><br>
        <strong>This will be confirmed when</strong> un visitante pueda recorrer la landing desplegada y acceder desde ella a la aplicación web publicada, un Encargado de Planta pueda navegar todas las vistas web, y el backend emita un token de acceso válido al iniciar sesión.
      </td>
    </tr>
    <tr>
      <td align="left">Sprint 1 Velocity</td>
      <td align="left">30 Story Points. Al ser el primer sprint no existe velocity histórica; el valor corresponde a la capacidad estimada por el equipo en el planning.</td>
    </tr>
    <tr>
      <td align="left">Sum of Story Points</td>
      <td align="left">27 Story Points (US01, US02, US05, US09, US08, US11, US12, US23 y TS21)</td>
    </tr>
  </tbody>
</table>

<a id="s-6-2-1-2"></a>
#### 6.2.1.2. Aspect Leaders and Collaborators

Los aspectos considerados en el Sprint 1 corresponden a los productos trabajados en la iteración: la landing page, la aplicación web del Encargado de Planta, el backend con el bounded context Identity & Access, el despliegue de los productos y la documentación del sprint en el informe. Para cada aspecto se define un líder (L), responsable de coordinar y validar el avance, y colaboradores (C) que participan en su implementación.

<table>
  <thead>
    <tr>
      <th align="left">Team Member (Last Name, First Name)</th>
      <th align="left">GitHub Username</th>
      <th align="left">Landing Page</th>
      <th align="left">Web Application</th>
      <th align="left">Backend (Identity &amp; Access)</th>
      <th align="left">Deployment</th>
      <th align="left">Report</th>
    </tr>
  </thead>
  <tbody>
    <tr><td align="left">Solano Armas, Angelo Héctor</td><td align="left">Angelo5214</td><td align="left">C</td><td align="left">C</td><td align="left">C</td><td align="left">C</td><td align="left">L</td></tr>
    <tr><td align="left">Gordillo Ramos, Santiago Alonso</td><td align="left">SantiIHC</td><td align="left">C</td><td align="left">C</td><td align="left">C</td><td align="left">C</td><td align="left">C</td></tr>
    <tr><td align="left">Huaman Cuba, Johan Giovani</td><td align="left">Johancuba</td><td align="left">C</td><td align="left">C</td><td align="left">C</td><td align="left">C</td><td align="left">C</td></tr>
    <tr><td align="left">Baldeon Vivar, Santiago Armando</td><td align="left">Santibal11</td><td align="left">C</td><td align="left">C</td><td align="left">C</td><td align="left">C</td><td align="left">L</td></tr>
    <tr><td align="left">Iglesias Pérez, Sergio Sebastián</td><td align="left">ghostrider101218</td><td align="left">C</td><td align="left">C</td><td align="left">L</td><td align="left">L</td><td align="left">C</td></tr>
    <tr><td align="left">Sanchez Gonzales, Gabriel</td><td align="left">yigabriel</td><td align="left">L</td><td align="left">L</td><td align="left">C</td><td align="left">C</td><td align="left">C</td></tr>
  </tbody>
</table>

<a id="s-6-2-1-3"></a>
#### 6.2.1.3. Sprint Backlog 1

El objetivo principal del Sprint 1 fue entregar el primer incremento visible de SafePlant: la landing page desplegada, las vistas de la aplicación web del Encargado de Planta y la autenticación en el backend. El tablero del sprint se gestionó en Trello, donde cada work-item avanzó por los estados To-do, In-Process, To-Review y Done.

La siguiente tabla detalla las User Stories asignadas al sprint, junto con los work-items resultantes de su descomposición y las tareas complementarias que no dependen de una User Story en particular.

<table>
  <thead>
    <tr>
      <th align="left">Sprint #</th>
      <th align="left" colspan="7">Sprint 1</th>
    </tr>
    <tr>
      <th align="left" colspan="2">User Story</th>
      <th align="left" colspan="6">Work-Item / Task</th>
    </tr>
    <tr>
      <th align="left">Id</th>
      <th align="left">Title</th>
      <th align="left">Id</th>
      <th align="left">Title</th>
      <th align="left">Description</th>
      <th align="left">Estimation (Hours)</th>
      <th align="left">Assigned To</th>
      <th align="left">Status (To-do / In-Process / To-Review / Done)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td align="left">US01</td>
      <td align="left">View SafePlant system information</td>
      <td align="left">T01</td>
      <td align="left">Hero, propósito y flujo del sistema</td>
      <td align="left">Maquetar la estructura base de la landing (navbar, hero) y las secciones "Qué es SafePlant", "Monitoreo en tiempo real", "Cómo responde el sistema" y "De la detección a la acción automática".</td>
      <td align="left">5</td>
      <td align="left">Sanchez Gonzales, Gabriel</td>
      <td align="left">Done</td>
    </tr>
    <tr>
      <td align="left">US02</td>
      <td align="left">View SafePlant benefits and advantages</td>
      <td align="left">T02</td>
      <td align="left">Sección de beneficios</td>
      <td align="left">Implementar la sección "El valor de SafePlant para tu planta" con las ventajas de la solución.</td>
      <td align="left">2</td>
      <td align="left">Sanchez Gonzales, Gabriel</td>
      <td align="left">Done</td>
    </tr>
    <tr>
      <td align="left">US05</td>
      <td align="left">View system technical architecture</td>
      <td align="left">T03</td>
      <td align="left">Sección de arquitectura técnica</td>
      <td align="left">Implementar la sección que explica la relación entre dispositivos ESP32, IoT Gateway, nube, aplicación móvil y aplicación web.</td>
      <td align="left">2</td>
      <td align="left">Sanchez Gonzales, Gabriel</td>
      <td align="left">Done</td>
    </tr>
    <tr>
      <td align="left" rowspan="2">US09</td>
      <td align="left" rowspan="2">Navigate to the governance and metrics web application</td>
      <td align="left">T04</td>
      <td align="left">Call-to-action hacia la aplicación web</td>
      <td align="left">Incluir en la landing el acceso a la aplicación web para el Encargado de Planta. El enlace apunta aún a un dominio provisional y debe actualizarse a la URL desplegada.</td>
      <td align="left">1</td>
      <td align="left">Sanchez Gonzales, Gabriel</td>
      <td align="left">To-Review</td>
    </tr>
    <tr>
      <td align="left">T05</td>
      <td align="left">Despliegue de la landing en GitHub Pages</td>
      <td align="left">Publicar la landing page desde el repositorio <code>landing-page</code> de la organización Macallys.</td>
      <td align="left">1</td>
      <td align="left">Sanchez Gonzales, Gabriel</td>
      <td align="left">Done</td>
    </tr>
    <tr>
      <td align="left" rowspan="2">US08</td>
      <td align="left" rowspan="2">Plant Manager sign-in on the web application</td>
      <td align="left">T06</td>
      <td align="left">Configuración inicial del proyecto Angular</td>
      <td align="left">Crear el proyecto Angular, definir la estructura por features (<code>core</code>, <code>shared</code>, <code>features</code>) y los environments.</td>
      <td align="left">3</td>
      <td align="left">Iglesias Pérez, Sergio Sebastián</td>
      <td align="left">Done</td>
    </tr>
    <tr>
      <td align="left">T07</td>
      <td align="left">Vistas de inicio de sesión y registro</td>
      <td align="left">Implementar las vistas Sign In y Sign Up, el store de sesión, el guard de rutas y el interceptor de autenticación, con API de muestra.</td>
      <td align="left">6</td>
      <td align="left">Sanchez Gonzales, Gabriel</td>
      <td align="left">Done</td>
    </tr>
    <tr>
      <td align="left">US23</td>
      <td align="left">Plant metrics dashboard and full history</td>
      <td align="left">T08</td>
      <td align="left">Dashboard de métricas e historial</td>
      <td align="left">Implementar el dashboard de métricas por área, el historial de alertas y el gráfico de telemetría, con datos de muestra.</td>
      <td align="left">8</td>
      <td align="left">Sanchez Gonzales, Gabriel</td>
      <td align="left">Done</td>
    </tr>
    <tr>
      <td align="left">US11</td>
      <td align="left">Create user accounts as Plant Manager</td>
      <td align="left">T09</td>
      <td align="left">Directorio y creación de cuentas</td>
      <td align="left">Implementar el directorio de cuentas y el panel lateral de creación de cuentas para Safety Supervisors y Plant Managers.</td>
      <td align="left">5</td>
      <td align="left">Sanchez Gonzales, Gabriel</td>
      <td align="left">Done</td>
    </tr>
    <tr>
      <td align="left">US12</td>
      <td align="left">Assign user roles and permissions</td>
      <td align="left">T10</td>
      <td align="left">Administración de roles</td>
      <td align="left">Implementar la asignación y modificación de roles desde el directorio de cuentas.</td>
      <td align="left">3</td>
      <td align="left">Sanchez Gonzales, Gabriel</td>
      <td align="left">Done</td>
    </tr>
    <tr>
      <td align="left">—</td>
      <td align="left">Despliegue de la aplicación web</td>
      <td align="left">T11</td>
      <td align="left">Despliegue en Vercel</td>
      <td align="left">Publicar la aplicación web Angular en Vercel con despliegue automático desde el repositorio <code>safeplant-web-client</code>.</td>
      <td align="left">1</td>
      <td align="left">Iglesias Pérez, Sergio Sebastián</td>
      <td align="left">Done</td>
    </tr>
    <tr>
      <td align="left" rowspan="5">TS21</td>
      <td align="left" rowspan="5">User authentication API endpoint for mobile and web</td>
      <td align="left">T12</td>
      <td align="left">Estructura modular del backend</td>
      <td align="left">Crear la solución ASP.NET Core con hosts separados (<code>Cloud.Api</code>, <code>Plant.Host</code>), módulos por bounded context, Shared Kernel con CQRS ligero y manejo global de errores.</td>
      <td align="left">6</td>
      <td align="left">Iglesias Pérez, Sergio Sebastián</td>
      <td align="left">Done</td>
    </tr>
    <tr>
      <td align="left">T13</td>
      <td align="left">Endpoint de inicio de sesión con JWT</td>
      <td align="left">Implementar <code>POST /api/v1/auth/login</code> con validación de credenciales, emisión de JWT y control de acceso por canal (web o móvil).</td>
      <td align="left">6</td>
      <td align="left">Iglesias Pérez, Sergio Sebastián</td>
      <td align="left">Done</td>
    </tr>
    <tr>
      <td align="left">T14</td>
      <td align="left">Endpoints de gestión de cuentas</td>
      <td align="left">Implementar los endpoints de creación, listado, cambio de rol y habilitación de cuentas (restringidos al Plant Manager), además de cierre de sesión y recuperación de credenciales.</td>
      <td align="left">4</td>
      <td align="left">Iglesias Pérez, Sergio Sebastián</td>
      <td align="left">Done</td>
    </tr>
    <tr>
      <td align="left">T15</td>
      <td align="left">Documentación OpenAPI</td>
      <td align="left">Exponer la especificación OpenAPI y Swagger UI de los endpoints de Identity &amp; Access.</td>
      <td align="left">1</td>
      <td align="left">Iglesias Pérez, Sergio Sebastián</td>
      <td align="left">Done</td>
    </tr>
    <tr>
      <td align="left">T16</td>
      <td align="left">Despliegue del backend en Azure App Service</td>
      <td align="left">Configurar el workflow de GitHub Actions que compila y despliega <code>Cloud.Api</code> en Azure App Service desde la rama <code>main</code>.</td>
      <td align="left">3</td>
      <td align="left">Iglesias Pérez, Sergio Sebastián</td>
      <td align="left">Done</td>
    </tr>
    <tr>
      <td align="left" rowspan="4">—</td>
      <td align="left" rowspan="4">Documentación del informe (TB1)</td>
      <td align="left">T17</td>
      <td align="left">Capítulo V: Solution UI/UX Design</td>
      <td align="left">Documentar wireframes, wireflows, mock-ups, user flows y prototipos de la landing page y las aplicaciones.</td>
      <td align="left">10</td>
      <td align="left">Gordillo Ramos, Santiago Alonso / Baldeon Vivar, Santiago Armando / Solano Armas, Angelo Héctor</td>
      <td align="left">Done</td>
    </tr>
    <tr>
      <td align="left">T18</td>
      <td align="left">Capítulo VI: Software Configuration Management</td>
      <td align="left">Documentar el entorno de desarrollo, la gestión del código fuente, las convenciones de código y la configuración de despliegue.</td>
      <td align="left">4</td>
      <td align="left">Gordillo Ramos, Santiago Alonso</td>
      <td align="left">Done</td>
    </tr>
    <tr>
      <td align="left">T19</td>
      <td align="left">Sprint 1 en el informe</td>
      <td align="left">Documentar el Sprint 1: planning, sprint backlog, evidencias de desarrollo, ejecución, servicios, despliegue y colaboración.</td>
      <td align="left">5</td>
      <td align="left">Sanchez Gonzales, Gabriel / Huaman Cuba, Johan Giovani</td>
      <td align="left">Done</td>
    </tr>
    <tr>
      <td align="left">T20</td>
      <td align="left">Correcciones de AV1, conclusiones y anexos</td>
      <td align="left">Aplicar las correcciones de estilo y referencias de la entrega AV1 y actualizar conclusiones, bibliografía y anexos.</td>
      <td align="left">4</td>
      <td align="left">Solano Armas, Angelo Héctor</td>
      <td align="left">Done</td>
    </tr>
  </tbody>
</table>

<a id="s-6-2-1-4"></a>
#### 6.2.1.4. Development Evidence for Sprint Review

Durante el Sprint 1 se implementó la landing page de SafePlant, las vistas de la aplicación web del Encargado de Planta en Angular y el bounded context Identity & Access del backend en ASP.NET Core, con los endpoints de autenticación y gestión de cuentas. Las siguientes tablas registran los commits de cada repositorio de la organización Macallys.

**Repositorios de producto (landing page, aplicación web y backend)**

Se registra el historial completo de los tres repositorios, ya que fueron creados para este incremento.

| Repository | Branch | Commit Id | Commit Message | Commit Message Body | Committed on (Date) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Macallys/landing-page | main | [9ba1a93](https://github.com/Macallys/landing-page/commit/9ba1a93dd2923408c13ece85a9839d930a680a1e) | Initial commit | - | 2026-09-09 |
| Macallys/landing-page | main | [ccefe6d](https://github.com/Macallys/landing-page/commit/ccefe6d1b451594ddc3d8d4898fe4059c8ceac4b) | feat: add landing page | - | 2026-09-09 |
| Macallys/safeplant-web-client | develop | [695489b](https://github.com/Macallys/safeplant-web-client/commit/695489b12b749aa18fbeffb8f17933abc79fcb33) | initial commit | - | 2026-10-02 |
| Macallys/safeplant-web-client | develop | [eaec417](https://github.com/Macallys/safeplant-web-client/commit/eaec417bcf9c478464338a9b9c215dec0003cecd) | chore: initial setup | - | 2026-10-02 |
| Macallys/safeplant-web-client | develop | [5e084de](https://github.com/Macallys/safeplant-web-client/commit/5e084de9ef9c2218d0db995505b3bb7020148986) | feat: add sign up, sign in, metrics, history features and pages | - | 2026-10-04 |
| Macallys/safeplant-web-client | main | [d1528d7](https://github.com/Macallys/safeplant-web-client/commit/d1528d733763e28654f4201f05a80a7d64a7cbb8) | feat: administracion de roles | - | 2026-10-07 |
| Macallys/safeplant-web-backend | develop | [7d011b6](https://github.com/Macallys/safeplant-web-backend/commit/7d011b6a4271da4cfaf1fa60a2d22c1194d8ddbf) | chore: initial setup | - | 2026-10-04 |
| Macallys/safeplant-web-backend | develop | [be399e5](https://github.com/Macallys/safeplant-web-backend/commit/be399e58592de36e84d9ab2269ec784c81393751) | chore: global error and extensions | - | 2026-10-06 |
| Macallys/safeplant-web-backend | develop | [b2d0c6a](https://github.com/Macallys/safeplant-web-backend/commit/b2d0c6af4c7ba3438b1b175e792b5ae552264ecc) | chore: light cqrs initialization - shared kernel initialization | - | 2026-10-08 |
| Macallys/safeplant-web-backend | develop | [69cd193](https://github.com/Macallys/safeplant-web-backend/commit/69cd1937519e18ed3f3c8a5e42d30ea3f760232b) | feat: sign in endpoints - jwt tokens | - | 2026-10-08 |
| Macallys/safeplant-web-backend | develop | [36fa06f](https://github.com/Macallys/safeplant-web-backend/commit/36fa06f4ceb74c0b09701f7d2f4897a397063ec2) | chore: Swagger UI | - | 2026-10-08 |
| Macallys/safeplant-web-backend | develop | [5abf8c9](https://github.com/Macallys/safeplant-web-backend/commit/5abf8c973ef31ad276c8905e6aacba7be6046b86) | Add or update the Azure App Service build and deployment workflow config | - | 2026-10-08 |
| Macallys/safeplant-web-backend | develop | [57c278c](https://github.com/Macallys/safeplant-web-backend/commit/57c278c1d07f5526e9a1f0e4bc39d9d31373a6e3) | feat: web manager endpoints for user management | - | 2026-10-08 |
| Macallys/safeplant-web-backend | develop | [2c6d416](https://github.com/Macallys/safeplant-web-backend/commit/2c6d416f0c7b02dfbf126c4f32124a1340e0c192) | chore: project refactorization :c | - | 2026-10-08 |
| Macallys/safeplant-web-backend | develop | [1c595f8](https://github.com/Macallys/safeplant-web-backend/commit/1c595f81906741d7a14fbffc4f5478adb6172f77) | Merge branch 'main' of github.com:Macallys/safeplant-web-backend into develop wa | - | 2026-10-08 |
| Macallys/safeplant-web-backend | develop | [9b8aa1b](https://github.com/Macallys/safeplant-web-backend/commit/9b8aa1bd19cda70722d71097de40466161f151b2) | feat: azure workflow | - | 2026-10-08 |

**Repositorio del informe (Report)**

Commits realizados sobre el repositorio del informe entre el 20 de septiembre y el 7 de octubre de 2026, posteriores a la entrega AV1. Se conservan los mensajes originales, incluidos los generados por la interfaz web de GitHub al subir archivos y los de integración de ramas, para mantener la trazabilidad real del trabajo.

| Repository | Branch | Commit Id | Commit Message | Commit Message Body | Committed on (Date) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Macallys/Report | develop | [f9dc3c7](https://github.com/Macallys/Report/commit/f9dc3c757e088e425bb11659906c57452685df45) | Agrega exportacion a PDF e ignora el perfil de Chrome | - | 2026-09-20 |
| Macallys/Report | develop | [59d61ad](https://github.com/Macallys/Report/commit/59d61adcc4dd0043bb670354df43a1c739d7f2ea) | Update 6. and fix chapter 1 | Updated the text to improve clarity and precision regarding occupational health risks, regulatory compliance, and the implementation of safety systems in the industrial sector. Added references to specific regulations and statistics to support the claims made. | 2026-10-02 |
| Macallys/Report | develop | [c76e5c9](https://github.com/Macallys/Report/commit/c76e5c9cb6f0c8bfaeeb38570c26b4ad22bff9af) | Document source code management and commit standards | Added details about source code management and commit standards. | 2026-10-04 |
| Macallys/Report | develop | [b1350fb](https://github.com/Macallys/Report/commit/b1350fbf0d4a8c4a67494952b7ae50381fbc8ea0) | docs: add chapter 5 | - | 2026-10-04 |
| Macallys/Report | develop | [b4cfb2b](https://github.com/Macallys/Report/commit/b4cfb2b48f2d2b2dbcc040a64912b60e68a4874f) | Merge branch 'develop' of https://github.com/Macallys/Report into develop | - | 2026-10-05 |
| Macallys/Report | develop | [f9183da](https://github.com/Macallys/Report/commit/f9183dad1b13212934e0e720f5ab1539fb2d1c0e) | roles | - | 2026-10-07 |
| Macallys/Report | develop | [f68236e](https://github.com/Macallys/Report/commit/f68236e0202a24c10ce1b3740e6619da83896f94) | landing page mobile web browser | - | 2026-10-07 |
| Macallys/Report | develop | [8cc8512](https://github.com/Macallys/Report/commit/8cc8512096f93fc025498cd7f812a65cf4e4a29c) | Document software development environment configuration | - | 2026-10-07 |
| Macallys/Report | develop | [cce8238](https://github.com/Macallys/Report/commit/cce8238ec8241232f2125d47521a774f9d440f71) | Document source code style guide and conventions | - | 2026-10-07 |
| Macallys/Report | develop | [b4bef89](https://github.com/Macallys/Report/commit/b4bef8959ae66a446ea8814488dae55ff701869f) | Add files via upload | - | 2026-10-07 |
| Macallys/Report | develop | [52fabcd](https://github.com/Macallys/Report/commit/52fabcd98ffa092220a9ab514407ce73178afe29) | Add files via upload | - | 2026-10-07 |
| Macallys/Report | develop | [4dce568](https://github.com/Macallys/Report/commit/4dce5684ad738b23f654295fc2714219cf747002) | Update landing page wireframe | - | 2026-10-07 |
| Macallys/Report | develop | [b460ffa](https://github.com/Macallys/Report/commit/b460ffabe69bb4be72316e0b67be60cbfb461329) | wireframes section with descriptions and images | - | 2026-10-07 |
| Macallys/Report | develop | [958245f](https://github.com/Macallys/Report/commit/958245f65289766a5fb7e7aa1a44f7871a9b30fe) | Add files via upload | - | 2026-10-07 |
| Macallys/Report | develop | [99c7424](https://github.com/Macallys/Report/commit/99c7424b1dbd0106dff6b704ef712e8634767334) | Add files via upload | - | 2026-10-07 |
| Macallys/Report | develop | [5afe6f1](https://github.com/Macallys/Report/commit/5afe6f161516112219824fe5169980c136cd5d40) | Update wireframes in informe.md | - | 2026-10-07 |
| Macallys/Report | develop | [b0abcdc](https://github.com/Macallys/Report/commit/b0abcdc3401d1c60b68c2f508dd23bd64a0fc175) | Add files via upload | - | 2026-10-07 |
| Macallys/Report | develop | [7a1ea3f](https://github.com/Macallys/Report/commit/7a1ea3feac002ba8f0e9e19ac673c2385df8ed46) | Update repository name and source code style guide | - | 2026-10-07 |
| Macallys/Report | develop | [2276b1d](https://github.com/Macallys/Report/commit/2276b1d61de0145163346766f0fb9499aa528695) | Delete assets/05-capitulo-v/applications/WF_1.png | - | 2026-10-07 |
| Macallys/Report | develop | [521de2a](https://github.com/Macallys/Report/commit/521de2a0cf25774881e5ac8548917072b2e06381) | Delete assets/05-capitulo-v/applications/WF_2.png | - | 2026-10-07 |
| Macallys/Report | develop | [2abb624](https://github.com/Macallys/Report/commit/2abb6243f367d1c5bfae2e5bc66a3c55215a1438) | Add files via upload | - | 2026-10-07 |
| Macallys/Report | develop | [1a00272](https://github.com/Macallys/Report/commit/1a00272f3f318e8412462580ac08543db9402a45) | Add files via upload | - | 2026-10-07 |
| Macallys/Report | develop | [71620b3](https://github.com/Macallys/Report/commit/71620b3e5dcd3f8ca22f88b07fb1870688de0b6f) | correciones style | - | 2026-10-07 |
| Macallys/Report | develop | [e49b979](https://github.com/Macallys/Report/commit/e49b979b54cc8a3dd1bfcfba0c9457f66ad3ad84) | style 2 | - | 2026-10-07 |
| Macallys/Report | develop | [93aa32d](https://github.com/Macallys/Report/commit/93aa32d80ba21087ee35ce5b6161772ffa393336) | docs: add sprint 1 | - | 2026-10-07 |
| Macallys/Report | develop | [422a2d2](https://github.com/Macallys/Report/commit/422a2d2f180650c5f2dd5a06f5554b3fba312fb9) | Merge branch 'develop' of https://github.com/Macallys/Report into develop | - | 2026-10-07 |
| Macallys/Report | develop | [f379e9b](https://github.com/Macallys/Report/commit/f379e9b49dbe7c2c1893d6d142416b501a9db0c8) | correcion 2 | - | 2026-10-07 |
| Macallys/Report | develop | [676f2e1](https://github.com/Macallys/Report/commit/676f2e1fcaf644af0d9a363598f1a0006ef85d03) | Merge origin/feature/chapter-02 into develop | - | 2026-10-07 |
| Macallys/Report | develop | [2e4dadf](https://github.com/Macallys/Report/commit/2e4dadf9dd3d88435650babb449f24c355fb819a) | correcciones de referencias | - | 2026-10-07 |
| Macallys/Report | develop | [16e38ea](https://github.com/Macallys/Report/commit/16e38eaf750e182d96c1c76d64f35c8833e1ad9f) | anexos correccion de link | - | 2026-10-07 |

**Trazabilidad por User Story**

| User Story | Tarea | Commits | Estado |
| :--- | :--- | :--- | :---: |
| US01 View SafePlant system information | T01 | `ccefe6d` | Done |
| US02 View SafePlant benefits and advantages | T02 | `ccefe6d` | Done |
| US05 View system technical architecture | T03 | `ccefe6d` | Done |
| US09 Navigate to the governance and metrics web application | T04, T05 | `ccefe6d` | To-Review |
| US08 Plant Manager sign-in on the web application | T06, T07 | `695489b`, `eaec417`, `5e084de` | Done |
| US23 Plant metrics dashboard and full history | T08 | `5e084de` | Done |
| US11 Create user accounts as Plant Manager | T09 | `d1528d7` (vista web), `57c278c` (endpoints) | Done |
| US12 Assign user roles and permissions | T10 | `d1528d7` (vista web), `57c278c` (endpoints) | Done |
| TS21 User authentication API endpoint for mobile and web | T12 – T16 | `7d011b6`, `be399e5`, `b2d0c6a`, `69cd193`, `57c278c`, `36fa06f`, `5abf8c9`, `2c6d416`, `9b8aa1b` | Done |


<a id="s-6-2-1-5"></a>
#### 6.2.1.5. Testing Suite Evidence for Sprint Review

En el Sprint 1 el equipo priorizó la construcción de la estructura modular del backend y los endpoints de Identity & Access, por lo que no se implementaron Unit Tests, Integration Tests ni Acceptance Tests automatizados para los Web Services. La única especificación existente es la prueba por defecto del componente raíz generada por Angular (`src/app/app.spec.ts`) en `safeplant-web-client`.

Para el Sprint 2 se incorporará un proyecto de pruebas en `safeplant-web-backend` con Unit Tests sobre los servicios de dominio de Identity & Access (`SignInService`, `DirectoryService`, `RecoveryService`) y archivos `.feature` en Gherkin para los escenarios de request/response de TS21, US11 y US12.

<a id="s-6-2-1-6"></a>
#### 6.2.1.6. Execution Evidence for Sprint Review

Al cierre del Sprint 1, la landing page de SafePlant está disponible públicamente y presenta el propósito del sistema, el monitoreo en tiempo real, la respuesta automática, el flujo de detección a acción, los beneficios y la arquitectura técnica. La aplicación web del Encargado de Planta está desplegada con sus vistas navegables: inicio de sesión, registro, dashboard de métricas, historial de alertas y directorio de cuentas con asignación de roles. Estas vistas trabajan con datos de muestra hasta su integración con el backend en el Sprint 2.

**URL de la landing page:** [https://macallys.github.io/landing-page/](https://macallys.github.io/landing-page/)


**URL de la aplicación web:** [https://safeplant-web-client.vercel.app/signIn](https://safeplant-web-client.vercel.app/signIn)


<a id="s-6-2-1-7"></a>
#### 6.2.1.7. Services Documentation Evidence for Sprint Review

En este sprint se documentaron con OpenAPI (Swagger UI) los endpoints del bounded context Identity & Access, implementados en el repositorio safeplant-web-backend. Los endpoints de la sección superior son públicos; los de gestión de sesión y cuentas requieren un token de acceso válido y, en el caso de la gestión de cuentas, el rol PlantManager. Los errores se devuelven en un formato uniforme con un código (invalid_credentials, role_not_allowed, etc.) y un identificador de correlación.

| Endpoint | Verbo HTTP | Sintaxis de llamada | Parámetros | Response | Commit |
| :--- | :---: | :--- | :--- | :--- | :---: |
| Sign in | POST | `/api/v1/auth/login` | Body JSON: `email`, `password`, `channel` (`Web` / `Mobile`) | `200 OK` con `accessToken`, `role` y `expiresAt`. `401` `invalid_credentials`; `403` `account_disabled` o `role_not_allowed` si el rol no corresponde al canal. | `69cd193` |
| Request recovery | POST | `/api/v1/auth/recovery` | Body JSON: `email` | `202 Accepted`. | `57c278c` |
| Reset password | POST | `/api/v1/auth/reset` | Body JSON: `token`, `password` | `204 No Content`. `422` `recovery_expired` si el token no es válido o expiró. | `57c278c` |
| Sign out | POST | `/api/v1/auth/logout` | Header `Authorization: Bearer <token>` | `204 No Content`. `401` `unauthorized`. | `57c278c` |
| Create user | POST | `/api/v1/users` | Header `Authorization`; Body JSON: `email`, `password`, `role` (`PlantManager` / `Supervisor`) | `201 Created` con `id`, `email`, `role`, `enabled`. `403` `role_not_allowed`; `409` `email_already_exists`. | `57c278c` |
| List users | GET | `/api/v1/users` | Header `Authorization` | `200 OK` con `items`: lista de cuentas (`id`, `email`, `role`, `enabled`). | `57c278c` |
| Assign role | PATCH | `/api/v1/users/{accountId}/role` | Header `Authorization`; path `accountId`; Body JSON: `role` | `200 OK` con la cuenta actualizada. `404` `account_not_found`. | `57c278c` |
| Enable / disable user | PATCH | `/api/v1/users/{accountId}/enabled` | Header `Authorization`; path `accountId`; Body JSON: `enabled` (boolean) | `200 OK` con la cuenta actualizada. `404` `account_not_found`. | `57c278c` |

**Ejemplo de interacción (Sign in):**

```http
POST /api/v1/auth/login
Content-Type: application/json

{
  "email": "manager@safeplant.io",
  "password": "********",
  "channel": "Web"
}
```

```json
{
  "accessToken": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "role": "PlantManager",
  "expiresAt": "2026-10-08T23:00:00+00:00"
}
```

**Documentación desplegada:** la especificación OpenAPI se expone en `/openapi/v1.json` y Swagger UI en `/swagger`. En este sprint ambos están habilitados en el entorno de desarrollo (`https://localhost:7222/swagger`).

**Repositorio de Web Services:** [https://github.com/Macallys/safeplant-web-backend](https://github.com/Macallys/safeplant-web-backend) — commits de documentación: `36fa06f` (Swagger UI).

<a id="s-6-2-1-8"></a>
#### 6.2.1.8. Software Deployment Evidence for Sprint Review

En el Sprint 1 se desplegaron los tres productos implementados. Las plataformas actuales difieren de la arquitectura objetivo descrita en la sección 6.1.4 (Azure Static Web Apps) para la landing page y la aplicación web; la migración se evaluará en el Sprint 2.

| Producto | Repositorio | Plataforma | URL | Mecanismo |
| :--- | :--- | :--- | :--- | :--- |
| Landing page | `landing-page` | GitHub Pages | [https://macallys.github.io/landing-page/](https://macallys.github.io/landing-page/) | Publicación desde la rama `main` |
| Aplicación web | `safeplant-web-client` | Vercel | [https://safeplant-web-client.vercel.app](https://safeplant-web-client.vercel.app) | Integración con GitHub, despliegue automático en cada push |
| Backend (Cloud API) | `safeplant-web-backend` | Azure App Service (`wa-safeplant-cloudbackend-prod`) | `https://wa-safeplant-cloudbackend-prod.azurewebsites.net` | Workflow de GitHub Actions (`5abf8c9`, `9b8aa1b`) |

Los pasos realizados fueron los siguientes:

1. **Landing page:** se habilitó GitHub Pages en el repositorio `landing-page` de la organización Macallys, sirviendo `index.html` y `styles.css` desde la rama `main`. Al ser un sitio estático no requiere proceso de compilación.
2. **Aplicación web:** se importó el repositorio `safeplant-web-client` en Vercel, que detecta el proyecto Angular, ejecuta la compilación y publica una nueva versión con cada integración.
3. **Backend:** se creó el recurso Azure App Service `wa-safeplant-cloudbackend-prod` y se generó el workflow de GitHub Actions que, en cada push a `main`, compila la solución con .NET 10, publica el proyecto `Cloud.Api` y lo despliega en el slot `Production` autenticándose con Azure mediante OpenID Connect.


<a id="s-6-2-1-9"></a>
#### 6.2.1.9. Team Collaboration Insights during Sprint

La colaboración del Sprint 1 se midió sobre los cuatro repositorios de la organización. Para el repositorio `Report` se consideran los commits del 20 de septiembre al 7 de octubre de 2026; para los repositorios de producto, su historial completo. Las cifras son reproducibles con `git shortlog -sn --all` y agrupan las distintas identidades de Git de un mismo integrante.

| Integrante | `Report` | `landing-page` | `safeplant-web-client` | `safeplant-web-backend` | Total |
| :--- | ---: | ---: | ---: | ---: | ---: |
| Gordillo Ramos, Santiago Alonso | 17 | 0 | 0 | 0 | 17 |
| Iglesias Pérez, Sergio Sebastián | 0 | 0 | 2 | 10 | 12 |
| Solano Armas, Angelo Héctor | 10 | 0 | 0 | 0 | 10 |
| Sanchez Gonzales, Gabriel | 3 | 2 | 2 | 0 | 7 |
| Baldeon Vivar, Santiago Armando | 0 | 0 | 0 | 0 | 0 |
| Huaman Cuba, Johan Giovani | 0 | 0 | 0 | 0 | 0 |
| **Total** | **30** | **2** | **4** | **10** | **46** |

La implementación de los productos se concentró en dos integrantes: Sanchez Gonzales, Gabriel, en la landing page y las vistas de la aplicación web, e Iglesias Pérez, Sergio Sebastián, en la configuración del proyecto Angular y el backend. La documentación del informe se distribuyó principalmente entre Gordillo Ramos, Santiago Alonso, Solano Armas, Angelo Héctor y Sanchez Gonzales, Gabriel.

Para el Sprint 2 el equipo adopta los siguientes compromisos:

- Cada User Story se desarrollará en su propia rama `feature/*`, creada por el integrante responsable, e integrada a `develop` mediante Pull Request revisado por otro integrante.
- Todos los integrantes tendrán commits propios en al menos un repositorio de producto.
- El trabajo realizado en pareja se registrará con el trailer `Co-authored-by` para que el historial refleje a ambos participantes.

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
