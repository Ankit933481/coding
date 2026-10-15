class Solution:

  def sumCounts(self, nums: List[int]) -> int:
    ans = 0
    n = len(nums)
    for i in range(n):
      distinct_elements = set()
      for j in range(i, n):
        distinct_elements.add(nums[j])
        ans += len(distinct_elements) ** 2
    return ans