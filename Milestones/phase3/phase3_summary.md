
---

### Phase 3 – Tor Overlay Architecture & Implementation Plan (Deep Dive)

This appendix specifies how we will use Tor as the transport overlay so every AlLibrary node exposes an onion service and all P2P interactions traverse Tor end-to-end. This aligns with our anti-censorship and decentralization requirements and replaces NAT traversal complexity with onion addressing.

References:
- Tor Control/Stem API (controller, control socket, descriptors) – [Stem API](https://stem.torproject.org/api.html)
- Tor C public API (embedding/controlling tor) – [tor_api.h](https://tpo.pages.torproject.net/core/doc/tor/tor__api_8h.html)

#### Goals
- Each app instance has a unique v3 onion service address (peer ID).
- All peer connections, search requests, and content fetches use onion circuits (SOCKS) for anonymity and censorship resistance.
- Zero cultural access gating: cultural context is informational only; search, replication, and transfer are never blocked based on cultural factors.

#### Architecture Overview
```
+---------------------+           +--------------------+
| AlLibrary Frontend  |  Tauri    |  Tauri Backend     |
| (SolidJS)           |<--------->|  (Rust)            |
| - SearchNetwork UI  |  commands |  - Tor Manager     |
| - Settings/Network  |           |    (Arti or tor)   |
| - P2P status        |           |  - Onion Service   |
+---------------------+           |  - HTTP mini-svc   |
                                  |  - IPFS/P2P glue   |
                                  +--------------------+
                                           |
                                           |  SOCKS5 (127.0.0.1:9050/9150) or embedded Tor client
                                           v
                                   Tor Network (v3 onion)
                                           |
                                           v
                               Peers (onion services)
```

Implementation choices (ranked):
1) Embedded Tor client (Rust Arti) managed by Tauri (no external dependency) – control via Rust APIs.
2) Spawn tor.exe/tor binary and control via Tor Control Protocol (Stem-equivalent logic, but in Rust) – stable, cross-platform.
3) Tor C API (tor_api.h) embedded – viable but heavier operationally on Windows.

We will start with 1) or 2) to avoid shipping Python for Stem and to keep the desktop footprint coherent. The API surface remains compatible with Stem concepts (control socket, hidden service, circuit rotation) should we switch later.

#### Backend (Tauri/Rust) Modules & Commands
- `src-tauri/src/network/tor.rs`
  - start_tor(config): boot client (Arti or tor process + control)
  - get_tor_status(): { bootstrapped, circuitEstablished, bridgesEnabled, socks }
  - enable_bridges(list): configure pluggable transports/bridges
  - use_socks(addr): switch to Tor Browser SOCKS (9150) if user prefers
  - create_hidden_service({ local_port }): returns onion v3 address
  - list_hidden_services(): enumerate local HS
  - rotate_tor_circuit(): request new circuit
  - stop_tor()
- `src-tauri/src/network/share_server.rs`
  - Minimal read-only HTTP JSON on `127.0.0.1:<port>` for:
    - `GET /index`: node metadata + shared catalogs
    - `POST /search`: query terms -> local index hits
    - `GET /document/:id/chunk?offset&len`: chunked document transfer
- `src-tauri/src/network/onion_client.rs`
  - `fetch_via_tor(onion_url, method, body)`: issues requests via SOCKS/CIRCUITS

Command surfaces (example):
```
#[tauri::command]
async fn start_tor(cfg: TorConfig) -> TorStatus { /* ... */ }
#[tauri::command]
async fn create_hidden_service(local_port: u16) -> String { /* onion addr */ }
#[tauri::command]
async fn fetch_onion(url: String, method: String, body: Option<String>) -> Response { /* ... */ }
```

#### Peer Identity & Discovery
- Peer ID = onion v3 address; no IP/port exposure.
- Bootstrap: manual add (paste onion), recent peers cache, optional lightweight rendezvous (an onion registry you control) later.
- `get_connected_peers` returns onion IDs and basic stats; discovery can be gossip-based (peers share known peers).

#### Data Plane Protocol (over Tor)
- Transport: HTTP/JSON over Tor (SOCKS). Optionally libp2p over TCP tunneled through Tor later.
- Endpoints:
  - `/index` -> lists catalogs and minimal metadata
  - `/search` -> returns local indexed hits with cultural context fields (information only)
  - `/document/:id/chunk` -> chunked file transfer with integrity check
- Integrity: per-chunk hash; full-file hash (IPFS-compatible) advertised in `/index` and `/search`.

#### Frontend Integration (SolidJS)
- Settings → Network Panel
  - Toggle Tor overlay
  - Bridges list editor
  - Option “Use Tor Browser SOCKS (127.0.0.1:9150)”
  - Show onion address and copy button
