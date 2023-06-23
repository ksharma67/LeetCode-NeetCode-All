class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        # Approach 1,   T.C =  O(max(N,K)) where K = length of str(k)
        
        data = 0
        for val in num:
            data = data*10+val

        data+=k
        res = []
        while data!=0:
            res.append(data%10)
            data//=10
        return res[::-1]
        

        # Approach 2,  T.C = O(max(N,K)) where K = length of str(k)
        
        n = len(num)
        for i in range(n-1,-1,-1):
            num[i],k = (num[i]+k)%10,(num[i]+k)//10
        if k!=0:
            return [int(val) for val in str(k)]+num
        return num
        
