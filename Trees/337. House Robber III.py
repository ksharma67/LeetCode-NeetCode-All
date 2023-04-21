# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        # Define the helper function
        def dfs(node):
            # Base case: if the node is None, return (0, 0)
            if not node:
                return (0, 0)
            
            # Recursive case: calculate the values for the left and right subtrees
            left_rob, left_not_rob = dfs(node.left)
            right_rob, right_not_rob = dfs(node.right)
            
            # Calculate the values for the current node
            rob_this = node.val + left_not_rob + right_not_rob
            not_rob_this = max(left_rob, left_not_rob) + max(right_rob, right_not_rob)
            
            # Return the values for the current node
            return (rob_this, not_rob_this)
        
        # Call the helper function on the root node and return the maximum value
        return max(dfs(root))
