class Node:
    has_apple: bool
    neighbours: List['Node']

    def __init__(self, has_apple: bool):
        self.has_apple = has_apple
        self.neighbours = []

    def count_edges_leading_to_apples(self, from_node: Optional['Node'] = None) -> int:
        return sum(
            (subtree_count + 1) if subtree_count != 0 or child.has_apple else 0
            for child, subtree_count in ((n, n.count_edges_leading_to_apples(self))
                                         for n in self.neighbours if n is not from_node)
        )


class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        # Create a tree of bi-directionally connected Nodes:
        nodes = [Node(ha) for ha in hasApple]
        for a, b in edges:
            na, nb = nodes[a], nodes[b]
            na.neighbours.append(nb)
            nb.neighbours.append(na)

        # Calculate the count of edges from the root, x by 2 for "coming back"
        return nodes[0].count_edges_leading_to_apples() * 2
