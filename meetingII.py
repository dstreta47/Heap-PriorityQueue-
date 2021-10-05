class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:x[0])
        freetime = []
        heapq.heappush(freetime,intervals[0][1])
        for i in intervals[1:]:
            if freetime[0]<=i[0]:
                heapq.heappop(freetime)
            heapq.heappush(freetime,i[1])
        return len(freetime) 
