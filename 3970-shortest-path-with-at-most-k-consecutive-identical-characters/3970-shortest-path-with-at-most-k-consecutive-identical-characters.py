import heapq
from typing import List

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        graph = [[] for _ in range(n)]
        for u, v, w in edges:
            graph[u].append((v, w))
            
        dist = [[float('inf')] * (k + 1) for _ in range(n)]
        pq = []
        
        initial_count = 1
        dist[0][initial_count] = 0
        heapq.heappush(pq, (0, 0, initial_count))
        
        while pq:
            d, u, count = heapq.heappop(pq)
            
            if u == n - 1:
                return d
                
            if d > dist[u][count]:
                continue
                
            u_label = labels[u]
            for v, w in graph[u]:
                v_label = labels[v]
                nxt_count = count + 1 if u_label == v_label else 1
                
                if nxt_count <= k:
                    if d + w < dist[v][nxt_count]:
                        dist[v][nxt_count] = d + w
                        heapq.heappush(pq, (d + w, v, nxt_count))
                        
        return -1