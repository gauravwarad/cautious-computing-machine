# i have so many questions!!!!!!!!!!!!!!!!!!!

class Solution:
    def rob(self, nums: list[int]) -> int:
        rob1 = 0
        rob2 = 0

        for i in nums:
            value = max(rob1 + i, rob2)
            print(value, rob1, rob2)
            
            rob1 = rob2
            rob2 = value
            

        return max(rob1, rob2)



nums = [2,7,9,3,1]
# can't rob adjacent houses
# 2 and 9 or 7 and 3 or 2 and 3
# 2 + 9 is greater so 2,9

# what if [2, 7, 9, 3, 1, 5, 6, 9, 8]
# [2] + max of [9,.......]
# 7 + max of [3, ........]

print(Solution().rob(nums))