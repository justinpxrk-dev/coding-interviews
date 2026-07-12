# Created by Justin Park at 2026/06/26 10:21
# leetgo: 1.4.17
# https://leetcode.com/problems/number-of-islands-ii/

from typing import List, Optional

from leetgo_py import deserialize, read_line, serialize

# @lc code=begin


class UnionFind:
    class Node:
        parent: "UnionFind.Node"
        rank: int

        def __init__(self, parent: Optional["UnionFind.Node"] = None, rank=1):
            self.parent = parent or self
            self.rank = rank

    m: int
    n: int
    nodes: dict[tuple[int, int], Node]
    num_islands: int
    _directions: list[tuple[int, int]]

    def __init__(self, m: int, n: int):
        self.m = m
        self.n = n
        self.nodes = {}
        self.num_islands = 0
        self._directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    def _find(self, node: Node) -> Node:
        # Root node
        if node == node.parent:
            return node

        node.parent = self._find(node.parent)
        return node.parent

    def _union(self, root_1: Node, root_2: Node) -> Node:
        if root_1.rank < root_2.rank:
            root_1.parent = root_2
            return root_2
        elif root_1.rank > root_2.rank:
            root_2.parent = root_1
            return root_1
        else:
            root_2.parent = root_1
            root_1.rank += 1
            return root_1

    def _in_bounds(self, position: tuple[int, int]) -> bool:
        r, c = position
        return 0 <= r and r < self.m and 0 <= c and c < self.n

    def add_land(self, position: list[int]) -> None:
        r, c = position

        if (r, c) in self.nodes:
            return

        self.nodes[(r, c)] = node = self.Node()
        self.num_islands += 1

        for dr, dc in self._directions:
            nr, nc = r + dr, c + dc

            if self._in_bounds((nr, nc)) and (nr, nc) in self.nodes:
                root = self._find(node)
                neighbor_root = self._find(self.nodes[(nr, nc)])

                if root != neighbor_root:
                    self.nodes[(r, c)] = self._union(root, neighbor_root)
                    self.num_islands -= 1

    def get_num_islands(self) -> int:
        return self.num_islands


class Solution:
    # Time Complexity: O(P α(P))
    # Space Complexity: O(P)
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        union_find = UnionFind(m, n)
        num_islands_list: list[int] = []
        for position in positions:
            union_find.add_land(position)
            num_islands_list.append(union_find.get_num_islands())

        return num_islands_list


# @lc code=end

if __name__ == "__main__":
    m: int = deserialize("int", read_line())
    n: int = deserialize("int", read_line())
    positions: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().numIslands2(m, n, positions)
    print("\noutput:", serialize(ans, "integer[]"))
