import heapq

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        min_heap = []

        # push first element of each row
        for r in range(n):
            heapq.heappush(min_heap, (matrix[r][0], r, 0))

        # pop k-1 elements
        for _ in range(k - 1):
            val, r, c = heapq.heappop(min_heap)
            if c + 1 < n:
                heapq.heappush(min_heap, (matrix[r][c + 1], r, c + 1))

        return heapq.heappop(min_heap)[0]
