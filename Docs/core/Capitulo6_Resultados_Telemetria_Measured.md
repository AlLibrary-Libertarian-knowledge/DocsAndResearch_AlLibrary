# AlLibrary — Resultados de telemetria measured (Cap. 6)

**Fonte:** Analytics Hub (`is_simulated=false`)  
**Atualizado em:** 2026-10-12 ~18:30 (BRT)  
**PoC:** DesktopApp v0.0.2 (Tor/onion) + PeerLab **52 VMs** (LAN Docker; cidades = metadado)  
**Hub:** TrackerRust `:8080` · Django `:8000` · Dashboard `:3000`

> Distinguir **(A) Tor doméstico** (1 seeder) de **(B) PeerLab** (sweep 2→20, multi-leecher, churn %, join dinâmico).

---

## 1. KPIs — visão consolidada

| Indicador | (A) Tor doméstico | (B) PeerLab seeder-sweep |
|-----------|------------------:|-------------------------:|
| Nós | 4 Desktops | **52** peers Docker |
| Documentos | Fahrenheit / Quixote / Historico | mesmos **títulos** (réplicas lab) |
| Runs úteis | 6 | **57** (3 docs × 19 níveis de seeders) |
| Sucesso | 100% | **100% (57/57)** |
| Seeds paralelos | 1 | **2 … 20** (forçado) |
| Throughput típico | ~33–154 kbps | ~6,4–10,3 **Mbps** (LAN) |
| Churn mid-transfer | não | sim (bateria anterior) |

---

## 2. (A) Sessões Tor P2P — Desktops (familiares)

### 2.1 Sessões únicas (`n = 6`)

| # | Documento | MB | Início (BRT) | Duração (s) | kbps | MB/s | Chunks | Seeds |
|--:|-----------|---:|--------------|------------:|-----:|-----:|-------:|------:|
| 1 | An_Historico… | 28,70 | 01:35:45 | 235,682 | 124,7 | 0,122 | 115/115 | 1 |
| 2 | Fahrenheit 451… | 1,30 | 01:35:46 | 20,600 | 64,5 | 0,063 | 6/6 | 1 |
| 3 | Don Quixote… | 4,83 | 01:42:44 | 48,352 | 102,3 | 0,100 | 20/20 | 1 |
| 4 | An_Historico… | 28,70 | 12:48:49 | 190,796 | 154,0 | 0,150 | 115/115 | 1 |
| 5 | Don Quixote… | 4,83 | 12:48:50 | 54,087 | 91,4 | 0,089 | 20/20 | 1 |
| 6 | Fahrenheit 451… | 1,30 | 13:01:20 | 40,305 | 33,0 | 0,032 | 6/6 | 1 |

**Hashes Tor (originais):**

| Documento | content_hash |
|-----------|--------------|
| An_Historico… | `472650b81a7b23d44c417a8625c6462d5e54b3b22b49b13e500d49a17c826e00` |
| Don Quixote… | `f27b5cb292a268fa70ef3cf211f2cbc2cb31d59eefa1b4053e74347f18bf91c4` |
| Fahrenheit 451… | `fa882d6974416da1319ac21569e3d76936575506aa875ce70abe28b7922c38b7` |

### 2.2 Agregados Tor

| Métrica | Valor |
|---------|------:|
| Sucesso / integridade | 100% |
| Throughput médio | ≈ 95 kbps |
| Seeds | sempre 1 |

---

## 3. (B) PeerLab — matriz de seeders 2→20 (insumo Cap. 6)

**Método:** 21 peers (SP downloader + 20 seeders). Contagem de seeders **forçada** via  
`POST /lab/download/{hash}?seeders=peer-rj,…` (bypass de lag do lobby).  
RTT sintético por cidade permanece ativo no serve de chunks.

**Topologia (21):** SP, RJ, CWB, POA, REC, MAN, BSB, BH, SSA, FOR, FLN, GYN, CPS, VIX, NAT, **JPA, MCZ, THE, CGR, CGB, RAE**.

