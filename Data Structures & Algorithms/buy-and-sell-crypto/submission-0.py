class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minBuy=prices[0]
        maxProfit=0
        j=0
        for i in range(1,len(prices)):
            if prices[j] < minBuy:
                minBuy=prices[j]
            profit=prices[i]-minBuy
            if profit>maxProfit:
                maxProfit=profit
            j+=1
        return maxProfit
        