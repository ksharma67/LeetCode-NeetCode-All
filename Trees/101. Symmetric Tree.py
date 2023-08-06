# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root.left is None and root.right is None:
            return True
        def sym(l,r):
            if l is None and r is None:
                return True
            if l is None or r is None:
                return False
            return l.val == r.val and sym(l.left,r.right) and sym(l.right,r.left)
        return sym(root,root)

            
                    
            
                
