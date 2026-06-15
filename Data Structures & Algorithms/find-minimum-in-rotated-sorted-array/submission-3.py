class Solution:
    def findMin(self, nums: List[int]) -> int:
        if(nums[0]<nums[len(nums)-1] or len(nums)==1):
            return nums[0]
        left=0
        right =len(nums)-1
        mid=(left+right)//2
        while(left<=right):
            if nums[mid] >= nums[0]:
                left=mid+1
            else:
                right=mid-1
            mid=(left+right)//2
        return(nums[mid+1])