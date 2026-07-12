# Created by Justin Park at 2026/06/27 10:00
# leetgo: 1.4.17
# https://leetcode.com/problems/merge-k-sorted-lists/

from heapq import heapify, heappop, heappush
from typing import List, Optional, cast

from leetgo_py import ListNode, deserialize, read_line, serialize

# @lc code=begin


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class HeapNode:
    node: ListNode

    def __init__(self, node: ListNode) -> None:
        self.node = node

    def __lt__(self, other: "HeapNode") -> bool:
        return self.node.val < other.node.val


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap: list[HeapNode] = [HeapNode(node) for node in lists if node]
        if not min_heap:
            return None

        heapify(min_heap)
        merged_list_dummy = curr = ListNode()
        while min_heap:
            node = heappop(min_heap).node
            curr.next = node
            curr = curr.next

            if node.next:
                node = node.next
                heappush(min_heap, HeapNode(node))

        return merged_list_dummy.next


# @lc code=end

if __name__ == "__main__":
    lists: List[Optional[ListNode]] = deserialize("List[ListNode]", read_line())
    ans = Solution().mergeKLists(lists)
    print("\noutput:", serialize(ans, "ListNode"))
