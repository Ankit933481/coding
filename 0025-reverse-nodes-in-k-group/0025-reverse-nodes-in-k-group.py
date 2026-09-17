# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        group_prev = dummy

        def get_kth(curr, step):
            while curr and step > 0:
                curr = curr.next
                step -= 1
            return curr

        while True:
            kth = get_kth(group_prev, k)
            if not kth:
                break
            group_next = kth.next

            # Reverse current k group
            prev, curr = kth.next, group_prev.next
            while curr != group_next:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            # Connect with previous group and advance group_prev
            tmp = group_prev.next
            group_prev.next = kth
            group_prev = tmp

        return dummy.next