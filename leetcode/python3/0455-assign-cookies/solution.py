# Created by Justin Park at 2026/07/09 19:26
# leetgo: 1.4.17
# https://leetcode.com/problems/assign-cookies/

from typing import List
from leetgo_py import deserialize, read_line, serialize

# @lc code=begin

class Solution:
    # Time Complexity: O(M log(M) + N log(N))
    # Space Complexity: O(M + N)
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        sorted_greeds, sorted_cookies = sorted(g), sorted(s)
        m, n = len(g), len(s)
        greed_index, cookie_index = 0, 0
        num_content_children = 0
        while greed_index < m and cookie_index < n:
            if sorted_cookies[cookie_index] >= sorted_greeds[greed_index]:
                num_content_children += 1
                greed_index += 1

            cookie_index += 1

        return num_content_children

# @lc code=end

if __name__ == "__main__":
    g: List[int] = deserialize("List[int]", read_line())
    s: List[int] = deserialize("List[int]", read_line())
    ans = Solution().findContentChildren(g, s)
    print("\noutput:", serialize(ans, "integer"))
