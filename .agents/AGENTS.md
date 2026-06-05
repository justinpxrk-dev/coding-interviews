# AGENTS.md

Guidance for AI coding agents working in this repository.

## What this is

A personal coding-interview practice repo. Today it holds LeetCode solutions in Python under `leetcode/python3/`, driven by the external **leetgo** CLI plus a small custom progress tracker (`leetcode/lc/`). Frontend exercises may be added alongside `leetcode/` later.

## Agent conventions

- **`.agents/lessons.md`** (gitignored, local-only) — a running log of mistakes and corrections. Read it before starting, and append a short dated entry whenever you get something wrong or the maintainer corrects you, so the same mistake isn't repeated. Because it's gitignored, a fresh clone won't have it — if it's missing, create it first with a `# Lessons` heading followed by `## YYYY-MM-DD` sections that hold the bullet entries.
- **`.agents/personalities/*.md`** — personality definitions you can adopt. When asked to assume a personality, read the matching file and follow its voice and priorities for that session. `template.md` is the skeleton for writing new ones, not a persona itself.

## Commands

Run everything from the `leetcode/` directory — that's where `leetgo.yaml` and the `lc` package live.

```bash
leetgo pick <id>        # scaffold python3/<id>-<slug>/ (accepts a number, slug, or `today`)
leetgo test <id> -L     # run that problem's testcases.txt LOCALLY (the -L flag is required for local)
leetgo test <id>        # run on LeetCode's judge; also back-fills expected outputs into testcases.txt
leetgo submit <id>      # submit to LeetCode (needs auth; see below)
python3 -m lc           # regenerate the progress tables from live LeetCode status
```

`last` works in place of `<id>` (the most recently picked problem); `leetgo test <id> -L` is the single-problem test loop. There is **no build or lint step and no unit-test framework** — leetgo is the whole dev/test loop.

Setup: `brew install j178/tap/leetgo`. Python 3.14 is pinned in `leetcode/.python-version`; leetgo auto-creates its own venv at `leetcode/python3/.venv` (from `python3/requirements.txt`: `sortedcontainers`, `leetgo_py`) on first pick/test.

## Architecture

**leetgo owns scaffolding, testing, and submitting.** Config is `leetcode/leetgo.yaml`. Each problem is a folder `python3/<id>-<slug>/` (id zero-padded to 4) containing `solution.py`, `question.md`, and `testcases.txt`. Solutions land in `python3/` per `code.python3.out_dir` — which also equals leetgo's default for the `python3` language slug.

**`solution.py` is partly generated.** Write solution code ONLY between the `# @lc code=begin` and `# @lc code=end` markers. leetgo regenerates everything outside them: imports plus a `__main__` harness that uses `leetgo_py` (`deserialize` / `read_line` / `serialize`) to read each case from stdin. `testcases.txt` is `input:` / `output:` blocks separated by blank lines.

**`lc` is a standalone progress tracker** (`leetcode/lc/`, run as `python3 -m lc`). Pure standard library, no third-party deps. It scans `python3/` for `<id>-<slug>` folders, makes one authenticated GET to `https://leetcode.com/api/problems/all/`, and rewrites two **generated** Markdown regions in place:
- full per-problem table in `leetcode/README.md` between `<!-- LC-INDEX:START -->` / `<!-- LC-INDEX:END -->`
- `solved / tracked` difficulty summary in the **root** `README.md` between `<!-- LC-SUMMARY:START -->` / `<!-- LC-SUMMARY:END -->`

Do not hand-edit content between those markers — it is overwritten on the next run. Status reflects the real LeetCode account no matter how a problem was solved (leetgo, website, anything).

**Coupling to keep in sync:** `PROBLEMS = ROOT / "python3"` in `lc/tracker.py` is hardcoded to mirror `code.python3.out_dir` in `leetgo.yaml`. If you change the output directory, update it in lockstep across four places: `leetgo.yaml`, `lc/tracker.py`, the root `.gitignore` (`leetcode/python3/requirements.txt`), and the `python3/` path references in both READMEs.

## Auth

Both tools read credentials from `leetcode/.env` (gitignored; copy from `.env.example`):
- **leetgo** is configured `credentials.from: [cookies]`, so it reads `LEETCODE_SESSION` + `LEETCODE_CSRFTOKEN` from `.env`/env — **not** the browser, despite the comment wording in `leetgo.yaml`.
- **tracker** reads `LEETCODE_SESSION`. Without it, `python3 -m lc` still runs but marks everything not-solved.

`leetgo test -L` works without auth; `submit` and live status require it.

## READMEs

Two levels, both partly generated: the **root `README.md`** is the landing page (description → progress summary → workflow → getting started); **`leetcode/README.md`** has the detailed workflow and the full progress table. Prose is hand-written; the marker regions above are machine-written.

## Commits

Do not add a `Co-Authored-By` trailer to commit messages.
