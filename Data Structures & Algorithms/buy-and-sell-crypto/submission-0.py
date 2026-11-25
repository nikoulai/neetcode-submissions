class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_profit = 0 

        b_price = prices[0]

        for i in range(0,len(prices)):
         
            max_profit = max(max_profit,prices[i]-b_price)

            if b_price > prices[i]:
                b_price = prices[i]

        return max_profit