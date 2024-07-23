class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = [[0]*n for _ in range(m)]
        directions = ((0,1), (1,0), (-1,0), (0,-1))
        def dfs(i, j):
            if visited[i][j] == 1:
                return 0
            if grid[i][j] == 0:
                # it's water
                visited[i][j] = 1
                return 0
            land = 1
            visited[i][j] = 1
            for x, y in directions:
                if 0 <= x+i < m and 0 <= y+j < n:
                    land += dfs(x+i, y+j)
            
            return land
        maxi = 0
        for x1 in range(0, m):
            for y1 in range(0,n):
                land_area = dfs(x1, y1)
                maxi = max(maxi, land_area)
        
        return maxi




grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
print(Solution().maxAreaOfIsland(grid))