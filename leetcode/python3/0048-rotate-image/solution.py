#!/usr/bin/env python3
# Created by Justin Park at 2026/07/27 21:11
# leetgo: 1.4.17
# https://leetcode.com/problems/rotate-image/

from typing import List

from leetgo_py import deserialize, read_line, serialize

# @lc code=begin

class Solution:
    # M = number of elements in matrix
    # Time Complexity: O(M)
    # Space Complexity: O(1)
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        for i in range(n):
            for j in range(i + 1):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for row in matrix:
            row.reverse()

# @lc code=end

if __name__ == "__main__":
    matrix: List[List[int]] = deserialize("List[List[int]]", read_line())
    Solution().rotate(matrix)
    ans = matrix
    print("\noutput:", serialize(ans, "List[List[int]]"))
