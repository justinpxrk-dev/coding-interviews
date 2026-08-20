# Created by Justin Park at 2026/07/29 00:27
# leetgo: 1.4.17
# https://leetcode.com/problems/set-matrix-zeroes/

from typing import List

from leetgo_py import deserialize, read_line, serialize

# @lc code=begin

class Solution:
    # M = number of rows, N = number of columns
    # Time Complexity: O(MN)
    # Space Complexity: O(1)
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])
        first_row_has_zero = any(matrix[0][j] == 0 for j in range(cols))
        first_col_has_zero = any(matrix[i][0] == 0 for i in range(rows))

        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if first_row_has_zero:
            for j in range(cols):
                matrix[0][j] = 0

        if first_col_has_zero:
            for i in range(rows):
                matrix[i][0] = 0

# @lc code=end

if __name__ == "__main__":
    matrix: List[List[int]] = deserialize("List[List[int]]", read_line())
    Solution().setZeroes(matrix)
    ans = matrix
    print("\noutput:", serialize(ans, "List[List[int]]"))
