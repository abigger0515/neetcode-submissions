class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 2 pointers
        l = 0
        res = 0
        seen = set()
        for r, r_ch in enumerate(s):
            # remove items until no dups
            while r_ch in seen:
                seen.remove(s[l])
                l += 1
            # keep track of cur max length
            seen.add(r_ch)
            res = max(res, r-l+1)

        return res

