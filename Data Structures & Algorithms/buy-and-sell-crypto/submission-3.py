class Solution:
    def maxProfit(self, prices: List[int]) -> int:
    #     [10, 1, 5, 6, 7, 1]
    # l    ^
    # r        ^
    
        l, r = 0, 1
        res = 0
        while r < len(prices):
            if prices[r] > prices[l]:
                res = max(res, prices[r] - prices[l])
            else:
                l = r
            r += 1

        return res 
        