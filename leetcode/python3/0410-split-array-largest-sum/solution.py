#!/usr/bin/env python
# Created by Justin Park at 2026/10/26 19:46
# leetgo: 1.5.1
# https://leetcode.com/problems/split-array-largest-sum/


from leetgo_py import deserialize, read_line, serialize

# @lc code=begin


class Solution:
    # N = length of array, S = sum of array - max of array + 1
    # Time Complexity: O(N log(S))
    # Space Complexity: O(1)
    def splitArray(self, nums: list[int], k: int) -> int:
        # Lower and upper bounds for sum limits
        left = max(nums)
        right = sum(nums)

        while left < right:
            mid = (left + right) // 2
            num_splits = 1
            curr_sum = 0

            # Partition nums according to sum limit
            for num in nums:
                curr_sum += num
                if curr_sum > mid:
                    curr_sum = num
                    num_splits += 1

                if num_splits > k:
                    break

            if num_splits > k:
                left = mid + 1
            else:
                right = mid

        return left


# @lc code=end

if __name__ == "__main__":
    nums: list[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().splitArray(nums, k)
    print("\noutput:", serialize(ans, "integer"))
