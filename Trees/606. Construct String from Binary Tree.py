# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Time Complexity: O(N) where N is the number of the nodes in the tree
# Space Complexity: O(H) where H is the height of the tree. 
# In worse case, H can be N when it is a left skewed binary tree / right skewed binary tree
class Solution:
    # case 1: root is nullptr -> ""
    # case 2: root doesn't have left sub tree and right sub tree -> root.val
    # case 3: root.left is not nullptr -> root.val + (dfs result from left sub tree)
    # case 4: root.left is nullptr but root.right is not nullptr -> root.val + () 
    # case 5: root.right is not nullptr -> root.val + (dfs result from right sub tree)
    def tree2str(self, root: Optional[TreeNode]) -> str:
        # handle case 1
        if root is None:
            return ''
        # we convert root.val to string here, then append results from different cases
        s = str(root.val)
        # handle case 2
        # this line is obviously not necessary
        if root.left is None and root.right is None:
            s += ''
        # handle case 3
        if root.left:
            s += '({})'.format(self.tree2str(root.left))
        # handle case 4
        # alternatively, you can use `elif root.right: s += '()'`
        if root.left is None and root.right:
            s += '()'
        # handle case 5
        if root.right:
            s += '({})'.format(self.tree2str(root.right))
        return s        
