import heapq
class Solution:
    def halveArray(self, nums: list[int]) -> int:
        sum = 0
        for i in nums:
            sum += i
        nums = [-num for num in nums]
        heapq.heapify(nums)
        target_sum = sum/2
        print("target sum is , ", target_sum)
        count = 0
        while sum > target_sum:
            temp = (heapq.heappop(nums))/2
            sum += temp
            print("new sum is - ", sum)
            heapq.heappush(nums, temp)
            count += 1
        return count

nums = [1]
print(Solution().halveArray(nums))