# Created by Justin Park at 2026/06/08 17:38
# leetgo: 1.4.17
# https://leetcode.com/problems/bus-routes/

from collections import defaultdict, deque
from typing import List

from leetgo_py import deserialize, read_line, serialize

# @lc code=begin


class Solution:
    def numBusesToDestination(
        self, routes: List[List[int]], source: int, target: int
    ) -> int:
        # Edge case: bus starts at target, no buses boarded.
        if source == target:
            return 0

        # Create mapping of bus stop -> routes.
        stop_routes: dict[int, set[int]] = defaultdict(set)
        for route_num, route in enumerate(routes):
            for stop in route:
                stop_routes[stop].add(route_num)

        # Edge case: source or target do not exist in mapping.
        if source not in stop_routes or target not in stop_routes:
            return -1

        # Use queue for BFS. Track visited stops, routes as well as number of
        # buses boarded.
        curr_routes, target_routes = (
            deque(stop_routes[source]),
            stop_routes[target],
        )
        visited_stops, visited_routes = {source}, set(curr_routes)
        buses_boarded = 1

        while curr_routes:
            # Traverse each route at the current BFS depth.
            for _ in range(len(curr_routes)):
                curr_route_num = curr_routes.popleft()

                # Return if current route is shared with target bus stop.
                if curr_route_num in target_routes:
                    return buses_boarded

                # Traverse each unvisited bus stop in the current route.
                for stop in routes[curr_route_num]:
                    if stop not in visited_stops:
                        visited_stops.add(stop)
                        # Add all unvisited routes for current bus stop to BFS
                        # queue.
                        for route in stop_routes[stop]:
                            if route not in visited_routes:
                                visited_routes.add(route)
                                curr_routes.append(route)

            # Increment BFS depth
            buses_boarded += 1

        # No path from source to target found.
        return -1


# @lc code=end

if __name__ == "__main__":
    routes: List[List[int]] = deserialize("List[List[int]]", read_line())
    source: int = deserialize("int", read_line())
    target: int = deserialize("int", read_line())
    ans = Solution().numBusesToDestination(routes, source, target)
    print("\noutput:", serialize(ans, "integer"))
