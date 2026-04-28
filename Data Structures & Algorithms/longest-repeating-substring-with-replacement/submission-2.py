class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # longest -> largest window
        # valid window: replacement time <= k
        # replacement time = window_length - most_common

        l = 0
        res = 0
        count = {}

        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1

            while (r-l+1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1

            res = max(res, r-l+1)
        
        return res