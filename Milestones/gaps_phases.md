# Gaps by Phase (0 → 4) and Corrective Action Plan

Scope: Analysis of `DesktopApp_AlLibrary/` vs milestones up to Phase 4 under:
- Coding rules: `.cursor/rules/allibrary-coding-rules.mdc`
- Coherence rules: `.cursor/rules/allibrary-coherence-rules.mdc`
- Custom rules: `.cursor/rules/allibrary-custom-rules.mdc`

References: `Screens+SoftwareEngineering/00_DEVELOPMENT_ARCHITECTURE_GUIDE.md`, `01_IMPLEMENTATION_WORKFLOW_GUIDE.md`, system/page diagrams.

---

## Status Snapshot


| Phase | Target Focus | Status | Notes |
|------:|---------------|--------|-------|
| 0 | Project foundation | Complete | Scaffold, SQLite, routing, base screens done |
| 1 | Arch. restructuring + cultural info-only + security validation | Mostly complete | Structure/services/validation present; audit info-only, routing hygiene, coverage |
| 2 | Foundation components + document management | Partially complete | Components/services/pages present; a11y/tests/perf budgets need work |
| 3 | P2P + distributed search + anti-censorship | Partially complete | Network services/UI exist; tests/metrics/behaviors incomplete |
| 4 | Collaboration/advanced features | Not complete | Sharing/comments flows not end-to-end |

---

## Phase 0 – Foundation (Complete)

No action required. Keep baseline metrics updated in `progress/`.

---

## Phase 1 – Architectural Restructuring


### Gaps (Phase 1)
- Cultural info-only enforcement: ensure no cultural approval/permission/gating exists; features provide education/info only.
- Routing hygiene: `/search-network` routes to `SearchPage`; placeholders exist for `/new-arrivals`, `/sharing`, `/downloads`, `/sync`.
- Coverage/gates: TS strict ≥95% and tests ≥80% not enforced in CI.

### Corrective Tasks (Phase 1)
1. Cultural info-only audit
   - Review: `src/components/cultural/**`, `src/services/validation/culturalValidator.ts`, `src/services/**/access*`, `src/stores/cultural/**`.
   - Action: remove/avoid cultural access checks; convert to information display/logging only; keep technical security (malware/legal) intact.
   - Output: ADR in `progress/Recent_History.md` stating info-only policy is enforced in code.

2. Router consistency
   - Update `src/routes/AppRouter.tsx` to map `/search-network` → `SearchNetworkPage`.
   - Replace inline placeholder components with real pages or lazy stubs for `/new-arrivals`, `/sharing`, `/downloads`, `/sync`.

3. CI quality gates
   - Add coverage thresholds (TS strict ≥95%, tests ≥80%) and a cultural compliance assertion test.

### Acceptance Criteria (Phase 1)
- No cultural access control anywhere (tests verify info-only behavior).
- Routes correct; no inline placeholders.
- CI enforces coverage thresholds.

---

## Phase 2 – Foundation Components & Document Management


### Gaps (Phase 2)
- Foundation a11y + unit tests to ≥80%.
- Import pipeline: malware/legal checks before persist; cultural metadata persisted as info-only.
- Local search performance targets unverified (<500ms typical).

### Corrective Tasks (Phase 2)
1. A11y/tests for foundation components
   - Add aria/keyboard patterns and tests to `Button`, `Input`, `Card`, `Modal`, `Loading`, `LanguageSwitcher`, etc.

2. Secure import pipeline tests
   - Ensure order: sanitize → malware scan → legal check → persist (+ cultural info metadata).
   - Add integration tests: happy path + blocked malware/legal.

3. Search performance tests
   - Optimize SQLite/FTS, pagination; add tests asserting <500ms median on typical dataset.

### Acceptance Criteria (Phase 2)
- Foundations pass a11y tests; coverage ≥80%.
- Import pipeline blocks malware/illegal; cultural metadata stored; no access gating.
- Local search <500ms in tests.

---

## Phase 3 – P2P Network & Distributed Search


### Gaps (Phase 3)
- Connectivity/replication/distributed search behaviors not validated.
- Anti-censorship fallbacks untested (transport diversity/TOR readiness).
- Cultural distribution must remain informational.

