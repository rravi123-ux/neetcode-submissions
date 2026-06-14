class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left=[1]
        right=[1]
        res=[]
        for i in range(len(nums)-1):
            left.append(left[len(left)-1]*nums[i])
        for i in range(len(nums)-1,0,-1):
            right.append(right[len(right)-1]*nums[i])
        right=right[::-1]
        for i in range(len(nums)):
            res.append(left[i]*right[i])
        return res