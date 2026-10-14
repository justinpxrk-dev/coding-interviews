#!/usr/bin/env python
# Created by Justin Park at 2026/09/11 15:00
# leetgo: 1.4.18
# https://leetcode.com/problems/unique-paths/

from leetgo_py import deserialize, read_line, serialize

# @lc code=begin


# M = length of grid, N = width of grid
# Time Complexity: O(MN)
# Auxiliary Space Complexity: O(N)
# Output Space Complexity: O(1)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1 for _ in range(n)]

        for r in range(1, m):
            for c in range(1, n):
                row[c] = row[c - 1] + row[c]

        return row[n - 1]


# @lc code=end

if __name__ == "__main__":
    m: int = deserialize("int", read_line())
    n: int = deserialize("int", read_line())
    ans = Solution().uniquePaths(m, n)
    print("\noutput:", serialize(ans, "integer"))
