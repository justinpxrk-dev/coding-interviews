#!/usr/bin/env python
# Created by Justin Park at 2026/11/04 16:39
# leetgo: 1.5.2
# https://leetcode.com/problems/network-delay-time/

from heapq import heappop, heappush
from math import inf

from leetgo_py import deserialize, read_line, serialize

# @lc code=begin


class Solution:
    # V = number of nodes, E = number of edges
    # Time Complexity: O(V + E log(V))
    # Space Complexity: O(V + E)
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        graph: list[list[tuple[int, int]]] = [[] for _ in range(n)]

        for src_node, dst_node, distance in times:
            graph[src_node - 1].append((dst_node - 1, distance))

        distances: list[int | float] = [inf] * n
        min_heap: list[tuple[int, int]] = []

        distances[k - 1] = 0
        heappush(min_heap, (0, k - 1))
        while min_heap:
            min_time, src_node = heappop(min_heap)

            if min_time != distances[src_node]:
                continue

            for dst_node, distance in graph[src_node]:
                new_distance = min_time + distance
                if new_distance < distances[dst_node]:
                    distances[dst_node] = new_distance
                    heappush(min_heap, (new_distance, dst_node))

        min_time = max(distances)
        return int(min_time) if min_time != inf else -1


# @lc code=end

if __name__ == "__main__":
    times: list[list[int]] = deserialize("List[List[int]]", read_line())
    n: int = deserialize("int", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().networkDelayTime(times, n, k)
    print("\noutput:", serialize(ans, "integer"))
