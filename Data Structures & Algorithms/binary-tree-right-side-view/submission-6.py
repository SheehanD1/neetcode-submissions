# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        result = []
        q = collections.deque()
        q.append(root)

        while q:
            for i in range(len(q) - 1):
                node = q.popleft()
                if node:
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            node2 = q.popleft()
            if node2:
                result.append(node2.val)
                if node2.left:
                    q.append(node2.left)
                if node2.right:
                    q.append(node2.right)
        return result

