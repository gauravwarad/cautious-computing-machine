from collections import defaultdict, deque
class Solution:
    def calcEquation(self, equations: list[list[str]], values: list[float], queries: list[list[str]]) -> list[float]:
        # a, b, c are nodes in a graph?

        edges = defaultdict(list)
        distance = defaultdict(float)
        i = 0
        for x, y in equations:
            edges[x].append(y)
            edges[y].append(x)
            distance[(x,y)] = values[i]
            distance[(y,x)] = 1/values[i]
            i += 1
        
        print(edges)
        print(distance)

        # queua = deque()
        # queua.append((equations[0][0], values[0]))
        # visited = set()
        # visited.add(equations[0][0])

        def bfs(x,y):
            print("in bfs for - ", x, y)
            queua = deque()
            queua.append((x,1))
            visited = set()
            visited.add(x)

            while len(queua) > 0:
                current, dist = queua.popleft()

                if current == y:
                    return dist
                
                for neighbour in edges[current]:
                    if neighbour not in visited:
                        # if not distance[(current,neighbour)]:
                        if not distance[(x, neighbour)]:
                            distance[(x, neighbour)] = dist*distance[(current,neighbour)]
                            distance[(neighbour,x)] = 1/dist*distance[(current,neighbour)]
                        queua.append((neighbour, dist*distance[(current,neighbour)]))
                        visited.add(neighbour)

            return -1
        
        op = []
        for x,y in queries:
            if distance[(x,y)]:
                op.append(distance[(x,y)])
            elif distance[(y,x)]:
                op.append(1/distance[(y,x)])
            elif not edges[x] or not edges[y]:
                op.append(-1)
            else:
                op.append(bfs(x,y))
        
        return op

equations = [["a","b"],["b","c"]]
values = [2.0,3.0]
queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
print(Solution().calcEquation(equations, values, queries))