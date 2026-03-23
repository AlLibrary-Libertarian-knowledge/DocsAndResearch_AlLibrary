#!/usr/bin/env python3
"""
AlLibrary – GitHub Project Gantt Setup
Reads milestones_data.json and populates:
  - GitHub repo milestones   (REST API, one per phase)
  - GitHub issues            (REST API, one per sub-milestone)
  - Projects V2 items        (GraphQL, adds issues to the project)
  - Start/End date fields    (GraphQL, enables Roadmap/Gantt view)
  - Priority, Size fields    (GraphQL, single-select)
  - Estimate field           (GraphQL, number)
  - Iteration field          (GraphQL, iteration)

Requirements:
  pip install -r requirements.txt
  export GITHUB_TOKEN=<PAT with scopes: repo, project>
  python setup_github_project.py [--dry-run] [--data milestones_data.json]
"""

import argparse
import json
import os
import sys
import time
from pathlib import Path

import requests

# ──────────────────────────────────────────────────────────────────────────────
# Constants
# ──────────────────────────────────────────────────────────────────────────────

REST_BASE = "https://api.github.com"
GRAPHQL_URL = "https://api.github.com/graphql"
API_VERSION = "2022-11-28"

DATE_FIELD_START = "Start date"
DATE_FIELD_END = "End date"

# ──────────────────────────────────────────────────────────────────────────────
# HTTP helpers
# ──────────────────────────────────────────────────────────────────────────────


def _get_token() -> str:
    token = os.environ.get("GITHUB_TOKEN", "")
    if not token:
        sys.exit(
            "ERROR: GITHUB_TOKEN environment variable is not set.\n"
            "Create a PAT with scopes 'repo' and 'project' and export it:\n"
            "  export GITHUB_TOKEN=ghp_..."
        )
    return token


def _rest_headers() -> dict:
    return {
        "Authorization": f"Bearer {_get_token()}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": API_VERSION,
    }


def _graphql_headers() -> dict:
    return {
        "Authorization": f"Bearer {_get_token()}",
        "Content-Type": "application/json",
    }


def _with_retry(fn, label: str, max_retries: int = 5):
    """Call fn() with exponential backoff on connection errors."""
    delay = 2.0
    for attempt in range(max_retries):
        try:
            return fn()
        except (requests.exceptions.ConnectionError,
                requests.exceptions.Timeout) as exc:
            if attempt == max_retries - 1:
                raise
            print(
                f"  [retry {attempt + 1}/{max_retries}] {label} – "
                f"connection error: {exc}. Retrying in {delay:.0f}s …",
                file=sys.stderr,
            )
            time.sleep(delay)
            delay = min(delay * 2, 60)


def rest_get(path: str) -> dict:
    url = f"{REST_BASE}{path}"
    r = _with_retry(
        lambda: requests.get(url, headers=_rest_headers(), timeout=30),
        f"GET {path}",
    )
    _check(r, f"GET {path}")
    return r.json()


def rest_post(path: str, body: dict, *, dry_run: bool = False) -> dict:
    if dry_run:
        print(f"  [dry-run] POST {path} {json.dumps(body, ensure_ascii=False)[:120]}")
        return {"number": 0, "node_id": "DRY_NODE_ID", "id": 0}
    url = f"{REST_BASE}{path}"
    r = _with_retry(
        lambda: requests.post(url, headers=_rest_headers(), json=body, timeout=30),
        f"POST {path}",
    )
    _check(r, f"POST {path}")
    return r.json()


def rest_patch(path: str, body: dict, *, dry_run: bool = False) -> dict:
    if dry_run:
        print(f"  [dry-run] PATCH {path} {json.dumps(body, ensure_ascii=False)[:120]}")
        return {}
    url = f"{REST_BASE}{path}"
    r = _with_retry(
        lambda: requests.patch(url, headers=_rest_headers(), json=body, timeout=30),
        f"PATCH {path}",
    )
    _check(r, f"PATCH {path}")
    return r.json()


