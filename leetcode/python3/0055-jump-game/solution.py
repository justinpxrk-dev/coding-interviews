# Created by Justin Park at 2026/07/09 21:05
# leetgo: 1.4.17
# https://leetcode.com/problems/jump-game/

from typing import List
from leetgo_py import deserialize, read_line, serialize

# @lc code=begin

class Solution:
    # Time Complexity: O(N)
    # Space Complexity: O(1)
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        reachable_index = 0
        for i in range(n):
            if i > reachable_index:
                return False

            reachable_index = max(reachable_index, i + nums[i])

        return True

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().canJump(nums)
    print("\noutput:", serialize(ans, "boolean"))
