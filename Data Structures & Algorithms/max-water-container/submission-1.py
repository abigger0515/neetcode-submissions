class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # area = short * (l-r)
        l, r = 0, len(heights)-1
        max_area = 0
        while l < r:
            cur_area = min(heights[l], heights[r])*(r-l)
            max_area = max(cur_area, max_area)
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return max_area