class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        
        # binary search within a 2D matrix
        l, r = 0, rows * cols - 1

        while l <= r:
            mid = (l + r) // 2
            mid_row = mid // cols # which row 
            mid_col = mid % cols  # which one in the row
            mid_val = matrix[mid_row][mid_col]

            if mid_val < target:
                l = mid + 1
            elif mid_val > target:
                r = mid - 1
            else:
                return True

        return False