- `SearchNetworkPage`
  - “Enable TOR Search” triggers `start_tor` → `create_hidden_service` → enable onion client
  - Display own onion address; allow “Add Peer Onion” and connect
  - Search aggregates results from known peers via `fetch_onion(peer+/search)` and merges
  - Never gate results by culture; display cultural info and educational links

#### Cultural & Anti‑Censorship Guarantees
- No cultural access control or approval gating anywhere in the network stack.
- Cultural fields are presented for education only; transport is never blocked by cultural sensitivity.
- Tor overlays provide anonymity and routing diversity to resist censorship.

#### Testing (Phase 3)
- Connectivity & reliability
  - Mock Tor control and verify bootstrap + circuit rotation
  - Connection success ≥90% under intermittent failures (already added pattern for P2P)
- Replication & availability (IPFS/HTTP over Tor)
  - Redundant copies, availability checks with anti-censorship flags (tests added)
- Distributed search
  - Aggregate results from multiple mocked onion peers; p95 < 2s on typical dataset
- Anti-censorship fallback
  - Bridges enablement path and rotation verified; search works with and without Tor Browser SOCKS

#### Security & Privacy
- Only technical security: malware/legal compliance on uploaded files remains enforced; cultural content never filtered.
- All external requests made through Tor when enabled; no leak of real IP.
- Optional Tor Browser SOCKS lets users reuse their existing Tor instance.

#### Migration/Deployment
- Windows: bundle tor binary or use Arti; default to embedded Tor; allow Tor Browser SOCKS fallback.
- Config persisted in app settings; auto-start Tor on boot if user enabled.

#### Future Enhancements
- Swap HTTP JSON for libp2p over Tor to unify with broader P2P stack.
- Add rendezvous onion directory (opt-in) for peer discovery.
- Background replication budgets and opportunistic seeding.

This plan maps directly to Milestone 3.1 (network setup), 3.2 (content distribution), and 3.3 (distributed search), while adhering to our anti-censorship and cultural information-only rules. Controller concepts are compatible with Stem’s API and Tor’s C API if we later need lower-level control.

# Phase 3: P2P Network & Distributed Architecture

## Overview

**UPDATED**: Phase 3 focuses on implementing the P2P network infrastructure with integrated cultural protocols and anti-censorship features, building upon the solid foundation established in Phases 1-2.

## Duration

- **Updated Estimate**: 3 weeks implementation
- **Start**: Week 7 (After Phase 2 completion)
- **End**: Week 9

## Prerequisites

- ✅ Phase 1 completed (architectural restructuring with cultural framework)
- ✅ Phase 2 completed (foundation components and document management)
- ✅ Cultural validation system operational
- ✅ Security infrastructure active
- ✅ Document management with cultural metadata functional

## Main Goals

1. **P2P Network Infrastructure** (Week 1)

   - Implement libp2p integration with cultural awareness
   - Create peer discovery with community validation
   - Establish secure connection protocols
   - Build network monitoring and health systems

2. **Cultural Content Distribution** (Week 2)

   - Implement culturally-aware content routing
   - Create community permission propagation
   - Build sacred content protection in transit
   - Establish cultural provenance tracking

3. **Decentralized Search & Anti-Censorship** (Week 3)
   - Implement distributed search with cultural filtering
   - Create censorship-resistant content discovery
   - Build community network resilience
   - Establish information integrity verification

## Detailed Goals

### 1. P2P Network Infrastructure

#### Network Architecture with Cultural Integration

```
P2P Network Layer:
├── libp2p Core/                     # Baseline P2P networking
├── Cultural Routing/                # Route content based on cultural permissions
├── Community Validation/            # Verify peers within cultural communities
├── Sacred Content Protection/       # Special protocols for highest sensitivity
└── Anti-Censorship Protocols/       # Resistance to network blocking
```

#### Core Network Features

- **Culturally-Aware Peer Discovery**: Find peers within cultural communities
- **Sacred Content Channels**: Encrypted, restricted channels for highest sensitivity content
- **Community Network Segments**: Separate network spaces for different cultural groups
- **Educational Content Propagation**: Spread learning materials to increase access
- **Censorship Resistance**: Multiple transport protocols and routing strategies

### 2. Cultural Content Distribution

#### Content Routing with Cultural Protocols

```typescript
// Cultural Content Distribution
const culturalContentRouting = {
  routeContent: async (
    contentHash: string,
    culturalLevel: CulturalSensitivityLevel
  ) => {
    // 1. Determine eligible peer communities
    // 2. Verify cultural permissions for each hop
    // 3. Apply sacred content protection if needed
    // 4. Track provenance and community approval chain
  },
  validateCulturalHop: async (
    peerId: string,
    contentLevel: CulturalSensitivityLevel
  ) => {
    // 1. Check peer's cultural access level
    // 2. Verify community membership if required
    // 3. Validate elder approval for sacred content
    // 4. Log cultural access for accountability
  },
};
```

