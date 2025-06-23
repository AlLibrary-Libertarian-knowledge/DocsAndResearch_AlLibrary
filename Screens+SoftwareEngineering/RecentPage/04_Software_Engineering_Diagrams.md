# RecentPage - Software Engineering Diagrams

## 🏗️ Component Architecture

### RecentPage Component Structure

```mermaid
graph TB
    subgraph "RecentPage Components"
        RP[RecentPage]
        RH[RecentHeader]
        ATL[ActivityTimeline]
        AF[ActivityFilter]
        AS[ActivitySearch]
        AP[ActivityPagination]
    end

    subgraph "Activity Components"
        AI[ActivityItem]
        AIC[ActivityIcon]
        AD[ActivityDetails]
        AT[ActivityTimestamp]
        CAI[CulturalActivityIndicator]
    end

    subgraph "Timeline Features"
        DG[DateGrouping]
        TF[TimeFilter]
        VT[VirtualTimeline]
        LM[LazyLoading]
    end

    subgraph "Cultural Integration"
        CCR[Cultural Context Renderer]
        CAW[Cultural Activity Workflow]
        SLI[Sensitivity Level Indicator]
        ACL[Activity Cultural Logger]
    end

    RP --> RH
    RP --> ATL
    RP --> AF
    RP --> AS
    RP --> AP

    ATL --> AI
    AI --> AIC
    AI --> AD
    AI --> AT
    AI --> CAI

    ATL --> DG
    AF --> TF
    ATL --> VT
    VT --> LM

    CAI --> CCR
    AI --> CAW
    AI --> SLI
    ATL --> ACL
```

---

## 🔄 Activity Tracking Flow

### Cultural-Aware Activity Logging

```mermaid
sequenceDiagram
    participant User
    participant App as "Application"
    participant ATS as "Activity Tracking Service"
    participant CulS as "Cultural Service"
    participant RP as "RecentPage"
    participant DB as "Database"
    participant Privacy as "Privacy Service"

    User->>App: Perform action (view document)
    App->>ATS: logActivity(userId, action, context)
    ATS->>CulS: analyzeCulturalContext(action, context)

    CulS->>CulS: Determine cultural significance

    alt Culturally Sensitive Action
        CulS->>CulS: Apply cultural logging protocols
        CulS-->>ATS: Cultural context added
        ATS->>Privacy: applyCulturalPrivacyRules(activity)
        Privacy-->>ATS: Privacy rules applied
    else Standard Action
        CulS-->>ATS: Standard logging approved
        ATS->>Privacy: applyStandardPrivacyRules(activity)
        Privacy-->>ATS: Privacy rules applied
    end

    ATS->>DB: storeActivity(activityData)
    DB-->>ATS: Activity stored

    ATS->>RP: notifyNewActivity(activityData)
    RP->>RP: Update activity timeline

    User->>RP: Load recent page
    RP->>ATS: getRecentActivities(userId)
    ATS->>CulS: filterCulturalActivities(activities, userId)
    CulS->>CulS: Apply cultural access rules
    CulS-->>ATS: Return filtered activities
    ATS-->>RP: Display filtered timeline
    RP->>User: Show recent activities with cultural context
```

---

## 📊 Activity Data Model

### Comprehensive Activity Schema

```mermaid
classDiagram
    class Activity {
        +String id
        +String userId
        +ActivityType type
        +String description
        +String targetId
        +String targetType
        +Date timestamp
        +CulturalContext culturalContext
        +PrivacyLevel privacyLevel
        +String metadata
        +Boolean isVisible
        +formatForDisplay()
        +checkVisibility()
    }

    class CulturalActivityContext {
        +String activityId
        +SensitivityLevel sensitivityLevel
        +Boolean requiresPrivacyProtection
        +String culturalSignificance
        +String[] culturalTags
        +Boolean loggedWithConsent
        +Date culturalReviewDate
        +applyCulturalPrivacy()
        +validateCulturalLogging()
    }

    class ActivityTimeline {
        +String userId
        +Date startDate
        +Date endDate
        +Activity[] activities
        +Number totalCount
        +Boolean hasMore
        +CulturalFilter culturalFilter
        +PrivacyFilter privacyFilter
        +loadMoreActivities()
        +applyCulturalFiltering()
    }

    class PrivacySettings {
        +String userId
        +Boolean trackDocumentViews
        +Boolean trackSearches
        +Boolean trackCulturalActivities
        +Number retentionDays
        +Boolean shareWithPeers
        +Boolean anonymizeData
        +CulturalPrivacyLevel culturalPrivacy
        +validatePrivacyCompliance()
    }

    Activity "1" --> "0..1" CulturalActivityContext
    ActivityTimeline "1" --> "*" Activity
    Activity "1" --> "1" PrivacySettings : respects
```

---

## 🛡️ Cultural Privacy Protection

### Activity Privacy Workflow

