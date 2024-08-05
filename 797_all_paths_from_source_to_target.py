class Solution:
    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        # backtracking 31st july 2024
        
        n = len(graph)
        op = []

        def backtrack(current):
            print("current is - ", current)
            if current[-1] == n-1:
                op.append(current[:])
                return
            
            for node in graph[current[-1]]:
                current.append(node)
                backtrack(current)
                current.pop()
            
            return
        
        backtrack([0])

        return op

graph = [[1,2],[3],[3],[]]
print(Solution().allPathsSourceTarget(graph))