### Corrective Tasks (Phase 3)
1. Connectivity & replication tests for `p2pNetworkService` and `ipfsService`.
2. Distributed search demo + tests via `P2PSearch` and `useNetworkSearch` (aggregate, label cultural context, no filtering; <2s target).
3. Anti-censorship validation for transport fallback and TOR readiness.

### Acceptance Criteria (Phase 3)
- Multi-transport connections succeed; replication ≥90% reliability.
- Distributed search aggregate works; cultural labels shown; <2s in tests.
- Resilience tests pass basic block scenarios.

---

## Phase 4 – Collaboration / Advanced Features


### Gaps (Phase 4)
- Missing end-to-end commenting and sharing flows.

### Corrective Tasks (Phase 4)
1. Commenting & activity feed components; integrate in `pages/DocumentDetail`.
2. Sharing dialog + P2P notifications/audit trail (within constraints).
3. Tests: unit/integration/e2e for comment CRUD and share-and-open.

### Acceptance Criteria (Phase 4)
- Comments persist/sync; share flows operational; a11y pass; cultural info-only preserved.

---

## Cross-Phase Enablers (Immediate)

- Lazy route loading: implemented using `lazy()` + `Suspense` in `src/routes/AppRouter.tsx`; loading fallbacks added. (grep confirms `lazy(` usage.)
- Performance budgets: add bundle/TTI/memory tests per `optimization/code-splitting-guide.md`.
- Progress: maintain `progress/Implementation_Gaps_Tasks.md`, `Project_Progress.md`, `Recent_History.md`.

## Task Register (Actionable)

- Router corrections + lazy loading (P1, cross-phase)
- Cultural info-only audit/remediation (P1)
- Foundation a11y + tests (P2)
- Import pipeline validation tests (P2)
- Local search perf test (<500ms) (P2)
- P2P connectivity/replication tests (P3)
- Distributed search aggregation UI/tests (P3)
- Anti-censorship fallback tests (P3)
- Comments/sharing E2E flows and tests (P4)

## Definition of Done (per phase)

- Phase 1: Structure fixed, cultural info-only enforced, quality gates active.
- Phase 2: Foundation components a11y+tests, secure import pipeline, fast local search.
- Phase 3: P2P behaviors validated, distributed search demo, resilience tests.
- Phase 4: Collaboration flows implemented and tested, cultural info-only assured.

---

## Detailed Evidence Snapshot (Repo Pointers)

- Aliases & bundling: `vite.config.ts` (aliases set; manualChunks present; lazy routes now active in router).
- Pages present: `src/pages/{Home,Search,SearchNetwork,Collections,Favorites,Recent,Trending,Browse,NewArrivals?,Peers,NetworkHealth,P2PSearch,ConnectionManager,CulturalContexts,TraditionalKnowledge,CommunityGuidelines,Preservation,DocumentReader,Settings}` (some routes not wired/placeholder).
- Cultural UI: `src/components/cultural/**` (Context, Indicator, Education, etc.).
- Validation: `src/services/validation/{culturalValidator,securityValidator,documentValidator}.ts` + tests under `validation/__tests__`.
- Network: `src/services/network/{p2pNetworkService,ipfsService,torService}.ts`, NetworkGraph composite with tests.
- i18n: `src/i18n/locales/{en,es,fr,pt,zh,ar,hi?,qu,mi,nv,de,it,ja}/...` (broad coverage present).
- Tests: NetworkGraph responsiveness, services tests, e2e `tests/e2e/home-page.spec.ts`.

## Phase 1 – Action Breakdown (Work Items)

- A1.1 Code search task: identify any `deny`, `restrict`, `approval`, `permission` tied to culture; open issues for each occurrence; remediate.
- A1.2 Add `CulturalInfoPolicy.test.ts` asserting components render `informationOnly` semantics and never gate access.
- A1.3 Replace inline routes with lazy imports:
  - Create `RouteLoading` component (spinner/placeholder)
  - Wrap routes with `<Suspense fallback={<RouteLoading/>}>`
- A1.4 Add CI config: vitest coverage thresholds + type-check step fail on errors.

KPIs
- ≤ 0 policy violations; routes all lazy; CI passing with configured gates.

### Phase 1 – Status Update (2025-08-11)
- Router consistency: Completed. `/search-network` now maps to `SearchNetworkPage`; placeholders replaced with lazy-loaded pages.
- Lazy route loading: Completed. All major routes use `lazy()` with `Suspense` fallback.
- Tests: All unit/integration tests passing (284/284). CI coverage thresholds pending configuration.

