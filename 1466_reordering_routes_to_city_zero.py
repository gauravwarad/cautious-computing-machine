from collections import defaultdict

class Solution:
    def minReorder(self, n: int, connections: list[list[int]]) -> int:
        # neighbours = {}
        connection2 = set()
        neighbours = defaultdict(list)
        for x,y in connections:
            neighbours[x].append(y)
            neighbours[y].append(x)
            connection2.add((x,y))
        
        visited = [0]*n
        
        def dfs(node):
            
            count = 0
            for n in neighbours[node]:
                if visited[n]==0:
                    if (node, n) in connection2:
                        print([node, n])
                        count+= 1
                    visited[node] = 1
                    count += dfs(n)
            return count
        op = 0
        op = dfs(0)
        
        return op

n = 6
connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]

print(Solution().minReorder(n, connections))