# AlLibrary System Architecture Diagrams

## 🏗️ System Overview

This document contains the comprehensive software engineering diagrams for the AlLibrary system, following SOLID principles, cultural sensitivity requirements, and anti-censorship architecture.

---

## 🌐 System Context Diagram

```mermaid
graph TB
    subgraph "External Actors"
        U[Users/Researchers]
        C[Cultural Communities]
        G[Cultural Guardians]
        E[Educational Institutions]
    end

    subgraph "AlLibrary System"
        AL[AlLibrary Desktop App]
    end

    subgraph "External Systems"
        P2P[P2P Network/IPFS]
        TOR[TOR Network]
        LS[Local SQLite Storage]
        CS[Cultural Authority Systems]
        VS[Verification Services]
    end

    U --> AL
    C --> AL
    G --> AL
    E --> AL

    AL --> P2P
    AL --> TOR
    AL --> LS
    AL --> CS
    AL --> VS

    AL -.->|"Cultural Validation"| C
    AL -.->|"Permission Requests"| G
    AL -.->|"Content Verification"| CS

    P2P -.->|"Decentralized Content"| AL
    TOR -.->|"Anonymous Access"| AL
```

---

## 🧩 Component Architecture Diagram

```mermaid
graph TB
    subgraph "Presentation Layer"
        HP[HomePage]
        SP[SearchPage]
        MDP[MyDocumentsPage]
        CP[CollectionsPage]
        BCP[BrowseCategoriesPage]
        AP[AboutPage]
        STP[SettingsPage]
    end

    subgraph "Component Library"
        subgraph "Foundation"
            BTN[Button]
            INP[Input]
            CRD[Card]
            MDL[Modal]
        end

        subgraph "Domain"
            DC[DocumentCard]
            CC[CollectionCard]
            CCX[CulturalContext]
            PC[PeerCard]
        end

        subgraph "Composite"
            SI[SearchInterface]
            DM[DownloadManager]
            NG[NetworkGraph]
        end
    end

    subgraph "Service Layer"
        DS[DocumentService]
        CS[CollectionService]
        CSS[CulturalService]
        NS[NetworkService]
        SS[SecurityService]
    end

    subgraph "Data Layer"
        SQL[SQLite Database]
        P2P[P2P Network]
        FS[File System]
    end

    HP --> DC
    SP --> SI
    MDP --> DC
    CP --> CC
    BCP --> DC

    DC --> DS
    CC --> CS
    CCX --> CSS
    SI --> DS

    DS --> SQL
    CS --> SQL
    CSS --> SQL
    NS --> P2P
    DS --> FS
```

---

## 🔄 Cultural Validation Sequence Diagram

```mermaid
sequenceDiagram
    participant User
    participant UI as "Collections Page"
    participant CS as "Collection Service"
    participant CulS as "Cultural Service"
    participant Guardian
    participant DB as "SQLite DB"
    participant P2P as "P2P Network"

    User->>UI: Create Sacred Collection
    UI->>CS: createCollection(culturalContext)

    CS->>CulS: validateCulturalContent()
    CulS->>CulS: Check sensitivity level

    alt Sensitivity Level >= 4 (Sacred)
        CulS->>Guardian: Request approval
        Guardian-->>CulS: Review content
        Guardian->>CulS: Approve/Deny

        alt Approved
            CulS->>CS: Validation approved
        else Denied
            CulS->>CS: Validation failed
            CS->>UI: Error: Cultural approval required
            UI->>User: Show cultural education
        end
    end

    CS->>DB: Store collection metadata
    CS->>CulS: Apply cultural protocols
    CulS->>DB: Store cultural restrictions

    CS->>P2P: Share with permissions
    P2P->>P2P: Encrypt sensitive content

    CS->>UI: Collection created
    UI->>User: Success with cultural guidelines
```

---

## 🗂️ Core Data Model Class Diagram

