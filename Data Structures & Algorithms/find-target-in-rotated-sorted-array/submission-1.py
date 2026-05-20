class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m 

            # determine m is at right or left part 
            if nums[m] >= nums[l]: # m is at the left part 
                if target > nums[m] or target < nums[l]: 
                    # search right in left part or in right part 
                    l = m + 1
                else:
                    r = m - 1
            else: # m at the right part 
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1


        return -1