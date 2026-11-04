#!/usr/bin/env python
# Created by Justin Park at 2026/11/02 22:24
# leetgo: 1.5.2
# https://leetcode.com/problems/minimum-window-subsequence/

from leetgo_py import deserialize, read_line, serialize

# @lc code=begin


class Solution:
    # M = length of s1, N = length of s2
    # Time Complexity: O(MN)
    # Space Complexity: O(N)
    def minWindow(self, s1: str, s2: str) -> str:
        m, n = len(s1), len(s2)
        dp: list[int] = [-1] * n
        min_start, min_end = -1, -1

        for j in range(m):
            upper_left = -1

            for i in range(min(j + 1, n)):
                temp = dp[i]

                if s1[j] == s2[i]:
                    dp[i] = upper_left if i != 0 else j

                upper_left = temp

            if dp[-1] != -1 and (
                min_start == -1 or j + 1 - dp[-1] < min_end - min_start
            ):
                min_start, min_end = dp[-1], j + 1

        return s1[min_start:min_end] if min_start != -1 else ""


# @lc code=end

if __name__ == "__main__":
    s1: str = deserialize("str", read_line())
    s2: str = deserialize("str", read_line())
    ans = Solution().minWindow(s1, s2)
    print("\noutput:", serialize(ans, "string"))
