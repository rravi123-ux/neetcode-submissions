class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hm={}
        for i in s:
            if i in hm:
                hm[i]=hm.get(i)+1
            else:
                hm[i]=1
        for i in t:
            if i not in hm:
                return False
            else:
                hm[i]=hm.get(i)-1
        for i in hm:
            if hm.get(i)!=0:
                return False
        return True

                