class Solution:
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
print(Solution().findCircleNum(isConnected))
