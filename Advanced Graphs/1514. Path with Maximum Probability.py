import heapq
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        adj=[[] for _ in range(n)]
        for i in range(len(edges)):
            adj[edges[i][0]].append((-1*succProb[i],edges[i][1]))
            adj[edges[i][1]].append((-1*succProb[i],edges[i][0]))
        dst=[0]*n
        st=[(-1,start)]
        heapq.heapify(st)
        dst[start]=-1
        while st:
            d,x=heapq.heappop(st)
            for dt,i in adj[x]:
                print(i,d,dt,dst[i])
                if -1*(d*dt)<dst[i]:
                    dst[i]=-1*(d*dt)
                    if i!=end:
                        heapq.heappush(st,(-1*(d*dt),i))
        return -1*dst[end]
