class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 10 1 5 6 7 1
        # ^ 
        #    ^ 4 5 6 0  
        
        # 10 8 7 5 2
        # ^ 
        #   ^ 
        #      ^ 
        #        ^
        #          ^

        # move forward when lower then current 

        res = 0 

        l, r = 0, 1
        while r < len(prices):
            if prices[r] > prices[l]:
                profit = prices[r] - prices[l]
                res = max(res, profit)
            else:
                l = r
            r += 1
        return res