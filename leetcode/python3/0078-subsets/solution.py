#!/usr/bin/env python
# Created by Justin Park at 2026/08/04 21:50
# leetgo: 1.4.17
# https://leetcode.com/problems/subsets/

from leetgo_py import deserialize, read_line, serialize

# @lc code=begin


class Solution:
    # N = number of elements
    # Time Complexity: O(N * 2 ^ N)
    # Auxiliary Space Complexity: O(N)
    # Output Space Complexity: O(N * 2 ^ N)
    def subsets(self, nums: list[int]) -> list[list[int]]:
        result: list[list[int]] = []
        self._backtrack(nums, 0, [], result)
        return result

    def _backtrack(
        self, nums: list[int], index: int, path: list[int], result: list[list[int]]
    ) -> None:
        if index == len(nums):
            result.append(path[:])
            return

        # Exclude current element
        self._backtrack(nums, index + 1, path, result)

        # Include current element
        path.append(nums[index])
        self._backtrack(nums, index + 1, path, result)
        path.pop()


# @lc code=end

if __name__ == "__main__":
    nums: list[int] = deserialize("List[int]", read_line())
    ans = Solution().subsets(nums)
    print("\noutput:", serialize(ans, "integer[][]"))
