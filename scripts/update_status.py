"""Refresh PR statuses from GitHub and rewrite the tables in README.md.

Usage:  python scripts/update_status.py            (needs internet; a GITHUB_TOKEN env var raises the rate limit)
        python scripts/update_status.py --offline  (rebuild the tables from data/contributions.json only)
"""
from __future__ import annotations

import json
import os
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "contributions.json"
README = ROOT / "README.md"
START, END = "<!-- CONTRIBUTIONS:START -->", "<!-- CONTRIBUTIONS:END -->"
STATS_START, STATS_END = "<!-- STATS:START -->", "<!-- STATS:END -->"
LABEL = {"merged": "Merged", "open": "Open", "closed": "Closed"}


def fetch_status(repo: str, number: int) -> tuple[str, str] | None:
    url = f"https://api.github.com/repos/{repo}/pulls/{number}"
    headers = {"User-Agent": "open-source-contributions", "Accept": "application/vnd.github+json"}
    if os.environ.get("GITHUB_TOKEN"):
        headers["Authorization"] = f"Bearer {os.environ['GITHUB_TOKEN']}"
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers=headers), timeout=20) as r:
            data = json.load(r)
    except Exception as exc:  # network, rate limit, deleted repo
        print(f"  could not fetch {repo}#{number}: {exc}")
        return None
    if data.get("merged_at"):
        return "merged", data["merged_at"][:10]
    return ("open" if data["state"] == "open" else "closed"), ""


def refresh(items: list[dict]) -> None:
    for item in items:
        result = fetch_status(item["repo"], item["number"])
        if result:
            item["status"], merged = result
            if merged:
                item["merged"] = merged


def table(items: list[dict]) -> str:
    rows = ["| Project | PR | What | Closes | Tests | Status |", "|---|---|---|---|---|---|"]
    for i in items:
        link = f"[#{i['number']}](https://github.com/{i['repo']}/pull/{i['number']})"
        status = LABEL[i["status"]] + (f" ({i['merged']})" if i["merged"] else "")
        rows.append(
            f"| {i['project']} | {link} | {i['title']} | {', '.join(i['closes'])} | {i['tests'] or '-'} | {status} |"
        )
    return "\n".join(rows)


def stats(items: list[dict]) -> str:
    merged = [i for i in items if i["status"] == "merged"]
    projects = {i["project"] for i in merged}
    tests = sum(i["tests"] for i in merged)
    opened = sum(1 for i in items if i["status"] == "open")
    return (
        "| Merged PRs | Projects | Tests added (merged) | Open PRs |\n|---|---|---|---|\n"
        f"| **{len(merged)}** | **{len(projects)}** | **{tests}** | **{opened}** |"
    )


def replace(text: str, start: str, end: str, body: str) -> str:
    a, b = text.index(start) + len(start), text.index(end)
    return text[:a] + "\n" + body + "\n" + text[b:]


def main() -> None:
    items = json.loads(DATA.read_text())
    if "--offline" not in sys.argv:
        refresh(items)
        DATA.write_text(json.dumps(items, indent=2) + "\n")
    text = README.read_text()
    text = replace(text, START, END, table(items))
    text = replace(text, STATS_START, STATS_END, stats(items))
    README.write_text(text)
    print("README updated")


if __name__ == "__main__":
    main()
