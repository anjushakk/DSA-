from typing import List

# Standard binary search
def binary_search(nums, left, right, target):
    while left <= right:
        mid = (left + right)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Find pivot using linear scan (single for loop)
def find_pivot(nums):
    n = len(nums)
    for i in range(1, n):
        if nums[i] < nums[i-1]:
            return i  # pivot found
    return 0  # array not rotated

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        
        pivot = find_pivot(nums)
        
        # Search in left part [0, pivot-1]
        index = binary_search(nums, 0, pivot-1, target)
        if index != -1:
            return index
        
        # Search in right part [pivot, n-1]
        return binary_search(nums, pivot, len(nums)-1, target)
