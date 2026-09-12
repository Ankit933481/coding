from bisect import bisect_right
from typing import List

class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        # Store intervals with original index: (l, r, weight, original_index)
        arr = sorted([(l, r, w, i) for i, (l, r, w) in enumerate(intervals)])
        
        # Extract start times for binary search
        start_times = [item[0] for item in arr]
        
        # Precompute next non-overlapping interval index for each interval
        next_indices = [bisect_right(start_times, arr[i][1]) for i in range(n)]
        
        # dp[c][i] = (max_weight, best_tuple) using AT MOST c intervals from arr[i:]
        dp = [[(0, ())] * (n + 1) for _ in range(5)]
        
        for c in range(1, 5):
            for i in range(n - 1, -1, -1):
                # Option 1: Skip arr[i]
                best_w, best_tuple = dp[c][i + 1]
                
                # Option 2: Take arr[i]
                nxt = next_indices[i]
                prev_w, prev_tuple = dp[c - 1][nxt]
                cand_w = arr[i][2] + prev_w
                cand_tuple = tuple(sorted(prev_tuple + (arr[i][3],)))
                
                # Pick the choice with higher weight or lexicographically smaller sorted index tuple
                if cand_w > best_w or (cand_w == best_w and cand_tuple < best_tuple):
                    best_w, best_tuple = cand_w, cand_tuple
                
                dp[c][i] = (best_w, best_tuple)
                
        return list(dp[4][0][1])