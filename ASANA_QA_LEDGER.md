# ASANA QA LEDGER — Amara Care Center

| | |
|---|---|
| Created | 2026-08-05 |
| Purpose | Master backlog of all Asana DEV and QA items, reconciled against the implementation |
| Status | **BLOCKED — zero items collected.** The attached project is not reachable from the connected Asana account |
| Companion ledgers | `MASTER_IMPLEMENTATION_LEDGER.md` (design/implementation audit) · `ASSET_MAP.md` (asset registry) |

---

## 0 · COLLECTION STATUS — BLOCKED

**No Asana task, subtask, comment, attachment, section or custom field has been read.** This file exists to record the blocker with evidence, not to stand in for the backlog. Every count below is zero because the collection could not start, not because the project is empty.

| Metric | Value |
|---|---|
| Tasks inspected | **0** |
| Subtasks inspected | **0** |
| Comments inspected | **0** |
| Attachments inspected | **0** |
| Sections enumerated | **0** |

### 0.1 · The target

| | |
|---|---|
| Supplied URL | `https://app.asana.com/1/1210357482925157/project/1217105105055924/list/1217105274249185` |
| Workspace / org GID (URL segment 2) | `1210357482925157` |
| Project GID (URL segment 4) | `1217105105055924` |
| List-view GID (URL segment 6) | `1217105274249185` |
| Project name | **unknown — could not be read** |

### 0.2 · The connection

The Asana connector **is authenticated.** `get_me` succeeds:

| | |
|---|---|
| User GID | `1216258602373851` |
| Name | Jasur Oybekov |
| Email | `oybekovj97@gmail.com` |
| Workspaces the account belongs to | **exactly one** — `1216258602373863` ("My workspace") |

### 0.3 · The blocker

**The account is not a member of workspace `1210357482925157`.**

The connected account belongs to workspace `1216258602373863`. The supplied URL points into workspace `1210357482925157`. These are different workspaces, and the connected account has no membership or guest access in the second one.

That the URL's second segment is the workspace GID is confirmed by the one project this account *can* see, whose Asana-issued permalink follows the identical pattern:

```
accessible : https://app.asana.com/1/1216258602373863/project/1216258473974357
                                    ^^^^^^^^^^^^^^^^ workspace the account belongs to
requested  : https://app.asana.com/1/1210357482925157/project/1217105105055924/list/1217105274249185
                                    ^^^^^^^^^^^^^^^^ workspace the account does NOT belong to
```

### 0.4 · Exact errors returned

Four independent access paths were attempted against the requested project. All four returned the same error verbatim:

```json
{"error":"unauthorized","message":"Not Authorized","suggestion":"Ask the user to re-authorize the Asana connection."}
```

| # | Call | Result |
|---|---|---|
| 1 | `get_project(project_id: 1217105105055924, include_sections: true)` | `unauthorized` |
| 2 | `get_project(project_id: 1217105105055924)` — minimal fields, to rule out a field-permission error | `unauthorized` |
| 3 | `get_tasks(project: 1217105105055924)` | `unauthorized` |
| 4 | `get_tasks(section: 1217105274249185)` — direct section access, bypassing the project | `unauthorized` |

### 0.5 · Enumeration proving the project is not reachable by any other route

| Call | Result |
|---|---|
| `get_projects(limit: 100)` | **1 project** — `1216258473974357` "Активные клиенты", workspace `1216258602373863`. Not the target |
| `get_projects(archived: true, limit: 100)` | **0 projects** — the target is not archived-but-visible |
| `search_objects(resource_type: "project", query: "", count: 100)` | **1 project** — the same one. The target does not appear in search |
| `search_objects(resource_type: "team", query: "", count: 50)` | **0 teams** — the account belongs to no organisation team |

**Project `1217105105055924` does not appear in any listing available to this account, in any state.**

### 0.6 · Not done, deliberately

Per the standing instruction — *"Do not search for a similarly named project. Do not use another workspace. Do not use an old Amara project."*

- The one accessible project, **"Активные клиенты"** (`1216258473974357`), was **not opened**. Its name does not match, it sits in the wrong workspace, and it is not the attached project.
- No similarly-named project was searched for.
- No Asana object was created, edited, moved, commented on, completed or deleted. Asana remains read-only, as instructed — and in practice nothing was writable either.

### 0.7 · What is required to unblock

Exactly one of the following. Both are actions on the client's side; neither can be performed from here.

**Option A — grant the connected account access (preferred, no reconnection needed)**
An Asana Admin of workspace/org `1210357482925157` invites **`oybekovj97@gmail.com`** to that workspace and adds the account to project `1217105105055924` with at least **Viewer / Comment-only** access.
Viewer access is sufficient for this entire collection phase — it covers tasks, subtasks, descriptions, comments, stories, attachments, custom fields, assignees and sections. Editor access is only needed later, if and when the board is to be updated.

**Option B — re-authorise the connector against an account that already has access**
If the Asana account that owns the agency board is a *different* account from `oybekovj97@gmail.com`, the Asana connector must be re-authorised as that account. In this non-interactive session the OAuth flow cannot be run; the user must reconnect Asana from claude.ai connector settings (or `/mcp` in an interactive session).

**Diagnostic note.** The Asana API returns the identical `Not Authorized` response for "this object does not exist" and "you may not see this object" — it does not distinguish them, by design, so that a non-member cannot probe for the existence of private objects. The distinguishing evidence here is §0.2: authentication itself succeeds and returns a workspace list that does not contain `1210357482925157`. The failure is therefore **membership, not credentials, and not a malformed URL.**

---

## 1 · BACKLOG

*Empty. To be populated once access is granted — every field required by the collection brief (task ID, title, URL, section, page, component, DEV/QA class, status, assignee, priority, description, comments, attachments, screenshot interpretation, requested correction, acceptance criteria, affected routes, affected shared components, dependency, implementation status, confidence, source date, newest instruction date) will be recorded per item.*

## 2 · SHARED-COMPONENT GROUPING

*Empty. Repeated QA items will be collapsed to one shared implementation issue with an explicit affected-routes list, per the deduplication rule.*

## 3 · CONFLICTS REQUIRING A DECISION

*Empty. Conflicts will be recorded with both source references, both dates, and the authority-order resolution — or flagged as unresolvable where the sources genuinely contradict each other.*
