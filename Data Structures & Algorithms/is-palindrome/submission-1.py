class Solution:
    def isPalindrome(self, s: str) -> bool:
        # remove special characters and make all character lower
        # reverse the string and compare
        
        s_list = []
        for c in s:
            if c.isalnum():
                s_list.append(c.lower())

        return s_list == s_list[::-1]
