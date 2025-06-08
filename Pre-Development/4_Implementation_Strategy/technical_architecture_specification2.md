# AlLibrary Technical Architecture Specification

_Aligned with Tauri v2 + SolidJS + Rust Technology Stack_

## Architecture Overview

AlLibrary is built as a cross-platform desktop application using Tauri v2 framework, combining a Rust backend with a SolidJS frontend to create a decentralized P2P document sharing platform. The architecture prioritizes performance, security, and cultural sensitivity while maintaining the censorship-resistant principles of the project.

## Technology Stack

### Core Framework

- **Desktop Framework**: Tauri v2 (Rust + Web Technologies)
- **Frontend**: SolidJS + TypeScript
- **Backend**: Rust 1.70+
- **UI Library**: Solid-headless
- **Build System**: Vite + Tauri CLI

### Data & Storage

- **Local Database**: SQLite 3 with SQLx
- **Distributed Storage**: IPFS integration
- **Content Addressing**: IPFS CID system
- **File System**: Tauri File System API

### Networking & P2P

- **P2P Network**: libp2p (Rust implementation)
- **Protocol Stack**: IPFS + Custom protocols
- **Network Discovery**: mDNS + DHT
- **Content Distribution**: BitSwap + Custom sharing

### Development & Quality

- **Package Manager**: npm (frontend) + Cargo (backend)
- **Testing**: Vitest (frontend) + Rust test framework
- **Linting**: ESLint + Prettier (frontend) + Clippy (backend)
- **State Management**: SolidJS stores

---

## Architectural Layers

## Layer 1: System Interface (Tauri Core)

### Tauri Application Shell

```rust
// Main Tauri application structure
#[tauri::command]
fn main() {
    tauri::Builder::default()
        .plugin(tauri_plugin_fs::init())
        .plugin(tauri_plugin_dialog::init())
        .plugin(tauri_plugin_shell::init())
        .invoke_handler(tauri::generate_handler![
            // Document management commands
            import_document,
            search_documents,
            create_collection,
            // P2P network commands
            start_network,
            connect_peer,
            share_content,
            // Cultural protocol commands
            verify_cultural_permissions,
            check_sacred_content_access
        ])
        .run(tauri::generate_context!())
        .expect("error while running tauri application");
}
```

### System Integration

- **File System Access**: Secure document import/export
- **Network Access**: P2P communication and web connectivity
- **System Notifications**: User alerts and status updates
- **Process Management**: Background network operations
- **Security Context**: Sandboxed execution environment

### Platform Abstraction

- **Cross-Platform APIs**: Windows, macOS, Linux support
- **Native Integration**: System file dialogs, notifications
- **Performance Optimization**: Native code execution
- **Security Model**: OS-level security integration

---

## Layer 2: Core Services (Rust Backend)

### Document Management Service

```rust
// Document management and storage
pub struct DocumentManager {
    db: SqlitePool,
    storage: LocalStorage,
    ipfs: IpfsClient,
    cultural_guard: CulturalProtectionService,
}

impl DocumentManager {
    pub async fn import_document(&self, file_path: &str, metadata: DocumentMetadata) -> Result<DocumentId> {
        // Cultural sensitivity check
        if self.cultural_guard.requires_special_handling(&metadata).await? {
            return self.handle_sacred_content(file_path, metadata).await;
        }

        // Standard document processing
        let document = self.process_document(file_path, metadata).await?;
        let content_hash = self.store_to_ipfs(&document).await?;
        self.save_to_database(document, content_hash).await
    }

    pub async fn search_documents(&self, query: &SearchQuery) -> Result<Vec<Document>> {
        // Apply cultural access controls
        let filtered_query = self.cultural_guard.filter_search_query(query).await?;
        self.db.search_documents(filtered_query).await
    }
}
```

#### Features:

- **Multi-format Support**: PDF, EPUB processing
- **Metadata Extraction**: Automatic and manual metadata
- **Version Control**: Document versioning and history
- **Cultural Tagging**: Traditional knowledge classification
- **Access Control**: Community-based permissions

### P2P Network Service

