# How OnionShare Works (Original Python Implementation)

This document describes how OnionShare works in its original form—the Python/Flask implementation. It focuses on architecture, data flow, and core functions, ignoring UI. Use this as a reference when integrating OnionShare into AlLibrary or porting it to Rust.

---

## 1. High-Level Architecture

```
┌─────────────────────────────────────────────────────────────────────────┐
│                         OnionShare Application                          │
├─────────────────────────────────────────────────────────────────────────┤
│  OnionShare (orchestrator)                                               │
│    ├── choose_port() → 17600–17650                                      │
│    ├── start_onion_service(mode, mode_settings)                         │
│    └── stop_onion_service(mode_settings)                                 │
├─────────────────────────────────────────────────────────────────────────┤
│  Onion (Tor layer)                    │  Web (HTTP layer)                │
│    ├── connect()                      │    ├── Flask + Waitress          │
│    ├── start_onion_service()          │    ├── ShareModeWeb              │
│    ├── stop_onion_service()          │    ├── ReceiveModeWeb            │
│    ├── get_tor_socks_port()          │    ├── WebsiteModeWeb             │
│    └── cleanup()                     │    └── ChatModeWeb               │
├─────────────────────────────────────────────────────────────────────────┤
│  stem.Controller (Tor control)        │  ModeSettings (per-mode config) │
└─────────────────────────────────────────────────────────────────────────┘
```

**Data flow:** User selects mode → OnionShare picks port → Web server binds to `127.0.0.1:port` → Onion creates ephemeral hidden service mapping Tor port 80 → local port → Clients reach `http://{id}.onion` → Tor forwards to Flask.

---

## 2. Tor / Onion Layer (`onion.py`)

### 2.1 Connection Types

| Type | Behavior |
|------|----------|
| **bundled** | Starts own Tor process; writes `torrc`; uses cookie auth; supports bridges (obfs4, meek-azure, snowflake, moat, custom) |
| **automatic** | Tries ports 9151, 9153, 9051; or `TOR_CONTROL_PORT` env; or socket paths (`~/Library/.../control.socket`, `/run/user/{uid}/Tor/control.socket`) |
| **control_port** | User-supplied address:port |
| **socket_file** | User-supplied socket path |

### 2.2 Authentication

- **Cookie**: Default for bundled; `CookieAuthentication 1` in torrc
- **Password**: `auth_password` in settings
- **No auth**: `auth_type == "no_auth"`

### 2.3 Key Functions

| Function | Purpose |
|----------|---------|
| `connect(local_only=False)` | Connect to Tor; if bundled, start Tor, wait for bootstrap, authenticate |
| `start_onion_service(mode, mode_settings, port, await_publication)` | `create_ephemeral_hidden_service({80: port})`; returns `{service_id}.onion` |
| `stop_onion_service(mode_settings)` | `remove_ephemeral_hidden_service(service_id)` |
| `get_tor_socks_port()` | Returns `(address, port)` for SOCKS5 proxy |
| `cleanup(stop_tor, wait)` | Remove all ephemeral services; optionally wait for rendezvous circuits to close; terminate Tor process |

### 2.4 Hidden Service Options

- **Key type**: `ED25519-V3` (v3 onions)
- **Public mode**: Anyone can access; `client_auth_v3` not set
- **Stealth mode**: `client_auth_v3` set; only clients with private key can access; key pair generated via `nacl.public.PrivateKey.generate()`
- **Persistent onion**: Reuse `private_key` from mode_settings; supports `client_auth_priv_key` / `client_auth_pub_key`

### 2.5 Graceful Shutdown (Share Mode)

- Share mode adds `service_id` to `graceful_close_onions`
- On cleanup with `wait=True`, polls `get_circuits()` for `HS_SERVICE_REND` circuits matching those IDs
- Waits until circuits close before terminating Tor

---

## 3. Orchestrator (`onionshare.py`)

