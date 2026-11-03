#!/usr/bin/env python
# Created by Justin Park at 2026/10/28 14:40
# leetgo: 1.5.2
# https://leetcode.com/problems/median-of-two-sorted-arrays/

import math

from leetgo_py import deserialize, read_line, serialize

# @lc code=begin


class Solution:
    # M = length of nums1, N = length of nums2
    # Time Complexity: O(log(min(M, N)))
    # Space Complexity: O(1)
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        m, n = len(nums1), len(nums2)
        if m > n:
            m, n = n, m
            nums1, nums2 = nums2, nums1

        left, right = 0, m
        while left <= right:
            i = (left + right) // 2
            j = (m + n) // 2 - i

            left1 = -math.inf if i == 0 else nums1[i - 1]
            right1 = math.inf if i == m else nums1[i]
            left2 = -math.inf if j == 0 else nums2[j - 1]
            right2 = math.inf if j == n else nums2[j]

            if left1 <= right2 and left2 <= right1:
                # Found median
                if (m + n) % 2 == 1:
                    return min(right1, right2)
                else:
                    return (max(left1, left2) + min(right1, right2)) / 2

            if left1 > right2:
                right = i - 1
            else:
                left = i + 1

        return 0.0


# @lc code=end

if __name__ == "__main__":
    nums1: list[int] = deserialize("List[int]", read_line())
    nums2: list[int] = deserialize("List[int]", read_line())
    ans = Solution().findMedianSortedArrays(nums1, nums2)
    print("\noutput:", serialize(ans, "double"))
