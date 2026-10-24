class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        def to_days(date_str: str) -> int:
            month, day = map(int, date_str.split('-'))
            return sum(days_in_months[:month - 1]) + day
        
        alice_start = to_days(arriveAlice)
        alice_end = to_days(leaveAlice)
        bob_start = to_days(arriveBob)
        bob_end = to_days(leaveBob)
        
        overlap_start = max(alice_start, bob_start)
        overlap_end = min(alice_end, bob_end)
        
        return max(0, overlap_end - overlap_start + 1)