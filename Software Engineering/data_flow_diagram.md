# AlLibrary Data Flow Diagram

## Overview

This diagram illustrates how data flows through the AlLibrary system, from document import to P2P sharing and community interaction.

## Complete System Data Flow

```mermaid
flowchart TD
    %% Input Sources
    UserFiles[User Document Files]
    NetworkContent[P2P Network Content]
    CommunityInput[Community Guidelines]
    CulturalRules[Cultural Protection Rules]

    %% Data Processing Layers
    subgraph "Data Input Layer"
        FileUpload[File Upload Handler]
        NetworkReceiver[Network Content Receiver]
        MetadataExtractor[Metadata Extraction]
        FormatValidator[Format Validation]
    end

    subgraph "Data Processing Layer"
        SecurityScanner[Security Scanner]
        CulturalFilter[Cultural Sensitivity Filter]
        ContentAnalyzer[Content Analyzer]
        DuplicateDetector[Duplicate Detection]
    end

    subgraph "Data Storage Layer"
        LocalDB[(SQLite Database)]
        LocalFiles[Local File Storage]
        CacheStorage[Cache Storage]
        IndexStorage[Search Index]
    end

    subgraph "Data Distribution Layer"
        IPFSStorage[IPFS Distributed Storage]
        DHTPubSub[DHT Pub/Sub System]
        PeerNetwork[Peer Network Distribution]
        ContentAddressing[Content Addressing System]
    end

    subgraph "Data Access Layer"
        SearchEngine[Search Engine]
        ContentRetrieval[Content Retrieval]
        PermissionManager[Permission Manager]
        CulturalAccessControl[Cultural Access Control]
    end

    %% User Interface
    UserInterface[User Interface]

    %% Data Flow Connections
    UserFiles --> FileUpload
    NetworkContent --> NetworkReceiver
    CommunityInput --> CulturalFilter
    CulturalRules --> CulturalFilter

    FileUpload --> MetadataExtractor
    NetworkReceiver --> MetadataExtractor
    MetadataExtractor --> FormatValidator
    FormatValidator --> SecurityScanner

    SecurityScanner --> CulturalFilter
    CulturalFilter --> ContentAnalyzer
    ContentAnalyzer --> DuplicateDetector

    DuplicateDetector --> LocalDB
    DuplicateDetector --> LocalFiles
    ContentAnalyzer --> IndexStorage
    SecurityScanner --> CacheStorage

    LocalDB --> IPFSStorage
    LocalFiles --> IPFSStorage
    IPFSStorage --> DHTPubSub
    DHTPubSub --> PeerNetwork
    PeerNetwork --> ContentAddressing

    LocalDB --> SearchEngine
    IndexStorage --> SearchEngine
    IPFSStorage --> ContentRetrieval
    ContentRetrieval --> PermissionManager
    PermissionManager --> CulturalAccessControl

    SearchEngine --> UserInterface
    CulturalAccessControl --> UserInterface
    ContentRetrieval --> UserInterface

    %% Feedback Loops
    UserInterface -.-> CommunityInput
    CulturalAccessControl -.-> CulturalRules

    %% Styling
    classDef input fill:#e3f2fd
    classDef processing fill:#f3e5f5
    classDef storage fill:#e8f5e8
    classDef distribution fill:#fff3e0
    classDef access fill:#fce4ec
    classDef ui fill:#f1f8e9

    class UserFiles,NetworkContent,CommunityInput,CulturalRules input
    class FileUpload,NetworkReceiver,MetadataExtractor,FormatValidator,SecurityScanner,CulturalFilter,ContentAnalyzer,DuplicateDetector processing
    class LocalDB,LocalFiles,CacheStorage,IndexStorage storage
    class IPFSStorage,DHTPubSub,PeerNetwork,ContentAddressing distribution
    class SearchEngine,ContentRetrieval,PermissionManager,CulturalAccessControl access
    class UserInterface ui
```

## Document Import Data Flow

