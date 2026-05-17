class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # find in row 
        # search in col

        # flatten the O(n)
        nums = []
        for rows in matrix:
            nums += rows
        l, r = 0, len(nums) - 1
        while r >= l:
            mid = (l + r) // 2
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                return True

        return False 