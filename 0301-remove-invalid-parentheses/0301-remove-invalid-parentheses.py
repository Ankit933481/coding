class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        def isValid(string):
            count = 0
            for char in string:
                if char == '(':
                    count += 1
                elif char == ')':
                    count -= 1
                    if count < 0:
                        return False
            return count == 0

        current_level = {s}
        
        while True:
            # Filter valid strings at the current level
            valid_strings = [curr for curr in current_level if isValid(curr)]
            if valid_strings:
                return valid_strings
            
            # Generate next level by removing one parenthesis at each position
            next_level = set()
            for curr in current_level:
                for i in range(len(curr)):
                    if curr[i] in ('(', ')'):
                        next_level.add(curr[:i] + curr[i+1:])
            current_level = next_level