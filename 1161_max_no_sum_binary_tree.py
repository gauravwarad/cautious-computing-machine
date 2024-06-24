# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:

        queua = []
        # sums = []
        max_sum = None
        indexi = 0
        max_index = 1

        if root is None:
            return 0

        queua.append(root)

        while len(queua) > 0:
            indexi += 1
            level_len = len(queua)
            sum = 0
            for i in range(0, level_len):
                current = queua.pop(0)
                if current.left is not None:
                    queua.append(current.left)
                if current.right is not None:
                    queua.append(current.right)
                sum += current.val
            if not max_sum:
                max_sum = sum
                max_index = indexi
            if sum > max_sum:
                max_sum = sum
                max_index = indexi
            # sums.append(sum)
            # print(sums)
        # maxi = sums[0]
        # op = 1
        # for i in range(0, len(sums)):
        #     if sums[i] > maxi:
        #         maxi = sums[i]
        #         op = i + 1
        # print(maxi)
        return max_index
