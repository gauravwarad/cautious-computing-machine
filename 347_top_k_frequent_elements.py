import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        if len(nums) == k:
            return nums

        counts = Counter(nums)

        print(counts)

        return heapq.nlargest(k, counts.keys(), counts.get())

nums = [1,2]
k = 2
print(Solution().topKFrequent(nums,k))