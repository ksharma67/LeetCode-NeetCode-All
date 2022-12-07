class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        import heapq
        heap = []
        for num in nums:
            heapq.heappush(heap, -1*int(num))
            
        for _ in range(k):
            v = heapq.heappop(heap)
            
        return str(-1*v)
