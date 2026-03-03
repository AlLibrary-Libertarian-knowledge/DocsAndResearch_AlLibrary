# Security Parity Checklist

## OnionShare Security Features to Replicate

### HTTP Headers

| Header | Value |
|--------|-------|
| `X-Frame-Options` | `DENY` |
| `X-Content-Type-Options` | `nosniff` |
| `Referrer-Policy` | `no-referrer` |
| `Content-Security-Policy` | `default-src 'self'; frame-ancestors 'none'; ...` (configurable) |
| `Permissions-Policy` | Restrict features as needed |

### URL Path

- Use random static URL path to avoid collisions and enumeration
- Example: `/abc123xyz` instead of `/` for share/receive
- Document how to generate and validate

### Filename Handling

- **Share**: Sanitize filenames in zip; no path traversal
- **Receive**: `sanitize_filename()` – allow alphanumeric, `.`, `-`, `_`; reject `..`, `/`, `\`
- Reject empty filenames; use `unnamed` or similar fallback

### Path Traversal

- **Share**: Resolve paths within allowed share root; reject `..` escapes
- **Receive**: Write only under `receive_dir`; reject `..` in filenames

### Rate Limiting

- Consider per-IP or per-session limits for uploads/downloads
- Document as future enhancement; not critical for Phase 1

### Graceful Shutdown

- Wait for in-flight rendezvous circuits before stopping
- Tor control: `DEL_ONION` after circuits drained
- Axum: `axum::serve` with `hyper::server::Server::with_graceful_shutdown`

### Stealth / Client Auth

- OnionShare supports `client_auth_v3` for stealth URLs
- Tor control protocol: `ADD_ONION` with `ClientAuth` parameter
- Document how to add if needed; optional for Phase 1

### Threat Model Notes (from OnionShare)

- Assumes Tor provides anonymity
- Assumes no malicious client code in browser
- Assumes HTTPS not needed (onion addresses are already authenticated)
- DoS: OnionShare has limited mitigations; document Arti limitations

---

## Checklist for Phase 1

- [ ] Security headers on all share responses
- [ ] Secure filename handling in zip
- [ ] No path traversal in share paths
- [ ] Random URL path (optional; document)
- [ ] Graceful shutdown

## Checklist for Phase 2

- [ ] Security headers on receive responses
- [ ] `sanitize_filename()` for uploads
- [ ] No path traversal in receive paths
- [ ] Text message length limit (524288)
