class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7
        end_with = [0] * 26
        
        for char in s:
            idx = ord(char) - ord('a')
            # 1 (for sequence consisting of just `char`) + total existing distinct subsequences
            end_with[idx] = (sum(end_with) + 1) % MOD
            
        return sum(end_with) % MOD