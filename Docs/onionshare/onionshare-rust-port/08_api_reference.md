# API Reference

## Tauri Commands

### Share Mode

```rust
#[tauri::command]
async fn start_onion_share(
    paths: Vec<PathBuf>,
    public: bool,
    autostop: bool,
) -> Result<OnionShareResult, String>

#[tauri::command]
async fn stop_onion_share() -> Result<(), String>
```

**`OnionShareResult`**:

```rust
pub struct OnionShareResult {
    pub onion_address: String,  // e.g. "abc123...onion"
    pub local_port: u16,
    pub url_path: Option<String>,  // random path if used
}
```

### Receive Mode

```rust
#[tauri::command]
async fn start_onion_receive(
    data_dir: PathBuf,
    webhook_url: Option<String>,
) -> Result<OnionShareResult, String>

#[tauri::command]
async fn stop_onion_receive() -> Result<(), String>
```

### Optional: Website Mode

```rust
#[tauri::command]
async fn start_onion_website(
    static_dir: PathBuf,
) -> Result<OnionShareResult, String>

#[tauri::command]
async fn stop_onion_website() -> Result<(), String>
```

### Optional: Chat Mode

```rust
#[tauri::command]
async fn start_onion_chat() -> Result<OnionShareResult, String>

#[tauri::command]
async fn stop_onion_chat() -> Result<(), String>
```

---

## Event Types

### Progress (Share)

```rust
// Emitted during chunked download
"onion-share-download-progress"

// Payload
struct ShareProgressPayload {
    bytes_sent: u64,
    total_bytes: u64,
}
```

### Progress (Receive)

```rust
// Emitted during multipart upload
"onion-share-progress"

// Payload
struct ReceiveProgressPayload {
    filename: String,
    bytes: u64,
    total: Option<u64>,
}
```

### State Change

```rust
// Emitted when share/receive starts or stops
"onion-share-state"

// Payload
struct OnionShareStatePayload {
    mode: String,  // "share" | "receive" | "website" | "chat"
    active: bool,
    onion_address: Option<String>,
}
```

---

## Command Registration

```rust
// In lib.rs or main
.invoke_handler(tauri::generate_handler![
    start_onion_share,
    stop_onion_share,
    start_onion_receive,
    stop_onion_receive,
])
```

---

## Frontend Usage (TypeScript)

```typescript
import { invoke } from '@tauri-apps/api/core';
import { listen } from '@tauri-apps/api/event';

// Start share
const result = await invoke<OnionShareResult>('start_onion_share', {
  paths: ['/path/to/files'],
  public: true,
  autostop: true,
});
console.log(`Share at: http://${result.onion_address}`);

// Listen for progress
const unlisten = await listen<ReceiveProgressPayload>('onion-share-progress', (event) => {
  console.log(event.payload.filename, event.payload.bytes);
});

// Stop share
await invoke('stop_onion_share');
```
