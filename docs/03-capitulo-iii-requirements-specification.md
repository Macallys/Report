**Navegación:** [Índice](./00-student-outcome.md#s-tabla-contenidos) · Anterior: [Capítulo II](./02-capitulo-ii-requirements-elicitation.md) · Siguiente: [Capítulo IV](./04-capitulo-iv-solution-software-design.md)

---

<a id="s-chapter-iii-requirements-specification"></a>
# Chapter III: Requirements Specification


<table>
  <thead>
    <tr>
      <th align="left">Epic ID</th>
      <th align="left">Title</th>
      <th align="left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td align="left">EP01</td>
      <td align="left">Startup and Product Landing Page</td>
      <td align="left">As a visitor, I want to learn about the SafePlant product, its benefits, and the responsible team so that I can evaluate the industrial safety and pollution-control solution and identify access to the mobile app for operation and technical configuration and to the web application for governance and metrics.</td>
    </tr>
    <tr>
      <td align="left">EP02</td>
      <td align="left">Registration and Authentication</td>
      <td align="left">As an authorized user, I want to authenticate on the channel matching my role — mobile app for the Safety Supervisor (operation and technical IoT configuration) and web application for the Plant Manager (user governance and metrics) — so that I can use the authorized functions of each segment in a controlled way.</td>
    </tr>
    <tr>
      <td align="left">EP03</td>
      <td align="left">Telemetry and Real-Time Monitoring</td>
      <td align="left">As a Safety Supervisor, I want to monitor CO₂, noise, and presence in real time by industrial areas from the mobile app, register areas and thresholds, associate sensors/actuators, and apply safety-system configuration or updates; and as a Plant Manager, I want to manage users and roles and consult the metrics dashboard and full history from the web application so that plant operations can be governed.</td>
    </tr>
    <tr>
      <td align="left">EP04</td>
      <td align="left">Presence-Based Exposure Assessment</td>
      <td align="left">As a Safety Supervisor, I want the system to correlate presence detected by sensors with CO₂ and noise environmental conditions so that personnel exposure in industrial areas can be identified and alerts prioritized from the mobile app.</td>
    </tr>
    <tr>
      <td align="left">EP05</td>
      <td align="left">Actuator Automation and Business Rules</td>
      <td align="left">As a Safety Supervisor, I want the system to automatically activate extractors, sirens, and acoustic barriers under risk conditions and to remotely override actuators from the mobile app so that personnel are protected and industrial pollution is reduced.</td>
    </tr>
    <tr>
      <td align="left">EP06</td>
      <td align="left">System Quality Attributes</td>
      <td align="left">As a Safety Supervisor and as a Plant Manager, I want SafePlant to meet performance, offline reliability, security, availability, and compatibility requirements for the mobile app for operation/technical configuration and the web application for governance and metrics so that the plant can be operated and administered continuously with information protection.</td>
    </tr>
    <tr>
      <td align="left">EP07</td>
      <td align="left">IoT Infrastructure, REST API, and Contingency</td>
      <td align="left">As a Developer, I want this epic to concentrate telemetry infrastructure, device authentication, TLS, offline SQLite, cloud synchronization, OTA, SLA metrics, and availability so that SafePlant operates reliably, securely, and resiliently.</td>
    </tr>
  </tbody>
</table>

<a id="s-3-1"></a>
## 3.1. User Stories and Technical Stories

This section contains the user stories and technical stories with acceptance criteria for SafePlant. Criteria use the Given-When-Then format in the third person to specify observable behavior.

US01: View SafePlant system information

As a visitor,
I want to learn the purpose and operation of the SafePlant system,
so that I can understand how it contributes to safety and environmental control in an industrial plant.

**Acceptance Criteria**

Scenario 1: Presentation of the purpose of the system
Given the visitor accesses the SafePlant static website,
When the visitor consults the section of purpose of the system,
Then the site presents a description of the objective of SafePlant in the control of safety and industrial pollution.

Scenario 2: Presentation of monitored variables
Given the visitor accesses the SafePlant static website,
When the visitor consults the section of operation of the system,
Then the site presents information about the monitoring of CO₂ in ppm, noise in dB and personnel presence in industrial areas.

Scenario 3: Presentation of automatic actions
Given the visitor accesses the SafePlant static website,
When the visitor consults the section of automatic response of the system,
Then the site presents information about the activation of extractors, preventive sirens and acoustic barriers under risk conditions.

Scenario 4: Access from compatible device
Given the visitor accesses the site from a compatible device,
When the visitor consults the informational sections of the system,
Then the site presents the content in a readable and functional way in the device used.

*Related epic: EP01*

US02: View SafePlant benefits and advantages

As a visitor,
I want to learn the benefits and competitive advantages of SafePlant,
so that I can evaluate the value the solution brings to operational safety in an industrial plant.

**Acceptance Criteria**

Scenario 1: Benefits in prevention of risks
Given the visitor accesses the SafePlant website,
When the visitor consults the section of benefits of the solution,
Then the site presents the benefits related to the prevention of environmental risks and of safety for operators.

Scenario 2: Benefits in monitoring continuous
Given the visitor accesses the SafePlant website,
When the visitor consults the section of benefits of the solution,
Then the site presents the benefits related to the continuous environmental monitoring in real time from the mobile app.

Scenario 3: Benefits in industrial automation
Given the visitor accesses the SafePlant website,
When the visitor consults the section of benefits of the solution,
Then the site presents the benefits related to the automation of responses under hazardous conditions and the remote operational control.

*Related epic: EP01*

US03: View the development team

As a visitor,
I want to learn about the SafePlant development team,
so that I can obtain information about the organization responsible for the solution.

**Acceptance Criteria**

Scenario 1: Presentation of the development team
Given the visitor accesses the SafePlant website,
When the visitor consults the section of the development team,
Then the site presents the information of the members of the team with their roles in the project.

Scenario 2: Presentation of the responsible startup
Given the visitor accesses the SafePlant website,
When the visitor consults the institutional section of the startup,
Then the site presents the name of the startup, their mission and their relationship with the project SafePlant.

Scenario 3: Section of team without data available
Given the section of the development team no has members published,
When the visitor query that section,
Then the site informs that the information of the team is being updated.

Scenario 4: Query from compatible mobile device
Given the visitor accesses from a compatible mobile device,
When the visitor consults the section of the team and of the startup,
Then the site presents the content in a readable way and navigable in the device used.

*Related epic: EP01*

US04: Submit contact form

As a visitor,
I want to submit a contact request through the website,
so that I can communicate with the SafePlant team and obtain additional information about the solution.

**Acceptance Criteria**

Scenario 1: Submission successful of contact request
Given the visitor accesses the contact form of the site web
And the visitor provides name, email and message with data valid,
When the visitor confirms the submission of the contact request,
Then the system registers the request and confirms to the visitor that the message fue recibido correctly.

Scenario 2: Submission with data required incomplete
Given the visitor accesses the contact form of the site web
And the visitor no provides one or more data required,
When the visitor confirms the submission of the contact request,
Then the system rejects the submission and informs the required fields that must completarse.

Scenario 3: Submission with email no valid
Given the visitor accesses the contact form of the site web
And the visitor provides a email with format no valid,
When the visitor confirms the submission of the contact request,
Then the system rejects the submission and informs that the email no has a format valid.

*Related epic: EP01*

US05: View system technical architecture

As a visitor,
I want to learn the technical architecture of SafePlant,
so that I can understand how embedded devices, the IoT Gateway, the cloud, the mobile app for operation and technical configuration, and the web application for governance and metrics are integrated.

**Acceptance Criteria**

Scenario 1: Layer of embedded devices
Given the visitor accesses the SafePlant website,
When the visitor consults the section of architecture technical,
Then the site presents information about the devices ESP32, sensors of CO₂, noise and presence, and actuators physical of the system.

Scenario 2: Layer of IoT Gateway
Given the visitor accesses the SafePlant website,
When the visitor consults the section of architecture technical,
Then the site presents information about the IoT Gateway basado in Raspberry Pi with processing local and persistence of contingency.

Scenario 3: Layer of platform in the cloud and channels of user
Given the visitor accesses the SafePlant website,
When the visitor consults the section of architecture technical,
Then the site presents information about the API REST, the relational database, the mobile app for monitoring, operational control, and technical configuration of the system of safety, and the web application for user governance, metrics, and history.

*Related epic: EP01*

US06: Navigate to the operations mobile app

As a visitor,
I want to access the mobile app for monitoring, operational control, and technical configuration from the informational site,
so that I can sign in as a Safety Supervisor.

**Acceptance Criteria**

Scenario 1: Redirection toward the access of the mobile app
Given the visitor is in the SafePlant website,
When the visitor requests the access a the mobile app,
Then the system redirects to the visitor to the mobile app access or authentication point of SafePlant.

Scenario 2: Access identifiable in the main navigation
Given the visitor consults the SafePlant website,
When the visitor reviews the main navigation of the site,
Then the site presents a access identifiable toward the mobile app for operation and technical configuration.

Scenario 3: Differentiation regarding to the web governance access
Given the visitor consults the main navigation,
When the visitor compares the accesos published,
Then the site distinguishes explicitly the access a the mobile app of the access a the governance and metrics web application.

Scenario 4: Access no available temporarily
Given the mobile app access point is under maintenance,
When the visitor requests enter a the mobile app,
Then the site informs temporary unavailability of the access mobile and maintains available the content informativo.

*Related epic: EP01*

US07: Safety Supervisor sign-in on the mobile app

As a Safety Supervisor,
I want to sign in to the mobile app,
so that I can remotely access monitoring, operational control, area and device registration, and configuration or updates of the safety system.

**Acceptance Criteria**

Scenario 1: Successful authentication of supervisor in the mobile app
Given the Safety Supervisor has valid credentials registered in the system,
When the supervisor provides their credentials of access in the mobile app,
Then the system grants access with the Safety Supervisor role and enables monitoring, operational control, administration of areas/devices and technical configuration.

Scenario 2: Unrecognized supervisor credentials
Given the Safety Supervisor attempts to access the mobile app,
When the supervisor provides unrecognized credentials by the system,
Then the system denies the access and informs that the credentials are not valid.

Scenario 3: Disabled supervisor account
Given the Safety Supervisor has a disabled account in the system,
When the supervisor provides credentials associated with the disabled account in the mobile app,
Then the system denies the access and informs that the account is disabled.

Scenario 4: Restriction of user governance in the mobile app
Given the Safety Supervisor maintains an active session in the mobile app,
When the supervisor attempts administrar accounts of user or roles of plant,
Then the system denies the operation and informs that the user governance performs in the Plant Manager web application.

*Related epic: EP02*

US08: Plant Manager sign-in on the web application

As a Plant Manager,
I want to sign in to the web application,
so that I can access user and role governance, the metrics dashboard, and the plant's full history.

**Acceptance Criteria**

Scenario 1: Successful authentication of Plant Manager
Given the Plant Manager has valid credentials registered in the system,
When the manager provides their credentials of access in the web application,
Then the system grants access with the role of Plant Manager and enables administration of users, metrics dashboard and full history.

Scenario 2: Unrecognized credentials of Plant Manager
Given the Plant Manager attempts to access the web application,
When the manager provides unrecognized credentials by the system,
Then the system denies the access and informs that the credentials are not valid.

Scenario 3: Restriction of operational control and technical configuration in the web application
Given the Plant Manager maintains an active session in the web application,
When the manager attempts ejecutar override of actuators, register devices IoT or apply updates technical of the system,
Then the system denies the operation and informs that those functions correspond to the Safety Supervisor in the mobile app.

*Related epic: EP02*

US09: Navigate to the governance and metrics web application

As a visitor,
I want to access the governance and metrics web application from the informational site,
so that I can sign in as a Plant Manager.

**Acceptance Criteria**

Scenario 1: Redirection toward the access of the web application
Given the visitor is in the SafePlant website,
When the visitor requests the access a the governance and metrics web application,
Then the system redirects to the visitor to the web application authentication point of SafePlant.

Scenario 2: Access identifiable in the main navigation
Given the visitor consults the SafePlant website,
When the visitor reviews the main navigation of the site,
Then the site presents a access identifiable toward the web application for governance, users, and metrics.

Scenario 3: Differentiation regarding to the access mobile of operation
Given the visitor consults the main navigation,
When the visitor compares the accesos published,
Then the site distinguishes explicitly the web governance access of the mobile access for operation and technical configuration.

Scenario 4: Access web no available temporarily
Given the web application authentication point is under maintenance,
When the visitor requests enter a the web application,
Then the site informs temporary unavailability of the access web and maintains available the content informativo.

*Related epic: EP01*

US10: Sign out of an authenticated user session

As a authenticated system user,
I want to end my active session on the mobile app or the web application,
so that I can protect access to system functions against unauthorized use of my account.

**Acceptance Criteria**

Scenario 1: Sign-out of session successful in the mobile app
Given a Safety Supervisor maintains an active session in the mobile app,
When the supervisor requests end their session,
Then the system closes the active session and restricts the access a the protected functions of the mobile app.

Scenario 2: Sign-out of session successful in the web application
Given a Plant Manager maintains an active session in the web application,
When the manager requests end their session,
Then the system closes the active session and restricts the access a the protected functions of the web application.

Scenario 3: Access attempt subsequent to the sign-out of session
Given a user ha ended their session in the mobile app or in the web application,
When the user attempts access function protegida without authenticating again,
Then the system denies the access and informs that requires authentication.

*Related epic: EP02*

US11: Create user accounts as Plant Manager

As a Plant Manager,
I want to create user accounts for Safety Supervisors and Plant Managers in the web application,
so that I can enable controlled access to mobile operations and web governance.

**Acceptance Criteria**

Scenario 1: Creation of account of Safety Supervisor
Given the Plant Manager accesses the administration of users in the web application,
When the manager registers a new account with name, email and role of Safety Supervisor,
Then the system creates the account and enables the access of the user a the mobile app with the role asignado.

Scenario 2: Creation of account of Plant Manager
Given the Plant Manager accesses the administration of users in the web application,
When the manager registers a new account with name, email and role of Plant Manager,
Then the system creates the account and enables the access of the user a the web application with the role asignado.

Scenario 3: Creation of account with email duplicate
Given the Plant Manager attempts register a new account of user in the web application,
When the email provided is already registered in the system,
Then the system rejects the creation and informs that the email is already in use.

*Related epic: EP02*

US12: Assign user roles and permissions

As a Plant Manager,
I want to assign and modify roles and permissions for system users in the web application,
so that I can control access to mobile operations and web governance.

**Acceptance Criteria**

Scenario 1: Assignment of role a user existente
Given there is a account of user registered in the system
And the Plant Manager accesses the administration of roles in the web application,
When the manager assigns a role valid of Safety Supervisor or Plant Manager a the account of the user,
Then the system updates the role of the user and applies the permissions corresponding to the channel authorized.

Scenario 2: Assignment of role no reconocido
Given the Plant Manager attempts assign a role a user in the web application,
When the role provided no is definido in the system,
Then the system rejects the assignment and informs that the role no es valid.

Scenario 3: Cambio of role of supervisor a manager
Given there is a account with role of Safety Supervisor,
When the manager assigns the role of Plant Manager a that account,
Then the system updates the permissions, restricts the access operational mobile and enables the governance web.

Scenario 4: Attempt of assignment without privileges of manager
Given a user authenticated without role of Plant Manager requests modify roles,
When the system evaluates the authorization of the operation,
Then the system denies the operation and informs that the administration of roles requires the role of Plant Manager.

*Related epic: EP02*

US13: Recover access credentials

As a registered system user,
I want to recover access to my account when I forget my credentials,
so that I can restore access to the mobile app or the web application according to my role.

**Acceptance Criteria**

Scenario 1: Request of recovery with email registered
Given a user registered ha forgotten their credentials of access,
When the user requests the recovery of access with a email registered in the system from the mobile app or the web application,
Then the system generates a process of recovery and sends the instructions to the email associated.

Scenario 2: Request of recovery with email no registered
Given a persona requests the recovery of access,
When the email provided no is registered in the system,
Then the system informs that there is no a account associated with the email provided.

Scenario 3: Reset with process of recovery expired
Given a user attempts restore their credentials,
When the process of recovery ha superado the time of validez configured,
Then the system rejects the reset and informs that the process of recovery ha expired.

*Related epic: EP02*

US14: Consolidated operational dashboard of plant areas

As a Safety Supervisor,
I want to view the consolidated operational status of all registered industrial areas in the mobile app,
so that I can obtain a remote real-time overview of environmental and safety status.

**Acceptance Criteria**

Scenario 1: Overview of industrial areas
Given the Safety Supervisor accesses the mobile app authenticated,
When the system loads the status of the industrial areas registered,
Then the mobile app presents the summary of CO₂ in ppm, noise in dB, presence and alert status of each area.

Scenario 2: Identification of areas in risk condition
Given one or more areas present conditions outside the allowed limits,
When the supervisor consults the operational dashboard in the mobile app,
Then the system identifies the areas that require immediate attention.

Scenario 3: Plant without areas registered
Given the system has no industrial areas registered,
When the supervisor consults the operational dashboard in the mobile app,
Then the system informs that there are are notas configured for monitoring.

*Related epic: EP03*

US15: Real-time CO₂ monitoring by area

As a Safety Supervisor,
I want to monitor in real time the CO₂ concentration in ppm of an industrial area from the mobile app,
so that I can promptly identify dangerous gas buildups in the industrial environment.

**Acceptance Criteria**

Scenario 1: Query of CO₂ concentration actual
Given the supervisor query an industrial area with CO₂ sensor activo from the mobile app,
When the sensor MQ-135 registers a CO₂ concentration in ppm,
Then the system registers and presents the value actual of CO₂ of the area in the mobile app.

Scenario 2: Update of measurement of CO₂
Given the supervisor monitors an industrial area in the mobile app
And the CO₂ sensor generates a new measurement,
When the system receives the new measurement through the IoT Gateway,
Then the system updates the value of CO₂ correspondiente the area monitored in the mobile app.

Scenario 3: CO₂ sensor without transmission of data
Given the supervisor monitors an industrial area in the mobile app,
When the CO₂ sensor stops send measurements within the expected interval,
Then the system identifies the sensor as no available and keeps the last valid measurement registered.

Scenario 4: Measurement of CO₂ outside the range valid of the sensor
Given the system receives a measurement of CO₂ from the embedded device,
When the value of the measurement is outside the range operational of the sensor MQ-135,
Then the system discards the measurement and registers the event as invalid measurement of CO₂.

*Related epic: EP03*

US16: Real-time noise monitoring by area

As a Safety Supervisor,
I want to monitor in real time the noise level in dB of an industrial area from the mobile app,
so that I can promptly identify hazardous noise exposure conditions for operators.

**Acceptance Criteria**

Scenario 1: Query of noise level actual
Given the supervisor query an industrial area with noise sensor activo from the mobile app,
When the sound level meter registers a sound level in dB,
Then the system registers and presents the value actual of noise of the area in the mobile app.

Scenario 2: Update of measurement of noise
Given the supervisor monitors an industrial area in the mobile app
And the noise sensor generates a new measurement,
When the system receives the new measurement through the IoT Gateway,
Then the system updates the value of noise correspondiente the area monitored in the mobile app.

Scenario 3: Noise sensor without transmission of data
Given the supervisor monitors an industrial area in the mobile app,
When the sound level meter stops send measurements within the expected interval,
Then the system identifies the sensor as no available and keeps the last valid measurement registered.

*Related epic: EP03*

US17: Personnel presence monitoring by area

As a Safety Supervisor,
I want to monitor personnel presence in an industrial area from the mobile app,
so that I can determine whether operators are exposed to hazardous environmental conditions.

**Acceptance Criteria**

Scenario 1: Detection of presence by PIR sensor
Given the supervisor monitors an industrial area with PIR sensor activo from the mobile app,
When the PIR sensor detects movimiento in the area,
Then the system registers the personnel presence in the area and the presents in the mobile app.

Scenario 2: Absence of personnel in area monitored
Given the supervisor monitors an industrial area in the mobile app,
When the PIR sensor no detects actividad in the interval configured,
Then the system records the area as without personnel present.

Scenario 3: PIR sensor without transmission of data
Given the supervisor monitors an industrial area in the mobile app,
When the PIR sensor stops send signals within the expected interval,
Then the system identifies the sensor as no available and keeps the last status of presence registered.

*Related epic: EP03*

US18: View active alerts

As a Safety Supervisor,
I want to view active environmental and safety alerts in the plant from the mobile app,
so that I can promptly address risk conditions detected by the system.

**Acceptance Criteria**

Scenario 1: Listing of alerts activas in the plant
Given the system ha detectado one or more risk conditions without resolver,
When the supervisor consults the alerts activas in the mobile app,
Then the system presents the area, the type of alerts, the measurement associated and the detection date of each alerts activates.

Scenario 2: Retiro of alerts by normalization of condition
Given the supervisor views the alerts activas in the mobile app,
When a risk condition ends in an area monitored,
Then the system removes the alerts correspondiente of the listing of alerts activas.

Scenario 3: Absence of alerts activas in the plant
Given there are no risk conditions activas in any area,
When the supervisor consults the alerts activas in the mobile app,
Then the system informs that there are no alerts activas in that moment.

*Related epic: EP03*

US19: View environmental status by industrial areas

As a Safety Supervisor,
I want to view in the mobile app the environmental status of each registered industrial area,
so that I can identify which areas require immediate attention.

**Acceptance Criteria**

Scenario 1: Listing of areas in safe status
Given all the industrial areas registered are within the allowed limits,
When the supervisor consults the listing of areas in the mobile app,
Then the system presents each area with its name, descriptive location, safe environmental status and recent measurements of CO₂, noise and presence.

Scenario 2: Identification of areas in risk condition
Given one or more industrial areas present conditions outside the allowed limits,
When the supervisor consults the listing of areas in the mobile app,
Then the system prioritizes and identifies the areas with active risk condition for operational attention.

Scenario 3: Plant without areas registered
Given the system has no industrial areas registered,
When the supervisor consults the listing of areas,
Then the system informs that there are are notas configured for monitoring.

Scenario 4: Query of the detalle of an area with machines associated
Given there is an area registered with location description and machine references or workstations,
When the supervisor selects the detalle of that area,
Then the system presents the information of the area, their thresholds, devices associated and the environmental status current.

*Related epic: EP03*

US20: Register and manage industrial areas

As a Safety Supervisor,
I want to register and manage industrial plant areas from the mobile app,
so that I can organize monitoring and associate devices and thresholds with each area.

**Acceptance Criteria**

Scenario 1: Registration of an industrial area
Given the Safety Supervisor accesses the administration of areas in the mobile app,
When the supervisor registers a new area with name, location description in the plant and machine references or associated workstations,
Then the system almacenthe area and the enables for the assignment of devices and thresholds.

Scenario 2: Modification of an area existente
Given there is an industrial area registered in the system,
When the supervisor modifies the name, the descriptive location or the referencia of machines of the area,
Then the system updates the information of the area keeping their history of events associated.

Scenario 3: Registration of area with name duplicate
Given the supervisor attempts register an industrial area,
When the name of the area already there is in the system,
Then the system rejects the registration and informs that the area already is registered.

Scenario 4: Registration with data required incomplete
Given the supervisor starts the registration of an area,
When omits the name or the location description,
Then the system rejects the registration and informs the required fields pendientes.

*Related epic: EP03*

US21: Configure environmental thresholds by area

As a Safety Supervisor,
I want to configure the allowed CO₂ limits in ppm and noise limits in dB for each registered industrial area from the mobile app,
so that I can determine when an environmental condition represents a risk in that plant sector.

**Acceptance Criteria**

Scenario 1: Configuration of limits ambientales by area
Given the supervisor has an industrial area registered,
When the supervisor configures the allowed limits of CO₂ in ppm and noise in dB for that area,
Then the system stores the limits associated to the area.

Scenario 2: Modification of limit environmental existente
Given an industrial area has limits ambientales configured,
When the supervisor modifies uno of the limits,
Then the system replaces the value previous by the new limit configured.

Scenario 3: Limit environmental outside the range allowed by the system
Given the supervisor configures a limit environmental,
When the value ingresado no meets the restrictions established by the system,
Then the system rejects the configuration and informs that the value no es valid.

Scenario 4: Area without thresholds configured
Given there is an area registered without thresholds,
When the system evaluates measurements of that area,
Then the system informs that no can classify risk by thresholds absent until that the supervisor the configure.

*Related epic: EP03*

US22: Register IoT devices by area

As a Safety Supervisor,
I want to register sensors and actuators in an industrial area from the mobile app,
so that I can enable environmental monitoring and automatic responses in that plant sector.

**Acceptance Criteria**

Scenario 1: Sensor registration in an industrial area
Given there is an industrial area registered in the system
And the Safety Supervisor accesses the administration of devices in the mobile app,
When the supervisor associates a sensor with its type, identifier and embedded device address to the area,
Then the system registers the sensor and enables it to receive measurements.

Scenario 2: Actuator registration in an industrial area
Given there is an industrial area registered in the system
And the Safety Supervisor accesses the administration of devices in the mobile app,
When the supervisor associates an actuator with its type, identifier and embedded device address to the area,
Then the system registers the actuator and enables it to receive control commands.

Scenario 3: Device registration with duplicate identifier
Given the Safety Supervisor attempts register a device IoT in the mobile app,
When the device identifier already is associated in the system,
Then the system rejects the registration and informs that the device is already in use.

Scenario 4: Registration attempt from the Plant Manager web application
Given a Plant Manager authenticated in the web application attempts register a device IoT,
When requests the creation of the device,
Then the system denies the operation and informs that the technical registration of devices belongs to the supervisor in the mobile app.

*Related epic: EP03*

US23: Plant metrics dashboard and full history

As a Plant Manager,
I want to consult the metrics dashboard and the full history of measurements, alerts, and plant events in the web application,
so that I can govern operations with consolidated information.

**Acceptance Criteria**

Scenario 1: Query of the metrics dashboard
Given the Plant Manager maintains an active session in the web application
And there are measurements and events registered,
When the manager opens the metrics dashboard,
Then the system presents consolidated indicators of CO₂, noise, alerts and overall status by area.

Scenario 2: Query of full history by area and period
Given there are events registered in one or more areas,
When the manager consults the full history for a given period in the web application,
Then the system provides measurements, alerts and actions corresponding to the queried period.

Scenario 3: History with no records in the queried period
Given there are no events in the queried period,
When the manager consults the history in the web application,
Then the system informs that there are no events registered for the indicated period.

Scenario 4: Restriction of override from the dashboard web
Given the manager views a alerts activates in the dashboard,
When attempts anular an actuator from the web application,
Then the system denies the operation and informs that the operational control performs in the mobile app.

*Related epic: EP03*

US24: Correlate personnel presence with CO₂ levels

As a Safety Supervisor,
I want the system to simultaneously evaluate personnel presence and CO₂ levels in an industrial area and present the resulting alert in the mobile app,
so that I can determine whether operators are exposed to dangerous gas concentrations.

**Acceptance Criteria**

Scenario 1: Personnel exposure a excessive CO₂
Given the system detects personnel present in an industrial area
And the CO₂ concentration in the area exceeds the allowed limit,
When the system evaluates the conditions of the area,
Then the system identifies a condition of exposure a CO₂, generates a alerts of safety for the area and the presents in the supervisor mobile app.

Scenario 2: Excessive CO₂ without personnel present
Given the system detects absence of personnel in an industrial area
And the CO₂ concentration in the area exceeds the allowed limit,
When the system evaluates the conditions of the area,
Then the system identifies a condition of excessive CO₂ without personnel exposure and activates the air extractor without activate the preventive siren.

Scenario 3: Personnel present with CO₂ inside of the limit
Given the system detects personnel present in an industrial area
And the CO₂ concentration is inside of the allowed limit,
When the system evaluates the conditions of the area,
Then the system maintains the area in exposure status segura for the personnel present.

*Related epic: EP04*

US25: Classify exposure severity by area

As a Safety Supervisor,
I want to view in the mobile app the exposure severity of each industrial area based on presence and environmental exceedance,
so that I can prioritize remote operational attention.

**Acceptance Criteria**

Scenario 1: Severity registration by presence with CO₂ exceeded
Given an area presents presenceDetected equal to true and co2Ppm above the threshold,
When the supervisor consults the exposure status in the mobile app,
Then the system presents severity equal to high, areaId, alertType equal to co2_exposure and the measurement associated.

Scenario 2: Severity media by noise exceeded without presence
Given an area presents noiseDb above the threshold and presenceDetected equal to false,
When the supervisor consults the exposure status,
Then the system presents severity equal to medium and alertType equal to noise_excess_no_presence.

Scenario 3: Severity nula in safe conditions
Given CO₂ and noise are inside of threshold with or without presence,
When the supervisor consultthe area,
Then the system presents severity equal to none and safe environmental status.

Scenario 4: Area without thresholds configured
Given the area no has thresholds current,
When the supervisor consults the severity,
Then the system informs that the severity no can calcularse by thresholds absent.

*Related epic: EP04*

US26: Short history of personnel exposures by area

As a Safety Supervisor,
I want to consult in the mobile app the short history of recent exposures by area,
so that I can address active incidents and verify the immediate effectiveness of automatic responses.

**Acceptance Criteria**

Scenario 1: Query of short history with exposiciones recent
Given there are events of exposure recent for an area,
When the supervisor consults the short history in the mobile app,
Then the system presents areaId, alertType, severity, measuredValue, detectedAt and resolvedAt when applies, prioritizing the events more recent.

Scenario 2: Filtrado by type of exposure
Given there are exposiciones of CO₂ and of noise in the area,
When the supervisor filters by alertType equal to co2_exposure,
Then the system returns only the exposiciones of CO₂ of the short history.

Scenario 3: Short history empty
Given there are no exposiciones recent in the area,
When the supervisor executes the query,
Then the system informs that there are no exposiciones recent registered.

Scenario 4: Exposure resolved after normalization
Given a exposure activates ends when the measurements return to the threshold,
When the supervisor consults the short history,
Then the system shows the exposure with status equal to resolved and resolvedAt.

*Related epic: EP04*

US27: Detect CO₂ excess

As a Safety Supervisor,
I want the system to detect when the CO₂ concentration exceeds the allowed limit in an industrial area,
so that automatic purification and prevention measures can be activated promptly.

**Acceptance Criteria**

Scenario 1: CO₂ inside of the allowed limit
Given the system monitors an industrial area with a limit of CO₂ configured,
When the sensor MQ-135 registers a concentration equal to or below the allowed limit,
Then the system maintains the area in allowed environmental status.

Scenario 2: CO₂ above the allowed limit
Given the system monitors an industrial area with a limit of CO₂ configured,
When the sensor MQ-135 registers a concentration above the allowed limit,
Then the system identifies a condition of excessive CO₂ and generates a environmental alert visible in the supervisor mobile app.

Scenario 3: Measurement of CO₂ invalid descartada
Given the system receives a measurement of CO₂ from the embedded device,
When the measurement is outside the range valid of the sensor MQ-135,
Then the system discards the measurement and registers the event as invalid measurement of CO₂.

*Related epic: EP05*

US28: Detect excessive noise

As a Safety Supervisor,
I want the system to detect when the sound level exceeds the allowed limit in an industrial area,
so that operator exposure to hazardous noise levels can be prevented.

**Acceptance Criteria**

Scenario 1: Noise inside of the allowed limit
Given the system monitors an industrial area with a limit sonoro configured,
When the sound level meter registers a nivel equal to or below the allowed limit,
Then the system maintains the area in allowed sound status.

Scenario 2: Excessive noise without personnel present
Given the system detects a sound level above the allowed limit
And the system registers absence of personnel in the area,
When the system evaluates the condition environmental,
Then the system registers the noise exposure without activate the preventive siren dirigida a operators.

Scenario 3: Excessive noise with personnel present
Given the system detects a sound level above the allowed limit
And the system detects personnel present in the area,
When the system evaluates the condition environmental,
Then the system generates a exposure alert sonora visible in the supervisor mobile app and activates the preventive siren.

*Related epic: EP05*

US29: Automatic air extractor activation for CO₂

As a Safety Supervisor,
I want the system to automatically activate the air extractor through the control relay when CO₂ excess is detected,
so that gas concentration can be reduced and safe environmental conditions restored.

**Acceptance Criteria**

Scenario 1: Activation of the extractor by CO₂ excess
Given an industrial area presents a CO₂ concentration above the allowed limit,
When the system confirms the condition of CO₂ excess,
Then the system activates the air extractor associated with the area through the control relay.

Scenario 2: Deactivation of the extractor to the normalize CO₂
Given the air extractor is activo by a condition of excessive CO₂,
When the CO₂ concentration returns to the range allowed,
Then the system deactivates the air extractor of the area.

Scenario 3: Failure in the activation of the extractor
Given the system determines that must activate the air extractor,
When the control relay no confirms the activation of the extractor,
Then the system registers the failure and generates a alerts of unavailable actuator visible in the supervisor mobile app.

Scenario 4: Communication loss with the embedded device during activation
Given the system sends the order of activation to the air extractor,
When the embedded device ESP32 no responds inside of the expected time,
Then the system registers the communication failure and maintains the alerts of excessive CO₂ activates in the supervisor mobile app.

*Related epic: EP05*

US30: Preventive siren activation for hazardous exposure

As a Safety Supervisor,
I want the system to activate the preventive siren when an operator is exposed to a hazardous CO₂ or excessive noise condition,
so that the existing risk can be warned immediately and area evacuation enabled.

**Acceptance Criteria**

Scenario 1: Siren activada by CO₂ hazardous with personnel present
Given the system detects a concentration hazardous of CO₂ in an industrial area
And the system detects personnel present in the area,
When the system determines that there is exposure of operators,
Then the system activates the preventive siren of the area.

Scenario 2: Siren activada by noise hazardous with personnel present
Given the system detects a noise level above the allowed limit
And the system detects personnel present in the area,
When the system determines that there is exposure of operators,
Then the system activates the preventive siren of the area.

Scenario 3: Siren inactiva in safe conditions with personnel present
Given the system detects personnel present in an industrial area,
When the concentraciones of CO₂ and the niveles of noise are within the allowed limits,
Then the system maintains the preventive siren desactivada.

Scenario 4: Deactivation of siren to the cesar risk condition
Given the preventive siren is activates by a condition of exposure,
When the hazardous condition disappears and there is no other condition of alarm activates in the area,
Then the system deactivates the preventive siren of the area.

*Related epic: EP05*

US31: Deploy acoustic barriers for noise exposure

As a Safety Supervisor,
I want the system to deploy mobile acoustic isolation barriers via servomotors when excessive noise with personnel present is detected,
so that operator noise exposure in the affected area can be reduced.

**Acceptance Criteria**

Scenario 1: Deployment of barriers by excessive noise with personnel
Given an industrial area presents a noise level above the allowed limit
And the system detects personnel present in the area,
When the system confirms the condition of noise exposure,
Then the system activates the servomotors and deploys the acoustic barriers of the area.

Scenario 2: Retraction of barriers to the normalize the noise
Given the acoustic barriers are desplegadas by a condition of excessive noise,
When the sound level returns to the range allowed,
Then the system retracts the acoustic barriers of the area.

Scenario 3: Failure in the deployment of acoustic barriers
Given the system determines that must desplegar the acoustic barriers,
When the servomotor no confirms the deployment inside of the expected time,
Then the system registers the failure and generates a alerts of unavailable actuator visible in the supervisor mobile app.

*Related epic: EP05*

US32: Remote manual actuator override in emergency

As a Safety Supervisor,
I want to manually override an actuator state remotely from the mobile app during an emergency,
so that I can take direct control of extractors, sirens, or barriers when the automatic response is not adequate for the situation.

**Acceptance Criteria**

Scenario 1: Remote manual override of extractor in emergency
Given the air extractor of an area is activo automatically
And the Safety Supervisor maintains an active session in the mobile app,
When the supervisor requests the manual override and activation forzada of the extractor from the mobile app,
Then the system applies the status solicitado to the extractor and registers the manual override with the identifier of the supervisor and the event date.

Scenario 2: Remote manual override of siren in emergency
Given the preventive siren of an area is activates automatically
And the Safety Supervisor maintains an active session in the mobile app,
When the supervisor requests the deactivation manual of the siren from the mobile app,
Then the system deactivates the siren and registers the manual override with the identifier of the supervisor and the event date.

Scenario 3: Manual override denegada without role of supervisor in the mobile app
Given a user authenticated in the web application or without role of Safety Supervisor attempts anular an actuator,
When the user requests the manual override of an actuator,
Then the system rejects the operation and informs that the remote manual override requires the role of Safety Supervisor in the mobile app.

*Related epic: EP05*

US33: Short log of executed automatic actions

As a Safety Supervisor,
I want to consult the short log of recent automatic actions from the mobile app,
so that I can verify that prevention mechanisms responded to the hazardous conditions detected.

**Acceptance Criteria**

Scenario 1: Registration of activation automatic of actuator
Given the system activates a extractor, a siren or a barrier acoustic,
When the automatic action executes in the area,
Then the system registers the actuator, the action realizada, the area and the moment of execution.

Scenario 2: Registration of deactivation automatic of actuator
Given an actuator is activo by a condition environmental,
When the system determines that the condition that originated the action ha ended,
Then the system registers the deactivation of the actuator with the area and the moment of the event.

Scenario 3: Query of the registration corto from the mobile app
Given there are automatic actions recent in an area,
When the supervisor consults the registration corto from the mobile app,
Then the system presents the actions recent with actuator, area, result and moment of execution.

Scenario 4: Registration of automatic action fallida
Given the system sends a order automatic an actuator,
When the actuator no confirms the execution,
Then the system registers the action as fallida with the actuator, the area and the reason of the failure.

*Related epic: EP05*

US34: Physical alarm notification to the exposed operator

As a plant operator,
I want to receive an audible physical alarm when exposed to a hazardous CO₂ or excessive noise condition,
so that I can recognize the risk situation and leave the affected area.

**Acceptance Criteria**

Scenario 1: Alarm audible by exposure a CO₂ hazardous
Given the operator is in an industrial area with hazardous condition of CO₂,
When the system activates the preventive siren of the area,
Then the operator receives the signal audible of alarm in the environment physical of the area.

Scenario 2: Alarm audible by exposure a excessive noise
Given the operator is in an industrial area with noise level above the allowed limit,
When the system activates the preventive siren of the area,
Then the operator receives the signal audible of alarm in the environment physical of the area.

Scenario 3: Absence of alarm in safe conditions
Given the operator is in an industrial area,
When the conditions of CO₂ and noise are within the allowed limits,
Then the system maintains the preventive siren desactivada in the area.

Scenario 4: Failure of siren with operator expuesto
Given the operator is in an area with risk condition activates,
When the buzzer of the siren no responds a the order of activation,
Then the system registers the failure of the actuator and maintains the exposure alert activates in the Safety Supervisor mobile app.

*Related epic: EP05*

US35: Update system configuration parameters

As a Safety Supervisor,
I want to apply updates to system configuration parameters from the mobile app,
so that areas, thresholds, devices, and rules remain aligned with plant safety operations.

**Acceptance Criteria**

Scenario 1: Update successful of parameters of configuration
Given the Safety Supervisor maintains an active session in the mobile app
And there are parameters of configuration valid for areas, thresholds or devices,
When the supervisor confirms the update of the parameters of the system,
Then the system stores the new configuration and the deja available for the monitoring and operational control.

Scenario 2: Update with parameters incomplete or invalid
Given the Safety Supervisor attempts actualizar the configuration of the system in the mobile app,
When one or more parameters required are incomplete or no meet the restrictions of the system,
Then the system rejects the update and informs the parameters that must corregirse.

Scenario 3: Query of version or status of configuration aplicada
Given the supervisor accesses the section of updates in the mobile app,
When the supervisor consults the status of the configuration of the system,
Then the system presents the configuration current and the date of the last update aplicada.

Scenario 4: Attempt of update technical by Plant Manager
Given a Plant Manager authenticated in the web application attempts apply a update technical of parameters of the system,
When requests the update,
Then the system denies the operation and informs that the technical configuration belongs to the supervisor in the mobile app.

*Related epic: EP05*

US36: Mobile app and web application compatibility

As a Safety Supervisor,
I want to use the mobile app on current Android and iOS devices to operate and technically configure the safety system, and as a Plant Manager I want to use the web application in modern browsers to govern users and consult metrics and history,
so that each role can use the authorized channel on supported environments.

**Acceptance Criteria**

Scenario 1: Operation from mobile app in compatible device
Given a Safety Supervisor accesses the mobile app in a device Android or iOS supported,
When the supervisor consults the operational dashboard and the detalle of an industrial area,
Then the system presents values of CO₂ in ppm, noise in dB, presence and alerts activas in a readable way and operable in the device used.

Scenario 2: Governance from web application in browser compatible
Given a Plant Manager accesses the web application from a supported modern web browser,
When the manager consults the administration of users or the metrics dashboard,
Then the system presents the functions of governance in a readable way and operable in the browser used.

Scenario 3: Access from browser or device no supported
Given a user attempts to access the web application or a the mobile app from a environment no included in the supported compatibility matrix,
When the user requests access a protected functions,
Then the system informs that the environment used no is supported
And the system indicates the environments compatible corresponding to each channel.

Scenario 4: Technical configuration of devices in compatible mobile device
Given a Safety Supervisor accesses the mobile app from a device supported,
When the supervisor registers a sensor or actuator in an area,
Then the system allows complete the registration in an operable way in the device used.

Scenario 5: Separation functional between channels compatible
Given a Safety Supervisor operates, configures devices and updates parameters from the mobile app and a Plant Manager administra users and query metrics from the web application,
When both users perform their functions autorizadas during the same workday,
Then the system maintains consistent the telemetry and the alerts in the mobile app
And reflects in the dashboard web the information consolidated without mixing the responsibilities of each channel.

*Related epic: EP06*

TS01: API endpoint for telemetry ingestion

As a Developer,
I want to expose a REST telemetry ingestion endpoint in JSON format,
so that CO₂, noise, and presence measurements sent by the IoT Gateway can be persisted to the cloud.

**Acceptance Criteria**

Scenario 1: Ingestion successful of telemetry valid
Given the IoT Gateway maintains a token of device current
And sends POST /api/v1/telemetry with Content-Type application/json and includes deviceId, areaId, co2Ppm, noiseDb, presenceDetected and measuredAt,
When the API processes the payload of telemetry,
Then the API responds 201 Created with a body JSON that contains telemetryId, areaId and status equal to accepted
And persists the registration in the relational database.

Scenario 2: Ingestion with fields opcionales omitidos
Given the IoT Gateway sends POST /api/v1/telemetry with the required fields deviceId, areaId, co2Ppm, noiseDb and measuredAt
And omits the field presenceDetected,
When the API validates the schema JSON of telemetry,
Then the API responds 201 Created with telemetryId and status equal to accepted
And stores presenceDetected with value nulo or false according to the policy of schema definida.

Scenario 3: Rejection due to payload JSON malformado
Given a emisor sends POST /api/v1/telemetry with a body that no es JSON valid,
When the API attempts deserializar the request,
Then the API responds 400 Bad Request with a body JSON that contains code equal to invalid_json and message descriptivo
And no inserts records of telemetry.

Scenario 4: Rejection due to measurement outside of range operational
Given the IoT Gateway sends POST /api/v1/telemetry with co2Ppm outside the range operational of the sensor MQ-135 or noiseDb outside the range of the sound level meter,
When the API executes the rules of validation of dominio,
Then the API responds 422 Unprocessable Entity with code equal to out_of_range, field and allowedRange
And no persists the invalid measurement.

Scenario 5: Indisponibilidad of the service of persistence
Given the IoT Gateway sends POST /api/v1/telemetry with a payload valid
And the service of relational database no accepts connections,
When the API attempts persist the telemetry,
Then the API responds 503 Service Unavailable with code equal to service_unavailable and retryAfter
And no confirms the acceptance of the telemetry.

Scenario 6: Timeout of network toward the API in the cloud
Given the IoT Gateway starts POST /api/v1/telemetry toward the API
And the connection of network exceeds the maximum wait time configured,
When the client HTTP of the Gateway detects the timeout,
Then the Gateway registers the network failure with status equal to timeout
And queues the telemetry for retry local without assume persistence in the cloud.

*Related epic: EP07*

TS02: Secure authentication and TLS channel for devices and sessions

As a Developer,
I want to authenticate ESP32 devices and the IoT Gateway via JWT or API Key and require TLS for API communication, in addition to valid user tokens,
so that access is restricted and confidentiality and integrity are preserved.

**Acceptance Criteria**

Scenario 1: Authentication successful with API Key current
Given the IoT Gateway includes the X-API-Key header with a registered key and current
And requests POST /api/v1/telemetry,
When the API validates the key of device,
Then the API responds 201 Created and associates the telemetry to the deviceId authorized in the payload JSON of response.

Scenario 2: Authentication successful with JWT of device
Given the IoT Gateway includes Authorization Bearer with a JWT signed, no expired and with role claim equal to gateway,
When the API validates the signature and the expiration of the token,
Then the API accepts the request protegida and responds with the code HTTP corresponding to the recurso solicitado, by ejemplo 201 Created or 200 OK.

Scenario 3: Rejection due to absence of credentials
Given a emisor requests POST /api/v1/telemetry without headers X-API-Key nor Authorization,
When the API evaluates the authentication middleware,
Then the API responds 401 Unauthorized with code equal to missing_credentials and message descriptivo
And no processes the body of the request.

Scenario 4: Rejection due to token JWT expired
Given the IoT Gateway sends Authorization Bearer with a JWT cuya marks exp already expired,
When the API validates the validity of the token,
Then the API responds 401 Unauthorized with code equal to token_expired
And no persists telemetry.

Scenario 5: Rejection due to API Key revocada
Given a emisor presents X-API-Key corresponding to a revoked key in the device repository,
When the API consults the status of the key,
Then the API responds 403 Forbidden with code equal to credential_revoked
And registers the attempt in the audit log.

Scenario 6: Link loss of the ESP32 to the Gateway during authentication local
Given the ESP32 starts a request authenticated toward the Gateway local
And the network link local interrupts before of receive response,
When the firmware detects the fails of communication,
Then the ESP32 retries the submission according to the reconnection policy local
And the Gateway no registers telemetry partial associated a that request incompleta.

Scenario 7: Transmission of telemetry by channel TLS
Given the IoT Gateway has credentials current and telemetry lista for submission,
When the Gateway executes POST /api/v1/telemetry about HTTPS,
Then the API accepts the request only if the channel es TLS and responds 201 Created with telemetryId
And rejects attempts equivalentes about channel no encrypted with 400 Bad Request or sign-out of connection segura according to the edge policy.

Scenario 8: Expiration of session of user with token vencido
Given a accessToken of supervisor or manager ha expired,
When the client requests a recurso protegido as GET /api/v1/areas/Z1/telemetry/latest,
Then the API responds 401 Unauthorized with code equal to token_expired and no returns telemetry.

*Related epic: EP07*

TS03: Local contingency persistence in Gateway SQLite

As a Developer,
I want to persist measurements and events in the IoT Gateway SQLite when internet connectivity loss is detected,
so that operational traceability is retained during offline contingency.

**Acceptance Criteria**

Scenario 1: Almacenamiento local of telemetry during internet outage
Given the IoT Gateway receives telemetry valid from a ESP32
And the probe of conectividad toward the API in the cloud fails,
When the contingency service processes the measurement,
Then the Gateway inserts a registration in SQLite with areaId, deviceId, co2Ppm, noiseDb, presenceDetected, measuredAt and syncStatus equal to pending.

Scenario 2: Almacenamiento local of alerts generada offline
Given the rules engine of the Gateway generates a environmental alert during offline contingency,
When the contingency service persists the event,
Then SQLite stores alertId, areaId, alertType, measuredValue, createdAt and syncStatus equal to pending.

Scenario 3: Rejection of insertion by schema local incomplete
Given the thread of contingency attempts insertar a measurement without areaId or without measuredAt,
When SQLite applies the NOT NULL constraints of the schema,
Then the insertion fails and the Gateway registers a local error event with code equal to sqlite_constraint
And no marks the registration as listo for synchronization.

Scenario 4: Saturation of capacity of retention local
Given the volume of records pending exceeds the threshold of retention configured in the Gateway,
When the contingency service applies the retention policy,
Then the Gateway keeps as a priority alerts and actions recent
And escribe a local event of storage_pressure with usedBytes and maxBytes.

Scenario 5: Write failure in the SQLite file
Given the filesystem of the Gateway reports I/or error to the escribir in the base SQLite,
When the contingency service attempts persist telemetry,
Then the Gateway registers code equal to sqlite_io_error
And maintains the measurement in a in-memory queue of corto plazo for retry of write.

Scenario 6: Continuidad of reception ESP32 without cloud
Given the connection a internet remains interrumpida
And a ESP32 sends a new measurement authenticated to the Gateway,
When the Gateway accepts the request local,
Then the Gateway responds 202 Accepted in the endpoint local with status equal to queued_local
And persists the registration with syncStatus equal to pending.

*Related epic: EP07*

TS04: Asynchronous synchronization of local data to the cloud

As a Developer,
I want to automatically synchronize SQLite-queued records to the cloud database when internet is restored,
so that operational history consistency is restored.

**Acceptance Criteria**

Scenario 1: Synchronization ordenada of measurements pendientes
Given there are records in SQLite with syncStatus equal to pending
And the conectividad toward the API restores,
When the synchronization worker sends the records in order chronological via POST /api/v1/telemetry,
Then the API responds 201 Created by each registration aceptado
And the Gateway updates syncStatus a synced with cloudTelemetryId.

Scenario 2: Synchronization of alerts and actions pendientes
Given there are alerts and automatic actions with syncStatus equal to pending,
When the worker publishes POST /api/v1/alerts/sync and POST /api/v1/actuator-events/sync,
Then the API responds 200 OK with acceptedCount
And the Gateway marks the records locales as synced.

Scenario 3: Retry before 503 Service Unavailable
Given the worker sends a batch of synchronization
And the API responds 503 Service Unavailable with retryAfter,
When the worker applies exponential backoff,
Then the records remain with syncStatus equal to pending
And the Gateway schedules a new attempt respecting retryAfter.

Scenario 4: Registration corrupt no sincronizable
Given a registration local presents JSON incomplete or fields inconsistentes,
When the worker attempts synchronize that registration,
Then the API responds 400 Bad Request or 422 Unprocessable Entity
And the Gateway marks syncStatus equal to failed with lastError without eliminar the registration original.

Scenario 5: Interruption of network a mitad of batch
Given the worker synchronizes a batch of N records
And the network interrupts after confirmar k records,
When the process of synchronization ends partially,
Then the k records confirmed remain synced
And the restantes remain pending for the next execution.

Scenario 6: Conflicto of idempotencia in resend
Given the Gateway resends a registration already aceptado previously with the same idempotencyKey,
When the API detects the key of idempotencia,
Then the API responds 200 OK with telemetryId existente and duplicate equal to true
And the Gateway marks the registration local as synced.

*Related epic: EP07*

TS05: OTA remote update distribution service

As a Developer,
I want to distribute authenticated OTA firmware updates to ESP32 devices from the cloud,
so that security patches and sensor corrections can be applied without physical intervention.

**Acceptance Criteria**

Scenario 1: Publication successful of package OTA
Given a process authorized sends POST /api/v1/ota/firmware with firmwareVersion, checksumSha256, targetDeviceModel and packageUrl signed,
When the API validates the package and registers the version,
Then the API responds 201 Created with otaReleaseId, firmwareVersion and status equal to published.

Scenario 2: Assignment of update a devices objective
Given there is a otaReleaseId published
And sends POST /api/v1/ota/deployments with deviceIds and otaReleaseId,
When the API creates the deployment OTA,
Then the API responds 202 Accepted with deploymentId and devicesQueued.

Scenario 3: Downloads authenticated of the firmware by the Gateway
Given the Gateway requests GET /api/v1/ota/firmware/{otaReleaseId}/package with credentials current,
When the API authorizes the downloads,
Then the API responds 200 OK with the binario or URL firmada
And the Gateway verifies checksumSha256 before of resend to the ESP32.

Scenario 4: Rejection of package with checksum invalid
Given the Gateway calculates a checksum distinto to the checksumSha256 published,
When the service OTA local aborts the installation,
Then the Gateway reports POST /api/v1/ota/deployments/{deploymentId}/status with status equal to failed and code equal to checksum_mismatch
And the API responds 200 OK registering the failure.

Scenario 5: Device ESP32 no alcanzable during OTA
Given the Gateway attempts transferir the firmware to the ESP32
And the local link no responds inside of the timeout,
When the process OTA local ends by timeout of hardware,
Then the Gateway publishes status equal to device_unreachable
And keeps the version of firmware previa in the device.

Scenario 6: Rejection of publication OTA no authorized
Given a emisor without role of deployment requests POST /api/v1/ota/firmware,
When the API evaluates authorization,
Then the API responds 403 Forbidden with code equal to insufficient_scope
And no registers the package.

*Related epic: EP07*

TS06: ESP32 telemetry reception at the IoT Gateway

As a Developer,
I want to expose a local endpoint on the IoT Gateway to receive authenticated telemetry from ESP32 devices and normalize it before sending it to the cloud or SQLite,
so that device measurements are accepted and prepared for cloud or local contingency paths.

**Acceptance Criteria**

Scenario 1: Reception local successful from ESP32
Given a ESP32 registered sends POST /local/v1/telemetry with token of device and measurements valid,
When the Gateway validates authentication and schema,
Then the Gateway responds 202 Accepted with localEventId and forwardStatus equal to queued_cloud or queued_local.

Scenario 2: Normalization of unidades and marcas temporales
Given the ESP32 sends measuredAt in epoch seconds and values numeric in format string,
When the Gateway normaliza the payload,
Then the Gateway produces a JSON canonical with measuredAt in ISO-8601 and types numeric
And responds 202 Accepted.

Scenario 3: Rejection due to token of ESP32 invalid
Given a emisor local presents a token no registered,
When the Gateway validates the device,
Then the Gateway responds 401 Unauthorized with code equal to invalid_device_token.

Scenario 4: Rejection due to payload incomplete
Given the ESP32 omits areaId in the request local,
When the Gateway validates the schema,
Then the Gateway responds 400 Bad Request with code equal to missing_field and field equal to areaId.

Scenario 5: Saturation of the buffer of entry local
Given the internal queue of the Gateway reaches their capacity maximum,
When arrives a new telemetry valid of the ESP32,
Then the Gateway responds 429 Too Many Requests with retryAfter
And no discards silently the message without response.

Scenario 6: Link loss ESP32-Gateway after acceptance partial
Given the Gateway accepts the telemetry and responds 202 Accepted
And the ESP32 no receives the response by corte of network,
When the ESP32 retries with the same idempotencyKey,
Then the Gateway detects the key and responds 202 Accepted with duplicate equal to true without duplicar the processing of negocio.

*Related epic: EP07*

TS07: Exposure evaluation engine by presence and thresholds

As a Developer,
I want to evaluate on the Gateway the combination of PIR presence with CO₂ and noise thresholds,
so that exposure alerts can be generated and actuator activation decided.

**Acceptance Criteria**

Scenario 1: Generation of alerts by CO₂ with presence
Given co2Ppm exceeds the threshold of the area
And presenceDetected es true,
When the rules engine evaluates the condition,
Then the Gateway generates a alerts with alertType equal to co2_exposure and severity registration
And queues command of siren and extractor.

Scenario 2: Activation of extractor without siren by CO₂ without presence
Given co2Ppm exceeds the threshold
And presenceDetected es false,
When the rules engine evaluates the condition,
Then the Gateway generates alerts co2_excess_no_presence
And queues only the command of extractor.

Scenario 3: Generation of alerts sonora with presence
Given noiseDb exceeds the threshold
And presenceDetected es true,
When the rules engine evaluates the condition,
Then the Gateway generates alerts noise_exposure
And queues commands of siren and barriers.

Scenario 4: Descartes by invalid measurement
Given arrives a measurement with co2Ppm outside of range,
When the rules engine receives the event,
Then the Gateway no generates commands of actuators
And registers eventType equal to invalid_measurement.

Scenario 5: Failure to the publish alerts toward the cloud
Given the engine generates a alerts valid
And POST /api/v1/alerts responds 503 Service Unavailable,
When the Gateway handles the error of publication,
Then the alerts remains in SQLite with syncStatus equal to pending
And the decision local of actuators continues.

Scenario 6: Threshold no configured for the area
Given there is telemetry valid for an areaId without thresholds loaded,
When the engine attempts evaluate rules,
Then the Gateway registers code equal to missing_thresholds
And no activates actuators by threshold indefinido.

*Related epic: EP04*

TS08: Actuator command emission to ESP32

As a Developer,
I want to send control commands from the IoT Gateway to the ESP32,
so that the extractor, buzzer, and barrier servomotors can be operated reliably.

**Acceptance Criteria**

Scenario 1: Command successful of activation of extractor
Given the Gateway sends POST /device/v1/actuators/command with actuatorType equal to extractor, action equal to on and commandId,
When the ESP32 confirms the execution of the relay,
Then the ESP32 responds 200 OK with commandId, actuatorType, state equal to on and appliedAt.

Scenario 2: Command successful of deployment of barriers
Given the Gateway sends a command with actuatorType equal to acoustic_barrier and action equal to deploy,
When the ESP32 confirms the movimiento of servomotors,
Then the ESP32 responds 200 OK with state equal to deployed.

Scenario 3: Rejection due to command with schema invalid
Given the Gateway sends a command without action or with actuatorType desconocido,
When the ESP32 validates the payload,
Then the ESP32 responds 400 Bad Request with code equal to invalid_command.

Scenario 4: Rejection due to token of command unauthorized
Given a emisor local presents a token invalid to the endpoint of commands of the ESP32,
When the ESP32 validates authentication,
Then the ESP32 responds 401 Unauthorized with code equal to invalid_device_token.

Scenario 5: Timeout of confirmation of the actuator
Given the Gateway sends a command valid
And the ESP32 no responds inside of the timeout,
When the Gateway detects expiration of wait,
Then the Gateway registers commandStatus equal to timeout
And publishes a event of actuator failure toward the cloud or SQLite.

Scenario 6: Link loss during execution of the command
Given the ESP32 receives the command and corta the link before of responder,
When the Gateway no obtains confirmation,
Then the Gateway marks the command as unconfirmed
And schedules a command of read of status of the actuator.

*Related epic: EP05*

TS09: API endpoint for telemetry query by area

As a Developer,
I want to expose a REST endpoint for recent telemetry queries by area,
so that the mobile app operational monitoring can be fed.

**Acceptance Criteria**

Scenario 1: Query successful of telemetry recent
Given there are measurements persisted for areaId Z1
And a client presents a valid supervisor JWT,
When the client requests GET /api/v1/areas/Z1/telemetry/latest,
Then the API responds 200 OK with areaId, co2Ppm, noiseDb, presenceDetected, measuredAt and quality.

Scenario 2: Query of history by range temporal
Given there are measurements in the range solicitado,
When the client requests GET /api/v1/areas/Z1/telemetry?from=...&to=...,
Then the API responds 200 OK with items[], nextCursor opcional and count.

Scenario 3: Area inexistente
Given the client requests telemetry of an areaId no registered,
When the API looks up the area,
Then the API responds 404 Not Found with code equal to area_not_found.

Scenario 4: Token of supervisor absent or invalid
Given the client omits Authorization or sends a JWT invalid,
When the API evaluates authentication,
Then the API responds 401 Unauthorized with code equal to unauthorized.

Scenario 5: Error interno of read in database
Given the query es valid
And the database produces a error inesperado,
When the API handles the exception,
Then the API responds 500 Internal Server error with code equal to internal_error and correlationId.

Scenario 6: Timeout of the client before latency elevada
Given the client mobile starts the query
And the latency exceeds the timeout of the client,
When the client aborts the request,
Then the client registers timeout without assume data updated
And can reintentar GET /api/v1/areas/Z1/telemetry/latest.

*Related epic: EP03*

TS10: API endpoint for remote actuator override

As a Developer,
I want to expose a REST endpoint for remote manual actuator override by an authenticated supervisor,
so that emergency operational control from the mobile app is enabled.

**Acceptance Criteria**

Scenario 1: Override remote successful of extractor
Given a valid supervisor JWT requests POST /api/v1/areas/Z1/actuators/override with actuatorType equal to extractor and action equal to on,
When the API authorizes and publishes the command toward the Gateway,
Then the API responds 202 Accepted with overrideId, status equal to queued and requestedBy.

Scenario 2: Confirmation of application of the override
Given the Gateway confirms the execution of the override,
When the API updates the status of the command,
Then GET /api/v1/overrides/{overrideId} responds 200 OK with status equal to applied and appliedAt.

Scenario 3: Rejection due to role unauthorized
Given a JWT of Plant Manager requests override of actuator,
When the API evaluates authorization of operational control,
Then the API responds 403 Forbidden with code equal to role_not_allowed.

Scenario 4: Rejection due to payload invalid
Given the client sends action with value no supported,
When the API validates the schema,
Then the API responds 400 Bad Request with code equal to invalid_action.

Scenario 5: Gateway no available for receive the command
Given the API attempts entregar the override to the Gateway
And the channel of command no responds,
When the API registers the delivery failure,
Then the API responds 503 Service Unavailable with code equal to gateway_unreachable and overrideId in status failed_to_queue.

Scenario 6: Timeout of confirmation of the device
Given the override fue queued
And the ESP32 no confirms inside of the SLA,
When the command service expires the wait,
Then GET /api/v1/overrides/{overrideId} responds 200 OK with status equal to timeout.

*Related epic: EP05*

TS11: Telemetry JSON schema validation

As a Developer,
I want to validate the telemetry JSON schema on the Gateway and API,
so that corrupt or incomplete payloads are rejected before persistence.

**Acceptance Criteria**

Scenario 1: Acceptance of payload conforme to the schema
Given the payload meets the JSON Schema of telemetry v1,
When the validador of schema processes the documento,
Then the service continues the flujo and responds 201 Created or 202 Accepted according to the channel.

Scenario 2: Rejection due to type of datum incorrecto
Given co2Ppm arrives as cadena no numeric,
When the validador evaluates types,
Then the service responds 400 Bad Request with code equal to schema_violation and path equal to $.co2Ppm.

Scenario 3: Rejection due to propiedad desconocida critical
Given the payload includes fields additional prohibidos by additionalProperties false,
When the validador evaluates propiedades,
Then the service responds 400 Bad Request with code equal to unexpected_property.

Scenario 4: Rejection due to marks temporal invalid
Given measuredAt no meets format ISO-8601,
When the validador evaluates formatos,
Then the service responds 400 Bad Request with code equal to invalid_datetime.

Scenario 5: Version of schema no supported
Given the emisor indicates schemaVersion equal to 99,
When the service resuelve the schema,
Then the service responds 415 Unsupported Media Type or 400 Bad Request with code equal to unsupported_schema_version.

Scenario 6: Failure interno of the engine of validation
Given the engine of JSON Schema lanza a error inesperado,
When the service captures the exception,
Then the service responds 500 Internal Server error with code equal to schema_engine_error.

*Related epic: EP07*

TS12: Idempotency for telemetry ingestion

As a Developer,
I want to support idempotency keys in telemetry ingestion,
so that duplicates from Gateway network retries are avoided.

**Acceptance Criteria**

Scenario 1: First ingestion with Idempotency-Key
Given the Gateway sends POST /api/v1/telemetry with header Idempotency-Key unique and payload valid,
When the API processes the request,
Then the API responds 201 Created with telemetryId and replayed equal to false.

Scenario 2: Retry with the same Idempotency-Key
Given there is a result almacenado for the same Idempotency-Key,
When the Gateway resends the same request,
Then the API responds 200 OK with the same telemetryId and replayed equal to true without create a second registration.

Scenario 3: Conflicto of Idempotency-Key with payload distinto
Given the same Idempotency-Key reutiliza with a body diferente,
When the API compares the hash of the payload,
Then the API responds 409 Conflict with code equal to idempotency_payload_mismatch.

Scenario 4: Idempotency-Key with format invalid
Given the header Idempotency-Key no meets the pattern allowed,
When the API validates the header,
Then the API responds 400 Bad Request with code equal to invalid_idempotency_key.

Scenario 5: Expiration of the window of idempotencia
Given the key expired in the store of idempotencia,
When arrives a retry late,
Then the API treats the request as new and responds 201 Created
And registers a warning of late_retry.

Scenario 6: Indisponibilidad of the store of idempotencia
Given the store of keys no responds,
When the API attempts register the key,
Then the API responds 503 Service Unavailable with code equal to idempotency_store_unavailable.

*Related epic: EP07*

TS13: Rate limiting on ingestion endpoints

As a Developer,
I want to apply rate limiting on ingestion endpoints,
so that the API is protected against excessive bursts or device abuse.

**Acceptance Criteria**

Scenario 1: Ingestion inside of the quota allowed
Given the Gateway sends telemetry by debajo of the limit configured by deviceId,
When the API applies the contador of tasa,
Then the API processes the request and responds 201 Created including headers X-RateLimit-Remaining.

Scenario 2: Exceso of tasa by device
Given deviceId exceeds the number maximum of requests by minute,
When the API evaluates the limitador,
Then the API responds 429 Too Many Requests with code equal to rate_limit_exceeded and retryAfter.

Scenario 3: Exceso of tasa global of the tenant
Given the volume agregado of the tenant exceeds the quota global,
When the API applies the limit of tenant,
Then the API responds 429 Too Many Requests with scope equal to tenant.

Scenario 4: Headers of limit absent by error of configuration
Given the service of rate limit no can leer the policy,
When the API handles the configuration failure,
Then the API responds 500 Internal Server error with code equal to rate_limit_config_error or degrades a safe mode documentado.

Scenario 5: Retry respecting retryAfter
Given the Gateway received 429 Too Many Requests with retryAfter,
When the Gateway wait the interval indicado and retries,
Then the API accepts the new request inside of quota and responds 201 Created.

Scenario 6: Bypass unauthorized of rate limit
Given a emisor attempts a header of bypass no reconocido,
When the API ignores the bypass,
Then the API maintains the limit and responds 429 Too Many Requests if the quota is exceeded.

*Related epic: EP07*

TS14: API and Gateway health checks

As a Developer,
I want to expose health checks for the cloud API and the IoT Gateway,
so that dependency degradations can be detected and synchronization retries guided.

**Acceptance Criteria**

Scenario 1: Health check saludable of the API
Given the database and dependencies critical respond,
When a monitor requests GET /api/v1/health,
Then the API responds 200 OK with status equal to up, db equal to up and uptimeSeconds.

Scenario 2: Health check degradado by database lenta
Given the database responds above the threshold of latency,
When the monitor requests GET /api/v1/health,
Then the API responds 200 OK or 503 Service Unavailable according to policy, with status equal to degraded and dbLatencyMs.

Scenario 3: Health check fallido of the API
Given the database no accepts connections,
When the monitor requests GET /api/v1/health,
Then the API responds 503 Service Unavailable with status equal to down.

Scenario 4: Health check local of the Gateway
Given SQLite and the listener local are operativos,
When a process requests GET /local/v1/health,
Then the Gateway responds 200 OK with status equal to up, sqlite equal to up and cloudLink equal to up or down.

Scenario 5: Detection of cloudLink down
Given the Gateway no can complete a ping authenticated a the API,
When the health local recalcula,
Then GET /local/v1/health responds 200 OK with cloudLink equal to down
And activates the contingency mode SQLite.

Scenario 6: Timeout of the monitor of salud
Given the request of health no responds inside of the timeout of the monitor,
When the monitor registers the fails,
Then the monitor treats the componente as unreachable without assume availability.

*Related epic: EP07*

TS15: Retry queue with exponential backoff

As a Developer,
I want to implement a retry queue with exponential backoff on the Gateway,
so that telemetry and events can be resent after transient network or API failures.

**Acceptance Criteria**

Scenario 1: Retry successful after failure transient
Given POST /api/v1/telemetry failed with 503 Service Unavailable
And the registration is in queue,
When the worker executes the next attempt after backoff,
Then the API responds 201 Created
And the registration exits of the queue with status synced.

Scenario 2: Backoff creciente between attempts
Given there are N failures consecutivos for a registration,
When the scheduler calculates the next attempt,
Then the interval of wait crece of way exponencial with cap maxBackoffSeconds.

Scenario 3: Abandonment after maximum of attempts
Given a registration reaches maxAttempts,
When the worker evaluates the abandonment policy,
Then the registration passes a status dead_letter with lastError
And emits a local event of technical alert.

Scenario 4: Retry before timeout of network
Given the client HTTP of the Gateway reports timeout,
When the worker reencola the message,
Then the registration remains pending with attemptCount incrementado.

Scenario 5: No retry before error 400 definitivo
Given the API responds 400 Bad Request by payload invalid,
When the worker classifies the error as no reintentable,
Then the registration passes a failed without new retries automatic.

Scenario 6: Reinicio of the Gateway with queue persistida
Given the process of the Gateway reinicia with mensajes pending in SQLite,
When the worker recovers the queue to the arrancar,
Then the mensajes pending reprograman respecting nextAttemptAt.

*Related epic: EP07*

TS16: Circuit breaker toward the cloud API

As a Developer,
I want to implement a circuit breaker on the Gateway toward the cloud API,
so that network saturation and local processing degradation during prolonged failures are avoided.

**Acceptance Criteria**

Scenario 1: Circuito cerrado in operation normal
Given the tasa of errors toward the API is under the threshold,
When the Gateway sends telemetry,
Then the requests fluyen normally and receive 201 Created or 200 OK.

Scenario 2: Apertura of the circuito by errors consecutivos
Given acumulan failures 5xx or timeouts above the threshold,
When the circuit breaker changes of status,
Then the Gateway stops llamar a the API during openInterval
And queues locally with forwardStatus equal to circuit_open.

Scenario 3: Prueba in status half-open
Given expires openInterval,
When the Gateway sends a request of prueba,
Then if the API responds 201 Created the circuito vuelve a closed; if fails regresa a open.

Scenario 4: Rejection fast in status open
Given the circuito is open,
When a new event requires submission a the cloud,
Then the Gateway no performs the llamada HTTP and registers short_circuit
And responds to the flujo local with queued_local.

Scenario 5: Metrics of status of the circuito
Given there are transiciones of status of the breaker,
When a monitor query GET /local/v1/metrics/circuit-breaker,
Then the Gateway responds 200 OK with state, failureRate and openedAt.

Scenario 6: Failure of the store of metrics of the breaker
Given the componente of metrics no persists the status,
When the Gateway continues with the policy in memoria,
Then the Gateway registers metric_store_error without interrumpir the contingency SQLite.

*Related epic: EP07*

TS17: Threshold and configuration sync to the Gateway

As a Developer,
I want to synchronize thresholds and area parameters from the cloud API to the IoT Gateway,
so that the local rules engine operates with the current configuration.

**Acceptance Criteria**

Scenario 1: Downloads successful of configuration of area
Given there are thresholds published for areaId Z1,
When the Gateway requests GET /api/v1/areas/Z1/config with credentials current,
Then the API responds 200 OK with areaId, co2ThresholdPpm, noiseThresholdDb, configVersion and updatedAt.

Scenario 2: Application local of new configVersion
Given the Gateway receives a configVersion mayor a the local,
When the configuration service updates the cache local,
Then the Gateway persists the configuration in SQLite and responds internally status equal to applied.

Scenario 3: Configuration no modificada
Given the Gateway sends If-None-Match with the version local,
When the API determines that no there is cambios,
Then the API responds 304 Not Modified.

Scenario 4: Rejection due to credencial of Gateway invalid
Given the Gateway presents a token invalid to the descargar configuration,
When the API authenticates the request,
Then the API responds 401 Unauthorized with code equal to unauthorized.

Scenario 5: Configuration corrupta rechazada locally
Given the payload of configuration no meets the schema local,
When the Gateway validates the documento,
Then the Gateway discards the update and keeps the configVersion previous
And reports 200 OK in POST /api/v1/gateway/config-ack with status equal to rejected_schema.

Scenario 6: Timeout during downloads of configuration
Given GET /api/v1/areas/Z1/config exceeds the timeout,
When the Gateway aborts the downloads,
Then the Gateway maintains the configuration local current and schedules a retry.

*Related epic: EP03*

TS18: API request auditing

As a Developer,
I want to record an audit trail of authenticated API requests,
so that security traceability and incident investigation are enabled.

**Acceptance Criteria**

Scenario 1: Registration of audit in ingestion successful
Given POST /api/v1/telemetry responds 201 Created,
When the audit middleware captures the event,
Then persists a auditLog with actorType, deviceId, route, httpStatus 201 and correlationId.

Scenario 2: Registration of audit in rechazo 401
Given a request fails authentication,
When the API responds 401 Unauthorized,
Then the auditLog registers httpStatus 401, reason equal to unauthorized and originIp.

Scenario 3: Query of audit authorized
Given a actor with permiso of safety requests GET /api/v1/audit-logs,
When the API authorizes the query,
Then the API responds 200 OK with items[] of audit and pagination.

Scenario 4: Rejection of query of audit without permiso
Given a JWT without scope of audit requests the logs,
When the API evaluates authorization,
Then the API responds 403 Forbidden with code equal to insufficient_scope.

Scenario 5: Persistence failure audit
Given the store of audit no is available,
When occurs a request of negocio successful,
Then the API responds to the client the code of negocio correspondiente
And registers a error local audit_persist_failed without revertir the operation already confirmada.

Scenario 6: Filtrado by correlationId
Given there are multiple auditLogs,
When the client query GET /api/v1/audit-logs?correlationId=...,
Then the API responds 200 OK with the events associated a that correlationId.

*Related epic: EP07*

TS19: ESP32 heartbeat and disconnect detection

As a Developer,
I want to process periodic ESP32 heartbeats on the Gateway,
so that hardware disconnections can be detected and devices marked unavailable.

**Acceptance Criteria**

Scenario 1: Heartbeat successful of device
Given a ESP32 registered sends POST /local/v1/devices/heartbeat with deviceId and firmwareVersion,
When the Gateway updates the status of the device,
Then the Gateway responds 200 OK with deviceId and status equal to online.

Scenario 2: Marcado offline by absence of heartbeat
Given transcurre the interval maximum without heartbeat of a deviceId,
When the monitor of presence of devices evaluates the timeout,
Then the Gateway marks status equal to offline and generates a event device_offline.

Scenario 3: Rejection of heartbeat no authenticated
Given a emisor sends heartbeat without token valid,
When the Gateway authenticates the request,
Then the Gateway responds 401 Unauthorized.

Scenario 4: Heartbeat with deviceId desconocido
Given the deviceId no is registered in the inventory local,
When the Gateway validates the inventory,
Then the Gateway responds 404 Not Found with code equal to device_not_registered.

Scenario 5: Publication of the status offline toward the cloud
Given a device passes a offline
And there is conectividad cloud,
When the Gateway publishes POST /api/v1/devices/{deviceId}/status,
Then the API responds 200 OK with status equal to offline.

Scenario 6: Failure of publication of status by network outage
Given the device passes a offline during offline contingency,
When the Gateway attempts publish the status,
Then the event remains in SQLite with syncStatus equal to pending.

*Related epic: EP07*

TS20: Cloud persistence of alerts and actuator actions

As a Developer,
I want to persist alerts and actuator actions in the cloud relational database,
so that operational history is available to the mobile app and full history to the web application.

**Acceptance Criteria**

Scenario 1: Persistence successful of alerts
Given the Gateway sends POST /api/v1/alerts with areaId, alertType, measuredValue and detectedAt,
When the API validates and stores the alerts,
Then the API responds 201 Created with alertId and status equal to active.

Scenario 2: Persistence successful of action of actuator
Given the Gateway sends POST /api/v1/actuator-events with actuatorType, action, result and executedAt,
When the API stores the event,
Then the API responds 201 Created with eventId.

Scenario 3: Rejection due to alerts with area inexistente
Given alert.areaId there is no in the catalog,
When the API validates integrity referencial,
Then the API responds 404 Not Found or 422 Unprocessable Entity with code equal to area_not_found.

Scenario 4: Rejection due to payload of action incomplete
Given faltan actuatorType in the body,
When the API validates the schema,
Then the API responds 400 Bad Request with field equal to actuatorType.

Scenario 5: Error 500 to the persist alerts
Given the database fails during the INSERT,
When the API captures the error,
Then the API responds 500 Internal Server error with correlationId.

Scenario 6: Query of history of alerts
Given there are alerts persisted for an area,
When a supervisor authenticated requests GET /api/v1/areas/Z1/alerts,
Then the API responds 200 OK with items[] that include alertId, alertType, status and detectedAt.

*Related epic: EP05*

TS21: User authentication API endpoint for mobile and web

As a Developer,
I want to expose a user authentication endpoint that issues supervisor or plant-manager JWTs,
so that mobile operation/technical-configuration resources and web governance resources are protected.

**Acceptance Criteria**

Scenario 1: Login successful of supervisor
Given there are valid credentials of supervisor,
When the client sends POST /api/v1/auth/login with email and password,
Then the API responds 200 OK with accessToken, refreshToken, role equal to supervisor and expiresIn.

Scenario 2: Login successful of Plant Manager
Given there are valid credentials of manager,
When the client sends POST /api/v1/auth/login,
Then the API responds 200 OK with role equal to plant_manager.

Scenario 3: Rejection due to credentials invalid
Given the password no coincide,
When the API authenticates to the user,
Then the API responds 401 Unauthorized with code equal to invalid_credentials.

Scenario 4: Rejection due to disabled account
Given the account there is with status disabled,
When the API evaluates the status of the account,
Then the API responds 403 Forbidden with code equal to account_disabled.

Scenario 5: Refresh token successful
Given the client presents a refreshToken current in POST /api/v1/auth/refresh,
When the API rotates the token,
Then the API responds 200 OK with a new accessToken.

Scenario 6: Refresh token expired
Given the refreshToken is vencido,
When the API validates the session,
Then the API responds 401 Unauthorized with code equal to refresh_token_expired.

*Related epic: EP02*

TS22: Batch telemetry ingestion

As a Developer,
I want to support batch telemetry ingestion from the Gateway,
so that delivery of multiple measurements accumulated after offline contingency is optimized.

**Acceptance Criteria**

Scenario 1: Ingestion batch successful
Given the Gateway sends POST /api/v1/telemetry/batch with a arreglo items[] of measurements valid,
When the API processes the batch,
Then the API responds 201 Created with acceptedCount, rejectedCount equal to 0 and results[].

Scenario 2: Ingestion batch partially aceptada
Given the batch contains measurements valid and invalid,
When the API evaluates item by item,
Then the API responds 207 Multi-Status with results[] that include status 201 or 422 by item.

Scenario 3: Rejection of batch empty
Given items[] arrives empty,
When the API validates the batch,
Then the API responds 400 Bad Request with code equal to empty_batch.

Scenario 4: Rejection due to size of batch exceeded
Given items[] exceeds maxBatchSize,
When the API validates the size,
Then the API responds 413 payload Too Large with maxBatchSize.

Scenario 5: Timeout during processing of batch grande
Given the processing of the batch exceeds the time maximum of the gateway of API,
When the infraestructura corta the request,
Then the client receives timeout or 504 Gateway Timeout
And the Gateway retries with lotes more small and Idempotency-Key.

Scenario 6: No authenticated in batch
Given the batch sends without credentials,
When the API authenticates,
Then the API responds 401 Unauthorized.

*Related epic: EP07*

TS23: CRUD API for industrial areas and environmental thresholds

As a Developer,
I want to expose REST endpoints for create, read, update, and soft-delete of industrial areas and thresholds,
so that the Safety Supervisor mobile app can persist the operational model by plant sectors.

**Acceptance Criteria**

Scenario 1: Successful creation of industrial area
Given a valid supervisor JWT sends POST /api/v1/areas with name, locationDescription and machineReferences,
When the API validates and persists the area,
Then the API responds 201 Created with areaId, name and status equal to active.

Scenario 2: Update of area thresholds
Given there are thresholds for areaId A1,
When the client sends PUT /api/v1/areas/A1/thresholds with co2ThresholdPpm and noiseThresholdDb,
Then the API responds 200 OK with configVersion incremented and updatedAt.

Scenario 3: Rejection due to duplicate area name
Given an area already exists with the same name,
When the client requests POST /api/v1/areas,
Then the API responds 409 Conflict with code equal to area_name_duplicate.

Scenario 4: Rejection due to out-of-range threshold
Given noiseThresholdDb is negative or exceeds the maximum allowed,
When the API validates dominio,
Then the API responds 422 Unprocessable Entity with field equal to noiseThresholdDb.

Scenario 5: Soft delete of area
Given the supervisor requests DELETE /api/v1/areas/A1,
When the API marcthe area as inactive,
Then the API responds 200 OK with status equal to inactive.

Scenario 6: Error of persistence in database
Given the database fails during INSERT of area,
When the API captures the exception,
Then the API responds 500 Internal Server error with correlationId.

*Related epic: EP03*

TS24: Near real-time alert stream to mobile clients

As a Developer,
I want to publish active alerts through an authenticated event channel,
so that the mobile app can receive risk updates without relying only on polling.

**Acceptance Criteria**

Scenario 1: Subscription successful to the channel of alerts
Given a valid supervisor JWT opens GET /api/v1/alerts/stream with Accept text/event-stream,
When the API accepts the subscription,
Then the API responds 200 OK and starts the stream SSE with event equal to heartbeat.

Scenario 2: Emission of alerts activates to the stream
Given persists a new alerts active,
When the publisher of events notifies a suscriptores of the plant,
Then the clients receive a event JSON with alertId, areaId, alertType and detectedAt.

Scenario 3: Rejection of stream without authentication
Given a client requests the stream without Authorization,
When the API evaluates authentication,
Then the API responds 401 Unauthorized.

Scenario 4: Rejection due to role no operational
Given a JWT of manager requests the stream of alerts operativas,
When the API evaluates authorization,
Then the API responds 403 Forbidden with code equal to role_not_allowed.

Scenario 5: Reconnection after outage of the stream
Given the client pierde the stream by timeout of network,
When the client vuelve a suscribir with Last-Event-ID,
Then the API responds 200 OK and resumes events posteriores to the Last-Event-ID.

Scenario 6: Degradation a polling before indisponibilidad of the publisher
Given the publisher of events no is available,
When the client detects failure of the stream,
Then the client executes GET /api/v1/alerts/active and receives 200 OK with items[] while the stream remains degraded.

*Related epic: EP03*

TS25: ESP32 device inventory and registration in the cloud

As a Developer,
I want to register and query the inventory of ESP32 devices and Gateways in the API,
so that telemetry, heartbeats, and OTA deployments are authorized only for known hardware, with registration authorized to the supervisor.

**Acceptance Criteria**

Scenario 1: Registration successful of device
Given a supervisor authenticated sends POST /api/v1/devices with deviceId, model, firmwareVersion and areaId,
When the API persists the inventory,
Then the API responds 201 Created with deviceId and status equal to registered.

Scenario 2: Query of inventory
Given there are devices registered,
When the client requests GET /api/v1/devices,
Then the API responds 200 OK with items[] that include deviceId, areaId, status and lastSeenAt.

Scenario 3: Rejection due to deviceId duplicate
Given the deviceId already there is,
When the client requests POST /api/v1/devices,
Then the API responds 409 Conflict with code equal to device_already_exists.

Scenario 4: Rejection due to area inexistente
Given areaId no is registered,
When the API validates integrity,
Then the API responds 422 Unprocessable Entity with code equal to area_not_found.

Scenario 5: Revocation of device
Given the supervisor requests POST /api/v1/devices/{deviceId}/revoke,
When the API updates the status,
Then the API responds 200 OK with status equal to revoked
And the siguientes ingestas with that deviceId receive 403 Forbidden.

Scenario 6: Rejection of registration by role of manager
Given a JWT of Plant Manager requests POST /api/v1/devices,
When the API evaluates authorization,
Then the API responds 403 Forbidden with code equal to role_not_allowed.

*Related epic: EP07*

TS26: Local response-time SLA for actuator commands

As a Developer,
I want to instrument and ensure that the local Gateway-ESP32 pipeline applies extractor, siren, and barrier commands with p95 under 2 seconds from the valid measurement that originated the alert,
so that personnel exposure is reduced.

**Acceptance Criteria**

Scenario 1: Cumplimiento of p95 under 2 seconds in activation of extractor
Given the Gateway confirms CO₂ excess with measurement valid and sends command of extractor to the ESP32,
When the ESP32 confirms state equal to on,
Then the Gateway registers latencyMs and responds internally to the evaluador of SLA with status 200 OK symbolic in GET /local/v1/metrics/actuator-latency including p95Ms menor a 2000.

Scenario 2: Cumplimiento of p95 under 2 seconds in siren with presence
Given there is risk condition with presenceDetected equal to true,
When the Gateway completes the activation of siren,
Then GET /local/v1/metrics/actuator-latency responds 200 OK with p95Ms menor a 2000 for actuatorType equal to buzzer.

Scenario 3: Incumplimiento of SLA by timeout of ESP32
Given the Gateway sends a command valid
And the ESP32 no confirms before of 2000 ms,
When the monitor of SLA evaluates the shows,
Then the Gateway registers slaBreach equal to true and publishes POST /api/v1/metrics/sla-breach receiving 202 Accepted when there is cloud, or queues the event in SQLite.

Scenario 4: Invalid measurement excluida of the calculation of SLA
Given arrives a measurement of CO₂ outside of range,
When the engine discards the measurement,
Then GET /local/v1/metrics/actuator-latency responds 200 OK without incrementar contadores of activation by that shows.

Scenario 5: Query of metrics without authentication local
Given a emisor requests GET /local/v1/metrics/actuator-latency without token of Gateway,
When the Gateway authenticates the request,
Then the Gateway responds 401 Unauthorized with code equal to missing_credentials.

Scenario 6: API cloud no available to the reportar breach
Given detects slaBreach equal to true during offline contingency,
When the Gateway attempts POST /api/v1/metrics/sla-breach,
Then the client receives timeout or 503 Service Unavailable
And the event remains pending in SQLite.

*Related epic: EP07*

TS27: Availability target and controlled degradation of API and channels

As a Developer,
I want to instrument a monthly 99.9% availability objective for the cloud API and controlled degradation of mobile/web apps,
so that operation and configuration are sustained with measurable evidence.

**Acceptance Criteria**

Scenario 1: Health up during operation nominal
Given the dependencies critical of the API respond inside of threshold,
When a monitor requests GET /api/v1/health,
Then the API responds 200 OK with status equal to up and db equal to up.

Scenario 2: Health down before fails of database
Given the database no accepts connections,
When the monitor requests GET /api/v1/health,
Then the API responds 503 Service Unavailable with status equal to down.

Scenario 3: Registration of maintenance window planned
Given a operator authorized sends POST /api/v1/maintenance-windows with startAt and endAt,
When the API registers the window,
Then the API responds 201 Created with maintenanceId and excludedFromAvailability equal to true.

Scenario 4: Calculation monthly of availability
Given ends the period monthly of evaluation,
When a process requests GET /api/v1/availability/monthly?period=YYYY-MM,
Then the API responds 200 OK with availabilityPct, objectivePct equal to 99.9 and maintained equal to true or false.

Scenario 5: Continuidad local during indisponibilidad cloud
Given GET /api/v1/health responds 503 Service Unavailable,
When the Gateway evaluates cloudLink,
Then GET /local/v1/health responds 200 OK with cloudLink equal to down and sqlite equal to up maintaining rules locales.

Scenario 6: Query of availability no authorized
Given a client without scope of operaciones requests GET /api/v1/availability/monthly,
When the API evaluates authorization,
Then the API responds 403 Forbidden with code equal to insufficient_scope.

*Related epic: EP07*

<a id="s-3-2"></a>
## 3.2. Impact Mapping

![Impact Map](../assets/03-capitulo-iii/impact-map.png)

<a id="s-3-3"></a>
## 3.3. Product Backlog
<table>
  <thead>
    <tr>
      <th align="left">#</th>
      <th align="left">User Story ID</th>
      <th align="left">Title</th>
      <th align="left">Description</th>
      <th align="left">Story Points</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td align="left">1</td>
      <td align="left">US01</td>
      <td align="left">View SafePlant system information</td>
      <td align="left">As a visitor,<br/>I want to learn the purpose and operation of the SafePlant system,<br/>so that I can understand how it contributes to safety and environmental control in an industrial plant.</td>
      <td align="left">2</td>
    </tr>
    <tr>
      <td align="left">2</td>
      <td align="left">US02</td>
      <td align="left">View SafePlant benefits and advantages</td>
      <td align="left">As a visitor,<br/>I want to learn the benefits and competitive advantages of SafePlant,<br/>so that I can evaluate the value the solution brings to operational safety in an industrial plant.</td>
      <td align="left">1</td>
    </tr>
    <tr>
      <td align="left">3</td>
      <td align="left">US03</td>
      <td align="left">View the development team</td>
      <td align="left">As a visitor,<br/>I want to learn about the SafePlant development team,<br/>so that I can obtain information about the organization responsible for the solution.</td>
      <td align="left">1</td>
    </tr>
    <tr>
      <td align="left">4</td>
      <td align="left">US04</td>
      <td align="left">Submit contact form</td>
      <td align="left">As a visitor,<br/>I want to submit a contact request through the website,<br/>so that I can communicate with the SafePlant team and obtain additional information about the solution.</td>
      <td align="left">3</td>
    </tr>
    <tr>
      <td align="left">5</td>
      <td align="left">US05</td>
      <td align="left">View system technical architecture</td>
      <td align="left">As a visitor,<br/>I want to learn the technical architecture of SafePlant,<br/>so that I can understand how embedded devices, the IoT Gateway, the cloud, the mobile app for operation and technical configuration, and the web application for governance and metrics are integrated.</td>
      <td align="left">2</td>
    </tr>
    <tr>
      <td align="left">6</td>
      <td align="left">US06</td>
      <td align="left">Navigate to the operations mobile app</td>
      <td align="left">As a visitor,<br/>I want to access the mobile app for monitoring, operational control, and technical configuration from the informational site,<br/>so that I can sign in as a Safety Supervisor.</td>
      <td align="left">2</td>
    </tr>
    <tr>
      <td align="left">7</td>
      <td align="left">US07</td>
      <td align="left">Safety Supervisor sign-in on the mobile app</td>
      <td align="left">As a Safety Supervisor,<br/>I want to sign in to the mobile app,<br/>so that I can remotely access monitoring, operational control, area and device registration, and configuration or updates of the safety system.</td>
      <td align="left">3</td>
    </tr>
    <tr>
      <td align="left">8</td>
      <td align="left">US08</td>
      <td align="left">Plant Manager sign-in on the web application</td>
      <td align="left">As a Plant Manager,<br/>I want to sign in to the web application,<br/>so that I can access user and role governance, the metrics dashboard, and the plant's full history.</td>
      <td align="left">3</td>
    </tr>
    <tr>
      <td align="left">9</td>
      <td align="left">US09</td>
      <td align="left">Navigate to the governance and metrics web application</td>
      <td align="left">As a visitor,<br/>I want to access the governance and metrics web application from the informational site,<br/>so that I can sign in as a Plant Manager.</td>
      <td align="left">2</td>
    </tr>
    <tr>
      <td align="left">10</td>
      <td align="left">US10</td>
      <td align="left">Sign out of an authenticated user session</td>
      <td align="left">As a authenticated system user,<br/>I want to end my active session on the mobile app or the web application,<br/>so that I can protect access to system functions against unauthorized use of my account.</td>
      <td align="left">3</td>
    </tr>
    <tr>
      <td align="left">11</td>
      <td align="left">US11</td>
      <td align="left">Create user accounts as Plant Manager</td>
      <td align="left">As a Plant Manager,<br/>I want to create user accounts for Safety Supervisors and Plant Managers in the web application,<br/>so that I can enable controlled access to mobile operations and web governance.</td>
      <td align="left">5</td>
    </tr>
    <tr>
      <td align="left">12</td>
      <td align="left">US12</td>
      <td align="left">Assign user roles and permissions</td>
      <td align="left">As a Plant Manager,<br/>I want to assign and modify roles and permissions for system users in the web application,<br/>so that I can control access to mobile operations and web governance.</td>
      <td align="left">5</td>
    </tr>
    <tr>
      <td align="left">13</td>
      <td align="left">US13</td>
      <td align="left">Recover access credentials</td>
      <td align="left">As a registered system user,<br/>I want to recover access to my account when I forget my credentials,<br/>so that I can restore access to the mobile app or the web application according to my role.</td>
      <td align="left">3</td>
    </tr>
    <tr>
      <td align="left">14</td>
      <td align="left">US14</td>
      <td align="left">Consolidated operational dashboard of plant areas</td>
      <td align="left">As a Safety Supervisor,<br/>I want to view the consolidated operational status of all registered industrial areas in the mobile app,<br/>so that I can obtain a remote real-time overview of environmental and safety status.</td>
      <td align="left">5</td>
    </tr>
    <tr>
      <td align="left">15</td>
      <td align="left">US15</td>
      <td align="left">Real-time CO₂ monitoring by area</td>
      <td align="left">As a Safety Supervisor,<br/>I want to monitor in real time the CO₂ concentration in ppm of an industrial area from the mobile app,<br/>so that I can promptly identify dangerous gas buildups in the industrial environment.</td>
      <td align="left">5</td>
    </tr>
    <tr>
      <td align="left">16</td>
      <td align="left">US16</td>
      <td align="left">Real-time noise monitoring by area</td>
      <td align="left">As a Safety Supervisor,<br/>I want to monitor in real time the noise level in dB of an industrial area from the mobile app,<br/>so that I can promptly identify hazardous noise exposure conditions for operators.</td>
      <td align="left">5</td>
    </tr>
    <tr>
      <td align="left">17</td>
      <td align="left">US17</td>
      <td align="left">Personnel presence monitoring by area</td>
      <td align="left">As a Safety Supervisor,<br/>I want to monitor personnel presence in an industrial area from the mobile app,<br/>so that I can determine whether operators are exposed to hazardous environmental conditions.</td>
      <td align="left">5</td>
    </tr>
    <tr>
      <td align="left">18</td>
      <td align="left">US18</td>
      <td align="left">View active alerts</td>
      <td align="left">As a Safety Supervisor,<br/>I want to view active environmental and safety alerts in the plant from the mobile app,<br/>so that I can promptly address risk conditions detected by the system.</td>
      <td align="left">5</td>
    </tr>
    <tr>
      <td align="left">19</td>
      <td align="left">US19</td>
      <td align="left">View environmental status by industrial areas</td>
      <td align="left">As a Safety Supervisor,<br/>I want to view in the mobile app the environmental status of each registered industrial area,<br/>so that I can identify which areas require immediate attention.</td>
      <td align="left">5</td>
    </tr>
    <tr>
      <td align="left">20</td>
      <td align="left">US20</td>
      <td align="left">Register and manage industrial areas</td>
      <td align="left">As a Safety Supervisor,<br/>I want to register and manage industrial plant areas from the mobile app,<br/>so that I can organize monitoring and associate devices and thresholds with each area.</td>
      <td align="left">3</td>
    </tr>
    <tr>
      <td align="left">21</td>
      <td align="left">US21</td>
      <td align="left">Configure environmental thresholds by area</td>
      <td align="left">As a Safety Supervisor,<br/>I want to configure the allowed CO₂ limits in ppm and noise limits in dB for each registered industrial area from the mobile app,<br/>so that I can determine when an environmental condition represents a risk in that plant sector.</td>
      <td align="left">3</td>
    </tr>
    <tr>
      <td align="left">22</td>
      <td align="left">US22</td>
      <td align="left">Register IoT devices by area</td>
      <td align="left">As a Safety Supervisor,<br/>I want to register sensors and actuators in an industrial area from the mobile app,<br/>so that I can enable environmental monitoring and automatic responses in that plant sector.</td>
      <td align="left">5</td>
    </tr>
    <tr>
      <td align="left">23</td>
      <td align="left">US23</td>
      <td align="left">Plant metrics dashboard and full history</td>
      <td align="left">As a Plant Manager,<br/>I want to consult the metrics dashboard and the full history of measurements, alerts, and plant events in the web application,<br/>so that I can govern operations with consolidated information.</td>
      <td align="left">5</td>
    </tr>
    <tr>
      <td align="left">24</td>
      <td align="left">US24</td>
      <td align="left">Correlate personnel presence with CO₂ levels</td>
      <td align="left">As a Safety Supervisor,<br/>I want the system to simultaneously evaluate personnel presence and CO₂ levels in an industrial area and present the resulting alert in the mobile app,<br/>so that I can determine whether operators are exposed to dangerous gas concentrations.</td>
      <td align="left">5</td>
    </tr>
    <tr>
      <td align="left">25</td>
      <td align="left">US25</td>
      <td align="left">Classify exposure severity by area</td>
      <td align="left">As a Safety Supervisor,<br/>I want to view in the mobile app the exposure severity of each industrial area based on presence and environmental exceedance,<br/>so that I can prioritize remote operational attention.</td>
      <td align="left">3</td>
    </tr>
    <tr>
      <td align="left">26</td>
      <td align="left">US26</td>
      <td align="left">Short history of personnel exposures by area</td>
      <td align="left">As a Safety Supervisor,<br/>I want to consult in the mobile app the short history of recent exposures by area,<br/>so that I can address active incidents and verify the immediate effectiveness of automatic responses.</td>
      <td align="left">3</td>
    </tr>
    <tr>
      <td align="left">27</td>
      <td align="left">US27</td>
      <td align="left">Detect CO₂ excess</td>
      <td align="left">As a Safety Supervisor,<br/>I want the system to detect when the CO₂ concentration exceeds the allowed limit in an industrial area,<br/>so that automatic purification and prevention measures can be activated promptly.</td>
      <td align="left">3</td>
    </tr>
    <tr>
      <td align="left">28</td>
      <td align="left">US28</td>
      <td align="left">Detect excessive noise</td>
      <td align="left">As a Safety Supervisor,<br/>I want the system to detect when the sound level exceeds the allowed limit in an industrial area,<br/>so that operator exposure to hazardous noise levels can be prevented.</td>
      <td align="left">3</td>
    </tr>
    <tr>
      <td align="left">29</td>
      <td align="left">US29</td>
      <td align="left">Automatic air extractor activation for CO₂</td>
      <td align="left">As a Safety Supervisor,<br/>I want the system to automatically activate the air extractor through the control relay when CO₂ excess is detected,<br/>so that gas concentration can be reduced and safe environmental conditions restored.</td>
      <td align="left">5</td>
    </tr>
    <tr>
      <td align="left">30</td>
      <td align="left">US30</td>
      <td align="left">Preventive siren activation for hazardous exposure</td>
      <td align="left">As a Safety Supervisor,<br/>I want the system to activate the preventive siren when an operator is exposed to a hazardous CO₂ or excessive noise condition,<br/>so that the existing risk can be warned immediately and area evacuation enabled.</td>
      <td align="left">3</td>
    </tr>
    <tr>
      <td align="left">31</td>
      <td align="left">US31</td>
      <td align="left">Deploy acoustic barriers for noise exposure</td>
      <td align="left">As a Safety Supervisor,<br/>I want the system to deploy mobile acoustic isolation barriers via servomotors when excessive noise with personnel present is detected,<br/>so that operator noise exposure in the affected area can be reduced.</td>
      <td align="left">3</td>
    </tr>
    <tr>
      <td align="left">32</td>
      <td align="left">US32</td>
      <td align="left">Remote manual actuator override in emergency</td>
      <td align="left">As a Safety Supervisor,<br/>I want to manually override an actuator state remotely from the mobile app during an emergency,<br/>so that I can take direct control of extractors, sirens, or barriers when the automatic response is not adequate for the situation.</td>
      <td align="left">8</td>
    </tr>
    <tr>
      <td align="left">33</td>
      <td align="left">US33</td>
      <td align="left">Short log of executed automatic actions</td>
      <td align="left">As a Safety Supervisor,<br/>I want to consult the short log of recent automatic actions from the mobile app,<br/>so that I can verify that prevention mechanisms responded to the hazardous conditions detected.</td>
      <td align="left">3</td>
    </tr>
    <tr>
      <td align="left">34</td>
      <td align="left">US34</td>
      <td align="left">Physical alarm notification to the exposed operator</td>
      <td align="left">As a plant operator,<br/>I want to receive an audible physical alarm when exposed to a hazardous CO₂ or excessive noise condition,<br/>so that I can recognize the risk situation and leave the affected area.</td>
      <td align="left">3</td>
    </tr>
    <tr>
      <td align="left">35</td>
      <td align="left">US35</td>
      <td align="left">Update system configuration parameters</td>
      <td align="left">As a Safety Supervisor,<br/>I want to apply updates to system configuration parameters from the mobile app,<br/>so that areas, thresholds, devices, and rules remain aligned with plant safety operations.</td>
      <td align="left">3</td>
    </tr>
    <tr>
      <td align="left">36</td>
      <td align="left">US36</td>
      <td align="left">Mobile app and web application compatibility</td>
      <td align="left">As a Safety Supervisor,<br/>I want to use the mobile app on current Android and iOS devices to operate and technically configure the safety system, and as a Plant Manager I want to use the web application in modern browsers to govern users and consult metrics and history,<br/>so that each role can use the authorized channel on supported environments.</td>
      <td align="left">3</td>
    </tr>
    <tr>
      <td align="left">37</td>
      <td align="left">TS01</td>
      <td align="left">API endpoint for telemetry ingestion</td>
      <td align="left">As a Developer,<br/>I want to expose a REST telemetry ingestion endpoint in JSON format,<br/>so that CO₂, noise, and presence measurements sent by the IoT Gateway can be persisted to the cloud.</td>
      <td align="left">5</td>
    </tr>
    <tr>
      <td align="left">38</td>
      <td align="left">TS02</td>
      <td align="left">Secure authentication and TLS channel for devices and sessions</td>
      <td align="left">As a Developer,<br/>I want to authenticate ESP32 devices and the IoT Gateway via JWT or API Key and require TLS for API communication, in addition to valid user tokens,<br/>so that access is restricted and confidentiality and integrity are preserved.</td>
      <td align="left">5</td>
    </tr>
    <tr>
      <td align="left">39</td>
      <td align="left">TS03</td>
      <td align="left">Local contingency persistence in Gateway SQLite</td>
      <td align="left">As a Developer,<br/>I want to persist measurements and events in the IoT Gateway SQLite when internet connectivity loss is detected,<br/>so that operational traceability is retained during offline contingency.</td>
      <td align="left">8</td>
    </tr>
    <tr>
      <td align="left">40</td>
      <td align="left">TS04</td>
      <td align="left">Asynchronous synchronization of local data to the cloud</td>
      <td align="left">As a Developer,<br/>I want to automatically synchronize SQLite-queued records to the cloud database when internet is restored,<br/>so that operational history consistency is restored.</td>
      <td align="left">8</td>
    </tr>
    <tr>
      <td align="left">41</td>
      <td align="left">TS05</td>
      <td align="left">OTA remote update distribution service</td>
      <td align="left">As a Developer,<br/>I want to distribute authenticated OTA firmware updates to ESP32 devices from the cloud,<br/>so that security patches and sensor corrections can be applied without physical intervention.</td>
      <td align="left">5</td>
    </tr>
    <tr>
      <td align="left">42</td>
      <td align="left">TS06</td>
      <td align="left">ESP32 telemetry reception at the IoT Gateway</td>
      <td align="left">As a Developer,<br/>I want to expose a local endpoint on the IoT Gateway to receive authenticated telemetry from ESP32 devices and normalize it before sending it to the cloud or SQLite,<br/>so that device measurements are accepted and prepared for cloud or local contingency paths.</td>
      <td align="left">8</td>
    </tr>
    <tr>
      <td align="left">43</td>
      <td align="left">TS07</td>
      <td align="left">Exposure evaluation engine by presence and thresholds</td>
      <td align="left">As a Developer,<br/>I want to evaluate on the Gateway the combination of PIR presence with CO₂ and noise thresholds,<br/>so that exposure alerts can be generated and actuator activation decided.</td>
      <td align="left">5</td>
    </tr>
    <tr>
      <td align="left">44</td>
      <td align="left">TS08</td>
      <td align="left">Actuator command emission to ESP32</td>
      <td align="left">As a Developer,<br/>I want to send control commands from the IoT Gateway to the ESP32,<br/>so that the extractor, buzzer, and barrier servomotors can be operated reliably.</td>
      <td align="left">5</td>
    </tr>
    <tr>
      <td align="left">45</td>
      <td align="left">TS09</td>
      <td align="left">API endpoint for telemetry query by area</td>
      <td align="left">As a Developer,<br/>I want to expose a REST endpoint for recent telemetry queries by area,<br/>so that the mobile app operational monitoring can be fed.</td>
      <td align="left">3</td>
    </tr>
    <tr>
      <td align="left">46</td>
      <td align="left">TS10</td>
      <td align="left">API endpoint for remote actuator override</td>
      <td align="left">As a Developer,<br/>I want to expose a REST endpoint for remote manual actuator override by an authenticated supervisor,<br/>so that emergency operational control from the mobile app is enabled.</td>
      <td align="left">5</td>
    </tr>
    <tr>
      <td align="left">47</td>
      <td align="left">TS11</td>
      <td align="left">Telemetry JSON schema validation</td>
      <td align="left">As a Developer,<br/>I want to validate the telemetry JSON schema on the Gateway and API,<br/>so that corrupt or incomplete payloads are rejected before persistence.</td>
      <td align="left">3</td>
    </tr>
    <tr>
      <td align="left">48</td>
      <td align="left">TS12</td>
      <td align="left">Idempotency for telemetry ingestion</td>
      <td align="left">As a Developer,<br/>I want to support idempotency keys in telemetry ingestion,<br/>so that duplicates from Gateway network retries are avoided.</td>
      <td align="left">5</td>
    </tr>
    <tr>
      <td align="left">49</td>
      <td align="left">TS13</td>
      <td align="left">Rate limiting on ingestion endpoints</td>
      <td align="left">As a Developer,<br/>I want to apply rate limiting on ingestion endpoints,<br/>so that the API is protected against excessive bursts or device abuse.</td>
      <td align="left">5</td>
    </tr>
    <tr>
      <td align="left">50</td>
      <td align="left">TS14</td>
      <td align="left">API and Gateway health checks</td>
      <td align="left">As a Developer,<br/>I want to expose health checks for the cloud API and the IoT Gateway,<br/>so that dependency degradations can be detected and synchronization retries guided.</td>
      <td align="left">3</td>
    </tr>
    <tr>
      <td align="left">51</td>
      <td align="left">TS15</td>
      <td align="left">Retry queue with exponential backoff</td>
      <td align="left">As a Developer,<br/>I want to implement a retry queue with exponential backoff on the Gateway,<br/>so that telemetry and events can be resent after transient network or API failures.</td>
      <td align="left">3</td>
    </tr>
    <tr>
      <td align="left">52</td>
      <td align="left">TS16</td>
      <td align="left">Circuit breaker toward the cloud API</td>
      <td align="left">As a Developer,<br/>I want to implement a circuit breaker on the Gateway toward the cloud API,<br/>so that network saturation and local processing degradation during prolonged failures are avoided.</td>
      <td align="left">5</td>
    </tr>
    <tr>
      <td align="left">53</td>
      <td align="left">TS17</td>
      <td align="left">Threshold and configuration sync to the Gateway</td>
      <td align="left">As a Developer,<br/>I want to synchronize thresholds and area parameters from the cloud API to the IoT Gateway,<br/>so that the local rules engine operates with the current configuration.</td>
      <td align="left">3</td>
    </tr>
    <tr>
      <td align="left">54</td>
      <td align="left">TS18</td>
      <td align="left">API request auditing</td>
      <td align="left">As a Developer,<br/>I want to record an audit trail of authenticated API requests,<br/>so that security traceability and incident investigation are enabled.</td>
      <td align="left">3</td>
    </tr>
    <tr>
      <td align="left">55</td>
      <td align="left">TS19</td>
      <td align="left">ESP32 heartbeat and disconnect detection</td>
      <td align="left">As a Developer,<br/>I want to process periodic ESP32 heartbeats on the Gateway,<br/>so that hardware disconnections can be detected and devices marked unavailable.</td>
      <td align="left">3</td>
    </tr>
    <tr>
      <td align="left">56</td>
      <td align="left">TS20</td>
      <td align="left">Cloud persistence of alerts and actuator actions</td>
      <td align="left">As a Developer,<br/>I want to persist alerts and actuator actions in the cloud relational database,<br/>so that operational history is available to the mobile app and full history to the web application.</td>
      <td align="left">3</td>
    </tr>
    <tr>
      <td align="left">57</td>
      <td align="left">TS21</td>
      <td align="left">User authentication API endpoint for mobile and web</td>
      <td align="left">As a Developer,<br/>I want to expose a user authentication endpoint that issues supervisor or plant-manager JWTs,<br/>so that mobile operation/technical-configuration resources and web governance resources are protected.</td>
      <td align="left">2</td>
    </tr>
    <tr>
      <td align="left">58</td>
      <td align="left">TS22</td>
      <td align="left">Batch telemetry ingestion</td>
      <td align="left">As a Developer,<br/>I want to support batch telemetry ingestion from the Gateway,<br/>so that delivery of multiple measurements accumulated after offline contingency is optimized.</td>
      <td align="left">5</td>
    </tr>
    <tr>
      <td align="left">59</td>
      <td align="left">TS23</td>
      <td align="left">CRUD API for industrial areas and environmental thresholds</td>
      <td align="left">As a Developer,<br/>I want to expose REST endpoints for create, read, update, and soft-delete of industrial areas and thresholds,<br/>so that the Safety Supervisor mobile app can persist the operational model by plant sectors.</td>
      <td align="left">3</td>
    </tr>
    <tr>
      <td align="left">60</td>
      <td align="left">TS24</td>
      <td align="left">Near real-time alert stream to mobile clients</td>
      <td align="left">As a Developer,<br/>I want to publish active alerts through an authenticated event channel,<br/>so that the mobile app can receive risk updates without relying only on polling.</td>
      <td align="left">3</td>
    </tr>
    <tr>
      <td align="left">61</td>
      <td align="left">TS25</td>
      <td align="left">ESP32 device inventory and registration in the cloud</td>
      <td align="left">As a Developer,<br/>I want to register and query the inventory of ESP32 devices and Gateways in the API,<br/>so that telemetry, heartbeats, and OTA deployments are authorized only for known hardware, with registration authorized to the supervisor.</td>
      <td align="left">5</td>
    </tr>
    <tr>
      <td align="left">62</td>
      <td align="left">TS26</td>
      <td align="left">Local response-time SLA for actuator commands</td>
      <td align="left">As a Developer,<br/>I want to instrument and ensure that the local Gateway-ESP32 pipeline applies extractor, siren, and barrier commands with p95 under 2 seconds from the valid measurement that originated the alert,<br/>so that personnel exposure is reduced.</td>
      <td align="left">5</td>
    </tr>
    <tr>
      <td align="left">63</td>
      <td align="left">TS27</td>
      <td align="left">Availability target and controlled degradation of API and channels</td>
      <td align="left">As a Developer,<br/>I want to instrument a monthly 99.9% availability objective for the cloud API and controlled degradation of mobile/web apps,<br/>so that operation and configuration are sustained with measurable evidence.</td>
      <td align="left">5</td>
    </tr>
  </tbody>
</table>
