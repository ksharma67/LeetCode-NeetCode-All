class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle:
            return 0

        for i in range(1,len(triangle)):
            l = len(triangle[i])
            for j in range(l):
                if j-1>=0 and j<l-1:
                    triangle[i][j] += min(triangle[i-1][j],triangle[i-1][j-1])
                elif j == l-1:
                    triangle[i][j] += triangle[i-1][j-1]
                else:
                    triangle[i][j] += triangle[i-1][j]

        return min(triangle[-1])
