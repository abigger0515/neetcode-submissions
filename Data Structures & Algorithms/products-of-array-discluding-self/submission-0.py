class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # [1,          2,        4,            6]

        #  1*()*(2*4*6), 1*(1)*(4*6), 1*(1*2)*6,    1*(1*2*4)*()
        n = len(nums)
        pref = [0] * n # [1, 1, 1, 1]
        pref[0] = 1
        for i in range(1, n):
            pref[i] = pref[i-1]*nums[i-1]
        # print(pref) # [1, 1, 1*2, 1*2*4]

        suff = [0] * n
        suff[-1] = 1
        for i in range(n-2, -1, -1):
            suff[i] = suff[i+1] * nums[i+1]
        # print(suff) # []

        res = []
        for i in range(n):
            res.append(pref[i] * suff[i])
        return res

