class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        mymap=dict()
        for s in strs:
            if tuple(sorted(s)) not in mymap:
                mymap[tuple(sorted(s))]=[]
            mymap[tuple(sorted(s))].append(s)
        return list(mymap.values())


        