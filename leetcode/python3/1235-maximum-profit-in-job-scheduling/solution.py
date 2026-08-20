#!/usr/bin/env python
# Created by Justin Park at 2026/08/05 03:36
# leetgo: 1.4.17
# https://leetcode.com/problems/maximum-profit-in-job-scheduling/


from bisect import bisect_left

from leetgo_py import deserialize, read_line, serialize

# @lc code=begin


class Solution:
    # N = number of jobs
    # Time Complexity: O(N log(N))
    # Space Complexity: O(N)
    def jobScheduling(
        self, startTime: list[int], endTime: list[int], profit: list[int]
    ) -> int:
        jobs = sorted(zip(startTime, endTime, profit))
        n = len(profit)
        dp: list[int] = [0 for _ in range(n)]
        dp[-1] = jobs[-1][2]
        for i in range(n - 2, -1, -1):
            _, end_time, job_profit = jobs[i]
            next_i = bisect_left(jobs, end_time, lo=i + 1, key=lambda job: job[0])
            dp[i] = max(
                dp[i + 1], job_profit + dp[next_i] if next_i < n else job_profit
            )

        return dp[0]


# @lc code=end

if __name__ == "__main__":
    startTime: list[int] = deserialize("List[int]", read_line())
    endTime: list[int] = deserialize("List[int]", read_line())
    profit: list[int] = deserialize("List[int]", read_line())
    ans = Solution().jobScheduling(startTime, endTime, profit)
    print("\noutput:", serialize(ans, "integer"))
