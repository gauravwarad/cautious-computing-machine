import math
class Solution:
    def smallestDivisor(self, nums: list[int], threshold: int) -> int:
    
        def checksum(divisor):
            sum = 0
            for num in nums:
                sum = sum + math.ceil(num/divisor)
            
            return sum <= threshold
        
        left = 1
        right = max(nums)

        while left <= right:
            mid = (left + right)//2

            if checksum(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left
 
nums = [1,2,5,9]
threshold = 6

print(Solution().smallestDivisor(nums, threshold))