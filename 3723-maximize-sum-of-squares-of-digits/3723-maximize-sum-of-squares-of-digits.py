class Solution:

  def maxSumOfSquares(self, num: int, sum: int) -> str:
    if sum < 1 or sum > 9 * num:
      return ""

    res = []
    for i in range(num):
      rem_slots = num - i
      # Greedily pick the largest possible digit for the current position
      d = min(9, sum)
      res.append(str(d))
      sum -= d

    return "".join(res)