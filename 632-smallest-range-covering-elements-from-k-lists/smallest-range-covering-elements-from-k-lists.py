import heapq
from typing import List

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        heap = []
        curr_max = float('-inf')
        for i in range(len(nums)):
            heapq.heappush(heap, (nums[i][0], i, 0))
            curr_max = max(curr_max, nums[i][0])
        
        mindiff = float('inf')
        best_range = [0, 0]
        
        while heap:
            val, i, j = heapq.heappop(heap)
            currdiff = curr_max - val
            if currdiff < mindiff:
                mindiff = currdiff
                best_range = [val, curr_max]
            
            if j + 1 == len(nums[i]):
                break
            
            next_val = nums[i][j + 1]
            heapq.heappush(heap, (next_val, i, j + 1))
            curr_max = max(curr_max, next_val)
        
        return best_range
