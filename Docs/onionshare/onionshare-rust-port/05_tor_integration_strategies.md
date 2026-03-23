# Tor Integration Strategies

## Strategy A: Extend Existing tor_manager

### Overview

AlLibrary already uses the Tor control protocol (`ADD_ONION`, cookie auth) via `tor_manager.rs`. This strategy extends that infrastructure to host an Axum HTTP server behind a hidden service.

### Flow

1. **Pick a local port**: Use `pick_free_port()` (or similar) to bind Axum to `127.0.0.1:local_port`.
2. **Create hidden service**: Call `tor_manager::create_hidden_service(local_port)`.
3. **Start Axum**: Run Axum on `127.0.0.1:local_port` with share or receive routes.
4. **Tor forwards**: Tor maps port 80 on the onion address to `127.0.0.1:local_port`.

### Pros

- No new Tor crates; minimal dependency changes
- Reuses existing Tor lifecycle (start/stop, cookie auth)
- Proven Tor binary; no Arti maturity concerns
- Smallest code surface

### Cons

- Requires Tor binary (bundled or system)
- Not a single-binary distribution

### Implementation Sketch

```rust
// In tor_manager or new onionshare module
pub async fn start_onion_share(paths: Vec<PathBuf>, ...) -> Result<OnionShareResult, String> {
    let port = pick_free_port()?;
    let app = share_routes(AppState::new(paths, ...));
    let listener = TcpListener::bind(("127.0.0.1", port)).await?;
    let (onion_id, onion_addr) = tor_manager.create_hidden_service(port).await?;
    tokio::spawn(axum::serve(listener, app));
    Ok(OnionShareResult { onion_address: onion_addr, local_port: port })
}
```

---

## Strategy B: Arti-Based (Pure Rust Tor)

### Overview

Use `arti-client` and `tor-hsservice` to run a hidden service entirely in Rust. No Tor binary required.

### Flow

1. **Bootstrap Tor**: `TorClient::create_bootstrapped(...)`.
2. **Launch onion service**: `tor_client.launch_onion_service(OnionServiceConfigBuilder::default().build()?)`.
3. **Serve Axum**: Use `arti-axum::serve(stream_requests, app)` to handle incoming streams and serve the Axum app.

### Pros

- Single binary; no external Tor process
- Pure Rust; easier cross-compilation
- No Tor binary dependency

### Cons

- Arti hidden service maturity; DoS/PoW/vanguard limitations
- Larger dependency tree
- On-disk state growth

### Implementation Sketch

```rust
let tor_client = TorClient::create_bootstrapped(TorClientConfig::default()).await?;
let (onion_service, rend_requests) = tor_client.launch_onion_service(
    OnionServiceConfigBuilder::default()
        .nickname("onionshare".to_owned().try_into().unwrap())
        .build()?,
)?;
let stream_requests = handle_rend_requests(rend_requests);
let app = share_routes(state);
arti_axum::serve(stream_requests, app).await;
```

---

## Strategy C: Hybrid

### Overview

Keep bundled Tor for control; use Axum for HTTP. Same as Strategy A but explicitly documents the split: Tor lifecycle in `tor_manager`, HTTP logic in a new `onionshare` module.

### Components

| Component | Responsibility |
|-----------|-----------------|
| `tor_manager` | Tor process, control protocol, `create_hidden_service` |
| `onionshare` | Axum app, share/receive routes, zip/gzip, multipart |
| Tauri commands | `start_onion_share`, `stop_onion_share`, etc. |

---

## Recommendation

| Phase | Strategy |
|-------|----------|
| Phase 1 (Share) | **Strategy A** – extend `tor_manager`, add Axum |
| Phase 2 (Receive) | Same |
| Phase 3+ | Evaluate **Strategy B** if single-binary becomes a requirement |

---

## Port Selection

- OnionShare uses ports 17600–17650 for local bindings
- AlLibrary uses `pick_free_port()` – align with existing logic
- Document chosen range in `tor_manager` or config

---

## Host Binding

- Default: `127.0.0.1` (localhost only)
- Whonix: OnionShare binds to `0.0.0.0` when `WHONIX` env var is set
- Add config or env var for host binding if needed: `ONIONSHARE_BIND_HOST=0.0.0.0`