```rust
// P2P networking using libp2p
pub struct P2PNetworkService {
    swarm: Swarm<NetworkBehaviour>,
    content_store: ContentStore,
    peer_manager: PeerManager,
    governance: CommunityGovernance,
}

#[derive(libp2p::NetworkBehaviour)]
struct NetworkBehaviour {
    kademlia: Kademlia<MemoryStore>,
    request_response: RequestResponse<ContentProtocol>,
    gossipsub: Gossipsub,
    identify: Identify,
}

impl P2PNetworkService {
    pub async fn start_network(&mut self) -> Result<()> {
        // Initialize libp2p swarm
        self.swarm.listen_on("/ip4/0.0.0.0/tcp/0".parse()?)?;

        // Start peer discovery
        self.discover_peers().await?;

        // Initialize community governance protocols
        self.governance.initialize_protocols().await?;

        Ok(())
    }

    pub async fn share_content(&mut self, content_id: ContentId, permissions: SharingPermissions) -> Result<()> {
        // Check cultural sharing permissions
        if !self.governance.can_share_content(&content_id, &permissions).await? {
            return Err(NetworkError::CulturalPermissionDenied);
        }

        // Distribute content to network
        self.announce_content_availability(content_id).await
    }
}
```

#### Features:

- **Peer Discovery**: Automatic peer discovery and connection
- **Content Distribution**: Efficient content sharing protocols
- **Network Health**: Connection monitoring and recovery
- **Governance Integration**: Community-controlled sharing
- **Cultural Protocols**: Traditional permission systems

### Cultural Protection Service

```rust
// Cultural sensitivity and protection systems
pub struct CulturalProtectionService {
    community_registry: CommunityRegistry,
    sacred_content_db: SqlitePool,
    elder_council: ElderCouncilInterface,
    permission_system: PermissionSystem,
}

impl CulturalProtectionService {
    pub async fn verify_cultural_permissions(&self, content: &Content, user: &User) -> Result<AccessLevel> {
        // Check if content is sacred or restricted
        if let Some(restrictions) = self.get_cultural_restrictions(content).await? {
            return self.evaluate_community_access(content, user, restrictions).await;
        }

        AccessLevel::Public
    }

    pub async fn handle_sacred_content(&self, content: &Content) -> Result<StorageDecision> {
        // Require elder council approval for sacred content
        let approval = self.elder_council.request_approval(content).await?;

        match approval.decision {
            ApprovalDecision::Approved => Ok(StorageDecision::StoreWithRestrictions(approval.restrictions)),
            ApprovalDecision::Rejected => Ok(StorageDecision::Reject),
            ApprovalDecision::RequiresModification => Ok(StorageDecision::RequiresModification(approval.requirements)),
        }
    }
}
```

#### Features:

- **Sacred Content Detection**: AI-assisted cultural content identification
- **Community Verification**: Elder and community leader approval workflows
- **Access Control**: Granular permission systems
- **Cultural Appropriation Prevention**: Automated protection systems
- **Traditional Authority Integration**: Formal community governance

### Database Service

```rust
// SQLite database management with cultural schema
pub struct DatabaseService {
    pool: SqlitePool,
    migration_manager: MigrationManager,
    cultural_schema: CulturalSchemaManager,
}

// Database schema aligned with cultural requirements
CREATE TABLE documents (
    id INTEGER PRIMARY KEY,
    content_hash TEXT UNIQUE NOT NULL,
    title TEXT NOT NULL,
    authors TEXT,
    language TEXT,
    format TEXT NOT NULL,
    file_size INTEGER NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,

    -- Cultural metadata
    cultural_classification TEXT,
    community_origin TEXT,
    traditional_knowledge_level INTEGER DEFAULT 0,
    sacred_content_flag BOOLEAN DEFAULT FALSE,
    access_restrictions TEXT,
    elder_approval_status TEXT
);

CREATE TABLE cultural_permissions (
    id INTEGER PRIMARY KEY,
    document_id INTEGER REFERENCES documents(id),
    community_id TEXT NOT NULL,
    permission_level TEXT NOT NULL,
    granted_by TEXT,
    granted_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    expires_at DATETIME,
    conditions TEXT
);

CREATE TABLE community_governance (
    id INTEGER PRIMARY KEY,
    community_id TEXT UNIQUE NOT NULL,
    governance_structure TEXT NOT NULL,
    contact_info TEXT,
    cultural_protocols TEXT,
    active_status BOOLEAN DEFAULT TRUE
);
```

