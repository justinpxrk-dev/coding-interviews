#!/usr/bin/env python
# Created by Justin Park at 2026/10/27 14:10
# leetgo: 1.5.2
# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/

from leetgo_py import deserialize, read_line, serialize

# @lc code=begin


class Solution:
    # N = length of matrix row, S = max(matrix) - min(matrix) + 1
    # Time Complexity: O(N log(S))
    # Space Complexity: O(1)
    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
        n = len(matrix)
        left, right = matrix[0][0], matrix[-1][-1]

        while left < right:
            mid = (left + right) // 2

            num_smaller_elements = 0
            col = n - 1
            for row in matrix:
                while col >= 0 and mid < row[col]:
                    col -= 1

                num_smaller_elements += col + 1

            if num_smaller_elements >= k:
                right = mid
            else:
                left = mid + 1

        return left


# @lc code=end

if __name__ == "__main__":
    matrix: list[list[int]] = deserialize("List[List[int]]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().kthSmallest(matrix, k)
    print("\noutput:", serialize(ans, "integer"))
