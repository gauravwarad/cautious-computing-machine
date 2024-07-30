from collections import deque
class Solution:
    def canReach(self, arr: list[int], start: int) -> bool:
        # not working for a few test cases - reason unknown.


        # dfs - recursion
        
        visited = [-1]*len(arr)
        
        def dfs(x):
            print("x and arr[x] ", x, arr[x])
            if arr[x] == 0:
                return True
            
            # possible choices = i - arr[i] or i + arr[i]
            op = False
            if 0 <= x-arr[x] and x-arr[x] < len(arr) and visited[x-arr[x]] == -1:
                print("\t 1 going for dfs of - ", x-arr[x])
                op = op or dfs(x-arr[x])
                visited[x-arr[x]] = 1
            if op:
                return True
            if 0 <= x + arr[x] and x+arr[x] < len(arr) and visited[x+arr[x]] == -1:
                print("\t 2 going for dfs of - ", x+arr[x])
                op = op or dfs(x+arr[x])
                visited[x+arr[x]] = 1
            return op
        visited[start] = 1
        ans = dfs(start)

        print(visited)
        return ans

    def canReach2(self, arr: list[int], start: int) -> bool:
        # following the leetcode method
        def dfs(x): # x is the start node
            if 0 <= x < len(arr):
                if arr[x] == 0:
                    return True
                if arr[x] > 0:
                    arr[x] = -arr[x] # making the value -ve to mark it as visited
                    return dfs(x+arr[x]) or dfs(x-arr[x])
                # return False
            return False
        return dfs(start)

    def canReach3(self, arr, start):
        # bfs?

        queua = deque()
        queua.append(start)
        visited = [-1]*len(arr)

        while len(queua) > 0:
            
            current = queua.popleft()
            if arr[current] == 0:
                return True
            
            if 0 <= current - arr[current] < len(arr) and visited[current-arr[current]] == -1:
                queua.append(current - arr[current])
                visited[current - arr[current]] = 1
            
            if 0 <= current + arr[current] < len(arr) and visited[current + arr[current]] == -1:
                queua.append(current + arr[current])
                visited[current + arr[current]] = 1
        
        return False
# arr = [4,2,3,0,3,1,2]
# start = 5
arr = [4,2,3,0,3,1,2]
# start = 0
# arr = [1,1,1,1,1,1,1,1,0]
start = 5
print(Solution().canReach3(arr, start))