#!/usr/bin/env python
# Created by Justin Park at 2026/10/28 14:10
# leetgo: 1.5.2
# https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

from leetgo_py import deserialize, read_line, serialize

# @lc code=begin


class Solution:
    # N = length of weights, S = sum(weights) - max(weights) + 1
    # Time Complexity: O(N log(S))
    # Space Complexity: O(1)
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)

        while left < right:
            weight_limit = (left + right) // 2

            num_days = 1
            curr_weight = 0
            for weight in weights:
                if curr_weight + weight > weight_limit:
                    num_days += 1
                    curr_weight = weight
                else:
                    curr_weight += weight

                if num_days > days:
                    break

            if num_days <= days:
                right = weight_limit
            else:
                left = weight_limit + 1

        return left


# @lc code=end

if __name__ == "__main__":
    weights: list[int] = deserialize("List[int]", read_line())
    days: int = deserialize("int", read_line())
    ans = Solution().shipWithinDays(weights, days)
    print("\noutput:", serialize(ans, "integer"))
