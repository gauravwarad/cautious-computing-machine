from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        # works on leetcode -- not here :(
        if root is None:
            return None
        
        queua = deque([root])
        # sum = 0
        while len(queua) > 0:

            row_length = len(queua)
            sum = 0
            print("row starting in - ", queua[0].val, row_length)
            for _ in range(0, row_length):
                
                current = queua.popleft()
                sum += current.val
                print("current node - ", current.val)
                if current.left is not None:
                    queua.append(current.left)
                if current.right is not None:
                    print("current.right - ", current.right.val)
                    queua.append(current.right)
            print("last row sum is - ", sum)
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
    
    nodes = [1,2,3,4,5,None,6,7,None,None,None,None,8]
    root = build_tree(nodes)
    # Create an instance of Solution
    sol = Solution()
    
    # Call the hasPathSum method
    result = sol.deepestLeavesSum(root)
    
    # Print the result
    print(result)