| Function | Purpose |
|----------|---------|
| `choose_port()` | `get_available_port(17600, 17650)` |
| `start_onion_service(mode, mode_settings, await_publication=True)` | Picks port if needed; starts autostop timer if set; if `local_only`, returns `127.0.0.1:{port}`; else calls `onion.start_onion_service()` |
| `stop_onion_service(mode_settings)` | Delegates to `onion.stop_onion_service()` |

**local_only**: Skips Tor; used for development. Returns `127.0.0.1:{port}`.

---

## 4. Web Server (`web/web.py`)

### 4.1 Stack

- **Flask** + **Flask-Compress** (gzip)
- **Waitress** (production WSGI; except chat mode)
- **Flask-SocketIO** (chat mode only; gevent if available)

### 4.2 Lifecycle

| Method | Purpose |
|--------|---------|
| `start(port)` | Binds to `127.0.0.1` (or `0.0.0.0` on Whonix: `/usr/share/anon-ws-base-files/workstation` exists) |
| `stop(port)` | Puts item in `stop_q`; if chat, stops SocketIO; else `waitress_custom_shutdown()` |
| `waitress_custom_shutdown()` | Sets `waitress.shutdown = True`; closes triggers; maintenance; task_dispatcher shutdown |

### 4.3 Shutdown

- Shutdown via HTTP: `/shutdown` with password (`shutdown_password` = random 16-char string)
- `stop_q`: Queue; if non-empty, user requested stop; handlers check it to abort transfers

### 4.4 Request Queue (`q`)

Events sent to GUI/CLI:

| Constant | Meaning |
|----------|---------|
| `REQUEST_LOAD` | Page load |
| `REQUEST_STARTED` | Download/upload started |
| `REQUEST_PROGRESS` | Progress update |
| `REQUEST_CANCELED` | Download canceled |
| `REQUEST_UPLOAD_INCLUDES_MESSAGE` | Text message received |
| `REQUEST_UPLOAD_FILE_RENAMED` | File renamed (secure_filename) |
| `REQUEST_UPLOAD_SET_DIR` | Receive dir for file |
| `REQUEST_UPLOAD_FINISHED` | Upload complete |
| `REQUEST_UPLOAD_CANCELED` | Upload canceled |
| `REQUEST_INDIVIDUAL_FILE_STARTED` | Individual file download started |
| `REQUEST_INDIVIDUAL_FILE_PROGRESS` | Individual file progress |
| `REQUEST_INDIVIDUAL_FILE_CANCELED` | Individual file canceled |
| `REQUEST_ERROR_DATA_DIR_CANNOT_CREATE` | Cannot create receive dir |

### 4.5 Security Headers

All responses get:

- `X-Frame-Options: DENY`
- `X-Xss-Protection: 1; mode=block`
- `X-Content-Type-Options: nosniff`
- `Referrer-Policy: no-referrer`
- `Server: OnionShare`
- `Content-Security-Policy`: `default-src 'self'; frame-ancestors 'none'; form-action 'self'; base-uri 'self'; img-src 'self' data:;` (unless website mode with custom/disabled CSP)

### 4.6 Static URL Path

- `static_url_path` = `/static_{random_16_chars}` to avoid collisions with shared filenames
- `mimetypes.add_type("text/javascript", ".js")` to avoid wrong MIME on some systems

### 4.7 Receive Mode Customization

- **ReceiveModeWSGIMiddleware**: Injects `web` and `stop_q` into `environ`
- **ReceiveModeRequest**: Custom Flask Request; creates per-upload dir; tracks progress; uses `ReceiveModeFile` for writes

---

## 5. Share Mode (`web/share_mode.py` + `send_base_mode.py`)

### 5.1 Flow

1. **set_file_info(filenames)** (from SendBaseModeWeb):
   - Builds `self.files` (path → filesystem path) and `self.root_files`
   - If single dir, expands to list of files inside
   - Calls `set_file_info_custom()` → `build_zipfile_list()`

2. **build_zipfile_list(filenames)**:
   - **Single file, no dirs**: Use file as-is; pre-gzip to temp `file.gz`; compute `download_etag`, `gzip_etag`
   - **Multiple files/dirs**: `ZipWriter` creates `onionshare_{random}.zip`; add files/dirs; compute `download_etag`

