class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        ans = ['.' for _ in range(len(dominoes))]

        queue = deque()
        for i, d in enumerate(dominoes):
            if d == 'L' or d == 'R':
                queue.append((i, d))
            ans[i] = d
        
        while queue:
            size = len(queue)
            collision = defaultdict(list)
            for _ in range(size):
                i, d = queue.popleft()
                if d == 'L' and i - 1 >= 0 and ans[i - 1] == '.':
                    collision[i - 1].append('L')
                elif d == 'R' and i + 1 < len(ans) and ans[i + 1] == '.':
                    collision[i + 1].append('R')
            for pos in collision:
                if len(collision[pos]) == 2:
                    ans[pos] = '.'
                else:
                    ans[pos] = collision[pos][0]
                    queue.append((pos, collision[pos][0]))
                
        return ''.join(ans)
