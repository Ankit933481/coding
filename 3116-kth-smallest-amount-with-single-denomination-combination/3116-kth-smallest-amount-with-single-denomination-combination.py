import math
from typing import List


class Solution:

  def findKthSmallest(self, coins: List[int], k: int) -> int:
    n = len(coins)
    subsets = []

    # Precalculate (LCM, sign) for all 2^N - 1 non-empty subsets
    for mask in range(1, 1 << n):
      lcm_val = 1
      bits = 0
      for i in range(n):
        if (mask >> i) & 1:
          bits += 1
          lcm_val = math.lcm(lcm_val, coins[i])

      sign = 1 if bits % 2 == 1 else -1
      subsets.append((lcm_val, sign))

    # Helper function to count unique amounts <= x
    def count(x: int) -> int:
      return sum(sign * (x // lcm_val) for lcm_val, sign in subsets)

    # Binary search within range [1, min(coins) * k]
    left, right = 1, min(coins) * k
    ans = right

    while left <= right:
      mid = (left + right) // 2
      if count(mid) >= k:
        ans = mid
        right = mid - 1
      else:
        left = mid + 1

    return ans