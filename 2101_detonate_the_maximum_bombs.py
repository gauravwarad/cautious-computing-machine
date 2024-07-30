class Solution:
    def maximumDetonation(self, bombs: list[list[int]]) -> int:
        
        # below doesn't work if same coordinate has two bombs.


        # dfs 
        # radius = r

        # visited = set()

        def detonate(current):
            x, y, r = current
            ans = 1
            visited.add((x,y))

            for bomb in bombs:
                if (bomb[0], bomb[1]) not in visited:
                    print("radius is - ", r)
                    print("distance between centers is - ", ((x-bomb[0])**2 + (y-bomb[1])**2)**1/2)
                    if r >= ((x-bomb[0])**2 + (y-bomb[1])**2)**(1/2):
                        ans += detonate(bomb)
            return ans

        # visited = set()
        # print(detonate(bombs[0]))
        # print(visited)
        op = []
        for bomb in bombs:
            visited = set()
            op.append(detonate(bomb))
            print(visited)
        print(op)
        return max(op)
        # greedy possible?
    

    def maximumDetonation2(self, bombs: list[list[int]]) -> int:
        
        
        def detonate(current, i):
            x, y, r = current
            ans = 1
            visited[i] = 1

            for j in range(0, len(bombs)):
                if visited[j] == 0:
                    print("radius is - ", r)
                    print("distance between centers is - ", ((x-bombs[j][0])**2 + (y-bombs[j][1])**2)**1/2)
                    if r >= ((x-bombs[j][0])**2 + (y-bombs[j][1])**2)**(1/2):
                        ans += detonate(bombs[j], j)
            return ans

        # visited = set()
        # print(detonate(bombs[0]))
        # print(visited)
        op = []
        i = 0
        for bomb in bombs:
            visited = [0]*len(bombs)
            op.append(detonate(bomb, i))
            i += 1
            print(visited)
        print(op)
        return max(op)
        # greedy possible?



    def maximumDetonation3(self, bombs: list[list[int]]) -> int:
        # greedy?
        # greedy doesn't work
        
        def detonate(current, i):
            print("detonating bomb - ", current)
            x, y, r = current
            ans = 1
            visited[i] = 1

            for j in range(0, len(bombs)):
                if visited[j] == 0:
                    # print("radius is - ", r)
                    # print("distance between centers is - ", ((x-bombs[j][0])**2 + (y-bombs[j][1])**2)**1/2)
                    if r >= ((x-bombs[j][0])**2 + (y-bombs[j][1])**2)**(1/2):
                        ans += detonate(bombs[j], j)
            return ans

        op = []
        i = 0
        max_r = 0
        max_r_index = -1
        for j in range(len(bombs)):
            if bombs[j][2] > max_r:
                max_r = bombs[j][2]
                max_r_index = j
        visited = [0]*len(bombs)
        return detonate(bombs[j], j)

# bombs = [[2,1,3],[2,1,3]]
bombs = [[1,2,3],[2,3,1],[3,4,2],[4,5,3],[5,6,4]]
print(Solution().maximumDetonation4(bombs))