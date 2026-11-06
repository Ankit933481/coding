from typing import List

class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        # Sort logs by their timestamp
        logs.sort(key=lambda log: log[1])
        
        # Sort queries while preserving their original indices
        indexed_queries = sorted(enumerate(queries), key=lambda q: q[1])
        
        ans = [0] * len(queries)
        server_counts = {}
        
        left = 0
        right = 0
        m = len(logs)
        
        for orig_idx, q in indexed_queries:
            start_time = q - x
            end_time = q
            
            # Expand the right pointer to include logs up to end_time
            while right < m and logs[right][1] <= end_time:
                server_id = logs[right][0]
                server_counts[server_id] = server_counts.get(server_id, 0) + 1
                right += 1
            
            # Shrink from the left to remove logs falling out of the window (< start_time)
            while left < m and logs[left][1] < start_time:
                server_id = logs[left][0]
                server_counts[server_id] -= 1
                if server_counts[server_id] == 0:
                    del server_counts[server_id]
                left += 1
            
            # Zero-request servers = Total servers - Servers with at least one request
            ans[orig_idx] = n - len(server_counts)
            
        return ans