def graphql(query: str, variables: dict | None = None, *, dry_run: bool = False) -> dict:
    if dry_run:
        op = (query.strip().splitlines()[0])[:80]
        print(f"  [dry-run] GraphQL: {op}")
        return {"data": {}}
    payload = {"query": query, "variables": variables or {}}
    # Small inter-request pause to avoid secondary rate limits (~5000 points/hour)
    time.sleep(0.25)
    r = _with_retry(
        lambda: requests.post(
            GRAPHQL_URL, headers=_graphql_headers(), json=payload, timeout=30
        ),
        "GraphQL request",
    )
    _check(r, "GraphQL request")
    data = r.json()
    if "errors" in data:
        for e in data["errors"]:
            print(f"  [GraphQL error] {e.get('message', e)}", file=sys.stderr)
        raise RuntimeError("GraphQL returned errors (see above).")
    return data


def _check(response: requests.Response, label: str) -> None:
    if not response.ok:
        print(
            f"ERROR {response.status_code} on {label}:\n{response.text[:400]}",
            file=sys.stderr,
        )
        raise RuntimeError(f"HTTP {response.status_code} on {label}")
    remaining = int(response.headers.get("x-ratelimit-remaining", "999"))
    if remaining < 10:
        reset = int(response.headers.get("x-ratelimit-reset", "0"))
        wait = max(0, reset - int(time.time())) + 2
        print(f"  [rate-limit] Only {remaining} requests left – sleeping {wait}s …")
        time.sleep(wait)


# ──────────────────────────────────────────────────────────────────────────────
# Label helpers
# ──────────────────────────────────────────────────────────────────────────────

LABEL_COLORS = {
    "phase-0": "e4e669",
    "phase-1": "0075ca",
    "phase-2": "d73a4a",
    "phase-3": "a2eeef",
    "phase-4": "0e8a16",
    "phase-5": "6f42c1",
    "phase-6": "e99695",
    "phase-7": "f9d0c4",
    "phase-8": "bfd4f2",
    "phase-9": "d4c5f9",
    "research": "ededed",
    "architecture": "84b6eb",
    "infrastructure": "c2e0c6",
    "backend": "fef2c0",
    "frontend": "c5def5",
    "ui": "bfe5bf",
    "ux": "cfd3d7",
    "security": "ee0701",
    "tor": "333333",
    "onionshare": "5319e7",
    "p2p": "0075ca",
    "networking": "006b75",
    "search": "e4e669",
    "documentation": "0075ca",
    "testing": "e11d48",
    "accessibility": "7057ff",
    "performance": "fbca04",
    "database": "c5def5",
    "refactor": "d4c5f9",
    "cultural-framework": "f9d0c4",
    "release": "0e8a16",
    "devops": "c2e0c6",
    "community": "d73a4a",
    "planning": "a2eeef",
    "critical-path": "ee0701",
    "setup": "fef2c0",
    "task": "ededed",
    "offline": "cfd3d7",
    "replication": "bfd4f2",
    "collections": "bfe5bf",
    "polish": "f9d0c4",
    "advanced-features": "6f42c1",
    "foundation": "0075ca",
    "document-management": "84b6eb",
}


def ensure_labels(owner: str, repo: str, labels: list[str], *, dry_run: bool) -> None:
    existing_raw = rest_get(f"/repos/{owner}/{repo}/labels")
    existing = {lbl["name"] for lbl in existing_raw}
    for name in labels:
        if name not in existing:
            color = LABEL_COLORS.get(name, "ededed")
            rest_post(
                f"/repos/{owner}/{repo}/labels",
                {"name": name, "color": color},
                dry_run=dry_run,
            )
            print(f"  Created label: {name}")


# ──────────────────────────────────────────────────────────────────────────────
# REST – Repo milestones
# ──────────────────────────────────────────────────────────────────────────────


def get_existing_repo_milestones(owner: str, repo: str) -> dict[str, int]:
    """Returns {title: number} for open + closed milestones."""
    result: dict[str, int] = {}
    for state in ("open", "closed"):
        page = 1
        while True:
            items = rest_get(
                f"/repos/{owner}/{repo}/milestones?state={state}&per_page=100&page={page}"
            )
            for m in items:
                result[m["title"]] = m["number"]
            if len(items) < 100:
                break
            page += 1
    return result


def create_repo_milestone(
    owner: str,
    repo: str,
    phase: dict,
    existing: dict[str, int],
    *,
    dry_run: bool,
) -> int:
    """Creates or returns existing repo milestone. Returns milestone number."""
    title = phase["title"]
    if title in existing:
        print(f"  Repo milestone already exists: {title!r} → #{existing[title]}")
        return existing[title]
    body = {
        "title": title,
        "description": phase.get("focus", ""),
        "due_on": f"{phase['end_date']}T23:59:59Z",
        "state": "closed" if phase["status"] == "completed" else "open",
    }
    result = rest_post(f"/repos/{owner}/{repo}/milestones", body, dry_run=dry_run)
    num = result.get("number", 0)
    print(f"  Created repo milestone: {title!r} → #{num}")
    return num