```mermaid
classDiagram
    class Document {
        +String id
        +String title
        +String content
        +DocumentFormat format
        +Number size
        +String hash
        +CulturalContext culturalContext
        +Date createdAt
        +validateAccess()
        +applyEncryption()
    }

    class Collection {
        +String id
        +String title
        +String description
        +CollectionType type
        +CulturalContext culturalContext
        +Date createdAt
        +addDocument()
        +validateCulturalContext()
    }

    class CulturalContext {
        +String region
        +String community
        +SensitivityLevel sensitivityLevel
        +String[] guardians
        +validateAccess()
        +requiresApproval()
    }

    class Peer {
        +String nodeId
        +String address
        +String publicKey
        +Number reputation
        +Date lastSeen
        +validateIdentity()
        +establishConnection()
    }

    class User {
        +String id
        +String username
        +UserProfile profile
        +Date createdAt
        +hasAccess()
        +getCulturalPermissions()
    }

    Document "1" --> "1" CulturalContext : has
    Collection "1" --> "*" Document : contains
    Collection "1" --> "1" CulturalContext : inherits
    User "1" --> "*" Collection : owns
    User "1" --> "*" Document : created
    Peer "1" --> "*" Document : shares
```

---

## 🛡️ Cultural Access Control Activity Diagram

```mermaid
flowchart TD
    Start([User requests document access]) --> CheckSensitivity{Check Cultural<br/>Sensitivity Level}

    CheckSensitivity -->|Level 1-2: Public| AllowAccess[Allow Access]
    CheckSensitivity -->|Level 3: Traditional| ShowEducation[Show Cultural<br/>Education Content]
    CheckSensitivity -->|Level 4-5: Sacred| RequireApproval[Require Guardian<br/>Approval]

    ShowEducation --> UserAccepts{User accepts<br/>educational content?}
    UserAccepts -->|Yes| AllowAccess
    UserAccepts -->|No| DenyAccess[Deny Access]

    RequireApproval --> ContactGuardian[Contact Cultural<br/>Guardian]
    ContactGuardian --> GuardianReview[Guardian Reviews<br/>Request]
    GuardianReview --> GuardianDecision{Guardian<br/>Decision}

    GuardianDecision -->|Approved| GrantPermission[Grant Temporary<br/>Permission]
    GuardianDecision -->|Denied| ProvideEducation[Provide Alternative<br/>Educational Resources]
    GuardianDecision -->|Conditional| SetConditions[Set Access<br/>Conditions]

    GrantPermission --> LogAccess[Log Access for<br/>Audit Trail]
    SetConditions --> LogAccess
    LogAccess --> AllowAccess

    AllowAccess --> End([Access Granted])
    DenyAccess --> End
    ProvideEducation --> End
```

---

## 🌐 Decentralized Deployment Diagram

```mermaid
graph TB
    subgraph "User Devices"
        D1[Desktop App 1<br/>Windows/macOS/Linux]
        D2[Desktop App 2<br/>Windows/macOS/Linux]
        D3[Desktop App 3<br/>Windows/macOS/Linux]
    end

    subgraph "Each Desktop App"
        subgraph "Frontend"
            SF[SolidJS Frontend]
            UI[User Interface]
        end

        subgraph "Backend"
            TR[Tauri Runtime]
            RS[Rust Services]
            DB[SQLite Database]
        end

        subgraph "P2P Layer"
            LP[libp2p]
            IPFS[IPFS Node]
            TOR[TOR Integration]
        end

        SF --> TR
        TR --> RS
        RS --> DB
        RS --> LP
        LP --> IPFS
        LP --> TOR
    end

    subgraph "Decentralized Network"
        P2PNet[P2P Network<br/>Content Distribution]
        DHT[Distributed Hash Table<br/>Peer Discovery]
        BC[Blockchain<br/>Verification]
    end

    subgraph "Cultural Authority Nodes"
        CA1[Cultural Authority 1]
        CA2[Cultural Authority 2]
        CA3[Cultural Authority 3]
    end

    D1 --> P2PNet
    D2 --> P2PNet
    D3 --> P2PNet

    P2PNet --> DHT
    P2PNet --> BC

    P2PNet -.->|Cultural Validation| CA1
    P2PNet -.->|Cultural Validation| CA2
    P2PNet -.->|Cultural Validation| CA3
```

---

## 👥 Use Case Diagram

