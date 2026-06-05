# Created by Justin Park at 2026/06/05 09:28
# leetgo: 1.4.17
# https://leetcode.com/problems/add-two-numbers/


from typing import Optional

from leetgo_py import ListNode, deserialize, read_line, serialize

# @lc code=begin


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        overflow = 0
        result_dummy_head = result_curr = ListNode()

        while l1 and l2:
            # Create new node for current value
            result_curr.next = ListNode()
            result_curr = result_curr.next

            # Calculate value and overflow
            val = l1.val + l2.val + overflow
            overflow = 1 if val >= 10 else 0
            val %= 10

            # Store value and iterate
            result_curr.val = val
            l1 = l1.next
            l2 = l2.next

        # Calculate sums for the remaining digits
        tail = l1 if l1 is not None else l2
        while tail:
            result_curr.next = ListNode()
            result_curr = result_curr.next

            val = tail.val + overflow
            overflow = 1 if val >= 10 else 0
            val %= 10

            result_curr.val = val
            tail = tail.next

        # Create digit for overflow
        if overflow > 0:
            result_curr.next = ListNode(1)

        return result_dummy_head.next


# @lc code=end

if __name__ == "__main__":
    l1: ListNode = deserialize("ListNode", read_line())
    l2: ListNode = deserialize("ListNode", read_line())
    ans = Solution().addTwoNumbers(l1, l2)
    print("\noutput:", serialize(ans, "ListNode"))
