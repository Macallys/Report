workspace "SafePlant" "IoT platform for occupational safety monitoring in industrial plants (Macallys)." {

    model {
        supervisor = person "Supervisor" "Field operator of the mobile app: plant setup, status, and actuator override."
        plantManager = person "Plant Manager" "Uses the web client for accounts, plant setup, and analytics."
        visitor = person "Visitor" "Anonymous visitor of the public landing site." "Visitor"

        fieldHardware = softwareSystem "Field Device Hardware" "ESP32, sensors (CO₂, noise, presence), and actuators (extractor, siren, acoustic barrier)." "External, Hardware"
        emailService = softwareSystem "Email Service" "Sends credential-recovery emails. Provider TBD." "External"

        safePlant = softwareSystem "SafePlant" "IoT platform for plant environmental monitoring, occupational safety, and actuation." {
            supervisorMobileApp = container "Supervisor Mobile App" "Sign-in, plant setup, operational status, and actuator override." "Flutter" "MobileApp"
            plantManagerWebClient = container "Plant Manager Web Client" "Sign-in, account management, and plant analytics." "Angular" "Browser"
            landingWebsite = container "SafePlant Landing Website" "Public marketing site." "TBD" "StaticContent"

            webBackend = container "Web Monolithic Backend" "Single cloud process. Four internal modules: Identity & Access, Plant Monitoring, Safety & Actuation, Device & Edge Management. Cloud Safety is audit, status, and override when WAN is up." "TBD" "Backend" {
                identityInterface = component "Identity Interface Layer" "UserAccountController, SessionController, CredentialRecoveryController. HTTP endpoints for sign-in, account/role management, and credential recovery." "TBD" "IdentityComponent"
                identityApplication = component "Identity Application Layer" "Command/query handlers: CreateUserAccount, AssignUserRole, SignIn, CloseSession, RequestCredentialRecovery, ResetCredentials, GetUserAccountsDirectory." "TBD" "IdentityComponent"
                identityDomain = component "Identity Domain Layer" "Aggregates UserAccount, Session, CredentialRecovery. Enforces unique email, channel/role rules (mobile supervisor vs. web plant manager)." "TBD" "IdentityComponent"
                identityInfrastructure = component "Identity Infrastructure Layer" "Repository implementations for UserAccount, Session, CredentialRecovery, and the EmailServiceAdapter." "TBD" "IdentityComponent"

                identityInterface -> identityApplication "Delegates commands and queries"
                identityApplication -> identityDomain "Invokes aggregates and enforces invariants"
                identityApplication -> identityInfrastructure "Persists via repositories"

                plantMonitoringInterface = component "Plant Monitoring Interface Layer" "PlantSetupController, PlantMetricsController, TelemetryIngestConsumer. HTTP for plant setup and history; in-process ingest from Edge." "TBD" "PlantMonitoringComponent"
                plantMonitoringApplication = component "Plant Monitoring Application Layer" "Command/query handlers: ManageIndustrialArea, ConfigureEnvironmentalThresholds, AssociateDeviceToArea, IngestTelemetry, GetAreaSetupSheet, GetPlantMetricsHistory." "TBD" "PlantMonitoringComponent"
                plantMonitoringDomain = component "Plant Monitoring Domain Layer" "Aggregates IndustrialArea, AreaThresholds, AreaDeviceAssignment, AreaTelemetry. Separate CO₂, noise, and presence facts; no exposure evaluation." "TBD" "PlantMonitoringComponent"
                plantMonitoringInfrastructure = component "Plant Monitoring Infrastructure Layer" "Repository implementations for the four aggregates and an in-process domain-event publisher." "TBD" "PlantMonitoringComponent"

                plantMonitoringInterface -> plantMonitoringApplication "Delegates commands and queries"
                plantMonitoringApplication -> plantMonitoringDomain "Invokes aggregates and enforces invariants"
                plantMonitoringApplication -> plantMonitoringInfrastructure "Persists via repositories"

                safetyInterface = component "Safety & Actuation Interface Layer" "AreaSafetyController. HTTP for operational status, alerts, and override; receives exposure/alert sync from the Edge runtime." "TBD" "SafetyActuationComponent"
                safetyApplication = component "Safety & Actuation Application Layer" "Command/query handlers: AreaOperationalStatus, ActiveAlerts, override actuator (forwarded to Edge when WAN is up). Audit of synced exposure." "TBD" "SafetyActuationComponent"
                safetyDomain = component "Safety & Actuation Domain Layer" "Aggregates ExposureState and AreaActuators (cloud copy). Same language as the Edge runtime; cloud is not the live control loop." "TBD" "SafetyActuationComponent"
                safetyInfrastructure = component "Safety & Actuation Infrastructure Layer" "Repositories on Cloud Database; override forwarding toward Edge Safety; no FirmwareActuatorAdapter here." "TBD" "SafetyActuationComponent"

                safetyInterface -> safetyApplication "Delegates commands and queries"
                safetyApplication -> safetyDomain "Invokes aggregates and enforces invariants"
                safetyApplication -> safetyInfrastructure "Persists via repositories"

                deviceEdgeInterface = component "Device & Edge Interface Layer (cloud)" "DeviceCredentialController. Issue and revoke device credentials; source of truth in the cloud." "TBD" "DeviceEdgeComponent"
                deviceEdgeApplication = component "Device & Edge Application Layer (cloud)" "Command handlers: issue, authenticate against master, revoke device credentials." "TBD" "DeviceEdgeComponent"
                deviceEdgeDomain = component "Device & Edge Domain Layer (cloud)" "Aggregate DeviceCredential. Device identity is not a user account." "TBD" "DeviceEdgeComponent"
                deviceEdgeInfrastructure = component "Device & Edge Infrastructure Layer (cloud)" "DeviceCredentialRepository and credential sync toward the Edge Application." "TBD" "DeviceEdgeComponent"

                deviceEdgeInterface -> deviceEdgeApplication "Delegates commands"
                deviceEdgeApplication -> deviceEdgeDomain "Invokes aggregates and enforces invariants"
                deviceEdgeApplication -> deviceEdgeInfrastructure "Persists via repositories"
            }

            cloudDatabase = container "Cloud Database" "Backing store for the monolithic backend." "TBD" "Database"
            messageBroker = container "MQTT Broker" "Internal pub/sub between field firmware and the Edge Application. Product TBD." "TBD" "MessageBroker"
            edgeApplication = container "Edge Application" "Plant-server software: Device & Edge runtime (MQTT ingest, queue, sync), Plant Monitoring projection, and Safety & Actuation live loop." "TBD" "Edge" {
                edgeRuntimeInterface = component "Device & Edge Interface Layer (runtime)" "DeviceAuthenticationController, MqttTelemetryConsumer, OfflineAlertConsumer. No IoT Gateway collaborator." "TBD" "DeviceEdgeComponent"
                edgeRuntimeApplication = component "Device & Edge Application Layer (runtime)" "Handlers: authenticate device, ingest telemetry, queue locally, sync, store offline alert copy." "TBD" "DeviceEdgeComponent"
                edgeRuntimeDomain = component "Device & Edge Domain Layer (runtime)" "Aggregate EdgeNode. Local queue, sync idempotency, offline alert copies. Does not evaluate exposure." "TBD" "DeviceEdgeComponent"
                edgeRuntimeInfrastructure = component "Device & Edge Infrastructure Layer (runtime)" "Edge queue repository, MQTT adapter, ingest adapter toward Plant Monitoring, credential sync adapter." "TBD" "DeviceEdgeComponent"

                edgeRuntimeInterface -> edgeRuntimeApplication "Delegates commands"
                edgeRuntimeApplication -> edgeRuntimeDomain "Invokes aggregates and enforces invariants"
                edgeRuntimeApplication -> edgeRuntimeInfrastructure "Persists via repositories"

                plantMonitoringProjection = component "Plant Monitoring Projection" "Cached thresholds and last CO₂, noise, and presence facts for the local Safety loop. Not a plant-setup API; system of record stays in the cloud." "TBD" "PlantMonitoringComponent"

                safetyEdgeInterface = component "Safety & Actuation Interface Layer (runtime)" "PlantTelemetryEventConsumer from the local projection; override forwarded from cloud Safety when WAN is up." "TBD" "SafetyActuationComponent"
                safetyEdgeApplication = component "Safety & Actuation Application Layer (runtime)" "Handlers: detect excess, evaluate exposure, classify, raise/withdraw alert, activate/normalize actuator (live loop)." "TBD" "SafetyActuationComponent"
                safetyEdgeDomain = component "Safety & Actuation Domain Layer (runtime)" "Aggregates ExposureState and AreaActuators. In-process PO-03–PO-08. Commands by area and actuator type; no Device entity." "TBD" "SafetyActuationComponent"
                safetyEdgeInfrastructure = component "Safety & Actuation Infrastructure Layer (runtime)" "Repositories on Edge Database, FirmwareActuatorAdapter, OfflineAlertCopyAdapter toward EdgeNode, sync of exposure/alerts toward cloud." "TBD" "SafetyActuationComponent"

                safetyEdgeInterface -> safetyEdgeApplication "Delegates commands"
                safetyEdgeApplication -> safetyEdgeDomain "Invokes aggregates and enforces invariants"
                safetyEdgeApplication -> safetyEdgeInfrastructure "Persists via repositories"
            }
            edgeDatabase = container "Edge Database" "Local queue, offline alert copies, and live exposure/actuator state." "TBD" "Database"
            deviceEmbeddedApp = container "Device Embedded Application" "Firmware on the field hardware: sensors, actuators, MQTT publish." "TBD" "IoT"

            supervisor -> supervisorMobileApp "Uses"
            plantManager -> plantManagerWebClient "Uses"
            visitor -> landingWebsite "Browses"

            supervisorMobileApp -> webBackend "Sign-in, plant setup, status, override"
            plantManagerWebClient -> webBackend "Sign-in, accounts, analytics"

            webBackend -> cloudDatabase "Reads from and writes to"
            webBackend -> emailService "Sends recovery emails"

            supervisorMobileApp -> identityInterface "Sign-in, close session"
            plantManagerWebClient -> identityInterface "Sign-in, accounts, role assignment, credential recovery"
            identityInfrastructure -> cloudDatabase "Reads from and writes to"
            identityInfrastructure -> emailService "Sends recovery emails"

            supervisorMobileApp -> plantMonitoringInterface "Plant setup (areas, thresholds, device assignment)"
            plantManagerWebClient -> plantMonitoringInterface "Plant metrics history"
            edgeApplication -> plantMonitoringInterface "Ingests telemetry"
            plantMonitoringInfrastructure -> cloudDatabase "Reads from and writes to"

            deviceEdgeInfrastructure -> cloudDatabase "Reads from and writes to"
            edgeRuntimeInfrastructure -> edgeDatabase "Reads from and writes to"
            edgeRuntimeInfrastructure -> plantMonitoringInterface "Ingests telemetry"
            edgeRuntimeInfrastructure -> deviceEdgeInterface "Syncs device credentials"
            deviceEmbeddedApp -> edgeRuntimeInterface "Authenticate device"
            edgeRuntimeInterface -> messageBroker "Consumes readings"
            edgeRuntimeInfrastructure -> plantMonitoringProjection "Feeds last readings for the local loop"
            plantMonitoringProjection -> safetyEdgeInterface "Publishes last readings and threshold context"
            plantMonitoringInfrastructure -> plantMonitoringProjection "Caches thresholds when WAN is up"

            supervisorMobileApp -> safetyInterface "Operational status, active alerts, actuator override"
            safetyInfrastructure -> cloudDatabase "Reads from and writes to"
            safetyInfrastructure -> safetyEdgeInterface "Forwards override when WAN is up"
            safetyEdgeInfrastructure -> edgeDatabase "Reads from and writes to"
            safetyEdgeInfrastructure -> deviceEmbeddedApp "Activate / normalize actuator"
            safetyEdgeInfrastructure -> edgeRuntimeInterface "Stores offline alert copies"
            safetyEdgeInfrastructure -> safetyInterface "Syncs exposure and alerts when WAN is up"

            deviceEmbeddedApp -> fieldHardware "Reads sensors and drives actuators"
            deviceEmbeddedApp -> messageBroker "Publishes readings"
            edgeApplication -> messageBroker "Consumes readings"
            edgeApplication -> webBackend "Ingests telemetry and syncs credentials, alerts, and exposure"
            edgeApplication -> edgeDatabase "Reads from and writes to"
            edgeApplication -> deviceEmbeddedApp "Activate / normalize actuator"
            webBackend -> edgeApplication "Syncs device credentials and forwards actuator override"
        }
    }

    views {
        systemLandscape "SystemLandscape" {
            include *
            autoLayout lr 300 150
        }

        systemContext safePlant "SystemContext" {
            include *
            autoLayout lr 300 150
        }

        container safePlant "ContainerView" {
            include *
            autoLayout lr 350 200
        }

        component webBackend "IdentityAccessComponents" {
            include supervisorMobileApp plantManagerWebClient identityInterface identityApplication identityDomain identityInfrastructure cloudDatabase emailService
            autoLayout lr 300 150
        }

        component webBackend "PlantMonitoringComponents" {
            include supervisorMobileApp plantManagerWebClient edgeApplication plantMonitoringInterface plantMonitoringApplication plantMonitoringDomain plantMonitoringInfrastructure cloudDatabase
            autoLayout lr 300 150
        }

        component webBackend "SafetyActuationComponents" {
            include supervisorMobileApp safetyInterface safetyApplication safetyDomain safetyInfrastructure cloudDatabase safetyEdgeInterface
            autoLayout lr 300 150
        }

        component edgeApplication "SafetyActuationEdgeComponents" {
            include plantMonitoringProjection safetyEdgeInterface safetyEdgeApplication safetyEdgeDomain safetyEdgeInfrastructure edgeDatabase deviceEmbeddedApp fieldHardware edgeRuntimeInterface
            autoLayout lr 300 150
        }

        component webBackend "DeviceEdgeCloudComponents" {
            include deviceEdgeInterface deviceEdgeApplication deviceEdgeDomain deviceEdgeInfrastructure cloudDatabase edgeRuntimeInfrastructure
            autoLayout lr 300 150
        }

        component edgeApplication "DeviceEdgeRuntimeComponents" {
            include deviceEmbeddedApp messageBroker edgeRuntimeInterface edgeRuntimeApplication edgeRuntimeDomain edgeRuntimeInfrastructure edgeDatabase plantMonitoringInterface plantMonitoringProjection safetyEdgeInterface
            autoLayout lr 300 150
        }

        styles {
            element "Element" {
                color darkcyan
                stroke darkcyan
                strokeWidth 7
                shape RoundedBox
            }
            element "Person" {
                shape Person
            }
            element "Visitor" {
                shape Person
                background gray
                stroke gray
                color white
            }
            element "Software System" {
            }
            element "Container" {
            }
            element "Database" {
                shape Cylinder
            }
            element "Backend" {
                background #eef0f5
                stroke #7f8c9a
                strokeWidth 3
            }
            element "MobileApp" {
                shape MobileDeviceLandscape
            }
            element "Browser" {
                shape WebBrowser
            }
            element "StaticContent" {
                shape Folder
            }
            element "MessageBroker" {
                shape Pipe
                background #f3f2f1
            }
            element "Edge" {
                shape RoundedBox
            }
            element "IoT" {
                shape RoundedBox
            }
            element "External" {
                color white
                stroke darkgray
                background darkgray
            }
            element "Hardware" {
            }
            element "IdentityComponent" {
                shape Hexagon
                background #eaf7f5
                stroke darkcyan
            }
            element "PlantMonitoringComponent" {
                shape Hexagon
                background #eaf7f5
                stroke darkcyan
            }
            element "SafetyActuationComponent" {
                shape Hexagon
                background #eaf7f5
                stroke darkcyan
            }
            element "DeviceEdgeComponent" {
                shape Hexagon
                background #eaf7f5
                stroke darkcyan
            }
        }
    }
}
