from collections import deque
class RecentCounter:

    def __init__(self):
        req = 0
        self.queua = deque()

    def ping(self, t: int) -> int:
        self.queua.append(t)
        start_time = t - 3000
        print("start time is , ", start_time)
        i = 0
        while i < len(self.queua):
            if self.queua[i] < start_time:
                self.queua.popleft()
            else:
                break
        print(self.queua)
        return len(self.queua)


# Your RecentCounter object will be instantiated and called as such:
obj = RecentCounter()
print(obj.ping(1))
print(obj.ping(100))
print(obj.ping(3000))
print(obj.ping(4000))