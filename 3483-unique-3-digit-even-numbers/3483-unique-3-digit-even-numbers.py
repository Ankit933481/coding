class Solution:

  def totalNumbers(self, digits: list[int]) -> int:
    freq = [0] * 10
    for d in digits:
      freq[d] += 1

    ans = 0
    for num in range(100, 1000, 2):
      d1, d2, d3 = num // 100, (num // 10) % 10, num % 10

      freq[d1] -= 1
      freq[d2] -= 1
      freq[d3] -= 1

      if freq[d1] >= 0 and freq[d2] >= 0 and freq[d3] >= 0:
        ans += 1

      freq[d1] += 1
      freq[d2] += 1
      freq[d3] += 1

    return ans