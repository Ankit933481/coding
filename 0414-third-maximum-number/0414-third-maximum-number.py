class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        s = sorted(set(nums))
        return s[-3] if len(s) >= 3 else s[-1]