# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = [0]
        def get_height(root):
            if not root:
                return 0 
            left = get_height(root.left)
            right = get_height(root.right)
            # update current max 
            res[0] = max(res[0], left+right)
            return 1 + max(left, right)

        get_height(root)

        return res[0]