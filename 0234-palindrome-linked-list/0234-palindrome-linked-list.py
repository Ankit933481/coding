# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        self.s=[]
        current=head
        while current:
            self.s.append(current.val)
            current=current.next
        current=head
        while current:
            if current.val !=self.s[-1]:
                return False
            self.s.pop()
            current=current.next
        return True