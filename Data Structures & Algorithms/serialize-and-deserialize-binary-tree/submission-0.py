# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        q = collections.deque()
        q.append(root)
        result = []

        while q:
            temp = q.popleft()
            if temp:
                result.append(str(temp.val))
                q.append(temp.left)
                q.append(temp.right)
            else:
                result.append("null")

        return ";".join(result)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        values = data.split(";")
        if values[0] == "null":
            return None
        root = TreeNode(int(values[0]))
        q = collections.deque([root])
        i = 1
        while q:
            cur = q.popleft()
            if values[i] != "null":
                cur.left = TreeNode(int(values[i]))
                q.append(cur.left)
            i += 1
            if values[i] != "null":
                cur.right = TreeNode(int(values[i]))
                q.append(cur.right)
            i += 1
            

        return root