**Documentos lab (títulos reais no dashboard):**

| Documento | Tamanho | Chunks @64KiB | content_hash (lab) |
|-----------|--------:|--------------:|--------------------|
| Fahrenheit 451… | 1,30 MB | 21 | `91d0810f8a8a8d4b…2381bc8b` |
| Don Quixote… | 4,83 MB | 78 | `2a4a6aae912e344d…d9b2f65d` |
| An_Historico… | 8,00 MB | 128 | `ba68ac5e0507eccc…d7c2ad63` |

### 3.1 Tabela completa — throughput (kbps) × seeders × documento

| Seeds | Fahrenheit (kbps) | Quixote (kbps) | Historico (kbps) | Média (kbps) | Média (MB/s) |
|------:|------------------:|---------------:|-----------------:|-------------:|-------------:|
| 2 | 6404,6 | 6874,5 | 7041,2 | 6773,4 | 6,61 |
| 3 | 7752,5 | 8934,6 | 9501,3 | 8729,5 | 8,53 |
| 4 | 7945,4 | 10179,1 | 10268,5 | **9464,3** | **9,24** |
| 5 | 7490,7 | 8931,0 | 9046,2 | 8489,3 | 8,29 |
| 6 | 7872,8 | 8662,2 | 9233,7 | 8589,6 | 8,39 |
| 7 | 7421,6 | 9167,7 | 9734,5 | 8774,6 | 8,57 |
| 8 | 8077,5 | 9219,8 | 9462,3 | 8919,9 | 8,71 |
| 9 | 7791,4 | 8796,6 | 9186,4 | 8591,5 | 8,39 |
| 10 | 7639,3 | 8984,7 | 9275,1 | 8633,0 | 8,43 |
| 11 | 7755,3 | 9097,8 | 9517,6 | 8790,2 | 8,58 |
| 12 | 8365,7 | 9534,2 | 9843,9 | 9247,9 | 9,03 |
| 13 | 8944,6 | 9464,0 | 9853,9 | **9420,8** | **9,20** |
| 14 | 8554,3 | 9462,2 | 9508,2 | 9174,9 | 8,96 |
| 15 | 8244,9 | 9144,7 | 9500,2 | 8963,3 | 8,75 |
| 16 | 8216,1 | 8881,4 | 9149,9 | 8749,1 | 8,54 |
| 17 | 7954,5 | 8779,5 | 9119,6 | 8617,9 | 8,42 |
| 18 | 8120,4 | 8986,8 | 9166,6 | 8757,9 | 8,55 |
| 19 | 7898,9 | 8676,4 | 9129,9 | 8568,4 | 8,37 |
| 20 | 7847,8 | 8830,5 | 9219,0 | 8632,4 | 8,43 |

**Todas as 57 células: status COMPLETED, chunk_failures = 0, retries = 0.**

### 3.2 Leitura para a conclusão

1. **Ganho forte 2→4 seeders:** média sobe de ~6,6 para ~9,2 MB/s (melhor região custo/benefício na LAN).  
2. **Platô após ~4–13 seeders:** ganhos marginais; em alguns pontos há leve queda (contenção / RTT / concurrency clamp 4).  
3. **Arquivos maiores aproveitam melhor o swarm:** Historico e Quixote > Fahrenheit no pico (~10,3 Mbps @ 4 seeds).  
4. **Escalabilidade funcional até 20 seeders:** 100% de sucesso — a lógica de chunks `(idx+offset)%N` sustenta o fan-out.  
5. **Tor vs lab:** Tor (~0,03–0,15 MB/s, 1 seed) ≪ lab LAN — o gargalo Tor é o circuito, não o escalonamento de seeders.

Artefato bruto: `PeerLab_AlLibrary/cap6_seeder_sweep.json`.

### 3.3 Agregados do sweep

| Métrica | Valor |
|---------|------:|
| Runs | 57 |
| Sucesso | 57/57 (100%) |
| Seeds testados | 2…20 |
| kbps min / max (célula) | 6404,6 / 10268,5 |
| Melhor média por N | **4 seeders** (9464 kbps) e **13 seeders** (9421 kbps) |

