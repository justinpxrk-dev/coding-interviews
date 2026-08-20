#!/usr/bin/env python
# Created by Justin Park at 2026/08/07 02:08
# leetgo: 1.4.17
# https://leetcode.com/problems/n-queens/


from leetgo_py import deserialize, read_line, serialize

# @lc code=begin


class Solution:
    # N = length of board, S = number of valid solutions
    # Time Complexity: O(N! + S * N ^ 2)
    # Auxiliary Space Complexity: O(N)
    # Output Space Complexity: O(S * N ^ 2)
    def solveNQueens(self, n: int) -> list[list[str]]:
        results: list[list[str]] = []
        self._backtrack(n, 0, [], set(), set(), set(), results)
        return results

    def _backtrack(
        self,
        n: int,
        row: int,
        columns_path: list[int],
        used_columns: set[int],
        used_diagonals_left: set[int],
        used_diagonals_right: set[int],
        results: list[list[str]],
    ) -> None:
        if row == n:
            results.append([])
            for column in columns_path:
                column_str: list[str] = ["Q" if c == column else "." for c in range(n)]
                results[-1].append("".join(column_str))
            return

        for c in range(n):
            diagonal_left = row + c
            diagonal_right = row - c

            if (
                c in used_columns
                or diagonal_left in used_diagonals_left
                or diagonal_right in used_diagonals_right
            ):
                continue

            columns_path.append(c)
            used_columns.add(c)
            used_diagonals_left.add(diagonal_left)
            used_diagonals_right.add(diagonal_right)

            self._backtrack(
                n,
                row + 1,
                columns_path,
                used_columns,
                used_diagonals_left,
                used_diagonals_right,
                results,
            )

            _ = columns_path.pop()
            used_columns.remove(c)
            used_diagonals_left.remove(diagonal_left)
            used_diagonals_right.remove(diagonal_right)


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().solveNQueens(n)
    print("\noutput:", serialize(ans, "string[][]"))
