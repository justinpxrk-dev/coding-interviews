# Coding Interviews

My personal workspace for coding interview practice — LeetCode solutions in Python (frontend exercises to come). Each problem lives in its own self-contained folder, and a tiny standard library tracker keeps the table below in sync with my live LeetCode account.

## Progress at a glance

<!-- LC-SUMMARY:START -->
| Total | Easy | Medium | Hard |
| :-: | :-: | :-: | :-: |
| 47 / 48 | 7 / 7 | 33 / 33 | 7 / 8 |
<!-- LC-SUMMARY:END -->

`solved / tracked`, refreshed by `python3 -m lc`. Full per-problem list: [`leetcode/README.md`](leetcode/README.md#progress).

## Workflow

Built around [leetgo](https://github.com/j178/leetgo) (scaffold, test, submit) plus the tracker — run from the [`leetcode/`](leetcode/) directory:

| Step | Command | What it does |
| --- | --- | --- |
| **Pick** | `leetgo pick <id>` | Scaffolds the `python3/<id>-<slug>/` folder |
| **Solve** | edit `solution.py` | Write your code between the `@lc code` markers |
| **Test** | `leetgo test <id> -L` | Run the sample cases locally |
| **Submit** | `leetgo submit <id>` | Send to LeetCode's online judge |
| **Track** | `python3 -m lc` | Refresh the progress tables |

## Getting started

These steps take a fresh clone to the point where you can generate, test, and track LeetCode problems.

### 1. Clone

```bash
git clone <repo-url>
cd coding-interviews
```

### 2. Install prerequisites

- **Python 3.15** — the version pinned in [`leetcode/.python-version`](leetcode/.python-version), available as `python3` for leetgo's automatic setup.
- **[uv](https://docs.astral.sh/uv/)** — creates the Python environment and installs its dependencies.
- **[leetgo](https://github.com/j178/leetgo)** — generates, tests, and submits problems.

Install uv and leetgo with Homebrew:

```bash
brew install uv j178/tap/leetgo
```

### 3. Set up the Python environment

From the repository root:

```bash
cd leetcode
uv venv python3/.venv
uv pip sync --python python3/.venv/bin/python python3/requirements.txt
```

uv reads `.python-version` when creating the environment. Leetgo uses `python3/.venv` for local tests; its generated `python3/requirements.txt` is tracked so fresh clones have the dependency versions. The environment itself is gitignored.

After a Python version change, follow the [environment rebuild instructions](leetcode/README.md#rebuilding-the-python-environment). The progress tracker (`python3 -m lc`) uses only the standard library and does not need the venv.

### 4. Set up LeetCode auth

Both leetgo and the progress tracker read your LeetCode credentials from `leetcode/.env`. From the `leetcode/` directory, copy the template:

```bash
cp .env.example .env
```

Then, while logged in to [leetcode.com](https://leetcode.com), open DevTools → Application → Cookies → `https://leetcode.com` and copy the cookie values into `.env`:

- `LEETCODE_SESSION` ← the `LEETCODE_SESSION` cookie
- `LEETCODE_CSRFTOKEN` ← the `csrftoken` cookie

`.env` is gitignored — never commit it.

### 5. Verify

From the `leetcode/` directory:

```bash
python3 -m lc    # rebuild the progress table from your live LeetCode status
leetgo pick 1    # scaffold python3/0001-two-sum/
```

See [`leetcode/README.md`](leetcode/README.md) for the full pick → test → submit → track workflow.

## License

This project is licensed under the **PolyForm Noncommercial License 1.0.0** — see [LICENSE.md](LICENSE.md) for the full text.

In short, you are free to use, study, modify, and share this code for **any noncommercial purpose** (personal learning, hobby projects, academic research, and similar). **Commercial use is not permitted** without a separate license from the author.

```
SPDX-License-Identifier: PolyForm-Noncommercial-1.0.0
```

© 2026 Justin Park