---

## 4. Insumos para a conclusão do Cap. 6

1. Integridade 100% em Tor (1-seed) e lab (2–20 seeds) com **52** peers.  
2. Multi-seeder **escala até 20** peers sem falha de transferência.  
3. Throughput sobe nitidamente até ~4 seeders; depois satura (LAN + concurrency).  
4. Distância/RTT sintético diferencia cidades (geo + multi-leecher: Manaus mais lento).  
5. Churn (perda de peers / %) gera retries, mas não impede conclusão se restar ≥1 seeder.  
6. Drop aleatório de chunks (`CHAOS_DROP_PCT`) → retries>0 com COMPLETED.  
7. Join dinâmico e seed-under-load permanecem COMPLETED.  
8. Cold start announce→lobby ~2 s.  
9. Dashboard com **títulos reais** (Fahrenheit / Quixote / Historico).  
10. Tor ≪ Lab no mesmo título (ordem de grandeza 50–100× na LAN).

---

## 5. Limitações remanescentes

1. PeerLab = réplicas lab (hashes ≠ Tor); títulos alinhados.  
2. Sessões Tor antigas no hub ainda com latency 0 — só transfers **após** rebuild Desktop.  
3. Gossip ainda sem emit automático (lookup já ativo no PeerLab).  
4. Concurrency de swarm no lab limitada (`SWARM_CONCURRENCY=4`) — explica platô.  
5. Cidades = metadado experimental.

---

## 6. Como reproduzir

```text
cd c:\TCC\PeerLab_AlLibrary
python scripts\gen_compose.py
python scripts\gen_seeds.py
docker compose up -d --build
python scripts\run_seeder_sweep.py --min 2 --max 20 --docs all
python scripts\run_multi_leecher.py
python scripts\run_churn_pct.py
python scripts\run_join_midway.py
```

---

## 7. Bateria estendida (52 peers) — 2026-10-12

### 7.1 B4 Multi-leecher (Quixote, 8 seeders, 8 leechers)

| Métrica | Valor |
|---------|------:|
| Solo SP | 9412,7 kbps |
| Paralelo (média 8) | 8054,6 kbps |
| Contenção | sim (solo > paralelo) |
| Sucesso | **8/8** COMPLETED |

Artefato: `PeerLab_AlLibrary/cap6_multi_leecher.json`.

### 7.2 B5 Churn parametrizado (Historico, N=20)

| % offline | status | retries | fails | kbps | wall (s) |
|----------:|--------|-------:|------:|-----:|---------:|
| 10 | COMPLETED | 10 | 10 | 9056,9 | 1,05 |
| 25 | COMPLETED | 11 | 11 | 8845,0 | 1,10 |
| 50 | COMPLETED | 12 | 12 | 8902,1 | 1,80 |
| 75 | COMPLETED | 12 | 12 | 8924,3 | 2,47 |

Artefato: `PeerLab_AlLibrary/cap6_churn_pct.json`.

### 7.3 C1 Join dinâmico (Historico)

| Modo | status | kbps | retries | wall (s) |
|------|--------|-----:|--------:|---------:|
| Só 2 seeders | COMPLETED | 6882,0 | 0 | 1,36 |
| Join mid-flight (+6) | COMPLETED | 9772,9 | 196 | 2,57 |

Artefato: `PeerLab_AlLibrary/cap6_join_midway.json`.

### 7.4 C3 Escada de tamanho (N=4 e N=10)

| Seeds | Fahrenheit | Quixote | Historico | Média |
|------:|-----------:|--------:|----------:|------:|
| 4 | 7843,7 | 10081,5 | 10037,9 | 9321,0 |
| 10 | 7331,8 | 8754,0 | 9224,8 | 8436,9 |

### 7.5 C2 Drop aleatório de chunks (`CHAOS_DROP_PCT=0.15` em RJ/CWB/POA)

