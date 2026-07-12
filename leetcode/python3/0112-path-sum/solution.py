# Created by Justin Park at 2026/07/07 19:33
# leetgo: 1.4.17
# https://leetcode.com/problems/path-sum/

from typing import Optional

from leetgo_py import TreeNode, deserialize, read_line, serialize

# @lc code=begin


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Time Complexity: O(N)
    # Space Complexity: O(N)
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False

        targetSum -= root.val
        if root.left is None and root.right is None:
            return targetSum == 0

        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(
            root.right, targetSum
        )


# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    targetSum: int = deserialize("int", read_line())
    ans = Solution().hasPathSum(root, targetSum)
    print("\noutput:", serialize(ans, "boolean"))
