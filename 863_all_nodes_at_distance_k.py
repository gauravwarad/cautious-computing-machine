from typing import Optional
from collections import deque, defaultdict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> list[int]:
        def dfs(node, parent):
            if node is None:
                return
            node.parent = parent
            dfs(node.left, node)
            dfs(node.right, node)
            return
        dfs(root, None)

        queua = deque()
        seen = set()
        queua.append(target)
        seen.add(target)

        dist = 0
        while len(queua) > 0 and dist < k:
            current = queua.popleft()
            current_len = len(queua)
            for _ in range(current_len):
                if current.left and current.left not in seen:
                    queua.append(current.left)
                    seen.add(current.left)
                if current.right is not None and current.right not in seen:
                    queua.append(current.right)
                    seen.add(current.right)
                if current.parent is not None and current.parent not in seen:
                    queua.append(current.parent)
                    seen.add(current.parent)
            dist += 1
        return [node.val for node in queua]




    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> list[int]:
        
        edges = defaultdict(set)
        queua = deque()
        queua.append(root)
        while len(queua) > 0:
            current = queua.popleft()
            if current.left:
                queua.append(current.left)
                edges[current.val].add(current.left.val)
                edges[current.left.val].add(current.val)
            if current.right:
                queua.append(current.right)
                edges[current.val].add(current.right.val)
                edges[current.right.val].add(current.val)

        print(edges)
        visited = set()
        queua.append((target, 0))
        visited.add(target)
        op = []
        while len(queua) > 0:
            node, dist = queua.popleft()
            print(node, dist)
            if dist == k:
                op.append(node)
            for nei in edges[node]:
                if nei not in visited:
                    queua.append((nei, dist+1))
                    visited.add(nei)
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
    nodes = [3,5,1,6,2,0,8,None,None,7,4]
    root = build_tree(nodes)
    # Create an instance of Solution
    sol = Solution()
    
    # Call the hasPathSum method
    result = sol.distanceK(root,5,2)
    
    # Print the result
    print(result)
