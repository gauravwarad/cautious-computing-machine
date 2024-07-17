class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return 0
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right)//2
            # print(left, right, mid, nums[mid])
            if mid == 0:
                if nums[mid] > nums[mid + 1]:
                    return mid
            elif mid == len(nums) - 1:
                if nums[mid] > nums[mid - 1]:
                    return mid
            elif nums[mid] > nums[mid + 1] and nums[mid] > nums[mid - 1]:
                return mid
        
            if nums[mid] > nums[mid + 1]:
                right = mid - 1
            else:
                left = mid + 1
    



nums = [1,2,1,3,5,6,7] # [1,2,3,1]
# nums = [1,2]
print(Solution().findPeakElement(nums))

