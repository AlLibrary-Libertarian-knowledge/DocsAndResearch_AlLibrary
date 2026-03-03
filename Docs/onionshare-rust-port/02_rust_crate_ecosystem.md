# Rust Crate Ecosystem

## Tor / Hidden Services

### tor-hsservice

- **Crate**: `tor-hsservice` (official Arti project)
- **Purpose**: Low-level onion service protocol implementation
- **Key types**: `OnionServiceBuilder`, `RunningOnionService`, `StreamRequest`, `HsId`
- **Limitations** (as of Feb 2024):
  - No resistance to denial of service attacks
  - No proof-of-work checking
  - No detection/response to out-of-memory conditions
  - Vanguard relays for path discovery resistance not yet complete
  - On-disk state grows without bound

### arti-client

- **Crate**: `arti-client`
- **Purpose**: High-level Tor client; can launch onion services
- **API**: `TorClient::launch_onion_service(OnionServiceConfigBuilder::default().build()?)`
- **Use case**: Pure Rust Tor without Tor binary

### arti-axum

- **Crate**: `arti-axum` (v0.1.0)

- **Purpose**: Serve an Axum app as a Tor hidden service
- **Example**:

```rust
let tor_client = TorClient::create_bootstrapped(TorClientConfig::default()).await?;
let (onion_service, rend_requests) = tor_client.launch_onion_service(
    OnionServiceConfigBuilder::default()
        .nickname("hello-world".to_owned().try_into().unwrap())
        .build()?,
)?;
let stream_requests = handle_rend_requests(rend_requests);
let app = Router::new().route("/", get(|| async { "Hello, World!" }));
println!("serving at: http://{}", onion_service.onion_name().unwrap());
arti_axum::serve(stream_requests, app).await;
```

- **Dependencies**: axum, tor-hsservice, tor-proto, tor-cell, hyper, tokio, tower

### ephemeral-arti

- **URL**: https://github.com/acheong08/ephemeral-arti
- **Purpose**: Fork of Arti with ephemeral/in-memory hidden services
- **License**: Apache-2.0, MIT

### Recommendation for Phase 1

Use **existing tor_manager** (Tor control protocol) rather than Arti. Add Arti as an option in a later phase if single-binary distribution becomes a priority.

---

## HTTP Server

### axum

- **Crate**: `axum` (recommended)
- **Purpose**: Async HTTP framework; routing, extractors, middleware
- **Features**:
  - `Router::new().route("/", get(handler))`
  - `axum::extract::Multipart` for file uploads
  - `axum::response::Stream` for chunked streaming
  - `State<T>` for shared state
  - `Json`, `Redirect`, `Response` for responses

- **Add to Cargo.toml**:

```toml
axum = { version = "0.7", features = ["multipart", "json"] }
```

### tower

- **Crate**: `tower` (used by axum)
- **Purpose**: Middleware layer (timeout, compression, etc.)
- **Use**: `tower_http::set_header::SetResponseHeader` for security headers

---

## File Handling

### zip

- **Crate**: `zip` (already in AlLibrary Cargo.toml)
- **Purpose**: Create and read ZIP archives
- **Usage**:

```rust
use zip::ZipWriter;
use std::io::Write;

let file = File::create("archive.zip")?;
let mut zip = ZipWriter::new(file);
zip.start_file("document.pdf", FileOptions::default())?;
zip.write_all(&file_bytes)?;
zip.finish()?;
```

### flate2

- **Crate**: `flate2`
- **Purpose**: Gzip compression for single-file downloads
- **Usage**:

```rust
use flate2::write::GzEncoder;
use flate2::Compression;

let mut encoder = GzEncoder::new(Vec::new(), Compression::new(6));
encoder.write_all(&file_bytes)?;
let compressed = encoder.finish()?;
```

### tokio

- **Crate**: `tokio` (already present)
- **Purpose**: Async file I/O
- **Usage**: `tokio::fs::File::open`, `tokio::io::AsyncReadExt`, `tokio::io::AsyncWriteExt`

---

## Multipart Upload

### axum::extract::Multipart

- **Built into axum** (with `multipart` feature)
- **Usage**:

```rust
async fn upload(mut multipart: Multipart) -> Result<impl IntoResponse> {
    while let Some(field) = multipart.next_field().await? {
        let name = field.name().unwrap_or_default().to_string();
        let data = field.bytes().await?;
        // Process field
    }
    Ok(Redirect::to("/"))
}
```

### Progress Tracking

- **Approach**: Wrap each field's `chunk()` stream in a custom `Stream` that yields progress events
- **Alternative**: Use `field.chunk()` in a loop and emit events via `tauri::AppHandle::emit` or a channel

---

## WebSocket (Chat Mode)

### axum WebSocket

- **Crate**: `axum` (with `ws` or `ws` feature) or `axum-extra`
- **Alternative**: `tower-http` with `ws` feature
- **Usage** (conceptual):

```rust
Router::new().route("/ws", get(ws_handler))

async fn ws_handler(ws: WebSocketUpgrade) -> Response {
    ws.on_upgrade(handle_socket)
}
```

---

## Summary: Cargo.toml Additions

```toml
# For Option B Phase 1 (extend tor_manager, add Axum)
axum = { version = "0.7", features = ["multipart", "json"] }
tower-http = { version = "0.5", features = ["set-header"] }
flate2 = "1.0"
mime_guess = "2.0"  # Already present
```

Optional for later phases:

```toml
# Arti-based (pure Rust Tor)
arti-client = "0.14"
arti-axum = "0.1"
```