## Phase 2 – Action Breakdown

- B2.1 A11y checklists per component (role, name, state; keyboard nav; focus trap for Modal).
- B2.2 Tests: per component `.test.tsx` with @solidjs/testing-library; snapshot optional; a11y assertions.
- B2.3 Import integration tests:
  - `upload.good.spec.ts`: sanitize→malware→legal→persist; assert cultural info is saved
  - `upload.malware.spec.ts`: blocks with error; DB untouched
  - `upload.legal.spec.ts`: blocks with error; DB untouched
- B2.4 Search perf tests: generate fixture dataset (N=1k); run timed query; assert p50 <500ms.

KPIs
- Foundation coverage ≥80%; import blocked cases 100%; p50 search <500ms.

### Phase 2 – Status Update (2025-08-12)
- A11y tests: Added `Modal` a11y tests (dialog role, aria-modal, ESC, backdrop) – passing.
- Import pipeline tests: Added upload service integration tests for happy path, malware block, legal block – passing.
- Local search performance: Added median <500ms performance test – passing under mocked invoke timing.

## Phase 3 – Action Breakdown

- C3.1 Connectivity tests: mock transports; simulate intermittent failure; measure recovery <2s.
- C3.2 Replication/integrity: push content → replicate → verify hash equality across peers.
- C3.3 Distributed search: mock N peers; aggregate; show cultural labels; measure p95 <2s.
- C3.4 Anti-censorship: simulate transport block; verify fallback; document TOR readiness toggle path (Settings in Phase 5).

KPIs
- Connect success ≥90%; recovery <2s; replication integrity >99.9%; distributed search p95 <2s.

## Phase 4 – Action Breakdown

- D4.1 Design Comment model (id, docId, author, text, createdAt, editedAt, reactions?).
- D4.2 UI: `CommentList`, `CommentComposer`, `ActivityFeed`, `ShareDialog` (with a11y and i18n).
- D4.3 Service: `commentService.ts` (local-first), `shareService.ts` (P2P notification or local link semantics); offline queue.
- D4.4 Tests: Unit (models/services), Integration (DocumentDetail w/ comments), E2E (share-and-open path).

KPIs
- Comments latency (local) <200ms; E2E pass rate ≥95% for share scenario.

### Phase 4 – Status Update (2025-08-12)
- Implemented real data flows on `DocumentDetail`:
  - Comments: list/add/edit/delete via Tauri (`list_comments`, `add_comment`, `edit_comment`, `delete_comment`).
  - Sharing: P2P share (`share_document_p2p`) and share link (`create_share_link`), peer selection via `getConnectedPeers`.
  - UI: Community tab with composer and list; Share modal with peers list; toasts for add/edit/delete/share.
- Tests added for services (`commentService`, `shareService`); full test suite green.

Acceptance Criteria Status
- Comments: add/edit/delete/list via real endpoints – DONE
- Sharing: P2P share + share link with UI feedback – DONE
- Favorites: toggle and persistence with real command + local fallback – DONE
- Counters: view/favorite/comment counts wired via `get_document_stats`; view increments on open – DONE
- i18n: all toasts localized in `pages.documentDetail.toasts` – DONE

## Dependencies & Ordering

1) Router + lazy load (A1.3) → unlocks perf tests and route-level budgets.
2) Cultural policy audit (A1.1) → needed before P2P tests to avoid false gating.
3) A11y/tests (B2.1–B2.2) → raises coverage to pass CI.
4) Import tests (B2.3) → sec/legal compliance validated.
5) Search perf (B2.4) → user experience baseline.
6) P2P tests (C3.1–C3.4) → network readiness.
7) Collaboration (D4.x) → feature completeness for Phase 4.

## Reporting & Dashboards

- Add `scripts/report-metrics.ts` to read coverage/perf logs and write to `progress/Project_Progress.md`.
- Track per-commit: coverage, p50/p95 search, bundle size, TTI, memory idle, P2P connect success.

## Risks & Mitigations

- R1: Lazy loading regressions → add route E2E smoke tests.
- R2: Over-zealous cultural removals → policy is info-only, not removal; ensure UI still shows educational context.
- R3: Perf flakiness → stabilize by fixed dataset and controlled env in tests.

