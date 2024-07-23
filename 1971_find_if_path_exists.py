from collections import defaultdict
class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True
        stacku = [source]
        connections = defaultdict(list)
        for x,y in edges:
            connections[x].append(y)
            connections[y].append(x)
        visisted = n*[0]
        visisted[0]=1
        while len(stacku) > 0:
            current = stacku.pop()
            for i in connections[current]:
                if i == destination:
                    return True
                if visisted[i] == 0:
                    stacku.append(i)
                    visisted[i] = 1
        
        return visisted[destination]


n = 3
edges = [[0,1],[1,2],[2,0]]
source = 0
destination = 2
print(Solution().validPath(n,edges,source,destination))