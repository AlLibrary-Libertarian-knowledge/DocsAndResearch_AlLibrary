# Share Mode Specification

## OnionShare Behavior (Reference)

Source: `onionshare/cli/onionshare_cli/web/share_mode.py`

### Core Functions

| Function | Purpose |
|----------|---------|
| `set_file_info(filenames)` | Build file list; optionally zip or gzip |
| `build_zipfile_list(filenames)` | Create zip for multiple files/dirs |
| `ZipWriter` | Add files and directories to zip |
| `make_etag(data)` | SHA-256 hash as `"sha256:{hex}"` |
| `parse_range_header(range_header, target_size)` | Parse `Range` header; return `[(start, end)]` |

### Single File

- If one file and no directories: serve as-is or gzip on-demand
- Gzip: `Accept-Encoding: gzip` → compress with level 6, cache in temp dir
- ETag: `sha256:...` of file content

### Multiple Files / Directories

- Zip archive via `ZipWriter`
- Filename: `onionshare_{random_string}.zip`
- Add files with `ZIP_DEFLATED`

### Routes

| Route | Method | Purpose |
|-------|--------|---------|
| `/` | GET | Root directory listing or download page |
| `/<path>` | GET | Directory listing or individual file (if `download_individual_files`) |
| `/download` | GET | Full zip or single file download |

### HTTP Features

- **Range requests**: `Range: bytes=0-1023` → 206 Partial Content
- **ETag**: `"sha256:{hex}"`
- **Last-Modified**: UTC datetime
- **304 Not Modified**: If `If-None-Match` or `If-Modified-Since` match
- **Chunked streaming**: 100KB chunks
- **Content-Disposition**: `attachment; filename="..."` or `inline`
- **Content-Type**: From `mime_guess` or `application/octet-stream`

### Autostop

- If `autostop_sharing`: deny new downloads while one is in progress; stop server after first complete download
- If not: allow multiple downloads; allow individual file downloads

---

## Rust Implementation

### Route Structure

```rust
fn share_routes(state: AppState) -> Router {
    Router::new()
        .route("/", get(index_or_directory_listing))
        .route("/download", get(download))
        .route("/*path", get(serve_path))
        .with_state(state)
}
```

### Index / Directory Listing

```rust
async fn index_or_directory_listing(
    State(state): State<AppState>,
    Path(path): Path<String>,
) -> Result<impl IntoResponse, AppError> {
    if path.is_empty() {
        return directory_listing(&state, "").await;
    }
    if let Some(fs_path) = state.files.get(&path) {
        if fs_path.is_dir() {
            return directory_listing(&state, &path).await;
        }
        if state.download_individual_files {
            return stream_individual_file(fs_path).await;
        }
    }
    Err(AppError::NotFound)
}
```

### Download Handler

```rust
async fn download(State(state): State<AppState>) -> Result<impl IntoResponse, AppError> {
    if state.autostop_sharing && state.download_in_progress {
        return Ok(denied_html());
    }
    let (range, status_code) = get_range_and_status_code(&state, &request_headers).await?;
    let body = stream_file_chunks(state.download_path, range, state.clone()).await;
    Ok(Response::builder()
        .status(status_code)
        .header("Content-Length", ...)
        .header("Content-Disposition", attachment_header(...))
        .header("ETag", state.etag)
        .header("Last-Modified", state.last_modified)
        .header("Accept-Ranges", "bytes")
        .body(body)?)
}
```

### Range Request Parsing

```rust
fn parse_range_header(range_header: Option<&str>, target_size: u64) -> Result<Vec<(u64, u64)>, AppError> {
    let end_index = target_size.saturating_sub(1);
    let range_header = match range_header {
        Some(s) if s.starts_with("bytes=") => s,
        _ => return Ok(vec![(0, end_index)]),
    };
    let range_str = &range_header[6..];
    let mut ranges = Vec::new();
    for part in range_str.split(',') {
        let (start, end) = parse_single_range(part, end_index)?;
        ranges.push((start, end));
    }
    // Merge overlapping ranges
    merge_ranges(ranges)
}
```

### Zip Creation

```rust
fn build_zip(filenames: &[PathBuf], output_path: &Path) -> Result<(), AppError> {
    let file = File::create(output_path)?;
    let mut zip = ZipWriter::new(file);
    let options = FileOptions::default().compression_method(zip::CompressionMethod::Deflated);
    for path in filenames {
        if path.is_file() {
            zip.start_file(path.file_name().unwrap().to_string_lossy().as_ref(), options)?;
            zip.write_all(&tokio::fs::read(path).await?)?;
        } else if path.is_dir() {
            add_dir_to_zip(&mut zip, path, path.parent().unwrap(), options).await?;
        }
    }
    zip.finish()?;
    Ok(())
}
```

### Gzip for Single File

```rust
fn gzip_file(input_path: &Path, output_path: &Path) -> Result<u64, AppError> {
    let input = File::open(input_path)?;
    let mut reader = BufReader::new(input);
    let output = File::create(output_path)?;
    let mut encoder = GzEncoder::new(output, Compression::new(6));
    let written = std::io::copy(&mut reader, &mut encoder)?;
    encoder.finish()?;
    Ok(written)
}
```

### Chunked Streaming

```rust
async fn stream_file_chunks(
    path: PathBuf,
    range: (u64, u64),
    state: AppState,
) -> impl Stream<Item = Result<Bytes, _>> {
    let (start, end) = range;
    let chunk_size = 102_400; // 100KB
    let mut buf = vec![0u8; chunk_size];
    let mut file = File::open(path).await?;
    file.seek(SeekFrom::Start(start)).await?;
    let mut pos = start;
    stream! {
        while pos <= end {
            let to_read = std::cmp::min(chunk_size, (end - pos + 1) as usize);
            let n = file.read(&mut buf[..to_read]).await?;
            if n == 0 { break; }
            pos += n as u64;
            state.emit_progress(pos - start, end - start + 1);
            yield Ok(Bytes::from(buf[..n].to_vec()));
        }
    }
}
```

### Security Headers

Apply to all share responses:

- `X-Frame-Options: DENY`
- `X-Content-Type-Options: nosniff`
- `Referrer-Policy: no-referrer`
- `Content-Security-Policy: default-src 'self'; frame-ancestors 'none'; ...`

---

## Settings (ModeSettings)

| Key | Type | Default |
|-----|------|---------|
| `autostop_sharing` | bool | true |
| `download_individual_files` | bool | !autostop_sharing |
| `log_filenames` | bool | false |
