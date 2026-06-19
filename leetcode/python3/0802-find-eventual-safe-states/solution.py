# Created by Justin Park at 2026/06/16 19:54
# leetgo: 1.4.17
# https://leetcode.com/problems/find-eventual-safe-states/

from typing import List

from leetgo_py import deserialize, read_line, serialize

# @lc code=begin


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        reversed_graph: list[list[int]] = [[] for _ in range(n)]
        outdegrees: list[int] = [0] * n

        for node, neighbors in enumerate(graph):
            for neighbor in neighbors:
                reversed_graph[neighbor].append(node)
                outdegrees[node] += 1

        stack: list[int] = [
            node for node, outdegree in enumerate(outdegrees) if outdegree == 0
        ]
        is_safe: list[bool] = [False] * n

        while stack:
            node = stack.pop()
            is_safe[node] = True

            for neighbor in reversed_graph[node]:
                outdegrees[neighbor] -= 1
                if outdegrees[neighbor] == 0:
                    stack.append(neighbor)

        return [node for node in range(n) if is_safe[node]]


# @lc code=end

if __name__ == "__main__":
    graph: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().eventualSafeNodes(graph)
    print("\noutput:", serialize(ans, "integer[]"))
