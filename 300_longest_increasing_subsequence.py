class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        # 2nd aug 2024 
        max_len = [-1]*len(nums)

        def dp(i):
            print(i)
            if max_len[i] != -1:
                return max_len[i]
            max_len[i] = 1
            for j in range(i, -1, -1):
                if nums[j] < nums[i]:
                    max_len[i] = max(max_len[i], dp(j) + 1)
                    if j < max_len[i]:
                        j -= 1
            return max_len[i]
            

        for i in range(len(nums)):
            dp(i)
        print(max_len)
        return max(max_len)
nums = [10,9,2,5,3,7,101,18]
# nums = [0,1,0,3,2,3]
print(Solution().lengthOfLIS(nums))