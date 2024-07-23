from collections import defaultdict
class Solution:
    def reachableNodes(self, n: int, edges: list[list[int]], restricted: list[int]) -> int:
        
        connections = defaultdict(list)

        for x, y in edges:
            # if x not in restricted and y not in restricted:
            connections[x].append(y)
            connections[y].append(x)
        
        print(connections)

        visited = set(x for x in restricted)

        def dfs(node):
            print("in dfs of - ", node)
            if node in visited:
                return 0
            visited.add(node)
            count = 1
            for nei in connections[node]:
                count += dfs(nei)
            return count

        return dfs(0)

n = 7
edges = [[0,1],[1,2],[3,1],[4,0],[0,5],[5,6]]
restricted = [4,5]
print(Solution().reachableNodes(n, edges, restricted))