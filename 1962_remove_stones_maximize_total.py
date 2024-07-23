import heapq
import math
class Solution:
    def minStoneSum(self, piles: list[int], k: int) -> int:
        piles = [-pile for pile in piles]
        heapq.heapify(piles)

        for _ in range(k):
            heapq.heappush(piles, -math.ceil(-heapq.heappop(piles)/2))
            print(piles)
        
        return -sum(piles)

piles = [5,4,9]
k = 2
print(Solution().minStoneSum(piles, k))