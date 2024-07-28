# this probably is the worst problem on leetcode.
from collections import deque
class Solution:
    def snakesAndLadders(self, board: list[list[int]]) -> int:
        n = len(board)
        nsquare = n**2
        cells = [None]*(nsquare + 1)
        i = 1
        rev = False
        cells[i] = (n-1, 0)
        for x in range(n-1, -1, -1):
            for y in range(0, n):
                if rev:
                    cells[i] = (x, n-y-1)
                else:
                    cells[i] = (x, y)
                i += 1
            if rev:
                rev = False
            else:
                rev = True

        print(cells)
        visited = set()
        queua = deque()
        directions = (1,2,3,4,5,6)
        queua.append((1, 0))
        visited.add(1)
        op = set()
        while len(queua) > 0:
            current, dist = queua.popleft()
            print("current cell is - ", current)
            # if cells[current] == (nsquare-1, nsquare-1):
            if current == i-1:
                op.add(dist)
            
            for d in directions:
                if current+d not in visited and current+d <= nsquare:
                    x,y = cells[current+d]
                    if board[x][y] == -1:
                        queua.append((current+d, dist+1))
                        visited.add(current+d)
                    else:
                        queua.append((board[x][y], dist+1))
                        visited.add(board[x][y])
                        visited.add(current+d)
        print(op)
        return min(op)
    
    def snakesAndLadders2(self, board: list[list[int]]) -> int:
        # the below code takes consecutive ladders, that is why it won't work.
        n = len(board)
        nsquare = n**2
        cells = [None]*(nsquare + 1)
        i = 1
        rev = False
        cells[i] = (n-1, 0)
        for x in range(n-1, -1, -1):
            for y in range(0, n):
                if rev:
                    cells[i] = (x, n-y-1)
                else:
                    cells[i] = (x, y)
                i += 1
            if rev:
                rev = False
            else:
                rev = True

        print(cells)
        # visited = set()
        queua = deque()
        directions = (1,2,3,4,5,6)
        queua.append(1)
        # visited.add(1)
        distance = [-1]*(nsquare + 1)
        distance[1] = 0
        # op = set()
        while len(queua) > 0:
            print(queua)
            current = queua.popleft()
            print("current cell is - ", current, "x,y is - ", cells[current], "distance is - ", distance[current])
            # if cells[current] == (nsquare-1, nsquare-1):
            if distance[nsquare] != -1:
                return distance[nsquare]
            for d in directions:
                next_node = min(current + d, nsquare)
                print("initial next node is - ", next_node)
                if distance[next_node] == -1: # the node is unvisited
                    x, y = cells[next_node]
                    while board[x][y] != -1:
                        if distance[next_node] == -1:
                            distance[next_node] = distance[current] + 1
                        print("in inner while loop - ", next_node)
                        next_node = board[x][y]
                        x, y = cells[next_node]
                        
                    print("final next node is - ", next_node)
                    print("distance = ", distance[next_node])
                    if distance[next_node] == -1:
                        queua.append(next_node)
                        distance[next_node] = distance[current] + 1


    def snakesAndLadders3(self, board: list[list[int]]) -> int:
        n = len(board)
        nsquare = n**2
        cells = [None]*(nsquare + 1)
        i = 1
        rev = False
        cells[i] = (n-1, 0)
        for x in range(n-1, -1, -1):
            for y in range(0, n):
                if rev:
                    cells[i] = (x, n-y-1)
                else:
                    cells[i] = (x, y)
                i += 1
            if rev:
                rev = False
            else:
                rev = True

        # print(cells)
        visited = set()
        queua = deque()
        directions = (1,2,3,4,5,6)
        queua.append((1, 0))
        visited.add(1)
        op = set()
        while len(queua) > 0:
            print(queua)
            current, dist = queua.popleft()
            print("current cell is - ", current)
            # if cells[current] == (nsquare-1, nsquare-1):
            if current == i-1:
                # op.add(dist)
                return dist
            # checking if current has a ladder/snake
            x, y = cells[current]
            if board[x][y] != -1 and board[x][y] not in visited and current+1 <= board[x][y] <= min(current+6, nsquare):
                queua.append((board[x][y], dist+1))
                visited.add(board[x][y])
            
            for d in directions:
                next_node = min(current+d, nsquare)
                if next_node not in visited:
                    x,y = cells[next_node]
                    if board[x][y] == -1:
                        queua.append((next_node, dist+1))
                        visited.add(next_node)
                    else:
                        queua.append((board[x][y], dist+1))
                        visited.add(board[x][y])
                        visited.add(next_node)
        # print(op)
        return -1





                # print("next_node - ", next_node)
                # if distance[next_node] == -1:
                #     x,y = cells[next_node]
                #     print("board of x,y is - ", board[x][y])
                #     if board[x][y] == -1:
                #         queua.append(next_node)
                #         print("adding - ", next_node)
                #         # visited.add(current+d)
                #     else:
                #         while board[x][y] != -1:
                #             next_in_line = board[x][y]
                            
                #             x, y = cells[next_in_line]
                #             print("while loop - ", board[x][y])
                                
                #             if distance[board[x][y]] == -1:
                #                 distance[board[x][y]] = distance[current] + 1
                #         queua.append(next_in_line)
                #         # visited.add(board[x][y])
                #         # visited.add(current+d)
                #     distance[next_node] = distance[current] + 1
                # print("end of d - ",d, "distance of 7 is - ", distance[7])
                    
        # print(op)
        return distance[nsquare]
# board = [[-1,-1,-1,-1,-1,-1],
#          [-1,-1,-1,-1,-1,-1],
#          [-1,-1,-1,-1,-1,-1],
#          [-1,35,-1,-1,13,-1],
#          [-1,-1,-1,-1,-1,-1],
#          [-1,15,-1,-1,-1,-1]]
board = [[-1,-1,-1,46,47,-1,-1,-1],
         [51,-1,-1,63,-1,31,21,-1],
         [-1,-1,26,-1,-1,38,-1,-1],
         [-1,-1,11,-1,14,23,56,57],
         [11,-1,-1,-1,49,36,-1,48],
         [-1,-1,-1,33,56,-1,57,21],
         [-1,-1,-1,-1,-1,-1,2,-1],
         [-1,-1,-1,8,3,-1,6,56]]
# board = [[-1,-1,-1,46,47,-1,-1,-1],[51,-1,-1,63,-1,31,21,-1],[-1,-1,26,-1,-1,38,-1,-1],[-1,-1,11,-1,14,23,56,57],[11,-1,-1,-1,49,36,-1,48],[-1,-1,-1,33,56,-1,57,21],[-1,-1,-1,-1,-1,-1,2,-1],[-1,-1,-1,8,3,-1,6,56]]
print(Solution().snakesAndLadders3(board))
# 5,0 + 1 = 5,1
# 5,2; 5,3; 5,4, 5,5; 4,5; 
