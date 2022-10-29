class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        def mergeSort(arr, l, r):
            if l < r:
                m = l + (r-l)//2
                mergeSort(arr, l, m)
                mergeSort(arr, m+1, r)
                merge(arr, l, m, r)
        
        def merge(arr, l, m, r):
            ans = []
            i = l
            j = m+1
            while i <= m and j <= r:
                if int(arr[i]+arr[j]) > int(arr[j]+arr[i]):
                    ans.append(arr[i])
                    i += 1
                else:
                    ans.append(arr[j])
                    j += 1
            while i <= m:
                ans.append(arr[i])
                i+=1
            while j <= r:
                ans.append(arr[j])
                j+=1
            
            for i in range(len(ans)):
                arr[l+i] = ans[i]
        
        arr = [str(num) for num in nums]

        mergeSort(arr, 0, len(arr)-1)

        return "0" if arr and arr[0] == "0" else "".join(arr)
