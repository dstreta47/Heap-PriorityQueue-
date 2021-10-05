#215. Kth Largest Element in an Array
class Solution(object):
    def findKthLargest(self, nums, k):
        return heapq.nlargest(k,nums)[-1]
