#1337. The K Weakest Rows in a Matrix
class Solution(object):
    def kWeakestRows(self, mat, k):
        m = len(mat)
        n = len(mat[0])

        def binary_search(row):
            low = 0
            high = n
            while low < high:
                mid = low + (high - low) // 2
                if row[mid] == 1:
                    low = mid + 1
                else:
                    high = mid
            return low
        pq = []
        for i, row in enumerate(mat):
            strength = binary_search(row)
            entry = (-strength, -i)
            if len(pq) < k or entry > pq[0]:
                heapq.heappush(pq, entry)
            if len(pq) > k:
                heapq.heappop(pq)
        indexes = []
        while pq:
            strength, i = heapq.heappop(pq)
            indexes.append(-i)

        indexes = indexes[::-1]

        return indexes
