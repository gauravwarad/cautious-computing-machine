from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        if root.left is None:
            return 1 + self.minDepth(root.right)
        
        if root.right is None:
            return 1 + self.minDepth(root.left)

        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
        
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
    # p = [1,2,1]
    # q = [1,1, 2]
    # targetSum = 5
    # Build the tree
    # root1 = build_tree(p)
    nodes = [3,9,20,None,None,15,7]
    root = build_tree(nodes)
    # Create an instance of Solution
    sol = Solution()
    
    # Call the hasPathSum method
    result = sol.minDepth(root)
    
    # Print the result
    print(result)
