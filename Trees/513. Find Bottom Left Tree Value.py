# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        ans = 0
        q = deque() 
        q.append((root,0)) 
        while q:
            node,level = q.popleft() 
            ans = node.val
            if node.right:
                q.append((node.right,level+1)) 
            if node.left:
                q.append((node.left,level+1)) 
        return ans 

        # if root:
        #     if not root.left and not root.right:
        #         return root.val   
        # ans = [0] 
        # max = [0] 
        # def dfs(root , level):
        #     if not root:
        #         return; 
        #     if level>max[0]:
        #         max[0] = level 
        #         ans[0] = root.val
        #     dfs(root.left,level+1) 
        #     dfs(root.right,level+1) 
        # dfs(root,0) 
        # return ans[0]
