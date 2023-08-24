class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])

        stack=[]
        for i in range(m):
            if grid[i][0]:
                stack.append((i,0))

            if grid[i][n-1]:
                stack.append((i,n-1))  

        for j in range(n):
            if grid[0][j]:
                stack.append((0,j))

            if grid[m-1][j]:
                stack.append((m-1,j))


        while stack:
            i,j=stack.pop()
            grid[i][j]=0
            for x,y in(i-1,j),(i,j-1),(i+1,j),(i,j+1):
                if 0<=x<m and 0<=y<n and grid[x][y]:
                    stack.append((x,y))

        return sum(map(sum,grid))            
