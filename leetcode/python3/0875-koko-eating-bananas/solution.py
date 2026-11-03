#!/usr/bin/env python
# Created by Justin Park at 2026/10/22 14:37
# leetgo: 1.5.1
# https://leetcode.com/problems/koko-eating-bananas/


from leetgo_py import deserialize, read_line, serialize

# @lc code=begin


class Solution:
    # N = number of piles, m = maximum value of piles
    # Time Complexity: O(N log(m))
    # Space Complexity: O(1)
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        left, right = 1, max(piles)

        while left < right:
            mid = (left + right) // 2
            hours = 0

            for num_bananas in piles:
                hours += (num_bananas + mid - 1) // mid

            if hours <= h:
                right = mid
            else:
                left = mid + 1

        return left


# @lc code=end

if __name__ == "__main__":
    piles: list[int] = deserialize("List[int]", read_line())
    h: int = deserialize("int", read_line())
    ans = Solution().minEatingSpeed(piles, h)
    print("\noutput:", serialize(ans, "integer"))
