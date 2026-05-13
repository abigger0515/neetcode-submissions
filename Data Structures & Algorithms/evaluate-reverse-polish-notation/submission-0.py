class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t == '+':
                stack.append(stack.pop() + stack.pop())
            elif t == '-':
                p1, p2 = stack.pop(), stack.pop()
                stack.append(p2 - p1)
            elif t == '*':
                stack.append(stack.pop() * stack.pop())
            elif t == '/':
                p1, p2 = stack.pop(), stack.pop()
                stack.append(int(float(p2) / p1))
            else:
                stack.append(int(t))
        return stack.pop()