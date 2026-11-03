#!/usr/bin/env python
# Created by Justin Park at 2026/10/15 00:33
# leetgo: 1.5.1
# https://leetcode.com/problems/maximum-profit-in-job-scheduling/

from heapq import heappop_max, heappush_max

from leetgo_py import deserialize, read_line, serialize

# @lc code=begin


class Solution:
    # N = number of jobs
    # Time Complexity: O(N log(N))
    # Auxiliary Space Complexity: O(N)
    # Output Space Complexity: O(1)
    def jobScheduling(
        self, startTime: list[int], endTime: list[int], profit: list[int]
    ) -> int:
        n = len(startTime)
        sorted_job_indices: list[int] = sorted(
            range(n), key=lambda job_index: -endTime[job_index]
        )
        # Max-heap storing tuples of start time and best total profit for that
        # start time
        max_heap: list[tuple[int, int]] = []
        max_profit = 0

        for job_index in sorted_job_indices:
            while max_heap and endTime[job_index] <= max_heap[0][0]:
                max_profit = max(max_profit, heappop_max(max_heap)[1])

            heappush_max(
                max_heap, (startTime[job_index], profit[job_index] + max_profit)
            )

        for _, total_profit in max_heap:
            max_profit = max(max_profit, total_profit)

        return max_profit


# @lc code=end

if __name__ == "__main__":
    startTime: list[int] = deserialize("List[int]", read_line())
    endTime: list[int] = deserialize("List[int]", read_line())
    profit: list[int] = deserialize("List[int]", read_line())
    ans = Solution().jobScheduling(startTime, endTime, profit)
    print("\noutput:", serialize(ans, "integer"))
