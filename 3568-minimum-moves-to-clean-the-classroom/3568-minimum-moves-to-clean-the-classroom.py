class Solution:
    def minMoves(self, classroom: list[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])
        
        start_r, start_c = -1, -1
        litter_map = {}
        litter_count = 0
        
        for r in range(m):
            for c in range(n):
                if classroom[r][c] == 'S':
                    start_r, start_c = r, c
                elif classroom[r][c] == 'L':
                    litter_map[(r, c)] = litter_count
                    litter_count += 1
                    
        target_mask = (1 << litter_count) - 1
        if target_mask == 0:
            return 0
            
        bestEnergy = [[[-1] * (1 << litter_count) for _ in range(n)] for _ in range(m)]
        
        # Plain list used as a FIFO queue via pointer index
        queue = [(start_r, start_c, 0, energy, 0)]
        bestEnergy[start_r][start_c][0] = energy
        
        head = 0
        while head < len(queue):
            r, c, mask, e, steps = queue[head]
            head += 1
            
            if mask == target_mask:
                return steps
                
            for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < m and 0 <= nc < n and classroom[nr][nc] != 'X':
                    next_e = e - 1
                    if next_e < 0:
                        continue
                        
                    cell = classroom[nr][nc]
                    next_mask = mask
                    
                    if cell == 'L':
                        next_mask = mask | (1 << litter_map[(nr, nc)])
                    elif cell == 'R':
                        next_e = energy
                        
                    if next_e > bestEnergy[nr][nc][next_mask]:
                        bestEnergy[nr][nc][next_mask] = next_e
                        queue.append((nr, nc, next_mask, next_e, steps + 1))
                        
        return -1