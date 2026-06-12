# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # can be see: on the right side or root no right side 
        res = []
        q = deque()
        q.append(root)

        while q:
            right_side = None
            q_len = len(q)
            for i in range(q_len):
                node = q.popleft()
                if node:
                    right_side = node.val
                    q.append(node.left)
                    q.append(node.right)

            if right_side:
                res.append(right_side)

        return res 
