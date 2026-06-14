class Solution:
    def trap(self, height: List[int]) -> int:
        total=0
        l=0
        r=len(height)-1
        lMax=height[l]
        rMax=height[r]
        while l<r:
            if lMax < rMax:
                l+=1
                lMax=max(lMax,height[l])
                total+=lMax-height[l]
            else:
                r-=1
                rMax=max(rMax,height[r])
                total+=rMax-height[r]
        return total