# Created by Justin Park at 2026/06/08 16:31
# leetgo: 1.4.17
# https://leetcode.com/problems/graph-valid-tree/

from collections import defaultdict
from typing import List

from leetgo_py import deserialize, read_line, serialize

# @lc code=begin


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        graph: dict[int, set[int]] = defaultdict(set)

        for src, dst in edges:
            graph[src].add(dst)
            graph[dst].add(src)

        visited: set[int] = set()

        def _dfs(src) -> None:
            visited.add(src)
            for dst in graph[src]:
                if dst not in visited:
                    _dfs(dst)

        _dfs(0)

        return len(visited) == n


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    edges: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().validTree(n, edges)
    print("\noutput:", serialize(ans, "boolean"))
