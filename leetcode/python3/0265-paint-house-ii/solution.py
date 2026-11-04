#!/usr/bin/env python
# Created by Justin Park at 2026/11/02 20:58
# leetgo: 1.5.2
# https://leetcode.com/problems/paint-house-ii/

import math

from leetgo_py import deserialize, read_line, serialize

# @lc code=begin


class Solution:
    # N = number of houses
    # Time Complexity: O(Nk)
    # Space Complexity: O(k)
    def minCostII(self, costs: list[list[int]]) -> int:
        n, k = len(costs), len(costs[0])

        dp: list[int] = costs[0][:]
        for i in range(1, n):
            # Find the two smallest costs from previous dp row
            min_cost_1: tuple[float, int] = (math.inf, -1)
            min_cost_2: float = math.inf
            for j, cost in enumerate(dp):
                if cost <= min_cost_1[0]:
                    min_cost_2 = min_cost_1[0]
                    min_cost_1 = (cost, j)
                elif cost < min_cost_2:
                    min_cost_2 = cost

            for j in range(k):
                dp[j] = costs[i][j] + int(
                    min_cost_1[0] if j != min_cost_1[1] else min_cost_2
                )

        return min(dp)


# @lc code=end

if __name__ == "__main__":
    costs: list[list[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().minCostII(costs)
    print("\noutput:", serialize(ans, "integer"))