# ──────────────────────────────────────────────────────────────────────────────
# REST – Issues
# ──────────────────────────────────────────────────────────────────────────────


def get_existing_issues(owner: str, repo: str) -> dict[str, dict]:
    """Returns {title: {"node_id": str, "number": int}} for open + closed issues."""
    result: dict[str, dict] = {}
    for state in ("open", "closed"):
        page = 1
        while True:
            items = rest_get(
                f"/repos/{owner}/{repo}/issues?state={state}&per_page=100&page={page}"
            )
            for issue in items:
                if "pull_request" not in issue:
                    result[issue["title"]] = {
                        "node_id": issue["node_id"],
                        "number": issue["number"],
                    }
            if len(items) < 100:
                break
            page += 1
    return result


def set_issue_type(
    owner: str,
    repo: str,
    issue_number: int,
    type_name: str,
    *,
    dry_run: bool,
) -> None:
    """Sets the issue type via PATCH (Bug / Feature / Task)."""
    rest_patch(
        f"/repos/{owner}/{repo}/issues/{issue_number}",
        {"type": type_name},
        dry_run=dry_run,
    )


def create_issue(
    owner: str,
    repo: str,
    sub: dict,
    milestone_number: int,
    existing: dict[str, dict],
    *,
    dry_run: bool,
) -> str:
    """Creates or updates existing issue. Returns node_id."""
    title = sub["title"]
    type_name: str | None = sub.get("type")

    if title in existing:
        info = existing[title]
        print(f"    Issue already exists: {title!r} → #{info['number']}")
        if type_name:
            set_issue_type(owner, repo, info["number"], type_name, dry_run=dry_run)
        return info["node_id"]

    body: dict = {
        "title": title,
        "body": sub.get("description", ""),
        "labels": sub.get("labels", []),
        "milestone": milestone_number if milestone_number else None,
    }
    if body["milestone"] is None:
        body.pop("milestone")
    if type_name:
        body["type"] = type_name
    result = rest_post(f"/repos/{owner}/{repo}/issues", body, dry_run=dry_run)
    node_id: str = result.get("node_id", "DRY_NODE_ID")
    number: int = result.get("number", 0)
    print(f"    Created issue: {title!r} → #{number}")
    existing[title] = {"node_id": node_id, "number": number}
    return node_id


# ──────────────────────────────────────────────────────────────────────────────
# GraphQL – Project V2 helpers
# ──────────────────────────────────────────────────────────────────────────────

GET_PROJECT_INFO_QUERY = """
query($org: String!, $number: Int!) {
  organization(login: $org) {
    projectV2(number: $number) {
      id
      title
      fields(first: 50) {
        nodes {
          ... on ProjectV2Field {
            id
            name
            dataType
          }
          ... on ProjectV2SingleSelectField {
            id
            name
            options {
              id
              name
            }
          }
          ... on ProjectV2IterationField {
            id
            name
            configuration {
              iterations {
                id
                title
                startDate
                duration
              }
            }
          }
        }
      }
    }
  }
}
"""

CREATE_FIELD_MUTATION = """
mutation($projectId: ID!, $name: String!, $dataType: ProjectV2CustomFieldType!) {
  createProjectV2Field(input: {projectId: $projectId, name: $name, dataType: $dataType}) {
    projectV2Field {
      ... on ProjectV2Field {
        id
        name
      }
    }
  }
}
"""

ADD_ITEM_MUTATION = """
mutation($projectId: ID!, $contentId: ID!) {
  addProjectV2ItemById(input: {projectId: $projectId, contentId: $contentId}) {
    item {
      id
    }
  }
}
"""

SET_DATE_MUTATION = """
mutation($projectId: ID!, $itemId: ID!, $fieldId: ID!, $value: Date!) {
  updateProjectV2ItemFieldValue(input: {
    projectId: $projectId,
    itemId: $itemId,
    fieldId: $fieldId,
    value: { date: $value }
  }) {
    projectV2Item { id }
  }
}
"""

