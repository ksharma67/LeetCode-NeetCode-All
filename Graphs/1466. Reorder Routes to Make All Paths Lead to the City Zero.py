class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        def dfs(node: int, parent: int) -> int:
            return sum(cost + dfs(kid, node) for kid, cost in graph[node] if kid != parent)

        graph = defaultdict(list)
        for u, v in connections:
            graph[u].append((v, 1))
            graph[v].append((u, 0))

        return dfs(0, parent=-1)
