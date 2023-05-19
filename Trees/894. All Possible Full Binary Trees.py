# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        cache = {
            1: [TreeNode(0)]
        }
        def rec(n, cache):
            res = []
            if n % 2 == 0:
                return []
            if n in cache:
                return cache[n]
            for i in range(1, n, 2):
                for left in rec(i, cache):
                    j = n-1-i
                    for right in rec(j, cache):

                        root = TreeNode(0)
                        root.left = left
                        root.right = right
                        res.append(root)

            cache[n] = res
            return res

        return rec(n, cache)  
