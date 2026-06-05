# Created by Justin Park at 2026/06/05 07:40
# leetgo: 1.4.17
# https://leetcode.com/problems/two-sum/


from typing import List

from leetgo_py import deserialize, read_line, serialize

# @lc code=begin


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen: dict[int, int] = {}

        for index, num in enumerate(nums):
            if num in seen:
                return [seen[num], index]
            else:
                seen[target - num] = index

        return []


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    target: int = deserialize("int", read_line())
    ans = Solution().twoSum(nums, target)
    print("\noutput:", serialize(ans, "integer[]"))
