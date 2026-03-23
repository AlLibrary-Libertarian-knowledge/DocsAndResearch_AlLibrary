# Phase 6: Security & Anti-Censorship

## Overview

Phase 6 focuses on complete TOR integration, OnionShare integration (anonymous file share and receive over Tor), and security hardening. It also covers API/integration scope (local-first Tauri commands and plugin hooks).

## Duration

- Estimated Time: 4 weeks
- Start: Week 17
- End: Week 20

## Main Goals

1. **Security & Anti-Censorship**
   - TOR integration for transport selection; document how to enable in settings.
   - **OnionShare integration**: Implement anonymous file share and receive over Tor (Option B Rust port per [Docs/onionshare/onionshare-rust-port](../../Docs/onionshare/onionshare-rust-port/README.md): extend `tor_manager`, Axum routes for share/receive, Tauri commands `start_onion_share`, `stop_onion_share`, `start_onion_receive`, `stop_onion_receive`; see [01_architecture_overview.md](../../Docs/onionshare/onionshare-rust-port/01_architecture_overview.md) and [06_implementation_roadmap.md](../../Docs/onionshare/onionshare-rust-port/06_implementation_roadmap.md)).
   - Harden Tauri IPC and Rust commands; input sanitization audit.

2. **API/Integration Scope**
   - Local-first API surface (Tauri commands) and plugin hooks; no centralized services.

## Key Deliverables

- RESTful API
- API documentation
- Integration framework
- Plugin system
- Automation tools

## Technical Requirements

- API development tools
- Authentication system
- Integration framework
- Plugin architecture
- Automation engine

## Success Criteria

- API is well-documented and secure
- Integrations work reliably
- Plugins can be developed and installed
- Automation tools function as expected
- System is extensible and maintainable

---

## Execution Blueprint (Append-Only)

1) Security & Anti‑Censorship Integration
- TOR integration for transport selection; document how to enable in settings.
- Harden Tauri IPC + Rust commands; input sanitization audit.

2) API/Integration Scope
- Local-first API surface (Tauri commands) and plugin hooks; no centralized services.

## Integration Map

- Services: security/validation, network/tor, plugin system.
- Settings page: controls for security and transport options.

## Acceptance Criteria (Phase 6)

- TOR transport works; connection fallback logic verified.
- OnionShare share/receive modes operational (Option B preferred).
- Security scans automated in CI; no high vulnerabilities.
- APIs documented and typed; samples included.

## Test Plan

- Security tests: injection, path traversal, IPC misuse.
- Network tests: route via TOR vs direct.

## Performance Budgets

- TOR overhead documented; app remains usable with < 2× latency for network ops.

## Cultural Info-Only Guardrails

- Security/legal checks remain technical; cultural content is never filtered.

## References

- Guides/Rules: see `.cursor/rules/*`, `01_IMPLEMENTATION_WORKFLOW_GUIDE.md`.