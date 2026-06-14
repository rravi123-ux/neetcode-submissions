class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair=[(p,s) for p,s in zip(position,speed)]
        pair.sort(reverse=True)
        stack=[]
        for i in pair:
            time = (target-i[0])/i[1]
            if (stack and time > stack[-1]) or not stack:
                stack.append(time)
        return len(stack)
