# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
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