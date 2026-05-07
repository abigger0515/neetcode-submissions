class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # valid window: current_len - max(count) <= k

        s_cnt = {}
        l = 0
        res = 0
        max_f = 0

        for r in range(len(s)):
            s_cnt[s[r]] = s_cnt.get(s[r], 0) + 1
            max_f = max(max_f, s_cnt[s[r]])
            # if window not valid
            while (r-l+1) - max_f > k:
                s_cnt[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)

        return res