```mermaid
graph TD
    subgraph "User Actions"
        U1[Browse Documents]
        U2[Search Content]
        U3[Create Collections]
        U4[Share Documents]
        U5[Access Cultural Content]
        U6[Manage Settings]
    end

    subgraph "Actors"
        User[Regular User]
        Researcher[Academic Researcher]
        Guardian[Cultural Guardian]
        Community[Community Member]
        Elder[Cultural Elder]
    end

    User --> U1
    User --> U2
    User --> U3
    User --> U6

    Researcher --> U1
    Researcher --> U2
    Researcher --> U4
    Researcher --> U5

    Guardian --> U5
    Guardian --> U4

    Community --> U1
    Community --> U3
    Community --> U5

    Elder --> U5
    Elder --> U4

    U5 -.->|Requires Approval| Guardian
    U5 -.->|Cultural Validation| Elder
    U4 -.->|Cultural Protocol| Guardian
```

---

## 🌊 Data Flow Diagram

```mermaid
flowchart LR
    subgraph "Input Sources"
        User[User Input]
        Upload[File Upload]
        P2P[P2P Network]
        Import[Bulk Import]
    end

    subgraph "Processing Layer"
        Validation[Input Validation<br/>& Sanitization]
        Cultural[Cultural Context<br/>Analysis]
        Security[Security Scanning<br/>& Malware Check]
        Meta[Metadata<br/>Extraction]
    end

    subgraph "Storage Layer"
        SQLite[SQLite Database<br/>Metadata]
        FileSystem[Local File System<br/>Documents]
        Encrypted[Encrypted Storage<br/>Sacred Content]
    end

    subgraph "Distribution Layer"
        IPFS[IPFS Network<br/>Content Addressing]
        Peers[Peer Network<br/>Sharing]
        Backup[Distributed<br/>Backups]
    end

    subgraph "Access Control"
        Permissions[Permission<br/>Management]
        CulturalAuth[Cultural<br/>Authority]
        Audit[Access<br/>Auditing]
    end

    User --> Validation
    Upload --> Security
    P2P --> Cultural
    Import --> Meta

    Validation --> SQLite
    Cultural --> Permissions
    Security --> FileSystem
    Meta --> SQLite

    FileSystem --> IPFS
    SQLite --> Peers
    Encrypted --> Backup

    Permissions --> CulturalAuth
    CulturalAuth --> Audit
```

---

## 🔄 Application State Machine

```mermaid
stateDiagram-v2
    [*] --> AppInitializing

    AppInitializing --> LoadingConfiguration
    LoadingConfiguration --> InitializingDatabase
    InitializingDatabase --> StartingP2PNetwork
    StartingP2PNetwork --> LoadingCulturalFramework
    LoadingCulturalFramework --> AppReady

    AppReady --> HomePage

    HomePage --> Browsing : User navigates
    HomePage --> Searching : User searches
    HomePage --> Managing : User manages content
    HomePage --> Networking : User accesses network
    HomePage --> Configuring : User opens settings

    state Browsing {
        [*] --> BrowsingCategories
        BrowsingCategories --> ViewingDocuments
        ViewingDocuments --> CulturalValidation
        CulturalValidation --> DocumentAccess : Approved
        CulturalValidation --> EducationalContent : Needs education
        CulturalValidation --> AccessDenied : Restricted
        DocumentAccess --> [*]
        EducationalContent --> DocumentAccess : User educated
        AccessDenied --> [*]
    }

    state Searching {
        [*] --> EnteringQuery
        EnteringQuery --> ProcessingSearch
        ProcessingSearch --> FilteringResults
        FilteringResults --> ApplyingCulturalFilters
        ApplyingCulturalFilters --> DisplayingResults
        DisplayingResults --> [*]
    }

    state Managing {
        [*] --> ViewingPersonalLibrary
        ViewingPersonalLibrary --> CreatingCollection
        ViewingPersonalLibrary --> EditingDocument
        ViewingPersonalLibrary --> SharingContent

        CreatingCollection --> CulturalReview
        CulturalReview --> GuardianApproval : Sacred content
        CulturalReview --> CollectionCreated : Approved
        GuardianApproval --> CollectionCreated : Approved
        GuardianApproval --> CreationDenied : Denied

        EditingDocument --> [*]
        SharingContent --> CulturalPermissionCheck
        CulturalPermissionCheck --> SharedSuccessfully : Allowed
        CulturalPermissionCheck --> SharingDenied : Restricted

        CollectionCreated --> [*]
        CreationDenied --> [*]
        SharedSuccessfully --> [*]
        SharingDenied --> [*]
    }

    state Networking {
        [*] --> ConnectingToPeers
        ConnectingToPeers --> DiscoveringContent
        DiscoveringContent --> SynchronizingData
        SynchronizingData --> NetworkActive
        NetworkActive --> [*]
    }

    state Configuring {
        [*] --> LoadingSettings
        LoadingSettings --> ModifyingSettings
        ModifyingSettings --> ValidatingChanges
        ValidatingChanges --> ApplyingSettings
        ApplyingSettings --> [*]
    }

    Browsing --> HomePage : Return home
    Searching --> HomePage : Return home
    Managing --> HomePage : Return home
    Networking --> HomePage : Return home
    Configuring --> HomePage : Return home

    AppReady --> AppShuttingDown : User exits
    AppShuttingDown --> SavingState
    SavingState --> DisconnectingP2P
    DisconnectingP2P --> CleaningUp
    CleaningUp --> [*]
```

