# AlLibrary – GitHub Project Gantt Setup

Populates the **AlLibrary Desktop App** GitHub Project (Projects V2) with repo milestones, issues, and Roadmap date fields so the **Gantt / Roadmap view** shows all 10 phases (0–9).

---

## What it does

1. Creates labels in the repo (phase-0 … phase-9, research, security, onionshare, …).
2. Creates **repo milestones** (one per phase, with due date = phase end date).
3. Creates **issues** (one per sub-milestone) and assigns them to their phase milestone.
4. Adds every issue to the **Projects V2** project as a project item.
5. Sets **"Start date"** and **"End date"** custom date fields on each item → bars appear in the Roadmap/Gantt view.

It is **idempotent**: re-running it skips milestones, labels, and issues that already exist by title.

---

## Requirements

- Python 3.11+
- A GitHub **Personal Access Token (PAT)** with the following scopes:
  - `repo` – create issues, milestones, and labels in the repo
  - `project` (or `read:org` + `write:org` for org-level projects) – read/write Projects V2 via GraphQL

---

## Setup

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Set your PAT
export GITHUB_TOKEN=ghp_your_token_here   # Linux / macOS
$env:GITHUB_TOKEN="ghp_your_token_here"   # PowerShell (Windows)

# 3. (Optional) Edit dates and phase data
#    Open milestones_data.json and adjust start_date / end_date for each phase.
```

---

## Run

```bash
# Full run (all phases, creates everything)
python setup_github_project.py

# Dry run – prints what would happen, makes no API calls
python setup_github_project.py --dry-run

# Only process specific phases (e.g. phase 0 and 2)
python setup_github_project.py --phases 0 2

# Skip label creation (faster if labels already exist)
python setup_github_project.py --skip-labels

# Use a custom data file path
python setup_github_project.py --data /path/to/my_milestones.json
```

---

## After running

1. Open [AlLibrary Desktop App project](https://github.com/orgs/AlLibrary-Libertarian-knowledge/projects/1/views/4).
2. Switch to the **Roadmap** view (or create one if it does not exist yet: + New view → Roadmap).
3. In the Roadmap view settings (⚙), set:
   - **Start date** field → `Start date`
   - **End date** field → `End date`
4. You should see 10 phases as Gantt bars spanning the timeline.

---

## Adjusting dates

All phase dates live in `milestones_data.json` under each phase's `start_date` and `end_date` (ISO 8601, `YYYY-MM-DD`). Edit these before running the script and the Gantt will reflect your actual schedule.

Current schedule (from `DocsAndResearch_AlLibrary/Milestones/detailed_milestones.md`):

| Phase | Title                          | Start      | End        | Status      |
|-------|--------------------------------|------------|------------|-------------|
| 0     | Research and Methodology       | 2026-01-06 | 2026-02-17 | Planned     |
| 1     | Project Foundation             | 2026-01-06 | 2026-02-17 | Completed   |
| 2     | Architectural Restructuring    | 2026-02-17 | 2026-03-10 | In Progress |
| 3     | Foundation Components          | 2026-03-10 | 2026-04-07 | Planned     |
| 4     | P2P Network & Cultural Protocols | 2026-04-07 | 2026-04-28 | Planned   |
| 5     | Advanced Features              | 2026-04-28 | 2026-05-19 | Planned     |
| 6     | Security & Anti-Censorship     | 2026-05-19 | 2026-06-16 | Planned     |
| 7     | Polish & Accessibility         | 2026-06-16 | 2026-07-07 | Planned     |
| 8     | Testing & Documentation        | 2026-07-07 | 2026-07-28 | Planned     |
| 9     | Release & Community Launch     | 2026-07-28 | 2026-08-18 | Planned     |

---

## Troubleshooting

| Error | Fix |
|-------|-----|
| `GITHUB_TOKEN not set` | Export the env var (see Setup). |
| `HTTP 401` | Token is invalid or expired. Re-create the PAT. |
| `HTTP 403 on GraphQL` | Add the `project` scope to your PAT (Settings → Developer settings → Personal access tokens). For org projects you may also need `read:org`. |
| `GraphQL error: Could not resolve to a ProjectV2` | Confirm `project_number` in `milestones_data.json` matches the number in the GitHub URL (`/projects/1`). |
| `HTTP 422 on issue creation` | Label does not exist yet; run without `--skip-labels`. |
| Rate limit sleep messages | Normal for large runs; the script backs off automatically. |

---

## File reference

| File | Purpose |
|------|---------|
| `milestones_data.json` | All phase data: titles, dates, labels, sub-milestones, descriptions |
| `setup_github_project.py` | Main script |
| `requirements.txt` | Python dependency (`requests`) |
| `README.md` | This file |
