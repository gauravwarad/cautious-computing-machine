from collections import Counter
import heapq
class Solution:
    def findLeastNumOfUniqueInts(self, arr: list[int], k: int) -> int:

        # find the counts of appearances
        # remove least appeared - using heap? or just sort and remove/count

        counts = dict(Counter(arr))

        sorted_cnts = sorted(counts, key=counts.get, reverse=True)

        print(sorted_cnts)

        for _ in range(k):
            # reduce values of sorted_cnt[0] from dict
            # if 0, pop from sorted_cnt and get next
            counts[sorted_cnts[0]] -= 1
            if counts[sorted_cnts[0]] == 0:
                sorted_cnts.pop()


        return sorted_cnts
    
    def findLeastNumOfUniqueInts2(self, arr: list[int], k: int) -> int:

        # find the counts of appearances
        # remove least appeared - using heap

        counts = dict(Counter(arr))

        # heapq.heapify()


        return heapq.nsmallest(k, counts, key=counts.get)


arr = [5,5,4,3,3,3,2]
k = 3

print(Solution().findLeastNumOfUniqueInts2(arr, k))