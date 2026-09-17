class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        n = len(arr)
        inf = float('inf')
        
        best_end = [inf] * n
        min_len = inf
        ans = inf
        
        current_sum = 0
        left = 0
        
        for right in range(n):
            current_sum += arr[right]
            
            while current_sum > target and left <= right:
                current_sum -= arr[left]
                left += 1
                
            if current_sum == target:
                curr_len = right - left + 1
                if left > 0 and best_end[left - 1] != inf:
                    ans = min(ans, curr_len + best_end[left - 1])
                min_len = min(min_len, curr_len)
                
            best_end[right] = min(best_end[right - 1] if right > 0 else inf, min_len)
            
        return ans if ans != inf else -1