#### Features:

- **Document Metadata**: Comprehensive document information
- **Cultural Schema**: Traditional knowledge classification
- **Permission System**: Community-based access control
- **Governance Integration**: Community structure data
- **Search Optimization**: Full-text search capabilities

---

## Layer 3: Frontend Services (SolidJS)

### Application State Management

```typescript
// SolidJS stores for application state
import { createStore, createMemo } from "solid-js/store";
import { createSignal, createEffect } from "solid-js";

// Document management state
export const [documentStore, setDocumentStore] = createStore({
  documents: [] as Document[],
  collections: [] as Collection[],
  searchResults: [] as Document[],
  activeDocument: null as Document | null,
  culturalFilters: {
    respectSacredContent: true,
    communityRestrictions: true,
    elderApprovalRequired: false,
  },
});

// P2P network state
export const [networkStore, setNetworkStore] = createStore({
  connectionStatus: "disconnected" as NetworkStatus,
  connectedPeers: [] as Peer[],
  sharedContent: [] as SharedContent[],
  networkHealth: {
    bandwidth: 0,
    latency: 0,
    activeConnections: 0,
  },
});

// Cultural protection state
export const [culturalStore, setCulturalStore] = createStore({
  userCommunityMembership: [] as CommunityMembership[],
  accessibleContent: [] as string[],
  pendingPermissions: [] as PermissionRequest[],
  culturalSettings: {
    language: "en",
    culturalContext: null as CulturalContext | null,
    respectTraditionalProtocols: true,
  },
});
```

### UI Component Architecture

```typescript
// Main application shell
export function AppShell() {
  return (
    <div class="app-shell">
      <NavigationHeader />
      <div class="app-content">
        <Sidebar />
        <MainContent />
      </div>
      <StatusBar />
      <CulturalProtectionOverlay />
    </div>
  );
}

// Document management interface
export function DocumentManager() {
  const [selectedDocument, setSelectedDocument] = createSignal<Document | null>(
    null
  );

  return (
    <div class="document-manager">
      <DocumentImport />
      <DocumentList onSelect={setSelectedDocument} />
      {selectedDocument() && (
        <DocumentPreview
          document={selectedDocument()!}
          culturalContext={culturalStore.culturalSettings.culturalContext}
        />
      )}
      <CulturalMetadataPanel document={selectedDocument()} />
    </div>
  );
}

// P2P network interface
export function NetworkInterface() {
  return (
    <div class="network-interface">
      <NetworkStatus />
      <PeerList />
      <ContentSharing />
      <CommunityGovernancePanel />
    </div>
  );
}
```

#### Features:

- **Reactive State**: Real-time UI updates with SolidJS reactivity
- **Cultural Context**: UI adaptation based on cultural settings
- **Accessibility**: WCAG 2.1 AA compliance
- **Multi-language**: Dynamic language switching
- **Responsive Design**: Mobile and desktop optimization

### Tauri Command Integration

```typescript
// Frontend integration with Rust backend
import { invoke } from "@tauri-apps/api/tauri";

// Document management commands
export async function importDocument(
  filePath: string,
  metadata: DocumentMetadata
): Promise<DocumentId> {
  return await invoke("import_document", { filePath, metadata });
}

export async function searchDocuments(query: SearchQuery): Promise<Document[]> {
  return await invoke("search_documents", { query });
}

// P2P network commands
export async function startNetwork(): Promise<void> {
  return await invoke("start_network");
}

export async function shareContent(
  contentId: string,
  permissions: SharingPermissions
): Promise<void> {
  return await invoke("share_content", { contentId, permissions });
}

// Cultural protection commands
export async function verifyCulturalPermissions(
  contentId: string
): Promise<AccessLevel> {
  return await invoke("verify_cultural_permissions", { contentId });
}

export async function requestElderApproval(
  contentId: string,
  reason: string
): Promise<ApprovalRequest> {
  return await invoke("request_elder_approval", { contentId, reason });
}
```

---

## Layer 4: Data & Content Layer

### Content Addressing System

