class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left=0
        right=len(nums)-1
        mid=(left+right)//2
        inLeft=True
        if target<nums[left]:
            inLeft=False
        while left<=right:
            if nums[mid]>=nums[0]:
                left=mid+1
            else:
                right=mid-1
            mid=(left+right)//2
        if inLeft:
            left=0
        else:
            right=len(nums)-1

        mid=(left+right)//2
        while nums[mid]!=target:
            if left>right:
                return -1
            elif nums[mid]>target:
                right=mid-1
            else:
                left=mid+1
            mid=(left+right)//2
        return mid
