class Solution:
    def minWindow(self, s: str, t: str) -> str:
        substrings={}
        hmT={}
        for i in t:
            hmT[i]=hmT.get(i,0)+1
        for l in range(len(s)):
            hmS={}
            strBuild=""
            if s[l] in hmT:
                r=l
                while(r<len(s)):
                    if s[r] in hmT:
                        hmS[s[r]]=hmS.get(s[r],0)+1
                    strBuild=strBuild+s[r]
                    
                    isValid = True
                    for char in hmT:
                        if hmS.get(char, 0) < hmT[char]:
                            isValid = False
                            break
                    
                    if isValid:
                        substrings[strBuild]=len(strBuild)
                        break
                    r+=1
        if not substrings:
            return ""
        else:
            return min(substrings, key=substrings.get)
