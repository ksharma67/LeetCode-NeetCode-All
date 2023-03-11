"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return
        if root.right:
            if root.next is not None and root.next.left:
                root.right.next = root.next.left
            self.connect(root.right)     
            if root.left:
                root.left.next = root.right
                self.connect(root.left)
        return root
