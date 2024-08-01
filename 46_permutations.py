class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        
        # backtracking
        # 31 july 2024
        op = []

        def backtrack(current):
            print("current is ", current)
            if current is None:
                current = []
            if len(current) == len(nums):
                op.append(current[:])
                return

            for num in nums:
                if num not in current:
                    current.append(num)
                    backtrack(current)
                    current.pop()
            return
        
        current1 = list()
        backtrack(current1)
        return op

nums = [1,2,3]
print(Solution().permute(nums))