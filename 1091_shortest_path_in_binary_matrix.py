from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        queua = deque()
        queua.append((0,0,1))
        m = len(grid)
        n = len(grid[0])
        # visited = [n*[0] for _ in range(m)]
        seen = set()
        # print(visited)
        directions = ((0,1),(1,0),(-1,0),(0,-1),(1,1),(-1,-1),(-1,1),(1,-1))

        while len(queua) > 0:
            x, y, dist = queua.popleft()
            print(x, y, dist)
            if grid[x][y] == 1:
                break
            if x == m - 1 and y == n - 1:
                return dist
            seen.add((x,y))
            # visited[x][y] = 1
            for i, j in directions:
                if 0 <= x+i < m and 0 <= y+j < n:
                    if (x+i, y+j) not in seen and grid[x+i][y+j] == 0:
                        queua.append((x+i, y+j, dist + 1))
        
        return -1

# grid = [[0,0,0],[1,1,0],[1,1,0]]
grid = [[0,0,0],
        [1,1,0],
        [1,1,1]]
print(Solution().shortestPathBinaryMatrix(grid))