class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanumStr=""
        for i in s:
            if i.isalnum():
                alphanumStr=alphanumStr+i
        alphanumStr=alphanumStr.lower()
        start=0
        end=len(alphanumStr)-1
        for i in range(len(alphanumStr)):
            if alphanumStr[start]!=alphanumStr[end]:
                return False
            start+=1
            end-=1
        return True