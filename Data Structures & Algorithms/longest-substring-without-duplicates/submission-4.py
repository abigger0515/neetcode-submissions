class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
    #     z x y z x y z
    #   l   ^
    #   r       ^     
        l = 0
        res = 0
        seen = set()
        
        for r, ch in enumerate(s):
            while ch in seen: # keep shrinking until the duplicate char removed
                seen.remove(s[l])
                l += 1
            seen.add(ch)
            res = max(res, r - l + 1)

        return res
