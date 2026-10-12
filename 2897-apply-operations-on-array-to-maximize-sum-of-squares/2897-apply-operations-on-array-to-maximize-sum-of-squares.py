class Solution:
    def maxSum(self, nums: list[int], k: int) -> int:
        MOD = 10**9 + 7
        
        # Count the frequency of each bit across all numbers
        cnt = [sum((x >> b) & 1 for x in nums) for b in range(30)]
        
        total = 0
        # Greedily construct the top k largest numbers
        for i in range(k):
            val = 0
            for b in range(30):
                if cnt[b] > i:
                    val |= (1 << b)
            total = (total + val * val) % MOD
            
        return total