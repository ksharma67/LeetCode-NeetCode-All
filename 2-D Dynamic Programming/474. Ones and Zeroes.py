class Solution:
    def findMaxForm(self, arr: List[str], m: int, n: int) -> int:
        
        @cache
		# cache used for the program to be executed faster
		# if not used may give time limit exceeded
		

        def solve(i,m,n):
            if m<0 or n<0:
                return -math.inf
            if (i>=len(arr)):
                return 0
            return max(solve(i+1,m,n), 1+solve(i+1,m-arr[i][0],n-arr[i][1]))

        for i in range(len(arr)):
            arr[i]=[arr[i].count("0"),arr[i].count("1")]

        return solve(0,m,n)
