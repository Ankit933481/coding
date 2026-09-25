class Solution:

  def braceExpansionII(self, expression: str) -> list[str]:
    def dfs(s: str) -> set[str]:
      i = s.find('}')
      if i == -1:
        return set(s.split(','))

      j = s.rfind('{', 0, i)
      left, mid, right = s[:j], s[j + 1 : i], s[i + 1 :]

      res = set()
      for word in mid.split(','):
        res.update(dfs(left + word + right))
      return res

    return sorted(list(dfs(expression)))