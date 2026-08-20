#!/usr/bin/env python3
# Created by Justin Park at 2026/08/04 06:09
# leetgo: 1.4.17
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

from typing import List

from leetgo_py import deserialize, read_line, serialize

# @lc code=begin


class Solution:
    phone_number_mapping: dict[str, str]

    def __init__(self):
        self.phone_number_mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

    # N = number of digits
    # Time Complexity: O(N* 4 ^ N)
    # Auxiliary Space Complexity: O(N)
    # Output Space Complexity: O(N * 4 ^ N)
    def letterCombinations(self, digits: str) -> List[str]:
        result: list[str] = []
        self._backtrack(digits, 0, [], result)
        return result

    def _backtrack(
        self, digits: str, index: int, path: list[str], result: list[str]
    ) -> None:
        if index == len(digits):
            result.append("".join(path))
            return

        digit = digits[index]
        for char in self.phone_number_mapping[digit]:
            path.append(char)
            self._backtrack(digits, index + 1, path, result)
            path.pop()


# @lc code=end

if __name__ == "__main__":
    digits: str = deserialize("str", read_line())
    ans = Solution().letterCombinations(digits)
    print("\noutput:", serialize(ans, "string[]"))
