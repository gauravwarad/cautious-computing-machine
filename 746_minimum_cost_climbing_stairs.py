from collections import defaultdict
class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        mini = 0

        total_cost = [cost[0], cost[1]]
        current = -1

        for i in range(2, len(cost)):
            option1 = cost[i] + total_cost[i-1]
            option2 = cost[i] + total_cost[i-2]

            total_cost.append(min(option1, option2))
        print(total_cost)
        return min(total_cost[-1],total_cost[-2])


    def minCostClimbingStairs2(self, cost: list[int]) -> int:

        def dp(i):
            print(i)
            if i<=1:
                cost_set[i] = 0
                return 0
            if i in cost_set:
                return cost_set[i]
            cost_set[i] = min(dp(i-1)+cost[i-1], dp(i-2)+cost[i-2])
            
            return cost_set[i]
        cost_set = {}
        op = dp(len(cost))
        print(cost_set)
        return op





# cost = [10,15,20,1]

# cost = [1,100,1,1,1,100,1,1,100,1]
# 1 or 100
cost=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0]
print(Solution().minCostClimbingStairs2(cost))