#451. Sort Characters By Frequency
import heapq

class PrioritryQueue:
    def __init__(self):
        self._queue = []
        self._index = 0
    
    def push(self, item):
        heapq.heappush(self._queue, (-item[1], self._index, item))
        self._index += 1
        
    def pop(self):
        return heapq.heappop(self._queue)[-1]

    
class Solution:
    def frequencySort(self, s):
        setChar = set(s)

        if len(setChar) == len(s):
            return s
        
        q = PrioritryQueue()
        
        for char in setChar:
            charCount = s.count(char)
            q.push((char, charCount))
            
        res = ''
        
        for _ in range(0, len(setChar)):
            char, count = q.pop()
            res += char*count
        
        return res
        