```mermaid
sequenceDiagram
    participant User
    participant UI as User Interface
    participant Handler as File Handler
    participant Validator as Format Validator
    participant Scanner as Security Scanner
    participant Filter as Cultural Filter
    participant DB as SQLite Database
    participant FS as File System
    participant IPFS as IPFS Network

    User->>UI: Select documents to import
    UI->>Handler: Process file selection
    Handler->>Validator: Validate file formats
    Validator->>Scanner: Security scan files
    Scanner->>Filter: Cultural sensitivity check
    Filter->>DB: Store metadata
    Filter->>FS: Store document files
    DB->>IPFS: Publish content hash
    IPFS-->>UI: Confirm successful import
    UI-->>User: Display import confirmation
```

## P2P Content Discovery Data Flow

```mermaid
sequenceDiagram
    participant User
    participant UI as User Interface
    participant Search as Search Engine
    participant DHT as Distributed Hash Table
    participant Peers as P2P Network
    participant Verify as Content Verifier
    participant Cultural as Cultural Filter
    participant Local as Local Storage

    User->>UI: Search for content
    UI->>Search: Execute search query
    Search->>DHT: Query distributed index
    DHT->>Peers: Request content from peers
    Peers-->>DHT: Return content references
    DHT-->>Search: Provide search results
    Search->>Verify: Verify content integrity
    Verify->>Cultural: Apply cultural filters
    Cultural-->>UI: Return filtered results
    UI-->>User: Display available content
    User->>UI: Select content to download
    UI->>Local: Download and store locally
```

## Content Sharing Data Flow

```mermaid
sequenceDiagram
    participant User
    participant UI as User Interface
    participant Perms as Permission Manager
    participant Cultural as Cultural Validator
    participant Local as Local Storage
    participant IPFS as IPFS Network
    participant DHT as DHT System
    participant Peers as P2P Network

    User->>UI: Select content to share
    UI->>Perms: Set sharing permissions
    Perms->>Cultural: Validate cultural sensitivity
    Cultural->>Local: Access local content
    Local->>IPFS: Upload to distributed storage
    IPFS->>DHT: Publish content references
    DHT->>Peers: Announce content availability
    Peers-->>UI: Confirm sharing success
    UI-->>User: Display sharing status
```

## Data Types and Structures

### **Document Metadata**

```yaml
DocumentMetadata:
  id: UUID
  title: String
  author: String
  file_type: Enum[PDF, EPUB]
  file_size: Integer
  content_hash: String
  cultural_sensitivity: Enum[Public, Restricted, Sacred]
  permissions: Array[Permission]
  created_at: DateTime
  modified_at: DateTime
  tags: Array[String]
  collections: Array[UUID]
```

### **Cultural Protection Data**

```yaml
CulturalProtection:
  content_id: UUID
  sensitivity_level: Enum[Low, Medium, High, Sacred]
  community_origin: String
  access_restrictions: Object
    geographic: Array[String]
    temporal: Object
    ceremonial: Boolean
  approval_required: Boolean
  elder_verification: Boolean
  attribution_required: Boolean
```

### **P2P Network Data**

```yaml
NetworkMessage:
  message_type: Enum[Query, Response, Announcement]
  peer_id: String
  content_hash: String
  metadata: Object
  signature: String
  timestamp: DateTime
  ttl: Integer
```

### **Search Index Data**

```yaml
SearchIndex:
  content_id: UUID
  content_text: String (Full-text)
  metadata_index: Object
    title: String
    author: String
    tags: Array[String]
  cultural_index: Object
    sensitivity: String
    community: String
    permissions: Array[String]
  vector_embeddings: Array[Float] (Future semantic search)
```

## Data Security and Privacy

### **Encryption Layers**

1. **Transport Encryption**: All network communication encrypted with TLS
2. **Content Encryption**: Sensitive content encrypted with user-controlled keys
3. **Metadata Protection**: Personal metadata encrypted locally
4. **Cultural Protection**: Sacred content protected with community keys

### **Data Sovereignty**

1. **User Control**: Users control their data sharing and retention
2. **Community Control**: Cultural communities control sensitive content
3. **Decentralized Storage**: No central data collection points
4. **Right to Deletion**: Users can remove content from network

### **Privacy Protection**

1. **Anonymous Sharing**: Content can be shared without revealing identity
2. **Selective Disclosure**: Granular control over what data is shared
3. **Local-First**: Primary data storage is local to user
4. **Network Anonymity**: P2P communication can be anonymous
