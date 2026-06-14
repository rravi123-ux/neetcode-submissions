class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea=0
        barOne=0
        barTwo=len(heights)-1
        while barOne<barTwo:
            area=min(heights[barOne],heights[barTwo])*(barTwo-barOne)
            if area>maxArea:
                maxArea=area
            if heights[barOne]>heights[barTwo]:
                barTwo-=1
            elif heights[barOne]<=heights[barTwo]:
                barOne+=1
        return maxArea