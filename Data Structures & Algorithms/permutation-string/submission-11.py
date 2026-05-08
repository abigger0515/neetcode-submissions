class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # sliding window
        if len(s1) > len(s2):
            return False

        s1_cnt = {}
        for c in s1:
            s1_cnt[c] = s1_cnt.get(c, 0) + 1

        l = 0 
        s2_cnt = {}
        for r in range(len(s2)):
            s2_cnt[s2[r]] = s2_cnt.get(s2[r], 0) + 1
            # shrink window (move l)
            if r - l + 1 > len(s1):
                s2_cnt[s2[l]] -= 1
                if s2_cnt[s2[l]] == 0:
                    del s2_cnt[s2[l]]
                l += 1

            if s2_cnt == s1_cnt:
                return True


        return False
