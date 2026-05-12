class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        summ = 0
        for i in range(len(prices) - 1):
            for j in range(i + 1,len(prices)):
                #take the max of the new difference and the old summ
                summ = max(summ,prices[j] - prices[i])
        return summ