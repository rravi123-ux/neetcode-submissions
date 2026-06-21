class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1)>len(nums2):
            temp=nums1
            nums1=nums2
            nums2=temp
        total=(len(nums1)+len(nums2))//2
        left=0
        right=len(nums1)-1
        mid=(left+right)//2
        otherMid=total-(mid+2)
        while True:
            left1=nums1[mid] if mid>=0 else float("-inf")
            right1=nums1[mid+1] if mid+1<len(nums1) else float("inf")
            left2=nums2[otherMid] if otherMid>=0 else float("-inf")
            right2=nums2[otherMid+1] if otherMid+1<len(nums2) else float("inf")
            if(left1<=right2 and left2<=right1):
                break
            if(left1>right2):
                right=mid-1
            else:
                left=mid+1
            mid=(left+right)//2
            otherMid=total-(mid+2)
        if(len(nums1)+len(nums2)) % 2 == 0:
            return (max(left1,left2)+min(right1,right2))/2
        else:
            return min(right1,right2)

  

        