| Doc | Seeds | status | retries | kbps |
|-----|------:|--------|--------:|-----:|
| Quixote | 4 | COMPLETED | **11** | 9587,9 |

Overlay: `docker-compose.chaos-drop.yml` · artefato: `cap6_chaos_drop.json`.

### 7.6 C4 Seed-under-load (leecher = seeder)

| Peer | Doc | status | kbps | retries |
|------|-----|--------|-----:|--------:|
| sp | Historico (baixa) | COMPLETED | 9297,0 | 0 |
| man | Fahrenheit (via sp+) | COMPLETED | 4339,1 | 0 |
| nat | Fahrenheit (via sp+) | COMPLETED | 4861,6 | 0 |

Artefato: `cap6_seed_under_load.json`.

### 7.7 C5 Cold start (`peer-rae`)

| Etapa | s |
|-------|--:|
| restart | 0,82 |
| announce ready (files≥1) | **2,11** |
| lobby visible (Fahrenheit) | **2,13** |

Artefato: `cap6_cold_start.json`.

### 7.8 Tor vs Lab (mesmo título) — tabela única

| Doc | Regime | Seeds | kbps | MB/s | Nota |
|------|--------|------:|-----:|-----:|------|
| Fahrenheit | Tor | 1 | 33–65 | ~0,03–0,06 | §2 |
| Fahrenheit | Lab | 4 | ~7844 | ~7,7 | LAN |
| Quixote | Tor | 1 | 91–102 | ~0,09–0,10 | §2 |
| Quixote | Lab | 4 | ~10082 | ~9,8 | LAN |
| Historico | Tor | 1 | 125–154 | ~0,12–0,15 | 28,7 MB |
| Historico | Lab | 4 | ~10038 | ~9,8 | 8 MB lab |

---

## 8. Bloco D (opcionais) — 2026-10-12

### 8.1 D1 Tor / first-byte latency instrumentation

| Campo | Status |
|-------|--------|
| DesktopApp `fetch.rs` | mede tempo até **1º chunk** → `tor_circuit_latency_ms` no ingest |
| PeerLab | envia `tor_circuit_latency_ms` (first-byte lab) no transfer |
| Verificação lab | nonzero no hub (ex.: **40,3 ms** no download Fahrenheit @4 seeds) |
| Tor doméstico | requer rebuild/reinstal do MSI para sessões novas |

### 8.2 D2 ChunkPerformanceLog

| Métrica | Valor |
|---------|------:|
| Após fix PeerLab | **21+** logs (amostra até `CHUNK_TELEMETRY_MAX=48`) |
| Lookup events | emitidos no manifesto (D3) |
| Nota | batch ingest liga `chunk` → `transfer_id` do mesmo POST |

### 8.3 D3 Experiment summary / churn tracker

| Indicador | Valor |
|-----------|------:|
| Transfers measured | 396+ (100% COMPLETED no snapshot) |
| speed_kbps p50 / p95 | 7161 / 9990 |
| retries_avg | 1,08 |
| Lookup / gossip events | 0 / 0 |
| Churn events (joins/leaves) | 22 / 10 |

Artefato: `cap6_experiment_summary.json`.

### 8.4 D4 Partição de rede (disconnect POA+CWB)

| Modo | status | kbps | retries | wall (s) |
|------|--------|-----:|--------:|---------:|
| Baseline 8 seeds | COMPLETED | 9382 | 0 | 0,67 |
| Particionado | COMPLETED | **90** | **20** | **55** |

Artefato: `cap6_network_partition.json`.

### 8.5 D5 CHUNK_SIZE (Quixote, 4 seeders)

| Chunk | chunks | kbps | wall (s) |
|------:|-------:|-----:|---------:|
| 32 KiB | 155 | 5181 | 1,11 |
| 64 KiB | 78 | 10020 | 0,62 |
| 256 KiB | 20 | **27697** | 0,33 |

Artefato: `cap6_chunk_size_sweep.json`. Na LAN, chunks maiores → menos round-trips → maior kbps.
