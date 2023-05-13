class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visit = set()

        def isValid(a,b):
            return 0<=a<n and 0<=b<m

        def dfs(i,j):
            if (i,j) in visit or not isValid(i,j) or not grid[i][j]:
                return
            visit.add((i,j))
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j-1)
            dfs(i,j+1)
            
        def bfs():
            level, queue = 0, collections.deque(visit)
            while queue:
                for _ in range(len(queue)):
                    x,y = queue.popleft()
                    for r, c in (x+1,y), (x,y+1), (x-1,y), (x,y-1):
                        if not isValid(r,c) or (r,c) in visit:
                            continue
                        if grid[r][c]:
                            return level
                        queue.append((r,c))
                        visit.add((r,c))

                level += 1

        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    dfs(i,j)
                    return bfs()
            

