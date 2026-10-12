# Capítulo 6 — Protocolo experimental (Analytics + DHT/Gossip)

Roteiro reprodutível para evidências **measured-only** (`is_simulated=false`) alinhado ao Report 4 (metas 6.1–6.3).

## Pré-requisitos

1. Tracker: `TrackerRust_AlLibrary` em `http://127.0.0.1:8080`
2. Analytics Django: migrate + `runserver 127.0.0.1:8000`
3. Next dashboard: `pnpm dev` em `AnalyticsNextApp_AlLibrary`
4. N desktops (10–15) com Tor + onion share iniciado

## Endpoints de medição

| Fonte | Endpoint / comando |
|-------|-------------------|
| Tracker churn | `GET /metrics/churn` |
| Tracker presença | `GET /metrics/presence` |
| DHT bootstrap | `GET /dht/bootstrap` |
| Desktop DHT | Tauri `bootstrap_kad`, `run_dht_lookup_benchmark` |
| Desktop gossip | Tauri `gossip_announce_content` |
| Export | Tauri `export_anonymous_telemetry` |
| Ingest | `POST /api/v1/telemetry/ingest/` |
| KPIs Cap. 6 | `GET /api/v1/experiment/summary/?include_simulated=0` |
| Collector | `python manage.py collect_tracker_metrics` |

## Passos

### A. Rede e churn (meta 6.1)

1. Subir tracker; iniciar N nós desktop com announce/WS.
2. Em loop (cron ou manual): `collect_tracker_metrics --tracker http://127.0.0.1:8080`
3. Forçar churn: encerrar 2–3 nós; registrar `node_leave` / `stale_evict`.
4. Capturar `experiment/summary` → bloco `churn` e `nodes.online`.

### B. Lookup DHT (meta 6.1)

1. Em cada nó: `bootstrap_kad`.
2. Escolher `content_hash` anunciado no lobby.
3. Bateria: `run_dht_lookup_benchmark(content_hash)` com N crescente (5, 10, 15).
4. Export + ingest; gráfico **duration_ms p50/p95** e **avg_hops** vs N.

### C. Gossip (meta 6.1)

1. Nó A: `gossip_announce_content(hash, size)`.
2. Demais nós recebem via `/gossip/recv` (rede Tor).
3. Export eventos `gossip`; curva **propagation_ms** p50/p95.

### D. Transferências onion-share (meta 6.2)

1. Downloads variando tamanho × seeders × churn durante transferência.
2. Completar fetches; `export_anonymous_telemetry` → ingest.
3. KPIs: success_rate, duration p50/p95, speed p50/p95, retries_avg, integrity.

### E. Fechamento

1. Painel Next → aba **Experimento** com `include_simulated=0`.
2. Screenshots + tabelas para Cap. 6 / Cap. 7.
3. Seed (`seed_tcc_analytics`) permanece apenas demonstração; não citar como amostra medida.

## O que não afirma este protocolo

- Equivalência a BitTorrent/IPFS global
- Resistência a adversário passivo global no Tor
- Identidade do leitor (nunca coletada)
