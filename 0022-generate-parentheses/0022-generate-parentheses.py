class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []
        
        def backtrack(open_count, close_count, current):
            # If the current string has n open and n close brackets, it's a valid combination
            if open_count == close_count == n:
                res.append("".join(current))
                return
            
            # We can add an open parenthesis if we haven't reached the limit n
            if open_count < n:
                current.append("(")
                backtrack(open_count + 1, close_count, current)
                current.pop()
                
            # We can add a close parenthesis if there are more open parentheses than close ones
            if close_count < open_count:
                current.append(")")
                backtrack(open_count, close_count + 1, current)
                current.pop()
                
        backtrack(0, 0, [])
        return res