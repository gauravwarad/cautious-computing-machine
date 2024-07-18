from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if root is None:
            return 0
        sum = 0
        if root.val >= low and root.val <= high:
            sum += root.val
            print("value is - ", root.val)
            sum += self.rangeSumBST(root.left, low, high)
            sum += self.rangeSumBST(root.right, low, high)
        else:
            if root.val > high: # skip the right part
                sum += self.rangeSumBST(root.left, low, high)
            
            if root.val < low: # skip left
                sum += self.rangeSumBST(root.right, low, high)

        return sum



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
    
    nodes = [10,5,15,3,7,None,18]
    root = build_tree(nodes)
    # Create an instance of Solution
    sol = Solution()
    
    # Call the hasPathSum method
    result = sol.rangeSumBST(root, 7, 15)
    
    # Print the result
    print(result)