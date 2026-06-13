# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def dfs(node, minn, maxx):
            if not node:
                return True  

            if not (node.val > minn and node.val < maxx):
                return False 

            return (
                dfs(node.left, minn, node.val) and # go left: update max
                dfs(node.right, node.val, maxx)    # go right: update min
            )

        return dfs(root, -math.inf, math.inf)

            