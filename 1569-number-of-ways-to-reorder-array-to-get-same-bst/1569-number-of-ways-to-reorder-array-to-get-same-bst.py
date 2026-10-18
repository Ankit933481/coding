import sys
from math import comb

sys.setrecursionlimit(2000)


class Solution:

  def numOfWays(self, nums: List[int]) -> int:
    MOD = 10**9 + 7

    def get_ways(arr):
      if len(arr) <= 2:
        return 1

      root = arr[0]
      left = [x for x in arr if x < root]
      right = [x for x in arr if x > root]

      # Choose positions for the left subtree elements among (left + right) total spots
      ways_comb = comb(len(left) + len(right), len(left))

      return (ways_comb * get_ways(left) * get_ways(right)) % MOD

    # Subtract 1 to exclude the original array ordering itself
    return (get_ways(nums) - 1) % MOD