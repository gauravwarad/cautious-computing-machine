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

    def rob2(self, nums: list[int]):
        # 2nd august 24 --- now i kinda get it.
        score = [-1]*len(nums)
        if len(nums) == 1:
            return nums[0]
        score[0] = nums[0]
        score[1] = max(nums[0], nums[1])
        def dp(i):
            if score[i] != -1:
                return score[i]
            score[i] = max(dp(i-1), dp(i-2) + nums[i])
            return score[i]
        return dp(len(nums)-1)

nums = [2,7,9,3,1]
print(Solution().rob2(nums))