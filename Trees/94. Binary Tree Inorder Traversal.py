# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ll=[]
        def tr(root):
            if root==None:
                return 
            
            tr(root.left)
            ll.append(root.val)
            tr(root.right)
            return ll
        return tr(root)
