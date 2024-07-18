from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor2(self, root, p, q):
        if root is None:
            return None
        
        if root.val == p or root.val == q:
            return root
        
        left = self.lowestCommonAncestor2(root.left, p, q)
        right = self.lowestCommonAncestor2(root.right, p, q)

        if left and right:
            return root
        
        if left:
            return left
        
        return right


    def lowestCommonAncestor(self, root: 'TreeNode', p, q) -> 'TreeNode':
        val, ans = self.find_common_ancestor(root, p, q)
        if ans is None:
            print("it's None?")
            return root
        return ans
    
    def find_common_ancestor(self, root, p, q):
        # base case - it finds p or q/ it is a leaf node/ p and q both are found
        found = 0
        if root is None:
            return 0, None

        if root.val == p or root.val == q:
            found += 1
        
        lfound, lwhere = self.find_common_ancestor(root.left, p, q)
        rfound, rwhere = self.find_common_ancestor(root.right, p, q)
        if lfound == 2:
            return 2, lwhere
        if rfound == 2:
            return 2, rwhere

        if found + lfound + rfound > 0:
            return found + lfound + rfound, root
        else:
            return found, None

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
    nodes = [3,5,1,6,2,0,8,None,None,7,4]
    root = build_tree(nodes)
    # Create an instance of Solution
    sol = Solution()
    
    # Call the hasPathSum method
    result = sol.lowestCommonAncestor2(root, 4, 7)
    
    # Print the result
    print(result.val)
