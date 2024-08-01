class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        # backtracking 31 july 2024
        op = []

        def backtrack(current, i):
            print("current is - ", current)
            if len(current) == k:
                op.append(current[:])
                return
        
            for j in range(i, n+1):
                current.append(j)
                backtrack(current, j+1)
                current.pop()

        backtrack([],1)
        return op
        
n = 4
k = 2

print(Solution().combine(n,k))