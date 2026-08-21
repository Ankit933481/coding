import math
from typing import List


class Solution:

  def findKthSmallest(self, coins: List[int], k: int) -> int:
    coins.sort()
    filtered = []
    for c in coins:
      if not any(c % prev == 0 for prev in filtered):
        filtered.append(c)

    limit = filtered[0] * k
    pos_lcms = []
    neg_lcms = []
    n = len(filtered)

    # 2. DFS subset generation with LCM upper-bound pruning
    def dfs(idx: int, curr_lcm: int, count: int) -> None:
      if idx == n:
        if count > 0:
          if count % 2 == 1:
            pos_lcms.append(curr_lcm)
          else:
            neg_lcms.append(curr_lcm)
        return

      # Exclude current coin
      dfs(idx + 1, curr_lcm, count)

      # Include current coin (only if LCM stays within upper limit)
      next_lcm = math.lcm(curr_lcm, filtered[idx])
      if next_lcm <= limit:
        dfs(idx + 1, next_lcm, count + 1)

    dfs(0, 1, 0)

    # 3. Binary search with fast sum calculation
    left, right = filtered[0], limit
    ans = right

    while left <= right:
      mid = (left + right) // 2
      total = sum(mid // l for l in pos_lcms) - sum(mid // l for l in neg_lcms)

      if total >= k:
        ans = mid
        right = mid - 1
      else:
        left = mid + 1

    return ans