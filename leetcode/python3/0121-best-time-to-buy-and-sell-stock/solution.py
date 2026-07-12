# Created by Justin Park at 2026/07/09 03:53
# leetgo: 1.4.17
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

from typing import List
from leetgo_py import deserialize, read_line, serialize

# @lc code=begin

class Solution:
    # Time Complexity: O(N)
    # Space Complexity: O(1)
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = float('inf')

        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price

        return int(max_profit)


# @lc code=end

if __name__ == "__main__":
    prices: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maxProfit(prices)
    print("\noutput:", serialize(ans, "integer"))
