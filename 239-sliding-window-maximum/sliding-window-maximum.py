class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or k==0:
            return []
        heap=[]
        res=[]
        for i, num in enumerate(nums):
            heapq.heappush(heap,(-num,i))

            if i>=k-1:
                while heap[0][1]<=i-k:
                    heapq.heappop(heap)
                res.append(-heap[0][0])
        return res
            
        