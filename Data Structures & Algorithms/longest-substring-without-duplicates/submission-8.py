class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # zxyzxyz
        #  ^  ^
        #    ^ ^ z already in cur_set 
        #        ^
        # set1: (z, x, y) len: 3
        # set2: (z, x, y) len: 3
        # set3: (z) len: 1
        longest = 0
        char_set = set()
        l = 0
        for r in range(len(s)):
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1
            char_set.add(s[r])
            longest = max(longest, len(char_set))

        return longest

