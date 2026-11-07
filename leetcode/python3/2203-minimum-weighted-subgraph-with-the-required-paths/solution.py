#!/usr/bin/env python
# Created by Justin Park at 2026/11/04 21:20
# leetgo: 1.5.2
# https://leetcode.com/problems/minimum-weighted-subgraph-with-the-required-paths/

from heapq import heappop, heappush
from math import inf

from leetgo_py import deserialize, read_line, serialize

# @lc code=begin


class Solution:
    # V = number of nodes, E = number of edges
    # Time Complexity: O(V + E log(E))
    # Space Complexity: O(V + E)
    def minimumWeight(
        self, n: int, edges: list[list[int]], src1: int, src2: int, dest: int
    ) -> int:
        graph: list[list[tuple[int, int]]] = [[] for _ in range(n)]
        reverse_graph: list[list[tuple[int, int]]] = [[] for _ in range(n)]
        for src_node, dst_node, curr_weight in edges:
            graph[src_node].append((dst_node, curr_weight))
            reverse_graph[dst_node].append((src_node, curr_weight))

        src1_distances: list[int | float] = self._dijkstras(graph, n, src1)
        src2_distances: list[int | float] = self._dijkstras(graph, n, src2)
        dest_distances: list[int | float] = self._dijkstras(reverse_graph, n, dest)

        min_weight = inf
        for src1_distance, src2_distance, dest_distance in zip(
            src1_distances, src2_distances, dest_distances
        ):
            min_weight = min(min_weight, src1_distance + src2_distance + dest_distance)

        return int(min_weight) if min_weight != inf else -1

    def _dijkstras(
        self, graph: list[list[tuple[int, int]]], n: int, src: int
    ) -> list[int | float]:
        # min_heap stores tuples (weight, node)
        min_heap: list[tuple[int, int]] = []
        min_heap.append((0, src))
        distances: list[int | float] = [inf] * n
        distances[src] = 0

        while min_heap:
            src_weight, src = heappop(min_heap)

            if src_weight != distances[src]:
                continue

            for dest, dest_weight in graph[src]:
                new_weight = src_weight + dest_weight

                if new_weight < distances[dest]:
                    distances[dest] = new_weight
                    heappush(min_heap, (new_weight, dest))

        return distances


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    edges: list[list[int]] = deserialize("List[List[int]]", read_line())
    src1: int = deserialize("int", read_line())
    src2: int = deserialize("int", read_line())
    dest: int = deserialize("int", read_line())
    ans = Solution().minimumWeight(n, edges, src1, src2, dest)
    print("\noutput:", serialize(ans, "long"))
