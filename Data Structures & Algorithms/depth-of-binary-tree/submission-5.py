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
        if self.recurse(root.right, height) >= self.recurse(root.left, height):
            return self.recurse(root.right, height)
        else:
            return self.recurse(root.left, height)
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.recurse(root, 0)
        