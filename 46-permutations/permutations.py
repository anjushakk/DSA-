from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        
        def backtrack(start):
            if start == n:
                res.append(nums[:])  # make a copy
                return
            
            for i in range(start, n):
                nums[start], nums[i] = nums[i], nums[start]  # swap
                backtrack(start + 1)
                nums[start], nums[i] = nums[i], nums[start]  # backtrack
        
        backtrack(0)
        return res
