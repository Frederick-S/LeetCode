class Node:
    def __init__(self, val: int = 0, left: 'Node' = None,
                 right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: Node) -> Node:
        if not root:
            return None

        if root.left:
            root.left.next = root.right

        if root.right:
            root.right.next = root.next.left if root.next else None

        self.connect(root.left)
        self.connect(root.right)

        return root
