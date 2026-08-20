#!/usr/bin/env python
# Created by Justin Park at 2026/08/06 01:58
# leetgo: 1.4.17
# https://leetcode.com/problems/decode-ways/


from leetgo_py import deserialize, read_line, serialize

# @lc code=begin


class Solution:
    # N = length of string
    # Time Complexity: O(N)
    # Space Complexity: O(1)
    def numDecodings(self, s: str) -> int:
        n = len(s)
        prev, curr = 1, 1

        for i in range(n):
            next_ = 0

            if s[i] != "0":
                next_ += curr

            digits = int(s[max(i - 1, 0) : i + 1])
            if 10 <= digits <= 26:
                next_ += prev

            prev, curr = curr, next_

        return curr


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().numDecodings(s)
    print("\noutput:", serialize(ans, "integer"))
