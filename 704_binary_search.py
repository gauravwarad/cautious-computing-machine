class Solution:
    def search(self, nums: list[int], target: int) -> int:
        
        left = 0
        right = len(nums) - 1
        mid = (left + right)//2

        while left <= right:
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
            
            mid = (left + right)//2

        return -1


nums = [-1,0,3,5,9,12]
target = 9
print(Solution().search(nums, target))