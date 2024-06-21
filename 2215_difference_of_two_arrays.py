class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        
        set1 = set(nums1)
        set2 = set(nums2)

        # print(type(set1))
        # print(set2)
        op1 = list(set1.difference(set2))
        op2 = list(set2.difference(set1))
        return [op1, op2]

    def findDifference2(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        
        # using hashmaps aka dictionary
        
        dict1 = {}
        for i in nums1:
            dict1[i] = True

        dict2 = {}        
        for j in nums2:
            dict2[j] = True

        op1 = []
        for i in dict1.keys():
            try:
                dict2[i]
            except:
                op1.append(i)

        op2 = []
        for j in dict2.keys():
            try:
                dict1[j]
            except:
                op2.append(j)
        return [op1, op2]

nums1 = [1,2,3]
nums2 = [2,4,6]
print(Solution().findDifference2(nums1, nums2))