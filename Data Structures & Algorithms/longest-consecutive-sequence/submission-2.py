class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=set(nums)
        longest=0
        for i in nums:
            if i-1 not in nums:
                length=1
                while i+1 in nums:
                    i+=1
                    length+=1
                if length>longest:
                    longest=length
        return longest