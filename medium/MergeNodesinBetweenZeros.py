# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        out = cur = ListNode(0)
        while head:
            if head.val == 0 and cur.val != 0:
                new = ListNode(0)
                cur.next = new
                cur = cur.next
            else:
                cur.val += head.val
            head = head.next
        out = self.removeLastNode(out)
        return out
        
    def removeLastNode(self,A):
        if A == None:
            return None
        if A.next == None: # remove the first element
            A = None
            return None
        second_last = A
        while(second_last.next.next):
            second_last = second_last.next
        second_last.next = None
        return A
