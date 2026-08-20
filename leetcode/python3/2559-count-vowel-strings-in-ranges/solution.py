# Created by Justin Park at 2026/07/15 18:48
# leetgo: 1.4.17
# https://leetcode.com/problems/count-vowel-strings-in-ranges/

from typing import List
from leetgo_py import deserialize, read_line, serialize

# @lc code=begin

class Solution:
    # W = number of words, Q = number of queries
    # Time Complexity: O(W + Q)
    # Space Complexity: O(W)
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        num_vowel_words_memo: list[int] = [0]
        vowels: set[str] = set("aeiou")
        for word in words:
            num_vowel_words_memo.append(num_vowel_words_memo[-1])
            if word[0] in vowels and word[-1] in vowels:
                num_vowel_words_memo[-1] += 1

        results: list[int] = []
        for start, end in queries:
            result = num_vowel_words_memo[end + 1] - num_vowel_words_memo[start]
            results.append(result)

        return results

# @lc code=end

if __name__ == "__main__":
    words: List[str] = deserialize("List[str]", read_line())
    queries: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().vowelStrings(words, queries)
    print("\noutput:", serialize(ans, "integer[]"))
