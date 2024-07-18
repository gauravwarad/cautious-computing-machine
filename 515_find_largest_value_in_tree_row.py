from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> list[int]:
        if root is None:
            return []
        
        queua = deque([root])
        op = []

        while len(queua) > 0:
            row_length = len(queua)
            maxi = queua[0].val

            for _ in range(0, row_length):
                current = queua.popleft()
                maxi = max(maxi, current.val)

                if current.left is not None:
                    queua.append(current.left)
                if current.right is not None:
                    queua.append(current.right)
            op.append(maxi)
        return op


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
    
    nodes = [1,3,2,5,3,None,9]
    root = build_tree(nodes)
    # Create an instance of Solution
    sol = Solution()
    
    # Call the hasPathSum method
    result = sol.largestValues(root)
    
    # Print the result
    print(result)