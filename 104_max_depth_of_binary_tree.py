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
    
    def maxDepth2(self, root: Optional[TreeNode]) -> int:
        
        if root is None:
            return 0
        
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


    def maxDepth3(self, root):
        # iterative.
        if root is None:
            return 0
        stacku = []
        stacku.append(root)
        depth = 1
        maxdepth = 1

        while stacku:
            node, depth = stacku.pop()
            stacku.append([node.left, depth + 1])
            stacku.append([node.right, depth + 1])

            maxdepth = max(depth, maxdepth)
        

