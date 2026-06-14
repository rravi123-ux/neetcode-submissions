class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        nums.sort()
        sequences=collections.defaultdict(list)
        for i in nums:
            print(i)
            if i-1 in sequences:
                sequences[i]=sequences.pop(i-1)+1
            elif i not in sequences:
                sequences[i]=1
            print(sequences)
        return max(sequences.values()) 