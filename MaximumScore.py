#1753. Maximum Score From Removing Stones
def maximumScore(a, b, c):
    import heapq
    l1 = []
    heapq.heapify(l1)
    for i in [a, b, c]:
        heapq.heappush(l1, -i)
        
    result = 0
    while len(l1) >= 2:
        top, top2 = heapq.nsmallest(2, l1)
        heapq.heappop(l1)
        heapq.heappop(l1)
        result -= 1
        top += 1
        top2 += 1
        if top < 0:
            heapq.heappush(l1, top)
        if top2 < 0:
            heapq.heappush(l1, top2)
    return abs(result)

res = maximumScore(2,4,6)    
print(res)
    
    
