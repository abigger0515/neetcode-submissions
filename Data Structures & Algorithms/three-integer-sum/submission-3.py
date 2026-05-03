class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []
        for i in range(len(nums)):
            # handle same first value
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = 0-nums[i]
            # print(i)
            l, r = i+1, len(nums)-1
            while l < r:
                cur_sum = nums[l] + nums[r]
                if cur_sum < target:
                    l += 1
                elif cur_sum > target:
                    r -= 1
                else:
                    # print(nums[i], nums[l], nums[r])
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l-1] and l<r:
                        l+=1

        return res
