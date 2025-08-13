# Papers Index

## Fake News

- [Trends in Cognitive Sciences article](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613(21)00051-6?dgcid=raven_jbs_etoc_email)
- [Science article](https://www.science.org/doi/abs/10.1126/science.aao2998)
- [ScienceDirect article](https://www.sciencedirect.com/science/article/abs/pii/S0306457318306794)

## SolidJS (performance, reactivity, frontend framework)

- [JCSI article](https://ph.pollub.pl/index.php/jcsi/article/view/6712)
- [Benchmarking Modern Frontend Frameworks - A Comparative Performance Analysis](https://webthesis.biblio.polito.it/35401/1/tesi.pdf)

## Tartarian Empire / Tartaria / Great Tartary

- [Google Books result](https://books.google.com.br/books?hl=pt-BR&lr=&id=WDYsAQAAMAAJ&oi=fnd&pg=PR1&dq=%22Tartarian+Empire%22+OR+Tartaria+OR+%22Great+Tartary%22&ots=pp2jA9dWnw&sig=_XAIqpuGBte-m5Cb3OuNsqvmJu4&redir_esc=y#v=onepage&q=%22Tartarian%20Empire%22%20OR%20Tartaria%20OR%20%22Great%20Tartary%22&f=false)
- [Deutsche Biographie: Philipp Johann von Strahlenberg](https://www.deutsche-biographie.de/sfz125638.html#ndbcontent)

## Intended Research Topics

# Human-Centered Research Topics for AlLibrary

## Information freedom and society

- Historical censorship patterns: comparative case studies across regions
- Effects of decentralized access on civic literacy and democratic participation
- Ethical frameworks: information paternalism vs user autonomy
- Cultural preservation as a public good: indigenous knowledge stewardship (information-only approach)

## Trust, provenance, and misinformation

- Source provenance standards for community libraries and amateur archivists
- Human-in-the-loop verification workflows that scale without gatekeeping
- Community reputation models that avoid central authority and bias
- UX patterns for credibility indicators and anti-dark-pattern design

## Cultural sensitivity and ethics

- Guidelines for respectful representation of cultures and communities
- Cultural context annotations vs access control: informing without restricting
- Handling sensitive/sacred content using an information-only model
- Attribution, consent, and community voices in metadata and narratives

## Governance and community operations

- Lightweight governance models: deliberation, consent, and transparency
- Moderation in decentralized systems: processes, escalation, and appeals
- Abuse mitigation vs freedom of expression: norms, tooling, and education
- Contributor onboarding, roles, incentives, and recognition systems

## Legal and compliance in practice

- Takedown processes (e.g., DMCA) in P2P settings: workflows and safeguards
- Jurisdictional conflicts and user risk mitigation in global networks
- Licensing education (Creative Commons) and default choices for contributors
- Data protection and privacy UX for local-first, P2P applications

## Accessibility and inclusion

- Low-bandwidth and intermittent-connectivity design patterns
- Screen reader affordances within desktop webviews (NVDA/JAWS) and keyboard-first UX
- Script coverage, font fallback, and RTL support in knowledge apps
- Cognitive accessibility for long-form reading, annotations, and dense UIs

## Education and pedagogy

- Classroom and university use cases for decentralized archives
- Information literacy curricula leveraging provenance and verification features
- Annotation as a learning activity: prompts, rubrics, and peer feedback
- Measuring learning outcomes and research skills development

## Adoption and field research

- User research in libraries, schools, and community centers
- Barriers to adoption and trust-building strategies in diverse contexts
- Offline-first workflows for constrained environments (power, bandwidth, devices)
- Success metrics and impact evaluations grounded in community goals

## Archival practice and community stewardship

- Community archiving methods: consent, attribution, and representation
- Selecting, describing, and preserving local materials with minimal resources
- Ethical digitization guidelines and cultural protocols
- Sustainability models for community-run archives and nodes

## UX for knowledge work

- Knowledge graph comprehension for non-experts and progressive disclosure
- Search and filtering UX for very large personal and community libraries
- Annotation/quoting workflows and shareable, verifiable references
- Credibility metadata and provenance surfaced without overwhelming users

## Global equity and the digital divide

- Device and power constraints: durability, portability, and resilience
- Community-run nodes: ownership, maintenance, and training models
- Multilingual UX research priorities and culturally responsive interfaces

## Measurement and community monitoring

- Privacy-preserving, opt-in telemetry frameworks for desktop apps
- Community dashboards that respect agency and minimize surveillance risks
- Qualitative feedback loops and continuous community research practices




### P2P networking and distribution
- libp2p gossipsub tuning AND Windows WebView2
- Kademlia DHT parameter tuning (alpha, k-bucket) libp2p
- NAT traversal hole punching libp2p relay v2
- IPFS pinning strategies desktop clients
- IPLD data modeling for documents and metadata

### Content-addressed storage and data layer
- SQLite FTS5 + IPFS CID mapping design
- CAR files vs raw blocks for archival
- Merkle proofs AND content verification (IPLD)
- Chunking strategies for large PDFs in IPFS

### Local and network search
- SQLite FTS5 vs Tantivy vs Meilisearch desktop
- Incremental indexing of PDFs (text + OCR)
- Semantic search offline (sentence-transformers Rust)
- Federated search across peers (privacy-preserving) libp2p

### Document processing pipeline
- Rust PDF text extraction (pdfium-render, lopdf)
- OCR with Tesseract from Tauri
- Metadata standards: Dublin Core, schema.org, IIIF
- Deduplication via perceptual hashes (PDF/thumbnail)

### Collections, ranking, and recommendations
- Topic modeling (LDA vs BERTopic) local-first
- Keyword extraction (YAKE, TextRank) Rust/TS
- Graph-based recommendations (knowledge graphs)
- Relevance ranking (BM25 vs hybrid dense-sparse)

### Security and privacy
- End-to-end encryption for stored documents (age/NaCl)
- Key management UX desktop apps (backup, rotation)
- Content signing and verification (ed25519 + IPLD links)
- Threat modeling for Tauri (CSP, isolation, IPC hardening)

### Performance and optimization
- Windows WebView2 performance tuning (cache, GPU)
- SolidJS code splitting + lazy routes in desktop
- Canvas/WebGL rendering for thumbnails and previews
- Rust + WASM for intensive text processing

### Tauri app architecture and operations
- Auto-update channels + code signing (Windows/macOS)
- Filesystem sandbox and scoped permissions
- Crash reporting and telemetry (opt-in) with Sentry
- Background tasks/schedulers in Tauri

### Internationalization and accessibility
- ICU MessageFormat + pluralization (i18n) Solid/Tauri
- RTL support, font fallback, glyph coverage
- NVDA/JAWS screen reader support in WebView2
- Date/number localization and timezone handling

### Offline-first sync and conflict resolution
- CRDTs (Automerge/Yjs) for annotations and notes
- Sync strategies (push/pull, backoff, resumable)
- Delta sync and compression over libp2p
- Versioning and rollback of documents

### Governance, legal, and compliance
- Content licensing (CC BY/SA/NC) in P2P contexts
- DMCA/GDPR compliance for decentralized apps
- Trust, reputation, and abuse mitigation in P2P
- Transparency reports for decentralized networks

### Dev workflow, testing, and release
- UI automation for Tauri (Playwright) desktop
- Network simulation tests for libp2p (latency, churn)
- Binary size optimization and symbol stripping
- Reproducible builds and SBOM generation

### Monitoring and reliability
- Local health metrics for P2P node (libp2p)
- Content availability tracking and repair
- Persistent caching layers (LRU + pinning policies)
- Backup/restore for SQLite + IPFS blocks

### Data ethics and cultural context
- Bias and provenance in community collections
- Cultural metadata enrichment and safeguards
- Community moderation workflows in decentralized systems

### UX for knowledge work
- Knowledge graph visualization patterns desktop
- Advanced filtering UX for large local libraries
- Annotation/quote workflows (export, share, verify)

### Integration and extensibility
- Plugin architecture for importers/exporters
- Interop with Zotero/Calibre (metadata + CIDs)
- Web capture → IPFS pipeline with verification

### Deployment and distribution
- Delta updates for large binaries on Windows
- Portable vs installed modes for Tauri apps
- Enterprise policy deployment and lockdown

### Accessibility and performance audits
- WCAG 2.2 audits inside WebView
- PDF accessibility (tags, structure, landmarks)
- Color contrast and keyboard navigation at scale

### Future-leaning research
- Private information retrieval for P2P search
- Verifiable credentials for content authorship
- Content authenticity (C2PA) + IPFS linkage