```rust
// IPFS integration for content-addressed storage
pub struct ContentAddressingSystem {
    ipfs_client: IpfsClient,
    local_cache: LruCache<ContentId, Content>,
    cultural_index: CulturalContentIndex,
}

impl ContentAddressingSystem {
    pub async fn store_content(&self, content: &[u8], metadata: &ContentMetadata) -> Result<ContentId> {
        // Generate content hash
        let content_hash = self.generate_content_hash(content);

        // Apply cultural protection
        if metadata.requires_cultural_protection {
            return self.store_protected_content(content, metadata, content_hash).await;
        }

        // Store to IPFS
        let cid = self.ipfs_client.add(content).await?;

        // Update local index
        self.cultural_index.index_content(&cid, metadata).await?;

        Ok(ContentId::from(cid))
    }

    pub async fn retrieve_content(&self, content_id: &ContentId, requester: &User) -> Result<Content> {
        // Check cultural access permissions
        if !self.cultural_index.can_access(content_id, requester).await? {
            return Err(ContentError::CulturalAccessDenied);
        }

        // Try local cache first
        if let Some(content) = self.local_cache.get(content_id) {
            return Ok(content.clone());
        }

        // Retrieve from IPFS network
        let content = self.ipfs_client.get(&content_id.to_cid()).await?;

        // Cache for future access
        self.local_cache.put(*content_id, content.clone());

        Ok(content)
    }
}
```

### Database Schema Architecture

```sql
-- Core document storage schema
CREATE TABLE documents (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    content_id TEXT UNIQUE NOT NULL, -- IPFS CID
    title TEXT NOT NULL,
    description TEXT,
    authors TEXT, -- JSON array
    languages TEXT, -- JSON array
    formats TEXT NOT NULL, -- JSON array of supported formats
    file_size INTEGER NOT NULL,
    page_count INTEGER,
    publication_date DATE,
    isbn TEXT,
    doi TEXT,

    -- Cultural metadata
    cultural_origin TEXT, -- Community or culture of origin
    traditional_knowledge_type TEXT,
    cultural_sensitivity_level INTEGER DEFAULT 0, -- 0=public, 5=sacred
    requires_elder_approval BOOLEAN DEFAULT FALSE,
    community_permissions TEXT, -- JSON array of permitted communities
    cultural_context TEXT, -- Additional cultural context

    -- Technical metadata
    content_hash TEXT UNIQUE NOT NULL,
    mime_type TEXT NOT NULL,
    encryption_status TEXT DEFAULT 'none',
    availability_status TEXT DEFAULT 'local',

    -- Timestamps
    imported_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    last_accessed DATETIME,
    last_modified DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- P2P network and sharing
CREATE TABLE peer_connections (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    peer_id TEXT NOT NULL,
    peer_address TEXT NOT NULL,
    connection_status TEXT NOT NULL,
    community_affiliation TEXT,
    trust_level INTEGER DEFAULT 0,
    bandwidth_limit INTEGER,
    connected_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    last_seen DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE content_sharing (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    content_id TEXT NOT NULL REFERENCES documents(content_id),
    shared_with_peer TEXT NOT NULL,
    sharing_permissions TEXT NOT NULL, -- JSON
    cultural_restrictions TEXT, -- JSON
    shared_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    expires_at DATETIME,
    download_count INTEGER DEFAULT 0
);

-- Cultural governance and permissions
CREATE TABLE communities (
    id TEXT PRIMARY KEY, -- Community identifier
    name TEXT NOT NULL,
    description TEXT,
    governance_structure TEXT NOT NULL, -- JSON
    cultural_protocols TEXT, -- JSON
    contact_information TEXT, -- JSON
    geographical_region TEXT,
    language_codes TEXT, -- JSON array
    traditional_authorities TEXT, -- JSON array
    active_status BOOLEAN DEFAULT TRUE,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE cultural_permissions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    content_id TEXT NOT NULL REFERENCES documents(content_id),
    community_id TEXT NOT NULL REFERENCES communities(id),
    permission_type TEXT NOT NULL, -- view, download, share, modify
    permission_level TEXT NOT NULL, -- public, community, restricted, sacred
    granted_by TEXT, -- Authority who granted permission
    approval_process TEXT, -- Description of approval process
    conditions TEXT, -- Special conditions or restrictions
    granted_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    expires_at DATETIME,
    active_status BOOLEAN DEFAULT TRUE
);

-- Search and discovery
CREATE VIRTUAL TABLE documents_fts USING fts5(
    title, description, authors, content_text, cultural_keywords,
    content='documents', content_id='id'
);

-- Collections and organization
CREATE TABLE collections (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    owner_type TEXT NOT NULL, -- user, community, system
    owner_id TEXT NOT NULL,
    collection_type TEXT NOT NULL, -- manual, smart, cultural_pathway
    rules TEXT, -- JSON rules for smart collections
    cultural_context TEXT, -- Cultural significance or context
    visibility TEXT DEFAULT 'private', -- private, community, public
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE collection_documents (
    collection_id INTEGER NOT NULL REFERENCES collections(id),
    document_id INTEGER NOT NULL REFERENCES documents(id),
    added_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    cultural_relationship TEXT, -- How this document relates culturally
    PRIMARY KEY (collection_id, document_id)
);
```

