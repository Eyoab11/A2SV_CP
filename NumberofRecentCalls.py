#933. Number of Recent Calls
import collections
class RecentCounter:
    def __init__(self):
        self.counter = collections.deque()
    def ping(self, t: int) -> int:
        self.counter.append(t)
        while self.counter[0] < t - 3000:
            self.counter.popleft()
        return len(self.counter)
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
