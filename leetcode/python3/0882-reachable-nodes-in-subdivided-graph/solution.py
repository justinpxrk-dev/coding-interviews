#!/usr/bin/env python
# Created by Justin Park at 2026/11/05 02:23
# leetgo: 1.5.2
# https://leetcode.com/problems/reachable-nodes-in-subdivided-graph/


from heapq import heappop, heappush
from math import inf

from leetgo_py import deserialize, read_line, serialize

# @lc code=begin


class Solution:
    # V = number of nodes, E = number of edges
    # Time Complexity: O(V + E log(V))
    # Space Complexity: O(V + E)
    def reachableNodes(self, edges: list[list[int]], maxMoves: int, n: int) -> int:
        # graph is an adjacency list which stores tuples of (dest, cnt, edge_id)
        graph: list[list[tuple[int, int, int]]] = [[] for _ in range(n)]
        uncounted_nodes: list[int] = []

        for edge_id, (src, dest, cnt) in enumerate(edges):
            graph[src].append((dest, cnt, edge_id))
            graph[dest].append((src, cnt, edge_id))
            uncounted_nodes.append(cnt)

        # min_heap stores tuples of (cnt, node)
        min_heap: list[tuple[int, int]] = []
        min_heap.append((0, 0))
        counts: list[int | float] = [inf] * n
        counts[0] = 0
        total_count = 0

        while min_heap:
            src_cnt, src = heappop(min_heap)

            if src_cnt != counts[src]:
                continue

            total_count += 1

            for dest, cnt, edge_id in graph[src]:
                new_cnt = src_cnt + cnt + 1

                if new_cnt < counts[dest]:
                    counts[dest] = new_cnt

                    if new_cnt <= maxMoves:
                        heappush(min_heap, (new_cnt, dest))

                uncounted = uncounted_nodes[edge_id]
                max_possible_moves = min(uncounted, maxMoves - src_cnt)
                total_count += max_possible_moves
                uncounted_nodes[edge_id] -= max_possible_moves

        return total_count


# @lc code=end

if __name__ == "__main__":
    edges: list[list[int]] = deserialize("List[List[int]]", read_line())
    maxMoves: int = deserialize("int", read_line())
    n: int = deserialize("int", read_line())
    ans = Solution().reachableNodes(edges, maxMoves, n)
    print("\noutput:", serialize(ans, "integer"))
