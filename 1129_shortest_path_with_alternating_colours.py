from collections import defaultdict, deque
class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: list[list[int]], blueEdges: list[list[int]]) -> list[int]:
        # n is the no. of nodes
        # directed graph
        # each edge is either red or blue => can be self edges or parallel edges
        # return len of shortest path from 0 to x for x in 0 to n-1 aka return array

        rede = defaultdict(list)
        bluee = defaultdict(list)

        for x, y in redEdges:
            rede[x].append(y)
        for x, y in blueEdges:
            bluee[x].append(y)
        

        RED = 0
        BLUE = 1


        queua = deque()
        queua.append((0, RED, 0))
        queua.append((0, BLUE, 0))

        print(bluee)
        print(rede)


        seen = set()
        seen.add((0, RED))
        seen.add((0, BLUE))

        op = [10000]*n

        while len(queua) > 0:
            current, colour, dist = queua.popleft()
            op[current] = min(op[current], dist)

            if colour == RED:
                for node in bluee[current]:
                    if (node,BLUE) not in seen:
                        queua.append((node, BLUE, dist + 1))
                        seen.add((node, BLUE))
            else:
                for node in rede[current]:
                    if (node, RED) not in seen:
                        queua.append((node, RED, dist + 1))
                        seen.add((node, RED))
        
        return [x if x != 10000 else -1 for x in op]

n = 3
redEdges = [[0,1],[1,2]]
blueEdges = []
print(Solution().shortestAlternatingPaths(n, redEdges, blueEdges))