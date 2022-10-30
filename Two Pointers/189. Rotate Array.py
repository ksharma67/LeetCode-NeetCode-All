class Solution:
    def reverse(self,arr,start,end):
         while start<end:
            arr[start],arr[end] = arr[end],arr[start] 
            end-=1 
            start+=1 
      
    def rotate(self,arr,k):
        n = len(arr)
        if  k==n: return 
    
        if k>n:
            k=k%n 
    
        self.reverse(arr,(n)-k,n-1)
        self.reverse(arr,0,(n)-k-1)
        self.reverse(arr,0,n-1)
