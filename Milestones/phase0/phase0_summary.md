# Phase 0: Research and Methodology

## Overview

Phase 0 establishes the academic and methodological foundation for the AlLibrary project. It includes introduction, literature review, materials and methods aligned with thesis/TCC structure, and a planned proof-of-concept for anonymous file sharing via Tor that will inform integration decisions (OnionShare Option A vs Option B).

**Status**: Planned  
**Duration**: To be scheduled (research and POC)  
**Prerequisites**: None (initial phase)

---

## 1. Introdução (Introduction)

### Problem

- Information control and censorship have historically been used as instruments of power, limiting democratic access to knowledge.
- Centralized systems enable narrative manipulation and cultural erasure.
- There is a need for decentralized, censorship-resistant access to information and for mechanisms that support anonymous sharing when needed.

### Objective

- AlLibrary aims to be a decentralized library platform with the capability for anonymous document sharing when users require it.
- This phase establishes the research basis and validates the feasibility of integrating anonymous transfer (Tor/onion services) into the platform.

### Relevance of Anonymous Transfer

- Tor and onion services provide anonymity and censorship resistance for both readers and sharers.
- Anonymous share/receive is relevant to anti-censorship goals and to privacy in sensitive or high-risk contexts.
- A proof-of-concept will validate architecture and performance before full integration (Phase 6).

---

## 2. Revisão Bibliográfica (Literature Review / State of the Art)

### Tor and Onion Services

- **Tor design**: Foundational work on onion routing (e.g. Dingledine, Mathewson & Syverson, *Tor: The second-generation onion router*, USENIX Security Symposium 2004) and subsequent surveys on the Tor anonymity network.
- **Onion services**: Use of .onion hidden services for hosting content and services without exposing server or client IPs; relevance to censorship resistance and privacy.

### P2P and Anonymity

- **Decentralized anonymity**: Literature on scaling strong anonymity in decentralized networks (e.g. DAENet-style and mix-network approaches).
- **Next-generation P2P**: Comparative work on IPFS and related P2P data networks; the challenge of strong, censorship-resistant anonymity in P2P transfer.
- **Academic references**: To be drawn from established surveys and papers on Tor anonymity, P2P systems, and secure file sharing (sources to be listed in the formal literature review document).

### Related Work: OnionShare

- **OnionShare** provides anonymous file share and receive over Tor via a local HTTP server exposed as an onion service.
- **Modes**: Share (serve files/folders for download), Receive (accept uploads and text messages), plus optional Website and Chat modes.
- **Project documentation**: The AlLibrary project maintains an analysis of how OnionShare works and integration options:
  - [Docs/onionshare/README.md](../../Docs/onionshare/README.md)
  - [Docs/onionshare/how-onionshare-works.md](../../Docs/onionshare/how-onionshare-works.md)
- **Integration options for AlLibrary**:
  - **Option A (Subprocess)**: Run OnionShare CLI from Tauri; minimal implementation effort; requires OnionShare as dependency.
  - **Option B (Rust port)**: Port OnionShare-like behaviour to Rust within AlLibrary; single binary, full control; see [Docs/onionshare/onionshare-rust-port/README.md](../../Docs/onionshare/onionshare-rust-port/README.md).

The literature review section of the thesis will cite OnionShare as related work and reference the project’s OnionShare documentation for functional analysis and Option A vs B comparison.

---

## 3. Materiais e Métodos / Metodologia (Materials and Methods)

### Proof of Concept (to be carried out)

A proof-of-concept for anonymous file sharing via Tor onion services will be designed and implemented to:

- Validate technical feasibility (Tor, hidden services, HTTP server, chunked transfer).
- Inform the choice between OnionShare Option A (subprocess) and Option B (Rust port) for AlLibrary.
- Produce a short report on architecture, performance, and recommendation.

**Planned POC scope** (described as future work):

1. **Tor and hidden service**: Local Tor process (or connection to existing Tor); creation of an onion v3 hidden service mapping to a local port.
2. **HTTP server**: A simple HTTP server (e.g. Axum in Rust) to serve files (share mode) and/or accept file uploads (receive mode).
3. **Optional tracker/lobby**: Lightweight in-memory “tracker” or lobby for discovery (no persistent file storage) to explore P2P discovery over Tor.
4. **Chunked transfer**: Files transferred in chunks; optional per-chunk encryption (e.g. XChaCha20-Poly1305) for confidentiality.
5. **Minimal GUI or CLI**: A small interface to exercise share and receive and to verify that traffic is routed via Tor and that anonymity properties hold in tests.

### Methods

- **Literature review**: Tor, P2P, anonymity, and related work (including OnionShare).
- **Functional analysis of OnionShare**: Using project docs under [Docs/onionshare](../../Docs/onionshare) (modes, components, integration options).
- **POC design**: Architecture and data flow for the planned POC.
- **POC implementation and tests**: Implementation of the above scope and basic tests (connectivity, transfer, optional encryption).
- **Outcome**: Recommendation for AlLibrary (Option A vs Option B) and reference to [Docs/onionshare/onionshare-rust-port](../../Docs/onionshare/onionshare-rust-port) for the chosen path.

### Deliverables (planned)

- Written introduction and literature review sections (thesis/TCC).
- Methodology and POC design document.
- POC implementation and short report (architecture, performance, lessons learned).
- Recommendation: Option A vs Option B for AlLibrary, with pointer to [Docs/onionshare/onionshare-rust-port](../../Docs/onionshare/onionshare-rust-port) for implementation (e.g. architecture overview and implementation roadmap).

---

## 4. Integration with Later Phases

- **Phase 1**: Development can proceed in parallel or after Phase 0; no technical dependency.
- **Phase 4 (P2P and Tor overlay)**: Will provide Tor manager and hidden-service support; Phase 0 POC validates concepts that Phase 4 and Phase 6 build on.
- **Phase 6 (Security and anti-censorship)**: Will implement full TOR integration and OnionShare-style anonymous share/receive per the Option A or B decision; see [Docs/onionshare/onionshare-rust-port](../../Docs/onionshare/onionshare-rust-port) for the Rust port specification (Option B).

---

## 5. References (project documentation)

- [Docs/onionshare](../../Docs/onionshare) – OnionShare analysis and integration options
- [Docs/onionshare/how-onionshare-works.md](../../Docs/onionshare/how-onionshare-works.md) – Original OnionShare behaviour
- [Docs/onionshare/onionshare-rust-port/README.md](../../Docs/onionshare/onionshare-rust-port/README.md) – Option B: Rust port overview
- [Docs/onionshare/onionshare-rust-port/01_architecture_overview.md](../../Docs/onionshare/onionshare-rust-port/01_architecture_overview.md) – Architecture and integration points
- [Docs/onionshare/onionshare-rust-port/06_implementation_roadmap.md](../../Docs/onionshare/onionshare-rust-port/06_implementation_roadmap.md) – Phased implementation (Share mode, Receive mode, etc.)

Academic references (Tor, P2P, anonymity) will be listed in the formal literature review document and in the thesis reference list.
