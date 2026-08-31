# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if not head or not head.next or not head.next.next:
            return [-1, -1]
        
        first_idx = -1
        prev_idx = -1
        min_dist = float('inf')
        
        prev = head
        curr = head.next
        idx = 1
        
        while curr and curr.next:
            is_maxima = curr.val > prev.val and curr.val > curr.next.val
            is_minima = curr.val < prev.val and curr.val < curr.next.val
            
            if is_maxima or is_minima:
                if first_idx == -1:
                    first_idx = idx
                else:
                    min_dist = min(min_dist, idx - prev_idx)
                prev_idx = idx
            
            prev = curr
            curr = curr.next
            idx += 1
        
        if first_idx == -1 or first_idx == prev_idx:
            return [-1, -1]
        
        return [min_dist, prev_idx - first_idx]