class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        firstNum=0
        secondNum=len(numbers)-1
        while firstNum < secondNum:
            if numbers[firstNum]+numbers[secondNum]>target:
                secondNum-=1
            elif numbers[firstNum]+numbers[secondNum]<target:
                firstNum+=1
            else:
                return [firstNum+1,secondNum+1]
        return []