---

## Integration Architecture

### Tauri Command Layer

```rust
// Tauri commands bridging frontend and backend
use tauri::{command, State};

#[command]
pub async fn import_document(
    file_path: String,
    metadata: DocumentMetadata,
    document_manager: State<'_, DocumentManager>
) -> Result<DocumentId, String> {
    document_manager
        .import_document(&file_path, metadata)
        .await
        .map_err(|e| e.to_string())
}

#[command]
pub async fn search_documents(
    query: SearchQuery,
    document_manager: State<'_, DocumentManager>
) -> Result<Vec<Document>, String> {
    document_manager
        .search_documents(&query)
        .await
        .map_err(|e| e.to_string())
}

#[command]
pub async fn start_p2p_network(
    network_service: State<'_, P2PNetworkService>
) -> Result<(), String> {
    network_service
        .lock()
        .await
        .start_network()
        .await
        .map_err(|e| e.to_string())
}

#[command]
pub async fn verify_cultural_permissions(
    content_id: String,
    user_context: UserContext,
    cultural_service: State<'_, CulturalProtectionService>
) -> Result<AccessLevel, String> {
    cultural_service
        .verify_cultural_permissions(&content_id, &user_context)
        .await
        .map_err(|e| e.to_string())
}
```

### Event System Architecture

```rust
// Event-driven architecture for real-time updates
use tauri::{Manager, Window};
use serde_json::json;

pub struct EventManager {
    app_handle: tauri::AppHandle,
}

impl EventManager {
    pub async fn emit_document_imported(&self, document: &Document) {
        self.app_handle.emit_all("document-imported", json!({
            "document": document,
            "timestamp": chrono::Utc::now()
        })).ok();
    }

    pub async fn emit_peer_connected(&self, peer: &Peer) {
        self.app_handle.emit_all("peer-connected", json!({
            "peer_id": peer.id,
            "peer_info": peer,
            "timestamp": chrono::Utc::now()
        })).ok();
    }

    pub async fn emit_cultural_alert(&self, alert: &CulturalAlert) {
        self.app_handle.emit_all("cultural-alert", json!({
            "alert_type": alert.alert_type,
            "message": alert.message,
            "severity": alert.severity,
            "requires_action": alert.requires_action
        })).ok();
    }
}
```

---

## Security Architecture

### Content Security

```rust
// Content verification and integrity
pub struct ContentSecurityManager {
    signature_service: DigitalSignatureService,
    encryption_service: EncryptionService,
    cultural_guard: CulturalProtectionService,
}

impl ContentSecurityManager {
    pub async fn verify_content_integrity(&self, content: &Content, signature: &Signature) -> Result<bool> {
        // Verify digital signature
        let signature_valid = self.signature_service.verify(content, signature).await?;

        // Check cultural authenticity if required
        if content.metadata.requires_cultural_verification {
            let cultural_valid = self.cultural_guard.verify_cultural_authenticity(content).await?;
            return Ok(signature_valid && cultural_valid);
        }

        Ok(signature_valid)
    }

    pub async fn encrypt_sacred_content(&self, content: &Content, community: &CommunityContext) -> Result<EncryptedContent> {
        // Use community-specific encryption keys
        let encryption_key = self.get_community_encryption_key(community).await?;
        self.encryption_service.encrypt(content, &encryption_key).await
    }
}
```

