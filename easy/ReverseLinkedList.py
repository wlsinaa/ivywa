class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        if head.next == None:
            return head
        chain = None
        while head:
            new = ListNode(head.val)
            new.next = chain
            chain  = new
            head = head.next
        return chain