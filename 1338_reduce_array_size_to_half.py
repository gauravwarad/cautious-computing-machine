from collections import Counter
class Solution:
    def minSetSize(self, arr: list[int]) -> int:
        
        counts = dict(Counter(arr))

        counts_sorted = dict(sorted(counts.items(), key=lambda item: item[1], reverse=True))

        print(counts_sorted)
        target = len(arr)/2
        ans = 0
        for k,v in counts_sorted.items():
            
            # removing k
            target -= v
            ans += 1
            if target <= 0:
                break

        return ans


arr = [3,3,3,3,5,5,5,2,2,7]
print(Solution().minSetSize(arr))