### Network Security

```rust
// P2P network security protocols
pub struct NetworkSecurityManager {
    trust_system: TrustManagementSystem,
    rate_limiter: RateLimiter,
    blacklist_manager: BlacklistManager,
}

impl NetworkSecurityManager {
    pub async fn authenticate_peer(&self, peer_id: &PeerId) -> Result<AuthenticationResult> {
        // Check if peer is blacklisted
        if self.blacklist_manager.is_blacklisted(peer_id).await? {
            return Ok(AuthenticationResult::Rejected("Blacklisted peer".to_string()));
        }

        // Evaluate trust score
        let trust_score = self.trust_system.evaluate_peer(peer_id).await?;

        if trust_score >= TrustThreshold::Minimum {
            Ok(AuthenticationResult::Accepted(trust_score))
        } else {
            Ok(AuthenticationResult::Rejected("Insufficient trust score".to_string()))
        }
    }
}
```

---

## Performance Architecture

### Caching Strategy

```rust
// Multi-layer caching system
pub struct CacheManager {
    memory_cache: Arc<Mutex<LruCache<String, CachedItem>>>,
    disk_cache: DiskCache,
    network_cache: NetworkCache,
}

impl CacheManager {
    pub async fn get_content(&self, content_id: &str) -> Option<Content> {
        // Try memory cache first (fastest)
        if let Some(content) = self.memory_cache.lock().await.get(content_id) {
            return Some(content.data.clone());
        }

        // Try disk cache (fast)
        if let Ok(content) = self.disk_cache.get(content_id).await {
            // Promote to memory cache
            self.memory_cache.lock().await.put(content_id.to_string(), CachedItem::new(content.clone()));
            return Some(content);
        }

        // Try network cache (slower)
        if let Ok(content) = self.network_cache.get(content_id).await {
            // Cache to disk and memory
            self.disk_cache.put(content_id, &content).await.ok();
            self.memory_cache.lock().await.put(content_id.to_string(), CachedItem::new(content.clone()));
            return Some(content);
        }

        None
    }
}
```

### Database Optimization

```sql
-- Performance optimization indexes
CREATE INDEX idx_documents_cultural_origin ON documents(cultural_origin);
CREATE INDEX idx_documents_sensitivity_level ON documents(cultural_sensitivity_level);
CREATE INDEX idx_documents_content_hash ON documents(content_hash);
CREATE INDEX idx_documents_imported_at ON documents(imported_at);

CREATE INDEX idx_cultural_permissions_content_community ON cultural_permissions(content_id, community_id);
CREATE INDEX idx_cultural_permissions_active ON cultural_permissions(active_status, expires_at);

CREATE INDEX idx_peer_connections_status ON peer_connections(connection_status, last_seen);
CREATE INDEX idx_content_sharing_content_peer ON content_sharing(content_id, shared_with_peer);

-- Query optimization for common searches
CREATE VIEW active_documents AS
SELECT d.*, cp.community_id, cp.permission_level
FROM documents d
LEFT JOIN cultural_permissions cp ON d.content_id = cp.content_id
WHERE cp.active_status = TRUE OR cp.id IS NULL;
```

---

## Deployment Architecture

### Build Configuration

```toml
# Cargo.toml - Rust backend dependencies
[package]
name = "allibrary"
version = "0.1.0"
edition = "2021"

[dependencies]
tauri = { version = "2.0", features = ["api-all"] }
serde = { version = "1.0", features = ["derive"] }
tokio = { version = "1.0", features = ["full"] }
sqlx = { version = "0.7", features = ["runtime-tokio-native-tls", "sqlite"] }
libp2p = { version = "0.53", features = ["tcp", "mdns", "noise", "yamux", "gossipsub", "kad"] }
ipfs-api-backend-hyper = "0.6"
tracing = "0.1"
tracing-subscriber = "0.3"

[build-dependencies]
tauri-build = { version = "2.0", features = [] }
```

