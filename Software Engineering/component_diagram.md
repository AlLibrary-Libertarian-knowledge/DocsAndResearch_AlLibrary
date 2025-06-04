```mermaid
graph TB
    %% Frontend Components
    subgraph Frontend
        Viewer[Document Viewer]
        Search[Search Interface]
        UI[User Interface]
    end

    %% Core Services
    subgraph CoreServices[Core Services]
        DocManager[Document Manager]
        Store[Content Store]
        Version[Version Control]
        Metadata[Metadata Manager]
    end

    %% P2P Network
    subgraph P2PNetwork[P2P Network]
        Network[Network Manager]
        Router[Content Router]
        Discovery[Peer Discovery]
    end

    %% Storage
    subgraph Storage
        IPFS[IPFS Interface]
        Cache[Local Cache]
        Verify[Content Verification]
    end

    %% Security
    subgraph Security
        Hash[Content Hash]
        Source[Source Verification]
        Access[Access Control]
    end

    %% Frontend Connections
    UI --> Viewer
    UI --> Search
    Viewer --> DocManager
    Search --> DocManager

    %% Core Service Connections
    DocManager --> Store
    DocManager --> Version
    DocManager --> Metadata
    Store --> IPFS
    Store --> Cache

    %% Network Connections
    Network --> Router
    Network --> Discovery
    Router --> IPFS
    Router --> Cache

    %% Security Connections
    Hash --> Verify
    Source --> Verify
    Access --> DocManager
```
