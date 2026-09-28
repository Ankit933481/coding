class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # nums.sort()
        # for i in range(1,len(nums)):
        #     if nums[i]==nums[i-1]:
        #         return True
        # return False
        seen=set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False