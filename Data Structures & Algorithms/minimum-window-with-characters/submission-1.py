class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # edge case
        if len(s) < len(t):
            return ""

        need, have = Counter(t), Counter()
        # keep need_cnt so that we don't need to loop through need every time
        need_cnt, have_cnt = len(need), len(have)
        l = 0
        res = [-1, -1]
        res_len = math.inf
        # expand the r pointer
        for r, char in enumerate(s):
            have[char] += 1
            if char in need and have[char] == need[char]:
                have_cnt += 1

            # shrink l pointer 
            while have_cnt == need_cnt:
                # update res current length is smaller
                cur_len = r - l + 1
                if cur_len < res_len:
                    res_len = cur_len
                    res = [l, r]
                l_char = s[l]
                have[l_char] -= 1
                if l_char in need and have[l_char] < need[l_char]:
                    have_cnt -= 1
                l += 1

        l, r = res
        return "" if res_len == math.inf else s[l: r+1]
        