#!/usr/bin/env python
# Created by Justin Park at 2026/08/06 18:38
# leetgo: 1.4.17
# https://leetcode.com/problems/palindrome-partitioning/


from leetgo_py import deserialize, read_line, serialize

# @lc code=begin


class Solution:
    # N = length of string
    # Time Complexity: O(N * 2 ^ N)
    # Auxiliary Space Complexity: O(N)
    # Output Space Complexity: O(N * 2 ^ N)
    def partition(self, s: str) -> list[list[str]]:
        results: list[list[str]] = []
        self._backtrack(s, 0, [], results)
        return results

    def _is_palindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1

        return True

    def _backtrack(
        self,
        s: str,
        start: int,
        palindrome_path: list[str],
        results: list[list[str]],
    ) -> None:
        n = len(s)

        if start == n:
            results.append(palindrome_path[:])
            return

        for i in range(start + 1, n + 1):
            substring = s[start:i]
            if self._is_palindrome(substring):
                palindrome_path.append(substring)
                self._backtrack(s, i, palindrome_path, results)
                _ = palindrome_path.pop()


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().partition(s)
    print("\noutput:", serialize(ans, "string[][]"))
