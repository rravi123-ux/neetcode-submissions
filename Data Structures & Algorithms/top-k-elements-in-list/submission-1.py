class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm={}
        bucket=[[] for i in range(len(nums)+1)]
        for i in nums:
            hm[i]=hm.get(i,0)+1
        for num,count in hm.items():
            bucket[count].append(num)
        res=[]
        for i in range(len(bucket)-1,0,-1):
            for j in bucket[i]:
                res.append(j)
                if len(res) == k:
                    return res      
