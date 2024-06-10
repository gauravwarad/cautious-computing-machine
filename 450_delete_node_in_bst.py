# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        key_pointer = root
        key_parent = root

        # handles empty root case
        if key_pointer is None:
            return root
        root_flag = False
        # case 0: root is key
        if root.val == key:
            root_flag = True

        while key_pointer is not None:
            if key_pointer.val == key:
                break
            elif key_pointer.val > key:
                key_parent = key_pointer
                key_pointer = key_pointer.left
            else:
                key_parent = key_pointer
                key_pointer = key_parent.right


        # handles key not found case
        if key_pointer is None:
            return root

        # case 1: key has no children
        if key_pointer.left is None and key_pointer.right is None:
            if root_flag:
                root = None
                return root
            if key_parent.left is not None and key_parent.left.val == key:
                key_parent.left = None
                return root
            elif key_parent.right is not None and key_parent.right.val == key:
                key_parent.right = None
                return root
            
        # case 2: key has one child
        if key_pointer.left != None and key_pointer.right == None:
            if root_flag:
                root = root.left
                return root
            if key_parent.left is not None and key_parent.left.val == key:
                key_parent.left = key_pointer.left
                return root
            elif key_parent.right is not None and key_parent.right.val == key:
                key_parent.right = key_pointer.left
                return root
        elif key_pointer.left == None and key_pointer.right != None:
            if root_flag:
                root = root.right
                return root
            if key_parent.left is not None and key_parent.left.val == key:
                key_parent.left = key_pointer.right
                return root
            elif key_parent.right is not None and key_parent.right.val == key:
                key_parent.right = key_pointer.right
                return root



        # the key is in pointer, parent in key parent
        # print(key_pointer.val)
        # print(key_parent.val)

        # case 3: the key has two children

        replacement = key_pointer.right
        replacement_parent = key_pointer
        while replacement.left is not None:
            replacement_parent = replacement
            replacement = replacement.left
        
        print("replacement values are - ")
        print(replacement_parent.val)
        print(replacement.val)

        # case 3a: replacement has no children
        if replacement.left is None and replacement.right is None:
            if replacement_parent.left is not None and replacement_parent.left == replacement:
                replacement_parent.left = None
            elif replacement_parent.right is not None and replacement_parent.right == replacement:
                replacement_parent.right = None
            if root_flag:
                replacement.left = key_pointer.left
                replacement.right = key_pointer.right
                root = replacement
                return root
            if key_parent.left is not None and key_parent.left.val == key:
                key_parent.left = replacement
                replacement.left = key_pointer.left
                replacement.right = key_pointer.right
                return root
            elif key_parent.right is not None and key_parent.right.val == key:
                key_parent.right = replacement
                replacement.left = key_pointer.left
                replacement.right = key_pointer.right
                return root

        # case 3b: replacement has 1 child
        if replacement.left is None and replacement.right is not None:
            if replacement_parent.left is not None and replacement_parent.left == replacement:
                replacement_parent.left = replacement.right
            elif replacement_parent.right is not None and replacement_parent.right == replacement:
                replacement_parent.right = replacement.right
            if root_flag:
                replacement.left = key_pointer.left
                replacement.right = key_pointer.right
                root = replacement
                return root
            if key_parent.left is not None and key_parent.left.val == key:
                key_parent.left = replacement
                replacement.left = key_pointer.left
                replacement.right = key_pointer.right
                return root
            elif key_parent.right is not None and key_parent.right.val == key:
                key_parent.right = replacement
                replacement.left = key_pointer.left
                replacement.right = key_pointer.right
                return root

        return root


    def deleteNode2(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # take2 - recursion

        # base case
        if not root:
            return root

        