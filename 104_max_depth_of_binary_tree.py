# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        maxi = 0 # max depth in the current subtree
        depth = 0

        if root is None:
            return 0
        if root.left is not None:
            depth = 1 + self.maxDepth(root.left)
            if maxi < depth:
                maxi = depth
        if root.right is not None:
            depth = 1 + self.maxDepth(root.right)
            if maxi < depth:
                maxi = depth
        if root.left is None and root.right is None:
            depth = 1
            if maxi < depth:
                maxi = depth
        return maxi


