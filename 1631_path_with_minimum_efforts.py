class Solution:
    def minimumEffortPath(self, heights: list[list[int]]) -> int:
    # dfs with binary search -- not the ideal way here, but somehow manages to run
    
        def check_path(effort):
            visited = set()
            next_stack = []

            directions = [(1,0), (0,1), (-1,0), (0,-1)]
            i = len(heights)
            j = len(heights[0])
            x, y = 0, 0
            while x != i and y != j:
                visited.add((x, y))
                if x == i-1 and y == j-1:
                    return True
                for direction in directions:
                    if 0 <= x + direction[0] < i and 0 <= y + direction[1] < j:
                        if abs(heights[x+ direction[0]][y+ direction[1]] - heights[x][y]) <= effort:
                            if x + direction[0] == i-1 and y + direction[1] == j-1:
                                return True
                            if (x+direction[0], y+direction[1]) not in visited:
                                next_stack.append((x+direction[0], y+direction[1]))
                if next_stack:
                    temp = next_stack.pop()
                    x = temp[0]
                    y = temp[1]
                else:
                    break
            return False

        left = 0
        right = max([max(height) for height in heights])
        
        
        while left <= right:
            mid = (left + right)//2
            if check_path(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left

# heights = [[1,2,2],[3,8,2],[5,3,5]]
heights = [[3]]
print(Solution().minimumEffortPath(heights))