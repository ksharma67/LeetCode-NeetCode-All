class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        heap = []
        m = len(dist)
        for i in range(m):
            heappush(heap, dist[i] / speed[i])
        ans, totalTime = 0, 0
        while heap:
            time = heappop(heap)
            time -= totalTime
            if time > 0:
                ans += 1
            else:
                break
            totalTime += 1
        return ans
