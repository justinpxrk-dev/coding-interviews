#!/usr/bin/env python
# Created by Justin Park at 2026/10/23 15:41
# leetgo: 1.5.1
# https://leetcode.com/problems/search-in-rotated-sorted-array/

from leetgo_py import deserialize, read_line, serialize

# @lc code=begin


class Solution:
    # N = length of array
    # Time Complexity: O(log(N))
    # Space Complexity: O(1)
    def search(self, nums: list[int], target: int) -> int:
        n = len(nums)
        left, right = 0, n - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            if nums[left] <= nums[mid]:
                # Left half is sorted
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                # Right half is sorted
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1


# @lc code=end

if __name__ == "__main__":
    nums: list[int] = deserialize("List[int]", read_line())
    target: int = deserialize("int", read_line())
    ans = Solution().search(nums, target)
    print("\noutput:", serialize(ans, "integer"))
