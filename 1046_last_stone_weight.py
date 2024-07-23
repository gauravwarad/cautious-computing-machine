import heapq

class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        stones = [stone*-1 for stone in stones]
        heapq.heapify(stones)
        last = None
        while len(stones) > 1:
            y = heapq.heappop(stones) # -100
            x = heapq.heappop(stones) # -99

            if x > y:
                heapq.heappush(stones, y-x)
            elif x == y:
                last = x-y
            else:
                # print("something terrible has happened")
                break
        if len(stones) == 0:
            return last
        return heapq.heappop(stones) * -1



stones = [2,2]
print(Solution().lastStoneWeight(stones))