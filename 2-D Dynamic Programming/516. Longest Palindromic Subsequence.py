class Solution:
    def longestCommonSubsequence(self, t1: str, t2: str) -> int:
        DP=[[0 for _ in range(len(t2))] for _ in range(len(t1))]
        for i in range(len(t1)):
            for j in range(len(t2)):
                if t1[i] == t2[j]:
                    if i == 0 or j == 0:
                        DP[i][j] = 1
                    else:
                        DP[i][j] = 1 + DP[i - 1][j - 1]
            
                else:
                    DP[i][j] = max(DP[i - 1][j], DP[i][j - 1])
        return DP[-1][-1]
    def longestPalindromeSubseq(self, s: str) -> int:
        return self.longestCommonSubsequence(s,s[::-1])
