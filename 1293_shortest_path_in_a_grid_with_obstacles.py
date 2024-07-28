from collections import deque
class Solution:
    def shortestPath(self, grid: list[list[int]], k: int) -> int:

        # start from the top left
        # BFS using queue - go to the bottom right
        # destroy atmost k walls
        m = len(grid)
        n = len(grid[0])
        print(m, n)
        queua = deque()
        queua.append((0,0,0,0)) # x, y, dist, bullet
        directions = ((1,0),(0,1),(-1,0),(0,-1))
        visited = set()
        visited.add((0,0,0)) # bullet goes in visite
        while len(queua) > 0:
            print(queua)
            
            x, y, dist, bullet = queua.popleft()
            print(x, y)
            if x == m-1 and y == n-1:
                # possible.append(dist)
                return dist
            for i, j in directions:
                newx = x + i
                newy = y + j
                if 0 <= newx < m and 0 <= newy < n :
                    if grid[newx][newy] == 0 and (newx, newy, bullet) not in visited:
                        queua.append((newx, newy, dist + 1, bullet))
                        visited.add((newx, newy, bullet))
                    elif bullet < k and (newx, newy, bullet + 1) not in visited:
                        queua.append((newx, newy, dist + 1, bullet + 1))
                        visited.add((newx, newy, bullet + 1))
        return -1





# grid = [[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]]
grid = [[0,0],[1,0],[1,0],[1,0],[1,0],[1,0],[0,0],[0,1],[0,1],[0,1],[0,0],[1,0],[1,0],[0,0]]
k = 4
print(Solution().shortestPath(grid, k))