3. **Routes**:
   - `GET /` or `GET /<path>`: `index(path)` → `render_logic(path)` → directory listing or `stream_individual_file` or 404
   - `GET /download`: Stream zip or single file (gzip if `Accept-Encoding: gzip`)

### 5.2 Single File vs Multiple

| Case | Behavior |
|------|----------|
| 1 file, 0 dirs | Serve raw or gzip; pre-compress to temp; `should_use_gzip()` checks `Accept-Encoding` |
| Multiple files/dirs | Zip via `ZipWriter`; `ZIP_DEFLATED` |

### 5.3 ZipWriter

- Writes to temp dir: `onionshare_{random_string(4,6)}.zip`
- `add_file(filename)`: `z.write(filename, basename, ZIP_DEFLATED)`
- `add_dir(filename)`: `os.walk`; skip symlinks; strip parent path for arc names
- Honors `cancel_compression` for early exit

### 5.4 HTTP Features

- **Range requests**: `parse_range_header(range_header, target_size)` → list of `(start, end)`; supports `bytes=0-`, `bytes=-100`, `bytes=100-200`; merges overlapping ranges; 416 if invalid
- **ETag**: `"sha256:{hex}"` via `make_etag(data)` (SHA-256 of file)
- **Last-Modified**: UTC datetime
- **304 Not Modified**: If `If-None-Match` or `If-Modified-Since` match
- **206 Partial Content**: For range requests
- **Chunked streaming**: 100KB chunks in `generate()`; yields chunks; emits `REQUEST_PROGRESS`
- **Content-Disposition**: `attachment` for download; `inline` for individual files
- **Vary: Accept-Encoding**: For range + gzip

### 5.5 Autostop

- `autostop_sharing`: If True, deny new downloads while `download_in_progress`; after first complete download, set `web.running = False`, call `web.stop()`
- `download_individual_files`: `not autostop_sharing`; if True, allow direct file links; else 404 for individual files

### 5.6 Gzip

- `_gzip_compress(input, output, level=6)`: 64KB blocks; optional `processed_size_callback`
- Single file: Pre-compress to temp; serve that file for gzip clients
- Individual files: Cache in `gzip_individual_files`; compress on first request

---

## 6. Receive Mode (`web/receive_mode.py`)

### 6.1 Request Flow

1. **ReceiveModeRequest.__init__** (on POST to `/upload` or `/upload-ajax`):
   - Create dir: `{data_dir}/{date}/{time}/` (e.g. `2025-03-03/143052123456`)
   - Collision: try `{dir}-1`, `{dir}-2`, … up to 100
   - `message_filename` = `{receive_mode_dir}-message.txt`
   - If `disable_text` is False and form has `text` with `len <= 524288` and non-empty: save to `message_filename`; set `includes_message = True`
   - `progress = {}` for per-file bytes

2. **_get_file_stream()** (per file in multipart):
   - `secure_filename(filename)` for safe name
   - Return `ReceiveModeFile` instance

3. **ReceiveModeFile**:
   - Writes to `{filename}.part`; on `close()`, rename to final filename
   - `write(b)` calls `file_write_func(filename, bytes_written)` → update `progress`; emit `REQUEST_PROGRESS`
   - `close()` calls `file_close_func`; marks `progress[filename]["complete"] = True`

4. **ReceiveModeRequest.close()**:
   - Emit `REQUEST_UPLOAD_FINISHED` or `REQUEST_UPLOAD_CANCELED`
   - Remove from `uploads_in_progress`
   - If dir empty, `os.rmdir`

### 6.2 Routes

| Route | Method | Purpose |
|-------|--------|---------|
| `/` | GET | Upload form (receive.html) |
| `/upload` | POST | Handle upload; redirect to `/`; flash messages |
| `/upload-ajax` | POST | Same; JSON response `{info_flashes: [...]}` or `{new_body: ...}` for thank-you |

### 6.3 Webhook

