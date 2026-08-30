class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        min_idx = nums.index(min(nums))
        max_idx = nums.index(max(nums))

        # Identify lower index (i) and higher index (j)
        i = min(min_idx, max_idx)
        j = max(min_idx, max_idx)

        # Three potential deletion strategies
        both_from_front = j + 1
        both_from_back = n - i
        from_both_sides = (i + 1) + (n - j)

        return min(both_from_front, both_from_back, from_both_sides)