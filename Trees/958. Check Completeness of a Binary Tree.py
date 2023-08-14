# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        queue = [root]
        while queue[0] is not None:
            node = queue.pop(0)
            queue.append(node.left)
            queue.append(node.right)
        return all([n is None for n in queue]) 
