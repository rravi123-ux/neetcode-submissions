class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        mid = (left+right)//2
        while(nums[mid] != target):
            if right<left:
                return -1
            elif nums[mid]<target:
                left=mid+1
                mid=(left+right)//2
            elif nums[mid]>target:
                right=mid-1
                mid=(left+right)//2
        return mid
