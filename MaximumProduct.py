#1464. Maximum Product of Two Elements in an Array
class Solution(object):
    def maxProduct(self, nums):   
        my_heap = []
        heapq.heapify(my_heap)
        for num in nums:
            if len(my_heap) < 2:
                heapq.heappush(my_heap, num)
            else:
                heapq.heappush(my_heap, num)
                heapq.heappop(my_heap)
        
        return (heapq.heappop(my_heap)-1) * (heapq.heappop(my_heap)-1)
