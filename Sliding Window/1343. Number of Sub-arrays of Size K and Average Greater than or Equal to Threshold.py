class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        s = sum(arr[0:k])
        threshold *= k
        ans = int(s >= threshold)
        for i in range(len(arr)-k):
            s += arr[i+k] - arr[i]
            if s >= threshold: ans = ans + 1
        return ans
