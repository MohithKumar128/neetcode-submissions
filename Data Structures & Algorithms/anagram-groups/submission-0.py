class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m={}
        for i in strs:
            key= ''.join(sorted(i))
            if key not in m :
                m[key]=[]
            m[key].append(i)
        return list(m.values())

        

        