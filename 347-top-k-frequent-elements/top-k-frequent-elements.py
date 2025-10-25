from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c=Counter(nums)
        l=list(c.items())
        l.sort(key=lambda x:x[1],reverse=True)
        res=[]
        for i in range(k):
            res.append(l[i][0])
        return res
        