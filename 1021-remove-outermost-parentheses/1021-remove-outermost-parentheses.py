class Solution:

  def removeOuterParentheses(self, s: str) -> str:
    res = []
    opened = 0
    start = 0

    for i, char in enumerate(s):
      if char == "(":
        opened += 1
      else:
        opened -= 1

      # When a primitive decomposition block is complete
      if opened == 0:
        res.append(s[start + 1 : i])
        start = i + 1

    return "".join(res)