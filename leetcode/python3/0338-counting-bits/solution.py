#!/usr/bin/env python
# Created by Justin Park at 2026/08/05 23:50
# leetgo: 1.4.17
# https://leetcode.com/problems/counting-bits/


from leetgo_py import deserialize, read_line, serialize

# @lc code=begin


class Solution:
    # N = number of integeres
    # Time Complexity: O(N)
    # Space Complexity: O(N)
    def countBits(self, n: int) -> list[int]:
        dp: list[int] = [0] * (n + 1)

        for i in range(1, n + 1):
            dp[i] = dp[i // 2] + i % 2

        return dp


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().countBits(n)
    print("\noutput:", serialize(ans, "integer[]"))
