# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        result = 0
        stack = [(root, root.val)]

        while stack:
            node, biggest_so_far = stack.pop()
            if node.val >= biggest_so_far:
                result += 1
                biggest_so_far = node.val
            if node.right: 
                stack.append((node.right, biggest_so_far))
            if node.left:
                stack.append((node.left, biggest_so_far))
        return result

        