class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        half = n // 2
        
        sum1 = sum(int(c) for c in num[:half] if c != '?')
        sum2 = sum(int(c) for c in num[half:] if c != '?')
        
        q1 = num[:half].count('?')
        q2 = num[half:].count('?')
        
        # Bob wins if and only if 2 * (sum1 - sum2) == 9 * (q2 - q1)
        return 2 * (sum1 - sum2) != 9 * (q2 - q1)