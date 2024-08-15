class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
      # another one bites the dust - 15th aug
        if len(nums) < 2:
            return 0
        prefix = [0]
        for i in nums:
            prefix.append(prefix[-1]+i)
        # print(prefix)
        
        for i in range(1, len(nums)):
            if prefix[i-1] == prefix[len(nums)] - prefix[i]:
                return i-1
        if i<len(prefix) and prefix[i] == 0:
            return i
        return -1
