class Solution:
    def resultArray(self, nums: list[int], k: int) -> list[int]:
        ans = [0] * k
        dp = [0] * k
        
        for num in nums:
            new_dp = [0] * k
            num_mod = num % k
            
            # Start a new subarray with just the current number
            new_dp[num_mod] = 1
            
            # Extend all previous subarrays ending at the previous index
            for i in range(k):
                new_mod = (i * num_mod) % k
                new_dp[new_mod] += dp[i]
                
            # Accumulate counts into the final answer
            for i in range(k):
                ans[i] += new_dp[i]
                
            dp = new_dp
            
        return ans