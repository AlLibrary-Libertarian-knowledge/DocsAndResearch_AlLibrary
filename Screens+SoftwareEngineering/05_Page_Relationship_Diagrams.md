# AlLibrary Page Relationship & Navigation Diagrams

## 🗺️ Overview

This document illustrates how all AlLibrary pages interconnect, showing navigation flows, data sharing, and cultural integration across the entire application ecosystem.

---

## 🌐 Complete AlLibrary Page Relationship Diagram

```mermaid
graph TB
    subgraph "Core Navigation Hub"
        HP[HomePage<br/>📱 Main Dashboard]
    end

    subgraph "Content Discovery"
        SP[SearchPage<br/>🔍 Global Search]
        SCP[SearchNetworkPage<br/>🌐 P2P Search]
        BCP[BrowseCategoriesPage<br/>📂 Category Navigation]
        TP[TrendingPage<br/>📈 Popular Content]
        NAP[NewArrivalsPage<br/>🆕 Fresh Content]
    end

    subgraph "Content Management"
        MDP[MyDocumentsPage<br/>📄 Personal Library]
        CP[CollectionsPage<br/>📚 Organized Groups]
        FP[FavoritesPage<br/>⭐ Bookmarked Items]
        RP[RecentPage<br/>🕒 Recent Activity]
    end

    subgraph "Content Detail"
        DDP[DocumentDetailPage<br/>📖 Document Viewer]
    end

    subgraph "Cultural & Community"
        CCP[CulturalContextsPage<br/>🌍 Cultural Framework]
        PNP[PeerNetworkPage<br/>🤝 Community Network]
    end

    subgraph "System & Info"
        SETP[SettingsPage<br/>⚙️ Configuration]
        AP[AboutPage<br/>ℹ️ Project Information]
    end

    %% Primary Navigation from HomePage
    HP --> SP
    HP --> MDP
    HP --> CP
    HP --> BCP
    HP --> PNP
    HP --> SETP

    %% Search & Discovery Flow
    SP --> DDP
    SCP --> DDP
    BCP --> SP
    BCP --> DDP
    TP --> DDP
    NAP --> DDP

    %% Content Management Flow
    MDP --> DDP
    MDP --> CP
    CP --> DDP
    FP --> DDP
    RP --> DDP
    RP --> MDP

    %% Cultural Integration
    CCP --> BCP
    CCP --> DDP
    CCP --> CP

    %% Network & Community
    PNP --> SCP
    PNP --> CCP
    PNP --> MDP

    %% Settings Integration
    SETP --> HP
    SETP --> CCP
    SETP --> PNP

    %% Information & About
    AP --> CCP
    AP --> SETP

    %% Cross-Page Relationships
    SP -.->|"Search in Collections"| CP
    MDP -.->|"Add to Collections"| CP
    DDP -.->|"Add to Favorites"| FP
    DDP -.->|"Share via Network"| PNP
    BCP -.->|"Cultural Context"| CCP

    %% Cultural Validation Flows
    DDP -.->|"Cultural Validation"| CCP
    CP -.->|"Cultural Approval"| CCP
    MDP -.->|"Cultural Assignment"| CCP
```

---

## 🏗️ Complete Technical Architecture Flow

```mermaid
graph TB
    subgraph "Frontend Layer - SolidJS"
        subgraph "Pages"
            HP[HomePage]
            SP[SearchPage]
            MDP[MyDocumentsPage]
            CP[CollectionsPage]
            BCP[BrowseCategoriesPage]
            DDP[DocumentDetailPage]
            CCP[CulturalContextsPage]
            PNP[PeerNetworkPage]
            SETP[SettingsPage]
            AP[AboutPage]
        end

        subgraph "Shared Components"
            FC[Foundation Components]
            DC[Domain Components]
            CC[Composite Components]
        end

        subgraph "State Management"
            DS[Document Store]
            CS[Collection Store]
            US[User Store]
            NS[Network Store]
            CuS[Cultural Store]
        end
    end

    subgraph "Service Layer - TypeScript"
        subgraph "Core Services"
            DocS[Document Service]
            ColS[Collection Service]
            CulS[Cultural Service]
            NetS[Network Service]
            SecS[Security Service]
        end

        subgraph "Specialized Services"
            SearchS[Search Service]
            SyncS[Sync Service]
            AnalS[Analytics Service]
            NotS[Notification Service]
        end
    end

    subgraph "Backend Layer - Rust + Tauri"
        subgraph "API Layer"
            DocAPI[Document API]
            ColAPI[Collection API]
            CulAPI[Cultural API]
            NetAPI[Network API]
            SecAPI[Security API]
        end

        subgraph "Business Logic"
            DocBL[Document Business Logic]
            ColBL[Collection Business Logic]
            CulBL[Cultural Business Logic]
            NetBL[Network Business Logic]
            SecBL[Security Business Logic]
        end
    end

    subgraph "Data Layer"
        subgraph "Local Storage"
            SQLite[SQLite Database]
            FS[File System]
            Cache[Local Cache]
        end

        subgraph "P2P Network"
            LibP2P[libp2p]
            IPFS[IPFS]
            DHT[Distributed Hash Table]
        end

        subgraph "External Integration"
            TOR[TOR Network]
            CulAuth[Cultural Authorities]
            VerSys[Verification Systems]
        end
    end

    %% Frontend to Service connections
    HP --> DocS
    SP --> SearchS
    MDP --> DocS
    CP --> ColS
    BCP --> SearchS
    DDP --> DocS
    CCP --> CulS
    PNP --> NetS
    SETP --> SecS
    AP --> DocS

    %% Service to Backend connections
    DocS --> DocAPI
    ColS --> ColAPI
    CulS --> CulAPI
    NetS --> NetAPI
    SecS --> SecAPI
    SearchS --> DocAPI
    SyncS --> NetAPI

    %% Backend to Data connections
    DocAPI --> DocBL
    ColAPI --> ColBL
    CulAPI --> CulBL
    NetAPI --> NetBL
    SecAPI --> SecBL

    DocBL --> SQLite
    ColBL --> SQLite
    CulBL --> SQLite
    NetBL --> LibP2P
    SecBL --> FS

    LibP2P --> IPFS
    LibP2P --> DHT
    NetBL --> TOR
    CulBL --> CulAuth
    SecBL --> VerSys
```

