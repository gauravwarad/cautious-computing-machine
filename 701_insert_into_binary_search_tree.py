from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if val > root.val:
            if root.right is not None:
                root.right = self.insertIntoBST(root.right, val)
            else:
                node = TreeNode(val, None, None)
                root.right = node
                return root
        elif val < root.val:
            if root.left is not None:
                root.left = self.insertIntoBST(root.left, val)
            else:
                node = TreeNode(val, None, None)
                root.left = node
                return root
        return root
    
# Helper function to create a binary tree from a list of values.
def create_binary_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    if not values:
        return None
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while i < len(values):
        current = queue.pop(0)
        if values[i] is not None:
            current.left = TreeNode(values[i])
            queue.append(current.left)
        i += 1
        if i < len(values) and values[i] is not None:
            current.right = TreeNode(values[i])
            queue.append(current.right)
        i += 1
    return root

# Example usage:
if __name__ == "__main__":
    # Create a binary tree from a list.
    values = [5,4,6,None,None,3,7]
    root = create_binary_tree(values)
    
    # Instantiate the solution and test the method.
    solution = Solution()
    result = solution.insertIntoBST(root)
    print(result)
