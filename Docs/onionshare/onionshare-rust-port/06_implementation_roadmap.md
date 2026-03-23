# Implementation Roadmap

## Phase 1: Share Mode (4–6 weeks)

### Goals

- Axum server with share routes
- Zip creation for multi-file/directory
- Gzip for single file
- Range requests, ETag, 304 Not Modified
- Integration with `tor_manager::create_hidden_service`
- Tauri commands: `start_onion_share`, `stop_onion_share`

### Tasks

1. Add `axum`, `tower-http`, `flate2` to Cargo.toml
2. Implement `share_routes()` (index, download, serve_path)
3. Implement `build_zip()` and `add_dir_to_zip()`
4. Implement gzip on-demand for single file
5. Implement `parse_range_header()` and 206 Partial Content
6. Implement ETag (`sha256:...`), Last-Modified, 304
7. Implement chunked streaming (100KB chunks)
8. Wire `tor_manager::create_hidden_service` to Axum listener
9. Add Tauri commands and state for active share
10. Optional: autostop after first download

---

## Phase 2: Receive Mode (3–4 weeks)

### Goals

- Multipart upload handling
- Progress tracking via events
- Webhook integration (optional)
- Tauri commands: `start_onion_receive`, `stop_onion_receive`

### Tasks

1. Implement `receive_routes()` (index, upload, upload-ajax)
2. Implement `sanitize_filename()` and secure path handling
3. Implement per-upload dir `{data_dir}/{date}/{time}/`
4. Implement text message handling (`{dir}-message.txt`, max 524288 chars)
5. Implement progress events (`onion-share-progress`)
6. Implement webhook POST on success
7. Add Tauri commands and state for active receive

---

## Phase 3: Website Mode (Optional, 1–2 weeks)

### Goals

- Static file serving
- CSP handling

### Tasks

1. Add `website_routes()` for static files
2. Apply CSP headers
3. Tauri command: `start_onion_website`

---

## Phase 4: Chat Mode (Optional, 2–3 weeks)

### Goals

- WebSocket support
- Username validation, session handling

### Tasks

1. Add WebSocket route
2. Implement chat protocol (join, message, leave)
3. Username validation (length, allowed chars)
4. Tauri command: `start_onion_chat`

---

## Phase 5: Security & Parity (Ongoing)

### Goals

- Security headers on all responses
- Stealth/client auth (if Tor supports via control)
- Autostop timers
- Graceful shutdown

### Tasks

1. Apply security headers (X-Frame-Options, X-Content-Type-Options, Referrer-Policy, CSP)
2. Document and implement client auth if needed
3. Autostop timers (share after N downloads, receive after N uploads)
4. Graceful shutdown (wait for rendezvous circuits)
5. Rate limiting considerations

---

## Milestone Summary

| Phase | Duration | Deliverable |
|-------|----------|-------------|
| 1 | 4–6 weeks | Share mode with Tor |
| 2 | 3–4 weeks | Receive mode |
| 3 | 1–2 weeks | Website mode (optional) |
| 4 | 2–3 weeks | Chat mode (optional) |
| 5 | Ongoing | Security parity |
