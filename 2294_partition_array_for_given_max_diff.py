class Solution:
    def partitionArray2(self, nums: list[int], k: int) -> int:
        nums.sort()
        x = nums[0]
        count = 1
        for i in range(0, len(nums)):
            if nums[i] > x + k:
                count += 1
                x = nums[i]
        return count









    def partitionArray(self, nums: list[int], k: int) -> int:

        nums.sort()
        diff = 0
        count = 0
        mini = nums[0]
        maxi = nums[0]
        for i in range(0, len(nums)):
            print("for loop - num is - ", nums[i])
            mini = min(nums[i], mini)
            maxi = max(nums[i], maxi)
            diff = abs(maxi - mini)
            print("mini, maxi and diff is = ", mini, maxi, diff)
            if diff > k:
                print("count incremented", count)
                count += 1
                if i + 1 < len(nums):
                    mini = nums[i+1]
                    maxi = nums[i+1]

        return count + 1
            

nums = [3,6,1,2,5]
k = 2

print(Solution().partitionArray2(nums, k))