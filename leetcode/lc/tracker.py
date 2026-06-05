"""Regenerate the repo's progress tables from your LIVE LeetCode status.

Repo-scoped: lists every problem present under python3/, with solved status pulled
straight from LeetCode (one authenticated GET to /api/problems/all/). Tool-agnostic and
self-healing -- it reflects your real account no matter how you submitted (leetgo,
the website, anything). Pure standard library: no third-party dependencies.

Writes a full per-problem table to leetcode/README.md and a `solved / tracked` summary
to the repo's root README.md, each between its own HTML comment markers.

Run with: python3 -m lc
Auth: set LEETCODE_SESSION in .env (or the environment) for real solved status;
without it everything shows as not-solved.
"""

from __future__ import annotations

import json
import os
import re
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROBLEMS = ROOT / "python3"  # mirror code.python3.out_dir in leetgo.yaml
README = ROOT / "README.md"
REPO_README = ROOT.parent / "README.md"
ENV = ROOT / ".env"

ALL_URL = "https://leetcode.com/api/problems/all/"
START, END = "<!-- LC-INDEX:START -->", "<!-- LC-INDEX:END -->"
SUMMARY_START, SUMMARY_END = "<!-- LC-SUMMARY:START -->", "<!-- LC-SUMMARY:END -->"
_DIR_RE = re.compile(r"^\d+[.\-_](?P<slug>.+)$")
_DIFF = {1: "Easy", 2: "Medium", 3: "Hard"}


def _session() -> str | None:
    """LEETCODE_SESSION from the environment, else from a .env file next to the project."""
    val = os.environ.get("LEETCODE_SESSION")
    if val:
        return val.strip()
    if ENV.exists():
        for line in ENV.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line.startswith("LEETCODE_SESSION="):
                return line.split("=", 1)[1].strip().strip('"').strip("'")
    return None


def _repo_slugs() -> set[str]:
    """Slugs of problems present under python3/, parsed from `<id><sep><slug>` dir names."""
    slugs: set[str] = set()
    if PROBLEMS.exists():
        for path in sorted(PROBLEMS.iterdir()):
            if path.is_dir():
                m = _DIR_RE.match(path.name)
                if m:
                    slugs.add(m.group("slug"))
    return slugs


def _fetch_pairs(session: str | None) -> list[dict]:
    headers = {"User-Agent": "lc-tracker"}
    if session:
        headers["Cookie"] = f"LEETCODE_SESSION={session}"
    req = urllib.request.Request(ALL_URL, headers=headers)
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.load(resp).get("stat_status_pairs", [])


def _rows(slugs: set[str], pairs: list[dict]) -> list[dict]:
    by_slug = {}
    for pair in pairs:
        stat = pair["stat"]
        by_slug[stat["question__title_slug"]] = {
            "id": stat["frontend_question_id"],
            "title": stat["question__title"],
            "difficulty": _DIFF.get(pair.get("difficulty", {}).get("level"), "?"),
            "ac": pair.get("status") == "ac",
        }
    rows = []
    for slug in slugs:
        info = by_slug.get(
            slug, {"id": 0, "title": slug, "difficulty": "?", "ac": False}
        )
        rows.append({**info, "slug": slug})
    rows.sort(key=lambda r: int(r["id"]) if str(r["id"]).isdigit() else 1 << 30)
    return rows


def _table(rows: list[dict]) -> str:
    out = ["| # | Problem | Difficulty | Status |", "| ---: | --- | --- | --- |"]
    for r in rows:
        url = f"https://leetcode.com/problems/{r['slug']}/"
        out.append(
            f"| {r['id']} | [{r['title']}]({url}) | {r['difficulty']} | {'✅' if r['ac'] else '—'} |"
        )
    solved = sum(1 for r in rows if r["ac"])
    out += ["", f"_{solved} solved / {len(rows)} tracked_"]
    return "\n".join(out)


def _summary(rows: list[dict]) -> str:
    """Compact `solved / tracked` table broken down by difficulty, for the repo landing page."""
    tally = {d: [0, 0] for d in ("Easy", "Medium", "Hard")}
    for r in rows:
        if r["difficulty"] in tally:
            tally[r["difficulty"]][1] += 1
            tally[r["difficulty"]][0] += int(bool(r["ac"]))
    solved, total = sum(1 for r in rows if r["ac"]), len(rows)
    cells = " | ".join(
        f"{s} / {t}" for s, t in (tally[d] for d in ("Easy", "Medium", "Hard"))
    )
    return (
        "| Total | Easy | Medium | Hard |\n"
        "| :-: | :-: | :-: | :-: |\n"
        f"| {solved} / {total} | {cells} |"
    )


def _write(path: Path, start: str, end: str, body: str, title: str) -> None:
    block = f"{start}\n{body}\n{end}"
    text = path.read_text(encoding="utf-8") if path.exists() else ""
    if start in text and end in text:
        text = text.split(start, 1)[0] + block + text.split(end, 1)[1]
    else:
        if text and not text.endswith("\n"):
            text += "\n"
        text += f"\n## {title}\n\n{block}\n"
    path.write_text(text, encoding="utf-8")


def main() -> None:
    session = _session()
    rows = _rows(_repo_slugs(), _fetch_pairs(session))
    _write(README, START, END, _table(rows), "Progress")
    _write(
        REPO_README, SUMMARY_START, SUMMARY_END, _summary(rows), "Progress at a glance"
    )
    solved = sum(1 for r in rows if r["ac"])
    note = (
        ""
        if session
        else "  (no LEETCODE_SESSION - status shown as not-solved; set it in .env for real status)"
    )
    print(f"Tracked {len(rows)} problem(s), {solved} solved.{note}")


if __name__ == "__main__":
    main()
