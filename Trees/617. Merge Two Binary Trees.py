# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = [(root1, root2)]
        
        if not root1:
            return root2
        if not root2:
            return root1
        
        root1.val += root2.val

        while queue:
            node1, node2 = queue.pop(0)
            
            if node2:
                if node2.right:
                    if not node1.right:
                        node1.right = node2.right
                    else:
                        node1.right.val += node2.right.val
                        queue.append((node1.right, node2.right))
                if node2.left:
                    if not node1.left:
                        node1.left = node2.left
                    else:
                        node1.left.val += node2.left.val
                        queue.append((node1.left, node2.left))
        return root1                
