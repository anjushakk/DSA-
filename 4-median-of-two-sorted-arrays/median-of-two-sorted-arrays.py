class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = []
        i, j = 0, 0
        m, n = len(nums1), len(nums2)
        
        # Merge until one array is exhausted
        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1
        
        # Add remaining elements
        while i < m:
            merged.append(nums1[i])
            i += 1
        while j < n:
            merged.append(nums2[j])
            j += 1
        
        p=(m+n)//2
        if (m+n)%2==0:
            
            return (merged[p]+merged[p-1])/2
        else:
            return merged[p]   