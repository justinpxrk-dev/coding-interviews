#!/usr/bin/env python
# Created by Justin Park at 2026/10/13 22:30
# leetgo: 1.5.1
# https://leetcode.com/problems/word-break/

from leetgo_py import deserialize, read_line, serialize

# @lc code=begin


class Trie:
    class TrieNode:
        is_end_of_word: bool
        children: dict[str, "Trie.TrieNode"]

        def __init__(self) -> None:
            self.is_end_of_word = False
            self.children = {}

    head: TrieNode

    def __init__(self) -> None:
        self.head = self.TrieNode()

    def insert(self, word: str) -> None:
        curr = self.head
        for char in word:
            if char not in curr.children:
                curr.children[char] = self.TrieNode()
            curr = curr.children[char]

        curr.is_end_of_word = True


class Solution:
    # N = length of string, M = number of words, k = max word length
    # Time Complexity: O(kN + kM)
    # Auxiliary Space Complexity: O(N + kM)
    # Output Space Complexity: O(1)
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        n = len(s)
        dp: list[bool] = [False] * (n + 1)
        dp[0] = True

        trie: Trie = Trie()
        for word in wordDict:
            trie.insert(word)

        for i in range(n):
            if dp[i]:
                curr = trie.head
                j = i
                for j in range(i, n):
                    char = s[j]
                    if char not in curr.children:
                        break
                    curr = curr.children[char]
                    if curr.is_end_of_word:
                        dp[j + 1] = True

        return dp[-1]


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    wordDict: list[str] = deserialize("List[str]", read_line())
    ans = Solution().wordBreak(s, wordDict)
    print("\noutput:", serialize(ans, "boolean"))
