# AlLibrary Detailed System Design

## Overview

This document provides comprehensive technical specifications for AlLibrary's decentralized architecture, including complete database schemas, API definitions, caching strategies, and P2P communication protocols.

## System Architecture Overview

<function_calls>
<invoke name="create_diagram">
<parameter name="content">graph TB
subgraph "Client Application (Tauri)"
UI["SolidJS Frontend"]
LocalDB["SQLite Database"]
Cache["Local Cache"]
end

    subgraph "P2P Network Layer"
        P2P["libp2p Node"]
        DHT["Distributed Hash Table"]
        PubSub["Publish/Subscribe"]
    end

    subgraph "Network Options"
        Internet["Regular Internet<br/>Direct P2P"]
        TOR["TOR Network<br/>Anonymous P2P"]
    end

    subgraph "Content Processing"
        Scanner["Security Scanner"]
        Cultural["Cultural Validator"]
        Index["Search Indexer"]
    end

    subgraph "External Peers"
        Peer1["Cultural Institution"]
        Peer2["Academic Library"]
        Peer3["Community Archive"]
    end

    UI --> LocalDB
    UI --> Cache
    UI --> P2P

    P2P --> DHT
    P2P --> PubSub
    P2P --> Internet
    P2P --> TOR

    Scanner --> LocalDB
    Cultural --> LocalDB
    Index --> LocalDB

    Internet --> Peer1
    Internet --> Peer2
    TOR --> Peer3

    style TOR fill:#9f6,stroke:#333,stroke-width:3px
    style Cultural fill:#f96,stroke:#333,stroke-width:2px

## 1. Database Schema Specification

### 1.1 Database Schema Overview

