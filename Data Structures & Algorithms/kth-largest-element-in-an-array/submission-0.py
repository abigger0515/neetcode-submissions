class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        # 1 2 3 4 5
        # 5-2
        return nums[len(nums)-k]