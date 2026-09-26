class Solution:

  def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
    mapping = dict(knowledge)
    res, key_chars, in_bracket = [], [], False

    for char in s:
      if char == '(':
        in_bracket = True
        key_chars = []
      elif char == ')':
        in_bracket = False
        key = ''.join(key_chars)
        res.append(mapping.get(key, '?'))
      elif in_bracket:
        key_chars.append(char)
      else:
        res.append(char)

    return ''.join(res)