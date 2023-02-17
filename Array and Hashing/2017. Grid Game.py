class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:

        top_sum, top_counter, bottom_counter, mini = sum(grid[0]), 0, 0, float("inf")
       
        for i in range(len(grid[0])): 
            top_counter+= grid[0][i]
            mini = min(mini, max(top_sum-top_counter, bottom_counter))
            bottom_counter+=grid[1][i]

        return mini
