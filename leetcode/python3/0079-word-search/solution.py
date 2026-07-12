# Created by Justin Park at 2026/06/13 23:02
# leetgo: 1.4.17
# https://leetcode.com/problems/word-search/

from itertools import product
from typing import List

from leetgo_py import deserialize, read_line, serialize

# @lc code=begin


class Solution:
    M: int
    N: int
    L: int
    board: list[list[str]]
    word: str
    _directions: list[tuple[int, int]]

    # Time Complexity: O(MN * 3 ^ L)
    # Space Complexity: O(L)
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.M, self.N, self.L, self.board, self.word, self._directions = (
            len(board),
            len(board[0]),
            len(word),
            board,
            word,
            [(-1, 0), (0, 1), (1, 0), (0, -1)],
        )

        path: set[tuple[int, int]] = set()
        for coordinate in product(range(self.M), range(self.N)):
            if self._backtrack(coordinate, 0, path):
                return True

        return False

    def _backtrack(
        self, coordinate: tuple[int, int], word_index: int, path: set[tuple[int, int]]
    ) -> bool:
        if word_index == self.L:
            return True

        r, c = coordinate
        if (
            not 0 <= r < self.M
            or not 0 <= c < self.N
            or coordinate in path
            or self.board[r][c] != self.word[word_index]
        ):
            return False

        path.add(coordinate)

        for dr, dc in self._directions:
            nr, nc = r + dr, c + dc
            if self._backtrack((nr, nc), word_index + 1, path):
                return True

        path.remove(coordinate)

        return False


# @lc code=end

if __name__ == "__main__":
    board: List[List[str]] = deserialize("List[List[str]]", read_line())
    word: str = deserialize("str", read_line())
    ans = Solution().exist(board, word)
    print("\noutput:", serialize(ans, "boolean"))