```json
// package.json - Frontend dependencies
{
  "name": "allibrary-frontend",
  "version": "0.1.0",
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "tauri": "tauri"
  },
  "dependencies": {
    "solid-js": "^1.8.0",
    "@tauri-apps/api": "^2.0.0",
    "@tauri-apps/plugin-fs": "^2.0.0",
    "@tauri-apps/plugin-dialog": "^2.0.0"
  },
  "devDependencies": {
    "vite": "^5.0.0",
    "vite-plugin-solid": "^2.8.0",
    "typescript": "^5.2.0",
    "@types/node": "^20.0.0",
    "vitest": "^1.0.0"
  }
}
```

### Distribution Strategy

```rust
// Cross-platform build configuration
// tauri.conf.json configuration for different platforms

{
  "build": {
    "beforeBuildCommand": "npm run build",
    "beforeDevCommand": "npm run dev",
    "devPath": "http://localhost:5173",
    "distDir": "../dist"
  },
  "package": {
    "productName": "AlLibrary",
    "version": "0.1.0",
    "description": "Decentralized Cultural Knowledge Platform",
    "authors": ["AlLibrary Team"],
    "license": "MIT"
  },
  "tauri": {
    "allowlist": {
      "all": false,
      "fs": {
        "all": true,
        "scope": ["$DOCUMENT/*", "$DOWNLOAD/*", "$HOME/.allibrary/*"]
      },
      "shell": {
        "all": false,
        "open": true
      },
      "dialog": {
        "all": true
      },
      "notification": {
        "all": true
      }
    },
    "bundle": {
      "active": true,
      "targets": ["deb", "appimage", "nsis", "dmg"],
      "identifier": "org.allibrary.app",
      "icon": [
        "icons/32x32.png",
        "icons/128x128.png",
        "icons/128x128@2x.png",
        "icons/icon.icns",
        "icons/icon.ico"
      ]
    },
    "security": {
      "csp": "default-src 'self'; connect-src ipc: https://tauri.localhost http://localhost:5173"
    }
  }
}
```

---

## Cultural Integration Architecture

### Community Governance Integration

```rust
// Integration with traditional governance systems
pub struct CommunityGovernanceIntegration {
    governance_protocols: HashMap<CommunityId, GovernanceProtocol>,
    decision_making_systems: DecisionMakingSystems,
    elder_council_interface: ElderCouncilInterface,
}

impl CommunityGovernanceIntegration {
    pub async fn make_community_decision(&self, proposal: &GovernanceProposal) -> Result<DecisionResult> {
        let community = &proposal.community_id;
        let protocol = self.governance_protocols.get(community)
            .ok_or(GovernanceError::UnknownCommunity)?;

        match &protocol.decision_making_type {
            DecisionMakingType::ElderCouncil => {
                self.elder_council_interface.submit_for_decision(proposal).await
            },
            DecisionMakingType::Consensus => {
                self.decision_making_systems.consensus_process(proposal).await
            },
            DecisionMakingType::Traditional(custom_process) => {
                self.decision_making_systems.custom_process(proposal, custom_process).await
            }
        }
    }
}
```

### Traditional Knowledge Protection

```rust
// Advanced cultural protection systems
pub struct TraditionalKnowledgeProtection {
    sacred_content_detector: SacredContentAI,
    cultural_context_analyzer: CulturalContextAnalyzer,
    community_verification: CommunityVerificationSystem,
}

impl TraditionalKnowledgeProtection {
    pub async fn analyze_content_cultural_significance(&self, content: &Content) -> Result<CulturalAnalysis> {
        // AI-assisted detection of culturally significant content
        let ai_analysis = self.sacred_content_detector.analyze(content).await?;

        // Cultural context analysis
        let context_analysis = self.cultural_context_analyzer.analyze(content).await?;

        // Community verification if needed
        let verification = if ai_analysis.requires_community_verification {
            Some(self.community_verification.verify(content, &ai_analysis.suspected_community).await?)
        } else {
            None
        };

        Ok(CulturalAnalysis {
            ai_analysis,
            context_analysis,
            community_verification: verification,
            protection_level: self.determine_protection_level(&ai_analysis, &context_analysis).await?,
        })
    }
}
```

---

This technical architecture specification aligns with AlLibrary's actual technology stack (Tauri v2 + SolidJS + Rust + libp2p + SQLite) and the 8-phase development structure. It provides a comprehensive foundation for the technical implementation while maintaining the cultural sensitivity and community-centered approach that defines the project.
