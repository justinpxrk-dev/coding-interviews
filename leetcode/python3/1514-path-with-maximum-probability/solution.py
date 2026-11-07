#!/usr/bin/env python
# Created by Justin Park at 2026/11/06 01:27
# leetgo: 1.5.2
# https://leetcode.com/problems/path-with-maximum-probability/

from heapq import heappop_max, heappush_max

from leetgo_py import deserialize, read_line, serialize

# @lc code=begin


class Solution:
    # V = number of nodes, E = number of edges
    # Time Complexity: O(V + E log(V))
    # Space Complexity: O(V + E)
    def maxProbability(
        self,
        n: int,
        edges: list[list[int]],
        succProb: list[float],
        start_node: int,
        end_node: int,
    ) -> float:
        # graph is an adjacency list representing edges for each node with
        # tuples (node, probability)
        graph: list[list[tuple[int, float]]] = [[] for _ in range(n)]

        for (src, dest), probability in zip(edges, succProb):
            graph[src].append((dest, probability))
            graph[dest].append((src, probability))

        max_heap: list[tuple[float, int]] = []
        max_heap.append((1.0, start_node))
        probabilities: list[float] = [0] * n
        probabilities[start_node] = 1

        while max_heap:
            src_probability, src = heappop_max(max_heap)

            if src == end_node:
                return src_probability

            if src_probability != probabilities[src]:
                continue

            for dest, dest_probability in graph[src]:
                new_probability = src_probability * dest_probability

                if new_probability > probabilities[dest]:
                    probabilities[dest] = new_probability
                    heappush_max(max_heap, (new_probability, dest))

        return 0


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    edges: list[list[int]] = deserialize("List[List[int]]", read_line())
    succProb: list[float] = deserialize("List[float]", read_line())
    start_node: int = deserialize("int", read_line())
    end_node: int = deserialize("int", read_line())
    ans = Solution().maxProbability(n, edges, succProb, start_node, end_node)
    print("\noutput:", serialize(ans, "double"))
