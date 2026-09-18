# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        temp = {}
        for i, n in enumerate(inorder):
            temp[n] = i

        def recurse(pre_start, in_start, in_end):
            if in_start > in_end:
                return None

            root = TreeNode(preorder[pre_start])
            mid = temp[preorder[pre_start]]
            left_size = mid - in_start

            root.left = recurse(pre_start + 1, in_start, mid - 1)
            root.right = recurse(pre_start + 1 + left_size, mid + 1, in_end)

            return root

        return recurse(0, 0, len(inorder) - 1)
            


        