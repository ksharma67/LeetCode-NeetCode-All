class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        lq = len(questions)
        dp = [0] * (lq + 1)

        for i in range(len(questions) - 1, -1, -1):
            pt, bp = questions[i]

            nxt = i + bp + 1
            nxt = lq if nxt >= lq else nxt

            dp[i] = max(dp[i+1], pt + dp[nxt])
        return dp[0]
