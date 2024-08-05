class Solution:
    def climbStairs(self, n: int) -> int:
        
        @cache
        def dp(i, n):
            if i >= n:
                return 0
            if i == n-2:
                return 2
            if i == n-1:
                return 1
            
            return dp(i+2, n) + dp(i+1,n)
        
        return dp(0,n)