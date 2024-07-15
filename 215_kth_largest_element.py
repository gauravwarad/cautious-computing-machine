import heapq

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:

        newnums = [-num for num in nums]

        print(newnums)

        heapa = []

        for i in newnums:
            heapq.heappush(heapa, i)
        
        while k != 0:
            small = heapq.heappop(heapa)
            k -= 1

        return -small

nums = [3,2,1,5,6,4]
# nums = [2, 1]
k = 2
print(Solution().findKthLargest(nums, k))