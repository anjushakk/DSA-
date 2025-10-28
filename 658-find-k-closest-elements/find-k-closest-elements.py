import heapq

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        max_heap = []

        for num in arr:
            diff = abs(num - x)
            heapq.heappush(max_heap, (-diff, -num))  # store negative to make max-heap
            if len(max_heap) > k:
                heapq.heappop(max_heap)  # pop farthest element

        result = [-num for _, num in max_heap]
        return sorted(result)
