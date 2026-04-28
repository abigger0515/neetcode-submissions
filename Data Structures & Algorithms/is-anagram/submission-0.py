class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        # create hash table
        s_hash = {}
        for i in range(len(s)):
            s_hash[s[i]] = s_hash.get(s[i], 0) + 1
        
        # check for 0s
        for i in range(len(t)):
            if t[i] not in s_hash:
                return False
            s_hash[t[i]] -= 1

        # s_hash = {
        #     'j': 0, 'a': 0, 'm': 0
        # }
        for i in s_hash:
            if s_hash[i] != 0:
                return False

        return True