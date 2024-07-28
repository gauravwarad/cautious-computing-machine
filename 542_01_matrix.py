from collections import deque
class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        m = len(mat)
        n = len(mat[0])
        op = mat.copy()
        # visited = [n*[0] for _ in range(m)]
        visited = set()
        queua = deque()
        # find out all 0s and adding them to seen
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    queua.append((i, j, 0))
                    visited.add((i,j))
        
        directions = ((1,0),(0,1),(-1,0),(0,-1))
        # op = []
        while len(queua) > 0:
            x, y, dist = queua.popleft()
            print(x, y, dist)
            
            for i, j in directions:
                if 0 <= x+i < m and 0 <= y+j < n:
                    if (x+i, y+j) not in visited and mat[x+i][y+j] == 1:
                        queua.append((x+i, y+j, dist + 1))
                        visited.add((x+i, y+j))
                        mat[x+i][y+j] = dist + 1
                        

        return mat

mat = [[0,0,0],[0,1,0],[1,1,1]]
print(Solution().updateMatrix(mat))