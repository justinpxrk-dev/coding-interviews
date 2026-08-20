#!/usr/bin/env python
# Created by Justin Park at 2026/07/13 21:20
# leetgo: 1.4.17
# https://leetcode.com/problems/jump-game-ii/


from leetgo_py import deserialize, read_line, serialize

# @lc code=begin


class Solution:
    # N = length of list
    # Time Complexity: O(N)
    # Space Complexity: O(1)
    def jump(self, nums: list[int]) -> int:
        num_jumps = 0
        i = 0
        n = len(nums)
        max_reachable_index = 0

        while i < n - 1:
            for j in range(i + 1, i + nums[i] + 1):
                if j + nums[j] > max_reachable_index:
                    max_reachable_index = j + nums[j]
                    i = j

            num_jumps += 1

        return num_jumps


# @lc code=end

if __name__ == "__main__":
    nums: list[int] = deserialize("List[int]", read_line())
    ans = Solution().jump(nums)
    print("\noutput:", serialize(ans, "integer"))
