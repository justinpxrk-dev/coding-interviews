#!/usr/bin/env python
# Created by Justin Park at 2026/09/11 14:59
# leetgo: 1.4.18
# https://leetcode.com/problems/n-queens-ii/

from leetgo_py import deserialize, read_line, serialize

# @lc code=begin


class Solution:
    # N = length of board
    # Time Complexity: O(N!)
    # Auxiliary Space Complexity: O(N)
    # Output Space Complexity: O(1)
    def totalNQueens(self, n: int) -> int:
        return self._backtrack(n, 0, set(), set(), set())

    def _backtrack(
        self,
        n: int,
        row: int,
        used_columns: set[int],
        used_diagonals_left: set[int],
        used_diagonals_right: set[int],
    ) -> int:
        if row == n:
            return 1

        num_solutions = 0

        for column in range(n):
            diagonal_left = column + row
            diagonal_right = column - row

            if (
                column not in used_columns
                and diagonal_left not in used_diagonals_left
                and diagonal_right not in used_diagonals_right
            ):
                used_columns.add(column)
                used_diagonals_left.add(diagonal_left)
                used_diagonals_right.add(diagonal_right)

                num_solutions += self._backtrack(
                    n,
                    row + 1,
                    used_columns,
                    used_diagonals_left,
                    used_diagonals_right,
                )

                used_columns.remove(column)
                used_diagonals_left.remove(diagonal_left)
                used_diagonals_right.remove(diagonal_right)

        return num_solutions


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().totalNQueens(n)
    print("\noutput:", serialize(ans, "integer"))