<function_calls>
<invoke name="create_diagram">
<parameter name="content">erDiagram
documents ||--o{ document_metadata : "has"
documents ||--o{ document_authors : "authored_by"
documents ||--o{ document_relationships : "relates_to"
documents ||--o{ content_availability : "available_on"
documents ||--o{ download_queue : "queued_for"
documents ||--o{ security_scans : "scanned_by"
documents ||--o{ processing_pipeline : "processed_by"

    authors ||--o{ document_authors : "authors"
    cultural_contexts ||--o{ documents : "categorizes"
    peers ||--o{ content_availability : "hosts"

    documents {
        string id PK
        string title
        string content_hash UK
        string file_type
        integer file_size
        string cultural_origin FK
        boolean is_shared
        string processing_status
        string malware_scan_status
        integer peer_availability_count
    }

    cultural_contexts {
        string id PK
        string culture_name
        string geographic_region
        string traditional_knowledge_protocols
        string access_restrictions
        string community_contact_info
    }

    peers {
        string id PK
        string peer_address
        string connection_status
        integer technical_reliability_score
        string cultural_specialization
        string network_type "internet_or_tor"
    }

    document_relationships {
        string id PK
        string source_document_id FK
        string target_document_id FK
        string relationship_type
        real confidence_score
    }

-- Complete document schema with cultural preservation focus
CREATE TABLE documents (
id TEXT PRIMARY KEY,
title TEXT NOT NULL,
description TEXT,
content_hash TEXT NOT NULL UNIQUE,
file_type TEXT NOT NULL CHECK (file_type IN ('PDF', 'EPUB')),
file_size INTEGER NOT NULL,
created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    -- Content metadata
    language_code TEXT,
    publication_date DATE,
    page_count INTEGER,

    -- Cultural context preservation
    cultural_origin TEXT,
    traditional_knowledge_protocols TEXT,
    indigenous_permissions TEXT,

    -- Technical metadata
    local_path TEXT,
    is_shared BOOLEAN DEFAULT true,
    processing_status TEXT DEFAULT 'pending'
        CHECK (processing_status IN ('pending', 'processing', 'verified', 'error')),

    -- Security and integrity
    content_verification_hash TEXT,
    malware_scan_status TEXT DEFAULT 'pending'
        CHECK (malware_scan_status IN ('pending', 'clean', 'suspicious', 'blocked')),
    javascript_stripped BOOLEAN DEFAULT false,

    -- P2P network metadata
    peer_availability_count INTEGER DEFAULT 0,
    last_availability_check TIMESTAMP,
    download_priority INTEGER DEFAULT 0,

    FOREIGN KEY (cultural_origin) REFERENCES cultural_contexts(id)

);

-- Extended metadata for comprehensive document description
CREATE TABLE document_metadata (
id TEXT PRIMARY KEY,
document_id TEXT NOT NULL,
metadata_key TEXT NOT NULL,
metadata_value TEXT NOT NULL,
metadata_type TEXT NOT NULL CHECK (metadata_type IN ('string', 'number', 'date', 'json')),
is_searchable BOOLEAN DEFAULT true,
created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (document_id) REFERENCES documents(id) ON DELETE CASCADE,
    UNIQUE(document_id, metadata_key)

);

-- Author information with cultural sensitivity
CREATE TABLE authors (
id TEXT PRIMARY KEY,
name TEXT NOT NULL,
birth_date DATE,
death_date DATE,
cultural_affiliation TEXT,
institutional_affiliation TEXT,
biographical_notes TEXT,
preferred_citation_format TEXT,
created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE document_authors (
document_id TEXT NOT NULL,
author_id TEXT NOT NULL,
author_role TEXT DEFAULT 'author'
CHECK (author_role IN ('author', 'editor', 'translator', 'compiler', 'contributor')),
attribution_order INTEGER DEFAULT 1,

    PRIMARY KEY (document_id, author_id),
    FOREIGN KEY (document_id) REFERENCES documents(id) ON DELETE CASCADE,
    FOREIGN KEY (author_id) REFERENCES authors(id)

);

-- Cultural context preservation
CREATE TABLE cultural_contexts (
id TEXT PRIMARY KEY,
culture_name TEXT NOT NULL,
geographic_region TEXT,
language_family TEXT,
traditional_knowledge_protocols TEXT,
access_restrictions TEXT,
community_contact_info TEXT,
preservation_guidelines TEXT,
created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- Content relationship mapping for multiple perspectives
CREATE TABLE document_relationships (
id TEXT PRIMARY KEY,
source_document_id TEXT NOT NULL,
target_document_id TEXT NOT NULL,
relationship_type TEXT NOT NULL
CHECK (relationship_type IN (
'conflicting_narrative', 'supporting_evidence', 'alternative_perspective',
'translation', 'summary', 'response', 'critique', 'supplement'
)),
relationship_description TEXT,
confidence_score REAL DEFAULT 0.5 CHECK (confidence_score >= 0 AND confidence_score <= 1),
created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (source_document_id) REFERENCES documents(id) ON DELETE CASCADE,
    FOREIGN KEY (target_document_id) REFERENCES documents(id) ON DELETE CASCADE,
    UNIQUE(source_document_id, target_document_id, relationship_type)

);

````

### 1.2 Core Document Storage (SQLite Local Storage)

```sql
-- Peer network tracking with reputation (technical only, no content control)
CREATE TABLE peers (
    id TEXT PRIMARY KEY,
    peer_address TEXT NOT NULL,
    last_seen TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    connection_status TEXT DEFAULT 'disconnected'
        CHECK (connection_status IN ('connected', 'disconnected', 'connecting', 'blocked')),

    -- Network type for routing decisions
    network_type TEXT DEFAULT 'internet'
        CHECK (network_type IN ('internet', 'tor', 'both')),
    onion_address TEXT, -- For TOR hidden services

    -- Technical performance metrics only
    average_response_time_ms INTEGER DEFAULT 0,
    successful_connections INTEGER DEFAULT 0,
    failed_connections INTEGER DEFAULT 0,
    bandwidth_mbps REAL DEFAULT 0,

    -- Geographic and cultural distribution (no control, just awareness)
    approximate_location TEXT,
    cultural_specialization TEXT,

    -- Technical capabilities
    supported_protocols TEXT,
    max_concurrent_downloads INTEGER DEFAULT 5,
    supports_tor BOOLEAN DEFAULT false,

    -- No voting power or content control capabilities
    technical_reliability_score REAL DEFAULT 0.5,
    anonymity_preference TEXT DEFAULT 'normal'
        CHECK (anonymity_preference IN ('normal', 'high', 'maximum')),

    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- Content availability tracking across peers
CREATE TABLE content_availability (
    id TEXT PRIMARY KEY,
    document_id TEXT NOT NULL,
    peer_id TEXT NOT NULL,
    availability_status TEXT DEFAULT 'unknown'
        CHECK (availability_status IN ('available', 'unavailable', 'partial', 'unknown')),
    last_verified TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    chunk_availability TEXT, -- JSON array of available chunks

    FOREIGN KEY (document_id) REFERENCES documents(id) ON DELETE CASCADE,
    FOREIGN KEY (peer_id) REFERENCES peers(id) ON DELETE CASCADE,
    UNIQUE(document_id, peer_id)
);

-- Download queue and transfer management
CREATE TABLE download_queue (
    id TEXT PRIMARY KEY,
    document_id TEXT NOT NULL,
    priority INTEGER DEFAULT 0,
    status TEXT DEFAULT 'queued'
        CHECK (status IN ('queued', 'downloading', 'completed', 'failed', 'paused')),
    progress_percentage REAL DEFAULT 0 CHECK (progress_percentage >= 0 AND progress_percentage <= 100),
    download_speed_kbps REAL DEFAULT 0,
    estimated_completion TIMESTAMP,
    source_peers TEXT, -- JSON array of peer IDs
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    started_at TIMESTAMP,
    completed_at TIMESTAMP,

    FOREIGN KEY (document_id) REFERENCES documents(id) ON DELETE CASCADE
);

-- TOR network configuration and routing
CREATE TABLE tor_configuration (
    id TEXT PRIMARY KEY,
    is_enabled BOOLEAN DEFAULT false,
    socks_proxy_port INTEGER DEFAULT 9050,
    control_port INTEGER DEFAULT 9051,
    hidden_service_dir TEXT,
    onion_address TEXT,
    private_key_path TEXT,
    circuit_timeout_seconds INTEGER DEFAULT 60,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- TOR circuit tracking for performance optimization
CREATE TABLE tor_circuits (
    id TEXT PRIMARY KEY,
    circuit_id TEXT NOT NULL,
    entry_node TEXT,
    middle_node TEXT,
    exit_node TEXT,
    is_active BOOLEAN DEFAULT true,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    last_used TIMESTAMP,
    performance_score REAL DEFAULT 0.5
);

-- Network routing preferences per user
CREATE TABLE network_preferences (
    user_id TEXT PRIMARY KEY,
    preferred_network TEXT DEFAULT 'internet'
        CHECK (preferred_network IN ('internet', 'tor', 'auto')),
    anonymity_level TEXT DEFAULT 'normal'
        CHECK (anonymity_level IN ('normal', 'high', 'maximum')),
    auto_switch_on_censorship BOOLEAN DEFAULT true,
    tor_always_for_sensitive_content BOOLEAN DEFAULT false,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);
```

### 1.4 P2P Network State Management with TOR Support

<function_calls>
<invoke name="create_diagram">
<parameter name="content">graph TB
    subgraph "Network Layer Selection"
        NetSelect["Network Selection UI"]
        InternetBtn["🌐 Internet P2P"]
        TORBtn["🧅 TOR Network"]
    end

    subgraph "Internet P2P"
        InternetP2P["Direct libp2p"]
        InternetDHT["Public DHT"]
        InternetPeers["Direct Peer Connections"]
    end

    subgraph "TOR P2P"
        TORProxy["TOR Proxy"]
        TORHiddenService["Hidden Services"]
        TOROnionPeers["Onion Peer Connections"]
    end

    subgraph "Content Sharing"
        Upload["Upload Content"]
        Download["Download Content"]
        Search["Search Network"]
    end

    NetSelect --> InternetBtn
    NetSelect --> TORBtn

    InternetBtn --> InternetP2P
    TORBtn --> TORProxy

    InternetP2P --> InternetDHT
    InternetP2P --> InternetPeers

    TORProxy --> TORHiddenService
    TORHiddenService --> TOROnionPeers

    InternetPeers --> Upload
    InternetPeers --> Download
    InternetPeers --> Search

    TOROnionPeers --> Upload
    TOROnionPeers --> Download
    TOROnionPeers --> Search

    style TORBtn fill:#9f6,stroke:#333,stroke-width:3px
    style TORProxy fill:#9f6,stroke:#333,stroke-width:2px
    style TORHiddenService fill:#9f6,stroke:#333,stroke-width:2px

```sql
-- Content security scanning results
CREATE TABLE security_scans (
    id TEXT PRIMARY KEY,
    document_id TEXT NOT NULL,
    scan_type TEXT NOT NULL
        CHECK (scan_type IN ('malware', 'content_filter', 'integrity_check', 'format_validation')),
    scan_result TEXT NOT NULL
        CHECK (scan_result IN ('clean', 'suspicious', 'blocked', 'error')),
    scan_details TEXT, -- JSON with detailed results
    scanner_version TEXT,
    scan_timestamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (document_id) REFERENCES documents(id) ON DELETE CASCADE
);

-- Content processing pipeline tracking
CREATE TABLE processing_pipeline (
    id TEXT PRIMARY KEY,
    document_id TEXT NOT NULL,
    pipeline_stage TEXT NOT NULL
        CHECK (pipeline_stage IN (
            'format_validation', 'security_scan', 'content_extraction',
            'metadata_generation', 'cultural_context_analysis', 'indexing'
        )),
    stage_status TEXT DEFAULT 'pending'
        CHECK (stage_status IN ('pending', 'processing', 'completed', 'failed', 'skipped')),
    processing_result TEXT, -- JSON with stage-specific results
    error_message TEXT,
    processing_time_ms INTEGER,
    started_at TIMESTAMP,
    completed_at TIMESTAMP,

    FOREIGN KEY (document_id) REFERENCES documents(id) ON DELETE CASCADE
);
```

## 2. API Specifications

### 2.1 RESTful API Endpoints (Rust/Axum Implementation)

```rust
// Complete API specification with OpenAPI documentation
use axum::{Json, extract::State, http::StatusCode};
use serde::{Deserialize, Serialize};
use utoipa::{OpenApi, ToSchema};

#[derive(OpenApi)]
#[openapi(
    paths(
        upload_document,
        get_document,
        search_documents,
        get_document_relationships,
        get_network_status,
        manage_download_queue
    ),
    components(schemas(
        DocumentUpload, DocumentResponse, SearchQuery, SearchResults,
        DocumentRelationship, NetworkStatus, DownloadQueueItem
    ))
)]
pub struct AlLibraryApi;

// Document management endpoints
#[derive(Deserialize, ToSchema)]
pub struct DocumentUpload {
    #[schema(format = "binary")]
    pub file_data: Vec<u8>,
    pub title: Option<String>,
    pub description: Option<String>,
    pub cultural_context: Option<CulturalContext>,
    pub author_information: Option<Vec<AuthorInfo>>,
    pub metadata: Option<serde_json::Value>,
}

#[derive(Serialize, ToSchema)]
pub struct DocumentResponse {
    pub id: String,
    pub title: String,
    pub content_hash: String,
    pub file_size: u64,
    pub processing_status: ProcessingStatus,
    pub cultural_context: Option<CulturalContext>,
    pub availability: ContentAvailability,
    pub relationships: Vec<DocumentRelationship>,
}

#[utoipa::path(
    post,
    path = "/api/v1/documents/upload",
    request_body = DocumentUpload,
    responses(
        (status = 201, description = "Document uploaded and processing started", body = DocumentResponse),
        (status = 400, description = "Invalid file format or malformed request"),
        (status = 413, description = "File too large"),
        (status = 415, description = "Unsupported file type (only PDF/EPUB accepted)"),
        (status = 422, description = "File failed security validation")
    ),
    tag = "Documents"
)]
pub async fn upload_document(
    State(app_state): State<AppState>,
    multipart: Multipart,
) -> Result<(StatusCode, Json<DocumentResponse>), ApiError> {
    // Implementation with comprehensive validation:
    // 1. Format validation (PDF/EPUB only)
    // 2. Security scanning (malware, executable content)
    // 3. Content sanitization (JavaScript removal)
    // 4. Metadata extraction and cultural context analysis
    // 5. P2P network integration for sharing
}

#[utoipa::path(
    get,
    path = "/api/v1/documents/{document_id}",
    params(
        ("document_id" = String, Path, description = "Document unique identifier")
    ),
    responses(
        (status = 200, description = "Document details with availability info", body = DocumentResponse),
        (status = 404, description = "Document not found"),
        (status = 403, description = "Access restricted by cultural protocols")
    ),
    tag = "Documents"
)]
pub async fn get_document(
    State(app_state): State<AppState>,
    Path(document_id): Path<String>,
) -> Result<Json<DocumentResponse>, ApiError> {
    // Implementation includes:
    // - Cultural access protocol verification
    // - P2P availability checking
    // - Relationship mapping
    // - Security status validation
}
```

### 2.2 Advanced Search API

```rust
#[derive(Deserialize, ToSchema)]
pub struct SearchQuery {
    pub query_text: Option<String>,
    pub filters: SearchFilters,
    pub cultural_context_filter: Option<Vec<String>>,
    pub perspective_diversity: bool, // Include conflicting viewpoints
    pub limit: Option<u32>,
    pub offset: Option<u32>,
    pub sort_by: SortOption,
}

#[derive(Deserialize, ToSchema)]
pub struct SearchFilters {
    pub languages: Option<Vec<String>>,
    pub date_range: Option<DateRange>,
    pub file_types: Option<Vec<String>>,
    pub cultural_origins: Option<Vec<String>>,
    pub relationship_types: Option<Vec<String>>,
    pub availability_status: Option<Vec<String>>,
}

#[utoipa::path(
    post,
    path = "/api/v1/search",
    request_body = SearchQuery,
    responses(
        (status = 200, description = "Search results with cultural and perspective diversity", body = SearchResults),
        (status = 400, description = "Invalid search parameters")
    ),
    tag = "Search"
)]
pub async fn search_documents(
    State(app_state): State<AppState>,
    Json(query): Json<SearchQuery>,
) -> Result<Json<SearchResults>, ApiError> {
    // Implementation includes:
    // - Distributed P2P search across network
    // - Cultural context-aware filtering
    // - Multiple perspective aggregation
    // - Availability-based result ranking
    // - Relationship-based result expansion
}
```

### 2.3 P2P Network Management API

```rust
#[derive(Serialize, ToSchema)]
pub struct NetworkStatus {
    pub connected_peers: u32,
    pub total_documents_available: u64,
    pub network_health_score: f64,
    pub bandwidth_usage: BandwidthStats,
    pub cultural_diversity_metrics: CulturalDiversityMetrics,
    pub geographic_distribution: Vec<GeographicRegion>,
}

#[utoipa::path(
    get,
    path = "/api/v1/network/status",
    responses(
        (status = 200, description = "Current P2P network status and health metrics", body = NetworkStatus)
    ),
    tag = "Network"
)]
pub async fn get_network_status(
    State(app_state): State<AppState>,
) -> Result<Json<NetworkStatus>, ApiError> {
    // Implementation provides:
    // - Real-time peer connectivity status
    // - Content availability distribution
    // - Cultural and geographic diversity metrics
    // - Network performance statistics
}
```

## 3. Caching Architecture

### 3.1 Multi-Level Caching Strategy

<function_calls>
<invoke name="create_diagram">
<parameter name="content">graph TB
    subgraph "Application Layer"
        App["AlLibrary App"]
        UI["User Interface"]
    end

    subgraph "Cache Hierarchy"
        L1["Level 1: Memory Cache<br/>LRU 100MB<br/>Hot Documents"]
        L2["Level 2: Disk Cache<br/>SSD 10GB<br/>Recent Documents"]
        L3["Level 3: Network Cache<br/>P2P Network<br/>Distributed Content"]
        L4["Level 4: Search Index Cache<br/>Elasticsearch/SQLite FTS<br/>Query Results"]
    end

    subgraph "Network Routes"
        Internet["Internet P2P"]
        TOR["🧅 TOR Network"]
    end

    subgraph "Cultural Cache"
        CulturalMem["Cultural Context Cache"]
        PermissionCache["Access Permission Cache"]
        CommunityCache["Community Liaison Cache"]
    end

    App --> L1
    UI --> L1

    L1 -.->|Cache Miss| L2
    L2 -.->|Cache Miss| L3
    L3 -.->|Cache Miss| Internet
    L3 -.->|Privacy Mode| TOR

    L1 --> CulturalMem
    L2 --> PermissionCache
    L3 --> CommunityCache

    L4 --> L1
    L4 --> L2

    style TOR fill:#9f6,stroke:#333,stroke-width:3px
    style CulturalMem fill:#f96,stroke:#333,stroke-width:2px
    style L1 fill:#bbf,stroke:#333,stroke-width:2px

```rust
// Comprehensive caching system for performance optimization
pub struct CacheManager {
    // Level 1: In-memory hot data cache
    memory_cache: Arc<RwLock<LruCache<String, CachedItem>>>,

    // Level 2: Local disk cache for documents
    disk_cache: DiskCacheManager,

    // Level 3: P2P network content cache
    network_cache: NetworkCacheManager,

    // Level 4: Search index cache
    search_cache: SearchIndexCache,
}

impl CacheManager {
    pub async fn get_document(&self, content_hash: &str) -> CacheResult<Document> {
        // Cache hierarchy with fallback strategy:

        // 1. Check memory cache first (fastest)
        if let Some(doc) = self.memory_cache.read().await.get(content_hash) {
            return Ok(doc.clone());
        }

        // 2. Check local disk cache
        if let Ok(doc) = self.disk_cache.get_document(content_hash).await {
            self.memory_cache.write().await.put(content_hash.to_string(), doc.clone());
            return Ok(doc);
        }

        // 3. Query P2P network
        if let Ok(doc) = self.network_cache.fetch_from_peers(content_hash).await {
            self.disk_cache.store_document(&doc).await?;
            self.memory_cache.write().await.put(content_hash.to_string(), doc.clone());
            return Ok(doc);
        }

        Err(CacheError::NotFound)
    }

    pub async fn cache_search_results(&self, query: &SearchQuery, results: &SearchResults) {
        let cache_key = self.generate_search_cache_key(query);
        self.search_cache.store(cache_key, results, Duration::from_secs(300)).await;
    }
}

// Cultural context-aware caching
pub struct CulturalContextCache {
    context_cache: HashMap<String, CulturalContext>,
    access_permissions: HashMap<String, AccessPermissions>,
}

impl CulturalContextCache {
    pub async fn get_cultural_context(&self, document_id: &str) -> Option<CulturalContext> {
        // Respect cultural protocols in caching
        if let Some(context) = self.context_cache.get(document_id) {
            if self.verify_access_permissions(document_id).await {
                return Some(context.clone());
            }
        }
        None
    }
}
```

### 3.2 Performance-Optimized Search Caching

```rust
// Search index caching with cultural sensitivity
pub struct SearchIndexCache {
    // Full-text search indices
    text_indices: HashMap<String, SearchIndex>,

    // Cultural context indices
    cultural_indices: HashMap<String, CulturalIndex>,

    // Relationship mapping cache
    relationship_cache: RelationshipCache,

    // Availability cache for P2P content
    availability_cache: AvailabilityCache,
}

impl SearchIndexCache {
    pub async fn perform_cached_search(&self, query: &SearchQuery) -> SearchResults {
        let mut results = SearchResults::new();

        // Combine multiple index sources
        if let Some(text_results) = self.search_text_index(query).await {
            results.merge(text_results);
        }

        if let Some(cultural_results) = self.search_cultural_index(query).await {
            results.merge(cultural_results);
        }

        // Include relationship-based results for multiple perspectives
        if query.perspective_diversity {
            let related_results = self.find_related_perspectives(&results).await;
            results.merge(related_results);
        }

        // Filter by availability in P2P network
        results.filter_by_availability(&self.availability_cache).await;

        results
    }
}
```

## 4. Message Queue Design for P2P Communication

### 4.1 Network Selection and TOR Integration

<function_calls>
<invoke name="create_diagram">
<parameter name="content">sequenceDiagram
    participant User
    participant UI
    participant NetworkSelector
    participant InternetP2P
    participant TORProxy
    participant Peer

    User->>UI: Click "Share Document"
    UI->>User: Show Network Selection

    alt Internet P2P Selected
        User->>NetworkSelector: Select "🌐 Internet P2P"
        NetworkSelector->>InternetP2P: Initialize Direct Connection
        InternetP2P->>Peer: Direct P2P Connection
        Peer-->>InternetP2P: Connection Established
        InternetP2P-->>UI: Ready to Share
    else TOR Network Selected
        User->>NetworkSelector: Select "🧅 TOR Network"
        NetworkSelector->>TORProxy: Initialize TOR Connection
        TORProxy->>TORProxy: Create Circuit
        TORProxy->>Peer: Onion Connection
        Peer-->>TORProxy: Hidden Service Response
        TORProxy-->>UI: Anonymous Connection Ready
    end

    UI->>User: "Connection Ready - Upload Document"
    User->>UI: Upload File
    UI->>NetworkSelector: Route via Selected Network

```rust
// P2P message queue system with TOR support using libp2p
use libp2p::{PeerId, Multiaddr};
use tokio::sync::mpsc;

pub struct P2PMessageQueue {
    // Outbound message queues per peer
    outbound_queues: HashMap<PeerId, mpsc::Sender<P2PMessage>>,

    // Inbound message processor
    inbound_processor: InboundMessageProcessor,

    // Message routing table
    routing_table: RoutingTable,

    // Cultural context routing
    cultural_routing: CulturalRoutingManager,

    // TOR network integration
    tor_manager: TORNetworkManager,

    // Network selection manager
    network_selector: NetworkSelector,
}

// TOR network integration manager
pub struct TORNetworkManager {
    tor_client: TorClient,
    hidden_service_manager: HiddenServiceManager,
    circuit_manager: CircuitManager,
    onion_address: Option<String>,
}

impl TORNetworkManager {
    pub async fn initialize_tor_network(&self) -> Result<TORNetworkStatus, TORError> {
        // Initialize TOR client connection
        let tor_status = self.tor_client.connect().await?;

        if tor_status.is_connected {
            // Create hidden service for receiving connections
            let hidden_service = self.hidden_service_manager
                .create_hidden_service().await?;

            // Initialize circuit management
            self.circuit_manager.initialize_circuits().await?;

            Ok(TORNetworkStatus {
                is_available: true,
                onion_address: hidden_service.onion_address,
                circuit_count: self.circuit_manager.active_circuits().await?,
            })
        } else {
            Err(TORError::ConnectionFailed)
        }
    }

    pub async fn route_message_through_tor(
        &self,
        message: P2PMessage,
        target_onion_address: &str
    ) -> Result<(), TORError> {
        // Select optimal circuit for message routing
        let optimal_circuit = self.circuit_manager
            .select_optimal_circuit(target_onion_address).await?;

        // Route message through TOR network
        let tor_result = self.tor_client
            .route_message(message, optimal_circuit).await?;

        Ok(tor_result)
    }
}

// Network selection UI component integration
pub struct NetworkSelector {
    current_selection: NetworkType,
    tor_availability: bool,
    user_preferences: NetworkPreferences,
}

#[derive(Debug, Clone)]
pub enum NetworkType {
    Internet,
    TOR,
    Auto, // Automatically select based on context
}

impl NetworkSelector {
    pub async fn show_network_selection_ui(&self) -> NetworkSelectionResult {
        // This would integrate with the SolidJS frontend
        let ui_options = NetworkSelectionOptions {
            internet_option: NetworkOption {
                label: "🌐 Internet P2P".to_string(),
                description: "Direct peer-to-peer connections over the internet".to_string(),
                speed: "Fast",
                privacy: "Standard",
                available: true,
            },
            tor_option: NetworkOption {
                label: "🧅 TOR Network".to_string(),
                description: "Anonymous connections through TOR hidden services".to_string(),
                speed: "Slower",
                privacy: "High",
                available: self.tor_availability,
            },
            auto_option: NetworkOption {
                label: "🔄 Auto Select".to_string(),
                description: "Automatically choose based on content sensitivity".to_string(),
                speed: "Variable",
                privacy: "Adaptive",
                available: true,
            },
        };

        NetworkSelectionResult {
            options: ui_options,
            recommended: self.get_recommended_network().await?,
        }
    }

    pub async fn handle_network_selection(&mut self, selection: NetworkType) -> SelectionResult {
        self.current_selection = selection.clone();

        match selection {
            NetworkType::Internet => {
                SelectionResult::Success {
                    message: "Direct internet P2P connections enabled".to_string(),
                    estimated_speed: "High",
                }
            },
            NetworkType::TOR => {
                if self.tor_availability {
                    SelectionResult::Success {
                        message: "Anonymous TOR network connections enabled".to_string(),
                        estimated_speed: "Medium",
                    }
                } else {
                    SelectionResult::Error {
                        message: "TOR network is not available. Please install TOR.".to_string(),
                        fallback_option: Some(NetworkType::Internet),
                    }
                }
            },
            NetworkType::Auto => {
                SelectionResult::Success {
                    message: "Auto-selection enabled. Network will be chosen based on content.".to_string(),
                    estimated_speed: "Variable",
                }
            }
        }
    }
}

#[derive(Debug, Clone)]
pub enum P2PMessage {
    ContentRequest {
        content_hash: String,
        requesting_peer: PeerId,
        priority: RequestPriority,
    },
    ContentResponse {
        content_hash: String,
        content_data: Vec<u8>,
        cultural_context: Option<CulturalContext>,
    },
    AvailabilityAnnouncement {
        available_content: Vec<String>,
        cultural_specializations: Vec<String>,
        peer_capabilities: PeerCapabilities,
    },
    SearchQuery {
        query: DistributedSearchQuery,
        response_channel: PeerId,
        cultural_filters: Vec<String>,
    },
    SearchResults {
        query_id: String,
        results: Vec<SearchResult>,
        perspective_diversity: bool,
    },
    NetworkHealthPing {
        timestamp: u64,
        peer_status: PeerStatus,
    },
}

impl P2PMessageQueue {
    pub async fn route_message(&self, message: P2PMessage, target_peer: Option<PeerId>) {
        match message {
            P2PMessage::ContentRequest { content_hash, .. } => {
                // Route to peers likely to have the content
                let candidate_peers = self.routing_table
                    .find_content_providers(&content_hash).await;

                for peer in candidate_peers {
                    self.send_to_peer(peer, message.clone()).await;
                }
            },

            P2PMessage::SearchQuery { cultural_filters, .. } => {
                // Route to culturally relevant peers
                let relevant_peers = self.cultural_routing
                    .find_cultural_specialists(&cultural_filters).await;

                for peer in relevant_peers {
                    self.send_to_peer(peer, message.clone()).await;
                }
            },

            _ => {
                // Broadcast or direct routing
                if let Some(peer) = target_peer {
                    self.send_to_peer(peer, message).await;
                } else {
                    self.broadcast_message(message).await;
                }
            }
        }
    }
}
```

### 4.2 Cultural Context-Aware Message Processing

```rust
// Message processing with cultural sensitivity
pub struct CulturalMessageProcessor {
    access_control: CulturalAccessControl,
    permission_validator: PermissionValidator,
}

impl CulturalMessageProcessor {
    pub async fn process_content_request(
        &self,
        request: ContentRequest,
        requesting_peer: PeerId
    ) -> ProcessingResult {
        // Verify cultural access permissions
        let cultural_context = self.get_cultural_context(&request.content_hash).await?;

        if let Some(context) = cultural_context {
            let has_permission = self.permission_validator
                .verify_access_permission(&context, &requesting_peer).await?;

            if !has_permission {
                return Ok(ProcessingResult::AccessDenied {
                    reason: "Cultural access restrictions apply".to_string(),
                    contact_info: context.community_contact_info,
                });
            }
        }

        // Proceed with content delivery
        Ok(ProcessingResult::ContentDelivery {
            content_hash: request.content_hash,
            delivery_method: DeliveryMethod::P2PTransfer,
        })
    }

    pub async fn process_search_query(
        &self,
        query: DistributedSearchQuery
    ) -> Vec<SearchResult> {
        let mut results = Vec::new();

        // Apply cultural filters while preserving multiple perspectives
        for result in self.perform_local_search(&query).await {
            if self.respects_cultural_protocols(&result).await {
                results.push(result);
            }
        }

        // Include conflicting perspectives if requested
        if query.include_alternative_perspectives {
            let alternative_results = self.find_alternative_perspectives(&results).await;
            results.extend(alternative_results);
        }

        results
    }
}
```

### 4.3 Background Task Management

```rust
// Background task queue for document processing and network maintenance
pub struct BackgroundTaskQueue {
    task_queues: HashMap<TaskPriority, VecDeque<BackgroundTask>>,
    worker_pool: WorkerPool,
    cultural_task_processor: CulturalTaskProcessor,
}

#[derive(Debug)]
pub enum BackgroundTask {
    DocumentProcessing {
        document_id: String,
        processing_pipeline: Vec<ProcessingStage>,
        cultural_context: Option<CulturalContext>,
    },
    SecurityScanning {
        document_id: String,
        scan_types: Vec<ScanType>,
    },
    NetworkMaintenance {
        maintenance_type: MaintenanceType,
        target_peers: Option<Vec<PeerId>>,
    },
    ContentReplication {
        content_hash: String,
        target_redundancy: u32,
        priority_regions: Vec<String>,
    },
    SearchIndexUpdate {
        document_ids: Vec<String>,
        index_types: Vec<IndexType>,
    },
}

impl BackgroundTaskQueue {
    pub async fn process_tasks(&self) {
        loop {
            // Process high-priority tasks first
            for priority in [TaskPriority::Critical, TaskPriority::High, TaskPriority::Normal] {
                if let Some(task) = self.task_queues.get_mut(&priority).unwrap().pop_front() {
                    self.execute_task(task).await;
                    break;
                }
            }

            tokio::time::sleep(Duration::from_millis(100)).await;
        }
    }

    async fn execute_task(&self, task: BackgroundTask) {
        match task {
            BackgroundTask::DocumentProcessing { document_id, cultural_context, .. } => {
                // Respect cultural processing protocols
                if let Some(context) = cultural_context {
                    self.cultural_task_processor
                        .process_with_cultural_sensitivity(document_id, context).await;
                } else {
                    self.worker_pool.process_document(document_id).await;
                }
            },

            BackgroundTask::ContentReplication { content_hash, target_redundancy, .. } => {
                // Ensure content availability across diverse geographic/cultural regions
                self.replicate_content_with_diversity(content_hash, target_redundancy).await;
            },

            _ => {
                // Standard task processing
                self.worker_pool.execute_standard_task(task).await;
            }
        }
    }
}
```

## 5. Frontend Network Selection Component

### 5.1 SolidJS Network Selection UI

```typescript
// Network selection component for SolidJS frontend
import { createSignal, createResource, Show, For } from "solid-js";
import { invoke } from "@tauri-apps/api/tauri";

interface NetworkOption {
  id: string;
  label: string;
  description: string;
  icon: string;
  speed: string;
  privacy: string;
  available: boolean;
}

interface NetworkStatus {
  tor_available: boolean;
  current_network: string;
  connection_quality: string;
}

export function NetworkSelectionModal() {
  const [selectedNetwork, setSelectedNetwork] = createSignal<string>("internet");
  const [isModalOpen, setIsModalOpen] = createSignal(false);

  const [networkStatus] = createResource<NetworkStatus>(async () => {
    return await invoke("get_network_status");
  });

  const networkOptions: NetworkOption[] = [
    {
      id: "internet",
      label: "🌐 Internet P2P",
      description: "Direct peer-to-peer connections over the internet",
      icon: "🌐",
      speed: "Fast",
      privacy: "Standard",
      available: true,
    },
    {
      id: "tor",
      label: "🧅 TOR Network",
      description: "Anonymous connections through TOR hidden services",
      icon: "🧅",
      speed: "Slower",
      privacy: "High",
      available: networkStatus()?.tor_available ?? false,
    },
    {
      id: "auto",
      label: "🔄 Auto Select",
      description: "Automatically choose based on content sensitivity",
      icon: "🔄",
      speed: "Variable",
      privacy: "Adaptive",
      available: true,
    },
  ];

  const handleNetworkSelection = async (networkId: string) => {
    try {
      await invoke("set_network_preference", { network: networkId });
      setSelectedNetwork(networkId);
      setIsModalOpen(false);

      // Show user feedback
      const networkLabel = networkOptions.find(opt => opt.id === networkId)?.label;
      console.log(`Switched to ${networkLabel}`);
    } catch (error) {
      console.error("Failed to change network:", error);
    }
  };

  return (
    <div class="network-selection">
      <button
        class="network-status-btn"
        onClick={() => setIsModalOpen(true)}
      >
        <span class="current-network-icon">
          {networkOptions.find(opt => opt.id === selectedNetwork())?.icon}
        </span>
        <span class="network-label">
          {selectedNetwork() === "internet" && "Internet P2P"}
          {selectedNetwork() === "tor" && "TOR Network"}
          {selectedNetwork() === "auto" && "Auto Select"}
        </span>
        <span class="connection-quality">
          {networkStatus()?.connection_quality}
        </span>
      </button>

      <Show when={isModalOpen()}>
        <div class="modal-backdrop" onClick={() => setIsModalOpen(false)}>
          <div class="network-modal" onClick={(e) => e.stopPropagation()}>
            <div class="modal-header">
              <h3>Choose Network Type</h3>
              <button
                class="close-btn"
                onClick={() => setIsModalOpen(false)}
              >
                ✕
              </button>
            </div>

            <div class="network-options">
              <For each={networkOptions}>
                {(option) => (
                  <div
                    class={`network-option ${selectedNetwork() === option.id ? 'selected' : ''} ${!option.available ? 'disabled' : ''}`}
                    onClick={() => option.available && handleNetworkSelection(option.id)}
                  >
                    <div class="option-header">
                      <span class="option-icon">{option.icon}</span>
                      <span class="option-label">{option.label}</span>
                      <Show when={selectedNetwork() === option.id}>
                        <span class="selected-indicator">✓</span>
                      </Show>
                    </div>

                    <p class="option-description">{option.description}</p>

                    <div class="option-metrics">
                      <div class="metric">
                        <span class="metric-label">Speed:</span>
                        <span class="metric-value">{option.speed}</span>
                      </div>
                      <div class="metric">
                        <span class="metric-label">Privacy:</span>
                        <span class="metric-value">{option.privacy}</span>
                      </div>
                    </div>

                    <Show when={!option.available}>
                      <div class="unavailable-notice">
                        {option.id === "tor" && "TOR not installed or unavailable"}
                      </div>
                    </Show>
                  </div>
                )}
              </For>
            </div>

            <div class="modal-footer">
              <div class="privacy-notice">
                <span class="privacy-icon">🔒</span>
                <span>Your network choice affects privacy and speed. TOR provides maximum anonymity.</span>
              </div>
            </div>
          </div>
        </div>
      </Show>
    </div>
  );
}

// CSS styles for the network selection component
const styles = `
.network-selection {
  position: relative;
}

.network-status-btn {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 8px 16px;
  background: var(--surface-color);
  border: 1px solid var(--border-color);
  border-radius: 8px;
  cursor: pointer;
  transition: all 0.2s ease;
}

.network-status-btn:hover {
  background: var(--surface-hover-color);
  border-color: var(--primary-color);
}

.current-network-icon {
  font-size: 1.2em;
}

.connection-quality {
  font-size: 0.8em;
  color: var(--text-secondary);
  padding: 2px 6px;
  border-radius: 4px;
  background: var(--success-color);
}

.modal-backdrop {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
}

.network-modal {
  background: var(--surface-color);
  border-radius: 12px;
  padding: 24px;
  max-width: 500px;
  width: 90%;
  max-height: 80vh;
  overflow-y: auto;
}

.modal-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}

.network-options {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.network-option {
  padding: 16px;
  border: 2px solid var(--border-color);
  border-radius: 8px;
  cursor: pointer;
  transition: all 0.2s ease;
}

.network-option:hover:not(.disabled) {
  border-color: var(--primary-color);
  background: var(--surface-hover-color);
}

.network-option.selected {
  border-color: var(--primary-color);
  background: var(--primary-color-alpha);
}

.network-option.disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.option-header {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 8px;
}

.option-icon {
  font-size: 1.5em;
}

.option-label {
  font-weight: 600;
  flex: 1;
}

.selected-indicator {
  color: var(--primary-color);
  font-weight: bold;
}

.option-description {
  color: var(--text-secondary);
  margin-bottom: 12px;
  line-height: 1.4;
}

.option-metrics {
  display: flex;
  gap: 20px;
}

.metric {
  display: flex;
  flex-direction: column;
  gap: 2px;
}

.metric-label {
  font-size: 0.8em;
  color: var(--text-secondary);
}

.metric-value {
  font-weight: 600;
  font-size: 0.9em;
}

.unavailable-notice {
  margin-top: 8px;
  padding: 8px;
  background: var(--warning-color-alpha);
  border-radius: 4px;
  font-size: 0.9em;
  color: var(--warning-color);
}

.modal-footer {
  margin-top: 20px;
  padding-top: 16px;
  border-top: 1px solid var(--border-color);
}

.privacy-notice {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 0.9em;
  color: var(--text-secondary);
}

.privacy-icon {
  color: var(--primary-color);
}
`;
```

This detailed system design provides the comprehensive technical foundation needed for AlLibrary's decentralized architecture while maintaining respect for cultural contexts and supporting multiple historical perspectives. The TOR integration ensures users can access and share content anonymously when needed, supporting the platform's commitment to combating censorship and information manipulation.
````
