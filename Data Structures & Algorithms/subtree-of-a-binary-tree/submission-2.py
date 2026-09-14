# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root, subRoot):
        if subRoot is None:
            return True
        if root is None:
            return False

        # Preorder traversal, including missing children.
        def serialize(node):
            result = []
            stack = [node]

            while stack:
                node = stack.pop()

                if node is None:
                    result.append(None)
                else:
                    result.append(node.val)

                    # Stack pops left first.
                    stack.append(node.right)
                    stack.append(node.left)

            return result

        text = serialize(root)
        pattern = serialize(subRoot)

        # Build the overlap table for the smaller tree.
        lps = [0] * len(pattern)
        j = 0

        for i in range(1, len(pattern)):
            while j > 0 and pattern[i] != pattern[j]:
                j = lps[j - 1]

            if pattern[i] == pattern[j]:
                j += 1

            lps[i] = j

        # Search the larger tree's sequence.
        j = 0

        for token in text:
            while j > 0 and token != pattern[j]:
                j = lps[j - 1]

            if token == pattern[j]:
                j += 1

            if j == len(pattern):
                return True

        return False
        