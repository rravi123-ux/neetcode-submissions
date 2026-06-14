class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        for i in range(len(nums)):
            match = target - nums[i]
            if match in hm:
                return [hm[match],i]
            hm[nums[i]]=i
            