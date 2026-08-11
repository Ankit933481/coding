class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        s=sorted(nums)
        a=nums[0]
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                a+=nums[i]
            else:
                break
        num_set = set(nums)
        while a in num_set:
            a += 1

        return a