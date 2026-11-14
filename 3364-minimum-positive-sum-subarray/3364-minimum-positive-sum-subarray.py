class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        min_sum = float('inf')
        
        # Check all possible subarray lengths from l to r
        for length in range(l, r + 1):
            # Compute the sum of the first window of size 'length'
            current_sum = sum(nums[:length])
            if current_sum > 0:
                min_sum = min(min_sum, current_sum)
            
            # Slide the window across the rest of the array
            for i in range(length, n):
                current_sum += nums[i] - nums[i - length]
                if current_sum > 0:
                    min_sum = min(min_sum, current_sum)
                    
        return min_sum if min_sum != float('inf') else -1