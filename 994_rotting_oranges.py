from collections import deque

class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        # 1 - normal orange
        # 2 - rotten orange
        # 0 - no orange
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        rows = len(grid)
        columns = len(grid[0])
        queua = deque([])
        # find out initial rotten oranges
        rotten = []
        normal = 0
        latest_time = 0
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if grid[i][j] == 2:
                    # rotten orange found
                    rotten.append((i, j, 0)) # 0 is the time
                elif grid[i][j] == 1:
                    normal += 1
        
        print(rotten)
        print("normal oranges initially are - ", normal)
        queua.append(rotten)

        while len(queua) > 0 and normal > 0:
            rotten = []
            currently_rotten = queua.popleft()

            while len(currently_rotten) > 0:
                x, y, time = currently_rotten.pop()
                print("inside the inner while, x, y, time are - ", x, y, time)
                for i, j in directions:
                    i += x
                    j += y

                    if 0 <= i < rows and 0 <= j < columns:
                        if grid[i][j] == 1:
                            print("orange fallen, ", i, j, time + 1)
                            normal -= 1
                            grid[i][j] = 2
                            print("oranges remaining = , ", normal)
                            print("updated grid is - ", grid)
                            rotten.append((i, j, time + 1))
                            if time + 1 > latest_time:
                                latest_time = time + 1
            if len(rotten) != 0:
                queua.append(rotten) 

        if len(queua) == 0 and normal != 0:
            return -1


        # print(list(queua))
        return latest_time




grid = [[0,2]]
# grid = [[2,1,1],[1,1,0],[0,1,1]]
# grid = [[2,1,1],[0,1,1],[1,0,1]]
print(Solution().orangesRotting(grid))