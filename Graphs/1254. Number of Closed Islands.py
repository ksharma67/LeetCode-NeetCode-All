class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        vis=defaultdict(lambda:False)
        n=len(grid)
        m=len(grid[0])
        '''
        '''
        def dfs(x,y):
            vis[(x,y)]=True
            isedge=True
            for i,j in ((x+1,y),(x-1,y),(x,y+1),(x,y-1)):
                if 0<=i<n and 0<=j<m:
                    if not vis[(i,j)] and (not grid[i][j]):
                        isedge=(dfs(i,j) and isedge)
                else:
                    isedge=(False and isedge)
            return isedge
        res=0
        for i in range(n):
            for j in range(m):
                if not vis[(i,j)] and (not grid[i][j]):
                    if dfs(i,j):
                        res+=1
                    # print(vis)
        return res
