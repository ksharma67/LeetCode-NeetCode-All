class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if '0000' in deadends:
            return -1
        if '0000' == target:
            return 0
        
        queue = collections.deque()
        queue.append(('0000', 0))
        visited = set('0000')
        
        while queue:
            node, dist = queue.popleft()
            
            if node in deadends:
                continue
            if node == target:
                return dist
            
            for i in range(len(node)):
                num = int(node[i])
				# For wrap round we consider both forward and reverse directions.
                for dx in [-1, 1]:
                    nodeUpdated = node[:i] + str((num + dx) % 10) + node[i+1:]
                    if nodeUpdated not in visited:
                        queue.append((nodeUpdated, dist + 1))
                        visited.add(nodeUpdated)
        return -1
