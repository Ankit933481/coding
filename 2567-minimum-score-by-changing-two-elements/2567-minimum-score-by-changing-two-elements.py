class Solution:
    def minimizeSum(self, nums: list[int]) -> int:
        nums.sort()
        n = len(nums)

        return min(
            nums[n - 1] - nums[2],  # drop 2 smallest
            nums[n - 3] - nums[0],  # drop 2 largest
            nums[n - 2] - nums[1],  # drop 1 smallest and 1 largest
        )