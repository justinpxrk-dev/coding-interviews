#!/usr/bin/env python
# Created by Justin Park at 2026/08/20 16:44
# leetgo: 1.4.18
# https://leetcode.com/problems/jump-game-ii/


from leetgo_py import deserialize, read_line, serialize

# @lc code=begin


class Solution:
    # N = length of array
    # Time Complexity: O(N)
    # Space Complexity: O(1)
    def jump(self, nums: list[int]) -> int:
        n = len(nums)
        last_reachable_index = max_reachable_index = 0
        num_jumps = 0

        for i in range(n - 1):
            max_reachable_index = max(max_reachable_index, i + nums[i])

            if i == last_reachable_index:
                num_jumps += 1
                last_reachable_index = min(max_reachable_index, n - 1)

        return num_jumps


# @lc code=end

if __name__ == "__main__":
    nums: list[int] = deserialize("List[int]", read_line())
    ans = Solution().jump(nums)
    print("\noutput:", serialize(ans, "integer"))
