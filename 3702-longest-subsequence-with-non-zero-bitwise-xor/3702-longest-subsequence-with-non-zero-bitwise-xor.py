class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        n = len(nums)
        xor_all = 0
        for x in nums:
            xor_all ^= x
            
        # If the total XOR is non-zero, take the whole array
        if xor_all != 0:
            return n
            
        # If all elements are 0, no non-zero subsequence is possible
        if all(x == 0 for x in nums):
            return 0
            
        # Otherwise, exclude any one element to get a non-zero XOR
        return n - 1