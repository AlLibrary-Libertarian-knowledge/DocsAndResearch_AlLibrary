# Receive Mode Specification

## OnionShare Behavior (Reference)

Source: `onionshare/cli/onionshare_cli/web/receive_mode.py`

### Core Components

| Component | Purpose |
|-----------|---------|
| `ReceiveModeRequest` | Custom Flask Request; creates per-upload dir, tracks progress |
| `ReceiveModeFile` | File-like object; `write()` calls progress callback |
| `ReceiveModeWSGIMiddleware` | Injects `web` into `environ` |
| `ReceiveModeWeb` | Routes, upload handling |

### Per-Upload Directory

- Format: `{data_dir}/{date}/{time}/`
- Example: `~/OnionShare/2025-03-03/143052123456/`
- If collision: `{dir}-1`, `{dir}-2`, etc.

### Text Message

- Form field: `text`
- Max length: 524288 characters
- Saved as: `{receive_dir}-message.txt`
- Stored in same directory as files (with `-message` suffix)

### Routes

| Route | Method | Purpose |
|-------|--------|---------|
| `/` | GET | Upload form |
| `/upload` | POST | Handle multipart (redirect response) |
| `/upload-ajax` | POST | Handle multipart (JSON response) |

### Features

- **disable_text**: If true, skip text message handling
- **disable_files**: If true, skip file upload handling
- **webhook_url**: Optional; POST to URL on successful upload

---

## Rust Implementation

### Route Structure

```rust
fn receive_routes(state: AppState) -> Router {
    Router::new()
        .route("/", get(index))
        .route("/upload", post(upload))
        .route("/upload-ajax", post(upload_ajax))
        .with_state(state)
}
```

### Index (Upload Form)

```rust
async fn index() -> impl IntoResponse {
    Html(include_str!("../templates/receive.html"))
}
```

Template should include:
- File input (multipart)
- Optional text area
- Submit button

### Upload Handler

```rust
async fn upload(
    State(state): State<AppState>,
    mut multipart: Multipart,
) -> Result<impl IntoResponse, AppError> {
    if !state.can_upload {
        return Ok(StatusCode::FORBIDDEN);
    }
    let now = Utc::now();
    let date_dir = now.format("%Y-%m-%d").to_string();
    let time_dir = now.format("%H%M%S%f").to_string();
    let receive_dir = state.data_dir.join(&date_dir).join(&time_dir);

    // Handle collision
    let receive_dir = ensure_unique_dir(receive_dir).await?;
    tokio::fs::create_dir_all(&receive_dir).await?;

    let mut files_received = Vec::new();
    let mut message_received = false;

    while let Some(field) = multipart.next_field().await? {
        let name = field.name().unwrap_or_default().to_string();
        if name == "text" {
            if !state.disable_text {
                let text = field.text().await?;
                if text.len() <= 524288 && !text.trim().is_empty() {
                    let msg_path = format!("{}-message.txt", receive_dir.display());
                    tokio::fs::write(&msg_path, &text).await?;
                    message_received = true;
                }
            }
            continue;
        }
        if name == "file[]" && !state.disable_files {
            let filename = field.file_name().map(sanitize_filename).unwrap_or_else(|| "unnamed".into());
            let path = receive_dir.join(&filename);
            let mut file = tokio::fs::File::create(&path).await?;
            let mut bytes: u64 = 0;
            while let Some(chunk) = field.chunk().await? {
                file.write_all(&chunk).await?;
                bytes += chunk.len() as u64;
                state.emit_progress(filename.clone(), bytes);
            }
            files_received.push(filename);
        }
    }

    if let Some(webhook) = &state.webhook_url {
        let msg = format!("{} files uploaded", files_received.len());
        let _ = reqwest::Client::new().post(webhook).body(msg).send().await;
    }

    if state.upload_ajax {
        Ok(Json(UploadResponse { info_flashes: vec![format!("Uploaded {}", files_received.join(", "))] }))
    } else {
        Ok(Redirect::to("/"))
    }
}
```

### Secure Filename Handling

```rust
fn sanitize_filename(filename: &str) -> String {
    filename
        .chars()
        .map(|c| if c.is_alphanumeric() || c == '.' || c == '-' || c == '_' { c } else { '_' })
        .collect::<String>()
    // Or use a crate like `sanitize-filename`
}
```

### Ensure Unique Directory

```rust
async fn ensure_unique_dir(mut path: PathBuf) -> Result<PathBuf, AppError> {
    let base = path.clone();
    for i in 0..100 {
        if i > 0 {
            path = format!("{}-{}", base.display(), i).into();
        }
        if tokio::fs::create_dir(&path).await.is_ok() {
            return Ok(path);
        }
    }
    Err(AppError::CannotCreateDir)
}
```

### Progress Tracking

Emit events to frontend via Tauri:

```rust
async fn emit_progress(&self, filename: String, bytes: u64) {
    if let Some(handle) = &self.app_handle {
        let _ = handle.emit("onion-share-progress", ProgressPayload {
            filename,
            bytes,
            total: None, // or total if known from Content-Length
        });
    }
}
```

### Webhook

- On successful upload (files or message), POST to `webhook_url`
- Body: `"1 file"` or `"3 files"` or `"1 file and a text message"`
- Timeout: 5 seconds
- Use Tor SOCKS proxy if configured (for anonymity of webhook request)

---

## Settings (ModeSettings)

| Key | Type | Default |
|-----|------|---------|
| `data_dir` | PathBuf | `~/OnionShare` (platform-specific) |
| `webhook_url` | Option<String> | None |
| `disable_text` | bool | false |
| `disable_files` | bool | false |
