#!/usr/bin/env python
# Created by Justin Park at 2026/11/02 19:23
# leetgo: 1.5.2
# https://leetcode.com/problems/paint-house/

from leetgo_py import deserialize, read_line, serialize

# @lc code=begin


class Solution:
    # N = number of houses
    # Time Complexity: O(N)
    # Space Complexity: O(1)
    def minCost(self, costs: list[list[int]]) -> int:
        n = len(costs)
        dp: list[int] = costs[0][:]

        for i in range(1, n):
            r_cost, b_cost, g_cost = dp
            dp[0] = costs[i][0] + min(b_cost, g_cost)
            dp[1] = costs[i][1] + min(r_cost, g_cost)
            dp[2] = costs[i][2] + min(r_cost, b_cost)

        return min(dp)


# @lc code=end

if __name__ == "__main__":
    costs: list[list[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().minCost(costs)
    print("\noutput:", serialize(ans, "integer"))
