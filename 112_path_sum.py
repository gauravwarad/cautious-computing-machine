from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        if root.left is None and root.right is None and root.val == targetSum:
            return True
        if root.left:
            if self.hasPathSum(root.left, targetSum - root.val):
                return True
        if root.right:
            if self.hasPathSum(root.right, targetSum - root.val):
                return True
        return False

# Helper function to build a binary tree from a list
def build_tree(nodes):
    if not nodes:
        return None
    
    def inner(index):
        if index < len(nodes) and nodes[index] is not None:
            node = TreeNode(nodes[index])
            node.left = inner(2 * index + 1)
            node.right = inner(2 * index + 2)
            return node
        return None
    
    return inner(0)

# Example usage:
if __name__ == "__main__":
    # Example binary tree and target sum
    # nodes = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, None, 5, 1]
    # targetSum = 22
    nodes = [1,2,3]
    targetSum = 5
    # Build the tree
    root = build_tree(nodes)
    
    # Create an instance of Solution
    sol = Solution()
    
    # Call the hasPathSum method
    result = sol.hasPathSum(root, targetSum)
    
    # Print the result
    print("Has path sum:", result)
