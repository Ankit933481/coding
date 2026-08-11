class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        c=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[c],nums[i]=nums[i],nums[c]
                c+=1

        