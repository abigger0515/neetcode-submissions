class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        res = 0
        while r < len(prices):
            l_price = prices[l]
            r_price = prices[r]

            if r_price < l_price: # find new low
                l = r
            else:
                res = max(res, r_price-l_price)
            r += 1

        return res
