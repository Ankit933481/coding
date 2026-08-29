from collections import deque

class Solution:
    def lexicographicallySmallestArray(self, nums: list[int], limit: int) -> list[int]:
        sorted_nums = sorted(nums)
        
        groups = []
        num_to_group = {}
        
        # Group adjacent sorted values if difference <= limit
        for num in sorted_nums:
            if not groups or num - groups[-1][-1] > limit:
                groups.append(deque())
            groups[-1].append(num)
            num_to_group[num] = len(groups) - 1
            
        # Place smallest available value for each index's component group
        res = []
        for num in nums:
            group_idx = num_to_group[num]
            res.append(groups[group_idx].popleft())
            
        return res