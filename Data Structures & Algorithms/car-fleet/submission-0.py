class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # the first car is the bottleneck
        # order the position with speed (p, s) in reverse order 
        # add the pair (car) to stack in reverse order 
        # calculate time to target, if faster then pop (will become the same fleet)

        p_s_pair = [[p, s] for p, s in zip(position, speed)]
        stack = []
        for p, s in sorted(p_s_pair)[::-1]:
            t = (target - p) / s
            stack.append(t)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()


        return len(stack)