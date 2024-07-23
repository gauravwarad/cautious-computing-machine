import heapq
class Solution:
    def kClosest2(self, points: list[list[int]], k: int) -> list[list[int]]:
        distance = {}
        op = []
        for point in points:
            dist = point[0]**2 + point[1]**2
            if distance.get(dist):
                distance[dist].append(point)
            else:
                distance[dist] = [point]

        print(distance)
        distances = list(distance.keys())
        heapq.heapify(distances)
        print(distances)
        while k != 0:
            temp = distance[heapq.heappop(distances)]
            print("temp is - ", temp)
            for t in temp:
                op.append(t)
                k -= 1

        return op




    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        # a great solution but doesn't work for duplicate points :(
        
        op2 = []
        distance = {}
        for point in points:

            distance[tuple(point)] = point[0]**2 + point[1]**2
        
        print(distance)

        op = heapq.nsmallest(k, distance.keys(), distance.get)
        for i in op:
            op2.append(list(i))

        return op2


points = [[1,1],[1,1]]
k = 2
print(Solution().kClosest2(points, k))