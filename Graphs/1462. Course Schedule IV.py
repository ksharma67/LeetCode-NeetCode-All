class Solution:

    def dfs(self,s,t,graph,dp,vis):
        if(s==t):return True
        if(dp.get((s,t),-1)!=-1):return dp[(s,t)]
        if(vis[s]):return False
        vis[s]=1
        ans=False
        for i in graph[s]:
            ans=ans or self.dfs(i,t,graph,dp,vis)
            if(ans):break
        dp[(s,t)]=ans
        return ans

    def checkIfPrerequisite(self, n: int, pre: List[List[int]], q: List[List[int]]) -> List[bool]:
        graph=[[] for i in range(n)]
        indegree=[0 for i in range(n)]
        for l in pre:
            graph[l[0]].append(l[1])
        dp={}
        ans=[]
        for l in q:
            vis=[0 for i in range(n)]
            ans.append(self.dfs(l[0],l[1],graph,dp,vis))
        return ans

        
