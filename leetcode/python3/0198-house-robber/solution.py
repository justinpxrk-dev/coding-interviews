#!/usr/bin/env python
# Created by Justin Park at 2026/08/05 03:22
# leetgo: 1.4.17
# https://leetcode.com/problems/house-robber/

from leetgo_py import deserialize, read_line, serialize

# @lc code=begin


class Solution:
    # N = number of houses
    # Time Complexity: O(N)
    # Space Complexity: O(1)
    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        prev, curr = 0, 0
        for i in range(n):
            prev, curr = curr, max(nums[i] + prev, curr)

        return curr


# @lc code=end

if __name__ == "__main__":
    nums: list[int] = deserialize("List[int]", read_line())
    ans = Solution().rob(nums)
    print("\noutput:", serialize(ans, "integer"))