---

## 🌊 Complete Data Flow Architecture

```mermaid
flowchart TD
    subgraph "Input Sources"
        User[User Actions]
        Upload[Document Upload]
        P2P[P2P Network Sync]
        Import[Bulk Import]
        Cultural[Cultural Authority Input]
    end

    subgraph "Input Processing"
        Validation[Input Validation<br/>& Sanitization]
        Security[Security Scanning<br/>Malware Detection]
        Cultural_Val[Cultural Validation<br/>Sensitivity Analysis]
        Metadata[Metadata Extraction<br/>& Enhancement]
    end

    subgraph "Business Logic Processing"
        DocProc[Document Processing]
        ColProc[Collection Processing]
        CulProc[Cultural Processing]
        SearchProc[Search Processing]
        NetworkProc[Network Processing]
    end

    subgraph "Data Storage"
        SQLite_Meta[SQLite Metadata<br/>Collections, Users, Cultural]
        FileSystem[File System<br/>Document Storage]
        Encrypted[Encrypted Storage<br/>Sacred Content]
        Cache_Layer[Cache Layer<br/>Performance Optimization]
    end

    subgraph "P2P Distribution"
        IPFS_Store[IPFS Content<br/>Addressing & Storage]
        Peer_Sync[Peer Synchronization<br/>Distributed Updates]
        DHT_Store[DHT Storage<br/>Peer Discovery]
    end

    subgraph "Output Processing"
        Rendering[Content Rendering<br/>& Presentation]
        Cultural_Filter[Cultural Filtering<br/>Access Control]
        Export[Export Processing<br/>Multiple Formats]
        Notification[Notification<br/>& Updates]
    end

    subgraph "User Interface"
        Pages[UI Pages<br/>User Interaction]
        Components[Reusable Components<br/>Consistent Experience]
        State[Application State<br/>Reactive Updates]
    end

    %% Input flow
    User --> Validation
    Upload --> Security
    P2P --> Cultural_Val
    Import --> Metadata
    Cultural --> Cultural_Val

    %% Processing flow
    Validation --> DocProc
    Security --> DocProc
    Cultural_Val --> CulProc
    Metadata --> SearchProc

    DocProc --> ColProc
    CulProc --> NetworkProc
    SearchProc --> DocProc

    %% Storage flow
    DocProc --> SQLite_Meta
    DocProc --> FileSystem
    CulProc --> Encrypted
    SearchProc --> Cache_Layer

    %% Distribution flow
    FileSystem --> IPFS_Store
    SQLite_Meta --> Peer_Sync
    NetworkProc --> DHT_Store

    %% Output flow
    SQLite_Meta --> Rendering
    FileSystem --> Cultural_Filter
    IPFS_Store --> Export
    Peer_Sync --> Notification

    %% UI flow
    Rendering --> Pages
    Cultural_Filter --> Components
    Export --> State
    Notification --> State

    %% Feedback loops
    Pages -.->|User Actions| User
    State -.->|State Updates| NetworkProc
    Components -.->|Cultural Requests| CulProc
```

---

## 🔄 Navigation Flow Patterns

### 📱 **Primary Navigation Flows**

