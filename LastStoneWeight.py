#1046. Last Stone Weight
class Solution(object):
    def lastStoneWeight(self, stones):
        for i in range(len(stones)):
            stones[i] *= -1

        heapq.heapify(stones)


        while len(stones) > 1:
            stone_1 = heapq.heappop(stones)
            stone_2 = heapq.heappop(stones)
            if stone_1 != stone_2:
                heapq.heappush(stones, stone_1 - stone_2)

        return -heapq.heappop(stones) if stones else 0
