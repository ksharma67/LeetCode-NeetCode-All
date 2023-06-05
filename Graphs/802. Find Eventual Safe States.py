class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        def dfs(sv,visited,path):
            visited[sv]=1
            path[sv]=1
            for u in graph[sv]:
                if visited[u]==0:
                    if dfs(u,visited,path):
                        return True
                elif path[u]:
                    return True
            path[sv]=0
            return False
        n=len(graph)
        visited=[0]*n
        path=[0]*n
        a=[]
        for i in range(n):
            if visited[i]==0:
                dfs(i,visited,path)
        for i in range(n):
            if path[i]==0:
                a.append(i)
        return a
