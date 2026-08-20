#!/usr/bin/env python
# Created by Justin Park at 2026/08/05 03:10
# leetgo: 1.4.17
# https://leetcode.com/problems/climbing-stairs/

from leetgo_py import deserialize, read_line, serialize

# @lc code=begin


class Solution:
    # N = n
    # Time Complexity: O(N)
    # Space Complexity: O(1)
    def climbStairs(self, n: int) -> int:
        prev_step = 1
        curr_step = 1

        for _ in range(2, n + 1):
            next_step = prev_step + curr_step
            prev_step, curr_step = curr_step, next_step

        return curr_step


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().climbStairs(n)
    print("\noutput:", serialize(ans, "integer"))
