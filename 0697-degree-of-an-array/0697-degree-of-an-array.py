from collections import Counter
from typing import List


class Solution:

  def findShortestSubArray(self, nums: List[int]) -> int:
    # Step 1: Compute the degree of the array
    degree = max(Counter(nums).values())

    # Step 2: Sliding Window with Two Pointers
    left = 0
    window_count = Counter()
    min_len = len(nums)

    for right in range(len(nums)):
      window_count[nums[right]] += 1

      # Shrink window from the left while the current right element maintains the degree
      while window_count[nums[right]] == degree:
        min_len = min(min_len, right - left + 1)
        window_count[nums[left]] -= 1
        left += 1

    return min_len