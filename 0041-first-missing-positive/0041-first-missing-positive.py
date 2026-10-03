class Solution:

  def firstMissingPositive(self, nums: list[int]) -> int:
    n = len(nums)

    # Step 1: Replace numbers <= 0 or > n with n + 1
    for i in range(n):
      if nums[i] <= 0 or nums[i] > n:
        nums[i] = n + 1

    # Step 2: Mark presence by negating the value at the corresponding index
    for i in range(n):
      val = abs(nums[i])
      if 1 <= val <= n:
        if nums[val - 1] > 0:
          nums[val - 1] = -nums[val - 1]

    # Step 3: Find the first index with a positive value
    for i in range(n):
      if nums[i] > 0:
        return i + 1

    # Step 4: If 1 to n are all present, return n + 1
    return n + 1