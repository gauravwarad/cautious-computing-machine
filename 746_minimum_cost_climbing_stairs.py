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

cost = [10,15,20]

cost = [1,100,1,1,1,100,1,1,100,1]
# 1 or 100
print(Solution().minCostClimbingStairs(cost))