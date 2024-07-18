from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        maxi, mini, diff = self.dfs(root)
        return diff

    def dfs(self, root):
        print("dfs in root - ", root.val)
        if root is None:
            return None, None, 0
        
        maxi, lmaxi, rmaxi = root.val, root.val, root.val
        mini, lmini, rmini = root.val, root.val, root.val
        diff, ldiff, rdiff = 0, 0, 0

        if root.left is None and root.right is None: # leaf node
            print("leaf node reached, ", root.val)
            return maxi, mini, diff
        
        if root.left is not None:
            lmaxi, lmini, ldiff = self.dfs(root.left)
            print("went to the root.left, got lmaxi, lmini and ldiff as - ", lmaxi, lmini, ldiff)
            ldiff = max(ldiff, abs(lmaxi - root.val), abs(lmini - root.val))
            lmaxi = max(lmaxi, root.val)
            lmini = min(lmini, root.val)
            print("and after comparing with the root, lmaxi, lmini, ldiff were - ",root.val, lmaxi, lmini, ldiff)

        if root.right is not None:
            rmaxi, rmini, rdiff = self.dfs(root.right)
            print("went to the root.right, got rmaxi, rmini and rdiff as - ", rmaxi, rmini, rdiff)
            rdiff = max(rdiff, abs(rmaxi - root.val), abs(rmini - root.val))
            rmaxi = max(rmaxi, root.val)
            rmini = min(rmini, root.val)
            print("and after comparing with the root, rmaxi, rmini, rdiff were - ",root.val, rmaxi, rmini, rdiff)

        print("end of function for root.val -> final max, min and diff values are - ", root.val, max(lmaxi, rmaxi), min(lmini, rmini), max(ldiff, rdiff))
        return max(lmaxi, rmaxi), min(lmini, rmini), max(ldiff, rdiff)


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
    nodes = [8,3,10,1,6,None,14,None,None,4,7,13]
    root = build_tree(nodes)
    # Create an instance of Solution
    sol = Solution()
    
    # Call the hasPathSum method
    result = sol.maxAncestorDiff(root)
    
    # Print the result
    print(result)
