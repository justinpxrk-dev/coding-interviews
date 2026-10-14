#!/usr/bin/env python
# Created by Justin Park at 2026/10/06 23:21
# leetgo: 1.5.1
# https://leetcode.com/problems/maximal-square/

from leetgo_py import deserialize, read_line, serialize

# @lc code=begin


class Solution:
    # M = length of matrix, N = width of matrix
    # Time Complexity: O(MN)
    # Auxiliary Space Complexity: O(N)
    # Output Space Complexity: O(1)
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp: list[int] = [0] * (n + 1)
        max_square_length = 0

        for row in range(1, m + 1):
            upper_left = dp[0]
            for col in range(1, n + 1):
                upper = dp[col]
                left = dp[col - 1]

                if matrix[row - 1][col - 1] == "1":
                    min_square_length = min(upper_left, upper, left)
                    dp[col] = min_square_length + 1
                    max_square_length = max(max_square_length, dp[col])
                    upper_left = upper
                else:
                    dp[col] = 0

        return max_square_length**2


# @lc code=end

if __name__ == "__main__":
    matrix: list[list[str]] = deserialize("List[List[str]]", read_line())
    ans = Solution().maximalSquare(matrix)
    print("\noutput:", serialize(ans, "integer"))
