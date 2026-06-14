class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left=1
        right = max(piles)
        mid=(left+right)//2
        while left<=right:
            total=0
            for i in piles:
                total=(i+mid-1)//mid+total
            if total<=h:
                right=mid-1
            else:
                left=mid+1
            mid=(left+right)//2
        return left

        