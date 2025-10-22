class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        count=[['a',a],['b',b],['c',c]]
        res=[]
        while (True):

            for i in range(3):
                count.sort(key=lambda x: -x[1])
                added = False
                c,f=count[i]
                if f==0:
                    continue
                if len(res)>=2 and res[-1]==res[-2]==c:
                    continue
                res.append(c)
                count[i][1]-=1
                added=True
                break
            
            if not added:
                break
        return "".join(res)





            