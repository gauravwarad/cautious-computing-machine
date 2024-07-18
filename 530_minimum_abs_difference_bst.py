from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root):
            if root is None:
                return
            
            dfs(root.left)
            # print(root.val)
            seq.append(root.val)
            dfs(root.right)

            return None
        
        seq = []
        dfs(root)
        mini = 10**5 + 1

        for i in range(0, len(seq) - 1):
            print(seq[i])
            print(seq[i+1])
            mini = min(mini, abs(seq[i] - seq[i+1]))
            print("mini is - ", mini)
        return mini

    

    

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
    
    nodes = [1,None,5,3]
    root = build_tree(nodes)
    # Create an instance of Solution
    sol = Solution()
    
    # Call the hasPathSum method
    result = sol.getMinimumDifference(root)
    
    # Print the result
    print(result)