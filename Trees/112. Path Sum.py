# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
    if not root: return False
    targetSum -= root.val
    return not (targetSum or root.left or root.right) or \
           self.hasPathSum(root.left, targetSum) or \
           self.hasPathSum(root.right, targetSum)
    