- If `webhook_url` set and no `upload_error` and (message or files received):
- `requests.post(webhook_url, data=msg, timeout=5, proxies=web.proxies)`
- `msg` e.g. `"1 file"`, `"3 files and a text message"`

### 6.4 Settings

- `disable_text`: Skip text message handling
- `disable_files`: Skip file handling
- `data_dir`: Default `~/OnionShare` (platform-specific)

---

## 7. Website Mode (`web/website_mode.py`)

- Extends `SendBaseModeWeb`; no zip
- `set_file_info_custom`: Sets `cancel_compression = True` (no zip)
- **Routes**: `GET /`, `GET /<path>`
- **Logic**: Directory → look for `index.html`; if present, serve it; else directory listing with trailing slash
- **CSP**: Can be disabled or customized via mode_settings

---

## 8. Chat Mode (`web/chat_mode.py`)

- **Flask-SocketIO** with namespace `/chat`
- **Routes**: `GET /` (chat.html); `POST /update-session-username`
- **Socket events**:
  - `connect`: Validate username; add to `connected_users`; broadcast `status` (joined)
  - `text`: Broadcast `chat_message` (username, msg)
  - `update_username`: Validate; update in `connected_users`; broadcast
  - `disconnect`: Remove from `connected_users`; broadcast left
- **Username validation**: `remove_unallowed_characters` (ASCII letters, numbers, `-`, `_`, space); must be unique; `len < 128`
- **Session**: `session["name"]`; default from `build_username()` (word list)

---

## 9. Mode Settings (`mode_settings.py`)

| Group | Keys |
|-------|------|
| `onion` | `private_key`, `client_auth_priv_key`, `client_auth_pub_key` |
| `persistent` | `mode`, `enabled`, `autostart_on_launch` |
| `general` | `title`, `public`, `autostart_timer`, `autostop_timer`, `service_id` |
| `share` | `autostop_sharing`, `filenames`, `log_filenames` |
| `receive` | `data_dir`, `webhook_url`, `disable_text`, `disable_files` |
| `website` | `disable_csp`, `custom_csp`, `log_filenames`, `filenames` |
| `chat` | (empty) |

---

## 10. Common Utilities (`common.py`)

| Function | Purpose |
|----------|---------|
| `get_available_port(min, max)` | Random free port in range |
| `get_tor_paths()` | Tor binary, geoip, obfs4, snowflake, meek paths |
| `build_password(word_count)` | Random words from wordlist |
| `build_username(word_count)` | Same for usernames |
| `random_string(num_bytes, output_len)` | Base32 random string |
| `human_readable_filesize(b)` | Human-readable size |
| `dir_size(path)` | Total directory size |
| `build_tmp_dir()` | Temp directory for session |
| `build_tor_dir()` | Tor data directory |
| `build_data_dir()` | OnionShare data directory |
| `get_resource_path(relative)` | Path to bundled resources |
| `build_persistent_dir()` | Persistent settings directory |

---

## 11. Port and Host Binding

| Aspect | Value |
|--------|-------|
| Port range | 17600–17650 |
| Default host | `127.0.0.1` |
| Whonix host | `0.0.0.0` (if `/usr/share/anon-ws-base-files/workstation` exists) |

---

## 12. Secure Filename

- **werkzeug.utils.secure_filename**: Used for uploads; strips path components; keeps safe chars

---

## 13. Integration Summary

For AlLibrary integration:

1. **Option A (subprocess)**: Run `onionshare-cli`; parse stdout for onion URL; control via SIGINT or shutdown endpoint.
2. **Option B (Rust port)**: Reimplement Tor control (or use existing `tor_manager`), HTTP (Axum), share/receive logic; see [onionshare-rust-port](./onionshare-rust-port/README.md).

Key touchpoints:

- Tor: `ADD_ONION` / `DEL_ONION` via stem or control protocol
- HTTP: Flask routes → Axum routes
- Share: ZipWriter, gzip, range, ETag, chunked streaming
- Receive: Multipart, ReceiveModeFile-style progress, per-upload dirs, webhook
