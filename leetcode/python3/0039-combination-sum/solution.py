#!/usr/bin/env python
# Created by Justin Park at 2026/08/04 23:40
# leetgo: 1.4.17
# https://leetcode.com/problems/combination-sum/

from leetgo_py import deserialize, read_line, serialize

# @lc code=begin


class Solution:
    # N = number of candidates, T = value of target, m = minimum value of candidates
    # K = number of combinations
    # Time Complexity: O(N log(N) + N ^ (T / m) + K * T / m)
    # Auxiliary Space Complexity: O(N + T / m)
    # Output Space Complexity: O(K * T / m)
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        sorted_candidates: list[int] = sorted(candidates)
        results: list[list[int]] = []
        self._backtrack(sorted_candidates, target, 0, [], results)
        return results

    def _backtrack(
        self,
        sorted_candidates: list[int],
        target: int,
        start: int,
        candidates_path: list[int],
        results: list[list[int]],
    ) -> None:
        n = len(sorted_candidates)

        if target == 0:
            results.append(candidates_path[:])
            return

        for i in range(start, n):
            candidate = sorted_candidates[i]

            if candidate > target:
                break

            candidates_path.append(candidate)
            self._backtrack(
                sorted_candidates,
                target - candidate,
                i,
                candidates_path,
                results,
            )
            _ = candidates_path.pop()


# @lc code=end

if __name__ == "__main__":
    candidates: list[int] = deserialize("List[int]", read_line())
    target: int = deserialize("int", read_line())
    ans = Solution().combinationSum(candidates, target)
    print("\noutput:", serialize(ans, "integer[][]"))
