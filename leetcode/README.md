# LeetCode (Python)

Problems are generated, tested, and submitted with [leetgo](https://github.com/j178/leetgo).
Progress tracking is a tiny standard-library script (`python3 -m lc`) that reads your **live**
LeetCode status — no third-party Python dependencies.

## Setup

- Install leetgo: `brew install j178/tap/leetgo`
- `leetgo.yaml` is configured to generate **Python3** solutions into `python3/<id>-<slug>/`.
- Auth: both leetgo and the tracker read credentials from `.env` (gitignored — never commit it). Copy `.env.example` to `.env`, then fill in from DevTools → Application → Cookies → leetcode.com:
  - `LEETCODE_SESSION` ← the `LEETCODE_SESSION` cookie
  - `LEETCODE_CSRFTOKEN` ← the `csrftoken` cookie

## Workflow

```bash
leetgo pick two-sum        # -> python3/0001-two-sum/{solution.py,testcases.txt,question.md}
# write your code between the `@lc code=begin` / `@lc code=end` markers in solution.py
leetgo test last -L        # run the sample cases LOCALLY (note the -L flag)
leetgo test last           # run on LeetCode's judge (also back-fills expected outputs)
leetgo submit last         # submit (needs credentials in .env)
python3 -m lc              # regenerate the Progress table below from live status
```

`leetgo pick` accepts a number (`2`), a slug (`add-two-numbers`), or `today`; `last` refers to the
most recently generated problem. Run `python3 -m lc` anytime to refresh the table (pure stdlib, so no venv is needed).

## How tracking works

`python3 -m lc` scans `python3/` for problem folders, fetches your solved status from LeetCode's
problem-list API (authenticated via `LEETCODE_SESSION`), and rewrites the table between the markers.
It reflects your real account no matter how you submitted — leetgo, the website, anything.

## Notes

- `python3/.venv` + `python3/requirements.txt` are leetgo's local-test harness (the `.venv` is gitignored).

## Progress

<!-- LC-INDEX:START -->
| # | Problem | Difficulty | Status |
| ---: | --- | --- | --- |
| 1 | [Two Sum](https://leetcode.com/problems/two-sum/) | Easy | ✅ |
| 2 | [Add Two Numbers](https://leetcode.com/problems/add-two-numbers/) | Medium | ✅ |
| 3 | [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | Medium | ✅ |
| 4 | [Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/) | Hard | — |
| 5 | [Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/) | Medium | ✅ |
| 16 | [3Sum Closest](https://leetcode.com/problems/3sum-closest/) | Medium | ✅ |
| 23 | [Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/) | Hard | ✅ |
| 55 | [Jump Game](https://leetcode.com/problems/jump-game/) | Medium | ✅ |
| 79 | [Word Search](https://leetcode.com/problems/word-search/) | Medium | ✅ |
| 112 | [Path Sum](https://leetcode.com/problems/path-sum/) | Easy | ✅ |
| 121 | [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) | Easy | ✅ |
| 134 | [Gas Station](https://leetcode.com/problems/gas-station/) | Medium | ✅ |
| 207 | [Course Schedule](https://leetcode.com/problems/course-schedule/) | Medium | ✅ |
| 210 | [Course Schedule II](https://leetcode.com/problems/course-schedule-ii/) | Medium | ✅ |
| 261 | [Graph Valid Tree](https://leetcode.com/problems/graph-valid-tree/) | Medium | ✅ |
| 295 | [Find Median from Data Stream](https://leetcode.com/problems/find-median-from-data-stream/) | Hard | ✅ |
| 305 | [Number of Islands II](https://leetcode.com/problems/number-of-islands-ii/) | Hard | ✅ |
| 412 | [Fizz Buzz](https://leetcode.com/problems/fizz-buzz/) | Easy | ✅ |
| 455 | [Assign Cookies](https://leetcode.com/problems/assign-cookies/) | Easy | ✅ |
| 609 | [Find Duplicate File in System](https://leetcode.com/problems/find-duplicate-file-in-system/) | Medium | ✅ |
| 658 | [Find K Closest Elements](https://leetcode.com/problems/find-k-closest-elements/) | Medium | ✅ |
| 802 | [Find Eventual Safe States](https://leetcode.com/problems/find-eventual-safe-states/) | Medium | ✅ |
| 815 | [Bus Routes](https://leetcode.com/problems/bus-routes/) | Hard | ✅ |

_22 solved / 23 tracked_
<!-- LC-INDEX:END -->
