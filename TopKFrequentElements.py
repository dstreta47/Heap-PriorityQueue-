#347. Top K Frequent Elements
from collections import Counter
class Solution(object):
    import heapq
    def topKFrequent(self, nums, k):
        count = Counter(nums)
        return heapq.nlargest(k,count.keys(), key =count.get)
        
