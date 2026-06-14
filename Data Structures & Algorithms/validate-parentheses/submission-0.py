class Solution:
    def isValid(self, s: str) -> bool:
        matches={")":"(","}":"{","]":"["}
        stack=[]
        for i in s:
            if i not in matches:
                stack.append(i)
            else:
                if stack and matches[i]==stack[-1]:
                    stack.pop()
                else:
                    return False
        if stack:
            return False
        else:
            return True
        