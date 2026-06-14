class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hm={}
        for i in s1:
            hm[i]=hm.get(i,0)+1
        print(hm)
        for left in range(len(s2)-len(s1)+1):
            counts={}
            if s2[left] in hm:
                right = left
                while (right<=len(s2)-1) and s2[right] in hm:
                    counts[s2[right]]=counts.get(s2[right],0)+1
                    if(counts==hm):
                        return True
                    print(counts)
                    right+=1
            
        return False