#### Community Network Features

- **Cultural Community Networks**: Separate network overlays for different cultural groups
- **Elder Node Validation**: Special nodes run by community elders for approval workflows
- **Educational Content Networks**: Dedicated channels for cultural education materials
- **Sacred Content Protocols**: Ultra-secure distribution for highest sensitivity materials
- **Community Sovereignty Enforcement**: Technical enforcement of cultural access rules

### 3. Decentralized Search & Anti-Censorship

#### Distributed Search with Cultural Context

```typescript
// Culturally-Aware Distributed Search
const distributedCulturalSearch = {
  searchNetwork: async (
    query: string,
    userId: string,
    culturalContext?: string
  ) => {
    // 1. Query appropriate cultural community networks
    // 2. Aggregate results from culturally-accessible peers
    // 3. Filter by user's cultural access permissions
    // 4. Provide educational context for restricted results
  },
  validateSearchResults: async (results: SearchResult[], userId: string) => {
    // 1. Check cultural permissions for each result
    // 2. Mark educational requirements
    // 3. Identify community permission needs
    // 4. Provide cultural context and learning paths
  },
};
```

#### Anti-Censorship Features

- **Multiple Transport Protocols**: TCP, WebSocket, WebRTC for connection diversity
- **TOR Integration Preparation**: Structure for onion routing (full implementation in Phase 5)
- **Content Mirroring**: Automatic replication of important cultural and educational content
- **Network Resilience**: Automatic route-around for blocked nodes or content
- **Information Integrity Verification**: Cryptographic verification of content authenticity

## Key Deliverables

### P2P Network Infrastructure

- **libp2p Integration** with cultural community awareness
- **Peer Discovery System** respecting cultural boundaries
- **Cultural Routing Protocols** for appropriate content distribution
- **Network Health Monitoring** including cultural access metrics
- **Connection Security** with cultural identity verification

### Cultural Content Distribution

- **Community Network Overlays** for different cultural groups
- **Sacred Content Protection** with encryption and access controls
- **Cultural Provenance Tracking** maintaining chain of cultural custody
- **Educational Content Propagation** spreading learning opportunities
- **Community Sovereignty Tools** for cultural content control

### Distributed Search & Anti-Censorship

- **Culturally-Filtered Network Search** respecting access permissions
- **Censorship-Resistant Discovery** using multiple protocols and routes
- **Content Integrity Verification** preventing manipulation and ensuring authenticity
- **Community Resilience Tools** for network and content protection
- **Educational Context Integration** providing learning opportunities within search

## Technical Requirements

### Network Infrastructure

- **libp2p v0.52+**: Core P2P networking library
- **IPFS Integration**: Content addressing and distributed storage
- **WebRTC Support**: Browser-based peer connections
- **Network Monitoring**: Real-time network health and performance tracking
- **Connection Security**: TLS encryption and peer verification

### Cultural Integration

- **Cultural Metadata Propagation**: Distribute cultural context with content
- **Community Identity Verification**: Verify peer membership in cultural communities
- **Sacred Content Encryption**: Additional encryption layers for highest sensitivity
- **Educational Content Tagging**: Mark content for cultural education purposes
- **Cultural Access Logging**: Track and audit cultural content access across network

### Anti-Censorship Preparation

- **Transport Diversity**: Multiple connection methods for resilience
- **Content Replication**: Automatic backup of important content
- **Route Optimization**: Dynamic routing around blocked paths
- **Network Monitoring**: Detect and respond to censorship attempts
- **Information Integrity**: Verify content hasn't been tampered with

## Success Criteria

### Network Functionality

- [ ] P2P network establishes connections successfully
- [ ] Cultural community networks operate independently
- [ ] Peer discovery respects cultural boundaries
- [ ] Content routing follows cultural protocols
- [ ] Network monitoring provides comprehensive visibility

### Cultural Protocol Compliance

- [ ] Sacred content remains within approved cultural boundaries
- [ ] Educational content propagates appropriately to increase access
- [ ] Community sovereignty is technically enforced
- [ ] Cultural provenance tracking maintains chain of custody
- [ ] Elder approval workflows function across network

### Anti-Censorship Effectiveness

- [ ] Network maintains connectivity under simulated blocking
- [ ] Content discovery works through multiple routes
- [ ] Information integrity verification prevents manipulation
- [ ] Community resilience tools protect against attacks
- [ ] Multiple transport protocols provide redundancy

### Performance Standards

- [ ] Network search response time <2 seconds
- [ ] Content distribution maintains 90%+ reliability
- [ ] Cultural validation adds <100ms latency
- [ ] Network supports 1000+ concurrent peers
- [ ] Content integrity verification success rate >99%

