import heapq
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: list[int], capital: list[int]) -> int:
        
        mapped = sorted(zip(capital, profits))

        # print(sorted(mapped))
        j = 0
        heapa = []
        for i in range(0,k):
            # heapa = []
            while j < len(capital) and mapped[j][0] <= w:
                heapq.heappush(heapa, -mapped[j][1])
                j += 1
                print(heapa)
            if len(heapa) == 0:
                break

            w -= heapq.heappop(heapa)
        
        return w

            

        # i = 0
        # while capital[i] <= w:
        #     heapq.heappush(heapa, -profits[i])
        #     i += 1
        
        # print(heapa)

k = 2
w = 0
profits = [1,2,3]
capital = [0,1,1]
print(Solution().findMaximizedCapital(k,w,profits,capital))