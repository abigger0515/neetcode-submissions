class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # (index, temp)

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][1]: # found warmer
                prev_id, prev_t = stack.pop()
                res[prev_id] = i - prev_id

            stack.append((i, t))

        return res
            