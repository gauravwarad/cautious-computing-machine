class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        # 1st aug
        # below works but it's too slow!
        op = []
        
        def backtrack(current):
            print("current is - ", current)
            if sum(current) == target:
                temp = current[:]
                temp.sort()
                if temp[:] not in op:
                    op.append(temp[:])
                return
            if sum(current) > target:
                return
            for i in candidates:
                current.append(i)
                backtrack(current)
                current.pop()
            
            return

        backtrack([])

        return op

    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        op = []
        n = len(candidates)

        def backtrack(current, i):
            print("current is - ", current)
            suma = sum(current)
            if suma == target:
                if current not in op:
                    op.append(current[:])
                return
            if suma > target:
                return
            
            for j in range(i, n):
                current.append(candidates[j])
                backtrack(current, j)
                current.pop()
            
            return
        
        backtrack([],0)

        return op
candidates = [2,3,6,7]
target = 7

print(Solution().combinationSum2(candidates, target))