## Cultural Framework Integration

### Community Network Governance

- **Cultural Community Councils**: Technical representation of cultural governance
- **Elder Node Network**: Special nodes operated by community elders
- **Educational Content Curation**: Community-driven educational material selection
- **Sacred Content Guardianship**: Technical implementation of cultural protection protocols
- **Community Sovereignty Enforcement**: Network-level enforcement of cultural access rules

### Protection Mechanisms

- **Multi-Layer Sacred Content Protection**: Encryption, access controls, and audit trails
- **Cultural Context Preservation**: Maintain meaning and significance during distribution
- **Community Permission Propagation**: Spread approval decisions across network
- **Educational Gatekeeping**: Ensure educational requirements before cultural access
- **Cultural Integrity Verification**: Verify content hasn't been altered or misrepresented

## Risk Management

### Network Risks

- **Scalability Challenges**: P2P networks face complexity growth
- **Cultural Protocol Overhead**: Cultural validation may impact performance
- **Network Partitioning**: Cultural boundaries might fragment network
- **Malicious Peers**: Bad actors could exploit cultural protocols
- **Content Propagation Issues**: Cultural restrictions might limit beneficial distribution

### Mitigation Strategies

- **Gradual Scaling**: Start with small communities and grow organically
- **Optimized Cultural Validation**: Efficient algorithms for cultural checks
- **Bridge Nodes**: Special nodes that connect different cultural networks
- **Reputation Systems**: Track peer behavior and cultural protocol compliance
- **Flexible Cultural Policies**: Allow communities to adjust restrictions as needed

### Cultural Risks

- **Digital Divide**: P2P complexity might exclude some community members
- **Cultural Misrepresentation**: Network distribution might lose cultural context
- **Technology Resistance**: Some communities might reject P2P technology
- **Elder Participation**: Technical barriers might prevent elder engagement
- **Cultural Appropriation**: P2P distribution might enable inappropriate use

### Cultural Mitigation

- **Community Education**: Training programs for P2P technology use
- **Cultural Context Preservation**: Rich metadata maintains meaning
- **Community Partnership**: Work directly with cultural leaders
- **Elder-Friendly Interfaces**: Simplified tools for elder participation
- **Usage Monitoring**: Track and prevent inappropriate cultural content use

---

## 🌐 DECENTRALIZED CULTURAL PRESERVATION NOTICE

**Phase 3 creates the world's first culturally-aware P2P network:**

- **Cultural communities control their content** through technical sovereignty
- **Sacred materials receive unprecedented protection** through multi-layer security
- **Educational opportunities expand** through decentralized content distribution
- **Censorship resistance preserves cultural heritage** against suppression attempts
- **Information integrity protects** against manipulation and misrepresentation

**This phase proves that decentralized technology can enhance rather than threaten cultural sovereignty.**

---

## Execution Blueprint (Append-Only)

1) P2P Networking Core
- Integrate libp2p with identity, transports (TCP/WebSocket/WebRTC), connection management.
- Health metrics API exposed to UI; no cultural gating in network paths.

2) Content Distribution
- IPFS addressing; replication strategies; integrity verification.
- Attach cultural metadata (context, sources) alongside content as descriptive info; do not enforce access logic.

3) Network Search (Foundations)
- Prototype distributed query/aggregation; present cultural labels and educational context with results.

## Integration Map

- Services: `network/*`, `services/api/*` for Tauri commands.
- UI: PeerNetwork, P2PSearch pages; add NetworkHealth widgets.
- Docs: reference `04_System_Architecture_Diagrams.md` flows (interpret cultural steps as info-only).

## Acceptance Criteria (Phase 3)

- Peers connect reliably across at least two transports; integrity checks pass.
- Content distribution replicates and verifies using hashes; metadata includes cultural context as information.
- Network search demo aggregates results with cultural labels; no access filtering.

## Test Plan

- Unit: address/identity utilities, integrity verifiers.
- Integration: multi-transport connections, replication success, result aggregation.
- Resilience: simulate blocked routes; verify alternate paths (anti-censorship goal).

## Performance Budgets

- Connection setup < 500ms median; replication reliability ≥ 90% lab conditions.
- Validation overhead (integrity + metadata attach) < 100ms per item.

## Cultural Info-Only Guardrails (Overrides)

- Replace any “community/elder approval”, “permission propagation”, or “sacred channels” as enforcement with information distribution and transparency only.
- Provide educational context and provenance; never block routing based on culture.

## Progress Tracking

- Track: peer counts, connection success rate, replication reliability, search latency.
- Update progress docs after each network milestone.

## References

- Architecture: `04_System_Architecture_Diagrams.md`
- Workflow: `01_IMPLEMENTATION_WORKFLOW_GUIDE.md`
- Rules: `.cursor/rules/allibrary-*.mdc`