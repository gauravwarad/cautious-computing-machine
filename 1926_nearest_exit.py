from collections import deque
class Solution:
    def nearestExit(self, maze: list[list[str]], entrance: list[int]) -> int:

        # maze[entrance[0]][entrance[1]] = "+"
        queua = deque([[entrance[0], entrance[1], 0]]) # x, y, distance
        print(list(queua))
        # visited = [[0]*len(maze[0]) for i in range(len(maze))]
        visited = set()
        # visited.add((entrance))
        # print(maze)
        print("initial visited ", visited)
        while len(queua) > 0:
            current = queua.popleft()
            visited.add((current[0], current[1]))
            # visited[current[0]][current[1]] = 1
            # print(current[1], len(maze[0]))
            if current[0] == 0 or current[0] == len(maze)-1 or current[1] == 0 or current[1] == len(maze[0])-1:
                # it is an exit
                print("in the exit if loop, current is, ", current)
                if current[2] != 0: # not the entrance
                    print("exit found, ", current)
                    return current[2]
                    # break
            
            if current[0] > 0 and maze[current[0] - 1][current[1]] != "+":
                if (current[0] - 1, current[1]) not in visited:
                    queua.append([current[0] - 1, current[1], current[2] + 1])

            if current[1] > 0 and maze[current[0]][current[1] - 1] != "+":
                if (current[0], current[1] - 1) not in visited:
                    queua.append([current[0], current[1] - 1, current[2] + 1])

            if current[0] < len(maze) - 1 and maze[current[0] + 1][current[1]] != "+":
                if (current[0] + 1, current[1]) not in visited:
                    queua.append([current[0] + 1, current[1], current[2] + 1])

            if current[1] < len(maze[0]) - 1 and maze[current[0]][current[1] + 1] != "+":
                if (current[0], current[1] + 1) not in visited:
                    queua.append([current[0], current[1] + 1, current[2] + 1])
            # visited.append(current)
            
            print("the queue is , ",list(queua))
            
            # break

        print(visited)
        return -1


    def nearestExit2(self, maze: list[list[str]], entrance: list[int]) -> int:
        queua = deque([(entrance[0], entrance[1], 0)])
        # visited = set()
        rows = len(maze[0])
        columns = len(maze)
        maze[entrance[0]][entrance[1]] = "+"
        directions = [(1,0), (0, 1), (-1, 0), (0, -1)]
        # print(len(queua))
        while len(queua) > 0:
            current = queua.popleft()
            # visited.add((current[0], current[1]))
            # maze[current[0]][current[1]] = "+"

            if current[0] in {0, columns-1} or current[1] in {0, rows-1}:
                if current[2] != 0:
                    return current[2]
            
            for i, j in directions:
                i += current[0]
                j += current[1]

                if 0 <= i < columns and 0 <= j < rows and maze[i][j] != "+":
                    # if maze[i][j] != 1:#(i,j) not in visited:
                    queua.append((i,j, current[2]+1))
                    maze[i][j] = "+"
            # print(maze)
        # print(list(visited))
        return -1
    
    def nearestExit3(self, maze: list[list[str]], entrance: list[int]) -> int:
        # 27 jul

        visited = set()
        queua = deque()
        queua.append((entrance[0], entrance[1], 0))
        visited.add((entrance[0], entrance[1]))
        directions = ((0,1),(1,0),(-1,0),(0,-1))
        while len(queua) > 0:

            x, y, dist = queua.popleft()
            if x == 0 or x == len(maze) - 1 or y == 0 or y == len(maze[0]) - 1:
                if x != entrance[0] or y != entrance[1]:
                    print("exit found, ", x,y)
                    return dist # handle not to return the entrance point
            
            for dx, dy in directions:
                if 0 <= x+dx < len(maze) and 0 <= y+dy < len(maze[0]):
                    if maze[x+dx][y+dy] != "+" and (x+dx, y+dy) not in visited:
                        queua.append((x+dx, y+dy, dist+1))
                        visited.add((x+dx, y+dy))
        
        return -1
            

# maze = [["+","."]]
# entrance = [0,1]
# maze = [["+","+","+"],[".",".","."],["+","+","+"]]
# entrance = [1,0]
# maze = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]]
maze = [["+","+","+"],[".",".","."],["+","+","+"]]
# entrance = [1,2]
entrance = [1,0]
print(Solution().nearestExit3(maze, entrance))