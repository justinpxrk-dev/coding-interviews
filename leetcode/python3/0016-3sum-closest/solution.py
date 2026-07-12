# Created by Justin Park at 2026/06/26 09:56
# leetgo: 1.4.17
# https://leetcode.com/problems/3sum-closest/

from typing import List

from leetgo_py import deserialize, read_line, serialize

# @lc code=begin


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums_sorted, n = sorted(nums), len(nums)

        min_distance = float("inf")
        for i in range(n - 2):
            left, right = i + 1, n - 1
            while left < right:
                distance = (
                    nums_sorted[i] + nums_sorted[left] + nums_sorted[right] - target
                )

                if abs(distance) < abs(min_distance):
                    min_distance = distance

                if distance > 0:
                    right -= 1
                elif distance < 0:
                    left += 1
                else:
                    return target

        return int(min_distance) + target


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    target: int = deserialize("int", read_line())
    ans = Solution().threeSumClosest(nums, target)
    print("\noutput:", serialize(ans, "integer"))