```mermaid
flowchart LR
    Start([User Opens AlLibrary]) --> HomePage

    HomePage --> Discovery{Content Discovery}
    HomePage --> Management{Content Management}
    HomePage --> Network{Network & Community}
    HomePage --> Config{Configuration}

    Discovery --> SearchPage
    Discovery --> BrowseCategoriesPage
    Discovery --> TrendingPage
    Discovery --> NewArrivalsPage

    Management --> MyDocumentsPage
    Management --> CollectionsPage
    Management --> FavoritesPage
    Management --> RecentPage

    Network --> PeerNetworkPage
    Network --> SearchNetworkPage
    Network --> CulturalContextsPage

    Config --> SettingsPage
    Config --> AboutPage

    SearchPage --> DocumentDetailPage
    BrowseCategoriesPage --> DocumentDetailPage
    MyDocumentsPage --> DocumentDetailPage
    CollectionsPage --> DocumentDetailPage
```

### 🌍 **Cultural Integration Flows**

```mermaid
flowchart TD
    CulturalTrigger([Cultural Content Accessed]) --> SensitivityCheck{Check Sensitivity Level}

    SensitivityCheck -->|Level 1-2| DirectAccess[Direct Access Granted]
    SensitivityCheck -->|Level 3| EducationalFlow[Educational Content Flow]
    SensitivityCheck -->|Level 4-5| GuardianFlow[Guardian Approval Flow]

    EducationalFlow --> CulturalContextsPage
    CulturalContextsPage --> UserEducated{User Completes Education}
    UserEducated -->|Yes| DirectAccess
    UserEducated -->|No| AccessDenied[Access Respectfully Denied]

    GuardianFlow --> CulturalContextsPage
    CulturalContextsPage --> GuardianContact[Contact Cultural Guardian]
    GuardianContact --> GuardianDecision{Guardian Decision}
    GuardianDecision -->|Approved| DirectAccess
    GuardianDecision -->|Denied| AlternativeEducation[Alternative Educational Content]
    GuardianDecision -->|Conditional| ConditionalAccess[Conditional Access Granted]

    DirectAccess --> ContentAccess[Content Accessed]
    ConditionalAccess --> ContentAccess
    AlternativeEducation --> CulturalContextsPage
    AccessDenied --> CulturalContextsPage
```

### 🔍 **Search & Discovery Integration**

```mermaid
flowchart LR
    SearchInput([User Search Query]) --> SearchPage

    SearchPage --> LocalSearch[Local Content Search]
    SearchPage --> NetworkSearch[P2P Network Search]
    SearchPage --> CategorySearch[Category-based Search]

    LocalSearch --> ResultsProcessing[Results Processing]
    NetworkSearch --> PeerNetworkPage
    CategorySearch --> BrowseCategoriesPage

    PeerNetworkPage --> NetworkResults[Network Search Results]
    BrowseCategoriesPage --> CategoryResults[Category Browse Results]

    ResultsProcessing --> CulturalFiltering[Cultural Sensitivity Filtering]
    NetworkResults --> CulturalFiltering
    CategoryResults --> CulturalFiltering

    CulturalFiltering --> SearchResults[Filtered Search Results]
    SearchResults --> DocumentDetailPage

    DocumentDetailPage --> RelatedContent{Show Related Content}
    RelatedContent --> CollectionsPage
    RelatedContent --> BrowseCategoriesPage
    RelatedContent --> SimilarDocuments[Similar Documents]
```

---

## 📊 **Page Interdependency Matrix**

| Page                 | HomePage | SearchPage | MyDocuments | Collections | BrowseCategories | DocumentDetail | Cultural | PeerNetwork | Settings | About  |
| -------------------- | -------- | ---------- | ----------- | ----------- | ---------------- | -------------- | -------- | ----------- | -------- | ------ |
| **HomePage**         | -        | High       | High        | High        | Medium           | Low            | Medium   | Medium      | High     | Low    |
| **SearchPage**       | Medium   | -          | Medium      | High        | High             | High           | High     | Medium      | Low      | Low    |
| **MyDocuments**      | High     | Medium     | -           | High        | Medium           | High           | High     | Medium      | Medium   | Low    |
| **Collections**      | High     | High       | High        | -           | Medium           | High           | High     | Medium      | Medium   | Low    |
| **BrowseCategories** | Medium   | High       | Medium      | Medium      | -                | High           | High     | Low         | Low      | Low    |
| **DocumentDetail**   | Low      | High       | High        | High        | High             | -              | High     | Medium      | Low      | Low    |
| **Cultural**         | Medium   | High       | High        | High        | High             | High           | -        | High        | High     | Medium |
| **PeerNetwork**      | Medium   | Medium     | Medium      | Medium      | Low              | Medium         | High     | -           | High     | Low    |
| **Settings**         | High     | Low        | Medium      | Medium      | Low              | Low            | High     | High        | -        | Medium |
| **About**            | Low      | Low        | Low         | Low         | Low              | Low            | Medium   | Low         | Medium   | -      |

**Legend:**

- **High**: Direct navigation and frequent data sharing
- **Medium**: Indirect relationship with some data sharing
- **Low**: Minimal or rare interaction

---

_Navigation Excellence: These diagrams ensure seamless user experience while maintaining cultural sensitivity and anti-censorship principles throughout the AlLibrary ecosystem._
