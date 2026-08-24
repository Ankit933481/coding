from itertools import accumulate
from typing import List


class Solution:

  def stoneGameVIII(self, stones: List[int]) -> int:
    # Compute prefix sums
    pref = list(accumulate(stones))

    # Base case: if forced to take all stones (last index n-1)
    dp = pref[-1]

    # Iterate backwards from index n - 2 down to index 1 (since x > 1)
    for i in range(len(stones) - 2, 0, -1):
      dp = max(dp, pref[i] - dp)

    return dp