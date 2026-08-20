#!/usr/bin/env python3
# Created by Justin Park at 2026/07/16 05:45
# leetgo: 1.4.17
# https://leetcode.com/problems/spiral-matrix/

from leetgo_py import deserialize, read_line, serialize

# @lc code=begin

class Solution:
    # M = number of rows, N = number of columns
    # Time Complexity: O(MN)
    # Space Complexity: O(1)
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        col_steps = len(matrix[0])
        row_steps = len(matrix) - 1
        direction = 1
        order: list[int] = []
        r, c = 0, -1
        while col_steps > 0 and row_steps >= 0:
            for _ in range(col_steps):
                c += direction
                order.append(matrix[r][c])

            for _ in range(row_steps):
                r += direction
                order.append(matrix[r][c])

            col_steps -= 1
            row_steps -= 1
            direction *= -1

        return order

# @lc code=end

if __name__ == "__main__":
    matrix: list[list[int]] = deserialize("list[list[int]]", read_line())
    ans = Solution().spiralOrder(matrix)
    print("\noutput:", serialize(ans, "integer[]"))
