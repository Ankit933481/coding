class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        # Find the overlapping requirement that needs both type 1 and type 2
        common = min(need1, need2)
        
        # Remaining needs after satisfying the common requirement
        rem1 = need1 - common
        rem2 = need2 - common
        
        # Cost for the overlapping part
        total_cost = common * min(costBoth, cost1 + cost2)
        
        # Cost for any leftover type 1 requirements
        total_cost += rem1 * min(cost1, costBoth)
        
        # Cost for any leftover type 2 requirements
        total_cost += rem2 * min(cost2, costBoth)
        
        return total_cost