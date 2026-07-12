# Created by Justin Park at 2026/06/19 02:08
# leetgo: 1.4.17
# https://leetcode.com/problems/find-k-closest-elements/

from typing import List

from leetgo_py import deserialize, read_line, serialize

# @lc code=begin


class Solution:
    # Time Complexity: O(k + log(n - k))
    # Space Complexity: O(1)
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        left, right = 0, n - k
        while left < right:
            mid = (left + right) // 2

            if x - arr[mid] <= arr[mid + k] - x:
                right = mid
            else:
                left = mid + 1

        return arr[left : left + k]


# @lc code=end

if __name__ == "__main__":
    arr: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    x: int = deserialize("int", read_line())
    ans = Solution().findClosestElements(arr, k, x)
    print("\noutput:", serialize(ans, "integer[]"))
