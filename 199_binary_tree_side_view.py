from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> list[int]:
        # vals_queue has no effect on the logic, it's only for debugging
           
        queua = []
        vals_queue = []
        op = []

        if root is None:
            return []
        
        queua.append(root)
        vals_queue.append(root.val)
        queua.append("*")
        vals_queue.append("*")
        
        while len(queua) > 0:
            
            current = queua.pop(0)
            vals_queue.pop(0)
            if current == "*":
                break
            if current.left is not None:
                queua.append(current.left)
                vals_queue.append(current.left.val)
            if current.right is not None:
                queua.append(current.right)
                vals_queue.append(current.right.val)
            if len(queua) > 1:
                if queua[0] == "*":
                    op.append(current.val)
                    queua.pop(0)
                    queua.append("*")
                    vals_queue.pop(0)
                    vals_queue.append("*")
                
            print(op)
        return op

    def rightSideView2(self, root: Optional[TreeNode]) -> list[int]:

        queua = deque([root])
        op = []

        while len(queua) > 0:
            current = len(queua)

            for _ in range(0,current):
                last = queua.popleft()

                if last.left is not None:
                    queua.append(last.left)
                if last.right is not None:
                    queua.append(last.right)

            op.append(last.val)
        
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
    # Example binary tree and target sum
    # nodes = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, None, 5, 1]
    # targetSum = 22
    # p = [1,2,1]
    # q = [1,1, 2]
    # targetSum = 5
    # Build the tree
    # root1 = build_tree(p)
    nodes = [1,2,3,None,5,None,4]
    root = build_tree(nodes)
    # Create an instance of Solution
    sol = Solution()
    
    # Call the hasPathSum method
    result = sol.rightSideView2(root)
    
    # Print the result
    print(result)