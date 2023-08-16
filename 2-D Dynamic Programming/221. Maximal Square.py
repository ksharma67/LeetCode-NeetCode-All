class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        dp=[[0]*(len(matrix[0])+1)]
        for i in matrix:
            l=[0]
            for j in i:l.append(int(j))
            dp.append(l)
        mx=0
        for i in range(len(dp)):
            for j in range(len(dp[0])):
                if dp[i][j]==1:
                    dp[i][j]=min(dp[i-1][j],dp[i-1][j-1],dp[i][j-1])+1
                mx=max(mx,dp[i][j])
        return mx*mx
