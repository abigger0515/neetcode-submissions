# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.cnt = k
        self.res = 0 
        
        def in_order(node):
            if not node:
                return

            in_order(node.left)
            self.cnt -= 1
            if self.cnt == 0:
                self.res = node.val
                return
            in_order(node.right)

        in_order(root)
        return self.res
