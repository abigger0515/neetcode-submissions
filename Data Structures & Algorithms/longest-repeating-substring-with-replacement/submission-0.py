class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
    #     X Y Y X
    #     ^
    #           ^
    #  k  2 1 0 0
    #     1 2 3 4


    #     A A A B A B B
    #     ^
    #             ^
    #  k. 1     0
    #         3 4 5

    #     A A A B A B B B B B -> 7 
    #           ^
    #                 ^
    # k.  1

    # A.  1 2 3 3 4 4 4 4
    # B.        1   2 3 4 

        # 2 pointers
        l = 0
        res = 0
        char_cnt = {}

        for r in range(len(s)):
            char_cnt[s[r]] = char_cnt.get(s[r], 0) + 1
            # condition: window_length - most_common_cnt <= k
            while (r-l+1) - max(char_cnt.values()) > k:
                # shrink size of window until valid
                char_cnt[s[l]] -= 1
                l += 1

            res = max(res, r-l+1)

        return res