SET_SINGLE_SELECT_MUTATION = """
mutation($projectId: ID!, $itemId: ID!, $fieldId: ID!, $optionId: String!) {
  updateProjectV2ItemFieldValue(input: {
    projectId: $projectId,
    itemId: $itemId,
    fieldId: $fieldId,
    value: { singleSelectOptionId: $optionId }
  }) {
    projectV2Item { id }
  }
}
"""

SET_NUMBER_MUTATION = """
mutation($projectId: ID!, $itemId: ID!, $fieldId: ID!, $value: Float!) {
  updateProjectV2ItemFieldValue(input: {
    projectId: $projectId,
    itemId: $itemId,
    fieldId: $fieldId,
    value: { number: $value }
  }) {
    projectV2Item { id }
  }
}
"""

SET_ITERATION_MUTATION = """
mutation($projectId: ID!, $itemId: ID!, $fieldId: ID!, $iterationId: String!) {
  updateProjectV2ItemFieldValue(input: {
    projectId: $projectId,
    itemId: $itemId,
    fieldId: $fieldId,
    value: { iterationId: $iterationId }
  }) {
    projectV2Item { id }
  }
}
"""


# ─── Field metadata dataclass-lite ───────────────────────────────────────────

class FieldMeta:
    """Holds id, dataType, options (single-select) and iterations."""

    def __init__(self, field_id: str, name: str, data_type: str):
        self.id = field_id
        self.name = name
        self.data_type = data_type          # DATE, NUMBER, SINGLE_SELECT, ITERATION, TEXT
        self.options: dict[str, str] = {}   # {option_name_lower: option_id}
        self.iterations: dict[str, str] = {}  # {iteration_title_lower: iteration_id}

    def option_id(self, name: str) -> str | None:
        return self.options.get(name.lower())

    def iteration_id(self, title: str) -> str | None:
        return self.iterations.get(title.lower())


def get_project_info(
    org: str, project_number: int, *, dry_run: bool
) -> tuple[str, dict[str, FieldMeta]]:
    """Returns (project_id, {field_name: FieldMeta})."""
    if dry_run:
        print(f"  [dry-run] get_project_info(org={org!r}, number={project_number})")
        return "DRY_PROJECT_ID", {}

    data = graphql(GET_PROJECT_INFO_QUERY, {"org": org, "number": project_number})
    project = data["data"]["organization"]["projectV2"]
    project_id: str = project["id"]
    fields: dict[str, FieldMeta] = {}

    for node in project["fields"]["nodes"]:
        if not node or "id" not in node or "name" not in node:
            continue
        name: str = node["name"]
        data_type: str = node.get("dataType", "")

        # Single-select fields don't carry dataType in the inline fragment;
        # detect by presence of "options"
        if "options" in node:
            data_type = "SINGLE_SELECT"
        elif "configuration" in node:
            data_type = "ITERATION"

        fm = FieldMeta(node["id"], name, data_type)

        if "options" in node:
            for opt in node["options"]:
                fm.options[opt["name"].lower()] = opt["id"]

        if "configuration" in node:
            for itr in node["configuration"].get("iterations", []):
                fm.iterations[itr["title"].lower()] = itr["id"]

        fields[name] = fm

    print(f"  Project: {project['title']!r}  (id={project_id})")
    for fname, fm in fields.items():
        extra = ""
        if fm.options:
            extra = f"  options={list(fm.options.keys())}"
        elif fm.iterations:
            extra = f"  iterations={list(fm.iterations.keys())}"
        print(f"    Field {fname!r}: type={fm.data_type}{extra}")

    return project_id, fields


def ensure_date_fields(
    project_id: str,
    fields: dict[str, FieldMeta],
    *,
    dry_run: bool,
) -> tuple[str, str]:
    """Ensures Start date and End date fields exist. Returns (start_id, end_id)."""

    def _ensure(field_name: str) -> str:
        if field_name in fields:
            fid = fields[field_name].id
            print(f"  Field {field_name!r} already exists (id={fid})")
            return fid
        print(f"  Creating field: {field_name!r} …")
        result = graphql(
            CREATE_FIELD_MUTATION,
            {"projectId": project_id, "name": field_name, "dataType": "DATE"},
            dry_run=dry_run,
        )
        if dry_run:
            return f"DRY_{field_name.upper().replace(' ', '_')}_ID"
        new_id: str = result["data"]["createProjectV2Field"]["projectV2Field"]["id"]
        fields[field_name] = FieldMeta(new_id, field_name, "DATE")
        return new_id

    return _ensure(DATE_FIELD_START), _ensure(DATE_FIELD_END)


