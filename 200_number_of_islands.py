class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        
        count = 0
        m = len(grid)
        n = len(grid[0])

        visited = [[0] * n for _ in range(m)]
        print(visited)
        directions = ((0,1),(1,0), (-1,0),(0,-1))
        def dfs(i, j):
            print("inside dfs, i,j, visited is - ",i, j, visited)
            if visited[i][j] == 1 or visited[i][j]== -1:
                return
            if grid[i][j] == '0':
                # water
                visited[i][j] = -1
                return
            visited[i][j] = 1
            for x, y in directions:
                if 0 <= x+i < m and 0<= y+j < n:
                    dfs(i+x, j+y)
            return
        for i1 in range(0, m):
            for j1 in range(0,n):
                if visited[i1][j1] == 0:
                    dfs(i1,j1)
                    if visited[i1][j1] != -1:
                        count += 1
                    print("count incremented - ", count)
        print(visited)
        return count
# grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
print(Solution().numIslands(grid))