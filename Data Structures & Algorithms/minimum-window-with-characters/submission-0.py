class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # expand r pointer to find window that contains t
        # shrink l pointer to get min window that contains t 

        if len(s) < len(t):
            return ""

        need, have = Counter(t), Counter()
        need_cnt, have_cnt = len(need), 0
        res_len = math.inf
        res = [-1, -1]

        l = 0

        for r, char in enumerate(s):
            have[char] += 1
            if char in need and have[char]==need[char]:
                have_cnt += 1
            
            while have_cnt == need_cnt:
                if r - l + 1 < res_len:
                    res_len = r - l + 1
                    res = [l, r]
                # shrink the l 
                have[s[l]] -= 1
                if s[l] in need and have[s[l]] < need[s[l]]:
                    have_cnt -= 1 
                l += 1

        if res_len == math.inf: # not found t in s
            return ""
        else:
            l, r = res
            return s[l: r+1]

            