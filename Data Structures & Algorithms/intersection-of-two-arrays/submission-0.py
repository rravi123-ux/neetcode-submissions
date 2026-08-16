class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        seen=set()
        res=[]
        for i in nums1:
            seen.add(i)
        for i in nums2:
            if i in seen and i not in res:
                res.append(i)
        return res