#!/usr/bin/env python
# Created by  Justin Park at 2026/10/07 18:12
# leetgo: 1.5.1
# https://leetcode.com/problems/longest-increasing-subsequence/

from bisect import bisect_left

from leetgo_py import deserialize, read_line, serialize

# @lc code=begin


class Solution:
    # N = length of nums
    # Time Complexity: O(N log(N))
    # Auxiliary Space Complexity: O(N)
    # Output Space Complexity: O(1)
    def lengthOfLIS(self, nums: list[int]) -> int:
        subsequence: list[int] = []
        lis_length = 0

        for num in nums:
            if not subsequence or num > subsequence[-1]:
                subsequence.append(num)
            else:
                index = bisect_left(subsequence, num)
                subsequence[index] = num

            lis_length = max(lis_length, len(subsequence))

        return lis_length


# @lc code=end

if __name__ == "__main__":
    nums: list[int] = deserialize("List[int]", read_line())
    ans = Solution().lengthOfLIS(nums)
    print("\noutput:", serialize(ans, "integer"))