---

## 🌐 Complete System Integration Architecture

```mermaid
graph TB
    subgraph "AlLibrary Core System"
        subgraph "Desktop Application"
            UI[SolidJS Frontend]
            BL[Business Logic]
            API[Tauri API Layer]
            DB[SQLite Database]
        end

        subgraph "P2P Network Layer"
            LibP2P[libp2p Protocol]
            IPFS[IPFS Content Storage]
            DHT[Distributed Hash Table]
        end

        subgraph "Security & Privacy"
            Encryption[End-to-End Encryption]
            TOR[TOR Integration]
            VPN[VPN Support]
            LocalAuth[Local Authentication]
        end
    end

    subgraph "Cultural Authority Network"
        subgraph "Indigenous Communities"
            IC1[Community 1<br/>Traditional Knowledge]
            IC2[Community 2<br/>Sacred Content]
            IC3[Community 3<br/>Cultural Protocols]
        end

        subgraph "Academic Institutions"
            AI1[University 1<br/>Research Repository]
            AI2[University 2<br/>Cultural Studies]
            AI3[Library System<br/>Academic Content]
        end

        subgraph "Cultural Organizations"
            CO1[Museum Network<br/>Cultural Heritage]
            CO2[UNESCO<br/>World Heritage]
            CO3[National Archives<br/>Historical Records]
        end
    end

    subgraph "External Systems"
        subgraph "Verification Services"
            VS1[Digital Signature<br/>Verification]
            VS2[Content Authenticity<br/>Blockchain]
            VS3[Reputation System<br/>Community Trust]
        end

        subgraph "Anti-Censorship Network"
            ACN1[Mirror Networks<br/>Content Backup]
            ACN2[Distributed CDN<br/>Access Points]
            ACN3[Emergency Networks<br/>Crisis Access]
        end
    end

    %% Core System Connections
    UI --> BL
    BL --> API
    API --> DB
    API --> LibP2P
    LibP2P --> IPFS
    LibP2P --> DHT

    %% Security Integration
    BL --> Encryption
    LibP2P --> TOR
    API --> LocalAuth
    TOR --> VPN

    %% Cultural Authority Integration
    BL -.->|Cultural Validation| IC1
    BL -.->|Sacred Content Approval| IC2
    BL -.->|Protocol Compliance| IC3
    BL -.->|Academic Verification| AI1
    BL -.->|Research Collaboration| AI2
    BL -.->|Library Integration| AI3
    BL -.->|Heritage Preservation| CO1
    BL -.->|Standards Compliance| CO2
    BL -.->|Historical Verification| CO3

    %% External Systems Integration
    IPFS --> VS1
    DHT --> VS2
    LibP2P --> VS3
    TOR --> ACN1
    IPFS --> ACN2
    LibP2P --> ACN3
```

---

_System Architecture Excellence: These diagrams represent AlLibrary's commitment to decentralized, culturally-respectful, anti-censorship knowledge sharing through technical excellence and community governance._
