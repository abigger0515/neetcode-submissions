class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # 2 pointers
        l = 0
        res = 0
        char_cnt = {}
        most_common = 0

        for r in range(len(s)):
            char_cnt[s[r]] = char_cnt.get(s[r], 0) + 1
            most_common = max(most_common, char_cnt[s[r]])
            # valid window: window_length - most_common_cnt <= k
            while (r-l+1) - most_common > k:
                # shrink size of window until valid
                char_cnt[s[l]] -= 1
                l += 1

            res = max(res, r-l+1)

        return res
