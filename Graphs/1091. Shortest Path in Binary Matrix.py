class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        N = len(grid)

        if grid[0][0] != 0 or grid[N-1][N-1] != 0:
            return -1 

        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        q = deque([(0,0)])
        grid[0][0] = 1 
        while q:  
            x,y = q.popleft()
            distance = grid[x][y]
            if (x,y) == (N-1,N-1): return distance
            for i,j in directions: 
                new_i = x + i 
                new_j = y + j 
                if (new_i >= 0 and new_i < N) and (new_j >= 0 and new_j < N) and grid[new_i][new_j] == 0:
                    grid[new_i][new_j] = distance + 1
                    q.append((new_i, new_j))
        
        return -1 
