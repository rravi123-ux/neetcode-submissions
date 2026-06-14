class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        bottom=0
        top=len(matrix)-1
        mid=(bottom+top)//2
        row=matrix[mid]
        while(row[0]>target or row[-1]<target):
            if bottom>top:
                return False
            elif target>row[-1]:
                bottom=mid+1
                mid=(bottom+top)//2
                row=matrix[mid]
            elif target<row[-1]:
                top=mid-1
                mid=(bottom+top)//2
                row=matrix[mid]
            else:
                break
        left=0
        right=len(row)-1
        mid=(left+right)//2
        while(row[mid]!=target):
            if left>right:
                return False
            elif target>row[mid]:
                left=mid+1
                mid=(left+right)//2
            elif target<row[mid]:
                right=mid-1
                mid=(left+right)//2
        return True


        