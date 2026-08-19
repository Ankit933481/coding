from collections import defaultdict
from typing import List

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        # Group reserved seats by row using a bitmask for seats 2 through 9
        occupied = defaultdict(int)
        for row, seat in reservedSeats:
            if 2 <= seat <= 9:
                occupied[row] |= (1 << (seat - 2))
        
        # Each row can seat at most 2 four-person groups
        ans = n * 2
        
        # Bitmasks for the 3 candidate 4-seat blocks (seats 2-5, 4-7, 6-9)
        LEFT = 0b00001111   # seats 2, 3, 4, 5
        MIDDLE = 0b00111100 # seats 4, 5, 6, 7
        RIGHT = 0b11110000  # seats 6, 7, 8, 9
        
        for mask in occupied.values():
            left_free = (mask & LEFT) == 0
            right_free = (mask & RIGHT) == 0
            middle_free = (mask & MIDDLE) == 0
            
            if left_free and right_free:
                # Can accommodate 2 groups; no reduction needed
                continue
            elif left_free or right_free or middle_free:
                # Can accommodate 1 group
                ans -= 1
            else:
                # Can accommodate 0 groups
                ans -= 2
                
        return ans