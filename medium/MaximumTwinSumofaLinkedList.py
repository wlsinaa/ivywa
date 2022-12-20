class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        re_ = self.reverseList(head)
        a = []
        while re_:
            a.append(head.val + re_.val)
            re_ = re_.next
            head = head.next
        return max(a)
    def reverseList(self, A: Optional[ListNode]) -> Optional[ListNode]:
        if A == None:
            return A
        if A.next == None:
            return A
        chain = None
        while A:
            new = ListNode(A.val)
            new.next = chain
            chain  = new
            A = A.next
        return chain