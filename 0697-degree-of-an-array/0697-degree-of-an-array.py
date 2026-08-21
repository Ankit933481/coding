class Solution:

  def findShortestSubArray(self, nums: list[int]) -> int:
    
    counts = {}
    for num in nums:
      counts[num] = counts.get(num, 0) + 1

    degree = max(counts.values())

    left = 0
    window = {}
    min_len = len(nums)

    for right in range(len(nums)):
      val = nums[right]
      window[val] = window.get(val, 0) + 1

      while window[val] == degree:
        min_len = min(min_len, right - left + 1)
        window[nums[left]] -= 1
        left += 1

    return min_len