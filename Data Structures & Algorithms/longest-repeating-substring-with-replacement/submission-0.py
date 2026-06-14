class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts={}
        res=0
        left=0
        for right in range(len(s)):
            counts[s[right]]=counts.get(s[right],0)+1
            while (right-left+1)-max(counts.values())>k:
                counts[s[left]]-=1
                left+=1
            res=max(res,right-left+1)
        return res

