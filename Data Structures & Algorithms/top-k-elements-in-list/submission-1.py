class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hm={}
        for num in nums:
            hm[num]=hm.get(num,0)+ 1
        sorted_items=sorted(hm.items(), key=lambda x:x[1],reverse=True)
        res=[]
        for value, count in sorted_items[:k]:
                res.append(value)
        return res
            