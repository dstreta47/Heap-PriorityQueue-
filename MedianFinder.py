class MedianFinder(object):

    def __init__(self):
        self.first = [] #max heap, to get the largest item in the first half
        self.second = [] #min heap, to get the smallest item in the second half
        

    def addNum(self, num):
        heapq.heappush(self.first, -num)
        heapq.heappush(self.second, -(heapq.heappop(self.first)))
        if len(self.first) < len(self.second):
            heapq.heappush(self.first, -(heapq.heappop(self.second)))
        

    def findMedian(self):
        if len(self.first) > len(self.second):
            return -(self.first[0])
        else:
            return (float(-(self.first[0]))+float(self.second[0]))/2