```mermaid
flowchart TD
    Start([Activity Occurs]) --> AnalyzeActivity[Analyze Activity Type and Context]

    AnalyzeActivity --> CheckCulturalSignificance{Cultural Significance?}

    CheckCulturalSignificance -->|None| StandardLogging[Apply Standard Logging]
    CheckCulturalSignificance -->|Low| MinimalCulturalLogging[Apply Minimal Cultural Logging]
    CheckCulturalSignificance -->|Medium| CulturalPrivacyProtection[Apply Cultural Privacy Protection]
    CheckCulturalSignificance -->|High| MaximalPrivacyProtection[Apply Maximal Privacy Protection]

    StandardLogging --> CheckUserPrivacy[Check User Privacy Settings]
    MinimalCulturalLogging --> CheckUserPrivacy
    CulturalPrivacyProtection --> CheckCulturalConsent[Check Cultural Consent]
    MaximalPrivacyProtection --> RequireExplicitConsent[Require Explicit Consent]

    CheckUserPrivacy --> UserAllows{User Privacy Allows?}
    UserAllows -->|Yes| LogActivity[Log Activity]
    UserAllows -->|No| SkipLogging[Skip Activity Logging]

    CheckCulturalConsent --> CulturalConsent{Cultural Consent Given?}
    CulturalConsent -->|Yes| LogWithCulturalContext[Log with Cultural Context]
    CulturalConsent -->|No| LogWithoutCulturalDetails[Log without Cultural Details]

    RequireExplicitConsent --> ExplicitConsent{Explicit Consent Given?}
    ExplicitConsent -->|Yes| LogWithMaximalContext[Log with Maximal Cultural Context]
    ExplicitConsent -->|No| SkipLogging

    LogActivity --> StoreInDatabase[Store in Activity Database]
    LogWithCulturalContext --> StoreInDatabase
    LogWithoutCulturalDetails --> StoreInDatabase
    LogWithMaximalContext --> StoreInDatabase

    StoreInDatabase --> UpdateTimeline[Update User Timeline]
    SkipLogging --> End([Activity Processing Complete])
    UpdateTimeline --> End
```

---

## ⚡ Timeline Performance

### Efficient Activity Loading

```mermaid
graph TB
    subgraph "Loading Strategy"
        VT[Virtual Timeline]
        IL[Incremental Loading]
        LL[Lazy Loading]
        PL[Progressive Loading]
    end

    subgraph "Caching Layers"
        MC[Memory Cache]
        SC[Session Cache]
        PC[Persistent Cache]
        CC[Cultural Cache]
    end

    subgraph "Data Processing"
        AG[Activity Grouping]
        DF[Data Filtering]
        DM[Data Minification]
        CF[Cultural Filtering]
    end

    subgraph "Timeline Optimization"
        TC[Timeline Compression]
        BU[Batch Updates]
        RU[Real-time Updates]
        IO[Index Optimization]
    end

    VT --> MC
    IL --> SC
    LL --> PC
    PL --> CC

    MC --> AG
    SC --> DF
    PC --> DM
    CC --> CF

    AG --> TC
    DF --> BU
    DM --> RU
    CF --> IO
```

---

## 🔍 Activity Search and Filtering

### Intelligent Activity Discovery

```mermaid
graph LR
    subgraph "Search Capabilities"
        TS[Text Search]
        DS[Date Search]
        TS_TYPE[Type Search]
        CS[Cultural Search]
    end

    subgraph "Filter Options"
        TF[Type Filter]
        DF[Date Filter]
        CF[Cultural Filter]
        PF[Privacy Filter]
    end

    subgraph "Result Processing"
        RP[Result Processing]
        CAF[Cultural Access Filtering]
        PV[Privacy Validation]
        RR[Result Ranking]
    end

    subgraph "Display"
        TL[Timeline Display]
        LD[List Display]
        CD[Card Display]
        DD[Detail Display]
    end

    TS --> TF
    DS --> DF
    TS_TYPE --> CF
    CS --> PF

    TF --> RP
    DF --> CAF
    CF --> PV
    PF --> RR

    RP --> TL
    CAF --> LD
    PV --> CD
    RR --> DD
```

---

## 📱 Activity Interaction

### User Activity Management

```mermaid
sequenceDiagram
    participant User
    participant RP as "RecentPage"
    participant AMS as "Activity Management Service"
    participant CulS as "Cultural Service"
    participant Privacy as "Privacy Service"
    participant DB as "Database"

    User->>RP: Click on activity item
    RP->>AMS: getActivityDetails(activityId)
    AMS->>CulS: validateActivityAccess(activityId, userId)

    CulS->>CulS: Check cultural access permissions

    alt Access Allowed
        CulS-->>AMS: Access granted
        AMS->>DB: getFullActivityDetails(activityId)
        DB-->>AMS: Return activity details
        AMS-->>RP: Display activity details
        RP->>User: Show detailed activity view
    else Cultural Restrictions
        CulS-->>AMS: Access restricted
        AMS-->>RP: Show cultural restriction explanation
        RP->>User: Display cultural education content
    end

    User->>RP: Delete activity
    RP->>Privacy: validateActivityDeletion(activityId, userId)
    Privacy->>Privacy: Check deletion permissions

    alt Deletion Allowed
        Privacy-->>RP: Deletion permitted
        RP->>AMS: deleteActivity(activityId)
        AMS->>DB: removeActivity(activityId)
        DB-->>AMS: Activity removed
        AMS-->>RP: Activity deleted successfully
        RP->>User: Update timeline display
    else Deletion Restricted
        Privacy-->>RP: Deletion not permitted
        RP->>User: Show deletion restriction explanation
    end
```

---

_RecentPage Excellence: Comprehensive activity tracking with cultural privacy protection, intelligent filtering, and user-controlled activity management._
