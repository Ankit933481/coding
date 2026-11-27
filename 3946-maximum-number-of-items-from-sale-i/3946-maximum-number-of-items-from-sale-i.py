from typing import List


class Solution:

  def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
    n = len(items)

    # bonus[i] = count of j != i such that items[j][0] % items[i][0] == 0
    bonus = [0] * n
    for i in range(n):
      fi = items[i][0]
      cnt = 0
      for j in range(n):
        if i != j and items[j][0] % fi == 0:
          cnt += 1
      bonus[i] = cnt

    dp = [0] * (budget + 1)

    for i in range(n):
      _, price = items[i]
      free_cnt = bonus[i]
      if price > budget:
        continue

      prev = dp[:]
      # best_chain[b] = max over k >= 1 of (prev[b - k * price] + k)
      best_chain = [0] * (budget + 1)

      for b in range(price, budget + 1):
        best_chain[b] = max(prev[b - price] + 1, best_chain[b - price] + 1)
        dp[b] = max(prev[b], best_chain[b] + free_cnt)

    return max(dp)