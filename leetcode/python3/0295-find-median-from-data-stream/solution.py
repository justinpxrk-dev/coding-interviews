# Created by Justin Park at 2026/07/07 20:13
# leetgo: 1.4.17
# https://leetcode.com/problems/find-median-from-data-stream/

import heapq
from typing import List

from leetgo_py import deserialize, join_array, read_line, serialize, split_array

# @lc code=begin


# Time Complexity: O(N log(N))
# Space Complexity: O(N)
class MedianFinder:
    left_heap: list[int]
    right_heap: list[int]

    def __init__(self):
        self.left_heap = []
        self.right_heap = []

    # E = number of elements
    # Time Complexity: O(log(N))
    # Space Complexity: O(1)
    def addNum(self, num: int) -> None:
        heapq.heappush_max(self.left_heap, num)
        heapq.heappush(self.right_heap, heapq.heappop_max(self.left_heap))
        if len(self.right_heap) > len(self.left_heap):
            heapq.heappush_max(self.left_heap, heapq.heappop(self.right_heap))

    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def findMedian(self) -> float:
        num_elements = len(self.left_heap) + len(self.right_heap)

        if num_elements % 2 == 0:
            return (self.left_heap[0] + self.right_heap[0]) / 2
        else:
            return self.left_heap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

# @lc code=end

if __name__ == "__main__":
    ops: List[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    obj = MedianFinder()

    for i in range(1, len(ops)):
        match ops[i]:
            case "addNum":
                method_params = split_array(params[i])
                num: int = deserialize("int", method_params[0])
                obj.addNum(num)
                output.append("null")
            case "findMedian":
                ans = serialize(obj.findMedian())
                output.append(ans)

    print("\noutput:", join_array(output))
