class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm=defaultdict(list)
        for i in strs:
            count=[0]*26
            for j in i:
                count[ord(j)-ord('a')]+=1
            hm[tuple(count)].append(i)
        return list(hm.values())