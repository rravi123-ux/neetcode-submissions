class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="":
            return ""
        countT={}
        window={}
        for i in t:
            countT[i]=countT.get(i,0)+1
        have=0
        need=len(countT)
        res=[-1,-1]
        resLen=float("infinity")
        l=0
        for r in range(len(s)):
            elem = s[r]
            window[elem]=1+window.get(elem,0)
            if elem in countT and window[elem]==countT[elem]:
                have+=1
            while have == need:
                if(r-l+1)<resLen:
                    resLen=r-l+1
                    res=[l,r]
                window[s[l]]-=1
                if s[l] in countT and window[s[l]]<countT[s[l]]:
                    have-=1
                l+=1
        if resLen!=float("infinity"):
            return s[res[0]:res[1]+1]
        else:
            return ""