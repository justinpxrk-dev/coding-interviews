# Created by Justin Park at 2026/07/09 20:18
# leetgo: 1.4.17
# https://leetcode.com/problems/gas-station/

from typing import List
from leetgo_py import deserialize, read_line, serialize

# @lc code=begin

class Solution:
    # Time Complexity: O(N)
    # Space Complexity: O(1)
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        net_gas, curr_gas, starting_station = 0, 0, 0

        for i in range(len(gas)):
            net_gas += gas[i] - cost[i]
            curr_gas += gas[i] - cost[i]

            if curr_gas < 0:
                curr_gas = 0
                starting_station = i + 1

        return -1 if net_gas < 0 else starting_station

# @lc code=end

if __name__ == "__main__":
    gas: List[int] = deserialize("List[int]", read_line())
    cost: List[int] = deserialize("List[int]", read_line())
    ans = Solution().canCompleteCircuit(gas, cost)
    print("\noutput:", serialize(ans, "integer"))
