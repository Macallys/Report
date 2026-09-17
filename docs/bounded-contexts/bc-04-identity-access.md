<a id="s-4-2-4"></a>
# 4.2.4. Bounded Context: Identity & Access

**Navegación:** [Capítulo IV](../04-capitulo-iv-solution-software-design.md) · [Índice](../00-student-outcome.md#s-tabla-contenidos)

---

Identity & Access resuelve quién entra a SafePlant, con qué rol y por qué canal —app móvil del supervisor o cliente web del encargado de planta—, y la recuperación de credenciales. Es un **Generic Subdomain**: no mide la planta ni evalúa exposición, solo concede o niega la sesión que Plant Monitoring y Safety & Actuation exigen vía Open Host Service. Vive enteramente en el monolito cloud; el Edge no administra usuarios, solo autentica dispositivos (Device & Edge Management).

Ubiquitous language: *User account* · *User role* · *Session* · *Sign in* · *Session granted* · *Protected action denied* · *Credential recovery* · *Channel (mobile / web)* · *Supervisor* · *Plant manager*.

<a id="s-4-2-4-1"></a>
## 4.2.4.1. Domain Layer

El core del contexto son tres aggregates —`UserAccount`, `Session`, `CredentialRecovery`— con sus value objects, un domain service de autorización y las interfaces de repositorio que persisten cada aggregate.

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
      <td align="left">`UserAccount`</td>
      <td align="left">Aggregate Root</td>
      <td align="left">Cuenta de un supervisor o encargado de planta, con su rol. Un correo = una cuenta (`E-07`).</td>
      <td align="left">`id`, `email`, `passwordHash`, `role`, `enabled`</td>
      <td align="left">`create()`, `assignRole()`, `disable()`, `verifyPassword()`</td>
      <td align="left">1—0..* `Session` (owns); 1—0..* `CredentialRecovery` (requests)</td>
    </tr>
    <tr>
      <td align="left">`Session`</td>
      <td align="left">Aggregate Root</td>
      <td align="left">Sesión activa en un canal (móvil o web) con token vigente (`C-06`–`C-09`).</td>
      <td align="left">`id`, `accountId`, `channel`, `token`, `issuedAt`, `expiresAt`, `closedAt`</td>
      <td align="left">`grant()`, `close()`, `isValid()`</td>
      <td align="left">pertenece a 1 `UserAccount`</td>
    </tr>
    <tr>
      <td align="left">`CredentialRecovery`</td>
      <td align="left">Aggregate Root</td>
      <td align="left">Proceso de recuperación de credenciales con vencimiento (TTL) (`C-03`–`C-05`).</td>
      <td align="left">`id`, `accountId`, `token`, `requestedAt`, `expiresAt`, `usedAt`</td>
      <td align="left">`request()`, `reset()`, `isExpired()`</td>
      <td align="left">pertenece a 1 `UserAccount`</td>
    </tr>
    <tr>
      <td align="left">`Email`</td>
      <td align="left">Value Object</td>
      <td align="left">Dirección de correo validada, única por cuenta.</td>
      <td align="left">`value`</td>
      <td align="left">`equals()`</td>
      <td align="left">usado por `UserAccount`</td>
    </tr>
    <tr>
      <td align="left">`UserRole`</td>
      <td align="left">Value Object (Enum)</td>
      <td align="left">Rol de canal: `Supervisor` o `PlantManager`.</td>
      <td align="left">`value`</td>
      <td align="left">—</td>
      <td align="left">usado por `UserAccount`</td>
    </tr>
    <tr>
      <td align="left">`Channel`</td>
      <td align="left">Value Object (Enum)</td>
      <td align="left">Canal de acceso: `Mobile` o `Web`.</td>
      <td align="left">`value`</td>
      <td align="left">—</td>
      <td align="left">usado por `Session`</td>
    </tr>
    <tr>
      <td align="left">`SessionToken`</td>
      <td align="left">Value Object</td>
      <td align="left">Token opaco de sesión.</td>
      <td align="left">`value`</td>
      <td align="left">`equals()`</td>
      <td align="left">usado por `Session`</td>
    </tr>
    <tr>
      <td align="left">`RecoveryToken`</td>
      <td align="left">Value Object</td>
      <td align="left">Token opaco de recuperación.</td>
      <td align="left">`value`</td>
      <td align="left">`equals()`</td>
      <td align="left">usado por `CredentialRecovery`</td>
    </tr>
    <tr>
      <td align="left">`AccessPolicy`</td>
      <td align="left">Domain Service</td>
      <td align="left">Evalúa si una acción protegida es permitida según rol y canal de la sesión (`C-08`). Setup de planta y override exigen supervisor **móvil**; web deniega.</td>
      <td align="left">—</td>
      <td align="left">`isActionAllowed()`</td>
      <td align="left">evalúa `Session`, `UserRole`</td>
    </tr>
    <tr>
      <td align="left">`IEmailSender`</td>
      <td align="left">Port (interface)</td>
      <td align="left">Puerto de salida hacia el servicio de recuperación de credenciales por correo.</td>
      <td align="left">—</td>
      <td align="left">`send()`</td>
      <td align="left">implementado en Infrastructure (`XS-01`)</td>
    </tr>
    <tr>
      <td align="left">`IUserAccountRepository`</td>
      <td align="left">Repository (interface)</td>
      <td align="left">Persistencia de `UserAccount`.</td>
      <td align="left">—</td>
      <td align="left">`findById()`, `findByEmail()`, `save()`</td>
      <td align="left">implementada en Infrastructure</td>
    </tr>
    <tr>
      <td align="left">`ISessionRepository`</td>
      <td align="left">Repository (interface)</td>
      <td align="left">Persistencia de `Session`.</td>
      <td align="left">—</td>
      <td align="left">`findByToken()`, `save()`</td>
      <td align="left">implementada en Infrastructure</td>
    </tr>
    <tr>
      <td align="left">`ICredentialRecoveryRepository`</td>
      <td align="left">Repository (interface)</td>
      <td align="left">Persistencia de `CredentialRecovery`.</td>
      <td align="left">—</td>
      <td align="left">`findByToken()`, `save()`</td>
      <td align="left">implementada en Infrastructure</td>
    </tr>
  </tbody>
</table>

<a id="s-4-2-4-2"></a>
## 4.2.4.2. Interface Layer

Tres controllers HTTP exponen el contexto hacia el Supervisor Mobile App y el Plant Manager Web Client. Identity & Access no consume MQTT: no hay Consumer, la autenticación de dispositivos vive en Device & Edge Management (`C-14`).

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
      <td align="left">`UserAccountController`</td>
      <td align="left">Controller</td>
      <td align="left">Alta de cuentas, asignación de rol y directorio de usuarios.</td>
      <td align="left">`createUserAccount()`, `assignUserRole()`, `getUserAccountsDirectory()`</td>
      <td align="left">Plant Manager Web Client; Application Layer</td>
    </tr>
    <tr>
      <td align="left">`SessionController`</td>
      <td align="left">Controller</td>
      <td align="left">Sign-in único (canal como parámetro) y cierre de sesión.</td>
      <td align="left">`signIn()`, `closeSession()`</td>
      <td align="left">Supervisor Mobile App; Plant Manager Web Client; Application Layer</td>
    </tr>
    <tr>
      <td align="left">`CredentialRecoveryController`</td>
      <td align="left">Controller</td>
      <td align="left">Solicitud y reseteo de credenciales.</td>
      <td align="left">`requestCredentialRecovery()`, `resetCredentials()`</td>
      <td align="left">Plant Manager Web Client; Application Layer</td>
    </tr>
  </tbody>
</table>

<a id="s-4-2-4-3"></a>
## 4.2.4.3. Application Layer

Un handler por comando del contexto (`C-01`–`C-09`) más el query de directorio (`RM-01`). `C-05` y `C-09` (expiración de TTL) son handlers disparados por tiempo, no por un controller.

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
      <td align="left">`CreateUserAccountHandler`</td>
      <td align="left">Command Handler</td>
      <td align="left">Create user account (`C-01`)</td>
      <td align="left">Crea la cuenta validando correo único.</td>
      <td align="left">`IUserAccountRepository`</td>
    </tr>
    <tr>
      <td align="left">`AssignUserRoleHandler`</td>
      <td align="left">Command Handler</td>
      <td align="left">Assign user role (`C-02`)</td>
      <td align="left">Asigna o cambia el rol de una cuenta existente.</td>
      <td align="left">`IUserAccountRepository`</td>
    </tr>
    <tr>
      <td align="left">`RequestCredentialRecoveryHandler`</td>
      <td align="left">Command Handler</td>
      <td align="left">Request credential recovery (`C-03`)</td>
      <td align="left">Inicia la recuperación y notifica por correo.</td>
      <td align="left">`IUserAccountRepository`, `ICredentialRecoveryRepository`, `IEmailSender`</td>
    </tr>
    <tr>
      <td align="left">`ResetCredentialsHandler`</td>
      <td align="left">Command Handler</td>
      <td align="left">Reset credentials (`C-04`)</td>
      <td align="left">Aplica el nuevo password si el token es válido.</td>
      <td align="left">`ICredentialRecoveryRepository`, `IUserAccountRepository`</td>
    </tr>
    <tr>
      <td align="left">`ExpireCredentialRecoveryHandler`</td>
      <td align="left">Event Handler (scheduled)</td>
      <td align="left">Expire credential recovery (`C-05`)</td>
      <td align="left">Marca vencidos los procesos fuera de TTL.</td>
      <td align="left">`ICredentialRecoveryRepository`</td>
    </tr>
    <tr>
      <td align="left">`SignInHandler`</td>
      <td align="left">Command Handler</td>
      <td align="left">Sign in (`C-06`)</td>
      <td align="left">Valida credenciales y concede sesión según canal.</td>
      <td align="left">`IUserAccountRepository`, `ISessionRepository`</td>
    </tr>
    <tr>
      <td align="left">`CloseSessionHandler`</td>
      <td align="left">Command Handler</td>
      <td align="left">Close session (`C-07`)</td>
      <td align="left">Cierra la sesión activa.</td>
      <td align="left">`ISessionRepository`</td>
    </tr>
    <tr>
      <td align="left">`DenyProtectedActionHandler`</td>
      <td align="left">Command Handler</td>
      <td align="left">Attempt protected action (`C-08`)</td>
      <td align="left">Evalúa `AccessPolicy` y deniega si el rol/canal no corresponde.</td>
      <td align="left">`AccessPolicy`</td>
    </tr>
    <tr>
      <td align="left">`ExpireAccessTokenHandler`</td>
      <td align="left">Event Handler (scheduled)</td>
      <td align="left">Expire access token (`C-09`)</td>
      <td align="left">Cierra sesiones cuyo token venció.</td>
      <td align="left">`ISessionRepository`</td>
    </tr>
    <tr>
      <td align="left">`GetUserAccountsDirectoryHandler`</td>
      <td align="left">Query Handler</td>
      <td align="left">Get UserAccountsDirectory (`RM-01`)</td>
      <td align="left">Lista cuentas y roles para el Plant Manager.</td>
      <td align="left">`IUserAccountRepository`</td>
    </tr>
  </tbody>
</table>

<a id="s-4-2-4-4"></a>
## 4.2.4.4. Infrastructure Layer

Implementaciones de los tres repositorios y el adaptador de correo. Motor de base de datos y proveedor de email quedan `TBD` (no se asume Auth0/Cognito ni marca de email — DEC-005).

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
      <td align="left">`UserAccountRepository`</td>
      <td align="left">Repository (implementación)</td>
      <td align="left">`IUserAccountRepository`</td>
      <td align="left">Cloud Database (motor TBD)</td>
      <td align="left">Persistencia relacional de cuentas.</td>
    </tr>
    <tr>
      <td align="left">`SessionRepository`</td>
      <td align="left">Repository (implementación)</td>
      <td align="left">`ISessionRepository`</td>
      <td align="left">Cloud Database (motor TBD)</td>
      <td align="left">Persistencia relacional de sesiones.</td>
    </tr>
    <tr>
      <td align="left">`CredentialRecoveryRepository`</td>
      <td align="left">Repository (implementación)</td>
      <td align="left">`ICredentialRecoveryRepository`</td>
      <td align="left">Cloud Database (motor TBD)</td>
      <td align="left">Persistencia relacional de procesos de recuperación.</td>
    </tr>
    <tr>
      <td align="left">`EmailServiceAdapter`</td>
      <td align="left">Adapter</td>
      <td align="left">`IEmailSender`</td>
      <td align="left">Email Service (`XS-01`, proveedor TBD)</td>
      <td align="left">Envía el correo de recuperación de credenciales.</td>
    </tr>
  </tbody>
</table>

<a id="s-4-2-4-5"></a>
## 4.2.4.5. Bounded Context Software Architecture Component Level Diagrams

Identity & Access vive dentro del único container `Web Monolithic Backend`. Interface recibe las llamadas de las apps, Application orquesta comandos y queries, Domain concentra los aggregates y `AccessPolicy`, e Infrastructure implementa los repositorios y habla con `Cloud Database` y `Email Service`.

![Component Level Diagram](../../assets/04-capitulo-iv/bounded-contexts/bc-04-component.png)

<a id="s-4-2-4-6"></a>
## 4.2.4.6. Bounded Context Software Architecture Code Level Diagrams

<a id="s-4-2-4-6-1"></a>
### 4.2.4.6.1. Bounded Context Domain Layer Class Diagrams

![Domain Layer Class Diagram](../../assets/04-capitulo-iv/bounded-contexts/bc-04-domain-class.png)

<a id="s-4-2-4-6-2"></a>
### 4.2.4.6.2. Bounded Context Database Design Diagram

Modelo relacional lógico: `user_accounts`, `sessions` y `credential_recoveries`, con `email` y los hashes de token como `UNIQUE`, y llaves foráneas de `sessions`/`credential_recoveries` hacia `user_accounts`.

![Database Design Diagram](../../assets/04-capitulo-iv/bounded-contexts/bc-04-database.png)
