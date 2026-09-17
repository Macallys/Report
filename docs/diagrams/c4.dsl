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

            webBackend = container "Web Monolithic Backend" "Single cloud process. Four internal modules: Identity & Access, Plant Monitoring, Safety & Actuation, Device & Edge Management." "TBD" "Backend" {
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
            }

            cloudDatabase = container "Cloud Database" "Backing store for the monolithic backend." "TBD" "Database"
            messageBroker = container "MQTT Broker" "Internal pub/sub between field firmware and the Edge Application. Product TBD." "TBD" "MessageBroker"
            edgeApplication = container "Edge Application" "Plant-server software: MQTT ingest, cloud sync, and offline queue." "TBD" "Edge"
            edgeDatabase = container "Edge Database" "Local queue and offline alert copies." "TBD" "Database"
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

            deviceEmbeddedApp -> fieldHardware "Reads sensors and drives actuators"
            deviceEmbeddedApp -> messageBroker "Publishes readings"
            edgeApplication -> messageBroker "Consumes readings"
            edgeApplication -> webBackend "Ingests telemetry and syncs credentials"
            edgeApplication -> edgeDatabase "Reads from and writes to"
            webBackend -> edgeApplication "Stores offline alert copies"
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
        }
    }
}
