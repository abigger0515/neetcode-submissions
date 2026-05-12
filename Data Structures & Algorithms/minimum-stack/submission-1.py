class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = [] # record min for each stack element

    def push(self, val: int) -> None:
        self.stack.append(val)
        cur_min = min(val, self.min_stack[-1] if self.min_stack else val)
        # if self.min_stack:
        #     cur_min = min(val, self.min_stack[-1])
        # else:
        #     cur_min = val
        self.min_stack.append(cur_min)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
        
