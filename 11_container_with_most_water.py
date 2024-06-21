class Solution:
    def maxArea(self, height: list[int]) -> int:
        
        # by brute force
        maxi = 0
        i = 0
        j = i + 1
        while i < len(height) and j < len(height):
            water = min(height[i], height[j]) * (j - i)
            if water > maxi:
                maxi = water
            j += 1
            if j == len(height):
                i += 1
                j = i + 1

        return maxi

    def maxArea2(self, height: list[int]) -> int:
        
        # by shifting the minimum height pointer
        maxi = 0
        i = 0
        j = len(height) - 1

        while i < j:
            water = min(height[i], height[j]) * (j - i)
            if water > maxi:
                maxi = water
            
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1
            print(i, height[i], j, height[j], maxi)

        return maxi

# print(Solution().maxArea2(height = [1,8,6,2,5,4,8,3,7]))

print(Solution().maxArea2(height = [1,1]))