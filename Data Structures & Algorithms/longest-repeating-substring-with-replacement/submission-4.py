class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # valid window: current_len - max(count) <= k

        s_cnt = {}
        l = 0
        res = 0

        for r in range(len(s)):
            s_cnt[s[r]] = s_cnt.get(s[r], 0) + 1
            # if window not valid
            while (r-l+1) - max(s_cnt.values()) > k:
                s_cnt[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)

        return res