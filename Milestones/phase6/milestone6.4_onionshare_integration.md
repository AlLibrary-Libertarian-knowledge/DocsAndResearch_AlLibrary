# Milestone 6.4: OnionShare Integration

## Overview

This milestone implements anonymous file share and receive over Tor (OnionShare-style functionality) within AlLibrary, following Option B (Rust port) per the project specification. It extends the existing `tor_manager` and adds Axum HTTP routes plus Tauri commands for share and receive modes.

## Prerequisites

- Phase 4 (P2P) completed: Tor overlay and `create_hidden_service` available.
- Phase 6 TOR UI and security work (transport toggle, IPC hardening) in progress or complete.

## Goals

- **Share mode**: Serve files or directories for download over a Tor onion service; optional zip for multiple files; range requests, ETag, 304; optional autostop after first download.
- **Receive mode**: Accept file uploads and optional text messages over Tor; per-upload directory; progress events; optional webhook.
- **Tauri commands**: `start_onion_share`, `stop_onion_share`, `start_onion_receive`, `stop_onion_receive`; return onion URL when ready.
- **Security parity**: Security headers, graceful shutdown, optional client auth (if supported by Tor control).

## Reference Documentation

- [Docs/onionshare/onionshare-rust-port/README.md](../../Docs/onionshare/onionshare-rust-port/README.md) – Option B overview and quick start
- [01_architecture_overview.md](../../Docs/onionshare/onionshare-rust-port/01_architecture_overview.md) – High-level architecture, component mapping, integration with `tor_manager`
- [03_share_mode_specification.md](../../Docs/onionshare/onionshare-rust-port/03_share_mode_specification.md) – Share mode: file serving, zip, gzip, range requests
- [04_receive_mode_specification.md](../../Docs/onionshare/onionshare-rust-port/04_receive_mode_specification.md) – Receive mode: multipart upload, progress, webhook
- [06_implementation_roadmap.md](../../Docs/onionshare/onionshare-rust-port/06_implementation_roadmap.md) – Phased implementation (Share mode then Receive mode)
- [08_api_reference.md](../../Docs/onionshare/onionshare-rust-port/08_api_reference.md) – Proposed Tauri commands and event types

## Implementation Order (per roadmap)

1. **Share mode (4–6 weeks)**  
   Axum share routes, zip/gzip, range requests, ETag/304, integration with `tor_manager::create_hidden_service`, Tauri commands `start_onion_share` / `stop_onion_share`.

2. **Receive mode (3–4 weeks)**  
   Multipart upload handling, progress events, optional webhook, Tauri commands `start_onion_receive` / `stop_onion_receive`.

3. **Security and parity (ongoing)**  
   Security headers on all responses, autostop timers, graceful shutdown (wait for rendezvous circuits).

## Success Criteria

- Share mode: User can start share, get onion URL, recipient downloads via Tor; stop share cleans up.
- Receive mode: User can start receive, get onion URL, sender uploads via Tor; files saved to configured directory; stop receive cleans up.
- No cultural access gating: anonymous share/receive is technical only; cultural context remains informational.
- Security: Same security headers and practices as in [07_security_parity_checklist.md](../../Docs/onionshare/onionshare-rust-port/07_security_parity_checklist.md).

## Dependencies

- `tor_manager` with `create_hidden_service(local_port)` (Phase 4).
- Axum, tower-http, multipart, zip/gzip crates per [02_rust_crate_ecosystem.md](../../Docs/onionshare/onionshare-rust-port/02_rust_crate_ecosystem.md).
- Port range 17600–17650 for onion share/receive (configurable).

## Cultural Info-Only Guardrails

- OnionShare integration is for anonymous transfer only. No content filtering or access control based on cultural sensitivity. Cultural metadata may be shown as information alongside content but must not block or gate share/receive.
