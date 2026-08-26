class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        # Collect 0-based indices of all '1's
        ones = [i for i, ch in enumerate(s) if ch == '1']
        
        # If there are fewer than k ones, no valid substring exists
        if len(ones) < k:
            return ""
        
        min_len = float('inf')
        ans = ""
        
        # Check every contiguous window of k '1's
        for i in range(len(ones) - k + 1):
            start = ones[i]
            end = ones[i + k - 1]
            sub = s[start : end + 1]
            length = len(sub)
            
            if length < min_len:
                min_len = length
                ans = sub
            elif length == min_len:
                ans = min(ans, sub)
                
        return ans