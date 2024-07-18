from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        if root is None:
            return None
        
        queua = deque([root])

        op = []
        zig = True
        while len(queua) > 0:

            row_length = len(queua)
            row = []
            stacku = []
            for _ in range(0, row_length):
                current = queua.popleft()
                if zig:
                    row.append(current.val)
                else:
                    stacku.append(current.val)
                if current.left is not None:
                    queua.append(current.left)
                if current.right is not None:
                    queua.append(current.right)
            if zig:
                zig = False
            else:
                row = []
                while len(stacku) > 0:
                    row.append(stacku.pop())
                zig = True
            
            # print("end of while, row is - ", row)
            op.append(row)
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
    
    nodes = [3,9,20,None,None,15,7]
    root = build_tree(nodes)
    # Create an instance of Solution
    sol = Solution()
    
    # Call the hasPathSum method
    result = sol.zigzagLevelOrder(root)
    
    # Print the result
    print(result)