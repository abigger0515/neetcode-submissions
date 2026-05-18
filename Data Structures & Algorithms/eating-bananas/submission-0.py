class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # search in candidate of eating rate
        # candidates: 1 ~ max(piles)

        l, r = 1, max(piles)
        res = r # max eating speed to finish
        while l <= r:
            k = (l + r) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(float(p)/k)

            # binary the search -> logm
            if hours <= h:
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1

        return res