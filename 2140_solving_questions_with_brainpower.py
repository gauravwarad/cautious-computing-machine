from functools import cache
class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        # 4aug, with a lot of help
        @cache
        def dp(i):
            # print("i is - ", i)
            if i >= len(questions):
                return 0
            return max(questions[i][0] + dp(i+1+questions[i][1]), dp(i+1))
        return dp(0)