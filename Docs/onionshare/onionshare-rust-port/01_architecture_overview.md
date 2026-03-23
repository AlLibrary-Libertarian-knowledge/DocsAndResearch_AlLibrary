# Architecture Overview

## High-Level Architecture

```mermaid
flowchart TB
    subgraph Frontend [SolidJS Frontend]
        ShareUI[Share UI]
        ReceiveUI[Receive UI]
    end

    subgraph Tauri [Tauri Commands]
        StartShare[start_onion_share]
        StopShare[stop_onion_share]
        StartReceive[start_onion_receive]
        StopReceive[stop_onion_receive]
    end

    subgraph HTTP [HTTP Server Layer]
        Axum[Axum Router]
        ShareMode[Share Mode]
        ReceiveMode[Receive Mode]
    end

    subgraph Tor [Tor Layer]
        TorManager[tor_manager]
        TorProcess[Tor Process]
    end

    subgraph Data [Data Layer]
        LocalFiles[Local Files]
        ReceiveDir[Receive Directory]
    end

    ShareUI --> StartShare
    ReceiveUI --> StartReceive
    StartShare --> Axum
    StartReceive --> Axum
    Axum --> ShareMode
    Axum --> ReceiveMode
    ShareMode --> LocalFiles
    ReceiveMode --> ReceiveDir
    StartShare --> TorManager
    TorManager --> TorProcess
    TorProcess -->|port 80| Axum
```

## Data Flow: Share Mode

```mermaid
sequenceDiagram
    participant User
    participant Tauri
    participant TorManager
    participant Axum
    participant Tor

    User->>Tauri: start_onion_share(paths)
    Tauri->>Axum: Start server on port P
    Tauri->>TorManager: create_hidden_service(P)
    TorManager->>Tor: ADD_ONION Port=80,127.0.0.1:P
    Tor-->>TorManager: ServiceID=abc123.onion
    TorManager-->>Tauri: http://abc123.onion
    Tauri-->>User: onion_url

    Note over User,Tor: Recipient visits http://abc123.onion
    User->>Tor: GET / (via Tor)
    Tor->>Axum: Forward to 127.0.0.1:P
    Axum-->>User: Directory listing or download
```

## Data Flow: Receive Mode

```mermaid
sequenceDiagram
    participant Sender
    participant Tor
    participant Axum
    participant Tauri
    participant Disk

    Sender->>Tor: POST /upload (multipart)
    Tor->>Axum: Forward to local port
    Axum->>Disk: Save to {data_dir}/{date}/{time}/
    Axum-->>Sender: Redirect or JSON response
    Axum->>Tauri: Emit progress event
    Tauri-->>Frontend: onion-share-progress
```

## Component Mapping: OnionShare Python → Rust

| OnionShare Python | Rust Module / Crate |
|-------------------|---------------------|
| `onion.py` (Tor control) | `tor_manager.rs` (existing) | 
| `onionshare.py` (orchestrator) | `onion_share.rs` (new) |
| `web/web.py` (Flask) | `axum` + custom routes |
| `web/share_mode.py` | `share_mode.rs` or `share_routes.rs` |
| `web/receive_mode.py` | `receive_mode.rs` or `receive_routes.rs` |
| `web/send_base_mode.py` | Shared utilities in `share_common.rs` |
| `common.py` (port, password, etc.) | `utils.rs` or `common.rs` |
| `mode_settings.py` | `Settings` struct or `AppState` |
| `ZipWriter` | `zip` crate |
| `Waitress` | `axum::serve` with `tokio` |

## Integration with Existing AlLibrary

### tor_manager.rs

AlLibrary already implements:

- **Tor lifecycle**: `start()`, `stop()`, `status()`
- **Hidden service creation**: `create_hidden_service(local_port)` → `{id}.onion`
- **Control protocol**: Cookie auth, `ADD_ONION NEW:ED25519-V3`
- **Bridges**: `enable_bridges()`

Location: `DesktopApp_AlLibrary/src-tauri/src/core/p2p/tor_manager.rs`

### Option: Extend vs Replace

| Approach | Pros | Cons |
|----------|------|------|
| **Extend tor_manager** | No new Tor crates; proven control protocol | Stays with Tor binary; no pure-Rust Tor |
| **Replace with Arti** | Pure Rust; no Tor binary | Larger deps; Arti HS maturity |

**Recommendation**: Extend `tor_manager` for Phase 1. Add Axum HTTP server that binds to a port returned by `pick_free_port()`, then call `create_hidden_service(port)`.

## Module Structure (Proposed)

```
src-tauri/src/
├── core/
│   └── p2p/
│       ├── tor_manager.rs      # Existing
│       └── onion_share/        # New
│           ├── mod.rs
│           ├── share.rs        # Share mode routes
│           ├── receive.rs      # Receive mode routes
│           ├── common.rs       # Security headers, utils
│           └── state.rs        # AppState, shutdown
├── commands/
│   ├── tor.rs                  # Existing
│   └── onion_share.rs          # New: start_onion_share, etc.
```

## Port Selection

- **OnionShare**: Uses port range 17600–17650
- **AlLibrary tor_manager**: Uses `pick_free_port()` (any available port)
- **Alignment**: Consider using 17600–17650 for onion share/receive to avoid conflicts with other services. Document in `common.rs`:

```rust
const ONION_SHARE_PORT_MIN: u16 = 17600;
const ONION_SHARE_PORT_MAX: u16 = 17650;
```

## Host Binding

- **Default**: Bind to `127.0.0.1` (localhost only; Tor forwards to it)
- **Whonix**: OnionShare binds to `0.0.0.0` when `/usr/share/anon-ws-base-files/workstation` exists
- **Config**: Add env var or config: `ONION_SHARE_BIND_HOST` (default `127.0.0.1`)
