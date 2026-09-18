# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        ans = 0
        def inOrder(root):
            nonlocal count
            nonlocal ans
            if not root:
                return None
            inOrder(root.left)
            count += 1

            if count == k:
                ans = root.val
            elif count < k: 
                inOrder(root.right)
        
        inOrder(root)
        return ans



        
