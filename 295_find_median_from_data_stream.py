import heapq
class MedianFinder:

    def __init__(self):
        self.max_heap = []
        heapq.heapify(self.max_heap)
        self.min_heap = []
        heapq.heapify(self.min_heap)

    def addNum(self, num: int) -> None:

        if len(self.max_heap) > len(self.min_heap):
            if -self.max_heap[0] > num:
                heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
                heapq.heappush(self.max_heap, -num)
            else:
                heapq.heappush(self.min_heap, num)

        elif len(self.max_heap) < len(self.min_heap):
            if self.min_heap[0] < num:
                heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
                heapq.heappush(self.min_heap, num)
            else:
                heapq.heappush(self.max_heap, -num)
        elif len(self.max_heap) == 0 and len(self.min_heap) == 0:
            heapq.heappush(self.max_heap, -num)
        else:
            if num < -self.max_heap[0]:
                heapq.heappush(self.max_heap, -num)
            else:
                heapq.heappush(self.min_heap, num)
    
    def findMedian(self) -> float:
        if len(self.min_heap) > len(self.max_heap):
            return self.min_heap[0]
        elif len(self.min_heap) < len(self.max_heap):
            return -self.max_heap[0]
        else:
            return (self.min_heap[0] - self.max_heap[0])/2



# Your MedianFinder object will be instantiated and called as such:
obj = MedianFinder()
num = 2
obj.addNum(1)
obj.addNum(2)
obj.addNum(3)
# obj.addNum(5)
print(obj.findMedian())