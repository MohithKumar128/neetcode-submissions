class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m={}
        for i in nums:
            if i not in m:
                m[i]=0
            m[i]+=1
        result= sorted(m.items(),key = lambda x : x[1] ,reverse = True)
        return [x[0] for x in result[:k]]
        
        
           
                
