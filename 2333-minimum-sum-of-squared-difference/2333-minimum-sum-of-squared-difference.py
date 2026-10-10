class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        # Calculate absolute differences for each pair
        diff = [abs(a - b) for a, b in zip(nums1, nums2)]
        total_k = k1 + k2
        
        # If total operations can reduce all differences to 0
        if sum(diff) <= total_k:
            return 0
            
        # Count frequencies of each difference value
        max_val = max(diff)
        count = [0] * (max_val + 1)
        for d in diff:
            count[d] += 1
            
        # Greedily reduce the largest differences
        for d in range(max_val, 0, -1):
            if count[d] > 0:
                # Determine how many elements of difference `d` we can reduce to `d - 1`
                take = min(total_k, count[d])
                count[d] -= take
                count[d - 1] += take
                total_k -= take
                
                if total_k == 0:
                    break
                    
        # Calculate the final minimum sum of squared difference
        ans = 0
        for d in range(len(count)):
            ans += count[d] * d * d
            
        return ans