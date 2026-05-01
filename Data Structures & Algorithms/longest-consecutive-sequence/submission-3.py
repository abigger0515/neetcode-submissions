class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_length = 0
        for n in nums:
            # check if it's a start of a sequence
            if n-1 not in nums_set:
                length = 0
                while n+length in nums_set: 
                    length += 1
                # update max_length when a sequence finished
                max_length = max(length, max_length)

        return max_length