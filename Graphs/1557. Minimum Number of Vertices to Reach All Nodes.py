class Solution:
    def dfs(self, vertex, first=False):
        if vertex in self.reachable:
            return
        if not first:
            self.reachable.add(vertex)
            first = False
        for _vertex in self.adj_matrix[vertex]:
            self.dfs(_vertex)

    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        self.adj_matrix = defaultdict(list)
        self.reachable = set()
        for edge in edges:
            self.adj_matrix[edge[0]].append(edge[1])
        
        all_nodes = set()
        for i in range(n):
            all_nodes.add(i)
            self.dfs(i, True)
        
        return list(all_nodes - self.reachable)
        
