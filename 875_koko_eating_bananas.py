import math

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        
        def check_speed(speed):
            time = 0
            for i in piles:
                time = time + math.ceil(i/speed)
            print("time required and speed is, ", time, speed)
            return time

        left = 1
        right = max(piles)

        # mid = (left + right)//2

        while left <= right:
            mid = (left + right)//2
            print("left, right, mid are - ", left, right, mid)
            if check_speed(mid) <= h:
                right = mid - 1
            else:
                left = mid + 1

        return left

# piles = [3,6,7,11]
# h = 8
piles = [30,11,23,4,20]
h = 6
print(Solution().minEatingSpeed(piles, h))