def add_item_to_project(
    project_id: str,
    issue_node_id: str,
    *,
    dry_run: bool,
) -> str:
    """Adds an issue to the project. Returns the project item id."""
    result = graphql(
        ADD_ITEM_MUTATION,
        {"projectId": project_id, "contentId": issue_node_id},
        dry_run=dry_run,
    )
    if dry_run:
        return "DRY_ITEM_ID"
    return result["data"]["addProjectV2ItemById"]["item"]["id"]


def set_item_dates(
    project_id: str,
    item_id: str,
    start_field_id: str,
    end_field_id: str,
    start_date: str,
    end_date: str,
    *,
    dry_run: bool,
) -> None:
    """Sets start and end date on a project item."""
    for fid, val in ((start_field_id, start_date), (end_field_id, end_date)):
        graphql(
            SET_DATE_MUTATION,
            {"projectId": project_id, "itemId": item_id, "fieldId": fid, "value": val},
            dry_run=dry_run,
        )


def set_item_metadata(
    project_id: str,
    item_id: str,
    sub: dict,
    fields: dict[str, FieldMeta],
    *,
    dry_run: bool,
) -> None:
    """Sets Priority, Size (single-select), Estimate (number), Iteration on a project item."""

    # ── Priority (single-select) ──────────────────────────────────────────────
    priority_val: str | None = sub.get("priority")
    if priority_val and "Priority" in fields:
        fm = fields["Priority"]
        opt_id = fm.option_id(priority_val)
        if opt_id:
            graphql(
                SET_SINGLE_SELECT_MUTATION,
                {
                    "projectId": project_id,
                    "itemId": item_id,
                    "fieldId": fm.id,
                    "optionId": opt_id,
                },
                dry_run=dry_run,
            )
        else:
            avail = list(fm.options.keys())
            print(
                f"    [warn] Priority option {priority_val!r} not found in project. "
                f"Available: {avail}"
            )

    # ── Size (single-select) ──────────────────────────────────────────────────
    size_val: str | None = sub.get("size")
    if size_val and "Size" in fields:
        fm = fields["Size"]
        opt_id = fm.option_id(size_val)
        if opt_id:
            graphql(
                SET_SINGLE_SELECT_MUTATION,
                {
                    "projectId": project_id,
                    "itemId": item_id,
                    "fieldId": fm.id,
                    "optionId": opt_id,
                },
                dry_run=dry_run,
            )
        else:
            avail = list(fm.options.keys())
            print(
                f"    [warn] Size option {size_val!r} not found in project. "
                f"Available: {avail}"
            )

    # ── Estimate (number) ─────────────────────────────────────────────────────
    estimate_val = sub.get("estimate")
    if estimate_val is not None and "Estimate" in fields:
        graphql(
            SET_NUMBER_MUTATION,
            {
                "projectId": project_id,
                "itemId": item_id,
                "fieldId": fields["Estimate"].id,
                "value": float(estimate_val),
            },
            dry_run=dry_run,
        )

    # ── Iteration ─────────────────────────────────────────────────────────────
    iter_val: str | None = sub.get("iteration")
    if iter_val and "Iteration" in fields:
        fm = fields["Iteration"]
        itr_id = fm.iteration_id(iter_val)
        if itr_id:
            graphql(
                SET_ITERATION_MUTATION,
                {
                    "projectId": project_id,
                    "itemId": item_id,
                    "fieldId": fm.id,
                    "iterationId": itr_id,
                },
                dry_run=dry_run,
            )
        else:
            avail = list(fm.iterations.keys())
            print(
                f"    [warn] Iteration {iter_val!r} not found in project. "
                f"Available: {avail}. "
                "Create the iteration in the project settings first."
            )


