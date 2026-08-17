class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode], carry: int = 0) -> Optional[ListNode]:
        if not l1 and not l2 and not carry:
            return None
        
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        
        total = val1 + val2 + carry
        node = ListNode(total % 10)
        
        next_l1 = l1.next if l1 else None
        next_l2 = l2.next if l2 else None
        
        node.next = self.addTwoNumbers(next_l1, next_l2, total // 10)
        return node