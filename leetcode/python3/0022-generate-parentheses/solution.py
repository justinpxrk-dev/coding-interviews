#!/usr/bin/env python
# Created by Justin Park at 2026/08/04 23:02
# leetgo: 1.4.17
# https://leetcode.com/problems/generate-parentheses/


from leetgo_py import deserialize, read_line, serialize

# @lc code=begin


class Solution:
    # N = number of parentheses
    # Time Complexity: O(N * Catalan(N)) = O(4 ^ N / sqrt(N))
    # Auxiliary Space Complexity: O(N)
    # Output Space Complexity: O(N * Catalan(N)) = O(4 ^ N / sqrt(N))
    def generateParenthesis(self, n: int) -> list[str]:
        result: list[str] = []
        self._backtrack(n, n, [], result)
        return result

    def _backtrack(
        self, num_left: int, num_right: int, path: list[str], result: list[str]
    ) -> None:
        if num_left == 0 and num_right == 0:
            result.append("".join(path))
            return

        if num_left > 0:
            path.append("(")
            self._backtrack(num_left - 1, num_right, path, result)
            path.pop()

        if num_right > num_left:
            path.append(")")
            self._backtrack(num_left, num_right - 1, path, result)
            path.pop()


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().generateParenthesis(n)
    print("\noutput:", serialize(ans, "string[]"))
