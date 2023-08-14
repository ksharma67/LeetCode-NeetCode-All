class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        edges = {0: defaultdict(list), 1: defaultdict(list)}
        
        for src,dest in redEdges:
            edges[0][src].append(dest)
        
        for src,dest in blueEdges:
            edges[1][src].append(dest)
            
            
        queue,result1, result2 = [(0,0,0),(0,1,0)], [float("inf")]*n, [float("inf")]*n
        
        result1[0], result2[0] = 0, 0
        while queue:
            node, direction, distance = queue.pop(0)
            for neighbour in edges[direction][node]:
                if direction and result2[neighbour] > distance + 1:
                    result2[neighbour] = 1 + distance
                    queue.append((neighbour, 1 - direction, 1 + distance))
                elif not direction and result1[neighbour] > distance + 1:
                    result1[neighbour] = 1 + distance
                    queue.append((neighbour, 1 - direction, 1 + distance))
                    
                        
            
            
        for i in range(n):
            result1[i] = min(result1[i], result2[i])
            if result1[i] == float("inf"):
                result1[i] = -1
        
        return result1
