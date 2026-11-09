from sortedcontainers import SortedList
import heapq

class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        busy = []  # Min-heap storing (free_time, server_id)
        available = SortedList(range(k))  # Sorted list of currently available servers
        count = [0] * k  # Request count for each server
        
        for i, (arr, ld) in enumerate(zip(arrival, load)):
            # 1. Free up servers whose tasks have finished by time `arr`
            while busy and busy[0][0] <= arr:
                _, s_id = heapq.heappop(busy)
                available.add(s_id)
            
            # 2. If no servers are available, drop the request
            if not available:
                continue
            
            # 3. Find the first available server >= (i % k)
            target = i % k
            idx = available.bisect_left(target)
            if idx == len(available):
                idx = 0  # Wrap around to the beginning
            
            server_id = available[idx]
            available.pop(idx)
            
            # 4. Assign the request to the chosen server
            count[server_id] += 1
            heapq.heappush(busy, (arr + ld, server_id))
        
        # 5. Find all busiest servers
        max_handled = max(count)
        return [i for i, c in enumerate(count) if c == max_handled]