# ──────────────────────────────────────────────────────────────────────────────
# Main orchestration
# ──────────────────────────────────────────────────────────────────────────────


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Populate GitHub Project Gantt (Roadmap) from milestones JSON."
    )
    parser.add_argument(
        "--data",
        default=str(Path(__file__).parent / "milestones_data.json"),
        help="Path to milestones_data.json (default: same directory as this script)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print what would be done without making any API calls.",
    )
    parser.add_argument(
        "--skip-labels",
        action="store_true",
        help="Skip creating missing labels (faster if labels are already set up).",
    )
    parser.add_argument(
        "--phases",
        nargs="*",
        type=int,
        metavar="N",
        help="Only process these phase numbers (e.g. --phases 0 1 2). Default: all.",
    )
    args = parser.parse_args()

    data_path = Path(args.data)
    if not data_path.exists():
        sys.exit(f"ERROR: Data file not found: {data_path}")

    with open(data_path, encoding="utf-8") as f:
        data = json.load(f)

    gh = data["github"]
    owner = gh["org"]
    repo = gh["repo"]
    project_number = int(gh["project_number"])
    dry = args.dry_run

    if dry:
        print("=== DRY RUN – no changes will be made ===\n")

    # ── 1. Collect all labels across phases ──────────────────────────────────
    if not args.skip_labels:
        all_labels: set[str] = set()
        for phase in data["phases"]:
            all_labels.update(phase.get("labels", []))
            for sm in phase.get("sub_milestones", []):
                all_labels.update(sm.get("labels", []))
        print("── Ensuring labels exist ──")
        ensure_labels(owner, repo, sorted(all_labels), dry_run=dry)

    # ── 2. Get project fields (including option/iteration metadata) ───────────
    print("\n── Connecting to Projects V2 ──")
    project_id, fields = get_project_info(owner, project_number, dry_run=dry)
    start_field_id, end_field_id = ensure_date_fields(project_id, fields, dry_run=dry)

    # Warn about missing optional fields so the user knows upfront
    for optional in ("Priority", "Size", "Estimate", "Iteration"):
        if optional not in fields:
            print(
                f"  [info] Field {optional!r} not found in project – "
                f"will skip {optional} updates. Add it in project settings if needed."
            )

    # ── 3. Pre-load existing repo milestones and issues ───────────────────────
    print("\n── Loading existing repo milestones and issues ──")
    existing_milestones = get_existing_repo_milestones(owner, repo)
    existing_issues = get_existing_issues(owner, repo)
    print(
        f"  Found {len(existing_milestones)} existing milestones, "
        f"{len(existing_issues)} existing issues."
    )

    # ── 4. Process each phase ─────────────────────────────────────────────────
    phases = data["phases"]
    if args.phases is not None:
        phases = [p for p in phases if p["number"] in args.phases]

    for phase in phases:
        num = phase["number"]
        print(f"\n── Phase {num}: {phase['title']} ──")

        milestone_num = create_repo_milestone(
            owner, repo, phase, existing_milestones, dry_run=dry
        )
        existing_milestones[phase["title"]] = milestone_num

        for sm in phase.get("sub_milestones", []):
            print(f"  Sub-milestone {sm['id']}: {sm['title']}")
            node_id = create_issue(
                owner, repo, sm, milestone_num, existing_issues, dry_run=dry
            )

            item_id = add_item_to_project(project_id, node_id, dry_run=dry)

            item_start = sm.get("start_date", phase["start_date"])
            item_end = sm.get("end_date", phase["end_date"])
            set_item_dates(
                project_id,
                item_id,
                start_field_id,
                end_field_id,
                item_start,
                item_end,
                dry_run=dry,
            )

            set_item_metadata(project_id, item_id, sm, fields, dry_run=dry)

            priority = sm.get("priority", "–")
            size = sm.get("size", "–")
            estimate = sm.get("estimate", "–")
            iteration = sm.get("iteration", "–")
            issue_type = sm.get("type", "–")
            print(
                f"    → dates: {item_start} → {item_end} | "
                f"type={issue_type} | priority={priority} | size={size} | "
                f"estimate={estimate}h | iteration={iteration}"
            )

    print("\n✓ Done. Open your project Roadmap view to see the Gantt chart.")
    print(
        f"  https://github.com/orgs/{owner}/projects/{project_number}/views/4\n"
        "  Tip: click 'Date fields' in the Roadmap view and set\n"
        f"  Start = {DATE_FIELD_START!r}  /  End = {DATE_FIELD_END!r}\n"
        "  to make the Gantt bars appear.\n"
        "\n"
        "  If Priority/Size/Iteration warnings appeared above, the option names\n"
        "  in milestones_data.json don't match your project's field options.\n"
        "  Run --dry-run first to see available option names, then update the JSON."
    )


if __name__ == "__main__":
    main()
