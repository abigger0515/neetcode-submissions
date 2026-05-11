class Solution:
    def isValid(self, s: str) -> bool:
        opening = []
        close_to_open = {
            '}': '{', 
            ')': '(', 
            ']': '['
        }

        for c in s:
            if opening and c in close_to_open: # open -> add to stack
                # check the last open mathes the current
                last_open = opening.pop()
                if last_open != close_to_open[c]:
                    return False 
            else:
                opening.append(c)
        return True  if not opening else False
