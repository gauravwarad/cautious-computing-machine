class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        # backtracking
        # 31st july 2024
        op = []

        def backtrack(current, i):
            print("current is - ", current)

            if current not in op:
                op.append(current[:])
            
            for j in range(i, len(nums)):
                current.append(nums[j])
                backtrack(current, j+1)
                current.pop()
            return
        
        current = []
        backtrack(current, 0)

        return op

nums = [1,2,3]
print(Solution().subsets(nums))