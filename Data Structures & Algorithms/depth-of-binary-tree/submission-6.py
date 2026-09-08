# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def recurse(self, root, height):
        if root == None:
            return height
        else:
            height +=1
        right = self.recurse(root.right, height)
        left = self.recurse(root.left, height)
        if right > left:
            return right
        return left
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.recurse(root, 0)
        