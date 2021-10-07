#1338. Reduce Array Size to The Half

import collections
import heapq

class Solution(object):
    def minSetSize(self, arr):
        freq = collections.Counter(arr)
        heap = []
        for key, values in freq.items():
            heap.append((-1*values, key))
        heapify(heap)
        
        size = len(arr)
        length = size
        
        for i in range(len(heap)):
            occ = -1*heappop(heap)[0]
            length = length - occ
            if length <= size/2:
                return i+1        
        
        
