import heapq

class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        self.kth = k
        self.stream = [num for num in nums]
        heapq.heapify(self.stream)
        while len(self.stream) > k:
            heapq.heappop(self.stream)
        print("end of init - heap length is - ", self.stream)
    def add(self, val: int) -> int:
        heapq.heappush(self.stream, val)
        while len(self.stream) > self.kth:
            heapq.heappop(self.stream)
        # temp = [-i for i in self.stream]
        # heapq.heapify(temp)
        # for _ in range(0, self.kth):
        #     op = heapq.heappop(self.stream)
        #     # print("ops are - ", op)
        return self.stream[0]
        # return heapq.nlargest(self.kth, self.stream)[-1]



# Your KthLargest object will be instantiated and called as such:
obj = KthLargest(3, [4, 5, 8, 2])
print(obj.add(3))
print(obj.add(5))
print(obj.add(10))
print(obj.add(9))
print(obj.add(4))