import heapq
class SmallestInfiniteSet:

    def __init__(self):
        self.li = []
        for i in range(1, 1001):
            heapq.heappush(self.li, i)

    def popSmallest(self) -> int:
        heapq.heappop(self.li, self.li[0])

    def addBack(self, num: int) -> None:
        heapq.heappush(self.li, int)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)