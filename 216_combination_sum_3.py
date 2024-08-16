class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
      # 15th aug - backtracking.
        op = []
        def backtrack(arr):
            if len(arr) == k:
                suma = sum(arr)
                if suma == n:
                    op.append(arr[:])
                return
            if len(arr) > 0:
                j = arr[-1]+1
            else:
                j = 1
            for i in range(j, 10):
                arr.append(i)
                backtrack(arr)
                arr.pop()
            return
        backtrack([])
        return op
