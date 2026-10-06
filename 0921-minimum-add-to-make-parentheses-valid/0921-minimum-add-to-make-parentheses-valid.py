class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_count = 0
        ans = 0
        
        for char in s:
            if char == '(':
                open_count += 1
            else:
                if open_count > 0:
                    open_count -= 1
                else:
                    ans += 1
                    
        return ans + open_count