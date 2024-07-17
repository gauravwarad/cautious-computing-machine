class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:

        left = [0,0]
        right = [len(matrix), len(matrix[0])]
        mid = [(left[0] + right[0])//2, (left[1] + right[1])//2]

        while left[0] <= right[0] and left[1] <= right[1]:
            if matrix[mid[0]][mid[1]] == target:
                return True
            elif matrix[mid[0]][mid[1]] < target:
                left[0], left[1] = mid[0], mid[1]
            else:
                right[0], right[1] = mid[0], mid[1]
            
            mid = [(left[0] + right[0])//2, (left[1] + right[1])//2]
        # something is going wrong here
        return False
    
    def searchMatrix2(self, matrix: list[list[int]], target: int) -> bool:

        left = 0
        right = len(matrix)*len(matrix[0]) - 1
        # coordinate = i//len(matrix), i%len(matrix[0])
        mid = (left + right)//2

        while left <= right:
            num = matrix[mid//len(matrix[0])][mid%len(matrix[0])]
            print("left, right, mid and num is , ", left, right, mid, mid//len(matrix),mid%len(matrix[0]), num)
            if num == target:
                return True
            elif num < target:
                left = mid + 1
            else:
                right = mid - 1
            
            mid = (left + right)//2
        return False

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 12
print(Solution().searchMatrix2(matrix, target))