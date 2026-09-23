# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        result = root.val

        def dfs(root):
            nonlocal result

            if not root:
                return 0

            lmax = dfs(root.left)
            rmax = dfs(root.right)
            lmax = max(lmax, 0)
            rmax = max(rmax, 0)

            result = max(result, root.val + lmax + rmax)

            return root.val + max(lmax, rmax)

        dfs(root)
        return result