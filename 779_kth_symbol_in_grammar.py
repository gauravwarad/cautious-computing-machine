import math
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        
        if n == 1:
            return 0
        
        row = self.kthGrammar(n-1, math.ceil(k/2))

        if row == 0:
            if k % 2 == 0:
                return 1
            else:
                return 0
        else:
            if k % 2 == 0:
                return 0
            else:
                return 1




    #     nth = self.nth_row(n)
    #     kth = nth[k-1]

    #     return int(kth)
        
    # def nth_row(self, n):
    #     if n == 1:
    #         row = "0"
    #         return row
        
    #     row = self.nth_row(n-1)
    #     op = ""
    #     for i in row:
    #         if i == "0":
    #             op = op + "01"
    #         else:
    #             op = op + "10"
        
    #     return op

        
print(Solution().kthGrammar(4,3))