# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> list[int]:

        def dfs(node):
            if not node: return

            ans.append(node.val)

            dfs(node.left)
            dfs(node.right)
  
            return   
        
        ans = []
        
        dfs(root)

        return ans
