# Option B: OnionShare Rust Port

## Overview

Option B is the strategy of **porting OnionShare's core functionality to Rust**, enabling AlLibrary to provide anonymous file sharing and receiving as a native Rust/Tauri feature without any Python dependencies.

This documentation provides an in-depth technical specification for implementing OnionShare-like behavior entirely within the AlLibrary codebase.

## Purpose

- **Single binary**: No external OnionShare CLI or Python runtime required
- **Native integration**: Share and receive flows integrate directly with Tauri commands
- **Full control**: Customize behavior for AlLibrary's document-focused use case
- **Performance**: Rust HTTP server (Axum) with efficient streaming and compression

## Document Index

| Document | Description |
|----------|-------------|
| [01_architecture_overview.md](./01_architecture_overview.md) | High-level architecture, component mapping, integration points |
| [02_rust_crate_ecosystem.md](./02_rust_crate_ecosystem.md) | Tor, HTTP, file handling, and multipart crates |
| [03_share_mode_specification.md](./03_share_mode_specification.md) | Share mode: file serving, zip, gzip, range requests |
| [04_receive_mode_specification.md](./04_receive_mode_specification.md) | Receive mode: multipart upload, progress, webhook |
| [05_tor_integration_strategies.md](./05_tor_integration_strategies.md) | Extend tor_manager vs Arti-based approaches |
| [06_implementation_roadmap.md](./06_implementation_roadmap.md) | Phased implementation plan with timelines |
| [07_security_parity_checklist.md](./07_security_parity_checklist.md) | Security features to replicate from OnionShare |
| [08_api_reference.md](./08_api_reference.md) | Proposed Tauri commands and event types |

## Option A vs Option B

| Aspect | Option A: Subprocess | Option B: Native Rust |
|--------|----------------------|------------------------|
| **Dependencies** | Requires OnionShare CLI installed | None beyond existing AlLibrary deps |
| **Packaging** | Must bundle or document OnionShare | Single Tauri binary |
| **Control** | Parse stdout, send SIGINT | Full programmatic control |
| **Customization** | Limited to CLI flags | Full control over behavior |
| **Effort** | Low (days) | High (weeks to months) |
| **Maintenance** | Track OnionShare releases | Maintain our own implementation |

## When to Choose Option B

- **Distribution**: You want a single installer with no external tools
- **Customization**: You need AlLibrary-specific sharing behavior (e.g. cultural metadata, document-only)
- **Long-term**: You prefer owning the implementation over depending on OnionShare
- **Platform**: OnionShare packaging is problematic on your target platforms

## When to Choose Option A

- **Speed**: You need anonymous sharing soon and can accept OnionShare as a dependency
- **Parity**: You want exact OnionShare behavior (chat, website modes, etc.)
- **Maintenance**: You prefer delegating Tor/sharing logic to the OnionShare project

## Quick Start (After Implementation)

```rust
// Share documents
let result = start_onion_share(
    vec![PathBuf::from("/path/to/document.pdf")],
    true,  // public
    true,  // autostop after first download
).await?;
// result.onion_url = "http://abc123...onion"

// Receive documents
let result = start_onion_receive(
    PathBuf::from("~/OnionShare"),
    Some("https://webhook.example.com/notify".into()),
).await?;
```

## Related Documentation

- [base.md](../../base.md) – Original OnionShare functional analysis and integration options
- [P2P.md](../technical/P2P.md) – AlLibrary P2P architecture
- [tor_manager.rs](../../../DesktopApp_AlLibrary/src-tauri/src/core/p2p/tor_manager.rs) – Existing Tor/hidden service implementation
