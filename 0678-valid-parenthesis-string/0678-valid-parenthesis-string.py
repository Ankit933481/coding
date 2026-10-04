class Solution:
    def checkValidString(self, s: str) -> bool:
        cmin = 0
        cmax = 0
        
        for char in s:
            if char == '(':
                cmin += 1
                cmax += 1
            elif char == ')':
                cmin = max(0, cmin - 1)
                cmax -= 1
            else:  # char == '*'
                cmin = max(0, cmin - 1)
                cmax += 1
            
            if cmax < 0:
                return False
                
        return cmin == 0