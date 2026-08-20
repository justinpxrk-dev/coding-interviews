# Created by Justin Park at 2026/07/15 19:34
# leetgo: 1.4.17
# https://leetcode.com/problems/subarray-sum-equals-k/

from typing import List
from leetgo_py import deserialize, read_line, serialize

# @lc code=begin

class Solution:
    # N = length of nums
    # Time Complexity: O(N)
    # Space Complexity: O(N)
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sums: dict[int, int] = {0: 1}
        num_subarrays = 0
        prefix_sum = 0
        for num in nums:
            prefix_sum += num
            target_sum = prefix_sum - k

            if target_sum in prefix_sums:
                num_subarrays += prefix_sums[target_sum]

            prefix_sums[prefix_sum] = prefix_sums.get(prefix_sum, 0) + 1

        return num_subarrays


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().subarraySum(nums, k)
    print("\noutput:", serialize(ans, "integer"))
