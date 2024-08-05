class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = [-2]*(amount+1)
        # 1, 2, 5
        # dp(11) = dp(10) + 1
        #           dp(9) + 2
        # dp(6) + 5
        # for loop -- 

        def dp(req):
            # print(req)
            if req < 0:
                return -1
            if memo[req] == -1:
                return -1
            if memo[req]!= -2:
                return memo[req] 

            if req in coins:
                return 1
            if req == 0:
                return 0
            
            possibilities = []
            for i in coins:
                temp = dp(req - i)
                if temp != -1:
                    possibilities.append(temp + 1)
            if len(possibilities) > 0:
                memo[req] = min(possibilities)

                return memo[req]
            else:
                memo[req] = -1
                return -1
        op = dp(amount)
        # print(memo)
        return op
