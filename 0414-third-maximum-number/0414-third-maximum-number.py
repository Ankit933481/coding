class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        a=set(nums)
        list(a)
        s=sorted(a)
        n=len(s)
        if n<3:
            return s[n-1]
        else:
            return s[n-3]