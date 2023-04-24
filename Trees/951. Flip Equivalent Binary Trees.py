# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
	    lru_cache(None)
	    def dfs(n1, n2):
		    if not(n1 or n2):
			    return True
		    if not(n1 and n2) or n1.val != n2.val:
			    return False
		    if((n1.left and n2.left) or (n1.right and n2.right)):
			    return (dfs(n1.left, n2.left) and dfs(n1.right, n2.right)) or (dfs(n1.right, n2.left) and dfs(n1.left, n2.right))        
		    else:
			    return dfs(n1.right, n2.left) and dfs(n1.left, n2.right)
	    return dfs(root1, root2)