## Test Index (Expanded)
- T1 Cultural info-only policy enforcement
- T2 Router mapping/no-placeholder
- T3 CI gates (coverage/type)
- T4 Foundations a11y+coverage
- T5 Import pipeline integration
- T6 Local search performance
- T7 Connectivity reliability
- T8 Replication integrity
- T9 Distributed search latency
- T10 Comments lifecycle
- T11 Share-and-open
- T12 Collaboration a11y
- T13 Route lazy-loading smoke
- T14 Bundle/TTI/memory budgets

## Metrics (Concrete Targets)
- Coverage (global): ≥80% | TS strict pass 100%
- Bundle initial: ≤250KB; TTI ≤1.5s; memory idle ≤50MB (post-Phase 6 expected, start tracking now)
- NetworkGraph FPS ≥60 sustained with test dataset
- P2P: connect ≥90%, recover <2s; replication integrity >99.9%

---

## Phase 5 – Security & Anti‑Censorship (Planned Additions)

### Gaps (Phase 5)

- TOR transport toggle not surfaced in UI; transport fallback not exercised in tests.
- IPC hardening checks not automated in CI.
- Legal-only filtering gate not codified in validation pipeline report.

### Corrective Tasks (Phase 5)

- TOR UI & Settings
  - Add `Settings/TorIntegrationPanel` to enable/disable TOR; persist in settings service; expose state to network services.
  - Integration test: start with TOR on/off, assert transport selection changes behavior.

- IPC Hardening & Input Sanitization
  - Audit all Tauri commands for argument validation; add schema checks; fuzz basic malformed inputs in tests.

- CI Security Gate
  - Add dev script to run dependency audit and basic static scan; fail build on high severity.

### Acceptance Criteria (Phase 5)

- TOR toggle functional; transport fallback verified by tests.
- IPC misuse tests pass; sanitization enforced.
- CI blocks on security issues; cultural filtering remains zero.

### KPIs (Phase 5)

- TOR path OK; 0 high vulns; 0 cultural blocks; 100% IPC inputs validated.

---

## Phase 6 – Performance & Optimization (Planned Additions)

### Gaps (Phase 6)

- Bundle/TTI/memory budgets not yet enforced by tests.
- NetworkGraph perf telemetry not reported.

### Corrective Tasks (Phase 6)

- Route/component code-splitting verification tests; assert lazy chunks created.
- Perf test suite: record bundle size, TTI, memory idle; export metrics JSON for dashboards.
- NetworkGraph FPS measurement on fixture dataset; fix hotspots using `utils/performance.ts`.

### Acceptance Criteria (Phase 6)

- Initial bundle ≤250KB; TTI ≤1.5s; memory idle ≤50MB (dev machine baseline).
- NetworkGraph ≥60 FPS on fixture.

### KPIs (Phase 6)

- Budgets green in CI; perf JSON published to `progress/` scripts.

---

## Phase 7 – Hardening, QA, Docs (Planned Additions)

### Gaps (Phase 7)

- Coverage gates not enforced in CI; a11y/perf/security e2e suites incomplete.
- Docs not cross-linked to Screens+SoftwareEngineering for all pages.

### Corrective Tasks (Phase 7)

- CI Coverage Gates: tests ≥80%, TS strict 100% pass required.
- A11y suite: add WCAG checks to critical pages; keyboard nav and ARIA assertions.
- Perf & Security e2e: smoke per route; injection/path traversal checks.
- Docs linkage: ensure each page links to its 01/02/03/04 docs.

### Acceptance Criteria (Phase 7)

- CI enforces gates; e2e runs stable; docs linked.

### KPIs (Phase 7)

- ≥80% tests; 0 a11y criticals; all routes smoke green.

---

## Phase 8 – Release & Ops (Planned Additions)

### Gaps (Phase 8)

- Release checklist, rollback plan, and telemetry sanity not codified.

### Corrective Tasks (Phase 8)

- Release Notes + Migration Notes templates.
- Telemetry sanity tests pre-release; smoke with upgrade/downgrade.
- Feedback channels documented in `Docs/deployment/`.

### Acceptance Criteria (Phase 8)

- Tagged release with notes; rollback steps tested; post-release triage checklist exists.

### KPIs (Phase 8)

- 0 critical regressions; telemetry healthy; docs published.
