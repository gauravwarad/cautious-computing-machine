from collections import defaultdict
class Solution:
    
    def findCircleNum2(self, isConnected: list[list[int]]) -> int:
        # 22 july - 
        # converting to a dict
        # connections = 1: [2, 3], 2:[1, 3, 4], 3:[1,2], 4:[2], 5:[]
        connections = {}
        for i in range(0, len(isConnected)):
            connections[i] = []
            for j in range(0, len(isConnected[i])):
                if isConnected[i][j] == 1 and i != j:
                    connections[i].append(j)
        print(connections)
        i = 0
        visited = set()
        
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for i in connections[node]:
                dfs(i)
        count = 0
        for j in connections.keys():
            if j not in visited:
                dfs(j)
                count += 1

        return count

    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        
        visited = [0]*len(isConnected)
        provinces = 0
        
        def check_con(i):
            visited[i] = 1
            for j in range(0, len(isConnected[i])):
                if visited[j] != 1:
                    if isConnected[i][j] == 1:
                        check_con(j)

        for city in range(0, len(isConnected)):
            if visited[city] == 0:
                provinces += 1
                check_con(city)
        return provinces

isConnected = [[1,1,0],[1,1,0],[0,0,1]]
# connections = 1: [2, 3], 2:[1, 3, 4], 3:[1,2], 4:[2], 5:[]
isConnected = [[1,1,1,0,0],[1,1,1,1,0],[1,1,1,0,0],[0,1,0,1,0],[0,0,0,0,0]]
print(Solution().findCircleNum2(isConnected))
