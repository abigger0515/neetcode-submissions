class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque() # stores index
        res = []
        for r in range(len(nums)):
            # decreasing queue 
            # value smaller then incoming is no longer useful
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)
            
            # make sure the current is in bound
            l = r + 1 - k
            if q[0] < l:
                q.popleft()

            # the first in the queue would be the max of current bound
            if l >= 0:
                res.append(nums[q[0]])

        return res 