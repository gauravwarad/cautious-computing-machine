from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        return self.dfs(root, None, None)
        
    def dfs(self, root, mini, maxi):
        ans = True
        print("root, mini and maxi are - ", root.val, mini, maxi)

        if mini is not None:
            if root.val <= mini:
                return False
        if maxi is not None:
            if root.val >= maxi:
                return False
        if root.left:
            if root.val > root.left.val:

                ans = ans and self.dfs(root.left, mini, root.val)
            else:
                ans = False
                return ans

        if root.right:
            if root.val < root.right.val:
                ans = ans and self.dfs(root.right, root.val, maxi)
            else:
                ans = False
                return ans
                
        return ans
    
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
    result = solution.isValidBST(root)
    print(result)
