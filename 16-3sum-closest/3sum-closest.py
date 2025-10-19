class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        csum=0
        mindiff=float('inf')
        res=0
        for i in range(0,len(nums)-2):
            left=i+1
            right=len(nums)-1
            while left<right:
                csum=nums[i]+nums[left]+nums[right];
                diff=abs(target-csum)
                if diff<mindiff:
                    mindiff=diff
                    res=csum
                if target<csum:
                    right-=1
                elif target>csum:
                    left+=1
                else:
                    return csum
            


        return res
        

        