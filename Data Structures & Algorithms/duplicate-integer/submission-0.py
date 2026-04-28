class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        cnt = {}
        for i in nums:
            cnt[i] = cnt.get(i, 0) + 1
            
            if cnt[i] > 1:
                return True

        return False