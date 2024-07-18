from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        # if the child is smaller than root - go there but don't count it
        if root is None:
            return 0
        
        return 1 + self.find_good_nodes(root, root.val)
        
    
    def find_good_nodes(self, root: TreeNode, maxi):
        print("the start of funtion, root.val, {} maxi is{}",root.val, maxi)
        if root is None:
            return 0
        goodnodes = 0
        if root.left is not None:
            if root.left.val >= maxi:
                goodnodes += 1 + self.find_good_nodes(root.left, max(maxi, root.left.val))
            else:
                goodnodes += self.find_good_nodes(root.left, maxi)

        if root.right is not None:
            if root.right.val >= maxi:
                goodnodes += 1 + self.find_good_nodes(root.right, max(maxi, root.right.val))
            else:
                goodnodes += self.find_good_nodes(root.right, maxi)
        print("on node {}, goodnodes are {}", root.val, goodnodes)
        return goodnodes


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
    nodes = [3,1,4,2,None,1,5]
    # targetSum = 5
    # Build the tree
    root = build_tree(nodes)
    
    # Create an instance of Solution
    sol = Solution()
    
    # Call the hasPathSum method
    result = sol.goodNodes(root)
    
    # Print the result
    print(result)
