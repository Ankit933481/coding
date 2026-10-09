class Solution:
    def minInsertions(self, s: str) -> int:
        needed_right = 0  # Tracks right parentheses needed
        missing_left = 0  # Tracks missing opening '('
        missing_right = 0 # Tracks missing closing ')'
        
        for c in s:
            if c == '(':
                # If needed_right is odd, we have an unmatched single ')' 
                # from a previous separation that needs a closing partner first.
                if needed_right % 2 == 1:
                    missing_right += 1
                    needed_right -= 1
                needed_right += 2
            else:
                needed_right -= 1
                # If needed_right drops below 0, we have an extra ')' 
                # without an opening '(', so we must insert a '('
                if needed_right < 0:
                    missing_left += 1
                    needed_right += 2  # The inserted '(' requires two ')'
                    
        return needed_right + missing_left + missing_right