import math
class Solution:
    def minSpeedOnTime(self, dist: list[int], hour: float) -> int:
        
        def check_speed(speed):
            time = 0
            for d in dist[:-1]:
                time = time + math.ceil(d/speed)
            time = time + dist[-1]/speed
            print("speed and time are - ", speed, time)
            return time <= hour
        left = 1
        right = max(dist)*hour*600 # or 10**7
        possible = False
        while left <= right:
            mid = (left + right)//2
            print("left, right, mid are - ", left, right, mid)
            if check_speed(mid):
                right = mid - 1
                possible = True

            else:
                left = mid + 1
        if possible:
            return left
        else:
            return -1


# dist = [1,3,2]
# hour = 6

# dist = [1,3,2]
dist = [1,1,100000]
hour = 2.01
print(Solution().minSpeedOnTime(dist, hour))