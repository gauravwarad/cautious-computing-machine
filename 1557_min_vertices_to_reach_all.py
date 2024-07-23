from collections import defaultdict
class Solution:
    def findSmallestSetOfVertices2(self, n: int, edges: list[list[int]]) -> list[int]:

        indegrees = n*[0]
        for x, y in edges:
            indegrees[y] += 1
        
        op = [x for x in range(0, n) if indegrees[x] == 0]
        return op
    
    def findSmallestSetOfVertices(self, n: int, edges: list[list[int]]) -> list[int]:
        visited = [0]*n
        connections = defaultdict(list)
        for x,y in edges:
            connections[x].append(y)
        print(connections)
        def dfs(node):
            if visited[node] != 0:
                return
            visited[node] += 1
            for n in connections[node]:
                dfs(n)
        count = []
        # dfs(0)
        for i in range(0,n):
            if visited[i] == 0:
                dfs(i)
                # count.append(i)
                visited[i] -= 1
        
        for i in range(0, n):
            if visited[i] == 0:
                count.append(i)
        return count
n = 6
edges = [[0,1],[0,2],[2,5],[3,4],[4,2]]
print(Solution().findSmallestSetOfVertices2(n, edges))