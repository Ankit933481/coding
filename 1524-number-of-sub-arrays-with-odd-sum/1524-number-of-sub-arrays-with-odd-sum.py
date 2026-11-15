class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        MOD = 10**9 + 7
        odd_count = 0
        even_count = 1  # Base case: prefix sum 0 is even
        current_sum = 0
        ans = 0
        
        for num in arr:
            current_sum += num
            
            if current_sum % 2 != 0:  # Current prefix sum is odd
                ans = (ans + even_count) % MOD
                odd_count += 1
            else:  # Current prefix sum is even
                ans = (ans + odd_count) % MOD
                even_count += 1
                
        return ans