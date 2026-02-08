import heapq

class MedianFinder:

    def __init__(self):
        self.small = []   # max heap (store negatives)
        self.large = []   # min heap

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -num)

        # ensure ordering
        if self.small and self.large and (-self.small[0] > self.large[0]):
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # rebalance: large too big
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)

        # rebalance: small too big (THIS WAS MISSING)
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)

    def findMedian(self) -> float:
        if len(self.small) == len(self.large):
            return (-self.small[0] + self.large[0]) / 2
        if len(self.small) > len(self.large):
            return float(-self.small[0])
        else:
            return float(self.large[0])
