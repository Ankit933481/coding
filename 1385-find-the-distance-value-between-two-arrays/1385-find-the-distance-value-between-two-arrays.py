import bisect


class Solution:

  def findTheDistanceValue(
      self, arr1: List[int], arr2: List[int], d: int
  ) -> int:
    arr2.sort()
    count = 0

    for x in arr1:
      # Find the insertion point to maintain sorted order
      idx = bisect.bisect_left(arr2, x)
      valid = True

      # Check the element at or after idx
      if idx < len(arr2) and abs(arr2[idx] - x) <= d:
        valid = False
      # Check the element just before idx
      if idx > 0 and abs(arr2[idx - 1] - x) <= d:
        valid = False

      if valid:
        count += 1

    return count